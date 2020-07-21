#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_ip_access_list
description:
    - Configure Access List
short_description: Configures A10 ip.access-list
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
    rules:
        description:
        - "Field rules"
        required: False
        suboptions:
            geo_location:
                description:
                - "Specify geo-location name"
            icmp_type:
                description:
                - "ICMP type number"
            ip:
                description:
                - "Any Internet Protocol"
            service_obj_group:
                description:
                - "Service object group (Source object group name)"
            udp:
                description:
                - "protocol UDP"
            tcp:
                description:
                - "protocol TCP"
            src_range:
                description:
                - "match only packets in the range of port numbers (Starting Port Number)"
            any_code:
                description:
                - "Any ICMP code"
            src_lt:
                description:
                - "Match only packets with a lower port number"
            src_mask:
                description:
                - "Source Mask 0=apply 255=ignore"
            src_port_end:
                description:
                - "Ending Port Number"
            dst_port_end:
                description:
                - "Edning Destination Port Number"
            dst_range:
                description:
                - "Match only packets in the range of port numbers (Starting Destination Port
          Number)"
            established:
                description:
                - "TCP established"
            src_subnet:
                description:
                - "Source Address"
            seq_num:
                description:
                - "Sequence Number"
            src_any:
                description:
                - "Any source host"
            fragments:
                description:
                - "IP fragments"
            icmp_code:
                description:
                - "ICMP code number"
            src_object_group:
                description:
                - "Network object group (Source network object group name)"
            dst_eq:
                description:
                - "Match only packets on a given destination port (port number)"
            dst_subnet:
                description:
                - "Destination Address"
            dst_mask:
                description:
                - "Destination Mask 0=apply 255=ignore"
            vlan:
                description:
                - "VLAN ID"
            dscp:
                description:
                - "DSCP"
            special_code:
                description:
                - "'frag-required'= Code 4, fragmentation required; 'host-unreachable'= Code 1,
          destination host unreachable; 'network-unreachable'= Code 0, destination
          network unreachable; 'port-unreachable'= Code 3, destination port unreachable;
          'proto-unreachable'= Code 2, destination protocol unreachable; 'route-failed'=
          Code 5, source route failed;"
            action:
                description:
                - "'deny'= Deny; 'permit'= Permit; 'l3-vlan-fwd-disable'= Disable L3 forwarding
          between VLANs;"
            trunk:
                description:
                - "Ethernet trunk (trunk number)"
            icmp:
                description:
                - "Internet Control Message Protocol"
            dst_gt:
                description:
                - "Match only packets with a greater port number"
            acl_log:
                description:
                - "Log matches against this entry"
            src_gt:
                description:
                - "Match only packets with a greater port number"
            remark:
                description:
                - "Access list entry comment (Notes for this ACL)"
            dst_object_group:
                description:
                - "Destination network object group name"
            any_type:
                description:
                - "Any ICMP type"
            transparent_session_only:
                description:
                - "Only log transparent sessions"
            dst_any:
                description:
                - "Any destination host"
            src_host:
                description:
                - "A single source host (Host address)"
            dst_lt:
                description:
                - "Match only packets with a lesser port number"
            ethernet:
                description:
                - "Ethernet interface (Port number)"
            special_type:
                description:
                - "'echo-reply'= Type 0, echo reply; 'echo-request'= Type 8, echo request; 'info-
          reply'= Type 16, information reply; 'info-request'= Type 15, information
          request; 'mask-reply'= Type 18, address mask reply; 'mask-request'= Type 17,
          address mask request; 'parameter-problem'= Type 12, parameter problem;
          'redirect'= Type 5, redirect message; 'source-quench'= Type 4, source quench;
          'time-exceeded'= Type 11, time exceeded; 'timestamp'= Type 13, timestamp;
          'timestamp-reply'= Type 14, timestamp reply; 'dest-unreachable'= Type 3,
          destination unreachable;"
            src_eq:
                description:
                - "Match only packets on a given source port (port number)"
            dst_host:
                description:
                - "A single destination host (Host address)"
    name:
        description:
        - "IP Access List Name. Does not support name as digits or start with digit."
        required: True
    user_tag:
        description:
        - "Customized tag"
        required: False
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
    "name",
    "rules",
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
        'rules': {
            'type': 'list',
            'geo_location': {
                'type': 'str',
            },
            'icmp_type': {
                'type': 'int',
            },
            'ip': {
                'type': 'bool',
            },
            'service_obj_group': {
                'type': 'str',
            },
            'udp': {
                'type': 'bool',
            },
            'tcp': {
                'type': 'bool',
            },
            'src_range': {
                'type': 'int',
            },
            'any_code': {
                'type': 'bool',
            },
            'src_lt': {
                'type': 'int',
            },
            'src_mask': {
                'type': 'str',
            },
            'src_port_end': {
                'type': 'int',
            },
            'dst_port_end': {
                'type': 'int',
            },
            'dst_range': {
                'type': 'int',
            },
            'established': {
                'type': 'bool',
            },
            'src_subnet': {
                'type': 'str',
            },
            'seq_num': {
                'type': 'int',
            },
            'src_any': {
                'type': 'bool',
            },
            'fragments': {
                'type': 'bool',
            },
            'icmp_code': {
                'type': 'int',
            },
            'src_object_group': {
                'type': 'str',
            },
            'dst_eq': {
                'type': 'int',
            },
            'dst_subnet': {
                'type': 'str',
            },
            'dst_mask': {
                'type': 'str',
            },
            'vlan': {
                'type': 'int',
            },
            'dscp': {
                'type': 'int',
            },
            'special_code': {
                'type':
                'str',
                'choices': [
                    'frag-required', 'host-unreachable', 'network-unreachable',
                    'port-unreachable', 'proto-unreachable', 'route-failed'
                ]
            },
            'action': {
                'type': 'str',
                'choices': ['deny', 'permit', 'l3-vlan-fwd-disable']
            },
            'trunk': {
                'type': 'str',
            },
            'icmp': {
                'type': 'bool',
            },
            'dst_gt': {
                'type': 'int',
            },
            'acl_log': {
                'type': 'bool',
            },
            'src_gt': {
                'type': 'int',
            },
            'remark': {
                'type': 'str',
            },
            'dst_object_group': {
                'type': 'str',
            },
            'any_type': {
                'type': 'bool',
            },
            'transparent_session_only': {
                'type': 'bool',
            },
            'dst_any': {
                'type': 'bool',
            },
            'src_host': {
                'type': 'str',
            },
            'dst_lt': {
                'type': 'int',
            },
            'ethernet': {
                'type': 'str',
            },
            'special_type': {
                'type':
                'str',
                'choices': [
                    'echo-reply', 'echo-request', 'info-reply', 'info-request',
                    'mask-reply', 'mask-request', 'parameter-problem',
                    'redirect', 'source-quench', 'time-exceeded', 'timestamp',
                    'timestamp-reply', 'dest-unreachable'
                ]
            },
            'src_eq': {
                'type': 'int',
            },
            'dst_host': {
                'type': 'str',
            }
        },
        'name': {
            'type': 'str',
            'required': True,
        },
        'user_tag': {
            'type': 'str',
        },
        'uuid': {
            'type': 'str',
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/ip/access-list/{name}"

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
    url_base = "/axapi/v3/ip/access-list/{name}"

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
        for k, v in payload["access-list"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["access-list"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["access-list"][k] = v
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
    payload = build_json("access-list", module)
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
