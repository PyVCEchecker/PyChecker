'''
# AWS::NetworkManager Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_networkmanager as networkmanager
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
class CfnCustomerGatewayAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkmanager.CfnCustomerGatewayAssociation",
):
    '''A CloudFormation ``AWS::NetworkManager::CustomerGatewayAssociation``.

    :cloudformationResource: AWS::NetworkManager::CustomerGatewayAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        customer_gateway_arn: builtins.str,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::CustomerGatewayAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param customer_gateway_arn: ``AWS::NetworkManager::CustomerGatewayAssociation.CustomerGatewayArn``.
        :param device_id: ``AWS::NetworkManager::CustomerGatewayAssociation.DeviceId``.
        :param global_network_id: ``AWS::NetworkManager::CustomerGatewayAssociation.GlobalNetworkId``.
        :param link_id: ``AWS::NetworkManager::CustomerGatewayAssociation.LinkId``.
        '''
        props = CfnCustomerGatewayAssociationProps(
            customer_gateway_arn=customer_gateway_arn,
            device_id=device_id,
            global_network_id=global_network_id,
            link_id=link_id,
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
    @jsii.member(jsii_name="customerGatewayArn")
    def customer_gateway_arn(self) -> builtins.str:
        '''``AWS::NetworkManager::CustomerGatewayAssociation.CustomerGatewayArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-customergatewayarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "customerGatewayArn"))

    @customer_gateway_arn.setter
    def customer_gateway_arn(self, value: builtins.str) -> None:
        jsii.set(self, "customerGatewayArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deviceId")
    def device_id(self) -> builtins.str:
        '''``AWS::NetworkManager::CustomerGatewayAssociation.DeviceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-deviceid
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceId"))

    @device_id.setter
    def device_id(self, value: builtins.str) -> None:
        jsii.set(self, "deviceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::CustomerGatewayAssociation.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="linkId")
    def link_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::CustomerGatewayAssociation.LinkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-linkid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkId"))

    @link_id.setter
    def link_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "linkId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkmanager.CfnCustomerGatewayAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "customer_gateway_arn": "customerGatewayArn",
        "device_id": "deviceId",
        "global_network_id": "globalNetworkId",
        "link_id": "linkId",
    },
)
class CfnCustomerGatewayAssociationProps:
    def __init__(
        self,
        *,
        customer_gateway_arn: builtins.str,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkManager::CustomerGatewayAssociation``.

        :param customer_gateway_arn: ``AWS::NetworkManager::CustomerGatewayAssociation.CustomerGatewayArn``.
        :param device_id: ``AWS::NetworkManager::CustomerGatewayAssociation.DeviceId``.
        :param global_network_id: ``AWS::NetworkManager::CustomerGatewayAssociation.GlobalNetworkId``.
        :param link_id: ``AWS::NetworkManager::CustomerGatewayAssociation.LinkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "customer_gateway_arn": customer_gateway_arn,
            "device_id": device_id,
            "global_network_id": global_network_id,
        }
        if link_id is not None:
            self._values["link_id"] = link_id

    @builtins.property
    def customer_gateway_arn(self) -> builtins.str:
        '''``AWS::NetworkManager::CustomerGatewayAssociation.CustomerGatewayArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-customergatewayarn
        '''
        result = self._values.get("customer_gateway_arn")
        assert result is not None, "Required property 'customer_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device_id(self) -> builtins.str:
        '''``AWS::NetworkManager::CustomerGatewayAssociation.DeviceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-deviceid
        '''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::CustomerGatewayAssociation.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::CustomerGatewayAssociation.LinkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-linkid
        '''
        result = self._values.get("link_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomerGatewayAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDevice(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkmanager.CfnDevice",
):
    '''A CloudFormation ``AWS::NetworkManager::Device``.

    :cloudformationResource: AWS::NetworkManager::Device
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.LocationProperty"]] = None,
        model: typing.Optional[builtins.str] = None,
        serial_number: typing.Optional[builtins.str] = None,
        site_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        type: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::Device``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param global_network_id: ``AWS::NetworkManager::Device.GlobalNetworkId``.
        :param description: ``AWS::NetworkManager::Device.Description``.
        :param location: ``AWS::NetworkManager::Device.Location``.
        :param model: ``AWS::NetworkManager::Device.Model``.
        :param serial_number: ``AWS::NetworkManager::Device.SerialNumber``.
        :param site_id: ``AWS::NetworkManager::Device.SiteId``.
        :param tags: ``AWS::NetworkManager::Device.Tags``.
        :param type: ``AWS::NetworkManager::Device.Type``.
        :param vendor: ``AWS::NetworkManager::Device.Vendor``.
        '''
        props = CfnDeviceProps(
            global_network_id=global_network_id,
            description=description,
            location=location,
            model=model,
            serial_number=serial_number,
            site_id=site_id,
            tags=tags,
            type=type,
            vendor=vendor,
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
    @jsii.member(jsii_name="attrDeviceArn")
    def attr_device_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: DeviceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeviceArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDeviceId")
    def attr_device_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DeviceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeviceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NetworkManager::Device.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::Device.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.LocationProperty"]]:
        '''``AWS::NetworkManager::Device.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-location
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.LocationProperty"]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.LocationProperty"]],
    ) -> None:
        jsii.set(self, "location", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="model")
    def model(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.Model``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-model
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "model"))

    @model.setter
    def model(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "model", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.SerialNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-serialnumber
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serialNumber"))

    @serial_number.setter
    def serial_number(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serialNumber", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="siteId")
    def site_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.SiteId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-siteid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "siteId"))

    @site_id.setter
    def site_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "siteId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.Vendor``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-vendor
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "vendor", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkmanager.CfnDevice.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "latitude": "latitude",
            "longitude": "longitude",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            latitude: typing.Optional[builtins.str] = None,
            longitude: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param address: ``CfnDevice.LocationProperty.Address``.
            :param latitude: ``CfnDevice.LocationProperty.Latitude``.
            :param longitude: ``CfnDevice.LocationProperty.Longitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if latitude is not None:
                self._values["latitude"] = latitude
            if longitude is not None:
                self._values["longitude"] = longitude

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''``CfnDevice.LocationProperty.Address``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def latitude(self) -> typing.Optional[builtins.str]:
            '''``CfnDevice.LocationProperty.Latitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-latitude
            '''
            result = self._values.get("latitude")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def longitude(self) -> typing.Optional[builtins.str]:
            '''``CfnDevice.LocationProperty.Longitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-longitude
            '''
            result = self._values.get("longitude")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkmanager.CfnDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "description": "description",
        "location": "location",
        "model": "model",
        "serial_number": "serialNumber",
        "site_id": "siteId",
        "tags": "tags",
        "type": "type",
        "vendor": "vendor",
    },
)
class CfnDeviceProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.LocationProperty]] = None,
        model: typing.Optional[builtins.str] = None,
        serial_number: typing.Optional[builtins.str] = None,
        site_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        type: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkManager::Device``.

        :param global_network_id: ``AWS::NetworkManager::Device.GlobalNetworkId``.
        :param description: ``AWS::NetworkManager::Device.Description``.
        :param location: ``AWS::NetworkManager::Device.Location``.
        :param model: ``AWS::NetworkManager::Device.Model``.
        :param serial_number: ``AWS::NetworkManager::Device.SerialNumber``.
        :param site_id: ``AWS::NetworkManager::Device.SiteId``.
        :param tags: ``AWS::NetworkManager::Device.Tags``.
        :param type: ``AWS::NetworkManager::Device.Type``.
        :param vendor: ``AWS::NetworkManager::Device.Vendor``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "global_network_id": global_network_id,
        }
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if model is not None:
            self._values["model"] = model
        if serial_number is not None:
            self._values["serial_number"] = serial_number
        if site_id is not None:
            self._values["site_id"] = site_id
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::Device.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.LocationProperty]]:
        '''``AWS::NetworkManager::Device.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.LocationProperty]], result)

    @builtins.property
    def model(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.Model``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-model
        '''
        result = self._values.get("model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serial_number(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.SerialNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-serialnumber
        '''
        result = self._values.get("serial_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def site_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.SiteId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-siteid
        '''
        result = self._values.get("site_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::NetworkManager::Device.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Device.Vendor``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-vendor
        '''
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnGlobalNetwork(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkmanager.CfnGlobalNetwork",
):
    '''A CloudFormation ``AWS::NetworkManager::GlobalNetwork``.

    :cloudformationResource: AWS::NetworkManager::GlobalNetwork
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::GlobalNetwork``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::NetworkManager::GlobalNetwork.Description``.
        :param tags: ``AWS::NetworkManager::GlobalNetwork.Tags``.
        '''
        props = CfnGlobalNetworkProps(description=description, tags=tags)

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
        '''``AWS::NetworkManager::GlobalNetwork.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::GlobalNetwork.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkmanager.CfnGlobalNetworkProps",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "tags": "tags"},
)
class CfnGlobalNetworkProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkManager::GlobalNetwork``.

        :param description: ``AWS::NetworkManager::GlobalNetwork.Description``.
        :param tags: ``AWS::NetworkManager::GlobalNetwork.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::GlobalNetwork.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::NetworkManager::GlobalNetwork.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGlobalNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLink(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkmanager.CfnLink",
):
    '''A CloudFormation ``AWS::NetworkManager::Link``.

    :cloudformationResource: AWS::NetworkManager::Link
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        bandwidth: typing.Union["CfnLink.BandwidthProperty", aws_cdk.core.IResolvable],
        global_network_id: builtins.str,
        site_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::Link``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bandwidth: ``AWS::NetworkManager::Link.Bandwidth``.
        :param global_network_id: ``AWS::NetworkManager::Link.GlobalNetworkId``.
        :param site_id: ``AWS::NetworkManager::Link.SiteId``.
        :param description: ``AWS::NetworkManager::Link.Description``.
        :param provider: ``AWS::NetworkManager::Link.Provider``.
        :param tags: ``AWS::NetworkManager::Link.Tags``.
        :param type: ``AWS::NetworkManager::Link.Type``.
        '''
        props = CfnLinkProps(
            bandwidth=bandwidth,
            global_network_id=global_network_id,
            site_id=site_id,
            description=description,
            provider=provider,
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
    @jsii.member(jsii_name="attrLinkArn")
    def attr_link_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: LinkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLinkId")
    def attr_link_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: LinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NetworkManager::Link.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bandwidth")
    def bandwidth(
        self,
    ) -> typing.Union["CfnLink.BandwidthProperty", aws_cdk.core.IResolvable]:
        '''``AWS::NetworkManager::Link.Bandwidth``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-bandwidth
        '''
        return typing.cast(typing.Union["CfnLink.BandwidthProperty", aws_cdk.core.IResolvable], jsii.get(self, "bandwidth"))

    @bandwidth.setter
    def bandwidth(
        self,
        value: typing.Union["CfnLink.BandwidthProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "bandwidth", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::Link.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="siteId")
    def site_id(self) -> builtins.str:
        '''``AWS::NetworkManager::Link.SiteId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-siteid
        '''
        return typing.cast(builtins.str, jsii.get(self, "siteId"))

    @site_id.setter
    def site_id(self, value: builtins.str) -> None:
        jsii.set(self, "siteId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Link.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Link.Provider``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-provider
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "provider", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Link.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkmanager.CfnLink.BandwidthProperty",
        jsii_struct_bases=[],
        name_mapping={
            "download_speed": "downloadSpeed",
            "upload_speed": "uploadSpeed",
        },
    )
    class BandwidthProperty:
        def __init__(
            self,
            *,
            download_speed: typing.Optional[jsii.Number] = None,
            upload_speed: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param download_speed: ``CfnLink.BandwidthProperty.DownloadSpeed``.
            :param upload_speed: ``CfnLink.BandwidthProperty.UploadSpeed``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if download_speed is not None:
                self._values["download_speed"] = download_speed
            if upload_speed is not None:
                self._values["upload_speed"] = upload_speed

        @builtins.property
        def download_speed(self) -> typing.Optional[jsii.Number]:
            '''``CfnLink.BandwidthProperty.DownloadSpeed``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-downloadspeed
            '''
            result = self._values.get("download_speed")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def upload_speed(self) -> typing.Optional[jsii.Number]:
            '''``CfnLink.BandwidthProperty.UploadSpeed``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-uploadspeed
            '''
            result = self._values.get("upload_speed")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BandwidthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLinkAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkmanager.CfnLinkAssociation",
):
    '''A CloudFormation ``AWS::NetworkManager::LinkAssociation``.

    :cloudformationResource: AWS::NetworkManager::LinkAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::LinkAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param device_id: ``AWS::NetworkManager::LinkAssociation.DeviceId``.
        :param global_network_id: ``AWS::NetworkManager::LinkAssociation.GlobalNetworkId``.
        :param link_id: ``AWS::NetworkManager::LinkAssociation.LinkId``.
        '''
        props = CfnLinkAssociationProps(
            device_id=device_id, global_network_id=global_network_id, link_id=link_id
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
    @jsii.member(jsii_name="deviceId")
    def device_id(self) -> builtins.str:
        '''``AWS::NetworkManager::LinkAssociation.DeviceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-deviceid
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceId"))

    @device_id.setter
    def device_id(self, value: builtins.str) -> None:
        jsii.set(self, "deviceId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::LinkAssociation.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="linkId")
    def link_id(self) -> builtins.str:
        '''``AWS::NetworkManager::LinkAssociation.LinkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-linkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "linkId"))

    @link_id.setter
    def link_id(self, value: builtins.str) -> None:
        jsii.set(self, "linkId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkmanager.CfnLinkAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "device_id": "deviceId",
        "global_network_id": "globalNetworkId",
        "link_id": "linkId",
    },
)
class CfnLinkAssociationProps:
    def __init__(
        self,
        *,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkManager::LinkAssociation``.

        :param device_id: ``AWS::NetworkManager::LinkAssociation.DeviceId``.
        :param global_network_id: ``AWS::NetworkManager::LinkAssociation.GlobalNetworkId``.
        :param link_id: ``AWS::NetworkManager::LinkAssociation.LinkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "device_id": device_id,
            "global_network_id": global_network_id,
            "link_id": link_id,
        }

    @builtins.property
    def device_id(self) -> builtins.str:
        '''``AWS::NetworkManager::LinkAssociation.DeviceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-deviceid
        '''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::LinkAssociation.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_id(self) -> builtins.str:
        '''``AWS::NetworkManager::LinkAssociation.LinkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-linkid
        '''
        result = self._values.get("link_id")
        assert result is not None, "Required property 'link_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinkAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkmanager.CfnLinkProps",
    jsii_struct_bases=[],
    name_mapping={
        "bandwidth": "bandwidth",
        "global_network_id": "globalNetworkId",
        "site_id": "siteId",
        "description": "description",
        "provider": "provider",
        "tags": "tags",
        "type": "type",
    },
)
class CfnLinkProps:
    def __init__(
        self,
        *,
        bandwidth: typing.Union[CfnLink.BandwidthProperty, aws_cdk.core.IResolvable],
        global_network_id: builtins.str,
        site_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkManager::Link``.

        :param bandwidth: ``AWS::NetworkManager::Link.Bandwidth``.
        :param global_network_id: ``AWS::NetworkManager::Link.GlobalNetworkId``.
        :param site_id: ``AWS::NetworkManager::Link.SiteId``.
        :param description: ``AWS::NetworkManager::Link.Description``.
        :param provider: ``AWS::NetworkManager::Link.Provider``.
        :param tags: ``AWS::NetworkManager::Link.Tags``.
        :param type: ``AWS::NetworkManager::Link.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bandwidth": bandwidth,
            "global_network_id": global_network_id,
            "site_id": site_id,
        }
        if description is not None:
            self._values["description"] = description
        if provider is not None:
            self._values["provider"] = provider
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def bandwidth(
        self,
    ) -> typing.Union[CfnLink.BandwidthProperty, aws_cdk.core.IResolvable]:
        '''``AWS::NetworkManager::Link.Bandwidth``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-bandwidth
        '''
        result = self._values.get("bandwidth")
        assert result is not None, "Required property 'bandwidth' is missing"
        return typing.cast(typing.Union[CfnLink.BandwidthProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::Link.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_id(self) -> builtins.str:
        '''``AWS::NetworkManager::Link.SiteId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-siteid
        '''
        result = self._values.get("site_id")
        assert result is not None, "Required property 'site_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Link.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Link.Provider``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-provider
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::NetworkManager::Link.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Link.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSite(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkmanager.CfnSite",
):
    '''A CloudFormation ``AWS::NetworkManager::Site``.

    :cloudformationResource: AWS::NetworkManager::Site
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSite.LocationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::Site``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param global_network_id: ``AWS::NetworkManager::Site.GlobalNetworkId``.
        :param description: ``AWS::NetworkManager::Site.Description``.
        :param location: ``AWS::NetworkManager::Site.Location``.
        :param tags: ``AWS::NetworkManager::Site.Tags``.
        '''
        props = CfnSiteProps(
            global_network_id=global_network_id,
            description=description,
            location=location,
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
    @jsii.member(jsii_name="attrSiteArn")
    def attr_site_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SiteArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSiteId")
    def attr_site_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SiteId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::NetworkManager::Site.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::Site.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Site.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSite.LocationProperty"]]:
        '''``AWS::NetworkManager::Site.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-location
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSite.LocationProperty"]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSite.LocationProperty"]],
    ) -> None:
        jsii.set(self, "location", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-networkmanager.CfnSite.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "latitude": "latitude",
            "longitude": "longitude",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            latitude: typing.Optional[builtins.str] = None,
            longitude: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param address: ``CfnSite.LocationProperty.Address``.
            :param latitude: ``CfnSite.LocationProperty.Latitude``.
            :param longitude: ``CfnSite.LocationProperty.Longitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if latitude is not None:
                self._values["latitude"] = latitude
            if longitude is not None:
                self._values["longitude"] = longitude

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''``CfnSite.LocationProperty.Address``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def latitude(self) -> typing.Optional[builtins.str]:
            '''``CfnSite.LocationProperty.Latitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-latitude
            '''
            result = self._values.get("latitude")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def longitude(self) -> typing.Optional[builtins.str]:
            '''``CfnSite.LocationProperty.Longitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-longitude
            '''
            result = self._values.get("longitude")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkmanager.CfnSiteProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "description": "description",
        "location": "location",
        "tags": "tags",
    },
)
class CfnSiteProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSite.LocationProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkManager::Site``.

        :param global_network_id: ``AWS::NetworkManager::Site.GlobalNetworkId``.
        :param description: ``AWS::NetworkManager::Site.Description``.
        :param location: ``AWS::NetworkManager::Site.Location``.
        :param tags: ``AWS::NetworkManager::Site.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "global_network_id": global_network_id,
        }
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::Site.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::NetworkManager::Site.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSite.LocationProperty]]:
        '''``AWS::NetworkManager::Site.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSite.LocationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::NetworkManager::Site.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSiteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTransitGatewayRegistration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-networkmanager.CfnTransitGatewayRegistration",
):
    '''A CloudFormation ``AWS::NetworkManager::TransitGatewayRegistration``.

    :cloudformationResource: AWS::NetworkManager::TransitGatewayRegistration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        global_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::NetworkManager::TransitGatewayRegistration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param global_network_id: ``AWS::NetworkManager::TransitGatewayRegistration.GlobalNetworkId``.
        :param transit_gateway_arn: ``AWS::NetworkManager::TransitGatewayRegistration.TransitGatewayArn``.
        '''
        props = CfnTransitGatewayRegistrationProps(
            global_network_id=global_network_id,
            transit_gateway_arn=transit_gateway_arn,
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
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::TransitGatewayRegistration.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-globalnetworkid
        '''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        jsii.set(self, "globalNetworkId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transitGatewayArn")
    def transit_gateway_arn(self) -> builtins.str:
        '''``AWS::NetworkManager::TransitGatewayRegistration.TransitGatewayArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-transitgatewayarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayArn"))

    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: builtins.str) -> None:
        jsii.set(self, "transitGatewayArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-networkmanager.CfnTransitGatewayRegistrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "transit_gateway_arn": "transitGatewayArn",
    },
)
class CfnTransitGatewayRegistrationProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::NetworkManager::TransitGatewayRegistration``.

        :param global_network_id: ``AWS::NetworkManager::TransitGatewayRegistration.GlobalNetworkId``.
        :param transit_gateway_arn: ``AWS::NetworkManager::TransitGatewayRegistration.TransitGatewayArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "global_network_id": global_network_id,
            "transit_gateway_arn": transit_gateway_arn,
        }

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''``AWS::NetworkManager::TransitGatewayRegistration.GlobalNetworkId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_arn(self) -> builtins.str:
        '''``AWS::NetworkManager::TransitGatewayRegistration.TransitGatewayArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-transitgatewayarn
        '''
        result = self._values.get("transit_gateway_arn")
        assert result is not None, "Required property 'transit_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransitGatewayRegistrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCustomerGatewayAssociation",
    "CfnCustomerGatewayAssociationProps",
    "CfnDevice",
    "CfnDeviceProps",
    "CfnGlobalNetwork",
    "CfnGlobalNetworkProps",
    "CfnLink",
    "CfnLinkAssociation",
    "CfnLinkAssociationProps",
    "CfnLinkProps",
    "CfnSite",
    "CfnSiteProps",
    "CfnTransitGatewayRegistration",
    "CfnTransitGatewayRegistrationProps",
]

publication.publish()
