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
from ._inputs import *

__all__ = [
    'GetTwingateSecurityPoliciesResult',
    'AwaitableGetTwingateSecurityPoliciesResult',
    'get_twingate_security_policies',
    'get_twingate_security_policies_output',
]

@pulumi.output_type
class GetTwingateSecurityPoliciesResult:
    """
    A collection of values returned by getTwingateSecurityPolicies.
    """
    def __init__(__self__, id=None, security_policies=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if security_policies and not isinstance(security_policies, list):
            raise TypeError("Expected argument 'security_policies' to be a list")
        pulumi.set(__self__, "security_policies", security_policies)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="securityPolicies")
    def security_policies(self) -> Optional[Sequence['outputs.GetTwingateSecurityPoliciesSecurityPolicyResult']]:
        return pulumi.get(self, "security_policies")


class AwaitableGetTwingateSecurityPoliciesResult(GetTwingateSecurityPoliciesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTwingateSecurityPoliciesResult(
            id=self.id,
            security_policies=self.security_policies)


def get_twingate_security_policies(security_policies: Optional[Sequence[pulumi.InputType['GetTwingateSecurityPoliciesSecurityPolicyArgs']]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTwingateSecurityPoliciesResult:
    """
    Security Policies are defined in the Twingate Admin Console and determine user and device authentication requirements for Resources.

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_twingate as twingate

    all = twingate.get_twingate_security_policies()
    ```
    <!--End PulumiCodeChooser -->
    """
    __args__ = dict()
    __args__['securityPolicies'] = security_policies
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('twingate:index/getTwingateSecurityPolicies:getTwingateSecurityPolicies', __args__, opts=opts, typ=GetTwingateSecurityPoliciesResult).value

    return AwaitableGetTwingateSecurityPoliciesResult(
        id=pulumi.get(__ret__, 'id'),
        security_policies=pulumi.get(__ret__, 'security_policies'))


@_utilities.lift_output_func(get_twingate_security_policies)
def get_twingate_security_policies_output(security_policies: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTwingateSecurityPoliciesSecurityPolicyArgs']]]]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTwingateSecurityPoliciesResult]:
    """
    Security Policies are defined in the Twingate Admin Console and determine user and device authentication requirements for Resources.

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_twingate as twingate

    all = twingate.get_twingate_security_policies()
    ```
    <!--End PulumiCodeChooser -->
    """
    ...