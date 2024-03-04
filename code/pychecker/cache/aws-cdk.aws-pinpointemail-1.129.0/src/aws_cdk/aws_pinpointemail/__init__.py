'''
# Amazon Pinpoint Email Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_pinpointemail as pinpointemail
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
class CfnConfigurationSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet",
):
    '''A CloudFormation ``AWS::PinpointEmail::ConfigurationSet``.

    :cloudformationResource: AWS::PinpointEmail::ConfigurationSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", aws_cdk.core.IResolvable]] = None,
        reputation_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.ReputationOptionsProperty"]] = None,
        sending_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.SendingOptionsProperty"]] = None,
        tags: typing.Optional[typing.Sequence["CfnConfigurationSet.TagsProperty"]] = None,
        tracking_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.TrackingOptionsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::ConfigurationSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::PinpointEmail::ConfigurationSet.Name``.
        :param delivery_options: ``AWS::PinpointEmail::ConfigurationSet.DeliveryOptions``.
        :param reputation_options: ``AWS::PinpointEmail::ConfigurationSet.ReputationOptions``.
        :param sending_options: ``AWS::PinpointEmail::ConfigurationSet.SendingOptions``.
        :param tags: ``AWS::PinpointEmail::ConfigurationSet.Tags``.
        :param tracking_options: ``AWS::PinpointEmail::ConfigurationSet.TrackingOptions``.
        '''
        props = CfnConfigurationSetProps(
            name=name,
            delivery_options=delivery_options,
            reputation_options=reputation_options,
            sending_options=sending_options,
            tags=tags,
            tracking_options=tracking_options,
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::PinpointEmail::ConfigurationSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryOptions")
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::PinpointEmail::ConfigurationSet.DeliveryOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-deliveryoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", aws_cdk.core.IResolvable]], jsii.get(self, "deliveryOptions"))

    @delivery_options.setter
    def delivery_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "deliveryOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="reputationOptions")
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.ReputationOptionsProperty"]]:
        '''``AWS::PinpointEmail::ConfigurationSet.ReputationOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-reputationoptions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.ReputationOptionsProperty"]], jsii.get(self, "reputationOptions"))

    @reputation_options.setter
    def reputation_options(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.ReputationOptionsProperty"]],
    ) -> None:
        jsii.set(self, "reputationOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sendingOptions")
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.SendingOptionsProperty"]]:
        '''``AWS::PinpointEmail::ConfigurationSet.SendingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-sendingoptions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.SendingOptionsProperty"]], jsii.get(self, "sendingOptions"))

    @sending_options.setter
    def sending_options(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.SendingOptionsProperty"]],
    ) -> None:
        jsii.set(self, "sendingOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]]:
        '''``AWS::PinpointEmail::ConfigurationSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trackingOptions")
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.TrackingOptionsProperty"]]:
        '''``AWS::PinpointEmail::ConfigurationSet.TrackingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-trackingoptions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.TrackingOptionsProperty"]], jsii.get(self, "trackingOptions"))

    @tracking_options.setter
    def tracking_options(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSet.TrackingOptionsProperty"]],
    ) -> None:
        jsii.set(self, "trackingOptions", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_pool_name": "sendingPoolName"},
    )
    class DeliveryOptionsProperty:
        def __init__(
            self,
            *,
            sending_pool_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param sending_pool_name: ``CfnConfigurationSet.DeliveryOptionsProperty.SendingPoolName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if sending_pool_name is not None:
                self._values["sending_pool_name"] = sending_pool_name

        @builtins.property
        def sending_pool_name(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSet.DeliveryOptionsProperty.SendingPoolName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html#cfn-pinpointemail-configurationset-deliveryoptions-sendingpoolname
            '''
            result = self._values.get("sending_pool_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeliveryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.ReputationOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"reputation_metrics_enabled": "reputationMetricsEnabled"},
    )
    class ReputationOptionsProperty:
        def __init__(
            self,
            *,
            reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param reputation_metrics_enabled: ``CfnConfigurationSet.ReputationOptionsProperty.ReputationMetricsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if reputation_metrics_enabled is not None:
                self._values["reputation_metrics_enabled"] = reputation_metrics_enabled

        @builtins.property
        def reputation_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnConfigurationSet.ReputationOptionsProperty.ReputationMetricsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html#cfn-pinpointemail-configurationset-reputationoptions-reputationmetricsenabled
            '''
            result = self._values.get("reputation_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReputationOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.SendingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_enabled": "sendingEnabled"},
    )
    class SendingOptionsProperty:
        def __init__(
            self,
            *,
            sending_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param sending_enabled: ``CfnConfigurationSet.SendingOptionsProperty.SendingEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if sending_enabled is not None:
                self._values["sending_enabled"] = sending_enabled

        @builtins.property
        def sending_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnConfigurationSet.SendingOptionsProperty.SendingEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html#cfn-pinpointemail-configurationset-sendingoptions-sendingenabled
            '''
            result = self._values.get("sending_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SendingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: ``CfnConfigurationSet.TagsProperty.Key``.
            :param value: ``CfnConfigurationSet.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSet.TagsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html#cfn-pinpointemail-configurationset-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSet.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html#cfn-pinpointemail-configurationset-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.TrackingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_redirect_domain": "customRedirectDomain"},
    )
    class TrackingOptionsProperty:
        def __init__(
            self,
            *,
            custom_redirect_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param custom_redirect_domain: ``CfnConfigurationSet.TrackingOptionsProperty.CustomRedirectDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_redirect_domain is not None:
                self._values["custom_redirect_domain"] = custom_redirect_domain

        @builtins.property
        def custom_redirect_domain(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSet.TrackingOptionsProperty.CustomRedirectDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html#cfn-pinpointemail-configurationset-trackingoptions-customredirectdomain
            '''
            result = self._values.get("custom_redirect_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrackingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnConfigurationSetEventDestination(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination",
):
    '''A CloudFormation ``AWS::PinpointEmail::ConfigurationSetEventDestination``.

    :cloudformationResource: AWS::PinpointEmail::ConfigurationSetEventDestination
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        configuration_set_name: builtins.str,
        event_destination_name: builtins.str,
        event_destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::ConfigurationSetEventDestination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param configuration_set_name: ``AWS::PinpointEmail::ConfigurationSetEventDestination.ConfigurationSetName``.
        :param event_destination_name: ``AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestinationName``.
        :param event_destination: ``AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestination``.
        '''
        props = CfnConfigurationSetEventDestinationProps(
            configuration_set_name=configuration_set_name,
            event_destination_name=event_destination_name,
            event_destination=event_destination,
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
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''``AWS::PinpointEmail::ConfigurationSetEventDestination.ConfigurationSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-configurationsetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

    @configuration_set_name.setter
    def configuration_set_name(self, value: builtins.str) -> None:
        jsii.set(self, "configurationSetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventDestinationName")
    def event_destination_name(self) -> builtins.str:
        '''``AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestinationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestinationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "eventDestinationName"))

    @event_destination_name.setter
    def event_destination_name(self, value: builtins.str) -> None:
        jsii.set(self, "eventDestinationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventDestination")
    def event_destination(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"]]:
        '''``AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"]], jsii.get(self, "eventDestination"))

    @event_destination.setter
    def event_destination(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"]],
    ) -> None:
        jsii.set(self, "eventDestination", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_configurations": "dimensionConfigurations"},
    )
    class CloudWatchDestinationProperty:
        def __init__(
            self,
            *,
            dimension_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]] = None,
        ) -> None:
            '''
            :param dimension_configurations: ``CfnConfigurationSetEventDestination.CloudWatchDestinationProperty.DimensionConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dimension_configurations is not None:
                self._values["dimension_configurations"] = dimension_configurations

        @builtins.property
        def dimension_configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]]:
            '''``CfnConfigurationSetEventDestination.CloudWatchDestinationProperty.DimensionConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html#cfn-pinpointemail-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations
            '''
            result = self._values.get("dimension_configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_dimension_value": "defaultDimensionValue",
            "dimension_name": "dimensionName",
            "dimension_value_source": "dimensionValueSource",
        },
    )
    class DimensionConfigurationProperty:
        def __init__(
            self,
            *,
            default_dimension_value: builtins.str,
            dimension_name: builtins.str,
            dimension_value_source: builtins.str,
        ) -> None:
            '''
            :param default_dimension_value: ``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DefaultDimensionValue``.
            :param dimension_name: ``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DimensionName``.
            :param dimension_value_source: ``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DimensionValueSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "default_dimension_value": default_dimension_value,
                "dimension_name": dimension_name,
                "dimension_value_source": dimension_value_source,
            }

        @builtins.property
        def default_dimension_value(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DefaultDimensionValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue
            '''
            result = self._values.get("default_dimension_value")
            assert result is not None, "Required property 'default_dimension_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_name(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DimensionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionname
            '''
            result = self._values.get("dimension_name")
            assert result is not None, "Required property 'dimension_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_value_source(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DimensionValueSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource
            '''
            result = self._values.get("dimension_value_source")
            assert result is not None, "Required property 'dimension_value_source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "matching_event_types": "matchingEventTypes",
            "cloud_watch_destination": "cloudWatchDestination",
            "enabled": "enabled",
            "kinesis_firehose_destination": "kinesisFirehoseDestination",
            "pinpoint_destination": "pinpointDestination",
            "sns_destination": "snsDestination",
        },
    )
    class EventDestinationProperty:
        def __init__(
            self,
            *,
            matching_event_types: typing.Sequence[builtins.str],
            cloud_watch_destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            kinesis_firehose_destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]] = None,
            pinpoint_destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.PinpointDestinationProperty"]] = None,
            sns_destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]] = None,
        ) -> None:
            '''
            :param matching_event_types: ``CfnConfigurationSetEventDestination.EventDestinationProperty.MatchingEventTypes``.
            :param cloud_watch_destination: ``CfnConfigurationSetEventDestination.EventDestinationProperty.CloudWatchDestination``.
            :param enabled: ``CfnConfigurationSetEventDestination.EventDestinationProperty.Enabled``.
            :param kinesis_firehose_destination: ``CfnConfigurationSetEventDestination.EventDestinationProperty.KinesisFirehoseDestination``.
            :param pinpoint_destination: ``CfnConfigurationSetEventDestination.EventDestinationProperty.PinpointDestination``.
            :param sns_destination: ``CfnConfigurationSetEventDestination.EventDestinationProperty.SnsDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "matching_event_types": matching_event_types,
            }
            if cloud_watch_destination is not None:
                self._values["cloud_watch_destination"] = cloud_watch_destination
            if enabled is not None:
                self._values["enabled"] = enabled
            if kinesis_firehose_destination is not None:
                self._values["kinesis_firehose_destination"] = kinesis_firehose_destination
            if pinpoint_destination is not None:
                self._values["pinpoint_destination"] = pinpoint_destination
            if sns_destination is not None:
                self._values["sns_destination"] = sns_destination

        @builtins.property
        def matching_event_types(self) -> typing.List[builtins.str]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.MatchingEventTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-matchingeventtypes
            '''
            result = self._values.get("matching_event_types")
            assert result is not None, "Required property 'matching_event_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def cloud_watch_destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.CloudWatchDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-cloudwatchdestination
            '''
            result = self._values.get("cloud_watch_destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def kinesis_firehose_destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.KinesisFirehoseDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-kinesisfirehosedestination
            '''
            result = self._values.get("kinesis_firehose_destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]], result)

        @builtins.property
        def pinpoint_destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.PinpointDestinationProperty"]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.PinpointDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-pinpointdestination
            '''
            result = self._values.get("pinpoint_destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.PinpointDestinationProperty"]], result)

        @builtins.property
        def sns_destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.SnsDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-snsdestination
            '''
            result = self._values.get("sns_destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_arn": "deliveryStreamArn",
            "iam_role_arn": "iamRoleArn",
        },
    )
    class KinesisFirehoseDestinationProperty:
        def __init__(
            self,
            *,
            delivery_stream_arn: builtins.str,
            iam_role_arn: builtins.str,
        ) -> None:
            '''
            :param delivery_stream_arn: ``CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.DeliveryStreamArn``.
            :param iam_role_arn: ``CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.IamRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "delivery_stream_arn": delivery_stream_arn,
                "iam_role_arn": iam_role_arn,
            }

        @builtins.property
        def delivery_stream_arn(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.DeliveryStreamArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html#cfn-pinpointemail-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn
            '''
            result = self._values.get("delivery_stream_arn")
            assert result is not None, "Required property 'delivery_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.IamRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html#cfn-pinpointemail-configurationseteventdestination-kinesisfirehosedestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"application_arn": "applicationArn"},
    )
    class PinpointDestinationProperty:
        def __init__(
            self,
            *,
            application_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param application_arn: ``CfnConfigurationSetEventDestination.PinpointDestinationProperty.ApplicationArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if application_arn is not None:
                self._values["application_arn"] = application_arn

        @builtins.property
        def application_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSetEventDestination.PinpointDestinationProperty.ApplicationArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html#cfn-pinpointemail-configurationseteventdestination-pinpointdestination-applicationarn
            '''
            result = self._values.get("application_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PinpointDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsDestinationProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''
            :param topic_arn: ``CfnConfigurationSetEventDestination.SnsDestinationProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.SnsDestinationProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html#cfn-pinpointemail-configurationseteventdestination-snsdestination-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "event_destination_name": "eventDestinationName",
        "event_destination": "eventDestination",
    },
)
class CfnConfigurationSetEventDestinationProps:
    def __init__(
        self,
        *,
        configuration_set_name: builtins.str,
        event_destination_name: builtins.str,
        event_destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::PinpointEmail::ConfigurationSetEventDestination``.

        :param configuration_set_name: ``AWS::PinpointEmail::ConfigurationSetEventDestination.ConfigurationSetName``.
        :param event_destination_name: ``AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestinationName``.
        :param event_destination: ``AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }
        if event_destination is not None:
            self._values["event_destination"] = event_destination

    @builtins.property
    def configuration_set_name(self) -> builtins.str:
        '''``AWS::PinpointEmail::ConfigurationSetEventDestination.ConfigurationSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-configurationsetname
        '''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination_name(self) -> builtins.str:
        '''``AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestinationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestinationname
        '''
        result = self._values.get("event_destination_name")
        assert result is not None, "Required property 'event_destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty]]:
        '''``AWS::PinpointEmail::ConfigurationSetEventDestination.EventDestination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination
        '''
        result = self._values.get("event_destination")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetEventDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "delivery_options": "deliveryOptions",
        "reputation_options": "reputationOptions",
        "sending_options": "sendingOptions",
        "tags": "tags",
        "tracking_options": "trackingOptions",
    },
)
class CfnConfigurationSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, aws_cdk.core.IResolvable]] = None,
        reputation_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.ReputationOptionsProperty]] = None,
        sending_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.SendingOptionsProperty]] = None,
        tags: typing.Optional[typing.Sequence[CfnConfigurationSet.TagsProperty]] = None,
        tracking_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.TrackingOptionsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::PinpointEmail::ConfigurationSet``.

        :param name: ``AWS::PinpointEmail::ConfigurationSet.Name``.
        :param delivery_options: ``AWS::PinpointEmail::ConfigurationSet.DeliveryOptions``.
        :param reputation_options: ``AWS::PinpointEmail::ConfigurationSet.ReputationOptions``.
        :param sending_options: ``AWS::PinpointEmail::ConfigurationSet.SendingOptions``.
        :param tags: ``AWS::PinpointEmail::ConfigurationSet.Tags``.
        :param tracking_options: ``AWS::PinpointEmail::ConfigurationSet.TrackingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if delivery_options is not None:
            self._values["delivery_options"] = delivery_options
        if reputation_options is not None:
            self._values["reputation_options"] = reputation_options
        if sending_options is not None:
            self._values["sending_options"] = sending_options
        if tags is not None:
            self._values["tags"] = tags
        if tracking_options is not None:
            self._values["tracking_options"] = tracking_options

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::PinpointEmail::ConfigurationSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::PinpointEmail::ConfigurationSet.DeliveryOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-deliveryoptions
        '''
        result = self._values.get("delivery_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.ReputationOptionsProperty]]:
        '''``AWS::PinpointEmail::ConfigurationSet.ReputationOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-reputationoptions
        '''
        result = self._values.get("reputation_options")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.ReputationOptionsProperty]], result)

    @builtins.property
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.SendingOptionsProperty]]:
        '''``AWS::PinpointEmail::ConfigurationSet.SendingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-sendingoptions
        '''
        result = self._values.get("sending_options")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.SendingOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]]:
        '''``AWS::PinpointEmail::ConfigurationSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]], result)

    @builtins.property
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.TrackingOptionsProperty]]:
        '''``AWS::PinpointEmail::ConfigurationSet.TrackingOptions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-trackingoptions
        '''
        result = self._values.get("tracking_options")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSet.TrackingOptionsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDedicatedIpPool(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpointemail.CfnDedicatedIpPool",
):
    '''A CloudFormation ``AWS::PinpointEmail::DedicatedIpPool``.

    :cloudformationResource: AWS::PinpointEmail::DedicatedIpPool
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        pool_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["CfnDedicatedIpPool.TagsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::DedicatedIpPool``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param pool_name: ``AWS::PinpointEmail::DedicatedIpPool.PoolName``.
        :param tags: ``AWS::PinpointEmail::DedicatedIpPool.Tags``.
        '''
        props = CfnDedicatedIpPoolProps(pool_name=pool_name, tags=tags)

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
    @jsii.member(jsii_name="poolName")
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::PinpointEmail::DedicatedIpPool.PoolName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-poolname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolName"))

    @pool_name.setter
    def pool_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "poolName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]]:
        '''``AWS::PinpointEmail::DedicatedIpPool.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnDedicatedIpPool.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: ``CfnDedicatedIpPool.TagsProperty.Key``.
            :param value: ``CfnDedicatedIpPool.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnDedicatedIpPool.TagsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html#cfn-pinpointemail-dedicatedippool-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnDedicatedIpPool.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html#cfn-pinpointemail-dedicatedippool-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpointemail.CfnDedicatedIpPoolProps",
    jsii_struct_bases=[],
    name_mapping={"pool_name": "poolName", "tags": "tags"},
)
class CfnDedicatedIpPoolProps:
    def __init__(
        self,
        *,
        pool_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[CfnDedicatedIpPool.TagsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::PinpointEmail::DedicatedIpPool``.

        :param pool_name: ``AWS::PinpointEmail::DedicatedIpPool.PoolName``.
        :param tags: ``AWS::PinpointEmail::DedicatedIpPool.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if pool_name is not None:
            self._values["pool_name"] = pool_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::PinpointEmail::DedicatedIpPool.PoolName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-poolname
        '''
        result = self._values.get("pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]]:
        '''``AWS::PinpointEmail::DedicatedIpPool.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDedicatedIpPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnIdentity(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpointemail.CfnIdentity",
):
    '''A CloudFormation ``AWS::PinpointEmail::Identity``.

    :cloudformationResource: AWS::PinpointEmail::Identity
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        mail_from_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIdentity.MailFromAttributesProperty"]] = None,
        tags: typing.Optional[typing.Sequence["CfnIdentity.TagsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::Identity``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::PinpointEmail::Identity.Name``.
        :param dkim_signing_enabled: ``AWS::PinpointEmail::Identity.DkimSigningEnabled``.
        :param feedback_forwarding_enabled: ``AWS::PinpointEmail::Identity.FeedbackForwardingEnabled``.
        :param mail_from_attributes: ``AWS::PinpointEmail::Identity.MailFromAttributes``.
        :param tags: ``AWS::PinpointEmail::Identity.Tags``.
        '''
        props = CfnIdentityProps(
            name=name,
            dkim_signing_enabled=dkim_signing_enabled,
            feedback_forwarding_enabled=feedback_forwarding_enabled,
            mail_from_attributes=mail_from_attributes,
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
    @jsii.member(jsii_name="attrIdentityDnsRecordName1")
    def attr_identity_dns_record_name1(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdentityDNSRecordName1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName1"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIdentityDnsRecordName2")
    def attr_identity_dns_record_name2(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdentityDNSRecordName2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName2"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIdentityDnsRecordName3")
    def attr_identity_dns_record_name3(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdentityDNSRecordName3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName3"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIdentityDnsRecordValue1")
    def attr_identity_dns_record_value1(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdentityDNSRecordValue1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue1"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIdentityDnsRecordValue2")
    def attr_identity_dns_record_value2(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdentityDNSRecordValue2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue2"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIdentityDnsRecordValue3")
    def attr_identity_dns_record_value3(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdentityDNSRecordValue3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue3"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::PinpointEmail::Identity.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dkimSigningEnabled")
    def dkim_signing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::PinpointEmail::Identity.DkimSigningEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-dkimsigningenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "dkimSigningEnabled"))

    @dkim_signing_enabled.setter
    def dkim_signing_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "dkimSigningEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="feedbackForwardingEnabled")
    def feedback_forwarding_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::PinpointEmail::Identity.FeedbackForwardingEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-feedbackforwardingenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "feedbackForwardingEnabled"))

    @feedback_forwarding_enabled.setter
    def feedback_forwarding_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "feedbackForwardingEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mailFromAttributes")
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIdentity.MailFromAttributesProperty"]]:
        '''``AWS::PinpointEmail::Identity.MailFromAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-mailfromattributes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIdentity.MailFromAttributesProperty"]], jsii.get(self, "mailFromAttributes"))

    @mail_from_attributes.setter
    def mail_from_attributes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnIdentity.MailFromAttributesProperty"]],
    ) -> None:
        jsii.set(self, "mailFromAttributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnIdentity.TagsProperty"]]:
        '''``AWS::PinpointEmail::Identity.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnIdentity.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnIdentity.TagsProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnIdentity.MailFromAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "behavior_on_mx_failure": "behaviorOnMxFailure",
            "mail_from_domain": "mailFromDomain",
        },
    )
    class MailFromAttributesProperty:
        def __init__(
            self,
            *,
            behavior_on_mx_failure: typing.Optional[builtins.str] = None,
            mail_from_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param behavior_on_mx_failure: ``CfnIdentity.MailFromAttributesProperty.BehaviorOnMxFailure``.
            :param mail_from_domain: ``CfnIdentity.MailFromAttributesProperty.MailFromDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if behavior_on_mx_failure is not None:
                self._values["behavior_on_mx_failure"] = behavior_on_mx_failure
            if mail_from_domain is not None:
                self._values["mail_from_domain"] = mail_from_domain

        @builtins.property
        def behavior_on_mx_failure(self) -> typing.Optional[builtins.str]:
            '''``CfnIdentity.MailFromAttributesProperty.BehaviorOnMxFailure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html#cfn-pinpointemail-identity-mailfromattributes-behavioronmxfailure
            '''
            result = self._values.get("behavior_on_mx_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mail_from_domain(self) -> typing.Optional[builtins.str]:
            '''``CfnIdentity.MailFromAttributesProperty.MailFromDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html#cfn-pinpointemail-identity-mailfromattributes-mailfromdomain
            '''
            result = self._values.get("mail_from_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MailFromAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnIdentity.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: ``CfnIdentity.TagsProperty.Key``.
            :param value: ``CfnIdentity.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnIdentity.TagsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html#cfn-pinpointemail-identity-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnIdentity.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html#cfn-pinpointemail-identity-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpointemail.CfnIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dkim_signing_enabled": "dkimSigningEnabled",
        "feedback_forwarding_enabled": "feedbackForwardingEnabled",
        "mail_from_attributes": "mailFromAttributes",
        "tags": "tags",
    },
)
class CfnIdentityProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        mail_from_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnIdentity.MailFromAttributesProperty]] = None,
        tags: typing.Optional[typing.Sequence[CfnIdentity.TagsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::PinpointEmail::Identity``.

        :param name: ``AWS::PinpointEmail::Identity.Name``.
        :param dkim_signing_enabled: ``AWS::PinpointEmail::Identity.DkimSigningEnabled``.
        :param feedback_forwarding_enabled: ``AWS::PinpointEmail::Identity.FeedbackForwardingEnabled``.
        :param mail_from_attributes: ``AWS::PinpointEmail::Identity.MailFromAttributes``.
        :param tags: ``AWS::PinpointEmail::Identity.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if dkim_signing_enabled is not None:
            self._values["dkim_signing_enabled"] = dkim_signing_enabled
        if feedback_forwarding_enabled is not None:
            self._values["feedback_forwarding_enabled"] = feedback_forwarding_enabled
        if mail_from_attributes is not None:
            self._values["mail_from_attributes"] = mail_from_attributes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::PinpointEmail::Identity.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dkim_signing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::PinpointEmail::Identity.DkimSigningEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-dkimsigningenabled
        '''
        result = self._values.get("dkim_signing_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def feedback_forwarding_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::PinpointEmail::Identity.FeedbackForwardingEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-feedbackforwardingenabled
        '''
        result = self._values.get("feedback_forwarding_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnIdentity.MailFromAttributesProperty]]:
        '''``AWS::PinpointEmail::Identity.MailFromAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-mailfromattributes
        '''
        result = self._values.get("mail_from_attributes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnIdentity.MailFromAttributesProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnIdentity.TagsProperty]]:
        '''``AWS::PinpointEmail::Identity.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnIdentity.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfigurationSet",
    "CfnConfigurationSetEventDestination",
    "CfnConfigurationSetEventDestinationProps",
    "CfnConfigurationSetProps",
    "CfnDedicatedIpPool",
    "CfnDedicatedIpPoolProps",
    "CfnIdentity",
    "CfnIdentityProps",
]

publication.publish()
