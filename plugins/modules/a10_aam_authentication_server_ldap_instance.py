#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_aam_authentication_server_ldap_instance
description:
    - LDAP Authentication Server
short_description: Configures A10 aam.authentication.server.ldap.instance
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
    health_check_disable:
        description:
        - "Disable configured health check configuration"
        required: False
    protocol:
        description:
        - "'ldap'= Use LDAP (default); 'ldaps'= Use LDAP over SSL; 'starttls'= Use LDAP
          StartTLS;"
        required: False
    encrypted:
        description:
        - "Do NOT use this option manually. (This is an A10 reserved keyword.) (The
          ENCRYPTED secret string)"
        required: False
    port:
        description:
        - "Specify the LDAP server's authentication port, default is 389"
        required: False
    ldaps_conn_reuse_idle_timeout:
        description:
        - "Specify LDAPS connection reuse idle timeout value (in seconds) (Specify idle
          timeout value (in seconds), default is 0 (not reuse LDAPS connection))"
        required: False
    port_hm:
        description:
        - "Check port's health status"
        required: False
    uuid:
        description:
        - "uuid of the object"
        required: False
    admin_dn:
        description:
        - "The LDAP server's admin DN"
        required: False
    default_domain:
        description:
        - "Specify default domain for LDAP"
        required: False
    auth_type:
        description:
        - "'ad'= Active Directory. Default; 'open-ldap'= OpenLDAP;"
        required: False
    admin_secret:
        description:
        - "Specify the LDAP server's admin secret password"
        required: False
    pwdmaxage:
        description:
        - "Specify the LDAP server's default password expiration time (in seconds) (The
          LDAP server's default password expiration time (in seconds), default is 0 (no
          expiration))"
        required: False
    health_check_string:
        description:
        - "Health monitor name"
        required: False
    derive_bind_dn:
        description:
        - "Field derive_bind_dn"
        required: False
        suboptions:
            username_attr:
                description:
                - "Specify attribute name of username"
    prompt_pw_change_before_exp:
        description:
        - "Prompt user to change password before expiration in N days. This option only
          takes effect when server type is AD (Prompt user to change password before
          expiration in N days, default is not to prompt the user)"
        required: False
    base:
        description:
        - "Specify the LDAP server's search base"
        required: False
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            bind_failure:
                description:
                - "User Bind Failure"
            authorize_failure:
                description:
                - "Authorization Failure"
            admin_bind_failure:
                description:
                - "Admin Bind Failure"
            search_failure:
                description:
                - "Search Failure"
            authorize_success:
                description:
                - "Authorization Success"
            pw_change_success:
                description:
                - "Password change success"
            timeout_error:
                description:
                - "Timeout"
            request:
                description:
                - "Request"
            pw_expiry:
                description:
                - "Password expiry"
            name:
                description:
                - "Specify LDAP authentication server name"
            admin_bind_success:
                description:
                - "Admin Bind Success"
            search_success:
                description:
                - "Search Success"
            other_error:
                description:
                - "Other Error"
            ssl_session_created:
                description:
                - "TLS/SSL Session Created"
            pw_change_failure:
                description:
                - "Password change failure"
            ssl_session_failure:
                description:
                - "TLS/SSL Session Failure"
            bind_success:
                description:
                - "User Bind Success"
    secret_string:
        description:
        - "secret password"
        required: False
    name:
        description:
        - "Specify LDAP authentication server name"
        required: True
    port_hm_disable:
        description:
        - "Disable configured port health check configuration"
        required: False
    host:
        description:
        - "Field host"
        required: False
        suboptions:
            hostipv6:
                description:
                - "Server's IPV6 address"
            hostip:
                description:
                - "Server's hostname(Length 1-31) or IP address"
    ca_cert:
        description:
        - "Specify the LDAPS CA cert filename (Trusted LDAPS CA cert filename)"
        required: False
    bind_with_dn:
        description:
        - "Enforce using DN for LDAP binding(All user input name will be used to create
          DN)"
        required: False
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'admin-bind-success'= Admin Bind Success; 'admin-bind-failure'=
          Admin Bind Failure; 'bind-success'= User Bind Success; 'bind-failure'= User
          Bind Failure; 'search-success'= Search Success; 'search-failure'= Search
          Failure; 'authorize-success'= Authorization Success; 'authorize-failure'=
          Authorization Failure; 'timeout-error'= Timeout; 'other-error'= Other Error;
          'request'= Request; 'ssl-session-created'= TLS/SSL Session Created; 'ssl-
          session-failure'= TLS/SSL Session Failure; 'pw_expiry'= Password expiry;
          'pw_change_success'= Password change success; 'pw_change_failure'= Password
          change failure;"
    dn_attribute:
        description:
        - "Specify Distinguished Name attribute, default is CN"
        required: False
    timeout:
        description:
        - "Specify timout for LDAP, default is 10 seconds (The timeout, default is 10
          seconds)"
        required: False
    health_check:
        description:
        - "Check server's health status"
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
    "admin_dn",
    "admin_secret",
    "auth_type",
    "base",
    "bind_with_dn",
    "ca_cert",
    "default_domain",
    "derive_bind_dn",
    "dn_attribute",
    "encrypted",
    "health_check",
    "health_check_disable",
    "health_check_string",
    "host",
    "ldaps_conn_reuse_idle_timeout",
    "name",
    "port",
    "port_hm",
    "port_hm_disable",
    "prompt_pw_change_before_exp",
    "protocol",
    "pwdmaxage",
    "sampling_enable",
    "secret_string",
    "stats",
    "timeout",
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
        'health_check_disable': {
            'type': 'bool',
        },
        'protocol': {
            'type': 'str',
            'choices': ['ldap', 'ldaps', 'starttls']
        },
        'encrypted': {
            'type': 'str',
        },
        'port': {
            'type': 'int',
        },
        'ldaps_conn_reuse_idle_timeout': {
            'type': 'int',
        },
        'port_hm': {
            'type': 'str',
        },
        'uuid': {
            'type': 'str',
        },
        'admin_dn': {
            'type': 'str',
        },
        'default_domain': {
            'type': 'str',
        },
        'auth_type': {
            'type': 'str',
            'choices': ['ad', 'open-ldap']
        },
        'admin_secret': {
            'type': 'bool',
        },
        'pwdmaxage': {
            'type': 'int',
        },
        'health_check_string': {
            'type': 'str',
        },
        'derive_bind_dn': {
            'type': 'dict',
            'username_attr': {
                'type': 'str',
            }
        },
        'prompt_pw_change_before_exp': {
            'type': 'int',
        },
        'base': {
            'type': 'str',
        },
        'stats': {
            'type': 'dict',
            'bind_failure': {
                'type': 'str',
            },
            'authorize_failure': {
                'type': 'str',
            },
            'admin_bind_failure': {
                'type': 'str',
            },
            'search_failure': {
                'type': 'str',
            },
            'authorize_success': {
                'type': 'str',
            },
            'pw_change_success': {
                'type': 'str',
            },
            'timeout_error': {
                'type': 'str',
            },
            'request': {
                'type': 'str',
            },
            'pw_expiry': {
                'type': 'str',
            },
            'name': {
                'type': 'str',
                'required': True,
            },
            'admin_bind_success': {
                'type': 'str',
            },
            'search_success': {
                'type': 'str',
            },
            'other_error': {
                'type': 'str',
            },
            'ssl_session_created': {
                'type': 'str',
            },
            'pw_change_failure': {
                'type': 'str',
            },
            'ssl_session_failure': {
                'type': 'str',
            },
            'bind_success': {
                'type': 'str',
            }
        },
        'secret_string': {
            'type': 'str',
        },
        'name': {
            'type': 'str',
            'required': True,
        },
        'port_hm_disable': {
            'type': 'bool',
        },
        'host': {
            'type': 'dict',
            'hostipv6': {
                'type': 'str',
            },
            'hostip': {
                'type': 'str',
            }
        },
        'ca_cert': {
            'type': 'str',
        },
        'bind_with_dn': {
            'type': 'bool',
        },
        'sampling_enable': {
            'type': 'list',
            'counters1': {
                'type':
                'str',
                'choices': [
                    'all', 'admin-bind-success', 'admin-bind-failure',
                    'bind-success', 'bind-failure', 'search-success',
                    'search-failure', 'authorize-success', 'authorize-failure',
                    'timeout-error', 'other-error', 'request',
                    'ssl-session-created', 'ssl-session-failure', 'pw_expiry',
                    'pw_change_success', 'pw_change_failure'
                ]
            }
        },
        'dn_attribute': {
            'type': 'str',
        },
        'timeout': {
            'type': 'int',
        },
        'health_check': {
            'type': 'bool',
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authentication/server/ldap/instance/{name}"

    f_dict = {}
    f_dict["name"] = module.params["name"]

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
    url_base = "/axapi/v3/aam/authentication/server/ldap/instance/{name}"

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
        for k, v in payload["instance"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["instance"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["instance"][k] = v
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
    payload = build_json("instance", module)
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
