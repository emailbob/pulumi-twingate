# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TwingateServiceAccountKeyArgs', 'TwingateServiceAccountKey']

@pulumi.input_type
class TwingateServiceAccountKeyArgs:
    def __init__(__self__, *,
                 service_account_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TwingateServiceAccountKey resource.
        :param pulumi.Input[str] service_account_id: The id of the Service Account
        :param pulumi.Input[str] name: The name of the Service Key
        """
        pulumi.set(__self__, "service_account_id", service_account_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Input[str]:
        """
        The id of the Service Account
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Service Key
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TwingateServiceAccountKeyState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TwingateServiceAccountKey resources.
        :param pulumi.Input[str] name: The name of the Service Key
        :param pulumi.Input[str] service_account_id: The id of the Service Account
        :param pulumi.Input[str] token: Autogenerated Service Key token. Used to configure a Twingate Client running in headless mode.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Service Key
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the Service Account
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        Autogenerated Service Key token. Used to configure a Twingate Client running in headless mode.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


class TwingateServiceAccountKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Service Key authorizes access to all Resources assigned to a Service Account.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import emailbob_twingate as twingate

        github_actions_prod = twingate.TwingateServiceAccount("githubActionsProd")
        github_key = twingate.TwingateServiceAccountKey("githubKey", service_account_id=github_actions_prod.id)
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the Service Key
        :param pulumi.Input[str] service_account_id: The id of the Service Account
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TwingateServiceAccountKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Service Key authorizes access to all Resources assigned to a Service Account.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import emailbob_twingate as twingate

        github_actions_prod = twingate.TwingateServiceAccount("githubActionsProd")
        github_key = twingate.TwingateServiceAccountKey("githubKey", service_account_id=github_actions_prod.id)
        ```
        <!--End PulumiCodeChooser -->

        :param str resource_name: The name of the resource.
        :param TwingateServiceAccountKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TwingateServiceAccountKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TwingateServiceAccountKeyArgs.__new__(TwingateServiceAccountKeyArgs)

            __props__.__dict__["name"] = name
            if service_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_account_id'")
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["token"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["token"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(TwingateServiceAccountKey, __self__).__init__(
            'twingate:index/twingateServiceAccountKey:TwingateServiceAccountKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            service_account_id: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None) -> 'TwingateServiceAccountKey':
        """
        Get an existing TwingateServiceAccountKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the Service Key
        :param pulumi.Input[str] service_account_id: The id of the Service Account
        :param pulumi.Input[str] token: Autogenerated Service Key token. Used to configure a Twingate Client running in headless mode.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TwingateServiceAccountKeyState.__new__(_TwingateServiceAccountKeyState)

        __props__.__dict__["name"] = name
        __props__.__dict__["service_account_id"] = service_account_id
        __props__.__dict__["token"] = token
        return TwingateServiceAccountKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Service Key
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[str]:
        """
        The id of the Service Account
        """
        return pulumi.get(self, "service_account_id")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        Autogenerated Service Key token. Used to configure a Twingate Client running in headless mode.
        """
        return pulumi.get(self, "token")
