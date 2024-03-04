'''
# AWS Transfer for SFTP Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_transfer as transfer
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnServer(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-transfer.CfnServer",
):
    '''A CloudFormation ``AWS::Transfer::Server``.

    :cloudformationResource: AWS::Transfer::Server
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        certificate: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        endpoint_details: typing.Optional[typing.Union["CfnServer.EndpointDetailsProperty", aws_cdk.core.IResolvable]] = None,
        endpoint_type: typing.Optional[builtins.str] = None,
        identity_provider_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.IdentityProviderDetailsProperty"]] = None,
        identity_provider_type: typing.Optional[builtins.str] = None,
        logging_role: typing.Optional[builtins.str] = None,
        protocol_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.ProtocolDetailsProperty"]] = None,
        protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_policy_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        workflow_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.WorkflowDetailsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::Transfer::Server``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param certificate: ``AWS::Transfer::Server.Certificate``.
        :param domain: ``AWS::Transfer::Server.Domain``.
        :param endpoint_details: ``AWS::Transfer::Server.EndpointDetails``.
        :param endpoint_type: ``AWS::Transfer::Server.EndpointType``.
        :param identity_provider_details: ``AWS::Transfer::Server.IdentityProviderDetails``.
        :param identity_provider_type: ``AWS::Transfer::Server.IdentityProviderType``.
        :param logging_role: ``AWS::Transfer::Server.LoggingRole``.
        :param protocol_details: ``AWS::Transfer::Server.ProtocolDetails``.
        :param protocols: ``AWS::Transfer::Server.Protocols``.
        :param security_policy_name: ``AWS::Transfer::Server.SecurityPolicyName``.
        :param tags: ``AWS::Transfer::Server.Tags``.
        :param workflow_details: ``AWS::Transfer::Server.WorkflowDetails``.
        '''
        props = CfnServerProps(
            certificate=certificate,
            domain=domain,
            endpoint_details=endpoint_details,
            endpoint_type=endpoint_type,
            identity_provider_details=identity_provider_details,
            identity_provider_type=identity_provider_type,
            logging_role=logging_role,
            protocol_details=protocol_details,
            protocols=protocols,
            security_policy_name=security_policy_name,
            tags=tags,
            workflow_details=workflow_details,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServerId")
    def attr_server_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Transfer::Server.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-certificate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "certificate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.Domain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-domain
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "domain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointDetails")
    def endpoint_details(
        self,
    ) -> typing.Optional[typing.Union["CfnServer.EndpointDetailsProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::Transfer::Server.EndpointDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointdetails
        '''
        return typing.cast(typing.Optional[typing.Union["CfnServer.EndpointDetailsProperty", aws_cdk.core.IResolvable]], jsii.get(self, "endpointDetails"))

    @endpoint_details.setter
    def endpoint_details(
        self,
        value: typing.Optional[typing.Union["CfnServer.EndpointDetailsProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "endpointDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.EndpointType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityProviderDetails")
    def identity_provider_details(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.IdentityProviderDetailsProperty"]]:
        '''``AWS::Transfer::Server.IdentityProviderDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityproviderdetails
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.IdentityProviderDetailsProperty"]], jsii.get(self, "identityProviderDetails"))

    @identity_provider_details.setter
    def identity_provider_details(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.IdentityProviderDetailsProperty"]],
    ) -> None:
        jsii.set(self, "identityProviderDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityProviderType")
    def identity_provider_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.IdentityProviderType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityprovidertype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderType"))

    @identity_provider_type.setter
    def identity_provider_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "identityProviderType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingRole")
    def logging_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.LoggingRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-loggingrole
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingRole"))

    @logging_role.setter
    def logging_role(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "loggingRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocolDetails")
    def protocol_details(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.ProtocolDetailsProperty"]]:
        '''``AWS::Transfer::Server.ProtocolDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocoldetails
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.ProtocolDetailsProperty"]], jsii.get(self, "protocolDetails"))

    @protocol_details.setter
    def protocol_details(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.ProtocolDetailsProperty"]],
    ) -> None:
        jsii.set(self, "protocolDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="protocols")
    def protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Transfer::Server.Protocols``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocols
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protocols"))

    @protocols.setter
    def protocols(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "protocols", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityPolicyName")
    def security_policy_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.SecurityPolicyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-securitypolicyname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyName"))

    @security_policy_name.setter
    def security_policy_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "securityPolicyName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workflowDetails")
    def workflow_details(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.WorkflowDetailsProperty"]]:
        '''``AWS::Transfer::Server.WorkflowDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-workflowdetails
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.WorkflowDetailsProperty"]], jsii.get(self, "workflowDetails"))

    @workflow_details.setter
    def workflow_details(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnServer.WorkflowDetailsProperty"]],
    ) -> None:
        jsii.set(self, "workflowDetails", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-transfer.CfnServer.EndpointDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address_allocation_ids": "addressAllocationIds",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
            "vpc_endpoint_id": "vpcEndpointId",
            "vpc_id": "vpcId",
        },
    )
    class EndpointDetailsProperty:
        def __init__(
            self,
            *,
            address_allocation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            vpc_endpoint_id: typing.Optional[builtins.str] = None,
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param address_allocation_ids: ``CfnServer.EndpointDetailsProperty.AddressAllocationIds``.
            :param security_group_ids: ``CfnServer.EndpointDetailsProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnServer.EndpointDetailsProperty.SubnetIds``.
            :param vpc_endpoint_id: ``CfnServer.EndpointDetailsProperty.VpcEndpointId``.
            :param vpc_id: ``CfnServer.EndpointDetailsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if address_allocation_ids is not None:
                self._values["address_allocation_ids"] = address_allocation_ids
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids
            if vpc_endpoint_id is not None:
                self._values["vpc_endpoint_id"] = vpc_endpoint_id
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def address_allocation_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnServer.EndpointDetailsProperty.AddressAllocationIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-addressallocationids
            '''
            result = self._values.get("address_allocation_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnServer.EndpointDetailsProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnServer.EndpointDetailsProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.EndpointDetailsProperty.VpcEndpointId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcendpointid
            '''
            result = self._values.get("vpc_endpoint_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.EndpointDetailsProperty.VpcId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-transfer.CfnServer.IdentityProviderDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_id": "directoryId",
            "invocation_role": "invocationRole",
            "url": "url",
        },
    )
    class IdentityProviderDetailsProperty:
        def __init__(
            self,
            *,
            directory_id: typing.Optional[builtins.str] = None,
            invocation_role: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param directory_id: ``CfnServer.IdentityProviderDetailsProperty.DirectoryId``.
            :param invocation_role: ``CfnServer.IdentityProviderDetailsProperty.InvocationRole``.
            :param url: ``CfnServer.IdentityProviderDetailsProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if directory_id is not None:
                self._values["directory_id"] = directory_id
            if invocation_role is not None:
                self._values["invocation_role"] = invocation_role
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def directory_id(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.IdentityProviderDetailsProperty.DirectoryId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-directoryid
            '''
            result = self._values.get("directory_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def invocation_role(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.IdentityProviderDetailsProperty.InvocationRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-invocationrole
            '''
            result = self._values.get("invocation_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.IdentityProviderDetailsProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityProviderDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-transfer.CfnServer.ProtocolDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"passive_ip": "passiveIp"},
    )
    class ProtocolDetailsProperty:
        def __init__(self, *, passive_ip: typing.Optional[builtins.str] = None) -> None:
            '''
            :param passive_ip: ``CfnServer.ProtocolDetailsProperty.PassiveIp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if passive_ip is not None:
                self._values["passive_ip"] = passive_ip

        @builtins.property
        def passive_ip(self) -> typing.Optional[builtins.str]:
            '''``CfnServer.ProtocolDetailsProperty.PassiveIp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-passiveip
            '''
            result = self._values.get("passive_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProtocolDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-transfer.CfnServer.WorkflowDetailProperty",
        jsii_struct_bases=[],
        name_mapping={"execution_role": "executionRole", "workflow_id": "workflowId"},
    )
    class WorkflowDetailProperty:
        def __init__(
            self,
            *,
            execution_role: builtins.str,
            workflow_id: builtins.str,
        ) -> None:
            '''
            :param execution_role: ``CfnServer.WorkflowDetailProperty.ExecutionRole``.
            :param workflow_id: ``CfnServer.WorkflowDetailProperty.WorkflowId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "execution_role": execution_role,
                "workflow_id": workflow_id,
            }

        @builtins.property
        def execution_role(self) -> builtins.str:
            '''``CfnServer.WorkflowDetailProperty.ExecutionRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html#cfn-transfer-server-workflowdetail-executionrole
            '''
            result = self._values.get("execution_role")
            assert result is not None, "Required property 'execution_role' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def workflow_id(self) -> builtins.str:
            '''``CfnServer.WorkflowDetailProperty.WorkflowId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html#cfn-transfer-server-workflowdetail-workflowid
            '''
            result = self._values.get("workflow_id")
            assert result is not None, "Required property 'workflow_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-transfer.CfnServer.WorkflowDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"on_upload": "onUpload"},
    )
    class WorkflowDetailsProperty:
        def __init__(
            self,
            *,
            on_upload: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnServer.WorkflowDetailProperty"]]],
        ) -> None:
            '''
            :param on_upload: ``CfnServer.WorkflowDetailsProperty.OnUpload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "on_upload": on_upload,
            }

        @builtins.property
        def on_upload(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnServer.WorkflowDetailProperty"]]]:
            '''``CfnServer.WorkflowDetailsProperty.OnUpload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html#cfn-transfer-server-workflowdetails-onupload
            '''
            result = self._values.get("on_upload")
            assert result is not None, "Required property 'on_upload' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnServer.WorkflowDetailProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-transfer.CfnServerProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "domain": "domain",
        "endpoint_details": "endpointDetails",
        "endpoint_type": "endpointType",
        "identity_provider_details": "identityProviderDetails",
        "identity_provider_type": "identityProviderType",
        "logging_role": "loggingRole",
        "protocol_details": "protocolDetails",
        "protocols": "protocols",
        "security_policy_name": "securityPolicyName",
        "tags": "tags",
        "workflow_details": "workflowDetails",
    },
)
class CfnServerProps:
    def __init__(
        self,
        *,
        certificate: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        endpoint_details: typing.Optional[typing.Union[CfnServer.EndpointDetailsProperty, aws_cdk.core.IResolvable]] = None,
        endpoint_type: typing.Optional[builtins.str] = None,
        identity_provider_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.IdentityProviderDetailsProperty]] = None,
        identity_provider_type: typing.Optional[builtins.str] = None,
        logging_role: typing.Optional[builtins.str] = None,
        protocol_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.ProtocolDetailsProperty]] = None,
        protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_policy_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        workflow_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.WorkflowDetailsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Transfer::Server``.

        :param certificate: ``AWS::Transfer::Server.Certificate``.
        :param domain: ``AWS::Transfer::Server.Domain``.
        :param endpoint_details: ``AWS::Transfer::Server.EndpointDetails``.
        :param endpoint_type: ``AWS::Transfer::Server.EndpointType``.
        :param identity_provider_details: ``AWS::Transfer::Server.IdentityProviderDetails``.
        :param identity_provider_type: ``AWS::Transfer::Server.IdentityProviderType``.
        :param logging_role: ``AWS::Transfer::Server.LoggingRole``.
        :param protocol_details: ``AWS::Transfer::Server.ProtocolDetails``.
        :param protocols: ``AWS::Transfer::Server.Protocols``.
        :param security_policy_name: ``AWS::Transfer::Server.SecurityPolicyName``.
        :param tags: ``AWS::Transfer::Server.Tags``.
        :param workflow_details: ``AWS::Transfer::Server.WorkflowDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if certificate is not None:
            self._values["certificate"] = certificate
        if domain is not None:
            self._values["domain"] = domain
        if endpoint_details is not None:
            self._values["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            self._values["endpoint_type"] = endpoint_type
        if identity_provider_details is not None:
            self._values["identity_provider_details"] = identity_provider_details
        if identity_provider_type is not None:
            self._values["identity_provider_type"] = identity_provider_type
        if logging_role is not None:
            self._values["logging_role"] = logging_role
        if protocol_details is not None:
            self._values["protocol_details"] = protocol_details
        if protocols is not None:
            self._values["protocols"] = protocols
        if security_policy_name is not None:
            self._values["security_policy_name"] = security_policy_name
        if tags is not None:
            self._values["tags"] = tags
        if workflow_details is not None:
            self._values["workflow_details"] = workflow_details

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.Domain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_details(
        self,
    ) -> typing.Optional[typing.Union[CfnServer.EndpointDetailsProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::Transfer::Server.EndpointDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointdetails
        '''
        result = self._values.get("endpoint_details")
        return typing.cast(typing.Optional[typing.Union[CfnServer.EndpointDetailsProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def endpoint_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.EndpointType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointtype
        '''
        result = self._values.get("endpoint_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_details(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.IdentityProviderDetailsProperty]]:
        '''``AWS::Transfer::Server.IdentityProviderDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityproviderdetails
        '''
        result = self._values.get("identity_provider_details")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.IdentityProviderDetailsProperty]], result)

    @builtins.property
    def identity_provider_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.IdentityProviderType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityprovidertype
        '''
        result = self._values.get("identity_provider_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.LoggingRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-loggingrole
        '''
        result = self._values.get("logging_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol_details(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.ProtocolDetailsProperty]]:
        '''``AWS::Transfer::Server.ProtocolDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocoldetails
        '''
        result = self._values.get("protocol_details")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.ProtocolDetailsProperty]], result)

    @builtins.property
    def protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Transfer::Server.Protocols``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocols
        '''
        result = self._values.get("protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_policy_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::Server.SecurityPolicyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-securitypolicyname
        '''
        result = self._values.get("security_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Transfer::Server.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def workflow_details(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.WorkflowDetailsProperty]]:
        '''``AWS::Transfer::Server.WorkflowDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-workflowdetails
        '''
        result = self._values.get("workflow_details")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnServer.WorkflowDetailsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnUser(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-transfer.CfnUser",
):
    '''A CloudFormation ``AWS::Transfer::User``.

    :cloudformationResource: AWS::Transfer::User
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        role: builtins.str,
        server_id: builtins.str,
        user_name: builtins.str,
        home_directory: typing.Optional[builtins.str] = None,
        home_directory_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnUser.HomeDirectoryMapEntryProperty"]]]] = None,
        home_directory_type: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        posix_profile: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUser.PosixProfileProperty"]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Transfer::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param role: ``AWS::Transfer::User.Role``.
        :param server_id: ``AWS::Transfer::User.ServerId``.
        :param user_name: ``AWS::Transfer::User.UserName``.
        :param home_directory: ``AWS::Transfer::User.HomeDirectory``.
        :param home_directory_mappings: ``AWS::Transfer::User.HomeDirectoryMappings``.
        :param home_directory_type: ``AWS::Transfer::User.HomeDirectoryType``.
        :param policy: ``AWS::Transfer::User.Policy``.
        :param posix_profile: ``AWS::Transfer::User.PosixProfile``.
        :param ssh_public_keys: ``AWS::Transfer::User.SshPublicKeys``.
        :param tags: ``AWS::Transfer::User.Tags``.
        '''
        props = CfnUserProps(
            role=role,
            server_id=server_id,
            user_name=user_name,
            home_directory=home_directory,
            home_directory_mappings=home_directory_mappings,
            home_directory_type=home_directory_type,
            policy=policy,
            posix_profile=posix_profile,
            ssh_public_keys=ssh_public_keys,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServerId")
    def attr_server_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUserName")
    def attr_user_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: UserName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Transfer::User.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''``AWS::Transfer::User.Role``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role
        '''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        jsii.set(self, "role", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> builtins.str:
        '''``AWS::Transfer::User.ServerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid
        '''
        return typing.cast(builtins.str, jsii.get(self, "serverId"))

    @server_id.setter
    def server_id(self, value: builtins.str) -> None:
        jsii.set(self, "serverId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''``AWS::Transfer::User.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username
        '''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        jsii.set(self, "userName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="homeDirectory")
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.HomeDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectory"))

    @home_directory.setter
    def home_directory(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "homeDirectory", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="homeDirectoryMappings")
    def home_directory_mappings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUser.HomeDirectoryMapEntryProperty"]]]]:
        '''``AWS::Transfer::User.HomeDirectoryMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorymappings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUser.HomeDirectoryMapEntryProperty"]]]], jsii.get(self, "homeDirectoryMappings"))

    @home_directory_mappings.setter
    def home_directory_mappings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUser.HomeDirectoryMapEntryProperty"]]]],
    ) -> None:
        jsii.set(self, "homeDirectoryMappings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="homeDirectoryType")
    def home_directory_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.HomeDirectoryType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorytype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectoryType"))

    @home_directory_type.setter
    def home_directory_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "homeDirectoryType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "policy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="posixProfile")
    def posix_profile(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUser.PosixProfileProperty"]]:
        '''``AWS::Transfer::User.PosixProfile``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-posixprofile
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUser.PosixProfileProperty"]], jsii.get(self, "posixProfile"))

    @posix_profile.setter
    def posix_profile(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUser.PosixProfileProperty"]],
    ) -> None:
        jsii.set(self, "posixProfile", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Transfer::User.SshPublicKeys``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "sshPublicKeys", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-transfer.CfnUser.HomeDirectoryMapEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"entry": "entry", "target": "target"},
    )
    class HomeDirectoryMapEntryProperty:
        def __init__(self, *, entry: builtins.str, target: builtins.str) -> None:
            '''
            :param entry: ``CfnUser.HomeDirectoryMapEntryProperty.Entry``.
            :param target: ``CfnUser.HomeDirectoryMapEntryProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "entry": entry,
                "target": target,
            }

        @builtins.property
        def entry(self) -> builtins.str:
            '''``CfnUser.HomeDirectoryMapEntryProperty.Entry``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-entry
            '''
            result = self._values.get("entry")
            assert result is not None, "Required property 'entry' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''``CfnUser.HomeDirectoryMapEntryProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HomeDirectoryMapEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-transfer.CfnUser.PosixProfileProperty",
        jsii_struct_bases=[],
        name_mapping={"gid": "gid", "uid": "uid", "secondary_gids": "secondaryGids"},
    )
    class PosixProfileProperty:
        def __init__(
            self,
            *,
            gid: jsii.Number,
            uid: jsii.Number,
            secondary_gids: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[jsii.Number]]] = None,
        ) -> None:
            '''
            :param gid: ``CfnUser.PosixProfileProperty.Gid``.
            :param uid: ``CfnUser.PosixProfileProperty.Uid``.
            :param secondary_gids: ``CfnUser.PosixProfileProperty.SecondaryGids``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "gid": gid,
                "uid": uid,
            }
            if secondary_gids is not None:
                self._values["secondary_gids"] = secondary_gids

        @builtins.property
        def gid(self) -> jsii.Number:
            '''``CfnUser.PosixProfileProperty.Gid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-gid
            '''
            result = self._values.get("gid")
            assert result is not None, "Required property 'gid' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def uid(self) -> jsii.Number:
            '''``CfnUser.PosixProfileProperty.Uid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-uid
            '''
            result = self._values.get("uid")
            assert result is not None, "Required property 'uid' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def secondary_gids(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]]:
            '''``CfnUser.PosixProfileProperty.SecondaryGids``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-secondarygids
            '''
            result = self._values.get("secondary_gids")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[jsii.Number]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PosixProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-transfer.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "role": "role",
        "server_id": "serverId",
        "user_name": "userName",
        "home_directory": "homeDirectory",
        "home_directory_mappings": "homeDirectoryMappings",
        "home_directory_type": "homeDirectoryType",
        "policy": "policy",
        "posix_profile": "posixProfile",
        "ssh_public_keys": "sshPublicKeys",
        "tags": "tags",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        role: builtins.str,
        server_id: builtins.str,
        user_name: builtins.str,
        home_directory: typing.Optional[builtins.str] = None,
        home_directory_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnUser.HomeDirectoryMapEntryProperty]]]] = None,
        home_directory_type: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        posix_profile: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUser.PosixProfileProperty]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Transfer::User``.

        :param role: ``AWS::Transfer::User.Role``.
        :param server_id: ``AWS::Transfer::User.ServerId``.
        :param user_name: ``AWS::Transfer::User.UserName``.
        :param home_directory: ``AWS::Transfer::User.HomeDirectory``.
        :param home_directory_mappings: ``AWS::Transfer::User.HomeDirectoryMappings``.
        :param home_directory_type: ``AWS::Transfer::User.HomeDirectoryType``.
        :param policy: ``AWS::Transfer::User.Policy``.
        :param posix_profile: ``AWS::Transfer::User.PosixProfile``.
        :param ssh_public_keys: ``AWS::Transfer::User.SshPublicKeys``.
        :param tags: ``AWS::Transfer::User.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "role": role,
            "server_id": server_id,
            "user_name": user_name,
        }
        if home_directory is not None:
            self._values["home_directory"] = home_directory
        if home_directory_mappings is not None:
            self._values["home_directory_mappings"] = home_directory_mappings
        if home_directory_type is not None:
            self._values["home_directory_type"] = home_directory_type
        if policy is not None:
            self._values["policy"] = policy
        if posix_profile is not None:
            self._values["posix_profile"] = posix_profile
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def role(self) -> builtins.str:
        '''``AWS::Transfer::User.Role``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_id(self) -> builtins.str:
        '''``AWS::Transfer::User.ServerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid
        '''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''``AWS::Transfer::User.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.HomeDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory
        '''
        result = self._values.get("home_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_directory_mappings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnUser.HomeDirectoryMapEntryProperty]]]]:
        '''``AWS::Transfer::User.HomeDirectoryMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorymappings
        '''
        result = self._values.get("home_directory_mappings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnUser.HomeDirectoryMapEntryProperty]]]], result)

    @builtins.property
    def home_directory_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.HomeDirectoryType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorytype
        '''
        result = self._values.get("home_directory_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''``AWS::Transfer::User.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_profile(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUser.PosixProfileProperty]]:
        '''``AWS::Transfer::User.PosixProfile``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-posixprofile
        '''
        result = self._values.get("posix_profile")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUser.PosixProfileProperty]], result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Transfer::User.SshPublicKeys``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys
        '''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Transfer::User.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnServer",
    "CfnServerProps",
    "CfnUser",
    "CfnUserProps",
]

publication.publish()
