# Copyright 2017-2019 Lenovo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""from Matthew Garret's 'firmware_config' project.

This contains functions to manage the firmware configuration of Lenovo servers
"""

import ast
import random
import struct

import six

import pyghmi.exceptions as pygexc
from pyghmi.ipmi.oem.lenovo import EfiDecompressor

try:
    import EfiCompressor
    from lxml import etree
except ImportError:
    etree = None
    EfiCompressor = None

IMM_NETFN = 0x2e
IMM_COMMAND = 0x90
LENOVO_ENTERPRISE = [0x4d, 0x4f, 0x00]

OPEN_RO_COMMAND = [0x01, 0x05, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10]
OPEN_WO_COMMAND = [0x01, 0x03, 0x01]
READ_COMMAND = [0x02]
WRITE_COMMAND = [0x03]
CLOSE_COMMAND = [0x05]
SIZE_COMMAND = [0x06]


def run_command_with_retry(connection, data):
    tries = 10
    while tries:
        tries -= 1
        try:
            return connection.xraw_command(
                netfn=IMM_NETFN, command=IMM_COMMAND, data=data)
        except pygexc.IpmiException as e:
            if e.ipmicode != 0xa or not tries:
                raise
            connection.ipmi_session.pause(1)


def _convert_syntax(raw):
    return raw.replace('!', 'not').replace('||', 'or').replace(
        '&&', 'and').replace('-', '_')


class _ExpEngine(object):
    def __init__(self, cfg, setting):
        self.cfg = cfg
        self.setting = setting
        self.relatedsettings = set([])

    def lookup(self, category, setting):
        for optkey in self.cfg:
            opt = self.cfg[optkey]
            lid = opt['lenovo_id'].replace('-', '_')
            if (lid == category
                    and opt['lenovo_setting'] == setting):
                self.relatedsettings.add(optkey)
                return opt['lenovo_value']
        return None

    def process(self, parsed):
        if isinstance(parsed, ast.UnaryOp) and isinstance(parsed.op, ast.Not):
            return not self.process(parsed.operand)
        if isinstance(parsed, ast.Compare):
            if isinstance(parsed.ops[0], ast.NotEq):
                return self.process(parsed.left) != self.process(
                    parsed.comparators[0])
            elif isinstance(parsed.ops[0], ast.Eq):
                return self.process(parsed.left) == self.process(
                    parsed.comparators[0])
        if isinstance(parsed, ast.Num):
            return parsed.n
        if isinstance(parsed, ast.Attribute):
            category = parsed.value.id
            setting = parsed.attr
            return self.lookup(category, setting)
        if isinstance(parsed, ast.Name):
            if parsed.id == 'true':
                return True
            elif parsed.id == 'false':
                return False
            else:
                category = self.setting['lenovo_id']
                setting = parsed.id
                return self.lookup(category, setting)
        if isinstance(parsed, ast.BoolOp):
            if isinstance(parsed.op, ast.Or):
                return self.process(parsed.values[0]) or self.process(
                    parsed.values[1])
            elif isinstance(parsed.op, ast.And):
                return self.process(parsed.values[0]) and self.process(
                    parsed.values[1])


def _eval_conditional(expression, cfg, setting):
    if not expression:
        return False, ()
    try:
        parsed = ast.parse(expression)
        parsed = parsed.body[0].value
        evaluator = _ExpEngine(cfg, setting)
        result = evaluator.process(parsed)
        return result, evaluator.relatedsettings
    except SyntaxError:
        return False, ()


class LenovoFirmwareConfig(object):
    def __init__(self, ipmicmd):
        if not etree:
            raise Exception("python-lxml and python-eficompressor required "
                            "for this function")
        self.connection = ipmicmd

    def imm_size(self, filename):
        data = bytearray()
        data.extend(LENOVO_ENTERPRISE)
        data.extend(SIZE_COMMAND)
        if not isinstance(filename, bytes):
            filename = filename.encode('utf-8')
        data.extend(filename)

        response = run_command_with_retry(self.connection, data=data)

        size = response['data'][3:7]

        size = struct.unpack("i", size)
        return size[0]

    def imm_open(self, filename, write=False, size=None):
        response = None
        retries = 12
        data = bytearray()
        data.extend(LENOVO_ENTERPRISE)
        if write is False:
            data.extend(OPEN_RO_COMMAND)
        else:
            assert size is not None
            data.extend(OPEN_WO_COMMAND)
            hex_size = struct.pack("<I", size)
            data.extend(bytearray(hex_size[:4]))
            data.extend([0x01, 0x10])
        if not isinstance(filename, bytes):
            filename = filename.encode('utf-8')
        data.extend(filename)
        while len(data) < 38:
            data.append(0)

        while retries:
            retries = retries - 1
            response = run_command_with_retry(self.connection, data=data)
            try:
                if response['code'] == 0 or retries == 0:
                    break
            except KeyError:
                pass
            self.connection.ipmi_session.pause(5)
        filehandle = response['data'][3:7]
        filehandle = struct.unpack("<I", filehandle)[0]
        return filehandle

    def imm_close(self, filehandle):
        data = []
        data += LENOVO_ENTERPRISE
        data += CLOSE_COMMAND

        hex_filehandle = struct.pack("<I", filehandle)
        data.extend(bytearray(hex_filehandle[:4]))
        run_command_with_retry(self.connection, data=data)

    def imm_write(self, filehandle, size, inputdata):
        blocksize = 0xc8
        offset = 0
        remaining = size

        hex_filehandle = struct.pack("<I", filehandle)

        while remaining > 0:
            data = bytearray()
            data.extend(LENOVO_ENTERPRISE)
            data.extend(WRITE_COMMAND)
            data.extend(hex_filehandle[:4])
            hex_offset = struct.pack("<I", offset)
            data.extend(hex_offset[:4])
            if remaining < blocksize:
                amount = remaining
            else:
                amount = blocksize
            data.extend(inputdata[offset:offset + amount])
            remaining -= blocksize
            offset += blocksize
            run_command_with_retry(self.connection, data=data)

    def imm_read(self, filehandle, size):
        blocksize = 0xc8
        offset = 0
        output = b''
        remaining = size

        hex_filehandle = struct.pack("<I", filehandle)
        hex_blocksize = struct.pack("<H", blocksize)

        while remaining > 0:
            data = []
            data += LENOVO_ENTERPRISE
            data += READ_COMMAND
            data.extend(bytearray(hex_filehandle[:4]))
            hex_offset = struct.pack("<I", offset)
            data.extend(bytearray(hex_offset[:4]))
            if remaining < blocksize:
                hex_blocksize = struct.pack("<H", remaining)
            data.extend(hex_blocksize[:2])
            remaining -= blocksize
            offset += blocksize

            response = run_command_with_retry(self.connection, data=data)
            output += response['data'][5:]

        return output

    def factory_reset(self):
        options = self.get_fw_options()
        for option in options:
            if options[option]['is_list']:
                options[option]['new_value'] = [options[option]['default']]
            else:
                options[option]['new_value'] = options[option]['default']
        self.set_fw_options(options)

    def get_fw_options(self, fetchimm=True):
        if fetchimm:
            cfgfilename = "config.efi"
        else:
            cfgfilename = "config"
        options = {}
        data = None
        for _ in range(0, 30):
            filehandle = self.imm_open(cfgfilename)
            size = self.imm_size(cfgfilename)
            data = self.imm_read(filehandle, size)
            self.imm_close(filehandle)
            data = EfiDecompressor.decompress(data)
            if len(data) != 0:
                break
            self.connection.ipmi_session.pause(2)
        if not data:
            raise Exception("BMC failed to return configuration information")
        xml = etree.fromstring(data)
        sortid = 0
        for config in xml.iter("config"):
            lenovo_id = config.get("ID")
            if lenovo_id == 'iSCSI':
                # Do not support iSCSI at this time
                continue
            cfglabel = config.find('mriName')
            cfglabel = lenovo_id if cfglabel is None else cfglabel.text
            if lenovo_id == 'SYSTEM_PROD_DATA':
                theiter = [config]
            else:
                theiter = config.iter('group')
            for group in theiter:
                if lenovo_id == 'SYSTEM_PROD_DATA':
                    lenovo_group = None
                else:
                    lenovo_group = group.get("ID")
                for setting in group.iter("setting"):
                    forceinstance = False
                    is_list = False
                    lenovo_setting = setting.get("ID")
                    protect = True if setting.get("protected") == 'true' \
                        else False
                    hide = setting.get('suppress-if')
                    if hide:
                        hide = _convert_syntax(hide)
                    readonly = setting.get('gray-if')
                    if readonly:
                        readonly = _convert_syntax(readonly)
                    possible = []
                    current = None
                    default = None
                    reset = False
                    name = setting.find("mriName").text
                    help = setting.find("desc").text
                    onedata = setting.find('text_data')
                    if onedata is not None:
                        if onedata.get('password') == 'true':
                            protect = True
                    enumdata = setting.find('enumerate_data')
                    if enumdata is not None:
                        if enumdata.get('maxinstance') is not None:
                            forceinstance = True
                    if onedata is None:
                        onedata = setting.find('numeric_data')
                    if onedata is not None:
                        if onedata.get('maxinstance') is not None:
                            forceinstance = True
                        instances = list(onedata.iter('instance'))
                        if not instances:
                            protect = True  # not supported yet
                        else:
                            current = [x.text for x in instances]
                        default = onedata.get('default', None)
                        if default == '':
                            default = None
                    if (setting.find('cmd_data') is not None
                            or setting.find('boolean_data') is not None):
                        protect = True  # Hide currently unsupported settings
                    ldata = setting.find("list_data")
                    extraorder = False
                    currentdict = {}
                    currentdef = {}
                    if ldata is not None:
                        is_list = True
                        current = []
                        extraorder = ldata.get('ordered') == 'true'
                    lenovo_value = None
                    instancetochoicemap = {}
                    for choice in setting.iter("choice"):
                        label = choice.find("label").text
                        possible.append(label)
                        for instance in choice.iter("instance"):
                            if is_list:
                                if not extraorder:
                                    current.append(label)
                                else:
                                    currentdict[
                                        int(instance.get("order"))] = label
                            else:
                                currid = instance.get('ID')
                                if currid:
                                    instancetochoicemap[currid] = label
                                else:
                                    current = label
                                try:
                                    lenovo_value = int(
                                        choice.find('value').text)
                                except ValueError:
                                    lenovo_value = choice.find('value').text
                        hasdefault = choice.get('default')
                        if hasdefault == "true":
                            default = label
                        elif hasdefault is not None:
                            try:
                                a = int(hasdefault)
                                currentdef[a] = label
                            except ValueError:
                                pass
                        if choice.get("reset-required") == "true":
                            reset = True
                    if len(currentdict) > 0:
                        for order in sorted(currentdict):
                            current.append(currentdict[order])
                    if len(currentdef) > 0:
                        default = []
                        for order in sorted(currentdef):
                            default.append(currentdef[order])
                    optionname = "%s.%s" % (cfglabel, name)
                    alias = "%s.%s" % (lenovo_id, name)
                    if onedata is not None:
                        if current and len(current) > 1:
                            instidx = 1
                            for inst in current:
                                optname = '{0}.{1}'.format(optionname, instidx)
                                options[optname] = dict(
                                    current=inst,
                                    default=default,
                                    possible=possible,
                                    pending=None,
                                    new_value=None,
                                    help=help,
                                    is_list=is_list,
                                    lenovo_value=lenovo_value,
                                    lenovo_id=lenovo_id,
                                    lenovo_group=lenovo_group,
                                    lenovo_setting=lenovo_setting,
                                    lenovo_reboot=reset,
                                    lenovo_protect=protect,
                                    lenovo_instance=instidx,
                                    readonly_expression=readonly,
                                    hide_expression=hide,
                                    sortid=sortid,
                                    alias=alias)
                                sortid += 1
                                instidx += 1
                            continue
                        if current:
                            current = current[0]
                    if instancetochoicemap:
                        for currid in sorted(instancetochoicemap):
                            optname = '{0}.{1}'.format(optionname, currid)
                            current = instancetochoicemap[currid]
                            options[optname] = dict(
                                current=current,
                                default=default,
                                possible=possible,
                                pending=None,
                                new_value=None,
                                help=help,
                                is_list=is_list,
                                lenovo_value=lenovo_value,
                                lenovo_id=lenovo_id,
                                lenovo_group=lenovo_group,
                                lenovo_setting=lenovo_setting,
                                lenovo_reboot=reset,
                                lenovo_protect=protect,
                                lenovo_instance=currid,
                                readonly_expression=readonly,
                                hide_expression=hide,
                                sortid=sortid,
                                alias=alias)
                            sortid += 1
                        continue
                    lenovoinstance = ""
                    if forceinstance:
                        optionname = '{0}.{1}'.format(optionname, 1)
                        lenovoinstance = 1
                    options[optionname] = dict(current=current,
                                               default=default,
                                               possible=possible,
                                               pending=None,
                                               new_value=None,
                                               help=help,
                                               is_list=is_list,
                                               lenovo_value=lenovo_value,
                                               lenovo_id=lenovo_id,
                                               lenovo_group=lenovo_group,
                                               lenovo_setting=lenovo_setting,
                                               lenovo_reboot=reset,
                                               lenovo_protect=protect,
                                               lenovo_instance=lenovoinstance,
                                               readonly_expression=readonly,
                                               hide_expression=hide,
                                               sortid=sortid,
                                               alias=alias)
                    sortid = sortid + 1
        for opt in options:
            opt = options[opt]
            opt['hidden'], opt['hidden_why'] = _eval_conditional(
                opt['hide_expression'], options, opt)
            opt['readonly'], opt['readonly_why'] = _eval_conditional(
                opt['readonly_expression'], options, opt)

        return options

    def set_fw_options(self, options):
        changes = False
        random.seed()
        ident = 'ASU-%x-%x-%x-0' % (random.getrandbits(48),
                                    random.getrandbits(32),
                                    random.getrandbits(64))

        configurations = etree.Element('configurations', ID=ident,
                                       type='update', update='ASU Client')

        for option in options.keys():
            if options[option]['new_value'] is None:
                continue
            if options[option]['current'] == options[option]['new_value']:
                continue
            if options[option]['pending'] == options[option]['new_value']:
                continue
            if options[option]['readonly']:
                errstr = '{0} is read only'.format(option)
                if options[option]['readonly_why']:
                    ea = ' due to one of the following settings: {0}'.format(
                        ','.join(sorted(options[option]['readonly_why'])))
                    errstr += ea
                raise pygexc.InvalidParameterValue(errstr)
            if isinstance(options[option]['new_value'], six.string_types):
                # Coerce a simple string parameter to the expected list format
                options[option]['new_value'] = [options[option]['new_value']]
            options[option]['pending'] = options[option]['new_value']

            is_list = options[option]['is_list']
            count = 0
            changes = True
            config = etree.Element('config', ID=options[option]['lenovo_id'])
            configurations.append(config)
            setting = etree.Element('setting',
                                    ID=options[option]['lenovo_setting'])
            if options[option]['lenovo_group'] is not None:
                group = etree.Element('group',
                                      ID=options[option]['lenovo_group'])
                config.append(group)
                group.append(setting)
            else:
                config.append(setting)
            if is_list:
                container = etree.Element('list_data')
                setting.append(container)
            else:
                container = etree.Element('enumerate_data')
                setting.append(container)

            for value in options[option]['new_value']:
                choice = etree.Element('choice')
                container.append(choice)
                label = etree.Element('label')
                label.text = value
                choice.append(label)
                if is_list:
                    count += 1
                    instance = etree.Element(
                        'instance', ID=str(options[option]['lenovo_instance']),
                        order=str(count))
                else:
                    instance = etree.Element(
                        'instance', ID=str(options[option]['lenovo_instance']))
                choice.append(instance)

        if not changes:
            return

        xml = etree.tostring(configurations)
        data = EfiCompressor.FrameworkCompress(xml, len(xml))
        filehandle = self.imm_open("asu_update.efi", write=True,
                                   size=len(data))
        self.imm_write(filehandle, len(data), data)
        self.imm_close(filehandle)
