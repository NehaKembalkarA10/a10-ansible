#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_cgnv6_lsn_rule_list
description:
    - Configure LSN Rule-List
short_description: Configures A10 cgnv6.lsn-rule-list
author: A10 Networks 2018
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
          - absent
        required: True
    ansible_host:
        description:
        - Host for AXAPI authentication
        required: True
    ansible_username:
        description:
        - Username for AXAPI authentication
        required: True
    ansible_password:
        description:
        - Password for AXAPI authentication
        required: True
    ansible_port:
        description:
        - Port for AXAPI authentication
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        required: False
    uuid:
        description:
        - "uuid of the object"
        required: False
    domain_ip:
        description:
        - "Field domain_ip"
        required: False
        suboptions:
            sampling_enable:
                description:
                - "Field sampling_enable"
            uuid:
                description:
                - "uuid of the object"
    default:
        description:
        - "Field default"
        required: False
        suboptions:
            sampling_enable:
                description:
                - "Field sampling_enable"
            uuid:
                description:
                - "uuid of the object"
            rule_cfg:
                description:
                - "Field rule_cfg"
    user_tag:
        description:
        - "Customized tag"
        required: False
    name:
        description:
        - "LSN Rule-List Name"
        required: True
    ip_list:
        description:
        - "Field ip_list"
        required: False
        suboptions:
            ipv4_addr:
                description:
                - "Configure a Specific Rule-Set (IP Network Address)"
            rule_cfg:
                description:
                - "Field rule_cfg"
            sampling_enable:
                description:
                - "Field sampling_enable"
            user_tag:
                description:
                - "Customized tag"
            uuid:
                description:
                - "uuid of the object"
    domain_list_name_list:
        description:
        - "Field domain_list_name_list"
        required: False
        suboptions:
            sampling_enable:
                description:
                - "Field sampling_enable"
            name_domain_list:
                description:
                - "Configure a Specific Rule-Set (Domain List Name)"
            uuid:
                description:
                - "uuid of the object"
            user_tag:
                description:
                - "Customized tag"
            rule_cfg:
                description:
                - "Field rule_cfg"
    domain_name_list:
        description:
        - "Field domain_name_list"
        required: False
        suboptions:
            name_domain:
                description:
                - "Configure a Specific Rule-Set (Domain Name)"
            sampling_enable:
                description:
                - "Field sampling_enable"
            uuid:
                description:
                - "uuid of the object"
            user_tag:
                description:
                - "Customized tag"
            rule_cfg:
                description:
                - "Field rule_cfg"
    http_match_domain_name:
        description:
        - "Enable match domain name in http request"
        required: False


'''

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = [
    "default",
    "domain_ip",
    "domain_list_name_list",
    "domain_name_list",
    "http_match_domain_name",
    "ip_list",
    "name",
    "user_tag",
    "uuid",
]

from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    errors as a10_ex
from ansible_collections.a10.acos_axapi.plugins.module_utils.axapi_http import \
    client_factory
from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import \
    KW_OUT, translate_blacklist as translateBlacklist


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str',
                   default="present",
                   choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(
            type='dict',
            name=dict(type='str', ),
            shared=dict(type='str', ),
            required=False,
        ),
        a10_device_context_id=dict(
            type='int',
            choices=[1, 2, 3, 4, 5, 6, 7, 8],
            required=False,
        ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )


def get_argspec():
    rv = get_default_argspec()
    rv.update({
        'uuid': {
            'type': 'str',
        },
        'domain_ip': {
            'type': 'dict',
            'sampling_enable': {
                'type': 'list',
                'counters1': {
                    'type': 'str',
                    'choices': ['all', 'placeholder']
                }
            },
            'uuid': {
                'type': 'str',
            }
        },
        'default': {
            'type': 'dict',
            'sampling_enable': {
                'type': 'list',
                'counters1': {
                    'type': 'str',
                    'choices': ['all', 'placeholder']
                }
            },
            'uuid': {
                'type': 'str',
            },
            'rule_cfg': {
                'type': 'list',
                'icmp_others_cfg': {
                    'type': 'dict',
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    }
                },
                'udp_cfg': {
                    'type': 'dict',
                    'port_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'end_port': {
                        'type': 'int',
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'start_port': {
                        'type': 'int',
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    }
                },
                'tcp_cfg': {
                    'type': 'dict',
                    'port_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp', 'template'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'end_port': {
                        'type': 'int',
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'start_port': {
                        'type': 'int',
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    },
                    'http_alg': {
                        'type': 'str',
                    }
                },
                'dscp_cfg': {
                    'type': 'dict',
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action']
                    },
                    'action_type': {
                        'type': 'str',
                        'choices': ['set-dscp']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'dscp_match': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', 'any', '0', '1', '2', '3', '4', '5',
                            '6', '7', '8', '9', '10', '11', '12', '13', '14',
                            '15', '16', '17', '18', '19', '20', '21', '22',
                            '23', '24', '25', '26', '27', '28', '29', '30',
                            '31', '32', '33', '34', '35', '36', '37', '38',
                            '39', '40', '41', '42', '43', '44', '45', '46',
                            '47', '48', '49', '50', '51', '52', '53', '54',
                            '55', '56', '57', '58', '59', '60', '61', '62',
                            '63'
                        ]
                    }
                },
                'proto': {
                    'type': 'str',
                    'choices': ['tcp', 'udp', 'icmp', 'others', 'dscp']
                }
            }
        },
        'user_tag': {
            'type': 'str',
        },
        'name': {
            'type': 'str',
            'required': True,
        },
        'ip_list': {
            'type': 'list',
            'ipv4_addr': {
                'type': 'str',
                'required': True,
            },
            'rule_cfg': {
                'type': 'list',
                'icmp_others_cfg': {
                    'type': 'dict',
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    }
                },
                'udp_cfg': {
                    'type': 'dict',
                    'port_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp', 'idle-timeout'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'timeout_val': {
                        'type': 'int',
                    },
                    'end_port': {
                        'type': 'int',
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'fast': {
                        'type': 'str',
                        'choices': ['fast']
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'start_port': {
                        'type': 'int',
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'pool': {
                        'type': 'str',
                    }
                },
                'tcp_cfg': {
                    'type': 'dict',
                    'port_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp', 'template', 'idle-timeout'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'timeout_val': {
                        'type': 'int',
                    },
                    'end_port': {
                        'type': 'int',
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'fast': {
                        'type': 'str',
                        'choices': ['fast']
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'start_port': {
                        'type': 'int',
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'pool': {
                        'type': 'str',
                    },
                    'http_alg': {
                        'type': 'str',
                    }
                },
                'dscp_cfg': {
                    'type': 'dict',
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action']
                    },
                    'action_type': {
                        'type': 'str',
                        'choices': ['set-dscp']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'dscp_match': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', 'any', '0', '1', '2', '3', '4', '5',
                            '6', '7', '8', '9', '10', '11', '12', '13', '14',
                            '15', '16', '17', '18', '19', '20', '21', '22',
                            '23', '24', '25', '26', '27', '28', '29', '30',
                            '31', '32', '33', '34', '35', '36', '37', '38',
                            '39', '40', '41', '42', '43', '44', '45', '46',
                            '47', '48', '49', '50', '51', '52', '53', '54',
                            '55', '56', '57', '58', '59', '60', '61', '62',
                            '63'
                        ]
                    }
                },
                'proto': {
                    'type': 'str',
                    'choices': ['tcp', 'udp', 'icmp', 'others', 'dscp']
                }
            },
            'sampling_enable': {
                'type': 'list',
                'counters1': {
                    'type': 'str',
                    'choices': ['all', 'placeholder']
                }
            },
            'user_tag': {
                'type': 'str',
            },
            'uuid': {
                'type': 'str',
            }
        },
        'domain_list_name_list': {
            'type': 'list',
            'sampling_enable': {
                'type': 'list',
                'counters1': {
                    'type': 'str',
                    'choices': ['all', 'placeholder']
                }
            },
            'name_domain_list': {
                'type': 'str',
                'required': True,
            },
            'uuid': {
                'type': 'str',
            },
            'user_tag': {
                'type': 'str',
            },
            'rule_cfg': {
                'type': 'list',
                'icmp_others_cfg': {
                    'type': 'dict',
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    }
                },
                'udp_cfg': {
                    'type': 'dict',
                    'port_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'end_port': {
                        'type': 'int',
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'start_port': {
                        'type': 'int',
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    }
                },
                'tcp_cfg': {
                    'type': 'dict',
                    'port_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp', 'template'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'end_port': {
                        'type': 'int',
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'start_port': {
                        'type': 'int',
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    },
                    'http_alg': {
                        'type': 'str',
                    }
                },
                'dscp_cfg': {
                    'type': 'dict',
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action']
                    },
                    'action_type': {
                        'type': 'str',
                        'choices': ['set-dscp']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'dscp_match': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', 'any', '0', '1', '2', '3', '4', '5',
                            '6', '7', '8', '9', '10', '11', '12', '13', '14',
                            '15', '16', '17', '18', '19', '20', '21', '22',
                            '23', '24', '25', '26', '27', '28', '29', '30',
                            '31', '32', '33', '34', '35', '36', '37', '38',
                            '39', '40', '41', '42', '43', '44', '45', '46',
                            '47', '48', '49', '50', '51', '52', '53', '54',
                            '55', '56', '57', '58', '59', '60', '61', '62',
                            '63'
                        ]
                    }
                },
                'proto': {
                    'type': 'str',
                    'choices': ['tcp', 'udp', 'icmp', 'others', 'dscp']
                }
            }
        },
        'domain_name_list': {
            'type': 'list',
            'name_domain': {
                'type': 'str',
                'required': True,
            },
            'sampling_enable': {
                'type': 'list',
                'counters1': {
                    'type': 'str',
                    'choices': ['all', 'placeholder']
                }
            },
            'uuid': {
                'type': 'str',
            },
            'user_tag': {
                'type': 'str',
            },
            'rule_cfg': {
                'type': 'list',
                'icmp_others_cfg': {
                    'type': 'dict',
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    }
                },
                'udp_cfg': {
                    'type': 'dict',
                    'port_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'end_port': {
                        'type': 'int',
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'start_port': {
                        'type': 'int',
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    }
                },
                'tcp_cfg': {
                    'type': 'dict',
                    'port_list': {
                        'type': 'str',
                    },
                    'action_type': {
                        'type':
                        'str',
                        'choices': [
                            'dnat', 'drop', 'one-to-one-snat', 'pass-through',
                            'snat', 'set-dscp', 'template'
                        ]
                    },
                    'no_snat': {
                        'type': 'bool',
                    },
                    'ipv4_list': {
                        'type': 'str',
                    },
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'end_port': {
                        'type': 'int',
                    },
                    'vrid': {
                        'type': 'int',
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action', 'no-action']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'start_port': {
                        'type': 'int',
                    },
                    'shared': {
                        'type': 'bool',
                    },
                    'pool': {
                        'type': 'str',
                    },
                    'http_alg': {
                        'type': 'str',
                    }
                },
                'dscp_cfg': {
                    'type': 'dict',
                    'dscp_value': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', '0', '1', '2', '3', '4', '5', '6',
                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                            '16', '17', '18', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '35', '36', '37', '38', '39',
                            '40', '41', '42', '43', '44', '45', '46', '47',
                            '48', '49', '50', '51', '52', '53', '54', '55',
                            '56', '57', '58', '59', '60', '61', '62', '63'
                        ]
                    },
                    'action_cfg': {
                        'type': 'str',
                        'choices': ['action']
                    },
                    'action_type': {
                        'type': 'str',
                        'choices': ['set-dscp']
                    },
                    'dscp_direction': {
                        'type': 'str',
                        'choices': ['inbound', 'outbound']
                    },
                    'dscp_match': {
                        'type':
                        'str',
                        'choices': [
                            'default', 'af11', 'af12', 'af13', 'af21', 'af22',
                            'af23', 'af31', 'af32', 'af33', 'af41', 'af42',
                            'af43', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'cs6',
                            'cs7', 'ef', 'any', '0', '1', '2', '3', '4', '5',
                            '6', '7', '8', '9', '10', '11', '12', '13', '14',
                            '15', '16', '17', '18', '19', '20', '21', '22',
                            '23', '24', '25', '26', '27', '28', '29', '30',
                            '31', '32', '33', '34', '35', '36', '37', '38',
                            '39', '40', '41', '42', '43', '44', '45', '46',
                            '47', '48', '49', '50', '51', '52', '53', '54',
                            '55', '56', '57', '58', '59', '60', '61', '62',
                            '63'
                        ]
                    }
                },
                'proto': {
                    'type': 'str',
                    'choices': ['tcp', 'udp', 'icmp', 'others', 'dscp']
                }
            }
        },
        'http_match_domain_name': {
            'type': 'bool',
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/lsn-rule-list/{name}"

    f_dict = {}
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)


def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]


def get(module):
    return module.client.get(existing_url(module))


def get_list(module):
    return module.client.get(list_url(module))


def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return None


def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")


def _build_dict_from_param(param):
    rv = {}

    for k, v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        elif isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv


def build_envelope(title, data):
    return {title: data}


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/lsn-rule-list/{name}"

    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([
        x for x in requires_one_of if x in params and params.get(x) is not None
    ])

    errors = []
    marg = []

    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc, msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc, msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc, msg = REQUIRED_VALID

    if not rc:
        errors.append(msg.format(", ".join(marg)))

    return rc, errors


def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v is not None:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            elif isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)


def report_changes(module, result, existing_config, payload):
    if existing_config:
        for k, v in payload["lsn-rule-list"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["lsn-rule-list"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["lsn-rule-list"][k] = v
            result.update(**existing_config)
    else:
        result.update(**payload)
    return result


def create(module, result, payload):
    try:
        post_result = module.client.post(new_url(module), payload)
        if post_result:
            result.update(**post_result)
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def update(module, result, existing_config, payload):
    try:
        post_result = module.client.post(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def present(module, result, existing_config):
    payload = build_json("lsn-rule-list", module)
    changed_config = report_changes(module, result, existing_config, payload)
    if module.check_mode:
        return changed_config
    elif not existing_config:
        return create(module, result, payload)
    elif existing_config and not changed_config.get('changed'):
        return update(module, result, existing_config, payload)
    else:
        result["changed"] = True
        return result


def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def absent(module, result, existing_config):
    if module.check_mode:
        if existing_config:
            result["changed"] = True
            return result
        else:
            result["changed"] = False
            return result
    else:
        return delete(module, result)


def replace(module, result, existing_config, payload):
    try:
        post_result = module.client.put(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def run_command(module):
    run_errors = []

    result = dict(changed=False, original_message="", message="", result={})

    state = module.params["state"]
    ansible_host = module.params["ansible_host"]
    ansible_username = module.params["ansible_username"]
    ansible_password = module.params["ansible_password"]
    ansible_port = module.params["ansible_port"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    if ansible_port == 80:
        protocol = "http"
    elif ansible_port == 443:
        protocol = "https"

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)

    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(ansible_host, ansible_port, protocol,
                                   ansible_username, ansible_password)

    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)

    if state == 'present':
        result = present(module, result, existing_config)

    if state == 'absent':
        result = absent(module, result, existing_config)

    if state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
    module.client.session.close()
    return result


def main():
    module = AnsibleModule(argument_spec=get_argspec(),
                           supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)


# standard ansible module imports
from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()
