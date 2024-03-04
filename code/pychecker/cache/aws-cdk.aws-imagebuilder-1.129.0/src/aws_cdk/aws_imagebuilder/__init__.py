'''
# AWS::ImageBuilder Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_imagebuilder as imagebuilder
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
class CfnComponent(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnComponent",
):
    '''A CloudFormation ``AWS::ImageBuilder::Component``.

    :cloudformationResource: AWS::ImageBuilder::Component
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        platform: builtins.str,
        version: builtins.str,
        change_description: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::Component``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::ImageBuilder::Component.Name``.
        :param platform: ``AWS::ImageBuilder::Component.Platform``.
        :param version: ``AWS::ImageBuilder::Component.Version``.
        :param change_description: ``AWS::ImageBuilder::Component.ChangeDescription``.
        :param data: ``AWS::ImageBuilder::Component.Data``.
        :param description: ``AWS::ImageBuilder::Component.Description``.
        :param kms_key_id: ``AWS::ImageBuilder::Component.KmsKeyId``.
        :param supported_os_versions: ``AWS::ImageBuilder::Component.SupportedOsVersions``.
        :param tags: ``AWS::ImageBuilder::Component.Tags``.
        :param uri: ``AWS::ImageBuilder::Component.Uri``.
        '''
        props = CfnComponentProps(
            name=name,
            platform=platform,
            version=version,
            change_description=change_description,
            data=data,
            description=description,
            kms_key_id=kms_key_id,
            supported_os_versions=supported_os_versions,
            tags=tags,
            uri=uri,
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
    @jsii.member(jsii_name="attrEncrypted")
    def attr_encrypted(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: Encrypted
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrEncrypted"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ImageBuilder::Component.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::Component.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        '''``AWS::ImageBuilder::Component.Platform``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-platform
        '''
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        jsii.set(self, "platform", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''``AWS::ImageBuilder::Component.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-version
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        jsii.set(self, "version", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="changeDescription")
    def change_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.ChangeDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-changedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "changeDescription"))

    @change_description.setter
    def change_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "changeDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.Data``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-data
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "data", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="supportedOsVersions")
    def supported_os_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ImageBuilder::Component.SupportedOsVersions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-supportedosversions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "supportedOsVersions"))

    @supported_os_versions.setter
    def supported_os_versions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "supportedOsVersions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-uri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnComponentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "platform": "platform",
        "version": "version",
        "change_description": "changeDescription",
        "data": "data",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "supported_os_versions": "supportedOsVersions",
        "tags": "tags",
        "uri": "uri",
    },
)
class CfnComponentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        platform: builtins.str,
        version: builtins.str,
        change_description: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ImageBuilder::Component``.

        :param name: ``AWS::ImageBuilder::Component.Name``.
        :param platform: ``AWS::ImageBuilder::Component.Platform``.
        :param version: ``AWS::ImageBuilder::Component.Version``.
        :param change_description: ``AWS::ImageBuilder::Component.ChangeDescription``.
        :param data: ``AWS::ImageBuilder::Component.Data``.
        :param description: ``AWS::ImageBuilder::Component.Description``.
        :param kms_key_id: ``AWS::ImageBuilder::Component.KmsKeyId``.
        :param supported_os_versions: ``AWS::ImageBuilder::Component.SupportedOsVersions``.
        :param tags: ``AWS::ImageBuilder::Component.Tags``.
        :param uri: ``AWS::ImageBuilder::Component.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "platform": platform,
            "version": version,
        }
        if change_description is not None:
            self._values["change_description"] = change_description
        if data is not None:
            self._values["data"] = data
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if supported_os_versions is not None:
            self._values["supported_os_versions"] = supported_os_versions
        if tags is not None:
            self._values["tags"] = tags
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::Component.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platform(self) -> builtins.str:
        '''``AWS::ImageBuilder::Component.Platform``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-platform
        '''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''``AWS::ImageBuilder::Component.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def change_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.ChangeDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-changedescription
        '''
        result = self._values.get("change_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.Data``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-data
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def supported_os_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ImageBuilder::Component.SupportedOsVersions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-supportedosversions
        '''
        result = self._values.get("supported_os_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::ImageBuilder::Component.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Component.Uri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComponentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnContainerRecipe(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe",
):
    '''A CloudFormation ``AWS::ImageBuilder::ContainerRecipe``.

    :cloudformationResource: AWS::ImageBuilder::ContainerRecipe
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        components: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnContainerRecipe.ComponentConfigurationProperty", aws_cdk.core.IResolvable]]],
        container_type: builtins.str,
        name: builtins.str,
        parent_image: builtins.str,
        target_repository: typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.TargetContainerRepositoryProperty"],
        version: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dockerfile_template_data: typing.Optional[builtins.str] = None,
        dockerfile_template_uri: typing.Optional[builtins.str] = None,
        image_os_version_override: typing.Optional[builtins.str] = None,
        instance_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.InstanceConfigurationProperty"]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        platform_override: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::ContainerRecipe``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param components: ``AWS::ImageBuilder::ContainerRecipe.Components``.
        :param container_type: ``AWS::ImageBuilder::ContainerRecipe.ContainerType``.
        :param name: ``AWS::ImageBuilder::ContainerRecipe.Name``.
        :param parent_image: ``AWS::ImageBuilder::ContainerRecipe.ParentImage``.
        :param target_repository: ``AWS::ImageBuilder::ContainerRecipe.TargetRepository``.
        :param version: ``AWS::ImageBuilder::ContainerRecipe.Version``.
        :param description: ``AWS::ImageBuilder::ContainerRecipe.Description``.
        :param dockerfile_template_data: ``AWS::ImageBuilder::ContainerRecipe.DockerfileTemplateData``.
        :param dockerfile_template_uri: ``AWS::ImageBuilder::ContainerRecipe.DockerfileTemplateUri``.
        :param image_os_version_override: ``AWS::ImageBuilder::ContainerRecipe.ImageOsVersionOverride``.
        :param instance_configuration: ``AWS::ImageBuilder::ContainerRecipe.InstanceConfiguration``.
        :param kms_key_id: ``AWS::ImageBuilder::ContainerRecipe.KmsKeyId``.
        :param platform_override: ``AWS::ImageBuilder::ContainerRecipe.PlatformOverride``.
        :param tags: ``AWS::ImageBuilder::ContainerRecipe.Tags``.
        :param working_directory: ``AWS::ImageBuilder::ContainerRecipe.WorkingDirectory``.
        '''
        props = CfnContainerRecipeProps(
            components=components,
            container_type=container_type,
            name=name,
            parent_image=parent_image,
            target_repository=target_repository,
            version=version,
            description=description,
            dockerfile_template_data=dockerfile_template_data,
            dockerfile_template_uri=dockerfile_template_uri,
            image_os_version_override=image_os_version_override,
            instance_configuration=instance_configuration,
            kms_key_id=kms_key_id,
            platform_override=platform_override,
            tags=tags,
            working_directory=working_directory,
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
        '''``AWS::ImageBuilder::ContainerRecipe.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="components")
    def components(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnContainerRecipe.ComponentConfigurationProperty", aws_cdk.core.IResolvable]]]:
        '''``AWS::ImageBuilder::ContainerRecipe.Components``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-components
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnContainerRecipe.ComponentConfigurationProperty", aws_cdk.core.IResolvable]]], jsii.get(self, "components"))

    @components.setter
    def components(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnContainerRecipe.ComponentConfigurationProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "components", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containerType")
    def container_type(self) -> builtins.str:
        '''``AWS::ImageBuilder::ContainerRecipe.ContainerType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-containertype
        '''
        return typing.cast(builtins.str, jsii.get(self, "containerType"))

    @container_type.setter
    def container_type(self, value: builtins.str) -> None:
        jsii.set(self, "containerType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::ContainerRecipe.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parentImage")
    def parent_image(self) -> builtins.str:
        '''``AWS::ImageBuilder::ContainerRecipe.ParentImage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-parentimage
        '''
        return typing.cast(builtins.str, jsii.get(self, "parentImage"))

    @parent_image.setter
    def parent_image(self, value: builtins.str) -> None:
        jsii.set(self, "parentImage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetRepository")
    def target_repository(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.TargetContainerRepositoryProperty"]:
        '''``AWS::ImageBuilder::ContainerRecipe.TargetRepository``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-targetrepository
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.TargetContainerRepositoryProperty"], jsii.get(self, "targetRepository"))

    @target_repository.setter
    def target_repository(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.TargetContainerRepositoryProperty"],
    ) -> None:
        jsii.set(self, "targetRepository", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''``AWS::ImageBuilder::ContainerRecipe.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-version
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        jsii.set(self, "version", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dockerfileTemplateData")
    def dockerfile_template_data(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.DockerfileTemplateData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplatedata
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfileTemplateData"))

    @dockerfile_template_data.setter
    def dockerfile_template_data(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dockerfileTemplateData", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dockerfileTemplateUri")
    def dockerfile_template_uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.DockerfileTemplateUri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplateuri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfileTemplateUri"))

    @dockerfile_template_uri.setter
    def dockerfile_template_uri(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dockerfileTemplateUri", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageOsVersionOverride")
    def image_os_version_override(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.ImageOsVersionOverride``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-imageosversionoverride
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageOsVersionOverride"))

    @image_os_version_override.setter
    def image_os_version_override(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "imageOsVersionOverride", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.InstanceConfigurationProperty"]]:
        '''``AWS::ImageBuilder::ContainerRecipe.InstanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-instanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.InstanceConfigurationProperty"]], jsii.get(self, "instanceConfiguration"))

    @instance_configuration.setter
    def instance_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.InstanceConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "instanceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="platformOverride")
    def platform_override(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.PlatformOverride``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-platformoverride
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformOverride"))

    @platform_override.setter
    def platform_override(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "platformOverride", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.WorkingDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-workingdirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "workingDirectory", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"component_arn": "componentArn"},
    )
    class ComponentConfigurationProperty:
        def __init__(
            self,
            *,
            component_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param component_arn: ``CfnContainerRecipe.ComponentConfigurationProperty.ComponentArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if component_arn is not None:
                self._values["component_arn"] = component_arn

        @builtins.property
        def component_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.ComponentConfigurationProperty.ComponentArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html#cfn-imagebuilder-containerrecipe-componentconfiguration-componentarn
            '''
            result = self._values.get("component_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_on_termination": "deleteOnTermination",
            "encrypted": "encrypted",
            "iops": "iops",
            "kms_key_id": "kmsKeyId",
            "snapshot_id": "snapshotId",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsInstanceBlockDeviceSpecificationProperty:
        def __init__(
            self,
            *,
            delete_on_termination: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            encrypted: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            iops: typing.Optional[jsii.Number] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            snapshot_id: typing.Optional[builtins.str] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param delete_on_termination: ``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.DeleteOnTermination``.
            :param encrypted: ``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.Encrypted``.
            :param iops: ``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.Iops``.
            :param kms_key_id: ``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.KmsKeyId``.
            :param snapshot_id: ``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.SnapshotId``.
            :param volume_size: ``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.VolumeSize``.
            :param volume_type: ``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delete_on_termination is not None:
                self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if snapshot_id is not None:
                self._values["snapshot_id"] = snapshot_id
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def delete_on_termination(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.DeleteOnTermination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-deleteontermination
            '''
            result = self._values.get("delete_on_termination")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.Encrypted``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_id(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.SnapshotId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-snapshotid
            '''
            result = self._values.get("snapshot_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.VolumeSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsInstanceBlockDeviceSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class InstanceBlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty"]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param device_name: ``CfnContainerRecipe.InstanceBlockDeviceMappingProperty.DeviceName``.
            :param ebs: ``CfnContainerRecipe.InstanceBlockDeviceMappingProperty.Ebs``.
            :param no_device: ``CfnContainerRecipe.InstanceBlockDeviceMappingProperty.NoDevice``.
            :param virtual_name: ``CfnContainerRecipe.InstanceBlockDeviceMappingProperty.VirtualName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.InstanceBlockDeviceMappingProperty.DeviceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty"]]:
            '''``CfnContainerRecipe.InstanceBlockDeviceMappingProperty.Ebs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.InstanceBlockDeviceMappingProperty.NoDevice``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.InstanceBlockDeviceMappingProperty.VirtualName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceBlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_device_mappings": "blockDeviceMappings",
            "image": "image",
        },
    )
    class InstanceConfigurationProperty:
        def __init__(
            self,
            *,
            block_device_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.InstanceBlockDeviceMappingProperty"]]]] = None,
            image: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param block_device_mappings: ``CfnContainerRecipe.InstanceConfigurationProperty.BlockDeviceMappings``.
            :param image: ``CfnContainerRecipe.InstanceConfigurationProperty.Image``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if block_device_mappings is not None:
                self._values["block_device_mappings"] = block_device_mappings
            if image is not None:
                self._values["image"] = image

        @builtins.property
        def block_device_mappings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.InstanceBlockDeviceMappingProperty"]]]]:
            '''``CfnContainerRecipe.InstanceConfigurationProperty.BlockDeviceMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html#cfn-imagebuilder-containerrecipe-instanceconfiguration-blockdevicemappings
            '''
            result = self._values.get("block_device_mappings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContainerRecipe.InstanceBlockDeviceMappingProperty"]]]], result)

        @builtins.property
        def image(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.InstanceConfigurationProperty.Image``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html#cfn-imagebuilder-containerrecipe-instanceconfiguration-image
            '''
            result = self._values.get("image")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={"repository_name": "repositoryName", "service": "service"},
    )
    class TargetContainerRepositoryProperty:
        def __init__(
            self,
            *,
            repository_name: typing.Optional[builtins.str] = None,
            service: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param repository_name: ``CfnContainerRecipe.TargetContainerRepositoryProperty.RepositoryName``.
            :param service: ``CfnContainerRecipe.TargetContainerRepositoryProperty.Service``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if repository_name is not None:
                self._values["repository_name"] = repository_name
            if service is not None:
                self._values["service"] = service

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.TargetContainerRepositoryProperty.RepositoryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html#cfn-imagebuilder-containerrecipe-targetcontainerrepository-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service(self) -> typing.Optional[builtins.str]:
            '''``CfnContainerRecipe.TargetContainerRepositoryProperty.Service``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html#cfn-imagebuilder-containerrecipe-targetcontainerrepository-service
            '''
            result = self._values.get("service")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetContainerRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnContainerRecipeProps",
    jsii_struct_bases=[],
    name_mapping={
        "components": "components",
        "container_type": "containerType",
        "name": "name",
        "parent_image": "parentImage",
        "target_repository": "targetRepository",
        "version": "version",
        "description": "description",
        "dockerfile_template_data": "dockerfileTemplateData",
        "dockerfile_template_uri": "dockerfileTemplateUri",
        "image_os_version_override": "imageOsVersionOverride",
        "instance_configuration": "instanceConfiguration",
        "kms_key_id": "kmsKeyId",
        "platform_override": "platformOverride",
        "tags": "tags",
        "working_directory": "workingDirectory",
    },
)
class CfnContainerRecipeProps:
    def __init__(
        self,
        *,
        components: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, aws_cdk.core.IResolvable]]],
        container_type: builtins.str,
        name: builtins.str,
        parent_image: builtins.str,
        target_repository: typing.Union[aws_cdk.core.IResolvable, CfnContainerRecipe.TargetContainerRepositoryProperty],
        version: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dockerfile_template_data: typing.Optional[builtins.str] = None,
        dockerfile_template_uri: typing.Optional[builtins.str] = None,
        image_os_version_override: typing.Optional[builtins.str] = None,
        instance_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnContainerRecipe.InstanceConfigurationProperty]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        platform_override: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ImageBuilder::ContainerRecipe``.

        :param components: ``AWS::ImageBuilder::ContainerRecipe.Components``.
        :param container_type: ``AWS::ImageBuilder::ContainerRecipe.ContainerType``.
        :param name: ``AWS::ImageBuilder::ContainerRecipe.Name``.
        :param parent_image: ``AWS::ImageBuilder::ContainerRecipe.ParentImage``.
        :param target_repository: ``AWS::ImageBuilder::ContainerRecipe.TargetRepository``.
        :param version: ``AWS::ImageBuilder::ContainerRecipe.Version``.
        :param description: ``AWS::ImageBuilder::ContainerRecipe.Description``.
        :param dockerfile_template_data: ``AWS::ImageBuilder::ContainerRecipe.DockerfileTemplateData``.
        :param dockerfile_template_uri: ``AWS::ImageBuilder::ContainerRecipe.DockerfileTemplateUri``.
        :param image_os_version_override: ``AWS::ImageBuilder::ContainerRecipe.ImageOsVersionOverride``.
        :param instance_configuration: ``AWS::ImageBuilder::ContainerRecipe.InstanceConfiguration``.
        :param kms_key_id: ``AWS::ImageBuilder::ContainerRecipe.KmsKeyId``.
        :param platform_override: ``AWS::ImageBuilder::ContainerRecipe.PlatformOverride``.
        :param tags: ``AWS::ImageBuilder::ContainerRecipe.Tags``.
        :param working_directory: ``AWS::ImageBuilder::ContainerRecipe.WorkingDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "components": components,
            "container_type": container_type,
            "name": name,
            "parent_image": parent_image,
            "target_repository": target_repository,
            "version": version,
        }
        if description is not None:
            self._values["description"] = description
        if dockerfile_template_data is not None:
            self._values["dockerfile_template_data"] = dockerfile_template_data
        if dockerfile_template_uri is not None:
            self._values["dockerfile_template_uri"] = dockerfile_template_uri
        if image_os_version_override is not None:
            self._values["image_os_version_override"] = image_os_version_override
        if instance_configuration is not None:
            self._values["instance_configuration"] = instance_configuration
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if platform_override is not None:
            self._values["platform_override"] = platform_override
        if tags is not None:
            self._values["tags"] = tags
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def components(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, aws_cdk.core.IResolvable]]]:
        '''``AWS::ImageBuilder::ContainerRecipe.Components``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-components
        '''
        result = self._values.get("components")
        assert result is not None, "Required property 'components' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, aws_cdk.core.IResolvable]]], result)

    @builtins.property
    def container_type(self) -> builtins.str:
        '''``AWS::ImageBuilder::ContainerRecipe.ContainerType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-containertype
        '''
        result = self._values.get("container_type")
        assert result is not None, "Required property 'container_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::ContainerRecipe.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_image(self) -> builtins.str:
        '''``AWS::ImageBuilder::ContainerRecipe.ParentImage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-parentimage
        '''
        result = self._values.get("parent_image")
        assert result is not None, "Required property 'parent_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_repository(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnContainerRecipe.TargetContainerRepositoryProperty]:
        '''``AWS::ImageBuilder::ContainerRecipe.TargetRepository``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-targetrepository
        '''
        result = self._values.get("target_repository")
        assert result is not None, "Required property 'target_repository' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnContainerRecipe.TargetContainerRepositoryProperty], result)

    @builtins.property
    def version(self) -> builtins.str:
        '''``AWS::ImageBuilder::ContainerRecipe.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dockerfile_template_data(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.DockerfileTemplateData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplatedata
        '''
        result = self._values.get("dockerfile_template_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dockerfile_template_uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.DockerfileTemplateUri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplateuri
        '''
        result = self._values.get("dockerfile_template_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_os_version_override(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.ImageOsVersionOverride``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-imageosversionoverride
        '''
        result = self._values.get("image_os_version_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnContainerRecipe.InstanceConfigurationProperty]]:
        '''``AWS::ImageBuilder::ContainerRecipe.InstanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-instanceconfiguration
        '''
        result = self._values.get("instance_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnContainerRecipe.InstanceConfigurationProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform_override(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.PlatformOverride``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-platformoverride
        '''
        result = self._values.get("platform_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::ImageBuilder::ContainerRecipe.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ContainerRecipe.WorkingDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-workingdirectory
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContainerRecipeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDistributionConfiguration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration",
):
    '''A CloudFormation ``AWS::ImageBuilder::DistributionConfiguration``.

    :cloudformationResource: AWS::ImageBuilder::DistributionConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        distributions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDistributionConfiguration.DistributionProperty"]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::DistributionConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param distributions: ``AWS::ImageBuilder::DistributionConfiguration.Distributions``.
        :param name: ``AWS::ImageBuilder::DistributionConfiguration.Name``.
        :param description: ``AWS::ImageBuilder::DistributionConfiguration.Description``.
        :param tags: ``AWS::ImageBuilder::DistributionConfiguration.Tags``.
        '''
        props = CfnDistributionConfigurationProps(
            distributions=distributions, name=name, description=description, tags=tags
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
        '''``AWS::ImageBuilder::DistributionConfiguration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="distributions")
    def distributions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDistributionConfiguration.DistributionProperty"]]]:
        '''``AWS::ImageBuilder::DistributionConfiguration.Distributions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDistributionConfiguration.DistributionProperty"]]], jsii.get(self, "distributions"))

    @distributions.setter
    def distributions(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDistributionConfiguration.DistributionProperty"]]],
    ) -> None:
        jsii.set(self, "distributions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::DistributionConfiguration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::DistributionConfiguration.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.DistributionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "ami_distribution_configuration": "amiDistributionConfiguration",
            "container_distribution_configuration": "containerDistributionConfiguration",
            "launch_template_configurations": "launchTemplateConfigurations",
            "license_configuration_arns": "licenseConfigurationArns",
        },
    )
    class DistributionProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            ami_distribution_configuration: typing.Any = None,
            container_distribution_configuration: typing.Any = None,
            launch_template_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDistributionConfiguration.LaunchTemplateConfigurationProperty"]]]] = None,
            license_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param region: ``CfnDistributionConfiguration.DistributionProperty.Region``.
            :param ami_distribution_configuration: ``CfnDistributionConfiguration.DistributionProperty.AmiDistributionConfiguration``.
            :param container_distribution_configuration: ``CfnDistributionConfiguration.DistributionProperty.ContainerDistributionConfiguration``.
            :param launch_template_configurations: ``CfnDistributionConfiguration.DistributionProperty.LaunchTemplateConfigurations``.
            :param license_configuration_arns: ``CfnDistributionConfiguration.DistributionProperty.LicenseConfigurationArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "region": region,
            }
            if ami_distribution_configuration is not None:
                self._values["ami_distribution_configuration"] = ami_distribution_configuration
            if container_distribution_configuration is not None:
                self._values["container_distribution_configuration"] = container_distribution_configuration
            if launch_template_configurations is not None:
                self._values["launch_template_configurations"] = launch_template_configurations
            if license_configuration_arns is not None:
                self._values["license_configuration_arns"] = license_configuration_arns

        @builtins.property
        def region(self) -> builtins.str:
            '''``CfnDistributionConfiguration.DistributionProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ami_distribution_configuration(self) -> typing.Any:
            '''``CfnDistributionConfiguration.DistributionProperty.AmiDistributionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-amidistributionconfiguration
            '''
            result = self._values.get("ami_distribution_configuration")
            return typing.cast(typing.Any, result)

        @builtins.property
        def container_distribution_configuration(self) -> typing.Any:
            '''``CfnDistributionConfiguration.DistributionProperty.ContainerDistributionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-containerdistributionconfiguration
            '''
            result = self._values.get("container_distribution_configuration")
            return typing.cast(typing.Any, result)

        @builtins.property
        def launch_template_configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDistributionConfiguration.LaunchTemplateConfigurationProperty"]]]]:
            '''``CfnDistributionConfiguration.DistributionProperty.LaunchTemplateConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-launchtemplateconfigurations
            '''
            result = self._values.get("launch_template_configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDistributionConfiguration.LaunchTemplateConfigurationProperty"]]]], result)

        @builtins.property
        def license_configuration_arns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDistributionConfiguration.DistributionProperty.LicenseConfigurationArns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-licenseconfigurationarns
            '''
            result = self._values.get("license_configuration_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DistributionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "launch_template_id": "launchTemplateId",
            "set_default_version": "setDefaultVersion",
        },
    )
    class LaunchTemplateConfigurationProperty:
        def __init__(
            self,
            *,
            account_id: typing.Optional[builtins.str] = None,
            launch_template_id: typing.Optional[builtins.str] = None,
            set_default_version: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param account_id: ``CfnDistributionConfiguration.LaunchTemplateConfigurationProperty.AccountId``.
            :param launch_template_id: ``CfnDistributionConfiguration.LaunchTemplateConfigurationProperty.LaunchTemplateId``.
            :param set_default_version: ``CfnDistributionConfiguration.LaunchTemplateConfigurationProperty.SetDefaultVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if account_id is not None:
                self._values["account_id"] = account_id
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if set_default_version is not None:
                self._values["set_default_version"] = set_default_version

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDistributionConfiguration.LaunchTemplateConfigurationProperty.AccountId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDistributionConfiguration.LaunchTemplateConfigurationProperty.LaunchTemplateId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def set_default_version(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDistributionConfiguration.LaunchTemplateConfigurationProperty.SetDefaultVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-setdefaultversion
            '''
            result = self._values.get("set_default_version")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchTemplateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnDistributionConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "distributions": "distributions",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDistributionConfigurationProps:
    def __init__(
        self,
        *,
        distributions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDistributionConfiguration.DistributionProperty]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ImageBuilder::DistributionConfiguration``.

        :param distributions: ``AWS::ImageBuilder::DistributionConfiguration.Distributions``.
        :param name: ``AWS::ImageBuilder::DistributionConfiguration.Name``.
        :param description: ``AWS::ImageBuilder::DistributionConfiguration.Description``.
        :param tags: ``AWS::ImageBuilder::DistributionConfiguration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "distributions": distributions,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def distributions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDistributionConfiguration.DistributionProperty]]]:
        '''``AWS::ImageBuilder::DistributionConfiguration.Distributions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions
        '''
        result = self._values.get("distributions")
        assert result is not None, "Required property 'distributions' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDistributionConfiguration.DistributionProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::DistributionConfiguration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::DistributionConfiguration.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::ImageBuilder::DistributionConfiguration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDistributionConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnImage(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImage",
):
    '''A CloudFormation ``AWS::ImageBuilder::Image``.

    :cloudformationResource: AWS::ImageBuilder::Image
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        infrastructure_configuration_arn: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_tests_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImage.ImageTestsConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::Image``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param infrastructure_configuration_arn: ``AWS::ImageBuilder::Image.InfrastructureConfigurationArn``.
        :param container_recipe_arn: ``AWS::ImageBuilder::Image.ContainerRecipeArn``.
        :param distribution_configuration_arn: ``AWS::ImageBuilder::Image.DistributionConfigurationArn``.
        :param enhanced_image_metadata_enabled: ``AWS::ImageBuilder::Image.EnhancedImageMetadataEnabled``.
        :param image_recipe_arn: ``AWS::ImageBuilder::Image.ImageRecipeArn``.
        :param image_tests_configuration: ``AWS::ImageBuilder::Image.ImageTestsConfiguration``.
        :param tags: ``AWS::ImageBuilder::Image.Tags``.
        '''
        props = CfnImageProps(
            infrastructure_configuration_arn=infrastructure_configuration_arn,
            container_recipe_arn=container_recipe_arn,
            distribution_configuration_arn=distribution_configuration_arn,
            enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
            image_recipe_arn=image_recipe_arn,
            image_tests_configuration=image_tests_configuration,
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
    @jsii.member(jsii_name="attrImageId")
    def attr_image_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ImageId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageId"))

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
        '''``AWS::ImageBuilder::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''``AWS::ImageBuilder::Image.InfrastructureConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-infrastructureconfigurationarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "infrastructureConfigurationArn"))

    @infrastructure_configuration_arn.setter
    def infrastructure_configuration_arn(self, value: builtins.str) -> None:
        jsii.set(self, "infrastructureConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containerRecipeArn")
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Image.ContainerRecipeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-containerrecipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRecipeArn"))

    @container_recipe_arn.setter
    def container_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "containerRecipeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="distributionConfigurationArn")
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Image.DistributionConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-distributionconfigurationarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionConfigurationArn"))

    @distribution_configuration_arn.setter
    def distribution_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "distributionConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ImageBuilder::Image.EnhancedImageMetadataEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-enhancedimagemetadataenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enhancedImageMetadataEnabled"))

    @enhanced_image_metadata_enabled.setter
    def enhanced_image_metadata_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enhancedImageMetadataEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageRecipeArn")
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Image.ImageRecipeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagerecipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageRecipeArn"))

    @image_recipe_arn.setter
    def image_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "imageRecipeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImage.ImageTestsConfigurationProperty"]]:
        '''``AWS::ImageBuilder::Image.ImageTestsConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagetestsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImage.ImageTestsConfigurationProperty"]], jsii.get(self, "imageTestsConfiguration"))

    @image_tests_configuration.setter
    def image_tests_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImage.ImageTestsConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "imageTestsConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImage.ImageTestsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_tests_enabled": "imageTestsEnabled",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class ImageTestsConfigurationProperty:
        def __init__(
            self,
            *,
            image_tests_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param image_tests_enabled: ``CfnImage.ImageTestsConfigurationProperty.ImageTestsEnabled``.
            :param timeout_minutes: ``CfnImage.ImageTestsConfigurationProperty.TimeoutMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if image_tests_enabled is not None:
                self._values["image_tests_enabled"] = image_tests_enabled
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def image_tests_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnImage.ImageTestsConfigurationProperty.ImageTestsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html#cfn-imagebuilder-image-imagetestsconfiguration-imagetestsenabled
            '''
            result = self._values.get("image_tests_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''``CfnImage.ImageTestsConfigurationProperty.TimeoutMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html#cfn-imagebuilder-image-imagetestsconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageTestsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnImagePipeline(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipeline",
):
    '''A CloudFormation ``AWS::ImageBuilder::ImagePipeline``.

    :cloudformationResource: AWS::ImageBuilder::ImagePipeline
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        infrastructure_configuration_arn: builtins.str,
        name: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_tests_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImagePipeline.ImageTestsConfigurationProperty"]] = None,
        schedule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImagePipeline.ScheduleProperty"]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::ImagePipeline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param infrastructure_configuration_arn: ``AWS::ImageBuilder::ImagePipeline.InfrastructureConfigurationArn``.
        :param name: ``AWS::ImageBuilder::ImagePipeline.Name``.
        :param container_recipe_arn: ``AWS::ImageBuilder::ImagePipeline.ContainerRecipeArn``.
        :param description: ``AWS::ImageBuilder::ImagePipeline.Description``.
        :param distribution_configuration_arn: ``AWS::ImageBuilder::ImagePipeline.DistributionConfigurationArn``.
        :param enhanced_image_metadata_enabled: ``AWS::ImageBuilder::ImagePipeline.EnhancedImageMetadataEnabled``.
        :param image_recipe_arn: ``AWS::ImageBuilder::ImagePipeline.ImageRecipeArn``.
        :param image_tests_configuration: ``AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration``.
        :param schedule: ``AWS::ImageBuilder::ImagePipeline.Schedule``.
        :param status: ``AWS::ImageBuilder::ImagePipeline.Status``.
        :param tags: ``AWS::ImageBuilder::ImagePipeline.Tags``.
        '''
        props = CfnImagePipelineProps(
            infrastructure_configuration_arn=infrastructure_configuration_arn,
            name=name,
            container_recipe_arn=container_recipe_arn,
            description=description,
            distribution_configuration_arn=distribution_configuration_arn,
            enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
            image_recipe_arn=image_recipe_arn,
            image_tests_configuration=image_tests_configuration,
            schedule=schedule,
            status=status,
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
        '''``AWS::ImageBuilder::ImagePipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImagePipeline.InfrastructureConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "infrastructureConfigurationArn"))

    @infrastructure_configuration_arn.setter
    def infrastructure_configuration_arn(self, value: builtins.str) -> None:
        jsii.set(self, "infrastructureConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImagePipeline.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containerRecipeArn")
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.ContainerRecipeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-containerrecipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRecipeArn"))

    @container_recipe_arn.setter
    def container_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "containerRecipeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="distributionConfigurationArn")
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.DistributionConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-distributionconfigurationarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionConfigurationArn"))

    @distribution_configuration_arn.setter
    def distribution_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "distributionConfigurationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ImageBuilder::ImagePipeline.EnhancedImageMetadataEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enhancedImageMetadataEnabled"))

    @enhanced_image_metadata_enabled.setter
    def enhanced_image_metadata_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enhancedImageMetadataEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageRecipeArn")
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.ImageRecipeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagerecipearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageRecipeArn"))

    @image_recipe_arn.setter
    def image_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "imageRecipeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImagePipeline.ImageTestsConfigurationProperty"]]:
        '''``AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImagePipeline.ImageTestsConfigurationProperty"]], jsii.get(self, "imageTestsConfiguration"))

    @image_tests_configuration.setter
    def image_tests_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImagePipeline.ImageTestsConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "imageTestsConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImagePipeline.ScheduleProperty"]]:
        '''``AWS::ImageBuilder::ImagePipeline.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-schedule
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImagePipeline.ScheduleProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImagePipeline.ScheduleProperty"]],
    ) -> None:
        jsii.set(self, "schedule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_tests_enabled": "imageTestsEnabled",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class ImageTestsConfigurationProperty:
        def __init__(
            self,
            *,
            image_tests_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param image_tests_enabled: ``CfnImagePipeline.ImageTestsConfigurationProperty.ImageTestsEnabled``.
            :param timeout_minutes: ``CfnImagePipeline.ImageTestsConfigurationProperty.TimeoutMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if image_tests_enabled is not None:
                self._values["image_tests_enabled"] = image_tests_enabled
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def image_tests_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnImagePipeline.ImageTestsConfigurationProperty.ImageTestsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-imagetestsenabled
            '''
            result = self._values.get("image_tests_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''``CfnImagePipeline.ImageTestsConfigurationProperty.TimeoutMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageTestsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipeline.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pipeline_execution_start_condition": "pipelineExecutionStartCondition",
            "schedule_expression": "scheduleExpression",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            pipeline_execution_start_condition: typing.Optional[builtins.str] = None,
            schedule_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param pipeline_execution_start_condition: ``CfnImagePipeline.ScheduleProperty.PipelineExecutionStartCondition``.
            :param schedule_expression: ``CfnImagePipeline.ScheduleProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if pipeline_execution_start_condition is not None:
                self._values["pipeline_execution_start_condition"] = pipeline_execution_start_condition
            if schedule_expression is not None:
                self._values["schedule_expression"] = schedule_expression

        @builtins.property
        def pipeline_execution_start_condition(self) -> typing.Optional[builtins.str]:
            '''``CfnImagePipeline.ScheduleProperty.PipelineExecutionStartCondition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html#cfn-imagebuilder-imagepipeline-schedule-pipelineexecutionstartcondition
            '''
            result = self._values.get("pipeline_execution_start_condition")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schedule_expression(self) -> typing.Optional[builtins.str]:
            '''``CfnImagePipeline.ScheduleProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html#cfn-imagebuilder-imagepipeline-schedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImagePipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "infrastructure_configuration_arn": "infrastructureConfigurationArn",
        "name": "name",
        "container_recipe_arn": "containerRecipeArn",
        "description": "description",
        "distribution_configuration_arn": "distributionConfigurationArn",
        "enhanced_image_metadata_enabled": "enhancedImageMetadataEnabled",
        "image_recipe_arn": "imageRecipeArn",
        "image_tests_configuration": "imageTestsConfiguration",
        "schedule": "schedule",
        "status": "status",
        "tags": "tags",
    },
)
class CfnImagePipelineProps:
    def __init__(
        self,
        *,
        infrastructure_configuration_arn: builtins.str,
        name: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_tests_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImagePipeline.ImageTestsConfigurationProperty]] = None,
        schedule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImagePipeline.ScheduleProperty]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ImageBuilder::ImagePipeline``.

        :param infrastructure_configuration_arn: ``AWS::ImageBuilder::ImagePipeline.InfrastructureConfigurationArn``.
        :param name: ``AWS::ImageBuilder::ImagePipeline.Name``.
        :param container_recipe_arn: ``AWS::ImageBuilder::ImagePipeline.ContainerRecipeArn``.
        :param description: ``AWS::ImageBuilder::ImagePipeline.Description``.
        :param distribution_configuration_arn: ``AWS::ImageBuilder::ImagePipeline.DistributionConfigurationArn``.
        :param enhanced_image_metadata_enabled: ``AWS::ImageBuilder::ImagePipeline.EnhancedImageMetadataEnabled``.
        :param image_recipe_arn: ``AWS::ImageBuilder::ImagePipeline.ImageRecipeArn``.
        :param image_tests_configuration: ``AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration``.
        :param schedule: ``AWS::ImageBuilder::ImagePipeline.Schedule``.
        :param status: ``AWS::ImageBuilder::ImagePipeline.Status``.
        :param tags: ``AWS::ImageBuilder::ImagePipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "name": name,
        }
        if container_recipe_arn is not None:
            self._values["container_recipe_arn"] = container_recipe_arn
        if description is not None:
            self._values["description"] = description
        if distribution_configuration_arn is not None:
            self._values["distribution_configuration_arn"] = distribution_configuration_arn
        if enhanced_image_metadata_enabled is not None:
            self._values["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if image_recipe_arn is not None:
            self._values["image_recipe_arn"] = image_recipe_arn
        if image_tests_configuration is not None:
            self._values["image_tests_configuration"] = image_tests_configuration
        if schedule is not None:
            self._values["schedule"] = schedule
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImagePipeline.InfrastructureConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn
        '''
        result = self._values.get("infrastructure_configuration_arn")
        assert result is not None, "Required property 'infrastructure_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImagePipeline.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.ContainerRecipeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-containerrecipearn
        '''
        result = self._values.get("container_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.DistributionConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-distributionconfigurationarn
        '''
        result = self._values.get("distribution_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ImageBuilder::ImagePipeline.EnhancedImageMetadataEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled
        '''
        result = self._values.get("enhanced_image_metadata_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.ImageRecipeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagerecipearn
        '''
        result = self._values.get("image_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImagePipeline.ImageTestsConfigurationProperty]]:
        '''``AWS::ImageBuilder::ImagePipeline.ImageTestsConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration
        '''
        result = self._values.get("image_tests_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImagePipeline.ImageTestsConfigurationProperty]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImagePipeline.ScheduleProperty]]:
        '''``AWS::ImageBuilder::ImagePipeline.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImagePipeline.ScheduleProperty]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImagePipeline.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::ImageBuilder::ImagePipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImagePipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImageProps",
    jsii_struct_bases=[],
    name_mapping={
        "infrastructure_configuration_arn": "infrastructureConfigurationArn",
        "container_recipe_arn": "containerRecipeArn",
        "distribution_configuration_arn": "distributionConfigurationArn",
        "enhanced_image_metadata_enabled": "enhancedImageMetadataEnabled",
        "image_recipe_arn": "imageRecipeArn",
        "image_tests_configuration": "imageTestsConfiguration",
        "tags": "tags",
    },
)
class CfnImageProps:
    def __init__(
        self,
        *,
        infrastructure_configuration_arn: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_tests_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImage.ImageTestsConfigurationProperty]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ImageBuilder::Image``.

        :param infrastructure_configuration_arn: ``AWS::ImageBuilder::Image.InfrastructureConfigurationArn``.
        :param container_recipe_arn: ``AWS::ImageBuilder::Image.ContainerRecipeArn``.
        :param distribution_configuration_arn: ``AWS::ImageBuilder::Image.DistributionConfigurationArn``.
        :param enhanced_image_metadata_enabled: ``AWS::ImageBuilder::Image.EnhancedImageMetadataEnabled``.
        :param image_recipe_arn: ``AWS::ImageBuilder::Image.ImageRecipeArn``.
        :param image_tests_configuration: ``AWS::ImageBuilder::Image.ImageTestsConfiguration``.
        :param tags: ``AWS::ImageBuilder::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
        }
        if container_recipe_arn is not None:
            self._values["container_recipe_arn"] = container_recipe_arn
        if distribution_configuration_arn is not None:
            self._values["distribution_configuration_arn"] = distribution_configuration_arn
        if enhanced_image_metadata_enabled is not None:
            self._values["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if image_recipe_arn is not None:
            self._values["image_recipe_arn"] = image_recipe_arn
        if image_tests_configuration is not None:
            self._values["image_tests_configuration"] = image_tests_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''``AWS::ImageBuilder::Image.InfrastructureConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-infrastructureconfigurationarn
        '''
        result = self._values.get("infrastructure_configuration_arn")
        assert result is not None, "Required property 'infrastructure_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Image.ContainerRecipeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-containerrecipearn
        '''
        result = self._values.get("container_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Image.DistributionConfigurationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-distributionconfigurationarn
        '''
        result = self._values.get("distribution_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ImageBuilder::Image.EnhancedImageMetadataEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-enhancedimagemetadataenabled
        '''
        result = self._values.get("enhanced_image_metadata_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::Image.ImageRecipeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagerecipearn
        '''
        result = self._values.get("image_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImage.ImageTestsConfigurationProperty]]:
        '''``AWS::ImageBuilder::Image.ImageTestsConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagetestsconfiguration
        '''
        result = self._values.get("image_tests_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImage.ImageTestsConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::ImageBuilder::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnImageRecipe(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe",
):
    '''A CloudFormation ``AWS::ImageBuilder::ImageRecipe``.

    :cloudformationResource: AWS::ImageBuilder::ImageRecipe
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        components: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.ComponentConfigurationProperty"]]],
        name: builtins.str,
        parent_image: builtins.str,
        version: builtins.str,
        additional_instance_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]] = None,
        block_device_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::ImageRecipe``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param components: ``AWS::ImageBuilder::ImageRecipe.Components``.
        :param name: ``AWS::ImageBuilder::ImageRecipe.Name``.
        :param parent_image: ``AWS::ImageBuilder::ImageRecipe.ParentImage``.
        :param version: ``AWS::ImageBuilder::ImageRecipe.Version``.
        :param additional_instance_configuration: ``AWS::ImageBuilder::ImageRecipe.AdditionalInstanceConfiguration``.
        :param block_device_mappings: ``AWS::ImageBuilder::ImageRecipe.BlockDeviceMappings``.
        :param description: ``AWS::ImageBuilder::ImageRecipe.Description``.
        :param tags: ``AWS::ImageBuilder::ImageRecipe.Tags``.
        :param working_directory: ``AWS::ImageBuilder::ImageRecipe.WorkingDirectory``.
        '''
        props = CfnImageRecipeProps(
            components=components,
            name=name,
            parent_image=parent_image,
            version=version,
            additional_instance_configuration=additional_instance_configuration,
            block_device_mappings=block_device_mappings,
            description=description,
            tags=tags,
            working_directory=working_directory,
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
        '''``AWS::ImageBuilder::ImageRecipe.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="components")
    def components(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.ComponentConfigurationProperty"]]]:
        '''``AWS::ImageBuilder::ImageRecipe.Components``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-components
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.ComponentConfigurationProperty"]]], jsii.get(self, "components"))

    @components.setter
    def components(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.ComponentConfigurationProperty"]]],
    ) -> None:
        jsii.set(self, "components", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImageRecipe.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parentImage")
    def parent_image(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImageRecipe.ParentImage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-parentimage
        '''
        return typing.cast(builtins.str, jsii.get(self, "parentImage"))

    @parent_image.setter
    def parent_image(self, value: builtins.str) -> None:
        jsii.set(self, "parentImage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImageRecipe.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-version
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        jsii.set(self, "version", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="additionalInstanceConfiguration")
    def additional_instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]]:
        '''``AWS::ImageBuilder::ImageRecipe.AdditionalInstanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]], jsii.get(self, "additionalInstanceConfiguration"))

    @additional_instance_configuration.setter
    def additional_instance_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "additionalInstanceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]]:
        '''``AWS::ImageBuilder::ImageRecipe.BlockDeviceMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-blockdevicemappings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]], jsii.get(self, "blockDeviceMappings"))

    @block_device_mappings.setter
    def block_device_mappings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]],
    ) -> None:
        jsii.set(self, "blockDeviceMappings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImageRecipe.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImageRecipe.WorkingDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-workingdirectory
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "workingDirectory", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "systems_manager_agent": "systemsManagerAgent",
            "user_data_override": "userDataOverride",
        },
    )
    class AdditionalInstanceConfigurationProperty:
        def __init__(
            self,
            *,
            systems_manager_agent: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.SystemsManagerAgentProperty"]] = None,
            user_data_override: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param systems_manager_agent: ``CfnImageRecipe.AdditionalInstanceConfigurationProperty.SystemsManagerAgent``.
            :param user_data_override: ``CfnImageRecipe.AdditionalInstanceConfigurationProperty.UserDataOverride``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if systems_manager_agent is not None:
                self._values["systems_manager_agent"] = systems_manager_agent
            if user_data_override is not None:
                self._values["user_data_override"] = user_data_override

        @builtins.property
        def systems_manager_agent(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.SystemsManagerAgentProperty"]]:
            '''``CfnImageRecipe.AdditionalInstanceConfigurationProperty.SystemsManagerAgent``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration-systemsmanageragent
            '''
            result = self._values.get("systems_manager_agent")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.SystemsManagerAgentProperty"]], result)

        @builtins.property
        def user_data_override(self) -> typing.Optional[builtins.str]:
            '''``CfnImageRecipe.AdditionalInstanceConfigurationProperty.UserDataOverride``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration-userdataoverride
            '''
            result = self._values.get("user_data_override")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdditionalInstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.ComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"component_arn": "componentArn", "parameters": "parameters"},
    )
    class ComponentConfigurationProperty:
        def __init__(
            self,
            *,
            component_arn: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.ComponentParameterProperty"]]]] = None,
        ) -> None:
            '''
            :param component_arn: ``CfnImageRecipe.ComponentConfigurationProperty.ComponentArn``.
            :param parameters: ``CfnImageRecipe.ComponentConfigurationProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if component_arn is not None:
                self._values["component_arn"] = component_arn
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def component_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnImageRecipe.ComponentConfigurationProperty.ComponentArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html#cfn-imagebuilder-imagerecipe-componentconfiguration-componentarn
            '''
            result = self._values.get("component_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.ComponentParameterProperty"]]]]:
            '''``CfnImageRecipe.ComponentConfigurationProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html#cfn-imagebuilder-imagerecipe-componentconfiguration-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.ComponentParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.ComponentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ComponentParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param name: ``CfnImageRecipe.ComponentParameterProperty.Name``.
            :param value: ``CfnImageRecipe.ComponentParameterProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnImageRecipe.ComponentParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html#cfn-imagebuilder-imagerecipe-componentparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.List[builtins.str]:
            '''``CfnImageRecipe.ComponentParameterProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html#cfn-imagebuilder-imagerecipe-componentparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_on_termination": "deleteOnTermination",
            "encrypted": "encrypted",
            "iops": "iops",
            "kms_key_id": "kmsKeyId",
            "snapshot_id": "snapshotId",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsInstanceBlockDeviceSpecificationProperty:
        def __init__(
            self,
            *,
            delete_on_termination: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            encrypted: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            iops: typing.Optional[jsii.Number] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            snapshot_id: typing.Optional[builtins.str] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param delete_on_termination: ``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.DeleteOnTermination``.
            :param encrypted: ``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.Encrypted``.
            :param iops: ``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.Iops``.
            :param kms_key_id: ``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.KmsKeyId``.
            :param snapshot_id: ``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.SnapshotId``.
            :param volume_size: ``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.VolumeSize``.
            :param volume_type: ``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delete_on_termination is not None:
                self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if snapshot_id is not None:
                self._values["snapshot_id"] = snapshot_id
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def delete_on_termination(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.DeleteOnTermination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-deleteontermination
            '''
            result = self._values.get("delete_on_termination")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.Encrypted``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_id(self) -> typing.Optional[builtins.str]:
            '''``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.SnapshotId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-snapshotid
            '''
            result = self._values.get("snapshot_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.VolumeSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''``CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsInstanceBlockDeviceSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class InstanceBlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty"]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param device_name: ``CfnImageRecipe.InstanceBlockDeviceMappingProperty.DeviceName``.
            :param ebs: ``CfnImageRecipe.InstanceBlockDeviceMappingProperty.Ebs``.
            :param no_device: ``CfnImageRecipe.InstanceBlockDeviceMappingProperty.NoDevice``.
            :param virtual_name: ``CfnImageRecipe.InstanceBlockDeviceMappingProperty.VirtualName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''``CfnImageRecipe.InstanceBlockDeviceMappingProperty.DeviceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty"]]:
            '''``CfnImageRecipe.InstanceBlockDeviceMappingProperty.Ebs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''``CfnImageRecipe.InstanceBlockDeviceMappingProperty.NoDevice``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''``CfnImageRecipe.InstanceBlockDeviceMappingProperty.VirtualName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceBlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty",
        jsii_struct_bases=[],
        name_mapping={"uninstall_after_build": "uninstallAfterBuild"},
    )
    class SystemsManagerAgentProperty:
        def __init__(
            self,
            *,
            uninstall_after_build: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param uninstall_after_build: ``CfnImageRecipe.SystemsManagerAgentProperty.UninstallAfterBuild``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if uninstall_after_build is not None:
                self._values["uninstall_after_build"] = uninstall_after_build

        @builtins.property
        def uninstall_after_build(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnImageRecipe.SystemsManagerAgentProperty.UninstallAfterBuild``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html#cfn-imagebuilder-imagerecipe-systemsmanageragent-uninstallafterbuild
            '''
            result = self._values.get("uninstall_after_build")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SystemsManagerAgentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnImageRecipeProps",
    jsii_struct_bases=[],
    name_mapping={
        "components": "components",
        "name": "name",
        "parent_image": "parentImage",
        "version": "version",
        "additional_instance_configuration": "additionalInstanceConfiguration",
        "block_device_mappings": "blockDeviceMappings",
        "description": "description",
        "tags": "tags",
        "working_directory": "workingDirectory",
    },
)
class CfnImageRecipeProps:
    def __init__(
        self,
        *,
        components: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.ComponentConfigurationProperty]]],
        name: builtins.str,
        parent_image: builtins.str,
        version: builtins.str,
        additional_instance_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.AdditionalInstanceConfigurationProperty]] = None,
        block_device_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ImageBuilder::ImageRecipe``.

        :param components: ``AWS::ImageBuilder::ImageRecipe.Components``.
        :param name: ``AWS::ImageBuilder::ImageRecipe.Name``.
        :param parent_image: ``AWS::ImageBuilder::ImageRecipe.ParentImage``.
        :param version: ``AWS::ImageBuilder::ImageRecipe.Version``.
        :param additional_instance_configuration: ``AWS::ImageBuilder::ImageRecipe.AdditionalInstanceConfiguration``.
        :param block_device_mappings: ``AWS::ImageBuilder::ImageRecipe.BlockDeviceMappings``.
        :param description: ``AWS::ImageBuilder::ImageRecipe.Description``.
        :param tags: ``AWS::ImageBuilder::ImageRecipe.Tags``.
        :param working_directory: ``AWS::ImageBuilder::ImageRecipe.WorkingDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "components": components,
            "name": name,
            "parent_image": parent_image,
            "version": version,
        }
        if additional_instance_configuration is not None:
            self._values["additional_instance_configuration"] = additional_instance_configuration
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def components(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.ComponentConfigurationProperty]]]:
        '''``AWS::ImageBuilder::ImageRecipe.Components``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-components
        '''
        result = self._values.get("components")
        assert result is not None, "Required property 'components' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.ComponentConfigurationProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImageRecipe.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_image(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImageRecipe.ParentImage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-parentimage
        '''
        result = self._values.get("parent_image")
        assert result is not None, "Required property 'parent_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''``AWS::ImageBuilder::ImageRecipe.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.AdditionalInstanceConfigurationProperty]]:
        '''``AWS::ImageBuilder::ImageRecipe.AdditionalInstanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration
        '''
        result = self._values.get("additional_instance_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.AdditionalInstanceConfigurationProperty]], result)

    @builtins.property
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]]:
        '''``AWS::ImageBuilder::ImageRecipe.BlockDeviceMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-blockdevicemappings
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImageRecipe.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::ImageBuilder::ImageRecipe.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::ImageRecipe.WorkingDirectory``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-workingdirectory
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageRecipeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInfrastructureConfiguration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfiguration",
):
    '''A CloudFormation ``AWS::ImageBuilder::InfrastructureConfiguration``.

    :cloudformationResource: AWS::ImageBuilder::InfrastructureConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_profile_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInfrastructureConfiguration.LoggingProperty"]] = None,
        resource_tags: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Create a new ``AWS::ImageBuilder::InfrastructureConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_profile_name: ``AWS::ImageBuilder::InfrastructureConfiguration.InstanceProfileName``.
        :param name: ``AWS::ImageBuilder::InfrastructureConfiguration.Name``.
        :param description: ``AWS::ImageBuilder::InfrastructureConfiguration.Description``.
        :param instance_types: ``AWS::ImageBuilder::InfrastructureConfiguration.InstanceTypes``.
        :param key_pair: ``AWS::ImageBuilder::InfrastructureConfiguration.KeyPair``.
        :param logging: ``AWS::ImageBuilder::InfrastructureConfiguration.Logging``.
        :param resource_tags: ``AWS::ImageBuilder::InfrastructureConfiguration.ResourceTags``.
        :param security_group_ids: ``AWS::ImageBuilder::InfrastructureConfiguration.SecurityGroupIds``.
        :param sns_topic_arn: ``AWS::ImageBuilder::InfrastructureConfiguration.SnsTopicArn``.
        :param subnet_id: ``AWS::ImageBuilder::InfrastructureConfiguration.SubnetId``.
        :param tags: ``AWS::ImageBuilder::InfrastructureConfiguration.Tags``.
        :param terminate_instance_on_failure: ``AWS::ImageBuilder::InfrastructureConfiguration.TerminateInstanceOnFailure``.
        '''
        props = CfnInfrastructureConfigurationProps(
            instance_profile_name=instance_profile_name,
            name=name,
            description=description,
            instance_types=instance_types,
            key_pair=key_pair,
            logging=logging,
            resource_tags=resource_tags,
            security_group_ids=security_group_ids,
            sns_topic_arn=sns_topic_arn,
            subnet_id=subnet_id,
            tags=tags,
            terminate_instance_on_failure=terminate_instance_on_failure,
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
        '''``AWS::ImageBuilder::InfrastructureConfiguration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> builtins.str:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.InstanceProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instanceprofilename
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileName"))

    @instance_profile_name.setter
    def instance_profile_name(self, value: builtins.str) -> None:
        jsii.set(self, "instanceProfileName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceTypes")
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.InstanceTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancetypes
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceTypes"))

    @instance_types.setter
    def instance_types(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "instanceTypes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyPair")
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.KeyPair``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-keypair
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPair"))

    @key_pair.setter
    def key_pair(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "keyPair", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logging")
    def logging(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInfrastructureConfiguration.LoggingProperty"]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.Logging``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-logging
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInfrastructureConfiguration.LoggingProperty"]], jsii.get(self, "logging"))

    @logging.setter
    def logging(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInfrastructureConfiguration.LoggingProperty"]],
    ) -> None:
        jsii.set(self, "logging", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.ResourceTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-resourcetags
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "resourceTags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-securitygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.SnsTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-snstopicarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snsTopicArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-subnetid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subnetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.TerminateInstanceOnFailure``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "terminateInstanceOnFailure"))

    @terminate_instance_on_failure.setter
    def terminate_instance_on_failure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "terminateInstanceOnFailure", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfiguration.LoggingProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_logs": "s3Logs"},
    )
    class LoggingProperty:
        def __init__(
            self,
            *,
            s3_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInfrastructureConfiguration.S3LogsProperty"]] = None,
        ) -> None:
            '''
            :param s3_logs: ``CfnInfrastructureConfiguration.LoggingProperty.S3Logs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_logs is not None:
                self._values["s3_logs"] = s3_logs

        @builtins.property
        def s3_logs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInfrastructureConfiguration.S3LogsProperty"]]:
            '''``CfnInfrastructureConfiguration.LoggingProperty.S3Logs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html#cfn-imagebuilder-infrastructureconfiguration-logging-s3logs
            '''
            result = self._values.get("s3_logs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInfrastructureConfiguration.S3LogsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket_name": "s3BucketName",
            "s3_key_prefix": "s3KeyPrefix",
        },
    )
    class S3LogsProperty:
        def __init__(
            self,
            *,
            s3_bucket_name: typing.Optional[builtins.str] = None,
            s3_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param s3_bucket_name: ``CfnInfrastructureConfiguration.S3LogsProperty.S3BucketName``.
            :param s3_key_prefix: ``CfnInfrastructureConfiguration.S3LogsProperty.S3KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name
            if s3_key_prefix is not None:
                self._values["s3_key_prefix"] = s3_key_prefix

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''``CfnInfrastructureConfiguration.S3LogsProperty.S3BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnInfrastructureConfiguration.S3LogsProperty.S3KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix
            '''
            result = self._values.get("s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-imagebuilder.CfnInfrastructureConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile_name": "instanceProfileName",
        "name": "name",
        "description": "description",
        "instance_types": "instanceTypes",
        "key_pair": "keyPair",
        "logging": "logging",
        "resource_tags": "resourceTags",
        "security_group_ids": "securityGroupIds",
        "sns_topic_arn": "snsTopicArn",
        "subnet_id": "subnetId",
        "tags": "tags",
        "terminate_instance_on_failure": "terminateInstanceOnFailure",
    },
)
class CfnInfrastructureConfigurationProps:
    def __init__(
        self,
        *,
        instance_profile_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInfrastructureConfiguration.LoggingProperty]] = None,
        resource_tags: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ImageBuilder::InfrastructureConfiguration``.

        :param instance_profile_name: ``AWS::ImageBuilder::InfrastructureConfiguration.InstanceProfileName``.
        :param name: ``AWS::ImageBuilder::InfrastructureConfiguration.Name``.
        :param description: ``AWS::ImageBuilder::InfrastructureConfiguration.Description``.
        :param instance_types: ``AWS::ImageBuilder::InfrastructureConfiguration.InstanceTypes``.
        :param key_pair: ``AWS::ImageBuilder::InfrastructureConfiguration.KeyPair``.
        :param logging: ``AWS::ImageBuilder::InfrastructureConfiguration.Logging``.
        :param resource_tags: ``AWS::ImageBuilder::InfrastructureConfiguration.ResourceTags``.
        :param security_group_ids: ``AWS::ImageBuilder::InfrastructureConfiguration.SecurityGroupIds``.
        :param sns_topic_arn: ``AWS::ImageBuilder::InfrastructureConfiguration.SnsTopicArn``.
        :param subnet_id: ``AWS::ImageBuilder::InfrastructureConfiguration.SubnetId``.
        :param tags: ``AWS::ImageBuilder::InfrastructureConfiguration.Tags``.
        :param terminate_instance_on_failure: ``AWS::ImageBuilder::InfrastructureConfiguration.TerminateInstanceOnFailure``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_profile_name": instance_profile_name,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if logging is not None:
            self._values["logging"] = logging
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if sns_topic_arn is not None:
            self._values["sns_topic_arn"] = sns_topic_arn
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if terminate_instance_on_failure is not None:
            self._values["terminate_instance_on_failure"] = terminate_instance_on_failure

    @builtins.property
    def instance_profile_name(self) -> builtins.str:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.InstanceProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instanceprofilename
        '''
        result = self._values.get("instance_profile_name")
        assert result is not None, "Required property 'instance_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.InstanceTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancetypes
        '''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.KeyPair``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-keypair
        '''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInfrastructureConfiguration.LoggingProperty]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.Logging``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-logging
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInfrastructureConfiguration.LoggingProperty]], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.ResourceTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.SnsTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def terminate_instance_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ImageBuilder::InfrastructureConfiguration.TerminateInstanceOnFailure``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure
        '''
        result = self._values.get("terminate_instance_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInfrastructureConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComponent",
    "CfnComponentProps",
    "CfnContainerRecipe",
    "CfnContainerRecipeProps",
    "CfnDistributionConfiguration",
    "CfnDistributionConfigurationProps",
    "CfnImage",
    "CfnImagePipeline",
    "CfnImagePipelineProps",
    "CfnImageProps",
    "CfnImageRecipe",
    "CfnImageRecipeProps",
    "CfnInfrastructureConfiguration",
    "CfnInfrastructureConfigurationProps",
]

publication.publish()
