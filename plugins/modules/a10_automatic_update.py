#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_automatic_update
description:
    - Automatic update configuration
short_description: Configures A10 automatic-update
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
    info:
        description:
        - "Field info"
        required: False
        suboptions:
            uuid:
                description:
                - "uuid of the object"
    reset:
        description:
        - "Field reset"
        required: False
        suboptions:
            feature_name:
                description:
                - "'app-fw'= Application Firewall;"
    uuid:
        description:
        - "uuid of the object"
        required: False
    use_mgmt_port:
        description:
        - "Use management port to connect"
        required: False
    checknow:
        description:
        - "Field checknow"
        required: False
        suboptions:
            uuid:
                description:
                - "uuid of the object"
    revert:
        description:
        - "Field revert"
        required: False
        suboptions:
            feature_name:
                description:
                - "'app-fw'= Application Firewall;"
    proxy_server:
        description:
        - "Field proxy_server"
        required: False
        suboptions:
            username:
                description:
                - "Username for proxy authentication"
            domain:
                description:
                - "Realm for NTLM authentication"
            uuid:
                description:
                - "uuid of the object"
            https_port:
                description:
                - "Proxy server HTTPs port"
            encrypted:
                description:
                - "Do NOT use this option manually. (This is an A10 reserved keyword.) (The
          ENCRYPTED secret string)"
            proxy_host:
                description:
                - "Proxy server hostname or IP address"
            auth_type:
                description:
                - "'ntlm'= NTLM authentication(default); 'basic'= Basic authentication;"
            password:
                description:
                - "Password for proxy authentication"
            secret_string:
                description:
                - "password value"
    check_now:
        description:
        - "Field check_now"
        required: False
        suboptions:
            feature_name:
                description:
                - "'app-fw'= Application Firewall;"
    config_list:
        description:
        - "Field config_list"
        required: False
        suboptions:
            day_time:
                description:
                - "Time of day to update (hh=mm) in 24 hour local time"
            uuid:
                description:
                - "uuid of the object"
            schedule:
                description:
                - "Field schedule"
            feature_name:
                description:
                - "'app-fw'= Application Firewall Configuration;"
            week_day:
                description:
                - "'Monday'= Monday; 'Tuesday'= Tuesday; 'Wednesday'= Wednesday; 'Thursday'=
          Thursday; 'Friday'= Friday; 'Saturday'= Saturday; 'Sunday'= Sunday;"
            daily:
                description:
                - "Every day"
            week_time:
                description:
                - "Time of day to update (hh=mm) in 24 hour local time"
            weekly:
                description:
                - "Every week"


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
    "check_now",
    "checknow",
    "config_list",
    "info",
    "proxy_server",
    "reset",
    "revert",
    "use_mgmt_port",
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
        'info': {
            'type': 'dict',
            'uuid': {
                'type': 'str',
            }
        },
        'reset': {
            'type': 'dict',
            'feature_name': {
                'type': 'str',
                'choices': ['app-fw']
            }
        },
        'uuid': {
            'type': 'str',
        },
        'use_mgmt_port': {
            'type': 'bool',
        },
        'checknow': {
            'type': 'dict',
            'uuid': {
                'type': 'str',
            }
        },
        'revert': {
            'type': 'dict',
            'feature_name': {
                'type': 'str',
                'choices': ['app-fw']
            }
        },
        'proxy_server': {
            'type': 'dict',
            'username': {
                'type': 'str',
            },
            'domain': {
                'type': 'str',
            },
            'uuid': {
                'type': 'str',
            },
            'https_port': {
                'type': 'int',
            },
            'encrypted': {
                'type': 'str',
            },
            'proxy_host': {
                'type': 'str',
            },
            'auth_type': {
                'type': 'str',
                'choices': ['ntlm', 'basic']
            },
            'password': {
                'type': 'bool',
            },
            'secret_string': {
                'type': 'str',
            }
        },
        'check_now': {
            'type': 'dict',
            'feature_name': {
                'type': 'str',
                'choices': ['app-fw']
            }
        },
        'config_list': {
            'type': 'list',
            'day_time': {
                'type': 'str',
            },
            'uuid': {
                'type': 'str',
            },
            'schedule': {
                'type': 'bool',
            },
            'feature_name': {
                'type': 'str',
                'required': True,
                'choices': ['app-fw']
            },
            'week_day': {
                'type':
                'str',
                'choices': [
                    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday'
                ]
            },
            'daily': {
                'type': 'bool',
            },
            'week_time': {
                'type': 'str',
            },
            'weekly': {
                'type': 'bool',
            }
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/automatic-update"

    f_dict = {}

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
    url_base = "/axapi/v3/automatic-update"

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
        for k, v in payload["automatic-update"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["automatic-update"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["automatic-update"][k] = v
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
    payload = build_json("automatic-update", module)
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
