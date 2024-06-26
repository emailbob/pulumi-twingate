# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'TwingateResourceAccessGroup',
    'TwingateResourceAccessService',
    'TwingateResourceProtocols',
    'TwingateResourceProtocolsTcp',
    'TwingateResourceProtocolsUdp',
    'GetTwingateConnectorsConnectorResult',
    'GetTwingateGroupsGroupResult',
    'GetTwingateRemoteNetworksRemoteNetworkResult',
    'GetTwingateResourceProtocolsResult',
    'GetTwingateResourceProtocolsTcpResult',
    'GetTwingateResourceProtocolsUdpResult',
    'GetTwingateResourcesResourceResult',
    'GetTwingateResourcesResourceProtocolsResult',
    'GetTwingateResourcesResourceProtocolsTcpResult',
    'GetTwingateResourcesResourceProtocolsUdpResult',
    'GetTwingateSecurityPoliciesSecurityPolicyResult',
    'GetTwingateServiceAccountsServiceAccountResult',
    'GetTwingateUsersUserResult',
]

@pulumi.output_type
class TwingateResourceAccessGroup(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupId":
            suggest = "group_id"
        elif key == "securityPolicyId":
            suggest = "security_policy_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TwingateResourceAccessGroup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TwingateResourceAccessGroup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TwingateResourceAccessGroup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_id: Optional[str] = None,
                 security_policy_id: Optional[str] = None):
        """
        :param str group_id: Group ID that will have permission to access the Resource.
        :param str security_policy_id: The ID of a `get_twingate_security_policy` to use as the access policy for the group IDs in the access block.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if security_policy_id is not None:
            pulumi.set(__self__, "security_policy_id", security_policy_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[str]:
        """
        Group ID that will have permission to access the Resource.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="securityPolicyId")
    def security_policy_id(self) -> Optional[str]:
        """
        The ID of a `get_twingate_security_policy` to use as the access policy for the group IDs in the access block.
        """
        return pulumi.get(self, "security_policy_id")


@pulumi.output_type
class TwingateResourceAccessService(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "serviceAccountId":
            suggest = "service_account_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TwingateResourceAccessService. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TwingateResourceAccessService.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TwingateResourceAccessService.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 service_account_id: Optional[str] = None):
        """
        :param str service_account_id: The ID of the service account that should have access to this Resource.
        """
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[str]:
        """
        The ID of the service account that should have access to this Resource.
        """
        return pulumi.get(self, "service_account_id")


@pulumi.output_type
class TwingateResourceProtocols(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowIcmp":
            suggest = "allow_icmp"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TwingateResourceProtocols. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TwingateResourceProtocols.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TwingateResourceProtocols.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allow_icmp: Optional[bool] = None,
                 tcp: Optional['outputs.TwingateResourceProtocolsTcp'] = None,
                 udp: Optional['outputs.TwingateResourceProtocolsUdp'] = None):
        """
        :param bool allow_icmp: Whether to allow ICMP (ping) traffic
        """
        if allow_icmp is not None:
            pulumi.set(__self__, "allow_icmp", allow_icmp)
        if tcp is not None:
            pulumi.set(__self__, "tcp", tcp)
        if udp is not None:
            pulumi.set(__self__, "udp", udp)

    @property
    @pulumi.getter(name="allowIcmp")
    def allow_icmp(self) -> Optional[bool]:
        """
        Whether to allow ICMP (ping) traffic
        """
        return pulumi.get(self, "allow_icmp")

    @property
    @pulumi.getter
    def tcp(self) -> Optional['outputs.TwingateResourceProtocolsTcp']:
        return pulumi.get(self, "tcp")

    @property
    @pulumi.getter
    def udp(self) -> Optional['outputs.TwingateResourceProtocolsUdp']:
        return pulumi.get(self, "udp")


@pulumi.output_type
class TwingateResourceProtocolsTcp(dict):
    def __init__(__self__, *,
                 policy: Optional[str] = None,
                 ports: Optional[Sequence[str]] = None):
        """
        :param str policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param Sequence[str] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> Optional[str]:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[str]]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")


@pulumi.output_type
class TwingateResourceProtocolsUdp(dict):
    def __init__(__self__, *,
                 policy: Optional[str] = None,
                 ports: Optional[Sequence[str]] = None):
        """
        :param str policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param Sequence[str] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> Optional[str]:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[str]]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")


@pulumi.output_type
class GetTwingateConnectorsConnectorResult(dict):
    def __init__(__self__, *,
                 id: str,
                 name: str,
                 remote_network_id: str,
                 status_updates_enabled: bool):
        """
        :param str id: The ID of the Connector.
        :param str name: The Name of the Connector.
        :param str remote_network_id: The ID of the Remote Network attached to the Connector.
        :param bool status_updates_enabled: Determines whether status notifications are enabled for the Connector.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "remote_network_id", remote_network_id)
        pulumi.set(__self__, "status_updates_enabled", status_updates_enabled)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Connector.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The Name of the Connector.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="remoteNetworkId")
    def remote_network_id(self) -> str:
        """
        The ID of the Remote Network attached to the Connector.
        """
        return pulumi.get(self, "remote_network_id")

    @property
    @pulumi.getter(name="statusUpdatesEnabled")
    def status_updates_enabled(self) -> bool:
        """
        Determines whether status notifications are enabled for the Connector.
        """
        return pulumi.get(self, "status_updates_enabled")


@pulumi.output_type
class GetTwingateGroupsGroupResult(dict):
    def __init__(__self__, *,
                 id: str,
                 is_active: bool,
                 name: str,
                 security_policy_id: str,
                 type: str):
        """
        :param str id: The ID of the Group
        :param bool is_active: Indicates if the Group is active
        :param str name: The name of the Group
        :param str security_policy_id: The Security Policy assigned to the Group.
        :param str type: The type of the Group
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "is_active", is_active)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "security_policy_id", security_policy_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Group
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isActive")
    def is_active(self) -> bool:
        """
        Indicates if the Group is active
        """
        return pulumi.get(self, "is_active")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Group
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="securityPolicyId")
    def security_policy_id(self) -> str:
        """
        The Security Policy assigned to the Group.
        """
        return pulumi.get(self, "security_policy_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the Group
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetTwingateRemoteNetworksRemoteNetworkResult(dict):
    def __init__(__self__, *,
                 id: str,
                 location: str,
                 name: Optional[str] = None):
        """
        :param str id: The ID of the Remote Network.
        :param str location: The location of the Remote Network. Must be one of the following: AWS, AZURE, GOOGLE*CLOUD, ON*PREMISE, OTHER.
        :param str name: The name of the Remote Network.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Remote Network.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the Remote Network. Must be one of the following: AWS, AZURE, GOOGLE*CLOUD, ON*PREMISE, OTHER.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the Remote Network.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetTwingateResourceProtocolsResult(dict):
    def __init__(__self__, *,
                 allow_icmp: bool,
                 tcp: Optional['outputs.GetTwingateResourceProtocolsTcpResult'] = None,
                 udp: Optional['outputs.GetTwingateResourceProtocolsUdpResult'] = None):
        """
        :param bool allow_icmp: Whether to allow ICMP (ping) traffic
        """
        pulumi.set(__self__, "allow_icmp", allow_icmp)
        if tcp is not None:
            pulumi.set(__self__, "tcp", tcp)
        if udp is not None:
            pulumi.set(__self__, "udp", udp)

    @property
    @pulumi.getter(name="allowIcmp")
    def allow_icmp(self) -> bool:
        """
        Whether to allow ICMP (ping) traffic
        """
        return pulumi.get(self, "allow_icmp")

    @property
    @pulumi.getter
    def tcp(self) -> Optional['outputs.GetTwingateResourceProtocolsTcpResult']:
        return pulumi.get(self, "tcp")

    @property
    @pulumi.getter
    def udp(self) -> Optional['outputs.GetTwingateResourceProtocolsUdpResult']:
        return pulumi.get(self, "udp")


@pulumi.output_type
class GetTwingateResourceProtocolsTcpResult(dict):
    def __init__(__self__, *,
                 policy: str,
                 ports: Sequence[str]):
        """
        :param str policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param Sequence[str] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> str:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def ports(self) -> Sequence[str]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")


@pulumi.output_type
class GetTwingateResourceProtocolsUdpResult(dict):
    def __init__(__self__, *,
                 policy: str,
                 ports: Sequence[str]):
        """
        :param str policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param Sequence[str] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> str:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def ports(self) -> Sequence[str]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")


@pulumi.output_type
class GetTwingateResourcesResourceResult(dict):
    def __init__(__self__, *,
                 address: str,
                 id: str,
                 name: str,
                 protocols: 'outputs.GetTwingateResourcesResourceProtocolsResult',
                 remote_network_id: str):
        """
        :param str address: The Resource's IP/CIDR or FQDN/DNS zone
        :param str id: The id of the Resource
        :param str name: The name of the Resource
        :param 'GetTwingateResourcesResourceProtocolsArgs' protocols: Restrict access to certain protocols and ports. By default or when this argument is not defined, there is no restriction, and all protocols and ports are allowed.
        :param str remote_network_id: Remote Network ID where the Resource lives
        """
        pulumi.set(__self__, "address", address)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "protocols", protocols)
        pulumi.set(__self__, "remote_network_id", remote_network_id)

    @property
    @pulumi.getter
    def address(self) -> str:
        """
        The Resource's IP/CIDR or FQDN/DNS zone
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the Resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def protocols(self) -> 'outputs.GetTwingateResourcesResourceProtocolsResult':
        """
        Restrict access to certain protocols and ports. By default or when this argument is not defined, there is no restriction, and all protocols and ports are allowed.
        """
        return pulumi.get(self, "protocols")

    @property
    @pulumi.getter(name="remoteNetworkId")
    def remote_network_id(self) -> str:
        """
        Remote Network ID where the Resource lives
        """
        return pulumi.get(self, "remote_network_id")


@pulumi.output_type
class GetTwingateResourcesResourceProtocolsResult(dict):
    def __init__(__self__, *,
                 allow_icmp: bool,
                 tcp: 'outputs.GetTwingateResourcesResourceProtocolsTcpResult',
                 udp: 'outputs.GetTwingateResourcesResourceProtocolsUdpResult'):
        """
        :param bool allow_icmp: Whether to allow ICMP (ping) traffic
        """
        pulumi.set(__self__, "allow_icmp", allow_icmp)
        pulumi.set(__self__, "tcp", tcp)
        pulumi.set(__self__, "udp", udp)

    @property
    @pulumi.getter(name="allowIcmp")
    def allow_icmp(self) -> bool:
        """
        Whether to allow ICMP (ping) traffic
        """
        return pulumi.get(self, "allow_icmp")

    @property
    @pulumi.getter
    def tcp(self) -> 'outputs.GetTwingateResourcesResourceProtocolsTcpResult':
        return pulumi.get(self, "tcp")

    @property
    @pulumi.getter
    def udp(self) -> 'outputs.GetTwingateResourcesResourceProtocolsUdpResult':
        return pulumi.get(self, "udp")


@pulumi.output_type
class GetTwingateResourcesResourceProtocolsTcpResult(dict):
    def __init__(__self__, *,
                 policy: str,
                 ports: Sequence[str]):
        """
        :param str policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param Sequence[str] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> str:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def ports(self) -> Sequence[str]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")


@pulumi.output_type
class GetTwingateResourcesResourceProtocolsUdpResult(dict):
    def __init__(__self__, *,
                 policy: str,
                 ports: Sequence[str]):
        """
        :param str policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param Sequence[str] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> str:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def ports(self) -> Sequence[str]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")


@pulumi.output_type
class GetTwingateSecurityPoliciesSecurityPolicyResult(dict):
    def __init__(__self__, *,
                 id: str,
                 name: str):
        """
        :param str id: Return a matching Security Policy by its ID. The ID for the Security Policy can be obtained from the Admin API or the URL string in the Admin Console.
        :param str name: Return a Security Policy that exactly matches this name.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Return a matching Security Policy by its ID. The ID for the Security Policy can be obtained from the Admin API or the URL string in the Admin Console.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Return a Security Policy that exactly matches this name.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetTwingateServiceAccountsServiceAccountResult(dict):
    def __init__(__self__, *,
                 id: str,
                 key_ids: Sequence[str],
                 name: str,
                 resource_ids: Sequence[str]):
        """
        :param str id: ID of the Service Account resource
        :param Sequence[str] key_ids: List of twingate*service*account_key IDs that are assigned to the Service Account.
        :param str name: Name of the Service Account
        :param Sequence[str] resource_ids: List of TwingateResource IDs that the Service Account is assigned to.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "key_ids", key_ids)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_ids", resource_ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the Service Account resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyIds")
    def key_ids(self) -> Sequence[str]:
        """
        List of twingate*service*account_key IDs that are assigned to the Service Account.
        """
        return pulumi.get(self, "key_ids")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Service Account
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceIds")
    def resource_ids(self) -> Sequence[str]:
        """
        List of TwingateResource IDs that the Service Account is assigned to.
        """
        return pulumi.get(self, "resource_ids")


@pulumi.output_type
class GetTwingateUsersUserResult(dict):
    def __init__(__self__, *,
                 email: str,
                 first_name: str,
                 id: str,
                 last_name: str,
                 role: str,
                 type: str):
        """
        :param str email: The email address of the User
        :param str first_name: The first name of the User
        :param str id: The ID of the User
        :param str last_name: The last name of the User
        :param str role: Indicates the User's role. Either ADMIN, DEVOPS, SUPPORT, or MEMBER.
        :param str type: Indicates the User's type. Either MANUAL or SYNCED.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "first_name", first_name)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "last_name", last_name)
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address of the User
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        """
        The first name of the User
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the User
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        """
        The last name of the User
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def role(self) -> str:
        """
        Indicates the User's role. Either ADMIN, DEVOPS, SUPPORT, or MEMBER.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Indicates the User's type. Either MANUAL or SYNCED.
        """
        return pulumi.get(self, "type")


