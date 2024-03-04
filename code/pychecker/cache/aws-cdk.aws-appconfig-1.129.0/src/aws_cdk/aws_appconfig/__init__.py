'''
# AWS::AppConfig Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_appconfig as appconfig
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
class CfnApplication(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appconfig.CfnApplication",
):
    '''A CloudFormation ``AWS::AppConfig::Application``.

    :cloudformationResource: AWS::AppConfig::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["CfnApplication.TagsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::AppConfig::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::AppConfig::Application.Name``.
        :param description: ``AWS::AppConfig::Application.Description``.
        :param tags: ``AWS::AppConfig::Application.Tags``.
        '''
        props = CfnApplicationProps(name=name, description=description, tags=tags)

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
        '''``AWS::AppConfig::Application.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::Application.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnApplication.TagsProperty"]]:
        '''``AWS::AppConfig::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnApplication.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnApplication.TagsProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appconfig.CfnApplication.TagsProperty",
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
            :param key: ``CfnApplication.TagsProperty.Key``.
            :param value: ``CfnApplication.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.TagsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-application-tags.html#cfn-appconfig-application-tags-value
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
    jsii_type="@aws-cdk/aws-appconfig.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[CfnApplication.TagsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppConfig::Application``.

        :param name: ``AWS::AppConfig::Application.Name``.
        :param description: ``AWS::AppConfig::Application.Description``.
        :param tags: ``AWS::AppConfig::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html
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
        '''``AWS::AppConfig::Application.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::Application.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnApplication.TagsProperty]]:
        '''``AWS::AppConfig::Application.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html#cfn-appconfig-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnApplication.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnConfigurationProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appconfig.CfnConfigurationProfile",
):
    '''A CloudFormation ``AWS::AppConfig::ConfigurationProfile``.

    :cloudformationResource: AWS::AppConfig::ConfigurationProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        location_uri: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        retrieval_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["CfnConfigurationProfile.TagsProperty"]] = None,
        validators: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationProfile.ValidatorsProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AppConfig::ConfigurationProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::AppConfig::ConfigurationProfile.ApplicationId``.
        :param location_uri: ``AWS::AppConfig::ConfigurationProfile.LocationUri``.
        :param name: ``AWS::AppConfig::ConfigurationProfile.Name``.
        :param description: ``AWS::AppConfig::ConfigurationProfile.Description``.
        :param retrieval_role_arn: ``AWS::AppConfig::ConfigurationProfile.RetrievalRoleArn``.
        :param tags: ``AWS::AppConfig::ConfigurationProfile.Tags``.
        :param validators: ``AWS::AppConfig::ConfigurationProfile.Validators``.
        '''
        props = CfnConfigurationProfileProps(
            application_id=application_id,
            location_uri=location_uri,
            name=name,
            description=description,
            retrieval_role_arn=retrieval_role_arn,
            tags=tags,
            validators=validators,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::AppConfig::ConfigurationProfile.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="locationUri")
    def location_uri(self) -> builtins.str:
        '''``AWS::AppConfig::ConfigurationProfile.LocationUri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-locationuri
        '''
        return typing.cast(builtins.str, jsii.get(self, "locationUri"))

    @location_uri.setter
    def location_uri(self, value: builtins.str) -> None:
        jsii.set(self, "locationUri", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::AppConfig::ConfigurationProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::ConfigurationProfile.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="retrievalRoleArn")
    def retrieval_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::ConfigurationProfile.RetrievalRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-retrievalrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retrievalRoleArn"))

    @retrieval_role_arn.setter
    def retrieval_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "retrievalRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(
        self,
    ) -> typing.Optional[typing.List["CfnConfigurationProfile.TagsProperty"]]:
        '''``AWS::AppConfig::ConfigurationProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnConfigurationProfile.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnConfigurationProfile.TagsProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="validators")
    def validators(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationProfile.ValidatorsProperty"]]]]:
        '''``AWS::AppConfig::ConfigurationProfile.Validators``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-validators
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationProfile.ValidatorsProperty"]]]], jsii.get(self, "validators"))

    @validators.setter
    def validators(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationProfile.ValidatorsProperty"]]]],
    ) -> None:
        jsii.set(self, "validators", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appconfig.CfnConfigurationProfile.TagsProperty",
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
            :param key: ``CfnConfigurationProfile.TagsProperty.Key``.
            :param value: ``CfnConfigurationProfile.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationProfile.TagsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationProfile.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-tags.html#cfn-appconfig-configurationprofile-tags-value
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
        jsii_type="@aws-cdk/aws-appconfig.CfnConfigurationProfile.ValidatorsProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content", "type": "type"},
    )
    class ValidatorsProperty:
        def __init__(
            self,
            *,
            content: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param content: ``CfnConfigurationProfile.ValidatorsProperty.Content``.
            :param type: ``CfnConfigurationProfile.ValidatorsProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationProfile.ValidatorsProperty.Content``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationProfile.ValidatorsProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-configurationprofile-validators.html#cfn-appconfig-configurationprofile-validators-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidatorsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appconfig.CfnConfigurationProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "location_uri": "locationUri",
        "name": "name",
        "description": "description",
        "retrieval_role_arn": "retrievalRoleArn",
        "tags": "tags",
        "validators": "validators",
    },
)
class CfnConfigurationProfileProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        location_uri: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        retrieval_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[CfnConfigurationProfile.TagsProperty]] = None,
        validators: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationProfile.ValidatorsProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppConfig::ConfigurationProfile``.

        :param application_id: ``AWS::AppConfig::ConfigurationProfile.ApplicationId``.
        :param location_uri: ``AWS::AppConfig::ConfigurationProfile.LocationUri``.
        :param name: ``AWS::AppConfig::ConfigurationProfile.Name``.
        :param description: ``AWS::AppConfig::ConfigurationProfile.Description``.
        :param retrieval_role_arn: ``AWS::AppConfig::ConfigurationProfile.RetrievalRoleArn``.
        :param tags: ``AWS::AppConfig::ConfigurationProfile.Tags``.
        :param validators: ``AWS::AppConfig::ConfigurationProfile.Validators``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "location_uri": location_uri,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if retrieval_role_arn is not None:
            self._values["retrieval_role_arn"] = retrieval_role_arn
        if tags is not None:
            self._values["tags"] = tags
        if validators is not None:
            self._values["validators"] = validators

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::AppConfig::ConfigurationProfile.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_uri(self) -> builtins.str:
        '''``AWS::AppConfig::ConfigurationProfile.LocationUri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-locationuri
        '''
        result = self._values.get("location_uri")
        assert result is not None, "Required property 'location_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::AppConfig::ConfigurationProfile.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::ConfigurationProfile.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retrieval_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::ConfigurationProfile.RetrievalRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-retrievalrolearn
        '''
        result = self._values.get("retrieval_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.List[CfnConfigurationProfile.TagsProperty]]:
        '''``AWS::AppConfig::ConfigurationProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnConfigurationProfile.TagsProperty]], result)

    @builtins.property
    def validators(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationProfile.ValidatorsProperty]]]]:
        '''``AWS::AppConfig::ConfigurationProfile.Validators``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html#cfn-appconfig-configurationprofile-validators
        '''
        result = self._values.get("validators")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationProfile.ValidatorsProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDeployment(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appconfig.CfnDeployment",
):
    '''A CloudFormation ``AWS::AppConfig::Deployment``.

    :cloudformationResource: AWS::AppConfig::Deployment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        configuration_version: builtins.str,
        deployment_strategy_id: builtins.str,
        environment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["CfnDeployment.TagsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::AppConfig::Deployment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::AppConfig::Deployment.ApplicationId``.
        :param configuration_profile_id: ``AWS::AppConfig::Deployment.ConfigurationProfileId``.
        :param configuration_version: ``AWS::AppConfig::Deployment.ConfigurationVersion``.
        :param deployment_strategy_id: ``AWS::AppConfig::Deployment.DeploymentStrategyId``.
        :param environment_id: ``AWS::AppConfig::Deployment.EnvironmentId``.
        :param description: ``AWS::AppConfig::Deployment.Description``.
        :param tags: ``AWS::AppConfig::Deployment.Tags``.
        '''
        props = CfnDeploymentProps(
            application_id=application_id,
            configuration_profile_id=configuration_profile_id,
            configuration_version=configuration_version,
            deployment_strategy_id=deployment_strategy_id,
            environment_id=environment_id,
            description=description,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.ConfigurationProfileId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationprofileid
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @configuration_profile_id.setter
    def configuration_profile_id(self, value: builtins.str) -> None:
        jsii.set(self, "configurationProfileId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationVersion")
    def configuration_version(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.ConfigurationVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationversion
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationVersion"))

    @configuration_version.setter
    def configuration_version(self, value: builtins.str) -> None:
        jsii.set(self, "configurationVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deploymentStrategyId")
    def deployment_strategy_id(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.DeploymentStrategyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-deploymentstrategyid
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentStrategyId"))

    @deployment_strategy_id.setter
    def deployment_strategy_id(self, value: builtins.str) -> None:
        jsii.set(self, "deploymentStrategyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.EnvironmentId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-environmentid
        '''
        return typing.cast(builtins.str, jsii.get(self, "environmentId"))

    @environment_id.setter
    def environment_id(self, value: builtins.str) -> None:
        jsii.set(self, "environmentId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::Deployment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnDeployment.TagsProperty"]]:
        '''``AWS::AppConfig::Deployment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnDeployment.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnDeployment.TagsProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appconfig.CfnDeployment.TagsProperty",
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
            :param key: ``CfnDeployment.TagsProperty.Key``.
            :param value: ``CfnDeployment.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnDeployment.TagsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnDeployment.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deployment-tags.html#cfn-appconfig-deployment-tags-value
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
    jsii_type="@aws-cdk/aws-appconfig.CfnDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration_profile_id": "configurationProfileId",
        "configuration_version": "configurationVersion",
        "deployment_strategy_id": "deploymentStrategyId",
        "environment_id": "environmentId",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDeploymentProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        configuration_version: builtins.str,
        deployment_strategy_id: builtins.str,
        environment_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[CfnDeployment.TagsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppConfig::Deployment``.

        :param application_id: ``AWS::AppConfig::Deployment.ApplicationId``.
        :param configuration_profile_id: ``AWS::AppConfig::Deployment.ConfigurationProfileId``.
        :param configuration_version: ``AWS::AppConfig::Deployment.ConfigurationVersion``.
        :param deployment_strategy_id: ``AWS::AppConfig::Deployment.DeploymentStrategyId``.
        :param environment_id: ``AWS::AppConfig::Deployment.EnvironmentId``.
        :param description: ``AWS::AppConfig::Deployment.Description``.
        :param tags: ``AWS::AppConfig::Deployment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "configuration_version": configuration_version,
            "deployment_strategy_id": deployment_strategy_id,
            "environment_id": environment_id,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_profile_id(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.ConfigurationProfileId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationprofileid
        '''
        result = self._values.get("configuration_profile_id")
        assert result is not None, "Required property 'configuration_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_version(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.ConfigurationVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-configurationversion
        '''
        result = self._values.get("configuration_version")
        assert result is not None, "Required property 'configuration_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_strategy_id(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.DeploymentStrategyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-deploymentstrategyid
        '''
        result = self._values.get("deployment_strategy_id")
        assert result is not None, "Required property 'deployment_strategy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''``AWS::AppConfig::Deployment.EnvironmentId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-environmentid
        '''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::Deployment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDeployment.TagsProperty]]:
        '''``AWS::AppConfig::Deployment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html#cfn-appconfig-deployment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDeployment.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDeploymentStrategy(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appconfig.CfnDeploymentStrategy",
):
    '''A CloudFormation ``AWS::AppConfig::DeploymentStrategy``.

    :cloudformationResource: AWS::AppConfig::DeploymentStrategy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        deployment_duration_in_minutes: jsii.Number,
        growth_factor: jsii.Number,
        name: builtins.str,
        replicate_to: builtins.str,
        description: typing.Optional[builtins.str] = None,
        final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
        growth_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["CfnDeploymentStrategy.TagsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::AppConfig::DeploymentStrategy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param deployment_duration_in_minutes: ``AWS::AppConfig::DeploymentStrategy.DeploymentDurationInMinutes``.
        :param growth_factor: ``AWS::AppConfig::DeploymentStrategy.GrowthFactor``.
        :param name: ``AWS::AppConfig::DeploymentStrategy.Name``.
        :param replicate_to: ``AWS::AppConfig::DeploymentStrategy.ReplicateTo``.
        :param description: ``AWS::AppConfig::DeploymentStrategy.Description``.
        :param final_bake_time_in_minutes: ``AWS::AppConfig::DeploymentStrategy.FinalBakeTimeInMinutes``.
        :param growth_type: ``AWS::AppConfig::DeploymentStrategy.GrowthType``.
        :param tags: ``AWS::AppConfig::DeploymentStrategy.Tags``.
        '''
        props = CfnDeploymentStrategyProps(
            deployment_duration_in_minutes=deployment_duration_in_minutes,
            growth_factor=growth_factor,
            name=name,
            replicate_to=replicate_to,
            description=description,
            final_bake_time_in_minutes=final_bake_time_in_minutes,
            growth_type=growth_type,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deploymentDurationInMinutes")
    def deployment_duration_in_minutes(self) -> jsii.Number:
        '''``AWS::AppConfig::DeploymentStrategy.DeploymentDurationInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes
        '''
        return typing.cast(jsii.Number, jsii.get(self, "deploymentDurationInMinutes"))

    @deployment_duration_in_minutes.setter
    def deployment_duration_in_minutes(self, value: jsii.Number) -> None:
        jsii.set(self, "deploymentDurationInMinutes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="growthFactor")
    def growth_factor(self) -> jsii.Number:
        '''``AWS::AppConfig::DeploymentStrategy.GrowthFactor``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthfactor
        '''
        return typing.cast(jsii.Number, jsii.get(self, "growthFactor"))

    @growth_factor.setter
    def growth_factor(self, value: jsii.Number) -> None:
        jsii.set(self, "growthFactor", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::AppConfig::DeploymentStrategy.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicateTo")
    def replicate_to(self) -> builtins.str:
        '''``AWS::AppConfig::DeploymentStrategy.ReplicateTo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-replicateto
        '''
        return typing.cast(builtins.str, jsii.get(self, "replicateTo"))

    @replicate_to.setter
    def replicate_to(self, value: builtins.str) -> None:
        jsii.set(self, "replicateTo", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::DeploymentStrategy.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="finalBakeTimeInMinutes")
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::AppConfig::DeploymentStrategy.FinalBakeTimeInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "finalBakeTimeInMinutes"))

    @final_bake_time_in_minutes.setter
    def final_bake_time_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "finalBakeTimeInMinutes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="growthType")
    def growth_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::DeploymentStrategy.GrowthType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "growthType"))

    @growth_type.setter
    def growth_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "growthType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(
        self,
    ) -> typing.Optional[typing.List["CfnDeploymentStrategy.TagsProperty"]]:
        '''``AWS::AppConfig::DeploymentStrategy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnDeploymentStrategy.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnDeploymentStrategy.TagsProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appconfig.CfnDeploymentStrategy.TagsProperty",
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
            :param key: ``CfnDeploymentStrategy.TagsProperty.Key``.
            :param value: ``CfnDeploymentStrategy.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnDeploymentStrategy.TagsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnDeploymentStrategy.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-deploymentstrategy-tags.html#cfn-appconfig-deploymentstrategy-tags-value
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
    jsii_type="@aws-cdk/aws-appconfig.CfnDeploymentStrategyProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_duration_in_minutes": "deploymentDurationInMinutes",
        "growth_factor": "growthFactor",
        "name": "name",
        "replicate_to": "replicateTo",
        "description": "description",
        "final_bake_time_in_minutes": "finalBakeTimeInMinutes",
        "growth_type": "growthType",
        "tags": "tags",
    },
)
class CfnDeploymentStrategyProps:
    def __init__(
        self,
        *,
        deployment_duration_in_minutes: jsii.Number,
        growth_factor: jsii.Number,
        name: builtins.str,
        replicate_to: builtins.str,
        description: typing.Optional[builtins.str] = None,
        final_bake_time_in_minutes: typing.Optional[jsii.Number] = None,
        growth_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[CfnDeploymentStrategy.TagsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppConfig::DeploymentStrategy``.

        :param deployment_duration_in_minutes: ``AWS::AppConfig::DeploymentStrategy.DeploymentDurationInMinutes``.
        :param growth_factor: ``AWS::AppConfig::DeploymentStrategy.GrowthFactor``.
        :param name: ``AWS::AppConfig::DeploymentStrategy.Name``.
        :param replicate_to: ``AWS::AppConfig::DeploymentStrategy.ReplicateTo``.
        :param description: ``AWS::AppConfig::DeploymentStrategy.Description``.
        :param final_bake_time_in_minutes: ``AWS::AppConfig::DeploymentStrategy.FinalBakeTimeInMinutes``.
        :param growth_type: ``AWS::AppConfig::DeploymentStrategy.GrowthType``.
        :param tags: ``AWS::AppConfig::DeploymentStrategy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "deployment_duration_in_minutes": deployment_duration_in_minutes,
            "growth_factor": growth_factor,
            "name": name,
            "replicate_to": replicate_to,
        }
        if description is not None:
            self._values["description"] = description
        if final_bake_time_in_minutes is not None:
            self._values["final_bake_time_in_minutes"] = final_bake_time_in_minutes
        if growth_type is not None:
            self._values["growth_type"] = growth_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def deployment_duration_in_minutes(self) -> jsii.Number:
        '''``AWS::AppConfig::DeploymentStrategy.DeploymentDurationInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-deploymentdurationinminutes
        '''
        result = self._values.get("deployment_duration_in_minutes")
        assert result is not None, "Required property 'deployment_duration_in_minutes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def growth_factor(self) -> jsii.Number:
        '''``AWS::AppConfig::DeploymentStrategy.GrowthFactor``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthfactor
        '''
        result = self._values.get("growth_factor")
        assert result is not None, "Required property 'growth_factor' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::AppConfig::DeploymentStrategy.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replicate_to(self) -> builtins.str:
        '''``AWS::AppConfig::DeploymentStrategy.ReplicateTo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-replicateto
        '''
        result = self._values.get("replicate_to")
        assert result is not None, "Required property 'replicate_to' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::DeploymentStrategy.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_bake_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::AppConfig::DeploymentStrategy.FinalBakeTimeInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-finalbaketimeinminutes
        '''
        result = self._values.get("final_bake_time_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def growth_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::DeploymentStrategy.GrowthType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-growthtype
        '''
        result = self._values.get("growth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDeploymentStrategy.TagsProperty]]:
        '''``AWS::AppConfig::DeploymentStrategy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html#cfn-appconfig-deploymentstrategy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDeploymentStrategy.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentStrategyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEnvironment(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appconfig.CfnEnvironment",
):
    '''A CloudFormation ``AWS::AppConfig::Environment``.

    :cloudformationResource: AWS::AppConfig::Environment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnEnvironment.MonitorsProperty", aws_cdk.core.IResolvable]]]] = None,
        tags: typing.Optional[typing.Sequence["CfnEnvironment.TagsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::AppConfig::Environment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::AppConfig::Environment.ApplicationId``.
        :param name: ``AWS::AppConfig::Environment.Name``.
        :param description: ``AWS::AppConfig::Environment.Description``.
        :param monitors: ``AWS::AppConfig::Environment.Monitors``.
        :param tags: ``AWS::AppConfig::Environment.Tags``.
        '''
        props = CfnEnvironmentProps(
            application_id=application_id,
            name=name,
            description=description,
            monitors=monitors,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::AppConfig::Environment.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::AppConfig::Environment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::Environment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="monitors")
    def monitors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEnvironment.MonitorsProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::AppConfig::Environment.Monitors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-monitors
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEnvironment.MonitorsProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "monitors"))

    @monitors.setter
    def monitors(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEnvironment.MonitorsProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "monitors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnEnvironment.TagsProperty"]]:
        '''``AWS::AppConfig::Environment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnEnvironment.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnEnvironment.TagsProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appconfig.CfnEnvironment.MonitorsProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_arn": "alarmArn", "alarm_role_arn": "alarmRoleArn"},
    )
    class MonitorsProperty:
        def __init__(
            self,
            *,
            alarm_arn: typing.Optional[builtins.str] = None,
            alarm_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param alarm_arn: ``CfnEnvironment.MonitorsProperty.AlarmArn``.
            :param alarm_role_arn: ``CfnEnvironment.MonitorsProperty.AlarmRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if alarm_arn is not None:
                self._values["alarm_arn"] = alarm_arn
            if alarm_role_arn is not None:
                self._values["alarm_role_arn"] = alarm_role_arn

        @builtins.property
        def alarm_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.MonitorsProperty.AlarmArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmarn
            '''
            result = self._values.get("alarm_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def alarm_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.MonitorsProperty.AlarmRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-monitors.html#cfn-appconfig-environment-monitors-alarmrolearn
            '''
            result = self._values.get("alarm_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitorsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-appconfig.CfnEnvironment.TagsProperty",
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
            :param key: ``CfnEnvironment.TagsProperty.Key``.
            :param value: ``CfnEnvironment.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.TagsProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.TagsProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appconfig-environment-tags.html#cfn-appconfig-environment-tags-value
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
    jsii_type="@aws-cdk/aws-appconfig.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "name": "name",
        "description": "description",
        "monitors": "monitors",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        monitors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnEnvironment.MonitorsProperty, aws_cdk.core.IResolvable]]]] = None,
        tags: typing.Optional[typing.Sequence[CfnEnvironment.TagsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppConfig::Environment``.

        :param application_id: ``AWS::AppConfig::Environment.ApplicationId``.
        :param name: ``AWS::AppConfig::Environment.Name``.
        :param description: ``AWS::AppConfig::Environment.Description``.
        :param monitors: ``AWS::AppConfig::Environment.Monitors``.
        :param tags: ``AWS::AppConfig::Environment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if monitors is not None:
            self._values["monitors"] = monitors
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::AppConfig::Environment.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::AppConfig::Environment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::Environment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnEnvironment.MonitorsProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::AppConfig::Environment.Monitors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-monitors
        '''
        result = self._values.get("monitors")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnEnvironment.MonitorsProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnEnvironment.TagsProperty]]:
        '''``AWS::AppConfig::Environment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html#cfn-appconfig-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnEnvironment.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnHostedConfigurationVersion(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appconfig.CfnHostedConfigurationVersion",
):
    '''A CloudFormation ``AWS::AppConfig::HostedConfigurationVersion``.

    :cloudformationResource: AWS::AppConfig::HostedConfigurationVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        content: builtins.str,
        content_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::AppConfig::HostedConfigurationVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::AppConfig::HostedConfigurationVersion.ApplicationId``.
        :param configuration_profile_id: ``AWS::AppConfig::HostedConfigurationVersion.ConfigurationProfileId``.
        :param content: ``AWS::AppConfig::HostedConfigurationVersion.Content``.
        :param content_type: ``AWS::AppConfig::HostedConfigurationVersion.ContentType``.
        :param description: ``AWS::AppConfig::HostedConfigurationVersion.Description``.
        :param latest_version_number: ``AWS::AppConfig::HostedConfigurationVersion.LatestVersionNumber``.
        '''
        props = CfnHostedConfigurationVersionProps(
            application_id=application_id,
            configuration_profile_id=configuration_profile_id,
            content=content,
            content_type=content_type,
            description=description,
            latest_version_number=latest_version_number,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::AppConfig::HostedConfigurationVersion.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationProfileId")
    def configuration_profile_id(self) -> builtins.str:
        '''``AWS::AppConfig::HostedConfigurationVersion.ConfigurationProfileId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-configurationprofileid
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationProfileId"))

    @configuration_profile_id.setter
    def configuration_profile_id(self, value: builtins.str) -> None:
        jsii.set(self, "configurationProfileId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''``AWS::AppConfig::HostedConfigurationVersion.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-content
        '''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        '''``AWS::AppConfig::HostedConfigurationVersion.ContentType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-contenttype
        '''
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        jsii.set(self, "contentType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::HostedConfigurationVersion.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="latestVersionNumber")
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''``AWS::AppConfig::HostedConfigurationVersion.LatestVersionNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-latestversionnumber
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latestVersionNumber"))

    @latest_version_number.setter
    def latest_version_number(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "latestVersionNumber", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appconfig.CfnHostedConfigurationVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration_profile_id": "configurationProfileId",
        "content": "content",
        "content_type": "contentType",
        "description": "description",
        "latest_version_number": "latestVersionNumber",
    },
)
class CfnHostedConfigurationVersionProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        content: builtins.str,
        content_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        latest_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AppConfig::HostedConfigurationVersion``.

        :param application_id: ``AWS::AppConfig::HostedConfigurationVersion.ApplicationId``.
        :param configuration_profile_id: ``AWS::AppConfig::HostedConfigurationVersion.ConfigurationProfileId``.
        :param content: ``AWS::AppConfig::HostedConfigurationVersion.Content``.
        :param content_type: ``AWS::AppConfig::HostedConfigurationVersion.ContentType``.
        :param description: ``AWS::AppConfig::HostedConfigurationVersion.Description``.
        :param latest_version_number: ``AWS::AppConfig::HostedConfigurationVersion.LatestVersionNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "content": content,
            "content_type": content_type,
        }
        if description is not None:
            self._values["description"] = description
        if latest_version_number is not None:
            self._values["latest_version_number"] = latest_version_number

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::AppConfig::HostedConfigurationVersion.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_profile_id(self) -> builtins.str:
        '''``AWS::AppConfig::HostedConfigurationVersion.ConfigurationProfileId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-configurationprofileid
        '''
        result = self._values.get("configuration_profile_id")
        assert result is not None, "Required property 'configuration_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> builtins.str:
        '''``AWS::AppConfig::HostedConfigurationVersion.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''``AWS::AppConfig::HostedConfigurationVersion.ContentType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-contenttype
        '''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::AppConfig::HostedConfigurationVersion.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latest_version_number(self) -> typing.Optional[jsii.Number]:
        '''``AWS::AppConfig::HostedConfigurationVersion.LatestVersionNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html#cfn-appconfig-hostedconfigurationversion-latestversionnumber
        '''
        result = self._values.get("latest_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHostedConfigurationVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnConfigurationProfile",
    "CfnConfigurationProfileProps",
    "CfnDeployment",
    "CfnDeploymentProps",
    "CfnDeploymentStrategy",
    "CfnDeploymentStrategyProps",
    "CfnEnvironment",
    "CfnEnvironmentProps",
    "CfnHostedConfigurationVersion",
    "CfnHostedConfigurationVersionProps",
]

publication.publish()
