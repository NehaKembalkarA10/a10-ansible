#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_slb_server_port
description:
    - Real Server Port
short_description: Configures A10 slb.server.port
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
    server_name:
        description:
        - Key to identify parent object
    oper:
        description:
        - "Field oper"
        required: False
        suboptions:
            down_grace_period_allowed:
                description:
                - "Field down_grace_period_allowed"
            protocol:
                description:
                - "'tcp'= TCP Port; 'udp'= UDP Port;"
            ip:
                description:
                - "Field ip"
            ports_freed_total:
                description:
                - "Field ports_freed_total"
            ports_consumed_total:
                description:
                - "Field ports_consumed_total"
            aflow_queue_size:
                description:
                - "Field aflow_queue_size"
            current_time:
                description:
                - "Field current_time"
            alloc_failed:
                description:
                - "Field alloc_failed"
            vrid:
                description:
                - "Field vrid"
            state:
                description:
                - "Field state"
            ipv6:
                description:
                - "Field ipv6"
            slow_start_conn_limit:
                description:
                - "Field slow_start_conn_limit"
            resv_conn:
                description:
                - "Field resv_conn"
            hm_index:
                description:
                - "Field hm_index"
            down_time_grace_period:
                description:
                - "Field down_time_grace_period"
            inband_hm_reassign_num:
                description:
                - "Field inband_hm_reassign_num"
            ports_consumed:
                description:
                - "Field ports_consumed"
            port_number:
                description:
                - "Port Number"
            curr_observe_rate:
                description:
                - "Field curr_observe_rate"
            curr_conn_rate:
                description:
                - "Field curr_conn_rate"
            disable:
                description:
                - "Field disable"
            aflow_conn_limit:
                description:
                - "Field aflow_conn_limit"
            diameter_enabled:
                description:
                - "Field diameter_enabled"
            soft_down_time:
                description:
                - "Field soft_down_time"
            ha_group_id:
                description:
                - "Field ha_group_id"
            hm_key:
                description:
                - "Field hm_key"
            es_resp_time:
                description:
                - "Field es_resp_time"
            conn_rate_unit:
                description:
                - "Field conn_rate_unit"
    health_check_disable:
        description:
        - "Disable health check"
        required: False
    protocol:
        description:
        - "'tcp'= TCP Port; 'udp'= UDP Port;"
        required: True
    weight:
        description:
        - "Port Weight (Connection Weight)"
        required: False
    shared_rport_health_check:
        description:
        - "Reference a health-check from shared partition"
        required: False
    stats_data_action:
        description:
        - "'stats-data-enable'= Enable statistical data collection for real server port;
          'stats-data-disable'= Disable statistical data collection for real server port;"
        required: False
    health_check_follow_port:
        description:
        - "Specify which port to follow for health status (Port Number)"
        required: False
    template_port:
        description:
        - "Port template (Port template name)"
        required: False
    conn_limit:
        description:
        - "Connection Limit"
        required: False
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            es_resp_invalid_http:
                description:
                - "Total non-http response"
            curr_req:
                description:
                - "Current requests"
            protocol:
                description:
                - "'tcp'= TCP Port; 'udp'= UDP Port;"
            total_rev_pkts_inspected_good_status_code:
                description:
                - "Total reverse packets with good status code inspected"
            resp_1xx:
                description:
                - "Response status 1xx"
            curr_ssl_conn:
                description:
                - "Current SSL connections"
            resp_2xx:
                description:
                - "Response status 2xx"
            es_resp_count:
                description:
                - "Total proxy response"
            total_fwd_bytes:
                description:
                - "Bytes processed in forward direction"
            es_resp_other:
                description:
                - "Response status other"
            fastest_rsp_time:
                description:
                - "Fastest response time"
            total_fwd_pkts:
                description:
                - "Packets processed in forward direction"
            resp_3xx:
                description:
                - "Response status 3xx"
            resp_latency:
                description:
                - "Time to First Response Byte"
            resp_count:
                description:
                - "Total Response Count"
            es_req_count:
                description:
                - "Total proxy requests"
            resp_other:
                description:
                - "Response status Other"
            es_resp_500:
                description:
                - "Response status 500"
            peak_conn:
                description:
                - "Peak connections"
            total_req:
                description:
                - "Total Requests"
            es_resp_400:
                description:
                - "Response status 400"
            es_resp_300:
                description:
                - "Response status 300"
            curr_pconn:
                description:
                - "Current persistent connections"
            curr_conn:
                description:
                - "Current connections"
            port_number:
                description:
                - "Port Number"
            es_resp_200:
                description:
                - "Response status 200"
            total_rev_bytes:
                description:
                - "Bytes processed in reverse direction"
            response_time:
                description:
                - "Response time"
            resp_4xx:
                description:
                - "Response status 4xx"
            total_ssl_conn:
                description:
                - "Total SSL connections"
            total_conn:
                description:
                - "Total connections"
            total_rev_pkts:
                description:
                - "Packets processed in reverse direction"
            total_req_succ:
                description:
                - "Total requests succ"
            last_total_conn:
                description:
                - "Last total connections"
            total_rev_pkts_inspected:
                description:
                - "Total reverse packets inspected"
            resp_5xx:
                description:
                - "Response status 5xx"
            slowest_rsp_time:
                description:
                - "Slowest response time"
    uuid:
        description:
        - "uuid of the object"
        required: False
    support_http2:
        description:
        - "Starting HTTP/2 with Prior Knowledge"
        required: False
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'curr_req'= Current requests; 'total_req'= Total Requests;
          'total_req_succ'= Total requests succ; 'total_fwd_bytes'= Bytes processed in
          forward direction; 'total_fwd_pkts'= Packets processed in forward direction;
          'total_rev_bytes'= Bytes processed in reverse direction; 'total_rev_pkts'=
          Packets processed in reverse direction; 'total_conn'= Total connections;
          'last_total_conn'= Last total connections; 'peak_conn'= Peak connections;
          'es_resp_200'= Response status 200; 'es_resp_300'= Response status 300;
          'es_resp_400'= Response status 400; 'es_resp_500'= Response status 500;
          'es_resp_other'= Response status other; 'es_req_count'= Total proxy requests;
          'es_resp_count'= Total proxy response; 'es_resp_invalid_http'= Total non-http
          response; 'total_rev_pkts_inspected'= Total reverse packets inspected;
          'total_rev_pkts_inspected_good_status_code'= Total reverse packets with good
          status code inspected; 'response_time'= Response time; 'fastest_rsp_time'=
          Fastest response time; 'slowest_rsp_time'= Slowest response time;
          'curr_ssl_conn'= Current SSL connections; 'total_ssl_conn'= Total SSL
          connections; 'resp-count'= Total Response Count; 'resp-1xx'= Response status
          1xx; 'resp-2xx'= Response status 2xx; 'resp-3xx'= Response status 3xx; 'resp-
          4xx'= Response status 4xx; 'resp-5xx'= Response status 5xx; 'resp-other'=
          Response status Other; 'resp-latency'= Time to First Response Byte;
          'curr_pconn'= Current persistent connections;"
    no_ssl:
        description:
        - "No SSL"
        required: False
    follow_port_protocol:
        description:
        - "'tcp'= TCP Port; 'udp'= UDP Port;"
        required: False
    template_server_ssl:
        description:
        - "Server side SSL template (Server side SSL Name)"
        required: False
    alternate_port:
        description:
        - "Field alternate_port"
        required: False
        suboptions:
            alternate_name:
                description:
                - "Alternate Name"
            alternate:
                description:
                - "Alternate Server Number"
            alternate_server_port:
                description:
                - "Port (Alternate Server Port Value)"
    port_number:
        description:
        - "Port Number"
        required: True
    extended_stats:
        description:
        - "Enable extended statistics on real server port"
        required: False
    rport_health_check_shared:
        description:
        - "Health Check (Monitor Name)"
        required: False
    conn_resume:
        description:
        - "Connection Resume"
        required: False
    user_tag:
        description:
        - "Customized tag"
        required: False
    range:
        description:
        - "Port range (Port range value - used for vip-to-rport-mapping and vport-rport
          range mapping)"
        required: False
    auth_cfg:
        description:
        - "Field auth_cfg"
        required: False
        suboptions:
            service_principal_name:
                description:
                - "Service Principal Name (Kerberos principal name)"
    action:
        description:
        - "'enable'= enable; 'disable'= disable; 'disable-with-health-check'= disable
          port, but health check work;"
        required: False
    health_check:
        description:
        - "Health Check (Monitor Name)"
        required: False
    no_logging:
        description:
        - "Do not log connection over limit event"
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
    "action",
    "alternate_port",
    "auth_cfg",
    "conn_limit",
    "conn_resume",
    "extended_stats",
    "follow_port_protocol",
    "health_check",
    "health_check_disable",
    "health_check_follow_port",
    "no_logging",
    "no_ssl",
    "oper",
    "port_number",
    "protocol",
    "range",
    "rport_health_check_shared",
    "sampling_enable",
    "shared_rport_health_check",
    "stats",
    "stats_data_action",
    "support_http2",
    "template_port",
    "template_server_ssl",
    "user_tag",
    "uuid",
    "weight",
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
        'oper': {
            'type': 'dict',
            'down_grace_period_allowed': {
                'type': 'int',
            },
            'protocol': {
                'type': 'str',
                'required': True,
                'choices': ['tcp', 'udp']
            },
            'ip': {
                'type': 'str',
            },
            'ports_freed_total': {
                'type': 'int',
            },
            'ports_consumed_total': {
                'type': 'int',
            },
            'aflow_queue_size': {
                'type': 'int',
            },
            'current_time': {
                'type': 'int',
            },
            'alloc_failed': {
                'type': 'int',
            },
            'vrid': {
                'type': 'int',
            },
            'state': {
                'type':
                'str',
                'choices': [
                    'Up', 'Down', 'Disabled', 'Maintenance', 'Unknown',
                    'DIS-UP', 'DIS-DOWN', 'DIS-MAINTENANCE', 'DIS-EXCEED-RATE',
                    'DIS-DAMP'
                ]
            },
            'ipv6': {
                'type': 'str',
            },
            'slow_start_conn_limit': {
                'type': 'int',
            },
            'resv_conn': {
                'type': 'int',
            },
            'hm_index': {
                'type': 'int',
            },
            'down_time_grace_period': {
                'type': 'int',
            },
            'inband_hm_reassign_num': {
                'type': 'int',
            },
            'ports_consumed': {
                'type': 'int',
            },
            'port_number': {
                'type': 'int',
                'required': True,
            },
            'curr_observe_rate': {
                'type': 'int',
            },
            'curr_conn_rate': {
                'type': 'int',
            },
            'disable': {
                'type': 'int',
            },
            'aflow_conn_limit': {
                'type': 'int',
            },
            'diameter_enabled': {
                'type': 'int',
            },
            'soft_down_time': {
                'type': 'int',
            },
            'ha_group_id': {
                'type': 'int',
            },
            'hm_key': {
                'type': 'int',
            },
            'es_resp_time': {
                'type': 'int',
            },
            'conn_rate_unit': {
                'type': 'str',
            }
        },
        'health_check_disable': {
            'type': 'bool',
        },
        'protocol': {
            'type': 'str',
            'required': True,
            'choices': ['tcp', 'udp']
        },
        'weight': {
            'type': 'int',
        },
        'shared_rport_health_check': {
            'type': 'bool',
        },
        'stats_data_action': {
            'type': 'str',
            'choices': ['stats-data-enable', 'stats-data-disable']
        },
        'health_check_follow_port': {
            'type': 'int',
        },
        'template_port': {
            'type': 'str',
        },
        'conn_limit': {
            'type': 'int',
        },
        'stats': {
            'type': 'dict',
            'es_resp_invalid_http': {
                'type': 'str',
            },
            'curr_req': {
                'type': 'str',
            },
            'protocol': {
                'type': 'str',
                'required': True,
                'choices': ['tcp', 'udp']
            },
            'total_rev_pkts_inspected_good_status_code': {
                'type': 'str',
            },
            'resp_1xx': {
                'type': 'str',
            },
            'curr_ssl_conn': {
                'type': 'str',
            },
            'resp_2xx': {
                'type': 'str',
            },
            'es_resp_count': {
                'type': 'str',
            },
            'total_fwd_bytes': {
                'type': 'str',
            },
            'es_resp_other': {
                'type': 'str',
            },
            'fastest_rsp_time': {
                'type': 'str',
            },
            'total_fwd_pkts': {
                'type': 'str',
            },
            'resp_3xx': {
                'type': 'str',
            },
            'resp_latency': {
                'type': 'str',
            },
            'resp_count': {
                'type': 'str',
            },
            'es_req_count': {
                'type': 'str',
            },
            'resp_other': {
                'type': 'str',
            },
            'es_resp_500': {
                'type': 'str',
            },
            'peak_conn': {
                'type': 'str',
            },
            'total_req': {
                'type': 'str',
            },
            'es_resp_400': {
                'type': 'str',
            },
            'es_resp_300': {
                'type': 'str',
            },
            'curr_pconn': {
                'type': 'str',
            },
            'curr_conn': {
                'type': 'str',
            },
            'port_number': {
                'type': 'int',
                'required': True,
            },
            'es_resp_200': {
                'type': 'str',
            },
            'total_rev_bytes': {
                'type': 'str',
            },
            'response_time': {
                'type': 'str',
            },
            'resp_4xx': {
                'type': 'str',
            },
            'total_ssl_conn': {
                'type': 'str',
            },
            'total_conn': {
                'type': 'str',
            },
            'total_rev_pkts': {
                'type': 'str',
            },
            'total_req_succ': {
                'type': 'str',
            },
            'last_total_conn': {
                'type': 'str',
            },
            'total_rev_pkts_inspected': {
                'type': 'str',
            },
            'resp_5xx': {
                'type': 'str',
            },
            'slowest_rsp_time': {
                'type': 'str',
            }
        },
        'uuid': {
            'type': 'str',
        },
        'support_http2': {
            'type': 'bool',
        },
        'sampling_enable': {
            'type': 'list',
            'counters1': {
                'type':
                'str',
                'choices': [
                    'all', 'curr_req', 'total_req', 'total_req_succ',
                    'total_fwd_bytes', 'total_fwd_pkts', 'total_rev_bytes',
                    'total_rev_pkts', 'total_conn', 'last_total_conn',
                    'peak_conn', 'es_resp_200', 'es_resp_300', 'es_resp_400',
                    'es_resp_500', 'es_resp_other', 'es_req_count',
                    'es_resp_count', 'es_resp_invalid_http',
                    'total_rev_pkts_inspected',
                    'total_rev_pkts_inspected_good_status_code',
                    'response_time', 'fastest_rsp_time', 'slowest_rsp_time',
                    'curr_ssl_conn', 'total_ssl_conn', 'resp-count',
                    'resp-1xx', 'resp-2xx', 'resp-3xx', 'resp-4xx', 'resp-5xx',
                    'resp-other', 'resp-latency', 'curr_pconn'
                ]
            }
        },
        'no_ssl': {
            'type': 'bool',
        },
        'follow_port_protocol': {
            'type': 'str',
            'choices': ['tcp', 'udp']
        },
        'template_server_ssl': {
            'type': 'str',
        },
        'alternate_port': {
            'type': 'list',
            'alternate_name': {
                'type': 'str',
            },
            'alternate': {
                'type': 'int',
            },
            'alternate_server_port': {
                'type': 'int',
            }
        },
        'port_number': {
            'type': 'int',
            'required': True,
        },
        'extended_stats': {
            'type': 'bool',
        },
        'rport_health_check_shared': {
            'type': 'str',
        },
        'conn_resume': {
            'type': 'int',
        },
        'user_tag': {
            'type': 'str',
        },
        'range': {
            'type': 'int',
        },
        'auth_cfg': {
            'type': 'dict',
            'service_principal_name': {
                'type': 'str',
            }
        },
        'action': {
            'type': 'str',
            'choices': ['enable', 'disable', 'disable-with-health-check']
        },
        'health_check': {
            'type': 'str',
        },
        'no_logging': {
            'type': 'bool',
        }
    })
    # Parent keys
    rv.update(dict(server_name=dict(type='str', required=True), ))
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/server/{server_name}/port/{port-number}+{protocol}"

    f_dict = {}
    f_dict["port-number"] = module.params["port_number"]
    f_dict["protocol"] = module.params["protocol"]
    f_dict["server_name"] = module.params["server_name"]

    return url_base.format(**f_dict)


def oper_url(module):
    """Return the URL for operational data of an existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/oper"


def stats_url(module):
    """Return the URL for statistical data of and existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/stats"


def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]


def get(module):
    return module.client.get(existing_url(module))


def get_list(module):
    return module.client.get(list_url(module))


def get_oper(module):
    if module.params.get("oper"):
        query_params = {}
        for k, v in module.params["oper"].items():
            query_params[k.replace('_', '-')] = v
        return module.client.get(oper_url(module), params=query_params)
    return module.client.get(oper_url(module))


def get_stats(module):
    if module.params.get("stats"):
        query_params = {}
        for k, v in module.params["stats"].items():
            query_params[k.replace('_', '-')] = v
        return module.client.get(stats_url(module), params=query_params)
    return module.client.get(stats_url(module))


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
    url_base = "/axapi/v3/slb/server/{server_name}/port/{port-number}+{protocol}"

    f_dict = {}
    f_dict["port-number"] = ""
    f_dict["protocol"] = ""
    f_dict["server_name"] = module.params["server_name"]

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
        for k, v in payload["port"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["port"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["port"][k] = v
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
    payload = build_json("port", module)
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
        elif module.params.get("get_type") == "oper":
            result["result"] = get_oper(module)
        elif module.params.get("get_type") == "stats":
            result["result"] = get_stats(module)
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
