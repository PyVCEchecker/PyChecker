'''
# Amazon ECS Service Discovery Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

This package contains constructs for working with **AWS Cloud Map**

AWS Cloud Map is a fully managed service that you can use to create and
maintain a map of the backend services and resources that your applications
depend on.

For further information on AWS Cloud Map,
see the [AWS Cloud Map documentation](https://docs.aws.amazon.com/cloud-map)

## HTTP Namespace Example

The following example creates an AWS Cloud Map namespace that
supports API calls, creates a service in that namespace, and
registers an instance to it:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
import ...lib as servicediscovery

app = cdk.App()
stack = cdk.Stack(app, "aws-servicediscovery-integ")

namespace = servicediscovery.HttpNamespace(stack, "MyNamespace",
    name="covfefe"
)

service1 = namespace.create_service("NonIpService",
    description="service registering non-ip instances"
)

service1.register_non_ip_instance("NonIpInstance",
    custom_attributes={"arn": "arn:aws:s3:::mybucket"}
)

service2 = namespace.create_service("IpService",
    description="service registering ip instances",
    health_check=HealthCheckConfig(
        type=servicediscovery.HealthCheckType.HTTP,
        resource_path="/check"
    )
)

service2.register_ip_instance("IpInstance",
    ipv4="54.239.25.192"
)

app.synth()
```

## Private DNS Namespace Example

The following example creates an AWS Cloud Map namespace that
supports both API calls and DNS queries within a vpc, creates a
service in that namespace, and registers a loadbalancer as an
instance:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_elasticloadbalancingv2 as elbv2
import aws_cdk.core as cdk
import ...lib as servicediscovery

app = cdk.App()
stack = cdk.Stack(app, "aws-servicediscovery-integ")

vpc = ec2.Vpc(stack, "Vpc", max_azs=2)

namespace = servicediscovery.PrivateDnsNamespace(stack, "Namespace",
    name="boobar.com",
    vpc=vpc
)

service = namespace.create_service("Service",
    dns_record_type=servicediscovery.DnsRecordType.A_AAAA,
    dns_ttl=cdk.Duration.seconds(30),
    load_balancer=True
)

loadbalancer = elbv2.ApplicationLoadBalancer(stack, "LB", vpc=vpc, internet_facing=True)

service.register_load_balancer("Loadbalancer", loadbalancer)

app.synth()
```

## Public DNS Namespace Example

The following example creates an AWS Cloud Map namespace that
supports both API calls and public DNS queries, creates a service in
that namespace, and registers an IP instance:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
import ...lib as servicediscovery

app = cdk.App()
stack = cdk.Stack(app, "aws-servicediscovery-integ")

namespace = servicediscovery.PublicDnsNamespace(stack, "Namespace",
    name="foobar.com"
)

service = namespace.create_service("Service",
    name="foo",
    dns_record_type=servicediscovery.DnsRecordType.A,
    dns_ttl=cdk.Duration.seconds(30),
    health_check=HealthCheckConfig(
        type=servicediscovery.HealthCheckType.HTTPS,
        resource_path="/healthcheck",
        failure_threshold=2
    )
)

service.register_ip_instance("IpInstance",
    ipv4="54.239.25.192",
    port=443
)

app.synth()
```

For DNS namespaces, you can also register instances to services with CNAME records:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
import ...lib as servicediscovery

app = cdk.App()
stack = cdk.Stack(app, "aws-servicediscovery-integ")

namespace = servicediscovery.PublicDnsNamespace(stack, "Namespace",
    name="foobar.com"
)

service = namespace.create_service("Service",
    name="foo",
    dns_record_type=servicediscovery.DnsRecordType.CNAME,
    dns_ttl=cdk.Duration.seconds(30)
)

service.register_cname_instance("CnameInstance",
    instance_cname="service.pizza"
)

app.synth()
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

import aws_cdk.aws_ec2
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.core
import constructs


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.BaseInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "custom_attributes": "customAttributes",
        "instance_id": "instanceId",
    },
)
class BaseInstanceProps:
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Used when the resource that's associated with the service instance is accessible using values other than an IP address or a domain name (CNAME), i.e. for non-ip-instances.

        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if instance_id is not None:
            self._values["instance_id"] = instance_id

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom attributes of the instance.

        :default: none
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The id of the instance resource.

        :default: Automatically generated name
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.BaseNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description"},
)
class BaseNamespaceProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: A name for the Namespace.
        :param description: A description of the Namespace. Default: none
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the Namespace.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the Namespace.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.BaseServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "custom_health_check": "customHealthCheck",
        "description": "description",
        "health_check": "healthCheck",
        "name": "name",
    },
)
class BaseServiceProps:
    def __init__(
        self,
        *,
        custom_health_check: typing.Optional["HealthCheckCustomConfig"] = None,
        description: typing.Optional[builtins.str] = None,
        health_check: typing.Optional["HealthCheckConfig"] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Basic props needed to create a service in a given namespace.

        Used by HttpNamespace.createService

        :param custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html Default: none
        :param description: A description of the service. Default: none
        :param health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
        :param name: A name for the Service. Default: CloudFormation-generated name
        '''
        if isinstance(custom_health_check, dict):
            custom_health_check = HealthCheckCustomConfig(**custom_health_check)
        if isinstance(health_check, dict):
            health_check = HealthCheckConfig(**health_check)
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_health_check is not None:
            self._values["custom_health_check"] = custom_health_check
        if description is not None:
            self._values["description"] = description
        if health_check is not None:
            self._values["health_check"] = health_check
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def custom_health_check(self) -> typing.Optional["HealthCheckCustomConfig"]:
        '''Structure containing failure threshold for a custom health checker.

        Only one of healthCheckConfig or healthCheckCustomConfig can be specified.
        See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html

        :default: none
        '''
        result = self._values.get("custom_health_check")
        return typing.cast(typing.Optional["HealthCheckCustomConfig"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check(self) -> typing.Optional["HealthCheckConfig"]:
        '''Settings for an optional health check.

        If you specify health check settings, AWS Cloud Map associates the health
        check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can
        be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to
        this service.

        :default: none
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["HealthCheckConfig"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the Service.

        :default: CloudFormation-generated name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnHttpNamespace(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.CfnHttpNamespace",
):
    '''A CloudFormation ``AWS::ServiceDiscovery::HttpNamespace``.

    :cloudformationResource: AWS::ServiceDiscovery::HttpNamespace
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceDiscovery::HttpNamespace``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::ServiceDiscovery::HttpNamespace.Name``.
        :param description: ``AWS::ServiceDiscovery::HttpNamespace.Description``.
        :param tags: ``AWS::ServiceDiscovery::HttpNamespace.Tags``.
        '''
        props = CfnHttpNamespaceProps(name=name, description=description, tags=tags)

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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ServiceDiscovery::HttpNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::HttpNamespace.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::HttpNamespace.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.CfnHttpNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnHttpNamespaceProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ServiceDiscovery::HttpNamespace``.

        :param name: ``AWS::ServiceDiscovery::HttpNamespace.Name``.
        :param description: ``AWS::ServiceDiscovery::HttpNamespace.Description``.
        :param tags: ``AWS::ServiceDiscovery::HttpNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::HttpNamespace.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::HttpNamespace.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ServiceDiscovery::HttpNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHttpNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInstance(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.CfnInstance",
):
    '''A CloudFormation ``AWS::ServiceDiscovery::Instance``.

    :cloudformationResource: AWS::ServiceDiscovery::Instance
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_attributes: typing.Any,
        service_id: builtins.str,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceDiscovery::Instance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_attributes: ``AWS::ServiceDiscovery::Instance.InstanceAttributes``.
        :param service_id: ``AWS::ServiceDiscovery::Instance.ServiceId``.
        :param instance_id: ``AWS::ServiceDiscovery::Instance.InstanceId``.
        '''
        props = CfnInstanceProps(
            instance_attributes=instance_attributes,
            service_id=service_id,
            instance_id=instance_id,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceAttributes")
    def instance_attributes(self) -> typing.Any:
        '''``AWS::ServiceDiscovery::Instance.InstanceAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceattributes
        '''
        return typing.cast(typing.Any, jsii.get(self, "instanceAttributes"))

    @instance_attributes.setter
    def instance_attributes(self, value: typing.Any) -> None:
        jsii.set(self, "instanceAttributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::Instance.ServiceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-serviceid
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceId"))

    @service_id.setter
    def service_id(self, value: builtins.str) -> None:
        jsii.set(self, "serviceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Instance.InstanceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "instanceId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.CfnInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_attributes": "instanceAttributes",
        "service_id": "serviceId",
        "instance_id": "instanceId",
    },
)
class CfnInstanceProps:
    def __init__(
        self,
        *,
        instance_attributes: typing.Any,
        service_id: builtins.str,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ServiceDiscovery::Instance``.

        :param instance_attributes: ``AWS::ServiceDiscovery::Instance.InstanceAttributes``.
        :param service_id: ``AWS::ServiceDiscovery::Instance.ServiceId``.
        :param instance_id: ``AWS::ServiceDiscovery::Instance.InstanceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_attributes": instance_attributes,
            "service_id": service_id,
        }
        if instance_id is not None:
            self._values["instance_id"] = instance_id

    @builtins.property
    def instance_attributes(self) -> typing.Any:
        '''``AWS::ServiceDiscovery::Instance.InstanceAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceattributes
        '''
        result = self._values.get("instance_attributes")
        assert result is not None, "Required property 'instance_attributes' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def service_id(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::Instance.ServiceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-serviceid
        '''
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Instance.InstanceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceid
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPrivateDnsNamespace(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.CfnPrivateDnsNamespace",
):
    '''A CloudFormation ``AWS::ServiceDiscovery::PrivateDnsNamespace``.

    :cloudformationResource: AWS::ServiceDiscovery::PrivateDnsNamespace
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        vpc: builtins.str,
        description: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.PropertiesProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceDiscovery::PrivateDnsNamespace``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Name``.
        :param vpc: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Vpc``.
        :param description: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Description``.
        :param properties: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Properties``.
        :param tags: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Tags``.
        '''
        props = CfnPrivateDnsNamespaceProps(
            name=name,
            vpc=vpc,
            description=description,
            properties=properties,
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Vpc``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-vpc
        '''
        return typing.cast(builtins.str, jsii.get(self, "vpc"))

    @vpc.setter
    def vpc(self, value: builtins.str) -> None:
        jsii.set(self, "vpc", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="properties")
    def properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.PropertiesProperty"]]:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Properties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-properties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.PropertiesProperty"]], jsii.get(self, "properties"))

    @properties.setter
    def properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.PropertiesProperty"]],
    ) -> None:
        jsii.set(self, "properties", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnPrivateDnsNamespace.PrivateDnsPropertiesMutableProperty",
        jsii_struct_bases=[],
        name_mapping={"soa": "soa"},
    )
    class PrivateDnsPropertiesMutableProperty:
        def __init__(
            self,
            *,
            soa: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.SOAProperty"]] = None,
        ) -> None:
            '''
            :param soa: ``CfnPrivateDnsNamespace.PrivateDnsPropertiesMutableProperty.SOA``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-privatednspropertiesmutable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if soa is not None:
                self._values["soa"] = soa

        @builtins.property
        def soa(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.SOAProperty"]]:
            '''``CfnPrivateDnsNamespace.PrivateDnsPropertiesMutableProperty.SOA``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-privatednspropertiesmutable.html#cfn-servicediscovery-privatednsnamespace-privatednspropertiesmutable-soa
            '''
            result = self._values.get("soa")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.SOAProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivateDnsPropertiesMutableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnPrivateDnsNamespace.PropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"dns_properties": "dnsProperties"},
    )
    class PropertiesProperty:
        def __init__(
            self,
            *,
            dns_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.PrivateDnsPropertiesMutableProperty"]] = None,
        ) -> None:
            '''
            :param dns_properties: ``CfnPrivateDnsNamespace.PropertiesProperty.DnsProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-properties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dns_properties is not None:
                self._values["dns_properties"] = dns_properties

        @builtins.property
        def dns_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.PrivateDnsPropertiesMutableProperty"]]:
            '''``CfnPrivateDnsNamespace.PropertiesProperty.DnsProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-properties.html#cfn-servicediscovery-privatednsnamespace-properties-dnsproperties
            '''
            result = self._values.get("dns_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPrivateDnsNamespace.PrivateDnsPropertiesMutableProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnPrivateDnsNamespace.SOAProperty",
        jsii_struct_bases=[],
        name_mapping={"ttl": "ttl"},
    )
    class SOAProperty:
        def __init__(self, *, ttl: typing.Optional[jsii.Number] = None) -> None:
            '''
            :param ttl: ``CfnPrivateDnsNamespace.SOAProperty.TTL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-soa.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ttl is not None:
                self._values["ttl"] = ttl

        @builtins.property
        def ttl(self) -> typing.Optional[jsii.Number]:
            '''``CfnPrivateDnsNamespace.SOAProperty.TTL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-privatednsnamespace-soa.html#cfn-servicediscovery-privatednsnamespace-soa-ttl
            '''
            result = self._values.get("ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SOAProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.CfnPrivateDnsNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "vpc": "vpc",
        "description": "description",
        "properties": "properties",
        "tags": "tags",
    },
)
class CfnPrivateDnsNamespaceProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        vpc: builtins.str,
        description: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPrivateDnsNamespace.PropertiesProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ServiceDiscovery::PrivateDnsNamespace``.

        :param name: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Name``.
        :param vpc: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Vpc``.
        :param description: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Description``.
        :param properties: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Properties``.
        :param tags: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "vpc": vpc,
        }
        if description is not None:
            self._values["description"] = description
        if properties is not None:
            self._values["properties"] = properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Vpc``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-vpc
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPrivateDnsNamespace.PropertiesProperty]]:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Properties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPrivateDnsNamespace.PropertiesProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ServiceDiscovery::PrivateDnsNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrivateDnsNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPublicDnsNamespace(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.CfnPublicDnsNamespace",
):
    '''A CloudFormation ``AWS::ServiceDiscovery::PublicDnsNamespace``.

    :cloudformationResource: AWS::ServiceDiscovery::PublicDnsNamespace
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.PropertiesProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceDiscovery::PublicDnsNamespace``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::ServiceDiscovery::PublicDnsNamespace.Name``.
        :param description: ``AWS::ServiceDiscovery::PublicDnsNamespace.Description``.
        :param properties: ``AWS::ServiceDiscovery::PublicDnsNamespace.Properties``.
        :param tags: ``AWS::ServiceDiscovery::PublicDnsNamespace.Tags``.
        '''
        props = CfnPublicDnsNamespaceProps(
            name=name, description=description, properties=properties, tags=tags
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ServiceDiscovery::PublicDnsNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::PublicDnsNamespace.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::PublicDnsNamespace.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="properties")
    def properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.PropertiesProperty"]]:
        '''``AWS::ServiceDiscovery::PublicDnsNamespace.Properties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-properties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.PropertiesProperty"]], jsii.get(self, "properties"))

    @properties.setter
    def properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.PropertiesProperty"]],
    ) -> None:
        jsii.set(self, "properties", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnPublicDnsNamespace.PropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"dns_properties": "dnsProperties"},
    )
    class PropertiesProperty:
        def __init__(
            self,
            *,
            dns_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.PublicDnsPropertiesMutableProperty"]] = None,
        ) -> None:
            '''
            :param dns_properties: ``CfnPublicDnsNamespace.PropertiesProperty.DnsProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-properties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dns_properties is not None:
                self._values["dns_properties"] = dns_properties

        @builtins.property
        def dns_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.PublicDnsPropertiesMutableProperty"]]:
            '''``CfnPublicDnsNamespace.PropertiesProperty.DnsProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-properties.html#cfn-servicediscovery-publicdnsnamespace-properties-dnsproperties
            '''
            result = self._values.get("dns_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.PublicDnsPropertiesMutableProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnPublicDnsNamespace.PublicDnsPropertiesMutableProperty",
        jsii_struct_bases=[],
        name_mapping={"soa": "soa"},
    )
    class PublicDnsPropertiesMutableProperty:
        def __init__(
            self,
            *,
            soa: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.SOAProperty"]] = None,
        ) -> None:
            '''
            :param soa: ``CfnPublicDnsNamespace.PublicDnsPropertiesMutableProperty.SOA``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-publicdnspropertiesmutable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if soa is not None:
                self._values["soa"] = soa

        @builtins.property
        def soa(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.SOAProperty"]]:
            '''``CfnPublicDnsNamespace.PublicDnsPropertiesMutableProperty.SOA``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-publicdnspropertiesmutable.html#cfn-servicediscovery-publicdnsnamespace-publicdnspropertiesmutable-soa
            '''
            result = self._values.get("soa")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPublicDnsNamespace.SOAProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublicDnsPropertiesMutableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnPublicDnsNamespace.SOAProperty",
        jsii_struct_bases=[],
        name_mapping={"ttl": "ttl"},
    )
    class SOAProperty:
        def __init__(self, *, ttl: typing.Optional[jsii.Number] = None) -> None:
            '''
            :param ttl: ``CfnPublicDnsNamespace.SOAProperty.TTL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-soa.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ttl is not None:
                self._values["ttl"] = ttl

        @builtins.property
        def ttl(self) -> typing.Optional[jsii.Number]:
            '''``CfnPublicDnsNamespace.SOAProperty.TTL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-publicdnsnamespace-soa.html#cfn-servicediscovery-publicdnsnamespace-soa-ttl
            '''
            result = self._values.get("ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SOAProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.CfnPublicDnsNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "properties": "properties",
        "tags": "tags",
    },
)
class CfnPublicDnsNamespaceProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPublicDnsNamespace.PropertiesProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ServiceDiscovery::PublicDnsNamespace``.

        :param name: ``AWS::ServiceDiscovery::PublicDnsNamespace.Name``.
        :param description: ``AWS::ServiceDiscovery::PublicDnsNamespace.Description``.
        :param properties: ``AWS::ServiceDiscovery::PublicDnsNamespace.Properties``.
        :param tags: ``AWS::ServiceDiscovery::PublicDnsNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if properties is not None:
            self._values["properties"] = properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ServiceDiscovery::PublicDnsNamespace.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::PublicDnsNamespace.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPublicDnsNamespace.PropertiesProperty]]:
        '''``AWS::ServiceDiscovery::PublicDnsNamespace.Properties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPublicDnsNamespace.PropertiesProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ServiceDiscovery::PublicDnsNamespace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublicDnsNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnService(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.CfnService",
):
    '''A CloudFormation ``AWS::ServiceDiscovery::Service``.

    :cloudformationResource: AWS::ServiceDiscovery::Service
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        dns_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsConfigProperty"]] = None,
        health_check_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigProperty"]] = None,
        health_check_custom_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckCustomConfigProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ServiceDiscovery::Service``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::ServiceDiscovery::Service.Description``.
        :param dns_config: ``AWS::ServiceDiscovery::Service.DnsConfig``.
        :param health_check_config: ``AWS::ServiceDiscovery::Service.HealthCheckConfig``.
        :param health_check_custom_config: ``AWS::ServiceDiscovery::Service.HealthCheckCustomConfig``.
        :param name: ``AWS::ServiceDiscovery::Service.Name``.
        :param namespace_id: ``AWS::ServiceDiscovery::Service.NamespaceId``.
        :param tags: ``AWS::ServiceDiscovery::Service.Tags``.
        :param type: ``AWS::ServiceDiscovery::Service.Type``.
        '''
        props = CfnServiceProps(
            description=description,
            dns_config=dns_config,
            health_check_config=health_check_config,
            health_check_custom_config=health_check_custom_config,
            name=name,
            namespace_id=namespace_id,
            tags=tags,
            type=type,
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ServiceDiscovery::Service.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Service.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsConfig")
    def dns_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsConfigProperty"]]:
        '''``AWS::ServiceDiscovery::Service.DnsConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-dnsconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsConfigProperty"]], jsii.get(self, "dnsConfig"))

    @dns_config.setter
    def dns_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsConfigProperty"]],
    ) -> None:
        jsii.set(self, "dnsConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckConfig")
    def health_check_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigProperty"]]:
        '''``AWS::ServiceDiscovery::Service.HealthCheckConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigProperty"]], jsii.get(self, "healthCheckConfig"))

    @health_check_config.setter
    def health_check_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigProperty"]],
    ) -> None:
        jsii.set(self, "healthCheckConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="healthCheckCustomConfig")
    def health_check_custom_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckCustomConfigProperty"]]:
        '''``AWS::ServiceDiscovery::Service.HealthCheckCustomConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckcustomconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckCustomConfigProperty"]], jsii.get(self, "healthCheckCustomConfig"))

    @health_check_custom_config.setter
    def health_check_custom_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckCustomConfigProperty"]],
    ) -> None:
        jsii.set(self, "healthCheckCustomConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Service.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Service.NamespaceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-namespaceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceId"))

    @namespace_id.setter
    def namespace_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "namespaceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Service.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnService.DnsConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_records": "dnsRecords",
            "namespace_id": "namespaceId",
            "routing_policy": "routingPolicy",
        },
    )
    class DnsConfigProperty:
        def __init__(
            self,
            *,
            dns_records: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsRecordProperty"]]],
            namespace_id: typing.Optional[builtins.str] = None,
            routing_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param dns_records: ``CfnService.DnsConfigProperty.DnsRecords``.
            :param namespace_id: ``CfnService.DnsConfigProperty.NamespaceId``.
            :param routing_policy: ``CfnService.DnsConfigProperty.RoutingPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "dns_records": dns_records,
            }
            if namespace_id is not None:
                self._values["namespace_id"] = namespace_id
            if routing_policy is not None:
                self._values["routing_policy"] = routing_policy

        @builtins.property
        def dns_records(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsRecordProperty"]]]:
            '''``CfnService.DnsConfigProperty.DnsRecords``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-dnsrecords
            '''
            result = self._values.get("dns_records")
            assert result is not None, "Required property 'dns_records' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsRecordProperty"]]], result)

        @builtins.property
        def namespace_id(self) -> typing.Optional[builtins.str]:
            '''``CfnService.DnsConfigProperty.NamespaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-namespaceid
            '''
            result = self._values.get("namespace_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def routing_policy(self) -> typing.Optional[builtins.str]:
            '''``CfnService.DnsConfigProperty.RoutingPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-routingpolicy
            '''
            result = self._values.get("routing_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DnsConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnService.DnsRecordProperty",
        jsii_struct_bases=[],
        name_mapping={"ttl": "ttl", "type": "type"},
    )
    class DnsRecordProperty:
        def __init__(self, *, ttl: jsii.Number, type: builtins.str) -> None:
            '''
            :param ttl: ``CfnService.DnsRecordProperty.TTL``.
            :param type: ``CfnService.DnsRecordProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "ttl": ttl,
                "type": type,
            }

        @builtins.property
        def ttl(self) -> jsii.Number:
            '''``CfnService.DnsRecordProperty.TTL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html#cfn-servicediscovery-service-dnsrecord-ttl
            '''
            result = self._values.get("ttl")
            assert result is not None, "Required property 'ttl' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnService.DnsRecordProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html#cfn-servicediscovery-service-dnsrecord-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DnsRecordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnService.HealthCheckConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "failure_threshold": "failureThreshold",
            "resource_path": "resourcePath",
        },
    )
    class HealthCheckConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            failure_threshold: typing.Optional[jsii.Number] = None,
            resource_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: ``CfnService.HealthCheckConfigProperty.Type``.
            :param failure_threshold: ``CfnService.HealthCheckConfigProperty.FailureThreshold``.
            :param resource_path: ``CfnService.HealthCheckConfigProperty.ResourcePath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if failure_threshold is not None:
                self._values["failure_threshold"] = failure_threshold
            if resource_path is not None:
                self._values["resource_path"] = resource_path

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnService.HealthCheckConfigProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def failure_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckConfigProperty.FailureThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-failurethreshold
            '''
            result = self._values.get("failure_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def resource_path(self) -> typing.Optional[builtins.str]:
            '''``CfnService.HealthCheckConfigProperty.ResourcePath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-resourcepath
            '''
            result = self._values.get("resource_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-servicediscovery.CfnService.HealthCheckCustomConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"failure_threshold": "failureThreshold"},
    )
    class HealthCheckCustomConfigProperty:
        def __init__(
            self,
            *,
            failure_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param failure_threshold: ``CfnService.HealthCheckCustomConfigProperty.FailureThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if failure_threshold is not None:
                self._values["failure_threshold"] = failure_threshold

        @builtins.property
        def failure_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnService.HealthCheckCustomConfigProperty.FailureThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html#cfn-servicediscovery-service-healthcheckcustomconfig-failurethreshold
            '''
            result = self._values.get("failure_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckCustomConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "dns_config": "dnsConfig",
        "health_check_config": "healthCheckConfig",
        "health_check_custom_config": "healthCheckCustomConfig",
        "name": "name",
        "namespace_id": "namespaceId",
        "tags": "tags",
        "type": "type",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        dns_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.DnsConfigProperty]] = None,
        health_check_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigProperty]] = None,
        health_check_custom_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckCustomConfigProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ServiceDiscovery::Service``.

        :param description: ``AWS::ServiceDiscovery::Service.Description``.
        :param dns_config: ``AWS::ServiceDiscovery::Service.DnsConfig``.
        :param health_check_config: ``AWS::ServiceDiscovery::Service.HealthCheckConfig``.
        :param health_check_custom_config: ``AWS::ServiceDiscovery::Service.HealthCheckCustomConfig``.
        :param name: ``AWS::ServiceDiscovery::Service.Name``.
        :param namespace_id: ``AWS::ServiceDiscovery::Service.NamespaceId``.
        :param tags: ``AWS::ServiceDiscovery::Service.Tags``.
        :param type: ``AWS::ServiceDiscovery::Service.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if dns_config is not None:
            self._values["dns_config"] = dns_config
        if health_check_config is not None:
            self._values["health_check_config"] = health_check_config
        if health_check_custom_config is not None:
            self._values["health_check_custom_config"] = health_check_custom_config
        if name is not None:
            self._values["name"] = name
        if namespace_id is not None:
            self._values["namespace_id"] = namespace_id
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Service.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.DnsConfigProperty]]:
        '''``AWS::ServiceDiscovery::Service.DnsConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-dnsconfig
        '''
        result = self._values.get("dns_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.DnsConfigProperty]], result)

    @builtins.property
    def health_check_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigProperty]]:
        '''``AWS::ServiceDiscovery::Service.HealthCheckConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckconfig
        '''
        result = self._values.get("health_check_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckConfigProperty]], result)

    @builtins.property
    def health_check_custom_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckCustomConfigProperty]]:
        '''``AWS::ServiceDiscovery::Service.HealthCheckCustomConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckcustomconfig
        '''
        result = self._values.get("health_check_custom_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnService.HealthCheckCustomConfigProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Service.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Service.NamespaceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-namespaceid
        '''
        result = self._values.get("namespace_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ServiceDiscovery::Service.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::ServiceDiscovery::Service.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.CnameInstanceBaseProps",
    jsii_struct_bases=[BaseInstanceProps],
    name_mapping={
        "custom_attributes": "customAttributes",
        "instance_id": "instanceId",
        "instance_cname": "instanceCname",
    },
)
class CnameInstanceBaseProps(BaseInstanceProps):
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
        instance_cname: builtins.str,
    ) -> None:
        '''
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        :param instance_cname: If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_cname": instance_cname,
        }
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if instance_id is not None:
            self._values["instance_id"] = instance_id

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom attributes of the instance.

        :default: none
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The id of the instance resource.

        :default: Automatically generated name
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_cname(self) -> builtins.str:
        '''If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.'''
        result = self._values.get("instance_cname")
        assert result is not None, "Required property 'instance_cname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CnameInstanceBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.CnameInstanceProps",
    jsii_struct_bases=[CnameInstanceBaseProps],
    name_mapping={
        "custom_attributes": "customAttributes",
        "instance_id": "instanceId",
        "instance_cname": "instanceCname",
        "service": "service",
    },
)
class CnameInstanceProps(CnameInstanceBaseProps):
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
        instance_cname: builtins.str,
        service: "IService",
    ) -> None:
        '''
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        :param instance_cname: If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.
        :param service: The Cloudmap service this resource is registered to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_cname": instance_cname,
            "service": service,
        }
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if instance_id is not None:
            self._values["instance_id"] = instance_id

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom attributes of the instance.

        :default: none
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The id of the instance resource.

        :default: Automatically generated name
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_cname(self) -> builtins.str:
        '''If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.'''
        result = self._values.get("instance_cname")
        assert result is not None, "Required property 'instance_cname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> "IService":
        '''The Cloudmap service this resource is registered to.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast("IService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CnameInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-servicediscovery.DnsRecordType")
class DnsRecordType(enum.Enum):
    A = "A"
    '''An A record.'''
    AAAA = "AAAA"
    '''An AAAA record.'''
    A_AAAA = "A_AAAA"
    '''Both an A and AAAA record.'''
    SRV = "SRV"
    '''A Srv record.'''
    CNAME = "CNAME"
    '''A CNAME record.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.DnsServiceProps",
    jsii_struct_bases=[BaseServiceProps],
    name_mapping={
        "custom_health_check": "customHealthCheck",
        "description": "description",
        "health_check": "healthCheck",
        "name": "name",
        "dns_record_type": "dnsRecordType",
        "dns_ttl": "dnsTtl",
        "load_balancer": "loadBalancer",
        "routing_policy": "routingPolicy",
    },
)
class DnsServiceProps(BaseServiceProps):
    def __init__(
        self,
        *,
        custom_health_check: typing.Optional["HealthCheckCustomConfig"] = None,
        description: typing.Optional[builtins.str] = None,
        health_check: typing.Optional["HealthCheckConfig"] = None,
        name: typing.Optional[builtins.str] = None,
        dns_record_type: typing.Optional[DnsRecordType] = None,
        dns_ttl: typing.Optional[aws_cdk.core.Duration] = None,
        load_balancer: typing.Optional[builtins.bool] = None,
        routing_policy: typing.Optional["RoutingPolicy"] = None,
    ) -> None:
        '''Service props needed to create a service in a given namespace.

        Used by createService() for PrivateDnsNamespace and
        PublicDnsNamespace

        :param custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html Default: none
        :param description: A description of the service. Default: none
        :param health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
        :param name: A name for the Service. Default: CloudFormation-generated name
        :param dns_record_type: The DNS type of the record that you want AWS Cloud Map to create. Supported record types include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV. Default: A
        :param dns_ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record. Default: Duration.minutes(1)
        :param load_balancer: Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance. Setting this to ``true`` correctly configures the ``routingPolicy`` and performs some additional validation. Default: false
        :param routing_policy: The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service. Default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
        '''
        if isinstance(custom_health_check, dict):
            custom_health_check = HealthCheckCustomConfig(**custom_health_check)
        if isinstance(health_check, dict):
            health_check = HealthCheckConfig(**health_check)
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_health_check is not None:
            self._values["custom_health_check"] = custom_health_check
        if description is not None:
            self._values["description"] = description
        if health_check is not None:
            self._values["health_check"] = health_check
        if name is not None:
            self._values["name"] = name
        if dns_record_type is not None:
            self._values["dns_record_type"] = dns_record_type
        if dns_ttl is not None:
            self._values["dns_ttl"] = dns_ttl
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if routing_policy is not None:
            self._values["routing_policy"] = routing_policy

    @builtins.property
    def custom_health_check(self) -> typing.Optional["HealthCheckCustomConfig"]:
        '''Structure containing failure threshold for a custom health checker.

        Only one of healthCheckConfig or healthCheckCustomConfig can be specified.
        See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html

        :default: none
        '''
        result = self._values.get("custom_health_check")
        return typing.cast(typing.Optional["HealthCheckCustomConfig"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check(self) -> typing.Optional["HealthCheckConfig"]:
        '''Settings for an optional health check.

        If you specify health check settings, AWS Cloud Map associates the health
        check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can
        be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to
        this service.

        :default: none
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["HealthCheckConfig"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the Service.

        :default: CloudFormation-generated name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_record_type(self) -> typing.Optional[DnsRecordType]:
        '''The DNS type of the record that you want AWS Cloud Map to create.

        Supported record types
        include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV.

        :default: A
        '''
        result = self._values.get("dns_record_type")
        return typing.cast(typing.Optional[DnsRecordType], result)

    @builtins.property
    def dns_ttl(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.

        :default: Duration.minutes(1)
        '''
        result = self._values.get("dns_ttl")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def load_balancer(self) -> typing.Optional[builtins.bool]:
        '''Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance.

        Setting this to ``true`` correctly configures the ``routingPolicy``
        and performs some additional validation.

        :default: false
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def routing_policy(self) -> typing.Optional["RoutingPolicy"]:
        '''The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service.

        :default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
        '''
        result = self._values.get("routing_policy")
        return typing.cast(typing.Optional["RoutingPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.HealthCheckConfig",
    jsii_struct_bases=[],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "resource_path": "resourcePath",
        "type": "type",
    },
)
class HealthCheckConfig:
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        resource_path: typing.Optional[builtins.str] = None,
        type: typing.Optional["HealthCheckType"] = None,
    ) -> None:
        '''Settings for an optional Amazon Route 53 health check.

        If you specify settings for a health check, AWS Cloud Map
        associates the health check with all the records that you specify in DnsConfig. Only valid with a PublicDnsNamespace.

        :param failure_threshold: The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. Default: 1
        :param resource_path: The path that you want Route 53 to request when performing health checks. Do not use when health check type is TCP. Default: '/'
        :param type: The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy. Cannot be modified once created. Supported values are HTTP, HTTPS, and TCP. Default: HTTP
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if resource_path is not None:
            self._values["resource_path"] = resource_path
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.

        :default: 1
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_path(self) -> typing.Optional[builtins.str]:
        '''The path that you want Route 53 to request when performing health checks.

        Do not use when health check type is TCP.

        :default: '/'
        '''
        result = self._values.get("resource_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["HealthCheckType"]:
        '''The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.

        Cannot be modified once created. Supported values are HTTP, HTTPS, and TCP.

        :default: HTTP
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["HealthCheckType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthCheckConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.HealthCheckCustomConfig",
    jsii_struct_bases=[],
    name_mapping={"failure_threshold": "failureThreshold"},
)
class HealthCheckCustomConfig:
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Specifies information about an optional custom health check.

        :param failure_threshold: The number of 30-second intervals that you want Cloud Map to wait after receiving an UpdateInstanceCustomHealthStatus request before it changes the health status of a service instance. Default: 1
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of 30-second intervals that you want Cloud Map to wait after receiving an UpdateInstanceCustomHealthStatus request before it changes the health status of a service instance.

        :default: 1
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthCheckCustomConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-servicediscovery.HealthCheckType")
class HealthCheckType(enum.Enum):
    HTTP = "HTTP"
    '''Route 53 tries to establish a TCP connection.

    If successful, Route 53 submits an HTTP request and waits for an HTTP
    status code of 200 or greater and less than 400.
    '''
    HTTPS = "HTTPS"
    '''Route 53 tries to establish a TCP connection.

    If successful, Route 53 submits an HTTPS request and waits for an
    HTTP status code of 200 or greater and less than 400.  If you specify HTTPS for the value of Type, the endpoint
    must support TLS v1.0 or later.
    '''
    TCP = "TCP"
    '''Route 53 tries to establish a TCP connection.

    If you specify TCP for Type, don't specify a value for ResourcePath.
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.HttpNamespaceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_arn": "namespaceArn",
        "namespace_id": "namespaceId",
        "namespace_name": "namespaceName",
    },
)
class HttpNamespaceAttributes:
    def __init__(
        self,
        *,
        namespace_arn: builtins.str,
        namespace_id: builtins.str,
        namespace_name: builtins.str,
    ) -> None:
        '''
        :param namespace_arn: Namespace ARN for the Namespace.
        :param namespace_id: Namespace Id for the Namespace.
        :param namespace_name: A name for the Namespace.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "namespace_arn": namespace_arn,
            "namespace_id": namespace_id,
            "namespace_name": namespace_name,
        }

    @builtins.property
    def namespace_arn(self) -> builtins.str:
        '''Namespace ARN for the Namespace.'''
        result = self._values.get("namespace_arn")
        assert result is not None, "Required property 'namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_id(self) -> builtins.str:
        '''Namespace Id for the Namespace.'''
        result = self._values.get("namespace_id")
        assert result is not None, "Required property 'namespace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''A name for the Namespace.'''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpNamespaceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.HttpNamespaceProps",
    jsii_struct_bases=[BaseNamespaceProps],
    name_mapping={"name": "name", "description": "description"},
)
class HttpNamespaceProps(BaseNamespaceProps):
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: A name for the Namespace.
        :param description: A description of the Namespace. Default: none
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the Namespace.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the Namespace.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IInstance")
class IInstance(aws_cdk.core.IResource, typing_extensions.Protocol):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The id of the instance resource.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        '''The Cloudmap service this resource is registered to.'''
        ...


class _IInstanceProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-servicediscovery.IInstance"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The id of the instance resource.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        '''The Cloudmap service this resource is registered to.'''
        return typing.cast("IService", jsii.get(self, "service"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstance).__jsii_proxy_class__ = lambda : _IInstanceProxy


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.INamespace")
class INamespace(aws_cdk.core.IResource, typing_extensions.Protocol):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> builtins.str:
        '''Namespace ARN for the Namespace.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        '''Namespace Id for the Namespace.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        '''A name for the Namespace.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> "NamespaceType":
        '''Type of Namespace.'''
        ...


class _INamespaceProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-servicediscovery.INamespace"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> builtins.str:
        '''Namespace ARN for the Namespace.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "namespaceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        '''Namespace Id for the Namespace.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        '''A name for the Namespace.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> "NamespaceType":
        '''Type of Namespace.'''
        return typing.cast("NamespaceType", jsii.get(self, "type"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INamespace).__jsii_proxy_class__ = lambda : _INamespaceProxy


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IPrivateDnsNamespace")
class IPrivateDnsNamespace(INamespace, typing_extensions.Protocol):
    pass


class _IPrivateDnsNamespaceProxy(
    jsii.proxy_for(INamespace) # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-servicediscovery.IPrivateDnsNamespace"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrivateDnsNamespace).__jsii_proxy_class__ = lambda : _IPrivateDnsNamespaceProxy


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IPublicDnsNamespace")
class IPublicDnsNamespace(INamespace, typing_extensions.Protocol):
    pass


class _IPublicDnsNamespaceProxy(
    jsii.proxy_for(INamespace) # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-servicediscovery.IPublicDnsNamespace"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicDnsNamespace).__jsii_proxy_class__ = lambda : _IPublicDnsNamespaceProxy


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IService")
class IService(aws_cdk.core.IResource, typing_extensions.Protocol):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsRecordType")
    def dns_record_type(self) -> DnsRecordType:
        '''The DnsRecordType used by the service.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> INamespace:
        '''The namespace for the Cloudmap Service.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routingPolicy")
    def routing_policy(self) -> "RoutingPolicy":
        '''The Routing Policy used by the service.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> builtins.str:
        '''The Arn of the namespace that you want to use for DNS configuration.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        '''The ID of the namespace that you want to use for DNS configuration.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''A name for the Cloudmap Service.

        :attribute: true
        '''
        ...


class _IServiceProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-servicediscovery.IService"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsRecordType")
    def dns_record_type(self) -> DnsRecordType:
        '''The DnsRecordType used by the service.'''
        return typing.cast(DnsRecordType, jsii.get(self, "dnsRecordType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> INamespace:
        '''The namespace for the Cloudmap Service.'''
        return typing.cast(INamespace, jsii.get(self, "namespace"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routingPolicy")
    def routing_policy(self) -> "RoutingPolicy":
        '''The Routing Policy used by the service.'''
        return typing.cast("RoutingPolicy", jsii.get(self, "routingPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> builtins.str:
        '''The Arn of the namespace that you want to use for DNS configuration.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        '''The ID of the namespace that you want to use for DNS configuration.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''A name for the Cloudmap Service.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IService).__jsii_proxy_class__ = lambda : _IServiceProxy


@jsii.implements(IInstance)
class InstanceBase(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-servicediscovery.InstanceBase",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        props = aws_cdk.core.ResourceProps(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="uniqueInstanceId")
    def _unique_instance_id(self) -> builtins.str:
        '''Generate a unique instance Id that is safe to pass to CloudMap.'''
        return typing.cast(builtins.str, jsii.invoke(self, "uniqueInstanceId", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    @abc.abstractmethod
    def instance_id(self) -> builtins.str:
        '''The Id of the instance.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    @abc.abstractmethod
    def service(self) -> IService:
        '''The Cloudmap service to which the instance is registered.'''
        ...


class _InstanceBaseProxy(
    InstanceBase, jsii.proxy_for(aws_cdk.core.Resource) # type: ignore[misc]
):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Id of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    def service(self) -> IService:
        '''The Cloudmap service to which the instance is registered.'''
        return typing.cast(IService, jsii.get(self, "service"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, InstanceBase).__jsii_proxy_class__ = lambda : _InstanceBaseProxy


class IpInstance(
    InstanceBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.IpInstance",
):
    '''Instance that is accessible using an IP address.

    :resource: AWS::ServiceDiscovery::Instance
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service: IService,
        ipv4: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param service: The Cloudmap service this resource is registered to.
        :param ipv4: If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record. Default: none
        :param ipv6: If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record. Default: none
        :param port: The port on the endpoint that you want AWS Cloud Map to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a default port that is applied to all instances in the Service configuration. Default: 80
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        props = IpInstanceProps(
            service=service,
            ipv4=ipv4,
            ipv6=ipv6,
            port=port,
            custom_attributes=custom_attributes,
            instance_id=instance_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Id of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipv4")
    def ipv4(self) -> builtins.str:
        '''The Ipv4 address of the instance, or blank string if none available.'''
        return typing.cast(builtins.str, jsii.get(self, "ipv4"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> builtins.str:
        '''The Ipv6 address of the instance, or blank string if none available.'''
        return typing.cast(builtins.str, jsii.get(self, "ipv6"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        '''The exposed port of the instance.'''
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    def service(self) -> IService:
        '''The Cloudmap service to which the instance is registered.'''
        return typing.cast(IService, jsii.get(self, "service"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.IpInstanceBaseProps",
    jsii_struct_bases=[BaseInstanceProps],
    name_mapping={
        "custom_attributes": "customAttributes",
        "instance_id": "instanceId",
        "ipv4": "ipv4",
        "ipv6": "ipv6",
        "port": "port",
    },
)
class IpInstanceBaseProps(BaseInstanceProps):
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
        ipv4: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        :param ipv4: If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record. Default: none
        :param ipv6: If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record. Default: none
        :param port: The port on the endpoint that you want AWS Cloud Map to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a default port that is applied to all instances in the Service configuration. Default: 80
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if ipv4 is not None:
            self._values["ipv4"] = ipv4
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom attributes of the instance.

        :default: none
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The id of the instance resource.

        :default: Automatically generated name
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv4(self) -> typing.Optional[builtins.str]:
        '''If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record.

        :default: none
        '''
        result = self._values.get("ipv4")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6(self) -> typing.Optional[builtins.str]:
        '''If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record.

        :default: none
        '''
        result = self._values.get("ipv6")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port on the endpoint that you want AWS Cloud Map to perform health checks on.

        This value is also used for
        the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a
        default port that is applied to all instances in the Service configuration.

        :default: 80
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IpInstanceBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.IpInstanceProps",
    jsii_struct_bases=[IpInstanceBaseProps],
    name_mapping={
        "custom_attributes": "customAttributes",
        "instance_id": "instanceId",
        "ipv4": "ipv4",
        "ipv6": "ipv6",
        "port": "port",
        "service": "service",
    },
)
class IpInstanceProps(IpInstanceBaseProps):
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
        ipv4: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        service: IService,
    ) -> None:
        '''
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        :param ipv4: If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record. Default: none
        :param ipv6: If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record. Default: none
        :param port: The port on the endpoint that you want AWS Cloud Map to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a default port that is applied to all instances in the Service configuration. Default: 80
        :param service: The Cloudmap service this resource is registered to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
        }
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if instance_id is not None:
            self._values["instance_id"] = instance_id
        if ipv4 is not None:
            self._values["ipv4"] = ipv4
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom attributes of the instance.

        :default: none
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The id of the instance resource.

        :default: Automatically generated name
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv4(self) -> typing.Optional[builtins.str]:
        '''If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record.

        :default: none
        '''
        result = self._values.get("ipv4")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6(self) -> typing.Optional[builtins.str]:
        '''If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record.

        :default: none
        '''
        result = self._values.get("ipv6")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port on the endpoint that you want AWS Cloud Map to perform health checks on.

        This value is also used for
        the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a
        default port that is applied to all instances in the Service configuration.

        :default: 80
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service(self) -> IService:
        '''The Cloudmap service this resource is registered to.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(IService, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IpInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-servicediscovery.NamespaceType")
class NamespaceType(enum.Enum):
    HTTP = "HTTP"
    '''Choose this option if you want your application to use only API calls to discover registered instances.'''
    DNS_PRIVATE = "DNS_PRIVATE"
    '''Choose this option if you want your application to be able to discover instances using either API calls or using DNS queries in a VPC.'''
    DNS_PUBLIC = "DNS_PUBLIC"
    '''Choose this option if you want your application to be able to discover instances using either API calls or using public DNS queries.

    You aren't required to use both methods.
    '''


class NonIpInstance(
    InstanceBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.NonIpInstance",
):
    '''Instance accessible using values other than an IP address or a domain name (CNAME).

    Specify the other values in Custom attributes.

    :resource: AWS::ServiceDiscovery::Instance
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service: IService,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param service: The Cloudmap service this resource is registered to.
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        props = NonIpInstanceProps(
            service=service,
            custom_attributes=custom_attributes,
            instance_id=instance_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Id of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    def service(self) -> IService:
        '''The Cloudmap service to which the instance is registered.'''
        return typing.cast(IService, jsii.get(self, "service"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.NonIpInstanceBaseProps",
    jsii_struct_bases=[BaseInstanceProps],
    name_mapping={
        "custom_attributes": "customAttributes",
        "instance_id": "instanceId",
    },
)
class NonIpInstanceBaseProps(BaseInstanceProps):
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if instance_id is not None:
            self._values["instance_id"] = instance_id

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom attributes of the instance.

        :default: none
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The id of the instance resource.

        :default: Automatically generated name
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NonIpInstanceBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.NonIpInstanceProps",
    jsii_struct_bases=[NonIpInstanceBaseProps],
    name_mapping={
        "custom_attributes": "customAttributes",
        "instance_id": "instanceId",
        "service": "service",
    },
)
class NonIpInstanceProps(NonIpInstanceBaseProps):
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
        service: IService,
    ) -> None:
        '''
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        :param service: The Cloudmap service this resource is registered to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
        }
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if instance_id is not None:
            self._values["instance_id"] = instance_id

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom attributes of the instance.

        :default: none
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The id of the instance resource.

        :default: Automatically generated name
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(self) -> IService:
        '''The Cloudmap service this resource is registered to.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(IService, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NonIpInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPrivateDnsNamespace)
class PrivateDnsNamespace(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.PrivateDnsNamespace",
):
    '''Define a Service Discovery HTTP Namespace.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        vpc: aws_cdk.aws_ec2.IVpc,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpc: The Amazon VPC that you want to associate the namespace with.
        :param name: A name for the Namespace.
        :param description: A description of the Namespace. Default: none
        '''
        props = PrivateDnsNamespaceProps(vpc=vpc, name=name, description=description)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromPrivateDnsNamespaceAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_private_dns_namespace_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        namespace_arn: builtins.str,
        namespace_id: builtins.str,
        namespace_name: builtins.str,
    ) -> IPrivateDnsNamespace:
        '''
        :param scope: -
        :param id: -
        :param namespace_arn: Namespace ARN for the Namespace.
        :param namespace_id: Namespace Id for the Namespace.
        :param namespace_name: A name for the Namespace.
        '''
        attrs = PrivateDnsNamespaceAttributes(
            namespace_arn=namespace_arn,
            namespace_id=namespace_id,
            namespace_name=namespace_name,
        )

        return typing.cast(IPrivateDnsNamespace, jsii.sinvoke(cls, "fromPrivateDnsNamespaceAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="createService")
    def create_service(
        self,
        id: builtins.str,
        *,
        dns_record_type: typing.Optional[DnsRecordType] = None,
        dns_ttl: typing.Optional[aws_cdk.core.Duration] = None,
        load_balancer: typing.Optional[builtins.bool] = None,
        routing_policy: typing.Optional["RoutingPolicy"] = None,
        custom_health_check: typing.Optional[HealthCheckCustomConfig] = None,
        description: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[HealthCheckConfig] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "Service":
        '''Creates a service within the namespace.

        :param id: -
        :param dns_record_type: The DNS type of the record that you want AWS Cloud Map to create. Supported record types include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV. Default: A
        :param dns_ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record. Default: Duration.minutes(1)
        :param load_balancer: Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance. Setting this to ``true`` correctly configures the ``routingPolicy`` and performs some additional validation. Default: false
        :param routing_policy: The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service. Default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
        :param custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html Default: none
        :param description: A description of the service. Default: none
        :param health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
        :param name: A name for the Service. Default: CloudFormation-generated name
        '''
        props = DnsServiceProps(
            dns_record_type=dns_record_type,
            dns_ttl=dns_ttl,
            load_balancer=load_balancer,
            routing_policy=routing_policy,
            custom_health_check=custom_health_check,
            description=description,
            health_check=health_check,
            name=name,
        )

        return typing.cast("Service", jsii.invoke(self, "createService", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> builtins.str:
        '''Namespace Arn of the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        '''Namespace Id of the PrivateDnsNamespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        '''The name of the PrivateDnsNamespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="privateDnsNamespaceArn")
    def private_dns_namespace_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "privateDnsNamespaceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="privateDnsNamespaceId")
    def private_dns_namespace_id(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "privateDnsNamespaceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="privateDnsNamespaceName")
    def private_dns_namespace_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "privateDnsNamespaceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> NamespaceType:
        '''Type of the namespace.'''
        return typing.cast(NamespaceType, jsii.get(self, "type"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.PrivateDnsNamespaceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_arn": "namespaceArn",
        "namespace_id": "namespaceId",
        "namespace_name": "namespaceName",
    },
)
class PrivateDnsNamespaceAttributes:
    def __init__(
        self,
        *,
        namespace_arn: builtins.str,
        namespace_id: builtins.str,
        namespace_name: builtins.str,
    ) -> None:
        '''
        :param namespace_arn: Namespace ARN for the Namespace.
        :param namespace_id: Namespace Id for the Namespace.
        :param namespace_name: A name for the Namespace.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "namespace_arn": namespace_arn,
            "namespace_id": namespace_id,
            "namespace_name": namespace_name,
        }

    @builtins.property
    def namespace_arn(self) -> builtins.str:
        '''Namespace ARN for the Namespace.'''
        result = self._values.get("namespace_arn")
        assert result is not None, "Required property 'namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_id(self) -> builtins.str:
        '''Namespace Id for the Namespace.'''
        result = self._values.get("namespace_id")
        assert result is not None, "Required property 'namespace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''A name for the Namespace.'''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateDnsNamespaceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.PrivateDnsNamespaceProps",
    jsii_struct_bases=[BaseNamespaceProps],
    name_mapping={"name": "name", "description": "description", "vpc": "vpc"},
)
class PrivateDnsNamespaceProps(BaseNamespaceProps):
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        vpc: aws_cdk.aws_ec2.IVpc,
    ) -> None:
        '''
        :param name: A name for the Namespace.
        :param description: A description of the Namespace. Default: none
        :param vpc: The Amazon VPC that you want to associate the namespace with.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "vpc": vpc,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the Namespace.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the Namespace.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''The Amazon VPC that you want to associate the namespace with.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateDnsNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPublicDnsNamespace)
class PublicDnsNamespace(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.PublicDnsNamespace",
):
    '''Define a Public DNS Namespace.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param name: A name for the Namespace.
        :param description: A description of the Namespace. Default: none
        '''
        props = PublicDnsNamespaceProps(name=name, description=description)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromPublicDnsNamespaceAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_public_dns_namespace_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        namespace_arn: builtins.str,
        namespace_id: builtins.str,
        namespace_name: builtins.str,
    ) -> IPublicDnsNamespace:
        '''
        :param scope: -
        :param id: -
        :param namespace_arn: Namespace ARN for the Namespace.
        :param namespace_id: Namespace Id for the Namespace.
        :param namespace_name: A name for the Namespace.
        '''
        attrs = PublicDnsNamespaceAttributes(
            namespace_arn=namespace_arn,
            namespace_id=namespace_id,
            namespace_name=namespace_name,
        )

        return typing.cast(IPublicDnsNamespace, jsii.sinvoke(cls, "fromPublicDnsNamespaceAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="createService")
    def create_service(
        self,
        id: builtins.str,
        *,
        dns_record_type: typing.Optional[DnsRecordType] = None,
        dns_ttl: typing.Optional[aws_cdk.core.Duration] = None,
        load_balancer: typing.Optional[builtins.bool] = None,
        routing_policy: typing.Optional["RoutingPolicy"] = None,
        custom_health_check: typing.Optional[HealthCheckCustomConfig] = None,
        description: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[HealthCheckConfig] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "Service":
        '''Creates a service within the namespace.

        :param id: -
        :param dns_record_type: The DNS type of the record that you want AWS Cloud Map to create. Supported record types include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV. Default: A
        :param dns_ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record. Default: Duration.minutes(1)
        :param load_balancer: Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance. Setting this to ``true`` correctly configures the ``routingPolicy`` and performs some additional validation. Default: false
        :param routing_policy: The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service. Default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
        :param custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html Default: none
        :param description: A description of the service. Default: none
        :param health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
        :param name: A name for the Service. Default: CloudFormation-generated name
        '''
        props = DnsServiceProps(
            dns_record_type=dns_record_type,
            dns_ttl=dns_ttl,
            load_balancer=load_balancer,
            routing_policy=routing_policy,
            custom_health_check=custom_health_check,
            description=description,
            health_check=health_check,
            name=name,
        )

        return typing.cast("Service", jsii.invoke(self, "createService", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> builtins.str:
        '''Namespace Arn for the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        '''Namespace Id for the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        '''A name for the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publicDnsNamespaceArn")
    def public_dns_namespace_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "publicDnsNamespaceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publicDnsNamespaceId")
    def public_dns_namespace_id(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "publicDnsNamespaceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publicDnsNamespaceName")
    def public_dns_namespace_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "publicDnsNamespaceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> NamespaceType:
        '''Type of the namespace.'''
        return typing.cast(NamespaceType, jsii.get(self, "type"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.PublicDnsNamespaceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_arn": "namespaceArn",
        "namespace_id": "namespaceId",
        "namespace_name": "namespaceName",
    },
)
class PublicDnsNamespaceAttributes:
    def __init__(
        self,
        *,
        namespace_arn: builtins.str,
        namespace_id: builtins.str,
        namespace_name: builtins.str,
    ) -> None:
        '''
        :param namespace_arn: Namespace ARN for the Namespace.
        :param namespace_id: Namespace Id for the Namespace.
        :param namespace_name: A name for the Namespace.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "namespace_arn": namespace_arn,
            "namespace_id": namespace_id,
            "namespace_name": namespace_name,
        }

    @builtins.property
    def namespace_arn(self) -> builtins.str:
        '''Namespace ARN for the Namespace.'''
        result = self._values.get("namespace_arn")
        assert result is not None, "Required property 'namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_id(self) -> builtins.str:
        '''Namespace Id for the Namespace.'''
        result = self._values.get("namespace_id")
        assert result is not None, "Required property 'namespace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''A name for the Namespace.'''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicDnsNamespaceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.PublicDnsNamespaceProps",
    jsii_struct_bases=[BaseNamespaceProps],
    name_mapping={"name": "name", "description": "description"},
)
class PublicDnsNamespaceProps(BaseNamespaceProps):
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: A name for the Namespace.
        :param description: A description of the Namespace. Default: none
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the Namespace.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the Namespace.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicDnsNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-servicediscovery.RoutingPolicy")
class RoutingPolicy(enum.Enum):
    WEIGHTED = "WEIGHTED"
    '''Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service.'''
    MULTIVALUE = "MULTIVALUE"
    '''If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.'''


@jsii.implements(IService)
class Service(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.Service",
):
    '''Define a CloudMap Service.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        namespace: INamespace,
        dns_record_type: typing.Optional[DnsRecordType] = None,
        dns_ttl: typing.Optional[aws_cdk.core.Duration] = None,
        load_balancer: typing.Optional[builtins.bool] = None,
        routing_policy: typing.Optional[RoutingPolicy] = None,
        custom_health_check: typing.Optional[HealthCheckCustomConfig] = None,
        description: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[HealthCheckConfig] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param namespace: The namespace that you want to use for DNS configuration.
        :param dns_record_type: The DNS type of the record that you want AWS Cloud Map to create. Supported record types include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV. Default: A
        :param dns_ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record. Default: Duration.minutes(1)
        :param load_balancer: Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance. Setting this to ``true`` correctly configures the ``routingPolicy`` and performs some additional validation. Default: false
        :param routing_policy: The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service. Default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
        :param custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html Default: none
        :param description: A description of the service. Default: none
        :param health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
        :param name: A name for the Service. Default: CloudFormation-generated name
        '''
        props = ServiceProps(
            namespace=namespace,
            dns_record_type=dns_record_type,
            dns_ttl=dns_ttl,
            load_balancer=load_balancer,
            routing_policy=routing_policy,
            custom_health_check=custom_health_check,
            description=description,
            health_check=health_check,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromServiceAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_service_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dns_record_type: DnsRecordType,
        namespace: INamespace,
        routing_policy: RoutingPolicy,
        service_arn: builtins.str,
        service_id: builtins.str,
        service_name: builtins.str,
    ) -> IService:
        '''
        :param scope: -
        :param id: -
        :param dns_record_type: 
        :param namespace: 
        :param routing_policy: 
        :param service_arn: 
        :param service_id: 
        :param service_name: 
        '''
        attrs = ServiceAttributes(
            dns_record_type=dns_record_type,
            namespace=namespace,
            routing_policy=routing_policy,
            service_arn=service_arn,
            service_id=service_id,
            service_name=service_name,
        )

        return typing.cast(IService, jsii.sinvoke(cls, "fromServiceAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="registerCnameInstance")
    def register_cname_instance(
        self,
        id: builtins.str,
        *,
        instance_cname: builtins.str,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> IInstance:
        '''Registers a resource that is accessible using a CNAME.

        :param id: -
        :param instance_cname: If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        props = CnameInstanceBaseProps(
            instance_cname=instance_cname,
            custom_attributes=custom_attributes,
            instance_id=instance_id,
        )

        return typing.cast(IInstance, jsii.invoke(self, "registerCnameInstance", [id, props]))

    @jsii.member(jsii_name="registerIpInstance")
    def register_ip_instance(
        self,
        id: builtins.str,
        *,
        ipv4: typing.Optional[builtins.str] = None,
        ipv6: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> IInstance:
        '''Registers a resource that is accessible using an IP address.

        :param id: -
        :param ipv4: If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record. Default: none
        :param ipv6: If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record. Default: none
        :param port: The port on the endpoint that you want AWS Cloud Map to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a default port that is applied to all instances in the Service configuration. Default: 80
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        props = IpInstanceBaseProps(
            ipv4=ipv4,
            ipv6=ipv6,
            port=port,
            custom_attributes=custom_attributes,
            instance_id=instance_id,
        )

        return typing.cast(IInstance, jsii.invoke(self, "registerIpInstance", [id, props]))

    @jsii.member(jsii_name="registerLoadBalancer")
    def register_load_balancer(
        self,
        id: builtins.str,
        load_balancer: aws_cdk.aws_elasticloadbalancingv2.ILoadBalancerV2,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> IInstance:
        '''Registers an ELB as a new instance with unique name instanceId in this service.

        :param id: -
        :param load_balancer: -
        :param custom_attributes: -
        '''
        return typing.cast(IInstance, jsii.invoke(self, "registerLoadBalancer", [id, load_balancer, custom_attributes]))

    @jsii.member(jsii_name="registerNonIpInstance")
    def register_non_ip_instance(
        self,
        id: builtins.str,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> IInstance:
        '''Registers a resource that is accessible using values other than an IP address or a domain name (CNAME).

        :param id: -
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        props = NonIpInstanceBaseProps(
            custom_attributes=custom_attributes, instance_id=instance_id
        )

        return typing.cast(IInstance, jsii.invoke(self, "registerNonIpInstance", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsRecordType")
    def dns_record_type(self) -> DnsRecordType:
        '''The DnsRecordType used by the service.'''
        return typing.cast(DnsRecordType, jsii.get(self, "dnsRecordType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> INamespace:
        '''The namespace for the Cloudmap Service.'''
        return typing.cast(INamespace, jsii.get(self, "namespace"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="routingPolicy")
    def routing_policy(self) -> RoutingPolicy:
        '''The Routing Policy used by the service.'''
        return typing.cast(RoutingPolicy, jsii.get(self, "routingPolicy"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> builtins.str:
        '''The Arn of the namespace that you want to use for DNS configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        '''The ID of the namespace that you want to use for DNS configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        '''A name for the Cloudmap Service.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.ServiceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "dns_record_type": "dnsRecordType",
        "namespace": "namespace",
        "routing_policy": "routingPolicy",
        "service_arn": "serviceArn",
        "service_id": "serviceId",
        "service_name": "serviceName",
    },
)
class ServiceAttributes:
    def __init__(
        self,
        *,
        dns_record_type: DnsRecordType,
        namespace: INamespace,
        routing_policy: RoutingPolicy,
        service_arn: builtins.str,
        service_id: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param dns_record_type: 
        :param namespace: 
        :param routing_policy: 
        :param service_arn: 
        :param service_id: 
        :param service_name: 
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dns_record_type": dns_record_type,
            "namespace": namespace,
            "routing_policy": routing_policy,
            "service_arn": service_arn,
            "service_id": service_id,
            "service_name": service_name,
        }

    @builtins.property
    def dns_record_type(self) -> DnsRecordType:
        result = self._values.get("dns_record_type")
        assert result is not None, "Required property 'dns_record_type' is missing"
        return typing.cast(DnsRecordType, result)

    @builtins.property
    def namespace(self) -> INamespace:
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(INamespace, result)

    @builtins.property
    def routing_policy(self) -> RoutingPolicy:
        result = self._values.get("routing_policy")
        assert result is not None, "Required property 'routing_policy' is missing"
        return typing.cast(RoutingPolicy, result)

    @builtins.property
    def service_arn(self) -> builtins.str:
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_id(self) -> builtins.str:
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.ServiceProps",
    jsii_struct_bases=[DnsServiceProps],
    name_mapping={
        "custom_health_check": "customHealthCheck",
        "description": "description",
        "health_check": "healthCheck",
        "name": "name",
        "dns_record_type": "dnsRecordType",
        "dns_ttl": "dnsTtl",
        "load_balancer": "loadBalancer",
        "routing_policy": "routingPolicy",
        "namespace": "namespace",
    },
)
class ServiceProps(DnsServiceProps):
    def __init__(
        self,
        *,
        custom_health_check: typing.Optional[HealthCheckCustomConfig] = None,
        description: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[HealthCheckConfig] = None,
        name: typing.Optional[builtins.str] = None,
        dns_record_type: typing.Optional[DnsRecordType] = None,
        dns_ttl: typing.Optional[aws_cdk.core.Duration] = None,
        load_balancer: typing.Optional[builtins.bool] = None,
        routing_policy: typing.Optional[RoutingPolicy] = None,
        namespace: INamespace,
    ) -> None:
        '''
        :param custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html Default: none
        :param description: A description of the service. Default: none
        :param health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
        :param name: A name for the Service. Default: CloudFormation-generated name
        :param dns_record_type: The DNS type of the record that you want AWS Cloud Map to create. Supported record types include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV. Default: A
        :param dns_ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record. Default: Duration.minutes(1)
        :param load_balancer: Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance. Setting this to ``true`` correctly configures the ``routingPolicy`` and performs some additional validation. Default: false
        :param routing_policy: The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service. Default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
        :param namespace: The namespace that you want to use for DNS configuration.
        '''
        if isinstance(custom_health_check, dict):
            custom_health_check = HealthCheckCustomConfig(**custom_health_check)
        if isinstance(health_check, dict):
            health_check = HealthCheckConfig(**health_check)
        self._values: typing.Dict[str, typing.Any] = {
            "namespace": namespace,
        }
        if custom_health_check is not None:
            self._values["custom_health_check"] = custom_health_check
        if description is not None:
            self._values["description"] = description
        if health_check is not None:
            self._values["health_check"] = health_check
        if name is not None:
            self._values["name"] = name
        if dns_record_type is not None:
            self._values["dns_record_type"] = dns_record_type
        if dns_ttl is not None:
            self._values["dns_ttl"] = dns_ttl
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if routing_policy is not None:
            self._values["routing_policy"] = routing_policy

    @builtins.property
    def custom_health_check(self) -> typing.Optional[HealthCheckCustomConfig]:
        '''Structure containing failure threshold for a custom health checker.

        Only one of healthCheckConfig or healthCheckCustomConfig can be specified.
        See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html

        :default: none
        '''
        result = self._values.get("custom_health_check")
        return typing.cast(typing.Optional[HealthCheckCustomConfig], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service.

        :default: none
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def health_check(self) -> typing.Optional[HealthCheckConfig]:
        '''Settings for an optional health check.

        If you specify health check settings, AWS Cloud Map associates the health
        check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can
        be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to
        this service.

        :default: none
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[HealthCheckConfig], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the Service.

        :default: CloudFormation-generated name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_record_type(self) -> typing.Optional[DnsRecordType]:
        '''The DNS type of the record that you want AWS Cloud Map to create.

        Supported record types
        include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV.

        :default: A
        '''
        result = self._values.get("dns_record_type")
        return typing.cast(typing.Optional[DnsRecordType], result)

    @builtins.property
    def dns_ttl(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.

        :default: Duration.minutes(1)
        '''
        result = self._values.get("dns_ttl")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def load_balancer(self) -> typing.Optional[builtins.bool]:
        '''Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance.

        Setting this to ``true`` correctly configures the ``routingPolicy``
        and performs some additional validation.

        :default: false
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def routing_policy(self) -> typing.Optional[RoutingPolicy]:
        '''The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service.

        :default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
        '''
        result = self._values.get("routing_policy")
        return typing.cast(typing.Optional[RoutingPolicy], result)

    @builtins.property
    def namespace(self) -> INamespace:
        '''The namespace that you want to use for DNS configuration.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(INamespace, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AliasTargetInstance(
    InstanceBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.AliasTargetInstance",
):
    '''Instance that uses Route 53 Alias record type.

    Currently, the only resource types supported are Elastic Load
    Balancers.

    :resource: AWS::ServiceDiscovery::Instance
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dns_name: builtins.str,
        service: IService,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dns_name: DNS name of the target.
        :param service: The Cloudmap service this resource is registered to.
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        props = AliasTargetInstanceProps(
            dns_name=dns_name,
            service=service,
            custom_attributes=custom_attributes,
            instance_id=instance_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        '''The Route53 DNS name of the alias target.'''
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Id of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    def service(self) -> IService:
        '''The Cloudmap service to which the instance is registered.'''
        return typing.cast(IService, jsii.get(self, "service"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-servicediscovery.AliasTargetInstanceProps",
    jsii_struct_bases=[BaseInstanceProps],
    name_mapping={
        "custom_attributes": "customAttributes",
        "instance_id": "instanceId",
        "dns_name": "dnsName",
        "service": "service",
    },
)
class AliasTargetInstanceProps(BaseInstanceProps):
    def __init__(
        self,
        *,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
        dns_name: builtins.str,
        service: IService,
    ) -> None:
        '''
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        :param dns_name: DNS name of the target.
        :param service: The Cloudmap service this resource is registered to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "dns_name": dns_name,
            "service": service,
        }
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if instance_id is not None:
            self._values["instance_id"] = instance_id

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom attributes of the instance.

        :default: none
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def instance_id(self) -> typing.Optional[builtins.str]:
        '''The id of the instance resource.

        :default: Automatically generated name
        '''
        result = self._values.get("instance_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_name(self) -> builtins.str:
        '''DNS name of the target.'''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> IService:
        '''The Cloudmap service this resource is registered to.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(IService, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasTargetInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CnameInstance(
    InstanceBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.CnameInstance",
):
    '''Instance that is accessible using a domain name (CNAME).

    :resource: AWS::ServiceDiscovery::Instance
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service: IService,
        instance_cname: builtins.str,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        instance_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param service: The Cloudmap service this resource is registered to.
        :param instance_cname: If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.
        :param custom_attributes: Custom attributes of the instance. Default: none
        :param instance_id: The id of the instance resource. Default: Automatically generated name
        '''
        props = CnameInstanceProps(
            service=service,
            instance_cname=instance_cname,
            custom_attributes=custom_attributes,
            instance_id=instance_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cname")
    def cname(self) -> builtins.str:
        '''The domain name returned by DNS queries for the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "cname"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Id of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="service")
    def service(self) -> IService:
        '''The Cloudmap service to which the instance is registered.'''
        return typing.cast(IService, jsii.get(self, "service"))


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IHttpNamespace")
class IHttpNamespace(INamespace, typing_extensions.Protocol):
    pass


class _IHttpNamespaceProxy(
    jsii.proxy_for(INamespace) # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-servicediscovery.IHttpNamespace"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHttpNamespace).__jsii_proxy_class__ = lambda : _IHttpNamespaceProxy


@jsii.implements(IHttpNamespace)
class HttpNamespace(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-servicediscovery.HttpNamespace",
):
    '''Define an HTTP Namespace.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param name: A name for the Namespace.
        :param description: A description of the Namespace. Default: none
        '''
        props = HttpNamespaceProps(name=name, description=description)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromHttpNamespaceAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_http_namespace_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        namespace_arn: builtins.str,
        namespace_id: builtins.str,
        namespace_name: builtins.str,
    ) -> IHttpNamespace:
        '''
        :param scope: -
        :param id: -
        :param namespace_arn: Namespace ARN for the Namespace.
        :param namespace_id: Namespace Id for the Namespace.
        :param namespace_name: A name for the Namespace.
        '''
        attrs = HttpNamespaceAttributes(
            namespace_arn=namespace_arn,
            namespace_id=namespace_id,
            namespace_name=namespace_name,
        )

        return typing.cast(IHttpNamespace, jsii.sinvoke(cls, "fromHttpNamespaceAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="createService")
    def create_service(
        self,
        id: builtins.str,
        *,
        custom_health_check: typing.Optional[HealthCheckCustomConfig] = None,
        description: typing.Optional[builtins.str] = None,
        health_check: typing.Optional[HealthCheckConfig] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> Service:
        '''Creates a service within the namespace.

        :param id: -
        :param custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html Default: none
        :param description: A description of the service. Default: none
        :param health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
        :param name: A name for the Service. Default: CloudFormation-generated name
        '''
        props = BaseServiceProps(
            custom_health_check=custom_health_check,
            description=description,
            health_check=health_check,
            name=name,
        )

        return typing.cast(Service, jsii.invoke(self, "createService", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="httpNamespaceArn")
    def http_namespace_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "httpNamespaceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="httpNamespaceId")
    def http_namespace_id(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "httpNamespaceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="httpNamespaceName")
    def http_namespace_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "httpNamespaceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> builtins.str:
        '''Namespace Arn for the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        '''Namespace Id for the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        '''A name for the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> NamespaceType:
        '''Type of the namespace.'''
        return typing.cast(NamespaceType, jsii.get(self, "type"))


__all__ = [
    "AliasTargetInstance",
    "AliasTargetInstanceProps",
    "BaseInstanceProps",
    "BaseNamespaceProps",
    "BaseServiceProps",
    "CfnHttpNamespace",
    "CfnHttpNamespaceProps",
    "CfnInstance",
    "CfnInstanceProps",
    "CfnPrivateDnsNamespace",
    "CfnPrivateDnsNamespaceProps",
    "CfnPublicDnsNamespace",
    "CfnPublicDnsNamespaceProps",
    "CfnService",
    "CfnServiceProps",
    "CnameInstance",
    "CnameInstanceBaseProps",
    "CnameInstanceProps",
    "DnsRecordType",
    "DnsServiceProps",
    "HealthCheckConfig",
    "HealthCheckCustomConfig",
    "HealthCheckType",
    "HttpNamespace",
    "HttpNamespaceAttributes",
    "HttpNamespaceProps",
    "IHttpNamespace",
    "IInstance",
    "INamespace",
    "IPrivateDnsNamespace",
    "IPublicDnsNamespace",
    "IService",
    "InstanceBase",
    "IpInstance",
    "IpInstanceBaseProps",
    "IpInstanceProps",
    "NamespaceType",
    "NonIpInstance",
    "NonIpInstanceBaseProps",
    "NonIpInstanceProps",
    "PrivateDnsNamespace",
    "PrivateDnsNamespaceAttributes",
    "PrivateDnsNamespaceProps",
    "PublicDnsNamespace",
    "PublicDnsNamespaceAttributes",
    "PublicDnsNamespaceProps",
    "RoutingPolicy",
    "Service",
    "ServiceAttributes",
    "ServiceProps",
]

publication.publish()
