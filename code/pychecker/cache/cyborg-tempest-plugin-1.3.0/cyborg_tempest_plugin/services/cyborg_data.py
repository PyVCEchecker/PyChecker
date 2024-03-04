# Copyright 2020 Inspur, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

NORMAL_DEVICE_PROFILE_DATA1 = [{
    "name": "fpga-num-1-dp1",
    "groups": [
        {
            "resources:FPGA": "1",
            "trait:CUSTOM_FAKE_DEVICE": "required"
        }],
    "description": "fpga-num-1-dp1-desc"
    }]

SCENARIO_DEVICE_PROFILE_DATA = [{
    "name": "fpga-num-1-scenario",
    "groups": [
        {
            "resources:FPGA": "1",
            "trait:CUSTOM_FAKE_DEVICE": "required"
        }]
    }]

BATCH_DELETE_DEVICE_PROFILE_DATA1 = [{
    "name": "afaas_example_1",
    "groups": [
        {
            "resources:FPGA": "1",
            "trait:CUSTOM_FPGA_1": "required",
            "trait:CUSTOM_FUNCTION_ID_3AFB": "required",
        }]
    }]

BATCH_DELETE_DEVICE_PROFILE_DATA2 = [{
    "name": "afaas_example_2",
    "groups": [
        {
            "resources:FPGA": "1",
            "trait:CUSTOM_FPGA_1": "required",
            "trait:CUSTOM_FUNCTION_ID_3AFB": "required",
        }]
    }]
