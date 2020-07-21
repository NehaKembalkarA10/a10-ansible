#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_router_ospf
description:
    - Open Shortest Path First (OSPF)
short_description: Configures A10 router.ospf
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
    distribute_internal_list:
        description:
        - "Field distribute_internal_list"
        required: False
        suboptions:
            di_cost:
                description:
                - "Cost of route"
            di_area_ipv4:
                description:
                - "OSPF area ID as a IP address format"
            di_area_num:
                description:
                - "OSPF area ID as a decimal value"
            di_type:
                description:
                - "'lw4o6'= LW4O6 Prefix; 'floating-ip'= Floating IP; 'ip-nat'= IP NAT; 'ip-nat-
          list'= IP NAT list; 'vip'= Only not flagged Virtual IP (VIP); 'vip-only-
          flagged'= Selected Virtual IP (VIP);"
    distribute_lists:
        description:
        - "Field distribute_lists"
        required: False
        suboptions:
            ospf_id:
                description:
                - "OSPF process ID"
            direction:
                description:
                - "'in'= Filter incoming routing updates; 'out'= Filter outgoing routing updates;"
            protocol:
                description:
                - "'bgp'= Border Gateway Protocol (BGP); 'connected'= Connected; 'floating-ip'=
          Floating IP; 'lw4o6'= LW4O6 Prefix; 'ip-nat'= IP NAT; 'ip-nat-list'= IP NAT
          list; 'isis'= ISO IS-IS; 'ospf'= Open Shortest Path First (OSPF); 'rip'=
          Routing Information Protocol (RIP); 'static'= Static routes;"
            option:
                description:
                - "'only-flagged'= Selected Virtual IP (VIP); 'only-not-flagged'= Only not
          flagged;"
            value:
                description:
                - "Access-list name"
    default_metric:
        description:
        - "Set metric of redistributed routes (Default metric)"
        required: False
    auto_cost_reference_bandwidth:
        description:
        - "Use reference bandwidth method to assign OSPF cost (The reference bandwidth in
          terms of Mbits per second)"
        required: False
    uuid:
        description:
        - "uuid of the object"
        required: False
    router_id:
        description:
        - "Field router_id"
        required: False
        suboptions:
            value:
                description:
                - "OSPF router-id in IPv4 address format"
    neighbor_list:
        description:
        - "Field neighbor_list"
        required: False
        suboptions:
            priority:
                description:
                - "OSPF priority of non-broadcast neighbor"
            cost:
                description:
                - "OSPF cost for point-to-multipoint neighbor (Metric)"
            poll_interval:
                description:
                - "OSPF dead-router polling interval (Seconds)"
            address:
                description:
                - "Neighbor address"
    ospf_1:
        description:
        - "Field ospf_1"
        required: False
        suboptions:
            abr_type:
                description:
                - "Field abr_type"
    host_list:
        description:
        - "Field host_list"
        required: False
        suboptions:
            host_address:
                description:
                - "Host address"
            area_cfg:
                description:
                - "Field area_cfg"
    log_adjacency_changes_cfg:
        description:
        - "Field log_adjacency_changes_cfg"
        required: False
        suboptions:
            state:
                description:
                - "'detail'= Log changes in adjacency state; 'disable'= Disable logging;"
    area_list:
        description:
        - "Field area_list"
        required: False
        suboptions:
            nssa_cfg:
                description:
                - "Field nssa_cfg"
            uuid:
                description:
                - "uuid of the object"
            filter_lists:
                description:
                - "Field filter_lists"
            area_num:
                description:
                - "OSPF area ID as a decimal value"
            virtual_link_list:
                description:
                - "Field virtual_link_list"
            stub_cfg:
                description:
                - "Field stub_cfg"
            shortcut:
                description:
                - "'default'= Set default shortcutting behavior; 'disable'= Disable shortcutting
          through the area; 'enable'= Enable shortcutting through the area;"
            auth_cfg:
                description:
                - "Field auth_cfg"
            range_list:
                description:
                - "Field range_list"
            default_cost:
                description:
                - "Set the summary-default cost of a NSSA or stub area (Stub's advertised default
          summary cost)"
            area_ipv4:
                description:
                - "OSPF area ID in IP address format"
    maximum_area:
        description:
        - "Maximum number of non-backbone areas (OSPF area limit)"
        required: False
    summary_address_list:
        description:
        - "Field summary_address_list"
        required: False
        suboptions:
            summary_address:
                description:
                - "Configure IP address summaries (Summary prefix)"
            not_advertise:
                description:
                - "Suppress routes that match the prefix"
            tag:
                description:
                - "Set tag (32-bit tag value)"
    rfc1583_compatible:
        description:
        - "Compatible with RFC 1583"
        required: False
    max_concurrent_dd:
        description:
        - "Maximum number allowed to process DD concurrently (Number of DD process)"
        required: False
    process_id:
        description:
        - "OSPF process ID"
        required: True
    passive_interface:
        description:
        - "Field passive_interface"
        required: False
        suboptions:
            tunnel_cfg:
                description:
                - "Field tunnel_cfg"
            loopback_cfg:
                description:
                - "Field loopback_cfg"
            ve_cfg:
                description:
                - "Field ve_cfg"
            lif_cfg:
                description:
                - "Field lif_cfg"
            trunk_cfg:
                description:
                - "Field trunk_cfg"
            eth_cfg:
                description:
                - "Field eth_cfg"
    default_information:
        description:
        - "Field default_information"
        required: False
        suboptions:
            originate:
                description:
                - "Distribute a default route"
            uuid:
                description:
                - "uuid of the object"
            always:
                description:
                - "Always advertise default route"
            metric:
                description:
                - "OSPF default metric (OSPF metric)"
            route_map:
                description:
                - "Route map reference (Pointer to route-map entries)"
            metric_type:
                description:
                - "OSPF metric type for default routes"
    overflow:
        description:
        - "Field overflow"
        required: False
        suboptions:
            database:
                description:
                - "Field database"
    bfd_all_interfaces:
        description:
        - "Enable BFD on all interfaces"
        required: False
    distance:
        description:
        - "Field distance"
        required: False
        suboptions:
            distance_value:
                description:
                - "OSPF Administrative distance"
            distance_ospf:
                description:
                - "Field distance_ospf"
    redistribute:
        description:
        - "Field redistribute"
        required: False
        suboptions:
            redist_list:
                description:
                - "Field redist_list"
            ospf_list:
                description:
                - "Field ospf_list"
            uuid:
                description:
                - "uuid of the object"
            ip_nat_floating_list:
                description:
                - "Field ip_nat_floating_list"
            vip_list:
                description:
                - "Field vip_list"
            route_map_ip_nat:
                description:
                - "Route map reference (Pointer to route-map entries)"
            ip_nat:
                description:
                - "IP-NAT"
            metric_ip_nat:
                description:
                - "OSPF default metric (OSPF metric)"
            tag_ip_nat:
                description:
                - "Set tag for routes redistributed into OSPF (32-bit tag value)"
            vip_floating_list:
                description:
                - "Field vip_floating_list"
            metric_type_ip_nat:
                description:
                - "'1'= Set OSPF External Type 1 metrics; '2'= Set OSPF External Type 2 metrics;"
    user_tag:
        description:
        - "Customized tag"
        required: False
    network_list:
        description:
        - "Field network_list"
        required: False
        suboptions:
            network_ipv4_cidr:
                description:
                - "OSPF network prefix"
            network_ipv4:
                description:
                - "Network number"
            network_area:
                description:
                - "Field network_area"
            network_ipv4_mask:
                description:
                - "OSPF wild card bits"
    timers:
        description:
        - "Field timers"
        required: False
        suboptions:
            spf:
                description:
                - "Field spf"
    ha_standby_extra_cost:
        description:
        - "Field ha_standby_extra_cost"
        required: False
        suboptions:
            group:
                description:
                - "Group (Group ID)"
            extra_cost:
                description:
                - "The extra cost value"


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
    "area_list",
    "auto_cost_reference_bandwidth",
    "bfd_all_interfaces",
    "default_information",
    "default_metric",
    "distance",
    "distribute_internal_list",
    "distribute_lists",
    "ha_standby_extra_cost",
    "host_list",
    "log_adjacency_changes_cfg",
    "max_concurrent_dd",
    "maximum_area",
    "neighbor_list",
    "network_list",
    "ospf_1",
    "overflow",
    "passive_interface",
    "process_id",
    "redistribute",
    "rfc1583_compatible",
    "router_id",
    "summary_address_list",
    "timers",
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
        'distribute_internal_list': {
            'type': 'list',
            'di_cost': {
                'type': 'int',
            },
            'di_area_ipv4': {
                'type': 'str',
            },
            'di_area_num': {
                'type': 'int',
            },
            'di_type': {
                'type':
                'str',
                'choices': [
                    'lw4o6', 'floating-ip', 'ip-nat', 'ip-nat-list', 'vip',
                    'vip-only-flagged'
                ]
            }
        },
        'distribute_lists': {
            'type': 'list',
            'ospf_id': {
                'type': 'int',
            },
            'direction': {
                'type': 'str',
                'choices': ['in', 'out']
            },
            'protocol': {
                'type':
                'str',
                'choices': [
                    'bgp', 'connected', 'floating-ip', 'lw4o6', 'ip-nat',
                    'ip-nat-list', 'isis', 'ospf', 'rip', 'static'
                ]
            },
            'option': {
                'type': 'str',
                'choices': ['only-flagged', 'only-not-flagged']
            },
            'value': {
                'type': 'str',
            }
        },
        'default_metric': {
            'type': 'int',
        },
        'auto_cost_reference_bandwidth': {
            'type': 'int',
        },
        'uuid': {
            'type': 'str',
        },
        'router_id': {
            'type': 'dict',
            'value': {
                'type': 'str',
            }
        },
        'neighbor_list': {
            'type': 'list',
            'priority': {
                'type': 'int',
            },
            'cost': {
                'type': 'int',
            },
            'poll_interval': {
                'type': 'int',
            },
            'address': {
                'type': 'str',
            }
        },
        'ospf_1': {
            'type': 'dict',
            'abr_type': {
                'type': 'dict',
                'option': {
                    'type': 'str',
                    'choices': ['cisco', 'ibm', 'shortcut', 'standard']
                }
            }
        },
        'host_list': {
            'type': 'list',
            'host_address': {
                'type': 'str',
            },
            'area_cfg': {
                'type': 'dict',
                'area_ipv4': {
                    'type': 'str',
                },
                'cost': {
                    'type': 'int',
                },
                'area_num': {
                    'type': 'int',
                }
            }
        },
        'log_adjacency_changes_cfg': {
            'type': 'dict',
            'state': {
                'type': 'str',
                'choices': ['detail', 'disable']
            }
        },
        'area_list': {
            'type': 'list',
            'nssa_cfg': {
                'type': 'dict',
                'default_information_originate': {
                    'type': 'bool',
                },
                'translator_role': {
                    'type': 'str',
                    'choices': ['always', 'candidate', 'never']
                },
                'metric': {
                    'type': 'int',
                },
                'nssa': {
                    'type': 'bool',
                },
                'no_redistribution': {
                    'type': 'bool',
                },
                'no_summary': {
                    'type': 'bool',
                },
                'metric_type': {
                    'type': 'int',
                }
            },
            'uuid': {
                'type': 'str',
            },
            'filter_lists': {
                'type': 'list',
                'acl_name': {
                    'type': 'str',
                },
                'acl_direction': {
                    'type': 'str',
                    'choices': ['in', 'out']
                },
                'filter_list': {
                    'type': 'bool',
                },
                'plist_name': {
                    'type': 'str',
                },
                'plist_direction': {
                    'type': 'str',
                    'choices': ['in', 'out']
                }
            },
            'area_num': {
                'type': 'int',
                'required': True,
            },
            'virtual_link_list': {
                'type': 'list',
                'dead_interval': {
                    'type': 'int',
                },
                'message_digest_key': {
                    'type': 'int',
                },
                'hello_interval': {
                    'type': 'int',
                },
                'bfd': {
                    'type': 'bool',
                },
                'transmit_delay': {
                    'type': 'int',
                },
                'virtual_link_authentication': {
                    'type': 'bool',
                },
                'virtual_link_ip_addr': {
                    'type': 'str',
                },
                'virtual_link_auth_type': {
                    'type': 'str',
                    'choices': ['message-digest', 'null']
                },
                'authentication_key': {
                    'type': 'str',
                },
                'retransmit_interval': {
                    'type': 'int',
                },
                'md5': {
                    'type': 'str',
                }
            },
            'stub_cfg': {
                'type': 'dict',
                'stub': {
                    'type': 'bool',
                },
                'no_summary': {
                    'type': 'bool',
                }
            },
            'shortcut': {
                'type': 'str',
                'choices': ['default', 'disable', 'enable']
            },
            'auth_cfg': {
                'type': 'dict',
                'authentication': {
                    'type': 'bool',
                },
                'message_digest': {
                    'type': 'bool',
                }
            },
            'range_list': {
                'type': 'list',
                'area_range_prefix': {
                    'type': 'str',
                },
                'option': {
                    'type': 'str',
                    'choices': ['advertise', 'not-advertise']
                }
            },
            'default_cost': {
                'type': 'int',
            },
            'area_ipv4': {
                'type': 'str',
                'required': True,
            }
        },
        'maximum_area': {
            'type': 'int',
        },
        'summary_address_list': {
            'type': 'list',
            'summary_address': {
                'type': 'str',
            },
            'not_advertise': {
                'type': 'bool',
            },
            'tag': {
                'type': 'int',
            }
        },
        'rfc1583_compatible': {
            'type': 'bool',
        },
        'max_concurrent_dd': {
            'type': 'int',
        },
        'process_id': {
            'type': 'int',
            'required': True,
        },
        'passive_interface': {
            'type': 'dict',
            'tunnel_cfg': {
                'type': 'list',
                'tunnel': {
                    'type': 'str',
                },
                'tunnel_address': {
                    'type': 'str',
                }
            },
            'loopback_cfg': {
                'type': 'list',
                'loopback_address': {
                    'type': 'str',
                },
                'loopback': {
                    'type': 'str',
                }
            },
            've_cfg': {
                'type': 'list',
                've_address': {
                    'type': 'str',
                },
                've': {
                    'type': 'str',
                }
            },
            'lif_cfg': {
                'type': 'list',
                'lif': {
                    'type': 'str',
                },
                'lif_address': {
                    'type': 'str',
                }
            },
            'trunk_cfg': {
                'type': 'list',
                'trunk_address': {
                    'type': 'str',
                },
                'trunk': {
                    'type': 'str',
                }
            },
            'eth_cfg': {
                'type': 'list',
                'ethernet': {
                    'type': 'str',
                },
                'eth_address': {
                    'type': 'str',
                }
            }
        },
        'default_information': {
            'type': 'dict',
            'originate': {
                'type': 'bool',
            },
            'uuid': {
                'type': 'str',
            },
            'always': {
                'type': 'bool',
            },
            'metric': {
                'type': 'int',
            },
            'route_map': {
                'type': 'str',
            },
            'metric_type': {
                'type': 'int',
            }
        },
        'overflow': {
            'type': 'dict',
            'database': {
                'type': 'dict',
                'count': {
                    'type': 'int',
                },
                'recovery_time': {
                    'type': 'int',
                },
                'limit': {
                    'type': 'str',
                    'choices': ['hard', 'soft']
                },
                'db_external': {
                    'type': 'int',
                }
            }
        },
        'bfd_all_interfaces': {
            'type': 'bool',
        },
        'distance': {
            'type': 'dict',
            'distance_value': {
                'type': 'int',
            },
            'distance_ospf': {
                'type': 'dict',
                'distance_external': {
                    'type': 'int',
                },
                'distance_intra_area': {
                    'type': 'int',
                },
                'distance_inter_area': {
                    'type': 'int',
                }
            }
        },
        'redistribute': {
            'type': 'dict',
            'redist_list': {
                'type': 'list',
                'metric': {
                    'type': 'int',
                },
                'route_map': {
                    'type': 'str',
                },
                'ntype': {
                    'type':
                    'str',
                    'choices': [
                        'bgp', 'connected', 'floating-ip', 'ip-nat-list',
                        'lw4o6', 'nat-map', 'isis', 'rip', 'static'
                    ]
                },
                'metric_type': {
                    'type': 'str',
                    'choices': ['1', '2']
                },
                'tag': {
                    'type': 'int',
                }
            },
            'ospf_list': {
                'type': 'list',
                'tag_ospf': {
                    'type': 'int',
                },
                'process_id': {
                    'type': 'int',
                },
                'route_map_ospf': {
                    'type': 'str',
                },
                'metric_ospf': {
                    'type': 'int',
                },
                'ospf': {
                    'type': 'bool',
                },
                'metric_type_ospf': {
                    'type': 'str',
                    'choices': ['1', '2']
                }
            },
            'uuid': {
                'type': 'str',
            },
            'ip_nat_floating_list': {
                'type': 'list',
                'ip_nat_floating_IP_forward': {
                    'type': 'str',
                },
                'ip_nat_prefix': {
                    'type': 'str',
                }
            },
            'vip_list': {
                'type': 'list',
                'metric_type_vip': {
                    'type': 'str',
                    'choices': ['1', '2']
                },
                'tag_vip': {
                    'type': 'int',
                },
                'route_map_vip': {
                    'type': 'str',
                },
                'type_vip': {
                    'type': 'str',
                    'choices': ['only-flagged', 'only-not-flagged']
                },
                'metric_vip': {
                    'type': 'int',
                }
            },
            'route_map_ip_nat': {
                'type': 'str',
            },
            'ip_nat': {
                'type': 'bool',
            },
            'metric_ip_nat': {
                'type': 'int',
            },
            'tag_ip_nat': {
                'type': 'int',
            },
            'vip_floating_list': {
                'type': 'list',
                'vip_address': {
                    'type': 'str',
                },
                'vip_floating_IP_forward': {
                    'type': 'str',
                }
            },
            'metric_type_ip_nat': {
                'type': 'str',
                'choices': ['1', '2']
            }
        },
        'user_tag': {
            'type': 'str',
        },
        'network_list': {
            'type': 'list',
            'network_ipv4_cidr': {
                'type': 'str',
            },
            'network_ipv4': {
                'type': 'str',
            },
            'network_area': {
                'type': 'dict',
                'network_area_num': {
                    'type': 'int',
                },
                'network_area_ipv4': {
                    'type': 'str',
                },
                'instance_value': {
                    'type': 'int',
                }
            },
            'network_ipv4_mask': {
                'type': 'str',
            }
        },
        'timers': {
            'type': 'dict',
            'spf': {
                'type': 'dict',
                'exp': {
                    'type': 'dict',
                    'max_delay': {
                        'type': 'int',
                    },
                    'min_delay': {
                        'type': 'int',
                    }
                }
            }
        },
        'ha_standby_extra_cost': {
            'type': 'list',
            'group': {
                'type': 'int',
            },
            'extra_cost': {
                'type': 'int',
            }
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/ospf/{process-id}"

    f_dict = {}
    f_dict["process-id"] = module.params["process_id"]

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
    url_base = "/axapi/v3/router/ospf/{process-id}"

    f_dict = {}
    f_dict["process-id"] = ""

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
        for k, v in payload["ospf"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["ospf"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["ospf"][k] = v
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
    payload = build_json("ospf", module)
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
