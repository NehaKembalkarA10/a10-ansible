#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_interface_ethernet
description:
    - Ethernet interface
short_description: Configures A10 interface.ethernet
author: A10 Networks 2018
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
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
            line_protocol:
                description:
                - "Field line_protocol"
            icmp6_rate_over_limit_drop:
                description:
                - "Field icmp6_rate_over_limit_drop"
            outgoing_pkts_mirrored:
                description:
                - "Field outgoing_pkts_mirrored"
            rate_byte_sent:
                description:
                - "Field rate_byte_sent"
            ipv6_link_local_type:
                description:
                - "Field ipv6_link_local_type"
            vlan_id:
                description:
                - "Field vlan_id"
            outgoing_pkts_monitored:
                description:
                - "Field outgoing_pkts_monitored"
            ipv4_address:
                description:
                - "IP address"
            icmp6_rate_limit_current:
                description:
                - "Field icmp6_rate_limit_current"
            config_speed:
                description:
                - "Field config_speed"
            ipv4_netmask:
                description:
                - "IP subnet mask"
            output_utilization:
                description:
                - "Field output_utilization"
            incoming_pkts_mirrored:
                description:
                - "Field incoming_pkts_mirrored"
            ipv4_list:
                description:
                - "Field ipv4_list"
            state:
                description:
                - "Field state"
            icmp_rate_limit_current:
                description:
                - "Field icmp_rate_limit_current"
            is_device_transparent:
                description:
                - "Field is_device_transparent"
            media_type:
                description:
                - "Field media_type"
            link_type:
                description:
                - "Field link_type"
            rate_pkt_rcvd:
                description:
                - "Field rate_pkt_rcvd"
            current_vnp_id:
                description:
                - "Field current_vnp_id"
            igmp_query_sent:
                description:
                - "Field igmp_query_sent"
            ipv4_addr_count:
                description:
                - "Field ipv4_addr_count"
            port_vnp_id:
                description:
                - "Field port_vnp_id"
            ipv6_link_local_scope:
                description:
                - "Field ipv6_link_local_scope"
            actual_duplexity:
                description:
                - "Field actual_duplexity"
            icmp_rate_over_limit_drop:
                description:
                - "Field icmp_rate_over_limit_drop"
            incoming_pkts_monitored:
                description:
                - "Field incoming_pkts_monitored"
            rate_byte_rcvd:
                description:
                - "Field rate_byte_rcvd"
            ipv6_list:
                description:
                - "Field ipv6_list"
            is_lead_member:
                description:
                - "Field is_lead_member"
            ipv6_link_local:
                description:
                - "Field ipv6_link_local"
            mac:
                description:
                - "Field mac"
            actual_speed:
                description:
                - "Field actual_speed"
            ipv6_link_local_prefix:
                description:
                - "Field ipv6_link_local_prefix"
            input_utilization:
                description:
                - "Field input_utilization"
            is_pristine:
                description:
                - "Field is_pristine"
            ifnum:
                description:
                - "Ethernet interface number"
            tagged_vlan_list:
                description:
                - "Field tagged_vlan_list"
            is_tagged:
                description:
                - "Field is_tagged"
            rate_pkt_sent:
                description:
                - "Field rate_pkt_sent"
            ipv6_addr_count:
                description:
                - "Field ipv6_addr_count"
            config_duplexity:
                description:
                - "Field config_duplexity"
    fec_forced_on:
        description:
        - "turn on the FEC"
        required: False
    trap_source:
        description:
        - "The trap source"
        required: False
    ip:
        description:
        - "Field ip"
        required: False
        suboptions:
            uuid:
                description:
                - "uuid of the object"
            address_list:
                description:
                - "Field address_list"
            generate_membership_query:
                description:
                - "Enable Membership Query"
            cache_spoofing_port:
                description:
                - "This interface connects to spoofing cache"
            inside:
                description:
                - "Configure interface as inside"
            allow_promiscuous_vip:
                description:
                - "Allow traffic to be associated with promiscuous VIP"
            client:
                description:
                - "Client facing interface for IPv4/v6 traffic"
            max_resp_time:
                description:
                - "Maximum Response Time (Max Response Time (Default is 100))"
            query_interval:
                description:
                - "1 - 255 (Default is 125)"
            outside:
                description:
                - "Configure interface as outside"
            helper_address_list:
                description:
                - "Field helper_address_list"
            stateful_firewall:
                description:
                - "Field stateful_firewall"
            rip:
                description:
                - "Field rip"
            ttl_ignore:
                description:
                - "Ignore TTL decrement for a received packet before sending out"
            router:
                description:
                - "Field router"
            dhcp:
                description:
                - "Use DHCP to configure IP address"
            server:
                description:
                - "Server facing interface for IPv4/v6 traffic"
            ospf:
                description:
                - "Field ospf"
            slb_partition_redirect:
                description:
                - "Redirect SLB traffic across partition"
    ddos:
        description:
        - "Field ddos"
        required: False
        suboptions:
            outside:
                description:
                - "DDoS outside (untrusted) interface"
            inside:
                description:
                - "DDoS inside (trusted) interface"
            uuid:
                description:
                - "uuid of the object"
    l3_vlan_fwd_disable:
        description:
        - "Field l3_vlan_fwd_disable"
        required: False
    access_list:
        description:
        - "Field access_list"
        required: False
        suboptions:
            acl_name:
                description:
                - "Apply an access list (Named Access List)"
            acl_id:
                description:
                - "ACL id"
    speed:
        description:
        - "'10'= 10; '100'= 100; '1000'= 1000; 'auto'= auto;"
        required: False
    speed_forced_40g:
        description:
        - "force the speed to be 40G on 100G link"
        required: False
    lldp:
        description:
        - "Field lldp"
        required: False
        suboptions:
            tx_dot1_cfg:
                description:
                - "Field tx_dot1_cfg"
            notification_cfg:
                description:
                - "Field notification_cfg"
            enable_cfg:
                description:
                - "Field enable_cfg"
            tx_tlvs_cfg:
                description:
                - "Field tx_tlvs_cfg"
            uuid:
                description:
                - "uuid of the object"
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            frame:
                description:
                - "Frames"
            rate_byte_sent:
                description:
                - "Byte sent rate bits/sec"
            runts:
                description:
                - "Runts"
            bytes_output:
                description:
                - "Output bytes"
            input_errors:
                description:
                - "Input errors"
            bytes_input:
                description:
                - "Input bytes"
            load_interval:
                description:
                - "Load Interval"
            transmitted_multicasts:
                description:
                - "Transmitted multicasts"
            packets_input:
                description:
                - "Input packets"
            received_multicasts:
                description:
                - "Received multicasts"
            received_broadcasts:
                description:
                - "Received broadcasts"
            transmitted_unicasts:
                description:
                - "Transmitted unicasts"
            collisions:
                description:
                - "Collisions"
            received_unicasts:
                description:
                - "Received unicasts"
            rate_pkt_sent:
                description:
                - "Packet sent rate packets/sec"
            giants:
                description:
                - "Giants"
            packets_output:
                description:
                - "Output packets"
            rate_byte_rcvd:
                description:
                - "Byte received rate bits/sec"
            rate_pkt_rcvd:
                description:
                - "Packet received rate packets/sec"
            transmitted_broadcasts:
                description:
                - "Transmitted broadcasts"
            crc:
                description:
                - "CRC"
            ifnum:
                description:
                - "Ethernet interface number"
            giants_output:
                description:
                - "Output Giants"
            output_errors:
                description:
                - "Output errors"
    uuid:
        description:
        - "uuid of the object"
        required: False
    bfd:
        description:
        - "Field bfd"
        required: False
        suboptions:
            interval_cfg:
                description:
                - "Field interval_cfg"
            authentication:
                description:
                - "Field authentication"
            echo:
                description:
                - "Enable BFD Echo"
            uuid:
                description:
                - "uuid of the object"
            demand:
                description:
                - "Demand mode"
    media_type_copper:
        description:
        - "Set the media type to copper"
        required: False
    ifnum:
        description:
        - "Ethernet interface number"
        required: True
    remove_vlan_tag:
        description:
        - "Remove the vlan tag for egressing packets"
        required: False
    monitor_list:
        description:
        - "Field monitor_list"
        required: False
        suboptions:
            monitor_vlan:
                description:
                - "VLAN number"
            monitor:
                description:
                - "'input'= Incoming packets; 'output'= Outgoing packets; 'both'= Both incoming
          and outgoing packets;"
            mirror_index:
                description:
                - "Mirror index"
    cpu_process:
        description:
        - "All Packets to this port are processed by CPU"
        required: False
    auto_neg_enable:
        description:
        - "enable auto-negotiation"
        required: False
    map:
        description:
        - "Field map"
        required: False
        suboptions:
            inside:
                description:
                - "Configure MAP inside interface (connected to MAP domains)"
            map_t_inside:
                description:
                - "Configure MAP inside interface (connected to MAP domains)"
            uuid:
                description:
                - "uuid of the object"
            map_t_outside:
                description:
                - "Configure MAP outside interface"
            outside:
                description:
                - "Configure MAP outside interface"
    traffic_distribution_mode:
        description:
        - "'sip'= sip; 'dip'= dip; 'primary'= primary; 'blade'= blade; 'l4-src-port'= l4
          -src-port; 'l4-dst-port'= l4-dst-port;"
        required: False
    trunk_group_list:
        description:
        - "Field trunk_group_list"
        required: False
        suboptions:
            uuid:
                description:
                - "uuid of the object"
            trunk_number:
                description:
                - "Trunk Number"
            user_tag:
                description:
                - "Customized tag"
            udld_timeout_cfg:
                description:
                - "Field udld_timeout_cfg"
            mode:
                description:
                - "'active'= enable initiation of LACP negotiation on a port(default); 'passive'=
          disable initiation of LACP negotiation on a port;"
            timeout:
                description:
                - "'long'= Set LACP long timeout (default); 'short'= Set LACP short timeout;"
            ntype:
                description:
                - "'static'= Static (default); 'lacp'= lacp; 'lacp-udld'= lacp-udld;"
            admin_key:
                description:
                - "LACP admin key (Admin key value)"
            port_priority:
                description:
                - "Set LACP priority for a port (LACP port priority)"
    nptv6:
        description:
        - "Field nptv6"
        required: False
        suboptions:
            domain_list:
                description:
                - "Field domain_list"
    cpu_process_dir:
        description:
        - "'primary'= Primary board; 'blade'= blade board; 'hash-dip'= Hash based on the
          Destination IP; 'hash-sip'= Hash based on the Source IP; 'hash-dmac'= Hash
          based on the Destination MAC; 'hash-smac'= Hash based on the Source MAC;"
        required: False
    isis:
        description:
        - "Field isis"
        required: False
        suboptions:
            priority_list:
                description:
                - "Field priority_list"
            padding:
                description:
                - "Add padding to IS-IS hello packets"
            hello_interval_minimal_list:
                description:
                - "Field hello_interval_minimal_list"
            mesh_group:
                description:
                - "Field mesh_group"
            network:
                description:
                - "'broadcast'= Specify IS-IS broadcast multi-access network; 'point-to-point'=
          Specify IS-IS point-to-point network;"
            authentication:
                description:
                - "Field authentication"
            csnp_interval_list:
                description:
                - "Field csnp_interval_list"
            retransmit_interval:
                description:
                - "Set per-LSP retransmission interval (Interval between retransmissions of the
          same LSP (seconds))"
            password_list:
                description:
                - "Field password_list"
            bfd_cfg:
                description:
                - "Field bfd_cfg"
            wide_metric_list:
                description:
                - "Field wide_metric_list"
            hello_interval_list:
                description:
                - "Field hello_interval_list"
            circuit_type:
                description:
                - "'level-1'= Level-1 only adjacencies are formed; 'level-1-2'= Level-1-2
          adjacencies are formed; 'level-2-only'= Level-2 only adjacencies are formed;"
            hello_multiplier_list:
                description:
                - "Field hello_multiplier_list"
            metric_list:
                description:
                - "Field metric_list"
            lsp_interval:
                description:
                - "Set LSP transmission interval (LSP transmission interval (milliseconds))"
            uuid:
                description:
                - "uuid of the object"
    name:
        description:
        - "Name for the interface"
        required: False
    duplexity:
        description:
        - "'Full'= Full; 'Half'= Half; 'auto'= auto;"
        required: False
    icmpv6_rate_limit:
        description:
        - "Field icmpv6_rate_limit"
        required: False
        suboptions:
            lockup_period_v6:
                description:
                - "Lockup period (second)"
            normal_v6:
                description:
                - "Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over
          the limit"
            lockup_v6:
                description:
                - "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate
          limit. If exceeds this limit, drop all ICMP packet for a time period)"
    user_tag:
        description:
        - "Customized tag"
        required: False
    mtu:
        description:
        - "Interface mtu (Interface MTU, default 1 (min MTU is 1280 for IPv6))"
        required: False
    ipv6:
        description:
        - "Field ipv6"
        required: False
        suboptions:
            uuid:
                description:
                - "uuid of the object"
            address_list:
                description:
                - "Field address_list"
            inside:
                description:
                - "Configure interface as inside"
            ipv6_enable:
                description:
                - "Enable IPv6 processing"
            rip:
                description:
                - "Field rip"
            outside:
                description:
                - "Configure interface as outside"
            stateful_firewall:
                description:
                - "Field stateful_firewall"
            ttl_ignore:
                description:
                - "Ignore TTL decrement for a received packet before sending out"
            router:
                description:
                - "Field router"
            access_list_cfg:
                description:
                - "Field access_list_cfg"
            ospf:
                description:
                - "Field ospf"
            router_adver:
                description:
                - "Field router_adver"
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'packets_input'= Input packets; 'bytes_input'= Input bytes;
          'received_broadcasts'= Received broadcasts; 'received_multicasts'= Received
          multicasts; 'received_unicasts'= Received unicasts; 'input_errors'= Input
          errors; 'crc'= CRC; 'frame'= Frames; 'runts'= Runts; 'giants'= Giants;
          'packets_output'= Output packets; 'bytes_output'= Output bytes;
          'transmitted_broadcasts'= Transmitted broadcasts; 'transmitted_multicasts'=
          Transmitted multicasts; 'transmitted_unicasts'= Transmitted unicasts;
          'output_errors'= Output errors; 'collisions'= Collisions; 'giants_output'=
          Output Giants; 'rate_pkt_sent'= Packet sent rate packets/sec; 'rate_byte_sent'=
          Byte sent rate bits/sec; 'rate_pkt_rcvd'= Packet received rate packets/sec;
          'rate_byte_rcvd'= Byte received rate bits/sec; 'load_interval'= Load Interval;"
    load_interval:
        description:
        - "Configure Load Interval (Seconds (5-300, Multiple of 5), default 300)"
        required: False
    lw_4o6:
        description:
        - "Field lw_4o6"
        required: False
        suboptions:
            outside:
                description:
                - "Configure LW-4over6 inside interface"
            inside:
                description:
                - "Configure LW-4over6 outside interface"
            uuid:
                description:
                - "uuid of the object"
    action:
        description:
        - "'enable'= Enable; 'disable'= Disable;"
        required: False
    fec_forced_off:
        description:
        - "turn off the FEC"
        required: False
    icmp_rate_limit:
        description:
        - "Field icmp_rate_limit"
        required: False
        suboptions:
            lockup:
                description:
                - "Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate
          limit. If exceeds this limit, drop all ICMP packet for a time period)"
            lockup_period:
                description:
                - "Lockup period (second)"
            normal:
                description:
                - "Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over
          the limit"
    flow_control:
        description:
        - "Enable 802.3x flow control on full duplex port"
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
    "access_list",
    "action",
    "auto_neg_enable",
    "bfd",
    "cpu_process",
    "cpu_process_dir",
    "ddos",
    "duplexity",
    "fec_forced_off",
    "fec_forced_on",
    "flow_control",
    "icmp_rate_limit",
    "icmpv6_rate_limit",
    "ifnum",
    "ip",
    "ipv6",
    "isis",
    "l3_vlan_fwd_disable",
    "lldp",
    "load_interval",
    "lw_4o6",
    "map",
    "media_type_copper",
    "monitor_list",
    "mtu",
    "name",
    "nptv6",
    "oper",
    "remove_vlan_tag",
    "sampling_enable",
    "speed",
    "speed_forced_40g",
    "stats",
    "traffic_distribution_mode",
    "trap_source",
    "trunk_group_list",
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
        state=dict(type='str', default="noop", choices=['noop', 'absent']),
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
            'line_protocol': {
                'type': 'str',
                'choices': ['up', 'down']
            },
            'icmp6_rate_over_limit_drop': {
                'type': 'int',
            },
            'outgoing_pkts_mirrored': {
                'type': 'int',
            },
            'rate_byte_sent': {
                'type': 'int',
            },
            'ipv6_link_local_type': {
                'type': 'str',
            },
            'vlan_id': {
                'type': 'int',
            },
            'outgoing_pkts_monitored': {
                'type': 'int',
            },
            'ipv4_address': {
                'type': 'str',
            },
            'icmp6_rate_limit_current': {
                'type': 'int',
            },
            'config_speed': {
                'type':
                'str',
                'choices':
                ['10Mbit', '100Mbit', '1Gbit', '10Gbit', '40Gbit', 'auto']
            },
            'ipv4_netmask': {
                'type': 'str',
            },
            'output_utilization': {
                'type': 'int',
            },
            'incoming_pkts_mirrored': {
                'type': 'int',
            },
            'ipv4_list': {
                'type': 'list',
                'mask': {
                    'type': 'str',
                },
                'addr': {
                    'type': 'str',
                }
            },
            'state': {
                'type': 'str',
                'choices': ['up', 'disabled', 'down']
            },
            'icmp_rate_limit_current': {
                'type': 'int',
            },
            'is_device_transparent': {
                'type': 'int',
            },
            'media_type': {
                'type': 'str',
                'choices': ['Copper', 'Fiber']
            },
            'link_type': {
                'type': 'str',
                'choices': ['GigabitEthernet', '10Gig', '40Gig']
            },
            'rate_pkt_rcvd': {
                'type': 'int',
            },
            'current_vnp_id': {
                'type': 'int',
            },
            'igmp_query_sent': {
                'type': 'int',
            },
            'ipv4_addr_count': {
                'type': 'int',
            },
            'port_vnp_id': {
                'type': 'int',
            },
            'ipv6_link_local_scope': {
                'type': 'str',
            },
            'actual_duplexity': {
                'type': 'str',
                'choices': ['Full', 'fdx', 'Half', 'hdx', 'auto']
            },
            'icmp_rate_over_limit_drop': {
                'type': 'int',
            },
            'incoming_pkts_monitored': {
                'type': 'int',
            },
            'rate_byte_rcvd': {
                'type': 'int',
            },
            'ipv6_list': {
                'type': 'list',
                'is_anycast': {
                    'type': 'int',
                },
                'prefix': {
                    'type': 'str',
                },
                'addr': {
                    'type': 'str',
                }
            },
            'is_lead_member': {
                'type': 'int',
            },
            'ipv6_link_local': {
                'type': 'str',
            },
            'mac': {
                'type': 'str',
            },
            'actual_speed': {
                'type':
                'str',
                'choices':
                ['10Mbit', '100Mbit', '1Gbit', '10Gbit', '40Gbit', 'unknown']
            },
            'ipv6_link_local_prefix': {
                'type': 'str',
            },
            'input_utilization': {
                'type': 'int',
            },
            'is_pristine': {
                'type': 'int',
            },
            'ifnum': {
                'type': 'str',
                'required': True,
            },
            'tagged_vlan_list': {
                'type': 'str',
            },
            'is_tagged': {
                'type': 'int',
            },
            'rate_pkt_sent': {
                'type': 'int',
            },
            'ipv6_addr_count': {
                'type': 'int',
            },
            'config_duplexity': {
                'type': 'str',
                'choices': ['Full', 'fdx', 'Half', 'hdx', 'auto']
            }
        },
        'fec_forced_on': {
            'type': 'bool',
        },
        'trap_source': {
            'type': 'bool',
        },
        'ip': {
            'type': 'dict',
            'uuid': {
                'type': 'str',
            },
            'address_list': {
                'type': 'list',
                'ipv4_address': {
                    'type': 'str',
                },
                'ipv4_netmask': {
                    'type': 'str',
                }
            },
            'generate_membership_query': {
                'type': 'bool',
            },
            'cache_spoofing_port': {
                'type': 'bool',
            },
            'inside': {
                'type': 'bool',
            },
            'allow_promiscuous_vip': {
                'type': 'bool',
            },
            'client': {
                'type': 'bool',
            },
            'max_resp_time': {
                'type': 'int',
            },
            'query_interval': {
                'type': 'int',
            },
            'outside': {
                'type': 'bool',
            },
            'helper_address_list': {
                'type': 'list',
                'helper_address': {
                    'type': 'str',
                }
            },
            'stateful_firewall': {
                'type': 'dict',
                'uuid': {
                    'type': 'str',
                },
                'class_list': {
                    'type': 'str',
                },
                'inside': {
                    'type': 'bool',
                },
                'outside': {
                    'type': 'bool',
                },
                'acl_id': {
                    'type': 'int',
                },
                'access_list': {
                    'type': 'bool',
                }
            },
            'rip': {
                'type': 'dict',
                'receive_cfg': {
                    'type': 'dict',
                    'receive': {
                        'type': 'bool',
                    },
                    'version': {
                        'type': 'str',
                        'choices': ['1', '2', '1-2']
                    }
                },
                'uuid': {
                    'type': 'str',
                },
                'receive_packet': {
                    'type': 'bool',
                },
                'split_horizon_cfg': {
                    'type': 'dict',
                    'state': {
                        'type': 'str',
                        'choices': ['poisoned', 'disable', 'enable']
                    }
                },
                'authentication': {
                    'type': 'dict',
                    'key_chain': {
                        'type': 'dict',
                        'key_chain': {
                            'type': 'str',
                        }
                    },
                    'mode': {
                        'type': 'dict',
                        'mode': {
                            'type': 'str',
                            'choices': ['md5', 'text']
                        }
                    },
                    'str': {
                        'type': 'dict',
                        'string': {
                            'type': 'str',
                        }
                    }
                },
                'send_cfg': {
                    'type': 'dict',
                    'version': {
                        'type': 'str',
                        'choices': ['1', '2', '1-compatible', '1-2']
                    },
                    'send': {
                        'type': 'bool',
                    }
                },
                'send_packet': {
                    'type': 'bool',
                }
            },
            'ttl_ignore': {
                'type': 'bool',
            },
            'router': {
                'type': 'dict',
                'isis': {
                    'type': 'dict',
                    'tag': {
                        'type': 'str',
                    },
                    'uuid': {
                        'type': 'str',
                    }
                }
            },
            'dhcp': {
                'type': 'bool',
            },
            'server': {
                'type': 'bool',
            },
            'ospf': {
                'type': 'dict',
                'ospf_ip_list': {
                    'type': 'list',
                    'dead_interval': {
                        'type': 'int',
                    },
                    'authentication_key': {
                        'type': 'str',
                    },
                    'uuid': {
                        'type': 'str',
                    },
                    'mtu_ignore': {
                        'type': 'bool',
                    },
                    'transmit_delay': {
                        'type': 'int',
                    },
                    'value': {
                        'type': 'str',
                        'choices': ['message-digest', 'null']
                    },
                    'priority': {
                        'type': 'int',
                    },
                    'authentication': {
                        'type': 'bool',
                    },
                    'cost': {
                        'type': 'int',
                    },
                    'database_filter': {
                        'type': 'str',
                        'choices': ['all']
                    },
                    'hello_interval': {
                        'type': 'int',
                    },
                    'ip_addr': {
                        'type': 'str',
                        'required': True,
                    },
                    'retransmit_interval': {
                        'type': 'int',
                    },
                    'message_digest_cfg': {
                        'type': 'list',
                        'md5_value': {
                            'type': 'str',
                        },
                        'message_digest_key': {
                            'type': 'int',
                        },
                        'encrypted': {
                            'type': 'str',
                        }
                    },
                    'out': {
                        'type': 'bool',
                    }
                },
                'ospf_global': {
                    'type': 'dict',
                    'cost': {
                        'type': 'int',
                    },
                    'dead_interval': {
                        'type': 'int',
                    },
                    'authentication_key': {
                        'type': 'str',
                    },
                    'network': {
                        'type': 'dict',
                        'broadcast': {
                            'type': 'bool',
                        },
                        'point_to_multipoint': {
                            'type': 'bool',
                        },
                        'non_broadcast': {
                            'type': 'bool',
                        },
                        'point_to_point': {
                            'type': 'bool',
                        },
                        'p2mp_nbma': {
                            'type': 'bool',
                        }
                    },
                    'mtu_ignore': {
                        'type': 'bool',
                    },
                    'transmit_delay': {
                        'type': 'int',
                    },
                    'authentication_cfg': {
                        'type': 'dict',
                        'authentication': {
                            'type': 'bool',
                        },
                        'value': {
                            'type': 'str',
                            'choices': ['message-digest', 'null']
                        }
                    },
                    'retransmit_interval': {
                        'type': 'int',
                    },
                    'bfd_cfg': {
                        'type': 'dict',
                        'disable': {
                            'type': 'bool',
                        },
                        'bfd': {
                            'type': 'bool',
                        }
                    },
                    'disable': {
                        'type': 'str',
                        'choices': ['all']
                    },
                    'hello_interval': {
                        'type': 'int',
                    },
                    'database_filter_cfg': {
                        'type': 'dict',
                        'database_filter': {
                            'type': 'str',
                            'choices': ['all']
                        },
                        'out': {
                            'type': 'bool',
                        }
                    },
                    'priority': {
                        'type': 'int',
                    },
                    'mtu': {
                        'type': 'int',
                    },
                    'message_digest_cfg': {
                        'type': 'list',
                        'message_digest_key': {
                            'type': 'int',
                        },
                        'md5': {
                            'type': 'dict',
                            'md5_value': {
                                'type': 'str',
                            },
                            'encrypted': {
                                'type': 'str',
                            }
                        }
                    },
                    'uuid': {
                        'type': 'str',
                    }
                }
            },
            'slb_partition_redirect': {
                'type': 'bool',
            }
        },
        'ddos': {
            'type': 'dict',
            'outside': {
                'type': 'bool',
            },
            'inside': {
                'type': 'bool',
            },
            'uuid': {
                'type': 'str',
            }
        },
        'l3_vlan_fwd_disable': {
            'type': 'bool',
        },
        'access_list': {
            'type': 'dict',
            'acl_name': {
                'type': 'str',
            },
            'acl_id': {
                'type': 'int',
            }
        },
        'speed': {
            'type': 'str',
            'choices': ['10', '100', '1000', 'auto']
        },
        'speed_forced_40g': {
            'type': 'bool',
        },
        'lldp': {
            'type': 'dict',
            'tx_dot1_cfg': {
                'type': 'dict',
                'link_aggregation': {
                    'type': 'bool',
                },
                'vlan': {
                    'type': 'bool',
                },
                'tx_dot1_tlvs': {
                    'type': 'bool',
                }
            },
            'notification_cfg': {
                'type': 'dict',
                'notification': {
                    'type': 'bool',
                },
                'notif_enable': {
                    'type': 'bool',
                }
            },
            'enable_cfg': {
                'type': 'dict',
                'rx': {
                    'type': 'bool',
                },
                'tx': {
                    'type': 'bool',
                },
                'rt_enable': {
                    'type': 'bool',
                }
            },
            'tx_tlvs_cfg': {
                'type': 'dict',
                'system_capabilities': {
                    'type': 'bool',
                },
                'system_description': {
                    'type': 'bool',
                },
                'management_address': {
                    'type': 'bool',
                },
                'tx_tlvs': {
                    'type': 'bool',
                },
                'exclude': {
                    'type': 'bool',
                },
                'port_description': {
                    'type': 'bool',
                },
                'system_name': {
                    'type': 'bool',
                }
            },
            'uuid': {
                'type': 'str',
            }
        },
        'stats': {
            'type': 'dict',
            'frame': {
                'type': 'str',
            },
            'rate_byte_sent': {
                'type': 'str',
            },
            'runts': {
                'type': 'str',
            },
            'bytes_output': {
                'type': 'str',
            },
            'input_errors': {
                'type': 'str',
            },
            'bytes_input': {
                'type': 'str',
            },
            'load_interval': {
                'type': 'str',
            },
            'transmitted_multicasts': {
                'type': 'str',
            },
            'packets_input': {
                'type': 'str',
            },
            'received_multicasts': {
                'type': 'str',
            },
            'received_broadcasts': {
                'type': 'str',
            },
            'transmitted_unicasts': {
                'type': 'str',
            },
            'collisions': {
                'type': 'str',
            },
            'received_unicasts': {
                'type': 'str',
            },
            'rate_pkt_sent': {
                'type': 'str',
            },
            'giants': {
                'type': 'str',
            },
            'packets_output': {
                'type': 'str',
            },
            'rate_byte_rcvd': {
                'type': 'str',
            },
            'rate_pkt_rcvd': {
                'type': 'str',
            },
            'transmitted_broadcasts': {
                'type': 'str',
            },
            'crc': {
                'type': 'str',
            },
            'ifnum': {
                'type': 'str',
                'required': True,
            },
            'giants_output': {
                'type': 'str',
            },
            'output_errors': {
                'type': 'str',
            }
        },
        'uuid': {
            'type': 'str',
        },
        'bfd': {
            'type': 'dict',
            'interval_cfg': {
                'type': 'dict',
                'interval': {
                    'type': 'int',
                },
                'min_rx': {
                    'type': 'int',
                },
                'multiplier': {
                    'type': 'int',
                }
            },
            'authentication': {
                'type': 'dict',
                'encrypted': {
                    'type': 'str',
                },
                'password': {
                    'type': 'str',
                },
                'method': {
                    'type':
                    'str',
                    'choices': [
                        'md5', 'meticulous-md5', 'meticulous-sha1', 'sha1',
                        'simple'
                    ]
                },
                'key_id': {
                    'type': 'int',
                }
            },
            'echo': {
                'type': 'bool',
            },
            'uuid': {
                'type': 'str',
            },
            'demand': {
                'type': 'bool',
            }
        },
        'media_type_copper': {
            'type': 'bool',
        },
        'ifnum': {
            'type': 'str',
            'required': True,
        },
        'remove_vlan_tag': {
            'type': 'bool',
        },
        'monitor_list': {
            'type': 'list',
            'monitor_vlan': {
                'type': 'int',
            },
            'monitor': {
                'type': 'str',
                'choices': ['input', 'output', 'both']
            },
            'mirror_index': {
                'type': 'int',
            }
        },
        'cpu_process': {
            'type': 'bool',
        },
        'auto_neg_enable': {
            'type': 'bool',
        },
        'map': {
            'type': 'dict',
            'inside': {
                'type': 'bool',
            },
            'map_t_inside': {
                'type': 'bool',
            },
            'uuid': {
                'type': 'str',
            },
            'map_t_outside': {
                'type': 'bool',
            },
            'outside': {
                'type': 'bool',
            }
        },
        'traffic_distribution_mode': {
            'type':
            'str',
            'choices':
            ['sip', 'dip', 'primary', 'blade', 'l4-src-port', 'l4-dst-port']
        },
        'trunk_group_list': {
            'type': 'list',
            'uuid': {
                'type': 'str',
            },
            'trunk_number': {
                'type': 'int',
                'required': True,
            },
            'user_tag': {
                'type': 'str',
            },
            'udld_timeout_cfg': {
                'type': 'dict',
                'slow': {
                    'type': 'int',
                },
                'fast': {
                    'type': 'int',
                }
            },
            'mode': {
                'type': 'str',
                'choices': ['active', 'passive']
            },
            'timeout': {
                'type': 'str',
                'choices': ['long', 'short']
            },
            'ntype': {
                'type': 'str',
                'choices': ['static', 'lacp', 'lacp-udld']
            },
            'admin_key': {
                'type': 'int',
            },
            'port_priority': {
                'type': 'int',
            }
        },
        'nptv6': {
            'type': 'dict',
            'domain_list': {
                'type': 'list',
                'domain_name': {
                    'type': 'str',
                    'required': True,
                },
                'bind_type': {
                    'type': 'str',
                    'required': True,
                    'choices': ['inside', 'outside']
                },
                'uuid': {
                    'type': 'str',
                }
            }
        },
        'cpu_process_dir': {
            'type':
            'str',
            'choices': [
                'primary', 'blade', 'hash-dip', 'hash-sip', 'hash-dmac',
                'hash-smac'
            ]
        },
        'isis': {
            'type': 'dict',
            'priority_list': {
                'type': 'list',
                'priority': {
                    'type': 'int',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'padding': {
                'type': 'bool',
            },
            'hello_interval_minimal_list': {
                'type': 'list',
                'hello_interval_minimal': {
                    'type': 'bool',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'mesh_group': {
                'type': 'dict',
                'value': {
                    'type': 'int',
                },
                'blocked': {
                    'type': 'bool',
                }
            },
            'network': {
                'type': 'str',
                'choices': ['broadcast', 'point-to-point']
            },
            'authentication': {
                'type': 'dict',
                'send_only_list': {
                    'type': 'list',
                    'send_only': {
                        'type': 'bool',
                    },
                    'level': {
                        'type': 'str',
                        'choices': ['level-1', 'level-2']
                    }
                },
                'mode_list': {
                    'type': 'list',
                    'mode': {
                        'type': 'str',
                        'choices': ['md5']
                    },
                    'level': {
                        'type': 'str',
                        'choices': ['level-1', 'level-2']
                    }
                },
                'key_chain_list': {
                    'type': 'list',
                    'key_chain': {
                        'type': 'str',
                    },
                    'level': {
                        'type': 'str',
                        'choices': ['level-1', 'level-2']
                    }
                }
            },
            'csnp_interval_list': {
                'type': 'list',
                'csnp_interval': {
                    'type': 'int',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'retransmit_interval': {
                'type': 'int',
            },
            'password_list': {
                'type': 'list',
                'password': {
                    'type': 'str',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'bfd_cfg': {
                'type': 'dict',
                'disable': {
                    'type': 'bool',
                },
                'bfd': {
                    'type': 'bool',
                }
            },
            'wide_metric_list': {
                'type': 'list',
                'wide_metric': {
                    'type': 'int',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'hello_interval_list': {
                'type': 'list',
                'hello_interval': {
                    'type': 'int',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'circuit_type': {
                'type': 'str',
                'choices': ['level-1', 'level-1-2', 'level-2-only']
            },
            'hello_multiplier_list': {
                'type': 'list',
                'hello_multiplier': {
                    'type': 'int',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'metric_list': {
                'type': 'list',
                'metric': {
                    'type': 'int',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'lsp_interval': {
                'type': 'int',
            },
            'uuid': {
                'type': 'str',
            }
        },
        'name': {
            'type': 'str',
        },
        'duplexity': {
            'type': 'str',
            'choices': ['Full', 'Half', 'auto']
        },
        'icmpv6_rate_limit': {
            'type': 'dict',
            'lockup_period_v6': {
                'type': 'int',
            },
            'normal_v6': {
                'type': 'int',
            },
            'lockup_v6': {
                'type': 'int',
            }
        },
        'user_tag': {
            'type': 'str',
        },
        'mtu': {
            'type': 'int',
        },
        'ipv6': {
            'type': 'dict',
            'uuid': {
                'type': 'str',
            },
            'address_list': {
                'type': 'list',
                'address_type': {
                    'type': 'str',
                    'choices': ['anycast', 'link-local']
                },
                'ipv6_addr': {
                    'type': 'str',
                }
            },
            'inside': {
                'type': 'bool',
            },
            'ipv6_enable': {
                'type': 'bool',
            },
            'rip': {
                'type': 'dict',
                'split_horizon_cfg': {
                    'type': 'dict',
                    'state': {
                        'type': 'str',
                        'choices': ['poisoned', 'disable', 'enable']
                    }
                },
                'uuid': {
                    'type': 'str',
                }
            },
            'outside': {
                'type': 'bool',
            },
            'stateful_firewall': {
                'type': 'dict',
                'uuid': {
                    'type': 'str',
                },
                'class_list': {
                    'type': 'str',
                },
                'acl_name': {
                    'type': 'str',
                },
                'inside': {
                    'type': 'bool',
                },
                'outside': {
                    'type': 'bool',
                },
                'access_list': {
                    'type': 'bool',
                }
            },
            'ttl_ignore': {
                'type': 'bool',
            },
            'router': {
                'type': 'dict',
                'ripng': {
                    'type': 'dict',
                    'uuid': {
                        'type': 'str',
                    },
                    'rip': {
                        'type': 'bool',
                    }
                },
                'ospf': {
                    'type': 'dict',
                    'area_list': {
                        'type': 'list',
                        'area_id_addr': {
                            'type': 'str',
                        },
                        'tag': {
                            'type': 'str',
                        },
                        'instance_id': {
                            'type': 'int',
                        },
                        'area_id_num': {
                            'type': 'int',
                        }
                    },
                    'uuid': {
                        'type': 'str',
                    }
                },
                'isis': {
                    'type': 'dict',
                    'tag': {
                        'type': 'str',
                    },
                    'uuid': {
                        'type': 'str',
                    }
                }
            },
            'access_list_cfg': {
                'type': 'dict',
                'inbound': {
                    'type': 'bool',
                },
                'v6_acl_name': {
                    'type': 'str',
                }
            },
            'ospf': {
                'type': 'dict',
                'uuid': {
                    'type': 'str',
                },
                'bfd': {
                    'type': 'bool',
                },
                'cost_cfg': {
                    'type': 'list',
                    'cost': {
                        'type': 'int',
                    },
                    'instance_id': {
                        'type': 'int',
                    }
                },
                'priority_cfg': {
                    'type': 'list',
                    'priority': {
                        'type': 'int',
                    },
                    'instance_id': {
                        'type': 'int',
                    }
                },
                'hello_interval_cfg': {
                    'type': 'list',
                    'hello_interval': {
                        'type': 'int',
                    },
                    'instance_id': {
                        'type': 'int',
                    }
                },
                'mtu_ignore_cfg': {
                    'type': 'list',
                    'mtu_ignore': {
                        'type': 'bool',
                    },
                    'instance_id': {
                        'type': 'int',
                    }
                },
                'retransmit_interval_cfg': {
                    'type': 'list',
                    'retransmit_interval': {
                        'type': 'int',
                    },
                    'instance_id': {
                        'type': 'int',
                    }
                },
                'disable': {
                    'type': 'bool',
                },
                'transmit_delay_cfg': {
                    'type': 'list',
                    'transmit_delay': {
                        'type': 'int',
                    },
                    'instance_id': {
                        'type': 'int',
                    }
                },
                'neighbor_cfg': {
                    'type': 'list',
                    'neighbor_priority': {
                        'type': 'int',
                    },
                    'neighbor_poll_interval': {
                        'type': 'int',
                    },
                    'neig_inst': {
                        'type': 'int',
                    },
                    'neighbor': {
                        'type': 'str',
                    },
                    'neighbor_cost': {
                        'type': 'int',
                    }
                },
                'network_list': {
                    'type': 'list',
                    'broadcast_type': {
                        'type':
                        'str',
                        'choices': [
                            'broadcast', 'non-broadcast', 'point-to-point',
                            'point-to-multipoint'
                        ]
                    },
                    'p2mp_nbma': {
                        'type': 'bool',
                    },
                    'network_instance_id': {
                        'type': 'int',
                    }
                },
                'dead_interval_cfg': {
                    'type': 'list',
                    'dead_interval': {
                        'type': 'int',
                    },
                    'instance_id': {
                        'type': 'int',
                    }
                }
            },
            'router_adver': {
                'type': 'dict',
                'max_interval': {
                    'type': 'int',
                },
                'default_lifetime': {
                    'type': 'int',
                },
                'reachable_time': {
                    'type': 'int',
                },
                'other_config_action': {
                    'type': 'str',
                    'choices': ['enable', 'disable']
                },
                'floating_ip_default_vrid': {
                    'type': 'str',
                },
                'managed_config_action': {
                    'type': 'str',
                    'choices': ['enable', 'disable']
                },
                'min_interval': {
                    'type': 'int',
                },
                'rate_limit': {
                    'type': 'int',
                },
                'adver_mtu_disable': {
                    'type': 'bool',
                },
                'prefix_list': {
                    'type': 'list',
                    'not_autonomous': {
                        'type': 'bool',
                    },
                    'not_on_link': {
                        'type': 'bool',
                    },
                    'valid_lifetime': {
                        'type': 'int',
                    },
                    'prefix': {
                        'type': 'str',
                    },
                    'preferred_lifetime': {
                        'type': 'int',
                    }
                },
                'floating_ip': {
                    'type': 'str',
                },
                'adver_vrid': {
                    'type': 'int',
                },
                'use_floating_ip_default_vrid': {
                    'type': 'bool',
                },
                'action': {
                    'type': 'str',
                    'choices': ['enable', 'disable']
                },
                'adver_vrid_default': {
                    'type': 'bool',
                },
                'adver_mtu': {
                    'type': 'int',
                },
                'retransmit_timer': {
                    'type': 'int',
                },
                'hop_limit': {
                    'type': 'int',
                },
                'use_floating_ip': {
                    'type': 'bool',
                }
            }
        },
        'sampling_enable': {
            'type': 'list',
            'counters1': {
                'type':
                'str',
                'choices': [
                    'all', 'packets_input', 'bytes_input',
                    'received_broadcasts', 'received_multicasts',
                    'received_unicasts', 'input_errors', 'crc', 'frame',
                    'runts', 'giants', 'packets_output', 'bytes_output',
                    'transmitted_broadcasts', 'transmitted_multicasts',
                    'transmitted_unicasts', 'output_errors', 'collisions',
                    'giants_output', 'rate_pkt_sent', 'rate_byte_sent',
                    'rate_pkt_rcvd', 'rate_byte_rcvd', 'load_interval'
                ]
            }
        },
        'load_interval': {
            'type': 'int',
        },
        'lw_4o6': {
            'type': 'dict',
            'outside': {
                'type': 'bool',
            },
            'inside': {
                'type': 'bool',
            },
            'uuid': {
                'type': 'str',
            }
        },
        'action': {
            'type': 'str',
            'choices': ['enable', 'disable']
        },
        'fec_forced_off': {
            'type': 'bool',
        },
        'icmp_rate_limit': {
            'type': 'dict',
            'lockup': {
                'type': 'int',
            },
            'lockup_period': {
                'type': 'int',
            },
            'normal': {
                'type': 'int',
            }
        },
        'flow_control': {
            'type': 'bool',
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/ethernet/{ifnum}"

    f_dict = {}
    f_dict["ifnum"] = module.params["ifnum"]

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

    module.client = client_factory(ansible_host, ansible_port, protocol,
                                   ansible_username, ansible_password)

    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)

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
