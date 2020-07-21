#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_system_hardware_forward
description:
    - Field hardware_forward
short_description: Configures A10 system.hardware-forward
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
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'hit-counts'= Total packts hit counts; 'hit-index'= HW Fwd hit
          index; 'ipv4-forward-counts'= Total IPv4 hardware forwarded packets; 'ipv6
          -forward-counts'= Total IPv6 hardware forwarded packets; 'hw-fwd-module-
          status'= hardware forwarder status flags; 'hw-fwd-prog-reqs'= hardware forward
          programming requests; 'hw-fwd-prog-errors'= hardware forward programming
          Errors; 'hw-fwd-flow-singlebit-errors'= hardware forward singlebit Errors; 'hw-
          fwd-flow-tag-mismatch'= hardware forward tag mismatch errors; 'hw-fwd-flow-seq-
          mismatch'= hardware forward sequence mismatch errors; 'hw-fwd-ageout-drop-
          count'= hardware forward ageout drop count; 'hw-fwd-invalidation-drop'=
          hardware forward invalid drop count; 'hw-fwd-flow-hit-index'= hardware forward
          flow hit index; 'hw-fwd-flow-reason-flags'= hardware forward flow reason flags;
          'hw-fwd-flow-drop-count'= hardware forward flow drop count; 'hw-fwd-flow-error-
          count'= hardware forward flow error count; 'hw-fwd-flow-unalign-count'=
          hardware forward flow unalign count; 'hw-fwd-flow-underflow-count'= hardware
          forward flow underflow count; 'hw-fwd-flow-tx-full-drop'= hardware forward flow
          tx full drop count; 'hw-fwd-flow-qdr-full-drop'= hardware forward flow qdr full
          drop count; 'hw-fwd-phyport-mismatch-drop'= hardware forward phyport mismatch
          count; 'hw-fwd-vlanid-mismatch-drop'= hardware forward vlanid mismatch count;
          'hw-fwd-vmid-drop'= hardware forward vmid mismatch count; 'hw-fwd-protocol-
          mismatch-drop'= hardware forward protocol mismatch count; 'hw-fwd-avail-
          ipv4-entry'= hardware forward available ipv4 entries count; 'hw-fwd-avail-
          ipv6-entry'= hardware forward available ipv6 entries count;"
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            hw_fwd_flow_unalign_count:
                description:
                - "hardware forward flow unalign count"
            hw_fwd_flow_error_count:
                description:
                - "hardware forward flow error count"
            hw_fwd_vmid_drop:
                description:
                - "hardware forward vmid mismatch count"
            hw_fwd_protocol_mismatch_drop:
                description:
                - "hardware forward protocol mismatch count"
            hw_fwd_flow_seq_mismatch:
                description:
                - "hardware forward sequence mismatch errors"
            hw_fwd_flow_drop_count:
                description:
                - "hardware forward flow drop count"
            ipv4_forward_counts:
                description:
                - "Total IPv4 hardware forwarded packets"
            hw_fwd_phyport_mismatch_drop:
                description:
                - "hardware forward phyport mismatch count"
            hw_fwd_invalidation_drop:
                description:
                - "hardware forward invalid drop count"
            ipv6_forward_counts:
                description:
                - "Total IPv6 hardware forwarded packets"
            hw_fwd_flow_hit_index:
                description:
                - "hardware forward flow hit index"
            hw_fwd_flow_tag_mismatch:
                description:
                - "hardware forward tag mismatch errors"
            hw_fwd_ageout_drop_count:
                description:
                - "hardware forward ageout drop count"
            hw_fwd_flow_tx_full_drop:
                description:
                - "hardware forward flow tx full drop count"
            hw_fwd_flow_singlebit_errors:
                description:
                - "hardware forward singlebit Errors"
            hw_fwd_avail_ipv4_entry:
                description:
                - "hardware forward available ipv4 entries count"
            hw_fwd_flow_qdr_full_drop:
                description:
                - "hardware forward flow qdr full drop count"
            hw_fwd_vlanid_mismatch_drop:
                description:
                - "hardware forward vlanid mismatch count"
            hw_fwd_prog_errors:
                description:
                - "hardware forward programming Errors"
            hit_index:
                description:
                - "HW Fwd hit index"
            hw_fwd_prog_reqs:
                description:
                - "hardware forward programming requests"
            hw_fwd_avail_ipv6_entry:
                description:
                - "hardware forward available ipv6 entries count"
            hw_fwd_flow_reason_flags:
                description:
                - "hardware forward flow reason flags"
            hw_fwd_flow_underflow_count:
                description:
                - "hardware forward flow underflow count"
            hw_fwd_module_status:
                description:
                - "hardware forwarder status flags"
            hit_counts:
                description:
                - "Total packts hit counts"
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
        'sampling_enable': {
            'type': 'list',
            'counters1': {
                'type':
                'str',
                'choices': [
                    'all', 'hit-counts', 'hit-index', 'ipv4-forward-counts',
                    'ipv6-forward-counts', 'hw-fwd-module-status',
                    'hw-fwd-prog-reqs', 'hw-fwd-prog-errors',
                    'hw-fwd-flow-singlebit-errors', 'hw-fwd-flow-tag-mismatch',
                    'hw-fwd-flow-seq-mismatch', 'hw-fwd-ageout-drop-count',
                    'hw-fwd-invalidation-drop', 'hw-fwd-flow-hit-index',
                    'hw-fwd-flow-reason-flags', 'hw-fwd-flow-drop-count',
                    'hw-fwd-flow-error-count', 'hw-fwd-flow-unalign-count',
                    'hw-fwd-flow-underflow-count', 'hw-fwd-flow-tx-full-drop',
                    'hw-fwd-flow-qdr-full-drop',
                    'hw-fwd-phyport-mismatch-drop',
                    'hw-fwd-vlanid-mismatch-drop', 'hw-fwd-vmid-drop',
                    'hw-fwd-protocol-mismatch-drop', 'hw-fwd-avail-ipv4-entry',
                    'hw-fwd-avail-ipv6-entry'
                ]
            }
        },
        'stats': {
            'type': 'dict',
            'hw_fwd_flow_unalign_count': {
                'type': 'str',
            },
            'hw_fwd_flow_error_count': {
                'type': 'str',
            },
            'hw_fwd_vmid_drop': {
                'type': 'str',
            },
            'hw_fwd_protocol_mismatch_drop': {
                'type': 'str',
            },
            'hw_fwd_flow_seq_mismatch': {
                'type': 'str',
            },
            'hw_fwd_flow_drop_count': {
                'type': 'str',
            },
            'ipv4_forward_counts': {
                'type': 'str',
            },
            'hw_fwd_phyport_mismatch_drop': {
                'type': 'str',
            },
            'hw_fwd_invalidation_drop': {
                'type': 'str',
            },
            'ipv6_forward_counts': {
                'type': 'str',
            },
            'hw_fwd_flow_hit_index': {
                'type': 'str',
            },
            'hw_fwd_flow_tag_mismatch': {
                'type': 'str',
            },
            'hw_fwd_ageout_drop_count': {
                'type': 'str',
            },
            'hw_fwd_flow_tx_full_drop': {
                'type': 'str',
            },
            'hw_fwd_flow_singlebit_errors': {
                'type': 'str',
            },
            'hw_fwd_avail_ipv4_entry': {
                'type': 'str',
            },
            'hw_fwd_flow_qdr_full_drop': {
                'type': 'str',
            },
            'hw_fwd_vlanid_mismatch_drop': {
                'type': 'str',
            },
            'hw_fwd_prog_errors': {
                'type': 'str',
            },
            'hit_index': {
                'type': 'str',
            },
            'hw_fwd_prog_reqs': {
                'type': 'str',
            },
            'hw_fwd_avail_ipv6_entry': {
                'type': 'str',
            },
            'hw_fwd_flow_reason_flags': {
                'type': 'str',
            },
            'hw_fwd_flow_underflow_count': {
                'type': 'str',
            },
            'hw_fwd_module_status': {
                'type': 'str',
            },
            'hit_counts': {
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
    url_base = "/axapi/v3/system/hardware-forward"

    f_dict = {}

    return url_base.format(**f_dict)


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
    url_base = "/axapi/v3/system/hardware-forward"

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
        for k, v in payload["hardware-forward"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["hardware-forward"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["hardware-forward"][k] = v
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
    payload = build_json("hardware-forward", module)
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
