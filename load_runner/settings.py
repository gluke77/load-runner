# Copyright 2014 Symantec.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from os import environ as env


CONTROLLER_IP = env.get('CONTROLLER_IP')

OS_TENANT_NAME = env.get('OS_TENANT_NAME', 'demo')
OS_USERNAME = env.get('OS_USERNAME', 'admin')
OS_PASSWORD = env.get('OS_PASSWORD', 'pass')
OS_AUTH_URL = env.get('OS_AUTH_URL', 'http://{}:5000/v2.0/'.format(CONTROLLER_IP))
OS_SERVICE_ENDPOINT = env.get('OS_SERVICE_ENDPOINT', 'http://{}:35357/v2.0/'.format(CONTROLLER_IP))
OS_TOKEN = env.get('OS_TOKEN')

SPAWN_DELAY = int(env.get('SPAWN_DELAY', 0))
ACTIVATION_TIMEOUT = int(env.get('ACTIVATION_TIMEOUT', 300))
BOOT_TIMEOUT = int(env.get('BOOT_TIMEOUT', 300))
TEST_TIMEOUT = int(env.get('TEST_TIMEOUT', 300))

MANAGEMENT_NETWORK_ID = env.get('MANAGEMENT_NETWORK_ID')
MANAGEMENT_NET_NAME = env.net('MANAGEMENT_NET_NAME', 'private')
MANAGEMENT_CIDR = env.get('MANAGEMENT_CIDR')
PRIVATE_CIDR = env.get('PRIVATE_CIDR', '192.168.0.0/24')
FLAVOR_ID = env.get('AGENT_FLAVOR_ID')
IMAGE_ID = env.get('AGENT_IMAGE_ID')
ROOT_DIR = env.get('ROOT_DIR', '/tmp')

UPDATE_NEUTRON_QUOTAS = False  # Set to False for Contrail testing
USE_DHCP = True  # Set to True for Contrail testing
