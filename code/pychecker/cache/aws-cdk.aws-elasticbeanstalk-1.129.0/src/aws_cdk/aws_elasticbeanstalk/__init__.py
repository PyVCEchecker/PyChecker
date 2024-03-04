'''
# AWS Elastic Beanstalk Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
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
    jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplication",
):
    '''A CloudFormation ``AWS::ElasticBeanstalk::Application``.

    :cloudformationResource: AWS::ElasticBeanstalk::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        resource_lifecycle_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.ApplicationResourceLifecycleConfigProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::ElasticBeanstalk::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: ``AWS::ElasticBeanstalk::Application.ApplicationName``.
        :param description: ``AWS::ElasticBeanstalk::Application.Description``.
        :param resource_lifecycle_config: ``AWS::ElasticBeanstalk::Application.ResourceLifecycleConfig``.
        '''
        props = CfnApplicationProps(
            application_name=application_name,
            description=description,
            resource_lifecycle_config=resource_lifecycle_config,
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Application.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "applicationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Application.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceLifecycleConfig")
    def resource_lifecycle_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.ApplicationResourceLifecycleConfigProperty"]]:
        '''``AWS::ElasticBeanstalk::Application.ResourceLifecycleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-resourcelifecycleconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.ApplicationResourceLifecycleConfigProperty"]], jsii.get(self, "resourceLifecycleConfig"))

    @resource_lifecycle_config.setter
    def resource_lifecycle_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.ApplicationResourceLifecycleConfigProperty"]],
    ) -> None:
        jsii.set(self, "resourceLifecycleConfig", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplication.ApplicationResourceLifecycleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "service_role": "serviceRole",
            "version_lifecycle_config": "versionLifecycleConfig",
        },
    )
    class ApplicationResourceLifecycleConfigProperty:
        def __init__(
            self,
            *,
            service_role: typing.Optional[builtins.str] = None,
            version_lifecycle_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.ApplicationVersionLifecycleConfigProperty"]] = None,
        ) -> None:
            '''
            :param service_role: ``CfnApplication.ApplicationResourceLifecycleConfigProperty.ServiceRole``.
            :param version_lifecycle_config: ``CfnApplication.ApplicationResourceLifecycleConfigProperty.VersionLifecycleConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if service_role is not None:
                self._values["service_role"] = service_role
            if version_lifecycle_config is not None:
                self._values["version_lifecycle_config"] = version_lifecycle_config

        @builtins.property
        def service_role(self) -> typing.Optional[builtins.str]:
            '''``CfnApplication.ApplicationResourceLifecycleConfigProperty.ServiceRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-servicerole
            '''
            result = self._values.get("service_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version_lifecycle_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.ApplicationVersionLifecycleConfigProperty"]]:
            '''``CfnApplication.ApplicationResourceLifecycleConfigProperty.VersionLifecycleConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationresourcelifecycleconfig.html#cfn-elasticbeanstalk-application-applicationresourcelifecycleconfig-versionlifecycleconfig
            '''
            result = self._values.get("version_lifecycle_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.ApplicationVersionLifecycleConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationResourceLifecycleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplication.ApplicationVersionLifecycleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"max_age_rule": "maxAgeRule", "max_count_rule": "maxCountRule"},
    )
    class ApplicationVersionLifecycleConfigProperty:
        def __init__(
            self,
            *,
            max_age_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.MaxAgeRuleProperty"]] = None,
            max_count_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.MaxCountRuleProperty"]] = None,
        ) -> None:
            '''
            :param max_age_rule: ``CfnApplication.ApplicationVersionLifecycleConfigProperty.MaxAgeRule``.
            :param max_count_rule: ``CfnApplication.ApplicationVersionLifecycleConfigProperty.MaxCountRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if max_age_rule is not None:
                self._values["max_age_rule"] = max_age_rule
            if max_count_rule is not None:
                self._values["max_count_rule"] = max_count_rule

        @builtins.property
        def max_age_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.MaxAgeRuleProperty"]]:
            '''``CfnApplication.ApplicationVersionLifecycleConfigProperty.MaxAgeRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxagerule
            '''
            result = self._values.get("max_age_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.MaxAgeRuleProperty"]], result)

        @builtins.property
        def max_count_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.MaxCountRuleProperty"]]:
            '''``CfnApplication.ApplicationVersionLifecycleConfigProperty.MaxCountRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-applicationversionlifecycleconfig.html#cfn-elasticbeanstalk-application-applicationversionlifecycleconfig-maxcountrule
            '''
            result = self._values.get("max_count_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.MaxCountRuleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationVersionLifecycleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplication.MaxAgeRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_source_from_s3": "deleteSourceFromS3",
            "enabled": "enabled",
            "max_age_in_days": "maxAgeInDays",
        },
    )
    class MaxAgeRuleProperty:
        def __init__(
            self,
            *,
            delete_source_from_s3: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            max_age_in_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param delete_source_from_s3: ``CfnApplication.MaxAgeRuleProperty.DeleteSourceFromS3``.
            :param enabled: ``CfnApplication.MaxAgeRuleProperty.Enabled``.
            :param max_age_in_days: ``CfnApplication.MaxAgeRuleProperty.MaxAgeInDays``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delete_source_from_s3 is not None:
                self._values["delete_source_from_s3"] = delete_source_from_s3
            if enabled is not None:
                self._values["enabled"] = enabled
            if max_age_in_days is not None:
                self._values["max_age_in_days"] = max_age_in_days

        @builtins.property
        def delete_source_from_s3(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnApplication.MaxAgeRuleProperty.DeleteSourceFromS3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-deletesourcefroms3
            '''
            result = self._values.get("delete_source_from_s3")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnApplication.MaxAgeRuleProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def max_age_in_days(self) -> typing.Optional[jsii.Number]:
            '''``CfnApplication.MaxAgeRuleProperty.MaxAgeInDays``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxagerule.html#cfn-elasticbeanstalk-application-maxagerule-maxageindays
            '''
            result = self._values.get("max_age_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaxAgeRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplication.MaxCountRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_source_from_s3": "deleteSourceFromS3",
            "enabled": "enabled",
            "max_count": "maxCount",
        },
    )
    class MaxCountRuleProperty:
        def __init__(
            self,
            *,
            delete_source_from_s3: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            max_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param delete_source_from_s3: ``CfnApplication.MaxCountRuleProperty.DeleteSourceFromS3``.
            :param enabled: ``CfnApplication.MaxCountRuleProperty.Enabled``.
            :param max_count: ``CfnApplication.MaxCountRuleProperty.MaxCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delete_source_from_s3 is not None:
                self._values["delete_source_from_s3"] = delete_source_from_s3
            if enabled is not None:
                self._values["enabled"] = enabled
            if max_count is not None:
                self._values["max_count"] = max_count

        @builtins.property
        def delete_source_from_s3(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnApplication.MaxCountRuleProperty.DeleteSourceFromS3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-deletesourcefroms3
            '''
            result = self._values.get("delete_source_from_s3")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnApplication.MaxCountRuleProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def max_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnApplication.MaxCountRuleProperty.MaxCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-application-maxcountrule.html#cfn-elasticbeanstalk-application-maxcountrule-maxcount
            '''
            result = self._values.get("max_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaxCountRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "description": "description",
        "resource_lifecycle_config": "resourceLifecycleConfig",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        resource_lifecycle_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplication.ApplicationResourceLifecycleConfigProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElasticBeanstalk::Application``.

        :param application_name: ``AWS::ElasticBeanstalk::Application.ApplicationName``.
        :param description: ``AWS::ElasticBeanstalk::Application.Description``.
        :param resource_lifecycle_config: ``AWS::ElasticBeanstalk::Application.ResourceLifecycleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name
        if description is not None:
            self._values["description"] = description
        if resource_lifecycle_config is not None:
            self._values["resource_lifecycle_config"] = resource_lifecycle_config

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Application.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-name
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Application.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_lifecycle_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplication.ApplicationResourceLifecycleConfigProperty]]:
        '''``AWS::ElasticBeanstalk::Application.ResourceLifecycleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html#cfn-elasticbeanstalk-application-resourcelifecycleconfig
        '''
        result = self._values.get("resource_lifecycle_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplication.ApplicationResourceLifecycleConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnApplicationVersion(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplicationVersion",
):
    '''A CloudFormation ``AWS::ElasticBeanstalk::ApplicationVersion``.

    :cloudformationResource: AWS::ElasticBeanstalk::ApplicationVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        source_bundle: typing.Union["CfnApplicationVersion.SourceBundleProperty", aws_cdk.core.IResolvable],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ElasticBeanstalk::ApplicationVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: ``AWS::ElasticBeanstalk::ApplicationVersion.ApplicationName``.
        :param source_bundle: ``AWS::ElasticBeanstalk::ApplicationVersion.SourceBundle``.
        :param description: ``AWS::ElasticBeanstalk::ApplicationVersion.Description``.
        '''
        props = CfnApplicationVersionProps(
            application_name=application_name,
            source_bundle=source_bundle,
            description=description,
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''``AWS::ElasticBeanstalk::ApplicationVersion.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        jsii.set(self, "applicationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceBundle")
    def source_bundle(
        self,
    ) -> typing.Union["CfnApplicationVersion.SourceBundleProperty", aws_cdk.core.IResolvable]:
        '''``AWS::ElasticBeanstalk::ApplicationVersion.SourceBundle``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-sourcebundle
        '''
        return typing.cast(typing.Union["CfnApplicationVersion.SourceBundleProperty", aws_cdk.core.IResolvable], jsii.get(self, "sourceBundle"))

    @source_bundle.setter
    def source_bundle(
        self,
        value: typing.Union["CfnApplicationVersion.SourceBundleProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "sourceBundle", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ApplicationVersion.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplicationVersion.SourceBundleProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_bucket": "s3Bucket", "s3_key": "s3Key"},
    )
    class SourceBundleProperty:
        def __init__(self, *, s3_bucket: builtins.str, s3_key: builtins.str) -> None:
            '''
            :param s3_bucket: ``CfnApplicationVersion.SourceBundleProperty.S3Bucket``.
            :param s3_key: ``CfnApplicationVersion.SourceBundleProperty.S3Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''``CfnApplicationVersion.SourceBundleProperty.S3Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html#cfn-beanstalk-sourcebundle-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''``CfnApplicationVersion.SourceBundleProperty.S3Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-sourcebundle.html#cfn-beanstalk-sourcebundle-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceBundleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnApplicationVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "source_bundle": "sourceBundle",
        "description": "description",
    },
)
class CfnApplicationVersionProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        source_bundle: typing.Union[CfnApplicationVersion.SourceBundleProperty, aws_cdk.core.IResolvable],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElasticBeanstalk::ApplicationVersion``.

        :param application_name: ``AWS::ElasticBeanstalk::ApplicationVersion.ApplicationName``.
        :param source_bundle: ``AWS::ElasticBeanstalk::ApplicationVersion.SourceBundle``.
        :param description: ``AWS::ElasticBeanstalk::ApplicationVersion.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_name": application_name,
            "source_bundle": source_bundle,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def application_name(self) -> builtins.str:
        '''``AWS::ElasticBeanstalk::ApplicationVersion.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_bundle(
        self,
    ) -> typing.Union[CfnApplicationVersion.SourceBundleProperty, aws_cdk.core.IResolvable]:
        '''``AWS::ElasticBeanstalk::ApplicationVersion.SourceBundle``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-sourcebundle
        '''
        result = self._values.get("source_bundle")
        assert result is not None, "Required property 'source_bundle' is missing"
        return typing.cast(typing.Union[CfnApplicationVersion.SourceBundleProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ApplicationVersion.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html#cfn-elasticbeanstalk-applicationversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnConfigurationTemplate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnConfigurationTemplate",
):
    '''A CloudFormation ``AWS::ElasticBeanstalk::ConfigurationTemplate``.

    :cloudformationResource: AWS::ElasticBeanstalk::ConfigurationTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        environment_id: typing.Optional[builtins.str] = None,
        option_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationTemplate.ConfigurationOptionSettingProperty"]]]] = None,
        platform_arn: typing.Optional[builtins.str] = None,
        solution_stack_name: typing.Optional[builtins.str] = None,
        source_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationTemplate.SourceConfigurationProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::ElasticBeanstalk::ConfigurationTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: ``AWS::ElasticBeanstalk::ConfigurationTemplate.ApplicationName``.
        :param description: ``AWS::ElasticBeanstalk::ConfigurationTemplate.Description``.
        :param environment_id: ``AWS::ElasticBeanstalk::ConfigurationTemplate.EnvironmentId``.
        :param option_settings: ``AWS::ElasticBeanstalk::ConfigurationTemplate.OptionSettings``.
        :param platform_arn: ``AWS::ElasticBeanstalk::ConfigurationTemplate.PlatformArn``.
        :param solution_stack_name: ``AWS::ElasticBeanstalk::ConfigurationTemplate.SolutionStackName``.
        :param source_configuration: ``AWS::ElasticBeanstalk::ConfigurationTemplate.SourceConfiguration``.
        '''
        props = CfnConfigurationTemplateProps(
            application_name=application_name,
            description=description,
            environment_id=environment_id,
            option_settings=option_settings,
            platform_arn=platform_arn,
            solution_stack_name=solution_stack_name,
            source_configuration=source_configuration,
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        jsii.set(self, "applicationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.EnvironmentId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-environmentid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentId"))

    @environment_id.setter
    def environment_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "environmentId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="optionSettings")
    def option_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationTemplate.ConfigurationOptionSettingProperty"]]]]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.OptionSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-optionsettings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationTemplate.ConfigurationOptionSettingProperty"]]]], jsii.get(self, "optionSettings"))

    @option_settings.setter
    def option_settings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationTemplate.ConfigurationOptionSettingProperty"]]]],
    ) -> None:
        jsii.set(self, "optionSettings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="platformArn")
    def platform_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.PlatformArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-platformarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformArn"))

    @platform_arn.setter
    def platform_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "platformArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="solutionStackName")
    def solution_stack_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.SolutionStackName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-solutionstackname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "solutionStackName"))

    @solution_stack_name.setter
    def solution_stack_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "solutionStackName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationTemplate.SourceConfigurationProperty"]]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.SourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationTemplate.SourceConfigurationProperty"]], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationTemplate.SourceConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "sourceConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnConfigurationTemplate.ConfigurationOptionSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "namespace": "namespace",
            "option_name": "optionName",
            "resource_name": "resourceName",
            "value": "value",
        },
    )
    class ConfigurationOptionSettingProperty:
        def __init__(
            self,
            *,
            namespace: builtins.str,
            option_name: builtins.str,
            resource_name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param namespace: ``CfnConfigurationTemplate.ConfigurationOptionSettingProperty.Namespace``.
            :param option_name: ``CfnConfigurationTemplate.ConfigurationOptionSettingProperty.OptionName``.
            :param resource_name: ``CfnConfigurationTemplate.ConfigurationOptionSettingProperty.ResourceName``.
            :param value: ``CfnConfigurationTemplate.ConfigurationOptionSettingProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "namespace": namespace,
                "option_name": option_name,
            }
            if resource_name is not None:
                self._values["resource_name"] = resource_name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def namespace(self) -> builtins.str:
            '''``CfnConfigurationTemplate.ConfigurationOptionSettingProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def option_name(self) -> builtins.str:
            '''``CfnConfigurationTemplate.ConfigurationOptionSettingProperty.OptionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-optionname
            '''
            result = self._values.get("option_name")
            assert result is not None, "Required property 'option_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_name(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationTemplate.ConfigurationOptionSettingProperty.ResourceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-resourcename
            '''
            result = self._values.get("resource_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationTemplate.ConfigurationOptionSettingProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html#cfn-elasticbeanstalk-configurationtemplate-configurationoptionsetting-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationOptionSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnConfigurationTemplate.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_name": "applicationName",
            "template_name": "templateName",
        },
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            application_name: builtins.str,
            template_name: builtins.str,
        ) -> None:
            '''
            :param application_name: ``CfnConfigurationTemplate.SourceConfigurationProperty.ApplicationName``.
            :param template_name: ``CfnConfigurationTemplate.SourceConfigurationProperty.TemplateName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "application_name": application_name,
                "template_name": template_name,
            }

        @builtins.property
        def application_name(self) -> builtins.str:
            '''``CfnConfigurationTemplate.SourceConfigurationProperty.ApplicationName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-applicationname
            '''
            result = self._values.get("application_name")
            assert result is not None, "Required property 'application_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def template_name(self) -> builtins.str:
            '''``CfnConfigurationTemplate.SourceConfigurationProperty.TemplateName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticbeanstalk-configurationtemplate-sourceconfiguration.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration-templatename
            '''
            result = self._values.get("template_name")
            assert result is not None, "Required property 'template_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnConfigurationTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "description": "description",
        "environment_id": "environmentId",
        "option_settings": "optionSettings",
        "platform_arn": "platformArn",
        "solution_stack_name": "solutionStackName",
        "source_configuration": "sourceConfiguration",
    },
)
class CfnConfigurationTemplateProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        environment_id: typing.Optional[builtins.str] = None,
        option_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationTemplate.ConfigurationOptionSettingProperty]]]] = None,
        platform_arn: typing.Optional[builtins.str] = None,
        solution_stack_name: typing.Optional[builtins.str] = None,
        source_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationTemplate.SourceConfigurationProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElasticBeanstalk::ConfigurationTemplate``.

        :param application_name: ``AWS::ElasticBeanstalk::ConfigurationTemplate.ApplicationName``.
        :param description: ``AWS::ElasticBeanstalk::ConfigurationTemplate.Description``.
        :param environment_id: ``AWS::ElasticBeanstalk::ConfigurationTemplate.EnvironmentId``.
        :param option_settings: ``AWS::ElasticBeanstalk::ConfigurationTemplate.OptionSettings``.
        :param platform_arn: ``AWS::ElasticBeanstalk::ConfigurationTemplate.PlatformArn``.
        :param solution_stack_name: ``AWS::ElasticBeanstalk::ConfigurationTemplate.SolutionStackName``.
        :param source_configuration: ``AWS::ElasticBeanstalk::ConfigurationTemplate.SourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_name": application_name,
        }
        if description is not None:
            self._values["description"] = description
        if environment_id is not None:
            self._values["environment_id"] = environment_id
        if option_settings is not None:
            self._values["option_settings"] = option_settings
        if platform_arn is not None:
            self._values["platform_arn"] = platform_arn
        if solution_stack_name is not None:
            self._values["solution_stack_name"] = solution_stack_name
        if source_configuration is not None:
            self._values["source_configuration"] = source_configuration

    @builtins.property
    def application_name(self) -> builtins.str:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.EnvironmentId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-environmentid
        '''
        result = self._values.get("environment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def option_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationTemplate.ConfigurationOptionSettingProperty]]]]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.OptionSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-optionsettings
        '''
        result = self._values.get("option_settings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationTemplate.ConfigurationOptionSettingProperty]]]], result)

    @builtins.property
    def platform_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.PlatformArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-platformarn
        '''
        result = self._values.get("platform_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def solution_stack_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.SolutionStackName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-solutionstackname
        '''
        result = self._values.get("solution_stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationTemplate.SourceConfigurationProperty]]:
        '''``AWS::ElasticBeanstalk::ConfigurationTemplate.SourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html#cfn-elasticbeanstalk-configurationtemplate-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnConfigurationTemplate.SourceConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEnvironment(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnEnvironment",
):
    '''A CloudFormation ``AWS::ElasticBeanstalk::Environment``.

    :cloudformationResource: AWS::ElasticBeanstalk::Environment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        cname_prefix: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        operations_role: typing.Optional[builtins.str] = None,
        option_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.OptionSettingProperty"]]]] = None,
        platform_arn: typing.Optional[builtins.str] = None,
        solution_stack_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        template_name: typing.Optional[builtins.str] = None,
        tier: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.TierProperty"]] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ElasticBeanstalk::Environment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: ``AWS::ElasticBeanstalk::Environment.ApplicationName``.
        :param cname_prefix: ``AWS::ElasticBeanstalk::Environment.CNAMEPrefix``.
        :param description: ``AWS::ElasticBeanstalk::Environment.Description``.
        :param environment_name: ``AWS::ElasticBeanstalk::Environment.EnvironmentName``.
        :param operations_role: ``AWS::ElasticBeanstalk::Environment.OperationsRole``.
        :param option_settings: ``AWS::ElasticBeanstalk::Environment.OptionSettings``.
        :param platform_arn: ``AWS::ElasticBeanstalk::Environment.PlatformArn``.
        :param solution_stack_name: ``AWS::ElasticBeanstalk::Environment.SolutionStackName``.
        :param tags: ``AWS::ElasticBeanstalk::Environment.Tags``.
        :param template_name: ``AWS::ElasticBeanstalk::Environment.TemplateName``.
        :param tier: ``AWS::ElasticBeanstalk::Environment.Tier``.
        :param version_label: ``AWS::ElasticBeanstalk::Environment.VersionLabel``.
        '''
        props = CfnEnvironmentProps(
            application_name=application_name,
            cname_prefix=cname_prefix,
            description=description,
            environment_name=environment_name,
            operations_role=operations_role,
            option_settings=option_settings,
            platform_arn=platform_arn,
            solution_stack_name=solution_stack_name,
            tags=tags,
            template_name=template_name,
            tier=tier,
            version_label=version_label,
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
    @jsii.member(jsii_name="attrEndpointUrl")
    def attr_endpoint_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: EndpointURL
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ElasticBeanstalk::Environment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-elasticbeanstalk-environment-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''``AWS::ElasticBeanstalk::Environment.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        jsii.set(self, "applicationName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cnamePrefix")
    def cname_prefix(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.CNAMEPrefix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-cnameprefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnamePrefix"))

    @cname_prefix.setter
    def cname_prefix(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cnamePrefix", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.EnvironmentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentName"))

    @environment_name.setter
    def environment_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "environmentName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="operationsRole")
    def operations_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.OperationsRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-operations-role
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationsRole"))

    @operations_role.setter
    def operations_role(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "operationsRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="optionSettings")
    def option_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.OptionSettingProperty"]]]]:
        '''``AWS::ElasticBeanstalk::Environment.OptionSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-optionsettings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.OptionSettingProperty"]]]], jsii.get(self, "optionSettings"))

    @option_settings.setter
    def option_settings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.OptionSettingProperty"]]]],
    ) -> None:
        jsii.set(self, "optionSettings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="platformArn")
    def platform_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.PlatformArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-platformarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformArn"))

    @platform_arn.setter
    def platform_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "platformArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="solutionStackName")
    def solution_stack_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.SolutionStackName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-solutionstackname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "solutionStackName"))

    @solution_stack_name.setter
    def solution_stack_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "solutionStackName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.TemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-templatename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tier")
    def tier(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.TierProperty"]]:
        '''``AWS::ElasticBeanstalk::Environment.Tier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-tier
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.TierProperty"]], jsii.get(self, "tier"))

    @tier.setter
    def tier(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEnvironment.TierProperty"]],
    ) -> None:
        jsii.set(self, "tier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionLabel")
    def version_label(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.VersionLabel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-versionlabel
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionLabel"))

    @version_label.setter
    def version_label(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionLabel", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnEnvironment.OptionSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "namespace": "namespace",
            "option_name": "optionName",
            "resource_name": "resourceName",
            "value": "value",
        },
    )
    class OptionSettingProperty:
        def __init__(
            self,
            *,
            namespace: builtins.str,
            option_name: builtins.str,
            resource_name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param namespace: ``CfnEnvironment.OptionSettingProperty.Namespace``.
            :param option_name: ``CfnEnvironment.OptionSettingProperty.OptionName``.
            :param resource_name: ``CfnEnvironment.OptionSettingProperty.ResourceName``.
            :param value: ``CfnEnvironment.OptionSettingProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "namespace": namespace,
                "option_name": option_name,
            }
            if resource_name is not None:
                self._values["resource_name"] = resource_name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def namespace(self) -> builtins.str:
            '''``CfnEnvironment.OptionSettingProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def option_name(self) -> builtins.str:
            '''``CfnEnvironment.OptionSettingProperty.OptionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-optionname
            '''
            result = self._values.get("option_name")
            assert result is not None, "Required property 'option_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_name(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.OptionSettingProperty.ResourceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-elasticbeanstalk-environment-optionsetting-resourcename
            '''
            result = self._values.get("resource_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.OptionSettingProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-option-settings.html#cfn-beanstalk-optionsettings-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OptionSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnEnvironment.TierProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type", "version": "version"},
    )
    class TierProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnEnvironment.TierProperty.Name``.
            :param type: ``CfnEnvironment.TierProperty.Type``.
            :param version: ``CfnEnvironment.TierProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if type is not None:
                self._values["type"] = type
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.TierProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.TierProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''``CfnEnvironment.TierProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment-tier.html#cfn-beanstalk-env-tier-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticbeanstalk.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "cname_prefix": "cnamePrefix",
        "description": "description",
        "environment_name": "environmentName",
        "operations_role": "operationsRole",
        "option_settings": "optionSettings",
        "platform_arn": "platformArn",
        "solution_stack_name": "solutionStackName",
        "tags": "tags",
        "template_name": "templateName",
        "tier": "tier",
        "version_label": "versionLabel",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        cname_prefix: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        operations_role: typing.Optional[builtins.str] = None,
        option_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.OptionSettingProperty]]]] = None,
        platform_arn: typing.Optional[builtins.str] = None,
        solution_stack_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        template_name: typing.Optional[builtins.str] = None,
        tier: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.TierProperty]] = None,
        version_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElasticBeanstalk::Environment``.

        :param application_name: ``AWS::ElasticBeanstalk::Environment.ApplicationName``.
        :param cname_prefix: ``AWS::ElasticBeanstalk::Environment.CNAMEPrefix``.
        :param description: ``AWS::ElasticBeanstalk::Environment.Description``.
        :param environment_name: ``AWS::ElasticBeanstalk::Environment.EnvironmentName``.
        :param operations_role: ``AWS::ElasticBeanstalk::Environment.OperationsRole``.
        :param option_settings: ``AWS::ElasticBeanstalk::Environment.OptionSettings``.
        :param platform_arn: ``AWS::ElasticBeanstalk::Environment.PlatformArn``.
        :param solution_stack_name: ``AWS::ElasticBeanstalk::Environment.SolutionStackName``.
        :param tags: ``AWS::ElasticBeanstalk::Environment.Tags``.
        :param template_name: ``AWS::ElasticBeanstalk::Environment.TemplateName``.
        :param tier: ``AWS::ElasticBeanstalk::Environment.Tier``.
        :param version_label: ``AWS::ElasticBeanstalk::Environment.VersionLabel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_name": application_name,
        }
        if cname_prefix is not None:
            self._values["cname_prefix"] = cname_prefix
        if description is not None:
            self._values["description"] = description
        if environment_name is not None:
            self._values["environment_name"] = environment_name
        if operations_role is not None:
            self._values["operations_role"] = operations_role
        if option_settings is not None:
            self._values["option_settings"] = option_settings
        if platform_arn is not None:
            self._values["platform_arn"] = platform_arn
        if solution_stack_name is not None:
            self._values["solution_stack_name"] = solution_stack_name
        if tags is not None:
            self._values["tags"] = tags
        if template_name is not None:
            self._values["template_name"] = template_name
        if tier is not None:
            self._values["tier"] = tier
        if version_label is not None:
            self._values["version_label"] = version_label

    @builtins.property
    def application_name(self) -> builtins.str:
        '''``AWS::ElasticBeanstalk::Environment.ApplicationName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cname_prefix(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.CNAMEPrefix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-cnameprefix
        '''
        result = self._values.get("cname_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.EnvironmentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-name
        '''
        result = self._values.get("environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operations_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.OperationsRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-operations-role
        '''
        result = self._values.get("operations_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def option_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.OptionSettingProperty]]]]:
        '''``AWS::ElasticBeanstalk::Environment.OptionSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-optionsettings
        '''
        result = self._values.get("option_settings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.OptionSettingProperty]]]], result)

    @builtins.property
    def platform_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.PlatformArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-platformarn
        '''
        result = self._values.get("platform_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def solution_stack_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.SolutionStackName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-solutionstackname
        '''
        result = self._values.get("solution_stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ElasticBeanstalk::Environment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-elasticbeanstalk-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def template_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.TemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-templatename
        '''
        result = self._values.get("template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tier(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.TierProperty]]:
        '''``AWS::ElasticBeanstalk::Environment.Tier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-tier
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEnvironment.TierProperty]], result)

    @builtins.property
    def version_label(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElasticBeanstalk::Environment.VersionLabel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-versionlabel
        '''
        result = self._values.get("version_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnApplicationVersion",
    "CfnApplicationVersionProps",
    "CfnConfigurationTemplate",
    "CfnConfigurationTemplateProps",
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()
