# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetTwingateRemoteNetworkResult',
    'AwaitableGetTwingateRemoteNetworkResult',
    'get_twingate_remote_network',
    'get_twingate_remote_network_output',
]

@pulumi.output_type
class GetTwingateRemoteNetworkResult:
    """
    A collection of values returned by getTwingateRemoteNetwork.
    """
    def __init__(__self__, id=None, location=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the Remote Network
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
        The name of the Remote Network
        """
        return pulumi.get(self, "name")


class AwaitableGetTwingateRemoteNetworkResult(GetTwingateRemoteNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTwingateRemoteNetworkResult(
            id=self.id,
            location=self.location,
            name=self.name)


def get_twingate_remote_network(id: Optional[str] = None,
                                name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTwingateRemoteNetworkResult:
    """
    A Remote Network represents a single private network in Twingate that can have one or more Connectors and Resources assigned to it. You must create a Remote Network before creating Resources and Connectors that belong to it. For more information, see Twingate's [documentation](https://docs.twingate.com/docs/remote-networks).

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_twingate as twingate

    foo = twingate.get_twingate_remote_network(name="<your network's name>")
    ```
    <!--End PulumiCodeChooser -->


    :param str id: The ID of the Remote Network
    :param str name: The name of the Remote Network
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('twingate:index/getTwingateRemoteNetwork:getTwingateRemoteNetwork', __args__, opts=opts, typ=GetTwingateRemoteNetworkResult).value

    return AwaitableGetTwingateRemoteNetworkResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_twingate_remote_network)
def get_twingate_remote_network_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                       name: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTwingateRemoteNetworkResult]:
    """
    A Remote Network represents a single private network in Twingate that can have one or more Connectors and Resources assigned to it. You must create a Remote Network before creating Resources and Connectors that belong to it. For more information, see Twingate's [documentation](https://docs.twingate.com/docs/remote-networks).

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_twingate as twingate

    foo = twingate.get_twingate_remote_network(name="<your network's name>")
    ```
    <!--End PulumiCodeChooser -->


    :param str id: The ID of the Remote Network
    :param str name: The name of the Remote Network
    """
    ...