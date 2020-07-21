#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_slb_dns_response_rate_limiting
description:
    - Configure DNS Response-Rate-Limiting
short_description: Configures A10 slb.dns-response-rate-limiting
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
    oper:
        description:
        - "Field oper"
        required: False
        suboptions:
            dnsrrl_cpu_list:
                description:
                - "Field dnsrrl_cpu_list"
            cpu_count:
                description:
                - "Field cpu_count"
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'curr_entries'= Current Entry Count; 'total_created'= Total Entry
          Created; 'total_inserted'= Total Entry Inserted; 'total_withdrew'= Total Entry
          Withdrew; 'total_ready_to_free'= Total Entry Ready To Free; 'total_freed'=
          Total Entry Freed; 'total_logs'= Total Logs; 'total_overflow_entry_hits'= Total
          Overflow Entry Hits; 'total_refill'= Total Refills; 'total_credit_exceeded'=
          Total Credit Exceeded; 'other_thread_refill'= Other Thread Refilling;
          'err_entry_create_failed'= Entry Creation Failure; 'err_entry_create_oom'=
          Entry Creation Out of Memory; 'err_entry_ext_create_oom'= Entry Extension
          Creation Out of Memory; 'err_entry_insert_failed'= Entry Insert Failed;
          'err_vport_fail_match'= Failed to Match Vport;"
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            total_ready_to_free:
                description:
                - "Total Entry Ready To Free"
            total_withdrew:
                description:
                - "Total Entry Withdrew"
            curr_entries:
                description:
                - "Current Entry Count"
            total_logs:
                description:
                - "Total Logs"
            err_entry_create_oom:
                description:
                - "Entry Creation Out of Memory"
            total_credit_exceeded:
                description:
                - "Total Credit Exceeded"
            err_vport_fail_match:
                description:
                - "Failed to Match Vport"
            total_freed:
                description:
                - "Total Entry Freed"
            total_inserted:
                description:
                - "Total Entry Inserted"
            total_refill:
                description:
                - "Total Refills"
            total_overflow_entry_hits:
                description:
                - "Total Overflow Entry Hits"
            other_thread_refill:
                description:
                - "Other Thread Refilling"
            total_created:
                description:
                - "Total Entry Created"
            err_entry_ext_create_oom:
                description:
                - "Entry Extension Creation Out of Memory"
            err_entry_create_failed:
                description:
                - "Entry Creation Failure"
            err_entry_insert_failed:
                description:
                - "Entry Insert Failed"
    uuid:
        description:
        - "uuid of the object"
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
    "oper",
    "sampling_enable",
    "stats",
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
        'oper': {
            'type': 'dict',
            'dnsrrl_cpu_list': {
                'type': 'list',
                'total_ready_to_free': {
                    'type': 'int',
                },
                'total_withdrew': {
                    'type': 'int',
                },
                'total_logs': {
                    'type': 'int',
                },
                'err_entry_create_oom': {
                    'type': 'int',
                },
                'total_credit_exceeded': {
                    'type': 'int',
                },
                'err_vport_fail_match': {
                    'type': 'int',
                },
                'total_freed': {
                    'type': 'int',
                },
                'total_inserted': {
                    'type': 'int',
                },
                'total_refill': {
                    'type': 'int',
                },
                'total_overflow_entry_hits': {
                    'type': 'int',
                },
                'other_thread_refill': {
                    'type': 'int',
                },
                'err_entry_insert_failed': {
                    'type': 'int',
                },
                'err_entry_ext_create_oom': {
                    'type': 'int',
                },
                'err_entry_create_failed': {
                    'type': 'int',
                },
                'total_created': {
                    'type': 'int',
                }
            },
            'cpu_count': {
                'type': 'int',
            }
        },
        'sampling_enable': {
            'type': 'list',
            'counters1': {
                'type':
                'str',
                'choices': [
                    'all', 'curr_entries', 'total_created', 'total_inserted',
                    'total_withdrew', 'total_ready_to_free', 'total_freed',
                    'total_logs', 'total_overflow_entry_hits', 'total_refill',
                    'total_credit_exceeded', 'other_thread_refill',
                    'err_entry_create_failed', 'err_entry_create_oom',
                    'err_entry_ext_create_oom', 'err_entry_insert_failed',
                    'err_vport_fail_match'
                ]
            }
        },
        'stats': {
            'type': 'dict',
            'total_ready_to_free': {
                'type': 'str',
            },
            'total_withdrew': {
                'type': 'str',
            },
            'curr_entries': {
                'type': 'str',
            },
            'total_logs': {
                'type': 'str',
            },
            'err_entry_create_oom': {
                'type': 'str',
            },
            'total_credit_exceeded': {
                'type': 'str',
            },
            'err_vport_fail_match': {
                'type': 'str',
            },
            'total_freed': {
                'type': 'str',
            },
            'total_inserted': {
                'type': 'str',
            },
            'total_refill': {
                'type': 'str',
            },
            'total_overflow_entry_hits': {
                'type': 'str',
            },
            'other_thread_refill': {
                'type': 'str',
            },
            'total_created': {
                'type': 'str',
            },
            'err_entry_ext_create_oom': {
                'type': 'str',
            },
            'err_entry_create_failed': {
                'type': 'str',
            },
            'err_entry_insert_failed': {
                'type': 'str',
            }
        },
        'uuid': {
            'type': 'str',
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/dns-response-rate-limiting"

    f_dict = {}

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
    url_base = "/axapi/v3/slb/dns-response-rate-limiting"

    f_dict = {}

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
        for k, v in payload["dns-response-rate-limiting"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["dns-response-rate-limiting"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["dns-response-rate-limiting"][k] = v
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
    payload = build_json("dns-response-rate-limiting", module)
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
