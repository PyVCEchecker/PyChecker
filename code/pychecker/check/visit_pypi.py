import time

from pychecker.check.common import crawl_content, compare_version
from pychecker.utils import read_object_from_file, write_object_to_file
from functools import cmp_to_key
import json
import pychecker.config as config
import zipfile
import tarfile
import os


metadata_cache_path = "/tmp/metadata_cache.json"  # cache metadata
pkgver_cache_path = "/tmp/pkgver_cache.json"  # cache pkg-ver
metadata_cache = read_object_from_file(metadata_cache_path)
if not metadata_cache:
    metadata_cache = dict()
pkgver_cache = read_object_from_file(pkgver_cache_path)
if not pkgver_cache:
    pkgver_cache = dict()
DEPS = "requires_dist"  # dep field in metadata
COMP = "requires_python"  # comp field in metadata


def get_urls(pkg, ver):
    json_url = f"https://pypi.org/pypi/{pkg}/{ver}/json"
    content = crawl_content(json_url)
    if not content:
        return None
    content = json.loads(content)
    urls = content["urls"]
    urls = [item["url"] for item in urls]
    return urls


def parse_whl_comp(pkg, ver):
    # parse comp Python versions of pkg ver's wheel resources
    urls = get_urls(pkg, ver)
    if urls==None:
        #try three times
        for times in range(3):
            time.sleep(0.1)
            urls=get_urls(pkg,ver)
            if urls!=None:
                break
        if urls==None:
            print("No urls(try three  times)")
            return None
    pyver = set()
    for item in urls:
        if ver not in item:
            continue
        if item.endswith(".tar.gz") or item.endswith(".tar.bz2") or item.endswith(".zip"):
            continue
        for version in config.PY_VERSIONS:
            cp_tag = "cp{}".format(version.replace(".", ""))
            py_tag = "py{}".format(version.replace(".", ""))
            if cp_tag in item or py_tag in item:
                pyver.add(version)
        if len(pyver) == 0:
            if "cp2" in item or "py2" in item:
                pyver.add("2.7")
            if "cp3" in item or "py3" in item:
                py3_set = set(config.PY_VERSIONS)
                py3_set.remove("2.7")
                pyver = pyver.union(py3_set)
    return pyver


def get_pkg_versions(pkg, cache=True):
    if cache:
        # cache visited pkg in a local dict
        try:
            versions = pkgver_cache[pkg]
            return versions
        except KeyError:
            pass
    # query PyPI for versions
    url = f"https://pypi.org/pypi/{pkg}/json"
    content = crawl_content(url)
    if not content:
        return None
    versions = json.loads(content)["releases"].keys()
    versions = sorted(versions, key=cmp_to_key(compare_version))

    if cache:
        # save info
        pkgver_cache[pkg] = versions
        write_object_to_file(pkgver_cache_path, pkgver_cache)
    return versions


def get_metadata(pkg, ver, cache=True):
    if cache:
        try:
            metadata = metadata_cache[pkg][ver]
            return metadata
        except KeyError:
            pass

    url = f"https://pypi.org/pypi/{pkg}/{ver}/json"
    content = crawl_content(url)
    if not content:
        return None
    content = json.loads(content)
    metadata = content["info"]

    if not metadata[DEPS]:
        # only provide source code on PyPI, which does not specify requires-dist in METADATA
        # download the source code archive, and extract its requires.txt(or requirements.txt)
        try:
            url = content["urls"][0]
            deps = download_extract_deps(url)#requires.txt(or requirements.txt)
            metadata[DEPS] = deps
        except (KeyError, IndexError):
            pass
    if not metadata[DEPS]:
        metadata[DEPS] = list()

    if cache:
        if pkg not in metadata_cache:
            metadata_cache[pkg] = dict()
        if ver not in metadata_cache[pkg]:
            metadata_cache[pkg][ver] = dict()
        if not metadata[DEPS]:
            metadata[DEPS] = list()
        if not metadata[COMP]:
            metadata[COMP] = ""
        metadata_cache[pkg][ver][DEPS] = metadata[DEPS]
        metadata_cache[pkg][ver][COMP] = metadata[COMP]
        write_object_to_file(metadata_cache_path, metadata_cache)
    return {DEPS: metadata[DEPS], COMP: metadata[COMP]}  # simplify, return useful results

def whether_requires_python(pkg, ver):

    url = f"https://pypi.org/pypi/{pkg}/{ver}/json"
    content = crawl_content(url)
    if not content:
        print(pkg,"==",ver,":No json")
        return False
    content = json.loads(content)
    metadata = content["info"]
    if not metadata[COMP]:
        print(pkg, "==", ver, ":no requires_python")
        return False
    print(pkg,"==",ver,":",metadata[COMP])
    return True

def whether_requires_dist(pkg, ver):

    url = f"https://pypi.org/pypi/{pkg}/{ver}/json"
    content = crawl_content(url)
    if not content:
        print(pkg,"==",ver,":No json")
        return False
    content = json.loads(content)
    metadata = content["info"]
    if not metadata[DEPS]:
        print(pkg, "==", ver, ":no requires_dist")
        return False
    print(pkg,"==",ver,":",metadata[COMP])
    return True


def download_extract_deps(url):
    # download the source code archive, and extract its requires.txt(or requirements.txt)
    # find the download url
    fileurl = url["url"]
    filename = url["filename"]
    content = crawl_content(fileurl)
    if not content:
        return
    tmp_path = os.path.join("/tmp", filename)
    with open(tmp_path, "wb") as f:
        f.write(content)

    # unzip, extract requires.txt
    if tmp_path.endswith(".whl") or tmp_path.endswith(".zip"):
        archive = zipfile.ZipFile(tmp_path)
        require_content = get_require_content_zip(archive)
    elif tmp_path.endswith(".tar.gz") or tmp_path.endswith(".tar.bz2") or \
            tmp_path.endswith("tgz"):
        archive = tarfile.TarFile.open(tmp_path)
        require_content = get_require_content_tar(archive)
    else:
        os.remove(tmp_path)
        return

    os.remove(tmp_path)
    return preprocess_require_content(require_content)


def get_require_content_tar(archive):
    files = archive.getnames()
    requires = [x for x in files if os.sep+"requires.txt" in x or os.sep+"requirements.txt" in x]
    if len(requires) == 0:
        return ""

    require_file = requires[0]
    # print(require_file)
    require_bytes = archive.extractfile(require_file).read()
    content = require_bytes.decode()
    return content


def get_require_content_zip(archive):
    files = archive.namelist()
    requires = [x for x in files if os.sep+"requires.txt" in x or os.sep+"requirements.txt" in x]
    if len(requires) == 0:
        return ""
    require_file = requires[0]
    require_bytes = archive.read(require_file)
    content = require_bytes.decode()
    return content


def preprocess_require_content(content):
    lines = content.split("\n")
    requires = list()
    for line in lines:
        line = line.strip()
        line = line.lower()
        if not line:
            continue  # empty line
        if line.startswith("["):
            break  # extra deps, stop
        if "[" in line:
            line = line.split("[")[0]  # ignore extra requires now
        if line.endswith("\\"):
            line = line[:-1]  # end of line
        if "#" in line:
            line = line.split("#")[0]  # comment
        requires.append(line)
    return requires


def get_source_url(pkg, ver,detect_runtime_error):
    urls = get_urls(pkg, ver)
    if not urls:
        print("The network is abnormal, please check the network settings or run again.")
        return None
    for url in urls:
        if url.endswith("tar.gz") or url.endswith("tar.bz2") or url.endswith(".zip"):
            return url
    for url in urls:
        if detect_runtime_error == True and url.endswith(".whl"):
            return url

    return None


def download_extract_source(url, target_path, cache_path=config.CACHE_DIR,detect_runtime_error=False):
    # download & unzip source code resource
    content = crawl_content(url)
    if not content:
        return None
    filename = url.split("/")[-1]
    path = os.path.join(cache_path, filename)
    with open(path, "wb") as f:
        f.write(content)

    if path.endswith(".zip"):
        with zipfile.ZipFile(path, 'r') as zipf:
            zipf.extractall(target_path)
    elif path.endswith(".tar.gz") or path.endswith(".tar.bz2") or path.endswith("tgz"):
        # with tarfile.open(path) as tarf:
        #     tarf.extractall(".")
        cmd = f"cd {cache_path} && tar -xvf {path} >/dev/null"
        os.system(cmd)  # tarfile.ReadError: bad checksum
        #change .whl to .zip
    elif path.endswith(".whl") and detect_runtime_error==True:
        IsWhl=True
        path2=path[:-4]+".zip"
        os.rename(path,path2)
        path=path2
        with zipfile.ZipFile(path, 'r') as zipf:
            zipf.extractall(target_path)
    #preprocessing uncompress directory
    root,tar_name=os.path.split(target_path)
    # 1.same as its child dir
    temp_path=os.path.join(target_path,tar_name)
    if os.path.exists(temp_path):
        os.system('mv {}/* {}'.format(temp_path,target_path))
        os.system('rm -r {}'.format(temp_path))

    # 2.upperAlha dir name to lower
    for dir in os.listdir(root):
        if dir.lower().replace('-', '_')==tar_name.replace('-', '_') and dir!=tar_name:
            origin_dir=os.path.join(root,dir)
            if os.path.exists(origin_dir):
                os.rename(origin_dir,target_path)

    # 3.
    # all files renamed to lower
    # for fpath,dirnames,fnames in os.walk(target_path):
    #     for name in fnames:
    #         if not name.islower():
    #             origin_name=os.path.join(fpath,name)
    #             after_name=os.path.join(fpath,name.lower())
    #             os.rename(origin_name,after_name)

    return target_path, path

def use_classifiers_to_detect_python2(pkg,ver,pyvers):

    url = f"https://pypi.org/pypi/{pkg}/{ver}/json"
    content = crawl_content(url)
    if not content:
        return None
    content = json.loads(content)
    metadata = content["info"]
    classifiers=metadata['classifiers']
    python3='Programming Language :: Python :: 3'
    python2='Programming Language :: Python :: 2'
    compatible2=False
    compatible3=False
    if classifiers:
        for classifier in classifiers:
            if python3 in classifier:
                compatible3=True
            if python2 in classifier:
                compatible3=True
        if compatible3 and not compatible2:
            #python 2 is not compatible
            if '2.7' in pyvers:
                return True
    return False

