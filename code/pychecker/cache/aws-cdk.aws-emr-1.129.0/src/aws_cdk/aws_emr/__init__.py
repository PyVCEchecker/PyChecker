'''
# Amazon EMR Construct Library

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
class CfnCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-emr.CfnCluster",
):
    '''A CloudFormation ``AWS::EMR::Cluster``.

    :cloudformationResource: AWS::EMR::Cluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instances: typing.Union["CfnCluster.JobFlowInstancesConfigProperty", aws_cdk.core.IResolvable],
        job_flow_role: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        additional_info: typing.Any = None,
        applications: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ApplicationProperty"]]]] = None,
        auto_scaling_role: typing.Optional[builtins.str] = None,
        bootstrap_actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.BootstrapActionConfigProperty"]]]] = None,
        configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        kerberos_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KerberosAttributesProperty"]] = None,
        log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        managed_scaling_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ManagedScalingPolicyProperty"]] = None,
        release_label: typing.Optional[builtins.str] = None,
        scale_down_behavior: typing.Optional[builtins.str] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        step_concurrency_level: typing.Optional[jsii.Number] = None,
        steps: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.StepConfigProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Create a new ``AWS::EMR::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instances: ``AWS::EMR::Cluster.Instances``.
        :param job_flow_role: ``AWS::EMR::Cluster.JobFlowRole``.
        :param name: ``AWS::EMR::Cluster.Name``.
        :param service_role: ``AWS::EMR::Cluster.ServiceRole``.
        :param additional_info: ``AWS::EMR::Cluster.AdditionalInfo``.
        :param applications: ``AWS::EMR::Cluster.Applications``.
        :param auto_scaling_role: ``AWS::EMR::Cluster.AutoScalingRole``.
        :param bootstrap_actions: ``AWS::EMR::Cluster.BootstrapActions``.
        :param configurations: ``AWS::EMR::Cluster.Configurations``.
        :param custom_ami_id: ``AWS::EMR::Cluster.CustomAmiId``.
        :param ebs_root_volume_size: ``AWS::EMR::Cluster.EbsRootVolumeSize``.
        :param kerberos_attributes: ``AWS::EMR::Cluster.KerberosAttributes``.
        :param log_encryption_kms_key_id: ``AWS::EMR::Cluster.LogEncryptionKmsKeyId``.
        :param log_uri: ``AWS::EMR::Cluster.LogUri``.
        :param managed_scaling_policy: ``AWS::EMR::Cluster.ManagedScalingPolicy``.
        :param release_label: ``AWS::EMR::Cluster.ReleaseLabel``.
        :param scale_down_behavior: ``AWS::EMR::Cluster.ScaleDownBehavior``.
        :param security_configuration: ``AWS::EMR::Cluster.SecurityConfiguration``.
        :param step_concurrency_level: ``AWS::EMR::Cluster.StepConcurrencyLevel``.
        :param steps: ``AWS::EMR::Cluster.Steps``.
        :param tags: ``AWS::EMR::Cluster.Tags``.
        :param visible_to_all_users: ``AWS::EMR::Cluster.VisibleToAllUsers``.
        '''
        props = CfnClusterProps(
            instances=instances,
            job_flow_role=job_flow_role,
            name=name,
            service_role=service_role,
            additional_info=additional_info,
            applications=applications,
            auto_scaling_role=auto_scaling_role,
            bootstrap_actions=bootstrap_actions,
            configurations=configurations,
            custom_ami_id=custom_ami_id,
            ebs_root_volume_size=ebs_root_volume_size,
            kerberos_attributes=kerberos_attributes,
            log_encryption_kms_key_id=log_encryption_kms_key_id,
            log_uri=log_uri,
            managed_scaling_policy=managed_scaling_policy,
            release_label=release_label,
            scale_down_behavior=scale_down_behavior,
            security_configuration=security_configuration,
            step_concurrency_level=step_concurrency_level,
            steps=steps,
            tags=tags,
            visible_to_all_users=visible_to_all_users,
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
    @jsii.member(jsii_name="attrMasterPublicDns")
    def attr_master_public_dns(self) -> builtins.str:
        '''
        :cloudformationAttribute: MasterPublicDNS
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMasterPublicDns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::EMR::Cluster.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="additionalInfo")
    def additional_info(self) -> typing.Any:
        '''``AWS::EMR::Cluster.AdditionalInfo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-additionalinfo
        '''
        return typing.cast(typing.Any, jsii.get(self, "additionalInfo"))

    @additional_info.setter
    def additional_info(self, value: typing.Any) -> None:
        jsii.set(self, "additionalInfo", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instances")
    def instances(
        self,
    ) -> typing.Union["CfnCluster.JobFlowInstancesConfigProperty", aws_cdk.core.IResolvable]:
        '''``AWS::EMR::Cluster.Instances``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-instances
        '''
        return typing.cast(typing.Union["CfnCluster.JobFlowInstancesConfigProperty", aws_cdk.core.IResolvable], jsii.get(self, "instances"))

    @instances.setter
    def instances(
        self,
        value: typing.Union["CfnCluster.JobFlowInstancesConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "instances", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobFlowRole")
    def job_flow_role(self) -> builtins.str:
        '''``AWS::EMR::Cluster.JobFlowRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-jobflowrole
        '''
        return typing.cast(builtins.str, jsii.get(self, "jobFlowRole"))

    @job_flow_role.setter
    def job_flow_role(self, value: builtins.str) -> None:
        jsii.set(self, "jobFlowRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::EMR::Cluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        '''``AWS::EMR::Cluster.ServiceRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-servicerole
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        jsii.set(self, "serviceRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applications")
    def applications(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ApplicationProperty"]]]]:
        '''``AWS::EMR::Cluster.Applications``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-applications
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ApplicationProperty"]]]], jsii.get(self, "applications"))

    @applications.setter
    def applications(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ApplicationProperty"]]]],
    ) -> None:
        jsii.set(self, "applications", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingRole")
    def auto_scaling_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.AutoScalingRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-autoscalingrole
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingRole"))

    @auto_scaling_role.setter
    def auto_scaling_role(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "autoScalingRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bootstrapActions")
    def bootstrap_actions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.BootstrapActionConfigProperty"]]]]:
        '''``AWS::EMR::Cluster.BootstrapActions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-bootstrapactions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.BootstrapActionConfigProperty"]]]], jsii.get(self, "bootstrapActions"))

    @bootstrap_actions.setter
    def bootstrap_actions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.BootstrapActionConfigProperty"]]]],
    ) -> None:
        jsii.set(self, "bootstrapActions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurations")
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]]:
        '''``AWS::EMR::Cluster.Configurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-configurations
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]], jsii.get(self, "configurations"))

    @configurations.setter
    def configurations(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]],
    ) -> None:
        jsii.set(self, "configurations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customAmiId")
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.CustomAmiId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-customamiid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customAmiId"))

    @custom_ami_id.setter
    def custom_ami_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "customAmiId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsRootVolumeSize")
    def ebs_root_volume_size(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EMR::Cluster.EbsRootVolumeSize``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-ebsrootvolumesize
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ebsRootVolumeSize"))

    @ebs_root_volume_size.setter
    def ebs_root_volume_size(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "ebsRootVolumeSize", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kerberosAttributes")
    def kerberos_attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KerberosAttributesProperty"]]:
        '''``AWS::EMR::Cluster.KerberosAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-kerberosattributes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KerberosAttributesProperty"]], jsii.get(self, "kerberosAttributes"))

    @kerberos_attributes.setter
    def kerberos_attributes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KerberosAttributesProperty"]],
    ) -> None:
        jsii.set(self, "kerberosAttributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logEncryptionKmsKeyId")
    def log_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.LogEncryptionKmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-logencryptionkmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logEncryptionKmsKeyId"))

    @log_encryption_kms_key_id.setter
    def log_encryption_kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logEncryptionKmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logUri")
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.LogUri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-loguri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logUri"))

    @log_uri.setter
    def log_uri(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logUri", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="managedScalingPolicy")
    def managed_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ManagedScalingPolicyProperty"]]:
        '''``AWS::EMR::Cluster.ManagedScalingPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-managedscalingpolicy
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ManagedScalingPolicyProperty"]], jsii.get(self, "managedScalingPolicy"))

    @managed_scaling_policy.setter
    def managed_scaling_policy(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ManagedScalingPolicyProperty"]],
    ) -> None:
        jsii.set(self, "managedScalingPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.ReleaseLabel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-releaselabel
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "releaseLabel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scaleDownBehavior")
    def scale_down_behavior(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.ScaleDownBehavior``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-scaledownbehavior
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleDownBehavior"))

    @scale_down_behavior.setter
    def scale_down_behavior(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "scaleDownBehavior", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.SecurityConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-securityconfiguration
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "securityConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stepConcurrencyLevel")
    def step_concurrency_level(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EMR::Cluster.StepConcurrencyLevel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-stepconcurrencylevel
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stepConcurrencyLevel"))

    @step_concurrency_level.setter
    def step_concurrency_level(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "stepConcurrencyLevel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="steps")
    def steps(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.StepConfigProperty"]]]]:
        '''``AWS::EMR::Cluster.Steps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-steps
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.StepConfigProperty"]]]], jsii.get(self, "steps"))

    @steps.setter
    def steps(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.StepConfigProperty"]]]],
    ) -> None:
        jsii.set(self, "steps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="visibleToAllUsers")
    def visible_to_all_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::EMR::Cluster.VisibleToAllUsers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-visibletoallusers
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "visibleToAllUsers"))

    @visible_to_all_users.setter
    def visible_to_all_users(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "visibleToAllUsers", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ApplicationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_info": "additionalInfo",
            "args": "args",
            "name": "name",
            "version": "version",
        },
    )
    class ApplicationProperty:
        def __init__(
            self,
            *,
            additional_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
            name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param additional_info: ``CfnCluster.ApplicationProperty.AdditionalInfo``.
            :param args: ``CfnCluster.ApplicationProperty.Args``.
            :param name: ``CfnCluster.ApplicationProperty.Name``.
            :param version: ``CfnCluster.ApplicationProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if additional_info is not None:
                self._values["additional_info"] = additional_info
            if args is not None:
                self._values["args"] = args
            if name is not None:
                self._values["name"] = name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def additional_info(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnCluster.ApplicationProperty.AdditionalInfo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html#cfn-elasticmapreduce-cluster-application-additionalinfo
            '''
            result = self._values.get("additional_info")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCluster.ApplicationProperty.Args``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html#cfn-elasticmapreduce-cluster-application-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.ApplicationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html#cfn-elasticmapreduce-cluster-application-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.ApplicationProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-application.html#cfn-elasticmapreduce-cluster-application-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.AutoScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"constraints": "constraints", "rules": "rules"},
    )
    class AutoScalingPolicyProperty:
        def __init__(
            self,
            *,
            constraints: typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingConstraintsProperty"],
            rules: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingRuleProperty"]]],
        ) -> None:
            '''
            :param constraints: ``CfnCluster.AutoScalingPolicyProperty.Constraints``.
            :param rules: ``CfnCluster.AutoScalingPolicyProperty.Rules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoscalingpolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "constraints": constraints,
                "rules": rules,
            }

        @builtins.property
        def constraints(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingConstraintsProperty"]:
            '''``CfnCluster.AutoScalingPolicyProperty.Constraints``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoscalingpolicy.html#cfn-elasticmapreduce-cluster-autoscalingpolicy-constraints
            '''
            result = self._values.get("constraints")
            assert result is not None, "Required property 'constraints' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingConstraintsProperty"], result)

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingRuleProperty"]]]:
            '''``CfnCluster.AutoScalingPolicyProperty.Rules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-autoscalingpolicy.html#cfn-elasticmapreduce-cluster-autoscalingpolicy-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingRuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.BootstrapActionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "script_bootstrap_action": "scriptBootstrapAction",
        },
    )
    class BootstrapActionConfigProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            script_bootstrap_action: typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScriptBootstrapActionConfigProperty"],
        ) -> None:
            '''
            :param name: ``CfnCluster.BootstrapActionConfigProperty.Name``.
            :param script_bootstrap_action: ``CfnCluster.BootstrapActionConfigProperty.ScriptBootstrapAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "script_bootstrap_action": script_bootstrap_action,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnCluster.BootstrapActionConfigProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html#cfn-elasticmapreduce-cluster-bootstrapactionconfig-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def script_bootstrap_action(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScriptBootstrapActionConfigProperty"]:
            '''``CfnCluster.BootstrapActionConfigProperty.ScriptBootstrapAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-bootstrapactionconfig.html#cfn-elasticmapreduce-cluster-bootstrapactionconfig-scriptbootstrapaction
            '''
            result = self._values.get("script_bootstrap_action")
            assert result is not None, "Required property 'script_bootstrap_action' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScriptBootstrapActionConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BootstrapActionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.CloudWatchAlarmDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "metric_name": "metricName",
            "period": "period",
            "threshold": "threshold",
            "dimensions": "dimensions",
            "evaluation_periods": "evaluationPeriods",
            "namespace": "namespace",
            "statistic": "statistic",
            "unit": "unit",
        },
    )
    class CloudWatchAlarmDefinitionProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            metric_name: builtins.str,
            period: jsii.Number,
            threshold: jsii.Number,
            dimensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.MetricDimensionProperty"]]]] = None,
            evaluation_periods: typing.Optional[jsii.Number] = None,
            namespace: typing.Optional[builtins.str] = None,
            statistic: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param comparison_operator: ``CfnCluster.CloudWatchAlarmDefinitionProperty.ComparisonOperator``.
            :param metric_name: ``CfnCluster.CloudWatchAlarmDefinitionProperty.MetricName``.
            :param period: ``CfnCluster.CloudWatchAlarmDefinitionProperty.Period``.
            :param threshold: ``CfnCluster.CloudWatchAlarmDefinitionProperty.Threshold``.
            :param dimensions: ``CfnCluster.CloudWatchAlarmDefinitionProperty.Dimensions``.
            :param evaluation_periods: ``CfnCluster.CloudWatchAlarmDefinitionProperty.EvaluationPeriods``.
            :param namespace: ``CfnCluster.CloudWatchAlarmDefinitionProperty.Namespace``.
            :param statistic: ``CfnCluster.CloudWatchAlarmDefinitionProperty.Statistic``.
            :param unit: ``CfnCluster.CloudWatchAlarmDefinitionProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "metric_name": metric_name,
                "period": period,
                "threshold": threshold,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if evaluation_periods is not None:
                self._values["evaluation_periods"] = evaluation_periods
            if namespace is not None:
                self._values["namespace"] = namespace
            if statistic is not None:
                self._values["statistic"] = statistic
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.ComparisonOperator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.MetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.Period``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.Threshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.MetricDimensionProperty"]]]]:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.MetricDimensionProperty"]]]], result)

        @builtins.property
        def evaluation_periods(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.EvaluationPeriods``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-evaluationperiods
            '''
            result = self._values.get("evaluation_periods")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def statistic(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.Statistic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-statistic
            '''
            result = self._values.get("statistic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.CloudWatchAlarmDefinitionProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-cluster-cloudwatchalarmdefinition-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchAlarmDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ComputeLimitsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maximum_capacity_units": "maximumCapacityUnits",
            "minimum_capacity_units": "minimumCapacityUnits",
            "unit_type": "unitType",
            "maximum_core_capacity_units": "maximumCoreCapacityUnits",
            "maximum_on_demand_capacity_units": "maximumOnDemandCapacityUnits",
        },
    )
    class ComputeLimitsProperty:
        def __init__(
            self,
            *,
            maximum_capacity_units: jsii.Number,
            minimum_capacity_units: jsii.Number,
            unit_type: builtins.str,
            maximum_core_capacity_units: typing.Optional[jsii.Number] = None,
            maximum_on_demand_capacity_units: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param maximum_capacity_units: ``CfnCluster.ComputeLimitsProperty.MaximumCapacityUnits``.
            :param minimum_capacity_units: ``CfnCluster.ComputeLimitsProperty.MinimumCapacityUnits``.
            :param unit_type: ``CfnCluster.ComputeLimitsProperty.UnitType``.
            :param maximum_core_capacity_units: ``CfnCluster.ComputeLimitsProperty.MaximumCoreCapacityUnits``.
            :param maximum_on_demand_capacity_units: ``CfnCluster.ComputeLimitsProperty.MaximumOnDemandCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "maximum_capacity_units": maximum_capacity_units,
                "minimum_capacity_units": minimum_capacity_units,
                "unit_type": unit_type,
            }
            if maximum_core_capacity_units is not None:
                self._values["maximum_core_capacity_units"] = maximum_core_capacity_units
            if maximum_on_demand_capacity_units is not None:
                self._values["maximum_on_demand_capacity_units"] = maximum_on_demand_capacity_units

        @builtins.property
        def maximum_capacity_units(self) -> jsii.Number:
            '''``CfnCluster.ComputeLimitsProperty.MaximumCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-maximumcapacityunits
            '''
            result = self._values.get("maximum_capacity_units")
            assert result is not None, "Required property 'maximum_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def minimum_capacity_units(self) -> jsii.Number:
            '''``CfnCluster.ComputeLimitsProperty.MinimumCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-minimumcapacityunits
            '''
            result = self._values.get("minimum_capacity_units")
            assert result is not None, "Required property 'minimum_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unit_type(self) -> builtins.str:
            '''``CfnCluster.ComputeLimitsProperty.UnitType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-unittype
            '''
            result = self._values.get("unit_type")
            assert result is not None, "Required property 'unit_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maximum_core_capacity_units(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.ComputeLimitsProperty.MaximumCoreCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-maximumcorecapacityunits
            '''
            result = self._values.get("maximum_core_capacity_units")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_on_demand_capacity_units(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.ComputeLimitsProperty.MaximumOnDemandCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-computelimits.html#cfn-elasticmapreduce-cluster-computelimits-maximumondemandcapacityunits
            '''
            result = self._values.get("maximum_on_demand_capacity_units")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeLimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configuration_properties": "configurationProperties",
            "configurations": "configurations",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            classification: typing.Optional[builtins.str] = None,
            configuration_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]] = None,
        ) -> None:
            '''
            :param classification: ``CfnCluster.ConfigurationProperty.Classification``.
            :param configuration_properties: ``CfnCluster.ConfigurationProperty.ConfigurationProperties``.
            :param configurations: ``CfnCluster.ConfigurationProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-configuration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if classification is not None:
                self._values["classification"] = classification
            if configuration_properties is not None:
                self._values["configuration_properties"] = configuration_properties
            if configurations is not None:
                self._values["configurations"] = configurations

        @builtins.property
        def classification(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.ConfigurationProperty.Classification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-configuration.html#cfn-elasticmapreduce-cluster-configuration-classification
            '''
            result = self._values.get("classification")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configuration_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnCluster.ConfigurationProperty.ConfigurationProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-configuration.html#cfn-elasticmapreduce-cluster-configuration-configurationproperties
            '''
            result = self._values.get("configuration_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]]:
            '''``CfnCluster.ConfigurationProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-configuration.html#cfn-elasticmapreduce-cluster-configuration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.EbsBlockDeviceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "volume_specification": "volumeSpecification",
            "volumes_per_instance": "volumesPerInstance",
        },
    )
    class EbsBlockDeviceConfigProperty:
        def __init__(
            self,
            *,
            volume_specification: typing.Union[aws_cdk.core.IResolvable, "CfnCluster.VolumeSpecificationProperty"],
            volumes_per_instance: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param volume_specification: ``CfnCluster.EbsBlockDeviceConfigProperty.VolumeSpecification``.
            :param volumes_per_instance: ``CfnCluster.EbsBlockDeviceConfigProperty.VolumesPerInstance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsblockdeviceconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "volume_specification": volume_specification,
            }
            if volumes_per_instance is not None:
                self._values["volumes_per_instance"] = volumes_per_instance

        @builtins.property
        def volume_specification(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.VolumeSpecificationProperty"]:
            '''``CfnCluster.EbsBlockDeviceConfigProperty.VolumeSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsblockdeviceconfig.html#cfn-elasticmapreduce-cluster-ebsblockdeviceconfig-volumespecification
            '''
            result = self._values.get("volume_specification")
            assert result is not None, "Required property 'volume_specification' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.VolumeSpecificationProperty"], result)

        @builtins.property
        def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.EbsBlockDeviceConfigProperty.VolumesPerInstance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsblockdeviceconfig.html#cfn-elasticmapreduce-cluster-ebsblockdeviceconfig-volumesperinstance
            '''
            result = self._values.get("volumes_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.EbsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_block_device_configs": "ebsBlockDeviceConfigs",
            "ebs_optimized": "ebsOptimized",
        },
    )
    class EbsConfigurationProperty:
        def __init__(
            self,
            *,
            ebs_block_device_configs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsBlockDeviceConfigProperty"]]]] = None,
            ebs_optimized: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param ebs_block_device_configs: ``CfnCluster.EbsConfigurationProperty.EbsBlockDeviceConfigs``.
            :param ebs_optimized: ``CfnCluster.EbsConfigurationProperty.EbsOptimized``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ebs_block_device_configs is not None:
                self._values["ebs_block_device_configs"] = ebs_block_device_configs
            if ebs_optimized is not None:
                self._values["ebs_optimized"] = ebs_optimized

        @builtins.property
        def ebs_block_device_configs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsBlockDeviceConfigProperty"]]]]:
            '''``CfnCluster.EbsConfigurationProperty.EbsBlockDeviceConfigs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsconfiguration.html#cfn-elasticmapreduce-cluster-ebsconfiguration-ebsblockdeviceconfigs
            '''
            result = self._values.get("ebs_block_device_configs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsBlockDeviceConfigProperty"]]]], result)

        @builtins.property
        def ebs_optimized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCluster.EbsConfigurationProperty.EbsOptimized``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ebsconfiguration.html#cfn-elasticmapreduce-cluster-ebsconfiguration-ebsoptimized
            '''
            result = self._values.get("ebs_optimized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.HadoopJarStepConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "jar": "jar",
            "args": "args",
            "main_class": "mainClass",
            "step_properties": "stepProperties",
        },
    )
    class HadoopJarStepConfigProperty:
        def __init__(
            self,
            *,
            jar: builtins.str,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
            main_class: typing.Optional[builtins.str] = None,
            step_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KeyValueProperty"]]]] = None,
        ) -> None:
            '''
            :param jar: ``CfnCluster.HadoopJarStepConfigProperty.Jar``.
            :param args: ``CfnCluster.HadoopJarStepConfigProperty.Args``.
            :param main_class: ``CfnCluster.HadoopJarStepConfigProperty.MainClass``.
            :param step_properties: ``CfnCluster.HadoopJarStepConfigProperty.StepProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "jar": jar,
            }
            if args is not None:
                self._values["args"] = args
            if main_class is not None:
                self._values["main_class"] = main_class
            if step_properties is not None:
                self._values["step_properties"] = step_properties

        @builtins.property
        def jar(self) -> builtins.str:
            '''``CfnCluster.HadoopJarStepConfigProperty.Jar``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html#cfn-elasticmapreduce-cluster-hadoopjarstepconfig-jar
            '''
            result = self._values.get("jar")
            assert result is not None, "Required property 'jar' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCluster.HadoopJarStepConfigProperty.Args``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html#cfn-elasticmapreduce-cluster-hadoopjarstepconfig-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def main_class(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.HadoopJarStepConfigProperty.MainClass``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html#cfn-elasticmapreduce-cluster-hadoopjarstepconfig-mainclass
            '''
            result = self._values.get("main_class")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def step_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KeyValueProperty"]]]]:
            '''``CfnCluster.HadoopJarStepConfigProperty.StepProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-hadoopjarstepconfig.html#cfn-elasticmapreduce-cluster-hadoopjarstepconfig-stepproperties
            '''
            result = self._values.get("step_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KeyValueProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HadoopJarStepConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.InstanceFleetConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type_configs": "instanceTypeConfigs",
            "launch_specifications": "launchSpecifications",
            "name": "name",
            "target_on_demand_capacity": "targetOnDemandCapacity",
            "target_spot_capacity": "targetSpotCapacity",
        },
    )
    class InstanceFleetConfigProperty:
        def __init__(
            self,
            *,
            instance_type_configs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceTypeConfigProperty"]]]] = None,
            launch_specifications: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetProvisioningSpecificationsProperty"]] = None,
            name: typing.Optional[builtins.str] = None,
            target_on_demand_capacity: typing.Optional[jsii.Number] = None,
            target_spot_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param instance_type_configs: ``CfnCluster.InstanceFleetConfigProperty.InstanceTypeConfigs``.
            :param launch_specifications: ``CfnCluster.InstanceFleetConfigProperty.LaunchSpecifications``.
            :param name: ``CfnCluster.InstanceFleetConfigProperty.Name``.
            :param target_on_demand_capacity: ``CfnCluster.InstanceFleetConfigProperty.TargetOnDemandCapacity``.
            :param target_spot_capacity: ``CfnCluster.InstanceFleetConfigProperty.TargetSpotCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if instance_type_configs is not None:
                self._values["instance_type_configs"] = instance_type_configs
            if launch_specifications is not None:
                self._values["launch_specifications"] = launch_specifications
            if name is not None:
                self._values["name"] = name
            if target_on_demand_capacity is not None:
                self._values["target_on_demand_capacity"] = target_on_demand_capacity
            if target_spot_capacity is not None:
                self._values["target_spot_capacity"] = target_spot_capacity

        @builtins.property
        def instance_type_configs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceTypeConfigProperty"]]]]:
            '''``CfnCluster.InstanceFleetConfigProperty.InstanceTypeConfigs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-instancetypeconfigs
            '''
            result = self._values.get("instance_type_configs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceTypeConfigProperty"]]]], result)

        @builtins.property
        def launch_specifications(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetProvisioningSpecificationsProperty"]]:
            '''``CfnCluster.InstanceFleetConfigProperty.LaunchSpecifications``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-launchspecifications
            '''
            result = self._values.get("launch_specifications")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetProvisioningSpecificationsProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.InstanceFleetConfigProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.InstanceFleetConfigProperty.TargetOnDemandCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-targetondemandcapacity
            '''
            result = self._values.get("target_on_demand_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.InstanceFleetConfigProperty.TargetSpotCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetconfig.html#cfn-elasticmapreduce-cluster-instancefleetconfig-targetspotcapacity
            '''
            result = self._values.get("target_spot_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceFleetConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.InstanceFleetProvisioningSpecificationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "on_demand_specification": "onDemandSpecification",
            "spot_specification": "spotSpecification",
        },
    )
    class InstanceFleetProvisioningSpecificationsProperty:
        def __init__(
            self,
            *,
            on_demand_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.OnDemandProvisioningSpecificationProperty"]] = None,
            spot_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.SpotProvisioningSpecificationProperty"]] = None,
        ) -> None:
            '''
            :param on_demand_specification: ``CfnCluster.InstanceFleetProvisioningSpecificationsProperty.OnDemandSpecification``.
            :param spot_specification: ``CfnCluster.InstanceFleetProvisioningSpecificationsProperty.SpotSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetprovisioningspecifications.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if on_demand_specification is not None:
                self._values["on_demand_specification"] = on_demand_specification
            if spot_specification is not None:
                self._values["spot_specification"] = spot_specification

        @builtins.property
        def on_demand_specification(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.OnDemandProvisioningSpecificationProperty"]]:
            '''``CfnCluster.InstanceFleetProvisioningSpecificationsProperty.OnDemandSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetprovisioningspecifications.html#cfn-elasticmapreduce-cluster-instancefleetprovisioningspecifications-ondemandspecification
            '''
            result = self._values.get("on_demand_specification")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.OnDemandProvisioningSpecificationProperty"]], result)

        @builtins.property
        def spot_specification(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.SpotProvisioningSpecificationProperty"]]:
            '''``CfnCluster.InstanceFleetProvisioningSpecificationsProperty.SpotSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancefleetprovisioningspecifications.html#cfn-elasticmapreduce-cluster-instancefleetprovisioningspecifications-spotspecification
            '''
            result = self._values.get("spot_specification")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.SpotProvisioningSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceFleetProvisioningSpecificationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.InstanceGroupConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "auto_scaling_policy": "autoScalingPolicy",
            "bid_price": "bidPrice",
            "configurations": "configurations",
            "ebs_configuration": "ebsConfiguration",
            "market": "market",
            "name": "name",
        },
    )
    class InstanceGroupConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            auto_scaling_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.AutoScalingPolicyProperty"]] = None,
            bid_price: typing.Optional[builtins.str] = None,
            configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]] = None,
            ebs_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsConfigurationProperty"]] = None,
            market: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_count: ``CfnCluster.InstanceGroupConfigProperty.InstanceCount``.
            :param instance_type: ``CfnCluster.InstanceGroupConfigProperty.InstanceType``.
            :param auto_scaling_policy: ``CfnCluster.InstanceGroupConfigProperty.AutoScalingPolicy``.
            :param bid_price: ``CfnCluster.InstanceGroupConfigProperty.BidPrice``.
            :param configurations: ``CfnCluster.InstanceGroupConfigProperty.Configurations``.
            :param ebs_configuration: ``CfnCluster.InstanceGroupConfigProperty.EbsConfiguration``.
            :param market: ``CfnCluster.InstanceGroupConfigProperty.Market``.
            :param name: ``CfnCluster.InstanceGroupConfigProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
            }
            if auto_scaling_policy is not None:
                self._values["auto_scaling_policy"] = auto_scaling_policy
            if bid_price is not None:
                self._values["bid_price"] = bid_price
            if configurations is not None:
                self._values["configurations"] = configurations
            if ebs_configuration is not None:
                self._values["ebs_configuration"] = ebs_configuration
            if market is not None:
                self._values["market"] = market
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnCluster.InstanceGroupConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnCluster.InstanceGroupConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_scaling_policy(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.AutoScalingPolicyProperty"]]:
            '''``CfnCluster.InstanceGroupConfigProperty.AutoScalingPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-autoscalingpolicy
            '''
            result = self._values.get("auto_scaling_policy")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.AutoScalingPolicyProperty"]], result)

        @builtins.property
        def bid_price(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.InstanceGroupConfigProperty.BidPrice``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-bidprice
            '''
            result = self._values.get("bid_price")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]]:
            '''``CfnCluster.InstanceGroupConfigProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]], result)

        @builtins.property
        def ebs_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsConfigurationProperty"]]:
            '''``CfnCluster.InstanceGroupConfigProperty.EbsConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-ebsconfiguration
            '''
            result = self._values.get("ebs_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsConfigurationProperty"]], result)

        @builtins.property
        def market(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.InstanceGroupConfigProperty.Market``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-market
            '''
            result = self._values.get("market")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.InstanceGroupConfigProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancegroupconfig.html#cfn-elasticmapreduce-cluster-instancegroupconfig-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceGroupConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.InstanceTypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "bid_price": "bidPrice",
            "bid_price_as_percentage_of_on_demand_price": "bidPriceAsPercentageOfOnDemandPrice",
            "configurations": "configurations",
            "ebs_configuration": "ebsConfiguration",
            "weighted_capacity": "weightedCapacity",
        },
    )
    class InstanceTypeConfigProperty:
        def __init__(
            self,
            *,
            instance_type: builtins.str,
            bid_price: typing.Optional[builtins.str] = None,
            bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
            configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]] = None,
            ebs_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsConfigurationProperty"]] = None,
            weighted_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param instance_type: ``CfnCluster.InstanceTypeConfigProperty.InstanceType``.
            :param bid_price: ``CfnCluster.InstanceTypeConfigProperty.BidPrice``.
            :param bid_price_as_percentage_of_on_demand_price: ``CfnCluster.InstanceTypeConfigProperty.BidPriceAsPercentageOfOnDemandPrice``.
            :param configurations: ``CfnCluster.InstanceTypeConfigProperty.Configurations``.
            :param ebs_configuration: ``CfnCluster.InstanceTypeConfigProperty.EbsConfiguration``.
            :param weighted_capacity: ``CfnCluster.InstanceTypeConfigProperty.WeightedCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_type": instance_type,
            }
            if bid_price is not None:
                self._values["bid_price"] = bid_price
            if bid_price_as_percentage_of_on_demand_price is not None:
                self._values["bid_price_as_percentage_of_on_demand_price"] = bid_price_as_percentage_of_on_demand_price
            if configurations is not None:
                self._values["configurations"] = configurations
            if ebs_configuration is not None:
                self._values["ebs_configuration"] = ebs_configuration
            if weighted_capacity is not None:
                self._values["weighted_capacity"] = weighted_capacity

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnCluster.InstanceTypeConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bid_price(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.InstanceTypeConfigProperty.BidPrice``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-bidprice
            '''
            result = self._values.get("bid_price")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bid_price_as_percentage_of_on_demand_price(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.InstanceTypeConfigProperty.BidPriceAsPercentageOfOnDemandPrice``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-bidpriceaspercentageofondemandprice
            '''
            result = self._values.get("bid_price_as_percentage_of_on_demand_price")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]]:
            '''``CfnCluster.InstanceTypeConfigProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationProperty"]]]], result)

        @builtins.property
        def ebs_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsConfigurationProperty"]]:
            '''``CfnCluster.InstanceTypeConfigProperty.EbsConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-ebsconfiguration
            '''
            result = self._values.get("ebs_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EbsConfigurationProperty"]], result)

        @builtins.property
        def weighted_capacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.InstanceTypeConfigProperty.WeightedCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-instancetypeconfig.html#cfn-elasticmapreduce-cluster-instancetypeconfig-weightedcapacity
            '''
            result = self._values.get("weighted_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceTypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.JobFlowInstancesConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "additional_master_security_groups": "additionalMasterSecurityGroups",
            "additional_slave_security_groups": "additionalSlaveSecurityGroups",
            "core_instance_fleet": "coreInstanceFleet",
            "core_instance_group": "coreInstanceGroup",
            "ec2_key_name": "ec2KeyName",
            "ec2_subnet_id": "ec2SubnetId",
            "ec2_subnet_ids": "ec2SubnetIds",
            "emr_managed_master_security_group": "emrManagedMasterSecurityGroup",
            "emr_managed_slave_security_group": "emrManagedSlaveSecurityGroup",
            "hadoop_version": "hadoopVersion",
            "keep_job_flow_alive_when_no_steps": "keepJobFlowAliveWhenNoSteps",
            "master_instance_fleet": "masterInstanceFleet",
            "master_instance_group": "masterInstanceGroup",
            "placement": "placement",
            "service_access_security_group": "serviceAccessSecurityGroup",
            "termination_protected": "terminationProtected",
        },
    )
    class JobFlowInstancesConfigProperty:
        def __init__(
            self,
            *,
            additional_master_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            additional_slave_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            core_instance_fleet: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetConfigProperty"]] = None,
            core_instance_group: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceGroupConfigProperty"]] = None,
            ec2_key_name: typing.Optional[builtins.str] = None,
            ec2_subnet_id: typing.Optional[builtins.str] = None,
            ec2_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            emr_managed_master_security_group: typing.Optional[builtins.str] = None,
            emr_managed_slave_security_group: typing.Optional[builtins.str] = None,
            hadoop_version: typing.Optional[builtins.str] = None,
            keep_job_flow_alive_when_no_steps: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            master_instance_fleet: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetConfigProperty"]] = None,
            master_instance_group: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceGroupConfigProperty"]] = None,
            placement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.PlacementTypeProperty"]] = None,
            service_access_security_group: typing.Optional[builtins.str] = None,
            termination_protected: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param additional_master_security_groups: ``CfnCluster.JobFlowInstancesConfigProperty.AdditionalMasterSecurityGroups``.
            :param additional_slave_security_groups: ``CfnCluster.JobFlowInstancesConfigProperty.AdditionalSlaveSecurityGroups``.
            :param core_instance_fleet: ``CfnCluster.JobFlowInstancesConfigProperty.CoreInstanceFleet``.
            :param core_instance_group: ``CfnCluster.JobFlowInstancesConfigProperty.CoreInstanceGroup``.
            :param ec2_key_name: ``CfnCluster.JobFlowInstancesConfigProperty.Ec2KeyName``.
            :param ec2_subnet_id: ``CfnCluster.JobFlowInstancesConfigProperty.Ec2SubnetId``.
            :param ec2_subnet_ids: ``CfnCluster.JobFlowInstancesConfigProperty.Ec2SubnetIds``.
            :param emr_managed_master_security_group: ``CfnCluster.JobFlowInstancesConfigProperty.EmrManagedMasterSecurityGroup``.
            :param emr_managed_slave_security_group: ``CfnCluster.JobFlowInstancesConfigProperty.EmrManagedSlaveSecurityGroup``.
            :param hadoop_version: ``CfnCluster.JobFlowInstancesConfigProperty.HadoopVersion``.
            :param keep_job_flow_alive_when_no_steps: ``CfnCluster.JobFlowInstancesConfigProperty.KeepJobFlowAliveWhenNoSteps``.
            :param master_instance_fleet: ``CfnCluster.JobFlowInstancesConfigProperty.MasterInstanceFleet``.
            :param master_instance_group: ``CfnCluster.JobFlowInstancesConfigProperty.MasterInstanceGroup``.
            :param placement: ``CfnCluster.JobFlowInstancesConfigProperty.Placement``.
            :param service_access_security_group: ``CfnCluster.JobFlowInstancesConfigProperty.ServiceAccessSecurityGroup``.
            :param termination_protected: ``CfnCluster.JobFlowInstancesConfigProperty.TerminationProtected``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if additional_master_security_groups is not None:
                self._values["additional_master_security_groups"] = additional_master_security_groups
            if additional_slave_security_groups is not None:
                self._values["additional_slave_security_groups"] = additional_slave_security_groups
            if core_instance_fleet is not None:
                self._values["core_instance_fleet"] = core_instance_fleet
            if core_instance_group is not None:
                self._values["core_instance_group"] = core_instance_group
            if ec2_key_name is not None:
                self._values["ec2_key_name"] = ec2_key_name
            if ec2_subnet_id is not None:
                self._values["ec2_subnet_id"] = ec2_subnet_id
            if ec2_subnet_ids is not None:
                self._values["ec2_subnet_ids"] = ec2_subnet_ids
            if emr_managed_master_security_group is not None:
                self._values["emr_managed_master_security_group"] = emr_managed_master_security_group
            if emr_managed_slave_security_group is not None:
                self._values["emr_managed_slave_security_group"] = emr_managed_slave_security_group
            if hadoop_version is not None:
                self._values["hadoop_version"] = hadoop_version
            if keep_job_flow_alive_when_no_steps is not None:
                self._values["keep_job_flow_alive_when_no_steps"] = keep_job_flow_alive_when_no_steps
            if master_instance_fleet is not None:
                self._values["master_instance_fleet"] = master_instance_fleet
            if master_instance_group is not None:
                self._values["master_instance_group"] = master_instance_group
            if placement is not None:
                self._values["placement"] = placement
            if service_access_security_group is not None:
                self._values["service_access_security_group"] = service_access_security_group
            if termination_protected is not None:
                self._values["termination_protected"] = termination_protected

        @builtins.property
        def additional_master_security_groups(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.AdditionalMasterSecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-additionalmastersecuritygroups
            '''
            result = self._values.get("additional_master_security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def additional_slave_security_groups(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.AdditionalSlaveSecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-additionalslavesecuritygroups
            '''
            result = self._values.get("additional_slave_security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def core_instance_fleet(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetConfigProperty"]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.CoreInstanceFleet``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-coreinstancefleet
            '''
            result = self._values.get("core_instance_fleet")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetConfigProperty"]], result)

        @builtins.property
        def core_instance_group(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceGroupConfigProperty"]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.CoreInstanceGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-coreinstancegroup
            '''
            result = self._values.get("core_instance_group")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceGroupConfigProperty"]], result)

        @builtins.property
        def ec2_key_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.Ec2KeyName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-ec2keyname
            '''
            result = self._values.get("ec2_key_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ec2_subnet_id(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.Ec2SubnetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-ec2subnetid
            '''
            result = self._values.get("ec2_subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ec2_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.Ec2SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-ec2subnetids
            '''
            result = self._values.get("ec2_subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def emr_managed_master_security_group(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.EmrManagedMasterSecurityGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-emrmanagedmastersecuritygroup
            '''
            result = self._values.get("emr_managed_master_security_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def emr_managed_slave_security_group(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.EmrManagedSlaveSecurityGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-emrmanagedslavesecuritygroup
            '''
            result = self._values.get("emr_managed_slave_security_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hadoop_version(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.HadoopVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-hadoopversion
            '''
            result = self._values.get("hadoop_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def keep_job_flow_alive_when_no_steps(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.KeepJobFlowAliveWhenNoSteps``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-keepjobflowalivewhennosteps
            '''
            result = self._values.get("keep_job_flow_alive_when_no_steps")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def master_instance_fleet(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetConfigProperty"]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.MasterInstanceFleet``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-masterinstancefleet
            '''
            result = self._values.get("master_instance_fleet")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceFleetConfigProperty"]], result)

        @builtins.property
        def master_instance_group(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceGroupConfigProperty"]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.MasterInstanceGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-masterinstancegroup
            '''
            result = self._values.get("master_instance_group")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.InstanceGroupConfigProperty"]], result)

        @builtins.property
        def placement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.PlacementTypeProperty"]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.Placement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-placement
            '''
            result = self._values.get("placement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.PlacementTypeProperty"]], result)

        @builtins.property
        def service_access_security_group(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.ServiceAccessSecurityGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-serviceaccesssecuritygroup
            '''
            result = self._values.get("service_access_security_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def termination_protected(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCluster.JobFlowInstancesConfigProperty.TerminationProtected``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-jobflowinstancesconfig.html#cfn-elasticmapreduce-cluster-jobflowinstancesconfig-terminationprotected
            '''
            result = self._values.get("termination_protected")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobFlowInstancesConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.KerberosAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kdc_admin_password": "kdcAdminPassword",
            "realm": "realm",
            "ad_domain_join_password": "adDomainJoinPassword",
            "ad_domain_join_user": "adDomainJoinUser",
            "cross_realm_trust_principal_password": "crossRealmTrustPrincipalPassword",
        },
    )
    class KerberosAttributesProperty:
        def __init__(
            self,
            *,
            kdc_admin_password: builtins.str,
            realm: builtins.str,
            ad_domain_join_password: typing.Optional[builtins.str] = None,
            ad_domain_join_user: typing.Optional[builtins.str] = None,
            cross_realm_trust_principal_password: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param kdc_admin_password: ``CfnCluster.KerberosAttributesProperty.KdcAdminPassword``.
            :param realm: ``CfnCluster.KerberosAttributesProperty.Realm``.
            :param ad_domain_join_password: ``CfnCluster.KerberosAttributesProperty.ADDomainJoinPassword``.
            :param ad_domain_join_user: ``CfnCluster.KerberosAttributesProperty.ADDomainJoinUser``.
            :param cross_realm_trust_principal_password: ``CfnCluster.KerberosAttributesProperty.CrossRealmTrustPrincipalPassword``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "kdc_admin_password": kdc_admin_password,
                "realm": realm,
            }
            if ad_domain_join_password is not None:
                self._values["ad_domain_join_password"] = ad_domain_join_password
            if ad_domain_join_user is not None:
                self._values["ad_domain_join_user"] = ad_domain_join_user
            if cross_realm_trust_principal_password is not None:
                self._values["cross_realm_trust_principal_password"] = cross_realm_trust_principal_password

        @builtins.property
        def kdc_admin_password(self) -> builtins.str:
            '''``CfnCluster.KerberosAttributesProperty.KdcAdminPassword``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-kdcadminpassword
            '''
            result = self._values.get("kdc_admin_password")
            assert result is not None, "Required property 'kdc_admin_password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def realm(self) -> builtins.str:
            '''``CfnCluster.KerberosAttributesProperty.Realm``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-realm
            '''
            result = self._values.get("realm")
            assert result is not None, "Required property 'realm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ad_domain_join_password(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.KerberosAttributesProperty.ADDomainJoinPassword``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-addomainjoinpassword
            '''
            result = self._values.get("ad_domain_join_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ad_domain_join_user(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.KerberosAttributesProperty.ADDomainJoinUser``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-addomainjoinuser
            '''
            result = self._values.get("ad_domain_join_user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cross_realm_trust_principal_password(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.KerberosAttributesProperty.CrossRealmTrustPrincipalPassword``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-kerberosattributes.html#cfn-elasticmapreduce-cluster-kerberosattributes-crossrealmtrustprincipalpassword
            '''
            result = self._values.get("cross_realm_trust_principal_password")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KerberosAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.KeyValueProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class KeyValueProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: ``CfnCluster.KeyValueProperty.Key``.
            :param value: ``CfnCluster.KeyValueProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-keyvalue.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.KeyValueProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-keyvalue.html#cfn-elasticmapreduce-cluster-keyvalue-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.KeyValueProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-keyvalue.html#cfn-elasticmapreduce-cluster-keyvalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ManagedScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"compute_limits": "computeLimits"},
    )
    class ManagedScalingPolicyProperty:
        def __init__(
            self,
            *,
            compute_limits: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ComputeLimitsProperty"]] = None,
        ) -> None:
            '''
            :param compute_limits: ``CfnCluster.ManagedScalingPolicyProperty.ComputeLimits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-managedscalingpolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if compute_limits is not None:
                self._values["compute_limits"] = compute_limits

        @builtins.property
        def compute_limits(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ComputeLimitsProperty"]]:
            '''``CfnCluster.ManagedScalingPolicyProperty.ComputeLimits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-managedscalingpolicy.html#cfn-elasticmapreduce-cluster-managedscalingpolicy-computelimits
            '''
            result = self._values.get("compute_limits")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ComputeLimitsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManagedScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnCluster.MetricDimensionProperty.Key``.
            :param value: ``CfnCluster.MetricDimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-metricdimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnCluster.MetricDimensionProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-metricdimension.html#cfn-elasticmapreduce-cluster-metricdimension-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnCluster.MetricDimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-metricdimension.html#cfn-elasticmapreduce-cluster-metricdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.OnDemandProvisioningSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"allocation_strategy": "allocationStrategy"},
    )
    class OnDemandProvisioningSpecificationProperty:
        def __init__(self, *, allocation_strategy: builtins.str) -> None:
            '''
            :param allocation_strategy: ``CfnCluster.OnDemandProvisioningSpecificationProperty.AllocationStrategy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ondemandprovisioningspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "allocation_strategy": allocation_strategy,
            }

        @builtins.property
        def allocation_strategy(self) -> builtins.str:
            '''``CfnCluster.OnDemandProvisioningSpecificationProperty.AllocationStrategy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-ondemandprovisioningspecification.html#cfn-elasticmapreduce-cluster-ondemandprovisioningspecification-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            assert result is not None, "Required property 'allocation_strategy' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnDemandProvisioningSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.PlacementTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"availability_zone": "availabilityZone"},
    )
    class PlacementTypeProperty:
        def __init__(self, *, availability_zone: builtins.str) -> None:
            '''
            :param availability_zone: ``CfnCluster.PlacementTypeProperty.AvailabilityZone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-placementtype.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "availability_zone": availability_zone,
            }

        @builtins.property
        def availability_zone(self) -> builtins.str:
            '''``CfnCluster.PlacementTypeProperty.AvailabilityZone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-placementtype.html#cfn-elasticmapreduce-cluster-placementtype-availabilityzone
            '''
            result = self._values.get("availability_zone")
            assert result is not None, "Required property 'availability_zone' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ScalingActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "simple_scaling_policy_configuration": "simpleScalingPolicyConfiguration",
            "market": "market",
        },
    )
    class ScalingActionProperty:
        def __init__(
            self,
            *,
            simple_scaling_policy_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnCluster.SimpleScalingPolicyConfigurationProperty"],
            market: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param simple_scaling_policy_configuration: ``CfnCluster.ScalingActionProperty.SimpleScalingPolicyConfiguration``.
            :param market: ``CfnCluster.ScalingActionProperty.Market``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "simple_scaling_policy_configuration": simple_scaling_policy_configuration,
            }
            if market is not None:
                self._values["market"] = market

        @builtins.property
        def simple_scaling_policy_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.SimpleScalingPolicyConfigurationProperty"]:
            '''``CfnCluster.ScalingActionProperty.SimpleScalingPolicyConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingaction.html#cfn-elasticmapreduce-cluster-scalingaction-simplescalingpolicyconfiguration
            '''
            result = self._values.get("simple_scaling_policy_configuration")
            assert result is not None, "Required property 'simple_scaling_policy_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.SimpleScalingPolicyConfigurationProperty"], result)

        @builtins.property
        def market(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.ScalingActionProperty.Market``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingaction.html#cfn-elasticmapreduce-cluster-scalingaction-market
            '''
            result = self._values.get("market")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ScalingConstraintsProperty",
        jsii_struct_bases=[],
        name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
    )
    class ScalingConstraintsProperty:
        def __init__(
            self,
            *,
            max_capacity: jsii.Number,
            min_capacity: jsii.Number,
        ) -> None:
            '''
            :param max_capacity: ``CfnCluster.ScalingConstraintsProperty.MaxCapacity``.
            :param min_capacity: ``CfnCluster.ScalingConstraintsProperty.MinCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingconstraints.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_capacity": max_capacity,
                "min_capacity": min_capacity,
            }

        @builtins.property
        def max_capacity(self) -> jsii.Number:
            '''``CfnCluster.ScalingConstraintsProperty.MaxCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingconstraints.html#cfn-elasticmapreduce-cluster-scalingconstraints-maxcapacity
            '''
            result = self._values.get("max_capacity")
            assert result is not None, "Required property 'max_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_capacity(self) -> jsii.Number:
            '''``CfnCluster.ScalingConstraintsProperty.MinCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingconstraints.html#cfn-elasticmapreduce-cluster-scalingconstraints-mincapacity
            '''
            result = self._values.get("min_capacity")
            assert result is not None, "Required property 'min_capacity' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingConstraintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ScalingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "name": "name",
            "trigger": "trigger",
            "description": "description",
        },
    )
    class ScalingRuleProperty:
        def __init__(
            self,
            *,
            action: typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingActionProperty"],
            name: builtins.str,
            trigger: typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingTriggerProperty"],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param action: ``CfnCluster.ScalingRuleProperty.Action``.
            :param name: ``CfnCluster.ScalingRuleProperty.Name``.
            :param trigger: ``CfnCluster.ScalingRuleProperty.Trigger``.
            :param description: ``CfnCluster.ScalingRuleProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
                "name": name,
                "trigger": trigger,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def action(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingActionProperty"]:
            '''``CfnCluster.ScalingRuleProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html#cfn-elasticmapreduce-cluster-scalingrule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingActionProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnCluster.ScalingRuleProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html#cfn-elasticmapreduce-cluster-scalingrule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def trigger(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingTriggerProperty"]:
            '''``CfnCluster.ScalingRuleProperty.Trigger``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html#cfn-elasticmapreduce-cluster-scalingrule-trigger
            '''
            result = self._values.get("trigger")
            assert result is not None, "Required property 'trigger' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScalingTriggerProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.ScalingRuleProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingrule.html#cfn-elasticmapreduce-cluster-scalingrule-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ScalingTriggerProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_alarm_definition": "cloudWatchAlarmDefinition"},
    )
    class ScalingTriggerProperty:
        def __init__(
            self,
            *,
            cloud_watch_alarm_definition: typing.Union[aws_cdk.core.IResolvable, "CfnCluster.CloudWatchAlarmDefinitionProperty"],
        ) -> None:
            '''
            :param cloud_watch_alarm_definition: ``CfnCluster.ScalingTriggerProperty.CloudWatchAlarmDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingtrigger.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cloud_watch_alarm_definition": cloud_watch_alarm_definition,
            }

        @builtins.property
        def cloud_watch_alarm_definition(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.CloudWatchAlarmDefinitionProperty"]:
            '''``CfnCluster.ScalingTriggerProperty.CloudWatchAlarmDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scalingtrigger.html#cfn-elasticmapreduce-cluster-scalingtrigger-cloudwatchalarmdefinition
            '''
            result = self._values.get("cloud_watch_alarm_definition")
            assert result is not None, "Required property 'cloud_watch_alarm_definition' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.CloudWatchAlarmDefinitionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingTriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.ScriptBootstrapActionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path", "args": "args"},
    )
    class ScriptBootstrapActionConfigProperty:
        def __init__(
            self,
            *,
            path: builtins.str,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param path: ``CfnCluster.ScriptBootstrapActionConfigProperty.Path``.
            :param args: ``CfnCluster.ScriptBootstrapActionConfigProperty.Args``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scriptbootstrapactionconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "path": path,
            }
            if args is not None:
                self._values["args"] = args

        @builtins.property
        def path(self) -> builtins.str:
            '''``CfnCluster.ScriptBootstrapActionConfigProperty.Path``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scriptbootstrapactionconfig.html#cfn-elasticmapreduce-cluster-scriptbootstrapactionconfig-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCluster.ScriptBootstrapActionConfigProperty.Args``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-scriptbootstrapactionconfig.html#cfn-elasticmapreduce-cluster-scriptbootstrapactionconfig-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScriptBootstrapActionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.SimpleScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scaling_adjustment": "scalingAdjustment",
            "adjustment_type": "adjustmentType",
            "cool_down": "coolDown",
        },
    )
    class SimpleScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            scaling_adjustment: jsii.Number,
            adjustment_type: typing.Optional[builtins.str] = None,
            cool_down: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param scaling_adjustment: ``CfnCluster.SimpleScalingPolicyConfigurationProperty.ScalingAdjustment``.
            :param adjustment_type: ``CfnCluster.SimpleScalingPolicyConfigurationProperty.AdjustmentType``.
            :param cool_down: ``CfnCluster.SimpleScalingPolicyConfigurationProperty.CoolDown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-simplescalingpolicyconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "scaling_adjustment": scaling_adjustment,
            }
            if adjustment_type is not None:
                self._values["adjustment_type"] = adjustment_type
            if cool_down is not None:
                self._values["cool_down"] = cool_down

        @builtins.property
        def scaling_adjustment(self) -> jsii.Number:
            '''``CfnCluster.SimpleScalingPolicyConfigurationProperty.ScalingAdjustment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-cluster-simplescalingpolicyconfiguration-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            assert result is not None, "Required property 'scaling_adjustment' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def adjustment_type(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.SimpleScalingPolicyConfigurationProperty.AdjustmentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-cluster-simplescalingpolicyconfiguration-adjustmenttype
            '''
            result = self._values.get("adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cool_down(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.SimpleScalingPolicyConfigurationProperty.CoolDown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-cluster-simplescalingpolicyconfiguration-cooldown
            '''
            result = self._values.get("cool_down")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SimpleScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.SpotProvisioningSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "timeout_action": "timeoutAction",
            "timeout_duration_minutes": "timeoutDurationMinutes",
            "allocation_strategy": "allocationStrategy",
            "block_duration_minutes": "blockDurationMinutes",
        },
    )
    class SpotProvisioningSpecificationProperty:
        def __init__(
            self,
            *,
            timeout_action: builtins.str,
            timeout_duration_minutes: jsii.Number,
            allocation_strategy: typing.Optional[builtins.str] = None,
            block_duration_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param timeout_action: ``CfnCluster.SpotProvisioningSpecificationProperty.TimeoutAction``.
            :param timeout_duration_minutes: ``CfnCluster.SpotProvisioningSpecificationProperty.TimeoutDurationMinutes``.
            :param allocation_strategy: ``CfnCluster.SpotProvisioningSpecificationProperty.AllocationStrategy``.
            :param block_duration_minutes: ``CfnCluster.SpotProvisioningSpecificationProperty.BlockDurationMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "timeout_action": timeout_action,
                "timeout_duration_minutes": timeout_duration_minutes,
            }
            if allocation_strategy is not None:
                self._values["allocation_strategy"] = allocation_strategy
            if block_duration_minutes is not None:
                self._values["block_duration_minutes"] = block_duration_minutes

        @builtins.property
        def timeout_action(self) -> builtins.str:
            '''``CfnCluster.SpotProvisioningSpecificationProperty.TimeoutAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html#cfn-elasticmapreduce-cluster-spotprovisioningspecification-timeoutaction
            '''
            result = self._values.get("timeout_action")
            assert result is not None, "Required property 'timeout_action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_duration_minutes(self) -> jsii.Number:
            '''``CfnCluster.SpotProvisioningSpecificationProperty.TimeoutDurationMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html#cfn-elasticmapreduce-cluster-spotprovisioningspecification-timeoutdurationminutes
            '''
            result = self._values.get("timeout_duration_minutes")
            assert result is not None, "Required property 'timeout_duration_minutes' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def allocation_strategy(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.SpotProvisioningSpecificationProperty.AllocationStrategy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html#cfn-elasticmapreduce-cluster-spotprovisioningspecification-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.SpotProvisioningSpecificationProperty.BlockDurationMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-spotprovisioningspecification.html#cfn-elasticmapreduce-cluster-spotprovisioningspecification-blockdurationminutes
            '''
            result = self._values.get("block_duration_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpotProvisioningSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.StepConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hadoop_jar_step": "hadoopJarStep",
            "name": "name",
            "action_on_failure": "actionOnFailure",
        },
    )
    class StepConfigProperty:
        def __init__(
            self,
            *,
            hadoop_jar_step: typing.Union[aws_cdk.core.IResolvable, "CfnCluster.HadoopJarStepConfigProperty"],
            name: builtins.str,
            action_on_failure: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param hadoop_jar_step: ``CfnCluster.StepConfigProperty.HadoopJarStep``.
            :param name: ``CfnCluster.StepConfigProperty.Name``.
            :param action_on_failure: ``CfnCluster.StepConfigProperty.ActionOnFailure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "hadoop_jar_step": hadoop_jar_step,
                "name": name,
            }
            if action_on_failure is not None:
                self._values["action_on_failure"] = action_on_failure

        @builtins.property
        def hadoop_jar_step(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.HadoopJarStepConfigProperty"]:
            '''``CfnCluster.StepConfigProperty.HadoopJarStep``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html#cfn-elasticmapreduce-cluster-stepconfig-hadoopjarstep
            '''
            result = self._values.get("hadoop_jar_step")
            assert result is not None, "Required property 'hadoop_jar_step' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.HadoopJarStepConfigProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnCluster.StepConfigProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html#cfn-elasticmapreduce-cluster-stepconfig-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def action_on_failure(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.StepConfigProperty.ActionOnFailure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-stepconfig.html#cfn-elasticmapreduce-cluster-stepconfig-actiononfailure
            '''
            result = self._values.get("action_on_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnCluster.VolumeSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "size_in_gb": "sizeInGb",
            "volume_type": "volumeType",
            "iops": "iops",
        },
    )
    class VolumeSpecificationProperty:
        def __init__(
            self,
            *,
            size_in_gb: jsii.Number,
            volume_type: builtins.str,
            iops: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param size_in_gb: ``CfnCluster.VolumeSpecificationProperty.SizeInGB``.
            :param volume_type: ``CfnCluster.VolumeSpecificationProperty.VolumeType``.
            :param iops: ``CfnCluster.VolumeSpecificationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "size_in_gb": size_in_gb,
                "volume_type": volume_type,
            }
            if iops is not None:
                self._values["iops"] = iops

        @builtins.property
        def size_in_gb(self) -> jsii.Number:
            '''``CfnCluster.VolumeSpecificationProperty.SizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html#cfn-elasticmapreduce-cluster-volumespecification-sizeingb
            '''
            result = self._values.get("size_in_gb")
            assert result is not None, "Required property 'size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_type(self) -> builtins.str:
            '''``CfnCluster.VolumeSpecificationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html#cfn-elasticmapreduce-cluster-volumespecification-volumetype
            '''
            result = self._values.get("volume_type")
            assert result is not None, "Required property 'volume_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''``CfnCluster.VolumeSpecificationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-cluster-volumespecification.html#cfn-elasticmapreduce-cluster-volumespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-emr.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "instances": "instances",
        "job_flow_role": "jobFlowRole",
        "name": "name",
        "service_role": "serviceRole",
        "additional_info": "additionalInfo",
        "applications": "applications",
        "auto_scaling_role": "autoScalingRole",
        "bootstrap_actions": "bootstrapActions",
        "configurations": "configurations",
        "custom_ami_id": "customAmiId",
        "ebs_root_volume_size": "ebsRootVolumeSize",
        "kerberos_attributes": "kerberosAttributes",
        "log_encryption_kms_key_id": "logEncryptionKmsKeyId",
        "log_uri": "logUri",
        "managed_scaling_policy": "managedScalingPolicy",
        "release_label": "releaseLabel",
        "scale_down_behavior": "scaleDownBehavior",
        "security_configuration": "securityConfiguration",
        "step_concurrency_level": "stepConcurrencyLevel",
        "steps": "steps",
        "tags": "tags",
        "visible_to_all_users": "visibleToAllUsers",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        instances: typing.Union[CfnCluster.JobFlowInstancesConfigProperty, aws_cdk.core.IResolvable],
        job_flow_role: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        additional_info: typing.Any = None,
        applications: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ApplicationProperty]]]] = None,
        auto_scaling_role: typing.Optional[builtins.str] = None,
        bootstrap_actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnCluster.BootstrapActionConfigProperty]]]] = None,
        configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ConfigurationProperty]]]] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        ebs_root_volume_size: typing.Optional[jsii.Number] = None,
        kerberos_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.KerberosAttributesProperty]] = None,
        log_encryption_kms_key_id: typing.Optional[builtins.str] = None,
        log_uri: typing.Optional[builtins.str] = None,
        managed_scaling_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ManagedScalingPolicyProperty]] = None,
        release_label: typing.Optional[builtins.str] = None,
        scale_down_behavior: typing.Optional[builtins.str] = None,
        security_configuration: typing.Optional[builtins.str] = None,
        step_concurrency_level: typing.Optional[jsii.Number] = None,
        steps: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnCluster.StepConfigProperty]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        visible_to_all_users: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EMR::Cluster``.

        :param instances: ``AWS::EMR::Cluster.Instances``.
        :param job_flow_role: ``AWS::EMR::Cluster.JobFlowRole``.
        :param name: ``AWS::EMR::Cluster.Name``.
        :param service_role: ``AWS::EMR::Cluster.ServiceRole``.
        :param additional_info: ``AWS::EMR::Cluster.AdditionalInfo``.
        :param applications: ``AWS::EMR::Cluster.Applications``.
        :param auto_scaling_role: ``AWS::EMR::Cluster.AutoScalingRole``.
        :param bootstrap_actions: ``AWS::EMR::Cluster.BootstrapActions``.
        :param configurations: ``AWS::EMR::Cluster.Configurations``.
        :param custom_ami_id: ``AWS::EMR::Cluster.CustomAmiId``.
        :param ebs_root_volume_size: ``AWS::EMR::Cluster.EbsRootVolumeSize``.
        :param kerberos_attributes: ``AWS::EMR::Cluster.KerberosAttributes``.
        :param log_encryption_kms_key_id: ``AWS::EMR::Cluster.LogEncryptionKmsKeyId``.
        :param log_uri: ``AWS::EMR::Cluster.LogUri``.
        :param managed_scaling_policy: ``AWS::EMR::Cluster.ManagedScalingPolicy``.
        :param release_label: ``AWS::EMR::Cluster.ReleaseLabel``.
        :param scale_down_behavior: ``AWS::EMR::Cluster.ScaleDownBehavior``.
        :param security_configuration: ``AWS::EMR::Cluster.SecurityConfiguration``.
        :param step_concurrency_level: ``AWS::EMR::Cluster.StepConcurrencyLevel``.
        :param steps: ``AWS::EMR::Cluster.Steps``.
        :param tags: ``AWS::EMR::Cluster.Tags``.
        :param visible_to_all_users: ``AWS::EMR::Cluster.VisibleToAllUsers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instances": instances,
            "job_flow_role": job_flow_role,
            "name": name,
            "service_role": service_role,
        }
        if additional_info is not None:
            self._values["additional_info"] = additional_info
        if applications is not None:
            self._values["applications"] = applications
        if auto_scaling_role is not None:
            self._values["auto_scaling_role"] = auto_scaling_role
        if bootstrap_actions is not None:
            self._values["bootstrap_actions"] = bootstrap_actions
        if configurations is not None:
            self._values["configurations"] = configurations
        if custom_ami_id is not None:
            self._values["custom_ami_id"] = custom_ami_id
        if ebs_root_volume_size is not None:
            self._values["ebs_root_volume_size"] = ebs_root_volume_size
        if kerberos_attributes is not None:
            self._values["kerberos_attributes"] = kerberos_attributes
        if log_encryption_kms_key_id is not None:
            self._values["log_encryption_kms_key_id"] = log_encryption_kms_key_id
        if log_uri is not None:
            self._values["log_uri"] = log_uri
        if managed_scaling_policy is not None:
            self._values["managed_scaling_policy"] = managed_scaling_policy
        if release_label is not None:
            self._values["release_label"] = release_label
        if scale_down_behavior is not None:
            self._values["scale_down_behavior"] = scale_down_behavior
        if security_configuration is not None:
            self._values["security_configuration"] = security_configuration
        if step_concurrency_level is not None:
            self._values["step_concurrency_level"] = step_concurrency_level
        if steps is not None:
            self._values["steps"] = steps
        if tags is not None:
            self._values["tags"] = tags
        if visible_to_all_users is not None:
            self._values["visible_to_all_users"] = visible_to_all_users

    @builtins.property
    def instances(
        self,
    ) -> typing.Union[CfnCluster.JobFlowInstancesConfigProperty, aws_cdk.core.IResolvable]:
        '''``AWS::EMR::Cluster.Instances``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-instances
        '''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(typing.Union[CfnCluster.JobFlowInstancesConfigProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def job_flow_role(self) -> builtins.str:
        '''``AWS::EMR::Cluster.JobFlowRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-jobflowrole
        '''
        result = self._values.get("job_flow_role")
        assert result is not None, "Required property 'job_flow_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::EMR::Cluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''``AWS::EMR::Cluster.ServiceRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-servicerole
        '''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_info(self) -> typing.Any:
        '''``AWS::EMR::Cluster.AdditionalInfo``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-additionalinfo
        '''
        result = self._values.get("additional_info")
        return typing.cast(typing.Any, result)

    @builtins.property
    def applications(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ApplicationProperty]]]]:
        '''``AWS::EMR::Cluster.Applications``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-applications
        '''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ApplicationProperty]]]], result)

    @builtins.property
    def auto_scaling_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.AutoScalingRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-autoscalingrole
        '''
        result = self._values.get("auto_scaling_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bootstrap_actions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.BootstrapActionConfigProperty]]]]:
        '''``AWS::EMR::Cluster.BootstrapActions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-bootstrapactions
        '''
        result = self._values.get("bootstrap_actions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.BootstrapActionConfigProperty]]]], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ConfigurationProperty]]]]:
        '''``AWS::EMR::Cluster.Configurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-configurations
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ConfigurationProperty]]]], result)

    @builtins.property
    def custom_ami_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.CustomAmiId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-customamiid
        '''
        result = self._values.get("custom_ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ebs_root_volume_size(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EMR::Cluster.EbsRootVolumeSize``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-ebsrootvolumesize
        '''
        result = self._values.get("ebs_root_volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kerberos_attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.KerberosAttributesProperty]]:
        '''``AWS::EMR::Cluster.KerberosAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-kerberosattributes
        '''
        result = self._values.get("kerberos_attributes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.KerberosAttributesProperty]], result)

    @builtins.property
    def log_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.LogEncryptionKmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-logencryptionkmskeyid
        '''
        result = self._values.get("log_encryption_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_uri(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.LogUri``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-loguri
        '''
        result = self._values.get("log_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ManagedScalingPolicyProperty]]:
        '''``AWS::EMR::Cluster.ManagedScalingPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-managedscalingpolicy
        '''
        result = self._values.get("managed_scaling_policy")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ManagedScalingPolicyProperty]], result)

    @builtins.property
    def release_label(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.ReleaseLabel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-releaselabel
        '''
        result = self._values.get("release_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_down_behavior(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.ScaleDownBehavior``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-scaledownbehavior
        '''
        result = self._values.get("scale_down_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_configuration(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Cluster.SecurityConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-securityconfiguration
        '''
        result = self._values.get("security_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def step_concurrency_level(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EMR::Cluster.StepConcurrencyLevel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-stepconcurrencylevel
        '''
        result = self._values.get("step_concurrency_level")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def steps(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.StepConfigProperty]]]]:
        '''``AWS::EMR::Cluster.Steps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-steps
        '''
        result = self._values.get("steps")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.StepConfigProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::EMR::Cluster.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def visible_to_all_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::EMR::Cluster.VisibleToAllUsers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html#cfn-elasticmapreduce-cluster-visibletoallusers
        '''
        result = self._values.get("visible_to_all_users")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInstanceFleetConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig",
):
    '''A CloudFormation ``AWS::EMR::InstanceFleetConfig``.

    :cloudformationResource: AWS::EMR::InstanceFleetConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster_id: builtins.str,
        instance_fleet_type: builtins.str,
        instance_type_configs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.InstanceTypeConfigProperty"]]]] = None,
        launch_specifications: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::EMR::InstanceFleetConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_id: ``AWS::EMR::InstanceFleetConfig.ClusterId``.
        :param instance_fleet_type: ``AWS::EMR::InstanceFleetConfig.InstanceFleetType``.
        :param instance_type_configs: ``AWS::EMR::InstanceFleetConfig.InstanceTypeConfigs``.
        :param launch_specifications: ``AWS::EMR::InstanceFleetConfig.LaunchSpecifications``.
        :param name: ``AWS::EMR::InstanceFleetConfig.Name``.
        :param target_on_demand_capacity: ``AWS::EMR::InstanceFleetConfig.TargetOnDemandCapacity``.
        :param target_spot_capacity: ``AWS::EMR::InstanceFleetConfig.TargetSpotCapacity``.
        '''
        props = CfnInstanceFleetConfigProps(
            cluster_id=cluster_id,
            instance_fleet_type=instance_fleet_type,
            instance_type_configs=instance_type_configs,
            launch_specifications=launch_specifications,
            name=name,
            target_on_demand_capacity=target_on_demand_capacity,
            target_spot_capacity=target_spot_capacity,
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
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        '''``AWS::EMR::InstanceFleetConfig.ClusterId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-clusterid
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        jsii.set(self, "clusterId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceFleetType")
    def instance_fleet_type(self) -> builtins.str:
        '''``AWS::EMR::InstanceFleetConfig.InstanceFleetType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancefleettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceFleetType"))

    @instance_fleet_type.setter
    def instance_fleet_type(self, value: builtins.str) -> None:
        jsii.set(self, "instanceFleetType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.InstanceTypeConfigProperty"]]]]:
        '''``AWS::EMR::InstanceFleetConfig.InstanceTypeConfigs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfigs
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.InstanceTypeConfigProperty"]]]], jsii.get(self, "instanceTypeConfigs"))

    @instance_type_configs.setter
    def instance_type_configs(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.InstanceTypeConfigProperty"]]]],
    ) -> None:
        jsii.set(self, "instanceTypeConfigs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty"]]:
        '''``AWS::EMR::InstanceFleetConfig.LaunchSpecifications``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-launchspecifications
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty"]], jsii.get(self, "launchSpecifications"))

    @launch_specifications.setter
    def launch_specifications(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty"]],
    ) -> None:
        jsii.set(self, "launchSpecifications", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::InstanceFleetConfig.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EMR::InstanceFleetConfig.TargetOnDemandCapacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-targetondemandcapacity
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetOnDemandCapacity"))

    @target_on_demand_capacity.setter
    def target_on_demand_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "targetOnDemandCapacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetSpotCapacity")
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EMR::InstanceFleetConfig.TargetSpotCapacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-targetspotcapacity
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetSpotCapacity"))

    @target_spot_capacity.setter
    def target_spot_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "targetSpotCapacity", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configuration_properties": "configurationProperties",
            "configurations": "configurations",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            classification: typing.Optional[builtins.str] = None,
            configuration_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.ConfigurationProperty"]]]] = None,
        ) -> None:
            '''
            :param classification: ``CfnInstanceFleetConfig.ConfigurationProperty.Classification``.
            :param configuration_properties: ``CfnInstanceFleetConfig.ConfigurationProperty.ConfigurationProperties``.
            :param configurations: ``CfnInstanceFleetConfig.ConfigurationProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-configuration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if classification is not None:
                self._values["classification"] = classification
            if configuration_properties is not None:
                self._values["configuration_properties"] = configuration_properties
            if configurations is not None:
                self._values["configurations"] = configurations

        @builtins.property
        def classification(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceFleetConfig.ConfigurationProperty.Classification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-configuration.html#cfn-elasticmapreduce-instancefleetconfig-configuration-classification
            '''
            result = self._values.get("classification")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configuration_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstanceFleetConfig.ConfigurationProperty.ConfigurationProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-configuration.html#cfn-elasticmapreduce-instancefleetconfig-configuration-configurationproperties
            '''
            result = self._values.get("configuration_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.ConfigurationProperty"]]]]:
            '''``CfnInstanceFleetConfig.ConfigurationProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-configuration.html#cfn-elasticmapreduce-instancefleetconfig-configuration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.ConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "volume_specification": "volumeSpecification",
            "volumes_per_instance": "volumesPerInstance",
        },
    )
    class EbsBlockDeviceConfigProperty:
        def __init__(
            self,
            *,
            volume_specification: typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.VolumeSpecificationProperty"],
            volumes_per_instance: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param volume_specification: ``CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty.VolumeSpecification``.
            :param volumes_per_instance: ``CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty.VolumesPerInstance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "volume_specification": volume_specification,
            }
            if volumes_per_instance is not None:
                self._values["volumes_per_instance"] = volumes_per_instance

        @builtins.property
        def volume_specification(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.VolumeSpecificationProperty"]:
            '''``CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty.VolumeSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig.html#cfn-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig-volumespecification
            '''
            result = self._values.get("volume_specification")
            assert result is not None, "Required property 'volume_specification' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.VolumeSpecificationProperty"], result)

        @builtins.property
        def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty.VolumesPerInstance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig.html#cfn-elasticmapreduce-instancefleetconfig-ebsblockdeviceconfig-volumesperinstance
            '''
            result = self._values.get("volumes_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig.EbsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_block_device_configs": "ebsBlockDeviceConfigs",
            "ebs_optimized": "ebsOptimized",
        },
    )
    class EbsConfigurationProperty:
        def __init__(
            self,
            *,
            ebs_block_device_configs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty"]]]] = None,
            ebs_optimized: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param ebs_block_device_configs: ``CfnInstanceFleetConfig.EbsConfigurationProperty.EbsBlockDeviceConfigs``.
            :param ebs_optimized: ``CfnInstanceFleetConfig.EbsConfigurationProperty.EbsOptimized``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ebs_block_device_configs is not None:
                self._values["ebs_block_device_configs"] = ebs_block_device_configs
            if ebs_optimized is not None:
                self._values["ebs_optimized"] = ebs_optimized

        @builtins.property
        def ebs_block_device_configs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty"]]]]:
            '''``CfnInstanceFleetConfig.EbsConfigurationProperty.EbsBlockDeviceConfigs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html#cfn-elasticmapreduce-instancefleetconfig-ebsconfiguration-ebsblockdeviceconfigs
            '''
            result = self._values.get("ebs_block_device_configs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.EbsBlockDeviceConfigProperty"]]]], result)

        @builtins.property
        def ebs_optimized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnInstanceFleetConfig.EbsConfigurationProperty.EbsOptimized``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ebsconfiguration.html#cfn-elasticmapreduce-instancefleetconfig-ebsconfiguration-ebsoptimized
            '''
            result = self._values.get("ebs_optimized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "on_demand_specification": "onDemandSpecification",
            "spot_specification": "spotSpecification",
        },
    )
    class InstanceFleetProvisioningSpecificationsProperty:
        def __init__(
            self,
            *,
            on_demand_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty"]] = None,
            spot_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty"]] = None,
        ) -> None:
            '''
            :param on_demand_specification: ``CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty.OnDemandSpecification``.
            :param spot_specification: ``CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty.SpotSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if on_demand_specification is not None:
                self._values["on_demand_specification"] = on_demand_specification
            if spot_specification is not None:
                self._values["spot_specification"] = spot_specification

        @builtins.property
        def on_demand_specification(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty"]]:
            '''``CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty.OnDemandSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications.html#cfn-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications-ondemandspecification
            '''
            result = self._values.get("on_demand_specification")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty"]], result)

        @builtins.property
        def spot_specification(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty"]]:
            '''``CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty.SpotSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications.html#cfn-elasticmapreduce-instancefleetconfig-instancefleetprovisioningspecifications-spotspecification
            '''
            result = self._values.get("spot_specification")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceFleetProvisioningSpecificationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig.InstanceTypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "bid_price": "bidPrice",
            "bid_price_as_percentage_of_on_demand_price": "bidPriceAsPercentageOfOnDemandPrice",
            "configurations": "configurations",
            "ebs_configuration": "ebsConfiguration",
            "weighted_capacity": "weightedCapacity",
        },
    )
    class InstanceTypeConfigProperty:
        def __init__(
            self,
            *,
            instance_type: builtins.str,
            bid_price: typing.Optional[builtins.str] = None,
            bid_price_as_percentage_of_on_demand_price: typing.Optional[jsii.Number] = None,
            configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.ConfigurationProperty"]]]] = None,
            ebs_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.EbsConfigurationProperty"]] = None,
            weighted_capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param instance_type: ``CfnInstanceFleetConfig.InstanceTypeConfigProperty.InstanceType``.
            :param bid_price: ``CfnInstanceFleetConfig.InstanceTypeConfigProperty.BidPrice``.
            :param bid_price_as_percentage_of_on_demand_price: ``CfnInstanceFleetConfig.InstanceTypeConfigProperty.BidPriceAsPercentageOfOnDemandPrice``.
            :param configurations: ``CfnInstanceFleetConfig.InstanceTypeConfigProperty.Configurations``.
            :param ebs_configuration: ``CfnInstanceFleetConfig.InstanceTypeConfigProperty.EbsConfiguration``.
            :param weighted_capacity: ``CfnInstanceFleetConfig.InstanceTypeConfigProperty.WeightedCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_type": instance_type,
            }
            if bid_price is not None:
                self._values["bid_price"] = bid_price
            if bid_price_as_percentage_of_on_demand_price is not None:
                self._values["bid_price_as_percentage_of_on_demand_price"] = bid_price_as_percentage_of_on_demand_price
            if configurations is not None:
                self._values["configurations"] = configurations
            if ebs_configuration is not None:
                self._values["ebs_configuration"] = ebs_configuration
            if weighted_capacity is not None:
                self._values["weighted_capacity"] = weighted_capacity

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnInstanceFleetConfig.InstanceTypeConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bid_price(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceFleetConfig.InstanceTypeConfigProperty.BidPrice``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-bidprice
            '''
            result = self._values.get("bid_price")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bid_price_as_percentage_of_on_demand_price(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceFleetConfig.InstanceTypeConfigProperty.BidPriceAsPercentageOfOnDemandPrice``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-bidpriceaspercentageofondemandprice
            '''
            result = self._values.get("bid_price_as_percentage_of_on_demand_price")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.ConfigurationProperty"]]]]:
            '''``CfnInstanceFleetConfig.InstanceTypeConfigProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.ConfigurationProperty"]]]], result)

        @builtins.property
        def ebs_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.EbsConfigurationProperty"]]:
            '''``CfnInstanceFleetConfig.InstanceTypeConfigProperty.EbsConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-ebsconfiguration
            '''
            result = self._values.get("ebs_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceFleetConfig.EbsConfigurationProperty"]], result)

        @builtins.property
        def weighted_capacity(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceFleetConfig.InstanceTypeConfigProperty.WeightedCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-instancetypeconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfig-weightedcapacity
            '''
            result = self._values.get("weighted_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceTypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"allocation_strategy": "allocationStrategy"},
    )
    class OnDemandProvisioningSpecificationProperty:
        def __init__(self, *, allocation_strategy: builtins.str) -> None:
            '''
            :param allocation_strategy: ``CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty.AllocationStrategy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ondemandprovisioningspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "allocation_strategy": allocation_strategy,
            }

        @builtins.property
        def allocation_strategy(self) -> builtins.str:
            '''``CfnInstanceFleetConfig.OnDemandProvisioningSpecificationProperty.AllocationStrategy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-ondemandprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-ondemandprovisioningspecification-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            assert result is not None, "Required property 'allocation_strategy' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnDemandProvisioningSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "timeout_action": "timeoutAction",
            "timeout_duration_minutes": "timeoutDurationMinutes",
            "allocation_strategy": "allocationStrategy",
            "block_duration_minutes": "blockDurationMinutes",
        },
    )
    class SpotProvisioningSpecificationProperty:
        def __init__(
            self,
            *,
            timeout_action: builtins.str,
            timeout_duration_minutes: jsii.Number,
            allocation_strategy: typing.Optional[builtins.str] = None,
            block_duration_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param timeout_action: ``CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty.TimeoutAction``.
            :param timeout_duration_minutes: ``CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty.TimeoutDurationMinutes``.
            :param allocation_strategy: ``CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty.AllocationStrategy``.
            :param block_duration_minutes: ``CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty.BlockDurationMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "timeout_action": timeout_action,
                "timeout_duration_minutes": timeout_duration_minutes,
            }
            if allocation_strategy is not None:
                self._values["allocation_strategy"] = allocation_strategy
            if block_duration_minutes is not None:
                self._values["block_duration_minutes"] = block_duration_minutes

        @builtins.property
        def timeout_action(self) -> builtins.str:
            '''``CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty.TimeoutAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-spotprovisioningspecification-timeoutaction
            '''
            result = self._values.get("timeout_action")
            assert result is not None, "Required property 'timeout_action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_duration_minutes(self) -> jsii.Number:
            '''``CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty.TimeoutDurationMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-spotprovisioningspecification-timeoutdurationminutes
            '''
            result = self._values.get("timeout_duration_minutes")
            assert result is not None, "Required property 'timeout_duration_minutes' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def allocation_strategy(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty.AllocationStrategy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-spotprovisioningspecification-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceFleetConfig.SpotProvisioningSpecificationProperty.BlockDurationMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-spotprovisioningspecification.html#cfn-elasticmapreduce-instancefleetconfig-spotprovisioningspecification-blockdurationminutes
            '''
            result = self._values.get("block_duration_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpotProvisioningSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfig.VolumeSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "size_in_gb": "sizeInGb",
            "volume_type": "volumeType",
            "iops": "iops",
        },
    )
    class VolumeSpecificationProperty:
        def __init__(
            self,
            *,
            size_in_gb: jsii.Number,
            volume_type: builtins.str,
            iops: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param size_in_gb: ``CfnInstanceFleetConfig.VolumeSpecificationProperty.SizeInGB``.
            :param volume_type: ``CfnInstanceFleetConfig.VolumeSpecificationProperty.VolumeType``.
            :param iops: ``CfnInstanceFleetConfig.VolumeSpecificationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "size_in_gb": size_in_gb,
                "volume_type": volume_type,
            }
            if iops is not None:
                self._values["iops"] = iops

        @builtins.property
        def size_in_gb(self) -> jsii.Number:
            '''``CfnInstanceFleetConfig.VolumeSpecificationProperty.SizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html#cfn-elasticmapreduce-instancefleetconfig-volumespecification-sizeingb
            '''
            result = self._values.get("size_in_gb")
            assert result is not None, "Required property 'size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_type(self) -> builtins.str:
            '''``CfnInstanceFleetConfig.VolumeSpecificationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html#cfn-elasticmapreduce-instancefleetconfig-volumespecification-volumetype
            '''
            result = self._values.get("volume_type")
            assert result is not None, "Required property 'volume_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceFleetConfig.VolumeSpecificationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancefleetconfig-volumespecification.html#cfn-elasticmapreduce-instancefleetconfig-volumespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-emr.CfnInstanceFleetConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_id": "clusterId",
        "instance_fleet_type": "instanceFleetType",
        "instance_type_configs": "instanceTypeConfigs",
        "launch_specifications": "launchSpecifications",
        "name": "name",
        "target_on_demand_capacity": "targetOnDemandCapacity",
        "target_spot_capacity": "targetSpotCapacity",
    },
)
class CfnInstanceFleetConfigProps:
    def __init__(
        self,
        *,
        cluster_id: builtins.str,
        instance_fleet_type: builtins.str,
        instance_type_configs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInstanceFleetConfig.InstanceTypeConfigProperty]]]] = None,
        launch_specifications: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        target_on_demand_capacity: typing.Optional[jsii.Number] = None,
        target_spot_capacity: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EMR::InstanceFleetConfig``.

        :param cluster_id: ``AWS::EMR::InstanceFleetConfig.ClusterId``.
        :param instance_fleet_type: ``AWS::EMR::InstanceFleetConfig.InstanceFleetType``.
        :param instance_type_configs: ``AWS::EMR::InstanceFleetConfig.InstanceTypeConfigs``.
        :param launch_specifications: ``AWS::EMR::InstanceFleetConfig.LaunchSpecifications``.
        :param name: ``AWS::EMR::InstanceFleetConfig.Name``.
        :param target_on_demand_capacity: ``AWS::EMR::InstanceFleetConfig.TargetOnDemandCapacity``.
        :param target_spot_capacity: ``AWS::EMR::InstanceFleetConfig.TargetSpotCapacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_id": cluster_id,
            "instance_fleet_type": instance_fleet_type,
        }
        if instance_type_configs is not None:
            self._values["instance_type_configs"] = instance_type_configs
        if launch_specifications is not None:
            self._values["launch_specifications"] = launch_specifications
        if name is not None:
            self._values["name"] = name
        if target_on_demand_capacity is not None:
            self._values["target_on_demand_capacity"] = target_on_demand_capacity
        if target_spot_capacity is not None:
            self._values["target_spot_capacity"] = target_spot_capacity

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''``AWS::EMR::InstanceFleetConfig.ClusterId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-clusterid
        '''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_fleet_type(self) -> builtins.str:
        '''``AWS::EMR::InstanceFleetConfig.InstanceFleetType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancefleettype
        '''
        result = self._values.get("instance_fleet_type")
        assert result is not None, "Required property 'instance_fleet_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type_configs(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInstanceFleetConfig.InstanceTypeConfigProperty]]]]:
        '''``AWS::EMR::InstanceFleetConfig.InstanceTypeConfigs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-instancetypeconfigs
        '''
        result = self._values.get("instance_type_configs")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInstanceFleetConfig.InstanceTypeConfigProperty]]]], result)

    @builtins.property
    def launch_specifications(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty]]:
        '''``AWS::EMR::InstanceFleetConfig.LaunchSpecifications``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-launchspecifications
        '''
        result = self._values.get("launch_specifications")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceFleetConfig.InstanceFleetProvisioningSpecificationsProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::InstanceFleetConfig.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_on_demand_capacity(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EMR::InstanceFleetConfig.TargetOnDemandCapacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-targetondemandcapacity
        '''
        result = self._values.get("target_on_demand_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_spot_capacity(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EMR::InstanceFleetConfig.TargetSpotCapacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html#cfn-elasticmapreduce-instancefleetconfig-targetspotcapacity
        '''
        result = self._values.get("target_spot_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceFleetConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInstanceGroupConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig",
):
    '''A CloudFormation ``AWS::EMR::InstanceGroupConfig``.

    :cloudformationResource: AWS::EMR::InstanceGroupConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_count: jsii.Number,
        instance_role: builtins.str,
        instance_type: builtins.str,
        job_flow_id: builtins.str,
        auto_scaling_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.AutoScalingPolicyProperty"]] = None,
        bid_price: typing.Optional[builtins.str] = None,
        configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ConfigurationProperty"]]]] = None,
        ebs_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.EbsConfigurationProperty"]] = None,
        market: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::EMR::InstanceGroupConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_count: ``AWS::EMR::InstanceGroupConfig.InstanceCount``.
        :param instance_role: ``AWS::EMR::InstanceGroupConfig.InstanceRole``.
        :param instance_type: ``AWS::EMR::InstanceGroupConfig.InstanceType``.
        :param job_flow_id: ``AWS::EMR::InstanceGroupConfig.JobFlowId``.
        :param auto_scaling_policy: ``AWS::EMR::InstanceGroupConfig.AutoScalingPolicy``.
        :param bid_price: ``AWS::EMR::InstanceGroupConfig.BidPrice``.
        :param configurations: ``AWS::EMR::InstanceGroupConfig.Configurations``.
        :param ebs_configuration: ``AWS::EMR::InstanceGroupConfig.EbsConfiguration``.
        :param market: ``AWS::EMR::InstanceGroupConfig.Market``.
        :param name: ``AWS::EMR::InstanceGroupConfig.Name``.
        '''
        props = CfnInstanceGroupConfigProps(
            instance_count=instance_count,
            instance_role=instance_role,
            instance_type=instance_type,
            job_flow_id=job_flow_id,
            auto_scaling_policy=auto_scaling_policy,
            bid_price=bid_price,
            configurations=configurations,
            ebs_configuration=ebs_configuration,
            market=market,
            name=name,
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
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        '''``AWS::EMR::InstanceGroupConfig.InstanceCount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfiginstancecount-
        '''
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        jsii.set(self, "instanceCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceRole")
    def instance_role(self) -> builtins.str:
        '''``AWS::EMR::InstanceGroupConfig.InstanceRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancerole
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceRole"))

    @instance_role.setter
    def instance_role(self, value: builtins.str) -> None:
        jsii.set(self, "instanceRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''``AWS::EMR::InstanceGroupConfig.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        jsii.set(self, "instanceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobFlowId")
    def job_flow_id(self) -> builtins.str:
        '''``AWS::EMR::InstanceGroupConfig.JobFlowId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-jobflowid
        '''
        return typing.cast(builtins.str, jsii.get(self, "jobFlowId"))

    @job_flow_id.setter
    def job_flow_id(self, value: builtins.str) -> None:
        jsii.set(self, "jobFlowId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingPolicy")
    def auto_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.AutoScalingPolicyProperty"]]:
        '''``AWS::EMR::InstanceGroupConfig.AutoScalingPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-elasticmapreduce-instancegroupconfig-autoscalingpolicy
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.AutoScalingPolicyProperty"]], jsii.get(self, "autoScalingPolicy"))

    @auto_scaling_policy.setter
    def auto_scaling_policy(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.AutoScalingPolicyProperty"]],
    ) -> None:
        jsii.set(self, "autoScalingPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bidPrice")
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::InstanceGroupConfig.BidPrice``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-bidprice
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bidPrice"))

    @bid_price.setter
    def bid_price(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bidPrice", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurations")
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ConfigurationProperty"]]]]:
        '''``AWS::EMR::InstanceGroupConfig.Configurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-configurations
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ConfigurationProperty"]]]], jsii.get(self, "configurations"))

    @configurations.setter
    def configurations(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ConfigurationProperty"]]]],
    ) -> None:
        jsii.set(self, "configurations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsConfiguration")
    def ebs_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.EbsConfigurationProperty"]]:
        '''``AWS::EMR::InstanceGroupConfig.EbsConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-ebsconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.EbsConfigurationProperty"]], jsii.get(self, "ebsConfiguration"))

    @ebs_configuration.setter
    def ebs_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.EbsConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "ebsConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="market")
    def market(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::InstanceGroupConfig.Market``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-market
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "market"))

    @market.setter
    def market(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "market", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::InstanceGroupConfig.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.AutoScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"constraints": "constraints", "rules": "rules"},
    )
    class AutoScalingPolicyProperty:
        def __init__(
            self,
            *,
            constraints: typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingConstraintsProperty"],
            rules: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingRuleProperty"]]],
        ) -> None:
            '''
            :param constraints: ``CfnInstanceGroupConfig.AutoScalingPolicyProperty.Constraints``.
            :param rules: ``CfnInstanceGroupConfig.AutoScalingPolicyProperty.Rules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-autoscalingpolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "constraints": constraints,
                "rules": rules,
            }

        @builtins.property
        def constraints(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingConstraintsProperty"]:
            '''``CfnInstanceGroupConfig.AutoScalingPolicyProperty.Constraints``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-autoscalingpolicy.html#cfn-elasticmapreduce-instancegroupconfig-autoscalingpolicy-constraints
            '''
            result = self._values.get("constraints")
            assert result is not None, "Required property 'constraints' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingConstraintsProperty"], result)

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingRuleProperty"]]]:
            '''``CfnInstanceGroupConfig.AutoScalingPolicyProperty.Rules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-autoscalingpolicy.html#cfn-elasticmapreduce-instancegroupconfig-autoscalingpolicy-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingRuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "metric_name": "metricName",
            "period": "period",
            "threshold": "threshold",
            "dimensions": "dimensions",
            "evaluation_periods": "evaluationPeriods",
            "namespace": "namespace",
            "statistic": "statistic",
            "unit": "unit",
        },
    )
    class CloudWatchAlarmDefinitionProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            metric_name: builtins.str,
            period: jsii.Number,
            threshold: jsii.Number,
            dimensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.MetricDimensionProperty"]]]] = None,
            evaluation_periods: typing.Optional[jsii.Number] = None,
            namespace: typing.Optional[builtins.str] = None,
            statistic: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param comparison_operator: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.ComparisonOperator``.
            :param metric_name: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.MetricName``.
            :param period: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Period``.
            :param threshold: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Threshold``.
            :param dimensions: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Dimensions``.
            :param evaluation_periods: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.EvaluationPeriods``.
            :param namespace: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Namespace``.
            :param statistic: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Statistic``.
            :param unit: ``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "metric_name": metric_name,
                "period": period,
                "threshold": threshold,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if evaluation_periods is not None:
                self._values["evaluation_periods"] = evaluation_periods
            if namespace is not None:
                self._values["namespace"] = namespace
            if statistic is not None:
                self._values["statistic"] = statistic
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.ComparisonOperator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.MetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def period(self) -> jsii.Number:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Period``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Threshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.MetricDimensionProperty"]]]]:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.MetricDimensionProperty"]]]], result)

        @builtins.property
        def evaluation_periods(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.EvaluationPeriods``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-evaluationperiods
            '''
            result = self._values.get("evaluation_periods")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def statistic(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Statistic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-statistic
            '''
            result = self._values.get("statistic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition.html#cfn-elasticmapreduce-instancegroupconfig-cloudwatchalarmdefinition-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchAlarmDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configuration_properties": "configurationProperties",
            "configurations": "configurations",
        },
    )
    class ConfigurationProperty:
        def __init__(
            self,
            *,
            classification: typing.Optional[builtins.str] = None,
            configuration_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ConfigurationProperty"]]]] = None,
        ) -> None:
            '''
            :param classification: ``CfnInstanceGroupConfig.ConfigurationProperty.Classification``.
            :param configuration_properties: ``CfnInstanceGroupConfig.ConfigurationProperty.ConfigurationProperties``.
            :param configurations: ``CfnInstanceGroupConfig.ConfigurationProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if classification is not None:
                self._values["classification"] = classification
            if configuration_properties is not None:
                self._values["configuration_properties"] = configuration_properties
            if configurations is not None:
                self._values["configurations"] = configurations

        @builtins.property
        def classification(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceGroupConfig.ConfigurationProperty.Classification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-classification
            '''
            result = self._values.get("classification")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configuration_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstanceGroupConfig.ConfigurationProperty.ConfigurationProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-configurationproperties
            '''
            result = self._values.get("configuration_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ConfigurationProperty"]]]]:
            '''``CfnInstanceGroupConfig.ConfigurationProperty.Configurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-cluster-configuration.html#cfn-emr-cluster-configuration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "volume_specification": "volumeSpecification",
            "volumes_per_instance": "volumesPerInstance",
        },
    )
    class EbsBlockDeviceConfigProperty:
        def __init__(
            self,
            *,
            volume_specification: typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.VolumeSpecificationProperty"],
            volumes_per_instance: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param volume_specification: ``CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty.VolumeSpecification``.
            :param volumes_per_instance: ``CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty.VolumesPerInstance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "volume_specification": volume_specification,
            }
            if volumes_per_instance is not None:
                self._values["volumes_per_instance"] = volumes_per_instance

        @builtins.property
        def volume_specification(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.VolumeSpecificationProperty"]:
            '''``CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty.VolumeSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification
            '''
            result = self._values.get("volume_specification")
            assert result is not None, "Required property 'volume_specification' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.VolumeSpecificationProperty"], result)

        @builtins.property
        def volumes_per_instance(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty.VolumesPerInstance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumesperinstance
            '''
            result = self._values.get("volumes_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.EbsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_block_device_configs": "ebsBlockDeviceConfigs",
            "ebs_optimized": "ebsOptimized",
        },
    )
    class EbsConfigurationProperty:
        def __init__(
            self,
            *,
            ebs_block_device_configs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty"]]]] = None,
            ebs_optimized: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param ebs_block_device_configs: ``CfnInstanceGroupConfig.EbsConfigurationProperty.EbsBlockDeviceConfigs``.
            :param ebs_optimized: ``CfnInstanceGroupConfig.EbsConfigurationProperty.EbsOptimized``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if ebs_block_device_configs is not None:
                self._values["ebs_block_device_configs"] = ebs_block_device_configs
            if ebs_optimized is not None:
                self._values["ebs_optimized"] = ebs_optimized

        @builtins.property
        def ebs_block_device_configs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty"]]]]:
            '''``CfnInstanceGroupConfig.EbsConfigurationProperty.EbsBlockDeviceConfigs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfigs
            '''
            result = self._values.get("ebs_block_device_configs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.EbsBlockDeviceConfigProperty"]]]], result)

        @builtins.property
        def ebs_optimized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnInstanceGroupConfig.EbsConfigurationProperty.EbsOptimized``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration.html#cfn-emr-ebsconfiguration-ebsoptimized
            '''
            result = self._values.get("ebs_optimized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnInstanceGroupConfig.MetricDimensionProperty.Key``.
            :param value: ``CfnInstanceGroupConfig.MetricDimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-metricdimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnInstanceGroupConfig.MetricDimensionProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-metricdimension.html#cfn-elasticmapreduce-instancegroupconfig-metricdimension-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnInstanceGroupConfig.MetricDimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-metricdimension.html#cfn-elasticmapreduce-instancegroupconfig-metricdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.ScalingActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "simple_scaling_policy_configuration": "simpleScalingPolicyConfiguration",
            "market": "market",
        },
    )
    class ScalingActionProperty:
        def __init__(
            self,
            *,
            simple_scaling_policy_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty"],
            market: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param simple_scaling_policy_configuration: ``CfnInstanceGroupConfig.ScalingActionProperty.SimpleScalingPolicyConfiguration``.
            :param market: ``CfnInstanceGroupConfig.ScalingActionProperty.Market``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "simple_scaling_policy_configuration": simple_scaling_policy_configuration,
            }
            if market is not None:
                self._values["market"] = market

        @builtins.property
        def simple_scaling_policy_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty"]:
            '''``CfnInstanceGroupConfig.ScalingActionProperty.SimpleScalingPolicyConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingaction.html#cfn-elasticmapreduce-instancegroupconfig-scalingaction-simplescalingpolicyconfiguration
            '''
            result = self._values.get("simple_scaling_policy_configuration")
            assert result is not None, "Required property 'simple_scaling_policy_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty"], result)

        @builtins.property
        def market(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceGroupConfig.ScalingActionProperty.Market``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingaction.html#cfn-elasticmapreduce-instancegroupconfig-scalingaction-market
            '''
            result = self._values.get("market")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.ScalingConstraintsProperty",
        jsii_struct_bases=[],
        name_mapping={"max_capacity": "maxCapacity", "min_capacity": "minCapacity"},
    )
    class ScalingConstraintsProperty:
        def __init__(
            self,
            *,
            max_capacity: jsii.Number,
            min_capacity: jsii.Number,
        ) -> None:
            '''
            :param max_capacity: ``CfnInstanceGroupConfig.ScalingConstraintsProperty.MaxCapacity``.
            :param min_capacity: ``CfnInstanceGroupConfig.ScalingConstraintsProperty.MinCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingconstraints.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_capacity": max_capacity,
                "min_capacity": min_capacity,
            }

        @builtins.property
        def max_capacity(self) -> jsii.Number:
            '''``CfnInstanceGroupConfig.ScalingConstraintsProperty.MaxCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingconstraints.html#cfn-elasticmapreduce-instancegroupconfig-scalingconstraints-maxcapacity
            '''
            result = self._values.get("max_capacity")
            assert result is not None, "Required property 'max_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_capacity(self) -> jsii.Number:
            '''``CfnInstanceGroupConfig.ScalingConstraintsProperty.MinCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingconstraints.html#cfn-elasticmapreduce-instancegroupconfig-scalingconstraints-mincapacity
            '''
            result = self._values.get("min_capacity")
            assert result is not None, "Required property 'min_capacity' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingConstraintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.ScalingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "name": "name",
            "trigger": "trigger",
            "description": "description",
        },
    )
    class ScalingRuleProperty:
        def __init__(
            self,
            *,
            action: typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingActionProperty"],
            name: builtins.str,
            trigger: typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingTriggerProperty"],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param action: ``CfnInstanceGroupConfig.ScalingRuleProperty.Action``.
            :param name: ``CfnInstanceGroupConfig.ScalingRuleProperty.Name``.
            :param trigger: ``CfnInstanceGroupConfig.ScalingRuleProperty.Trigger``.
            :param description: ``CfnInstanceGroupConfig.ScalingRuleProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
                "name": name,
                "trigger": trigger,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def action(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingActionProperty"]:
            '''``CfnInstanceGroupConfig.ScalingRuleProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html#cfn-elasticmapreduce-instancegroupconfig-scalingrule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingActionProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnInstanceGroupConfig.ScalingRuleProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html#cfn-elasticmapreduce-instancegroupconfig-scalingrule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def trigger(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingTriggerProperty"]:
            '''``CfnInstanceGroupConfig.ScalingRuleProperty.Trigger``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html#cfn-elasticmapreduce-instancegroupconfig-scalingrule-trigger
            '''
            result = self._values.get("trigger")
            assert result is not None, "Required property 'trigger' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.ScalingTriggerProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceGroupConfig.ScalingRuleProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingrule.html#cfn-elasticmapreduce-instancegroupconfig-scalingrule-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.ScalingTriggerProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_alarm_definition": "cloudWatchAlarmDefinition"},
    )
    class ScalingTriggerProperty:
        def __init__(
            self,
            *,
            cloud_watch_alarm_definition: typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty"],
        ) -> None:
            '''
            :param cloud_watch_alarm_definition: ``CfnInstanceGroupConfig.ScalingTriggerProperty.CloudWatchAlarmDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingtrigger.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cloud_watch_alarm_definition": cloud_watch_alarm_definition,
            }

        @builtins.property
        def cloud_watch_alarm_definition(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty"]:
            '''``CfnInstanceGroupConfig.ScalingTriggerProperty.CloudWatchAlarmDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-scalingtrigger.html#cfn-elasticmapreduce-instancegroupconfig-scalingtrigger-cloudwatchalarmdefinition
            '''
            result = self._values.get("cloud_watch_alarm_definition")
            assert result is not None, "Required property 'cloud_watch_alarm_definition' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInstanceGroupConfig.CloudWatchAlarmDefinitionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingTriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "scaling_adjustment": "scalingAdjustment",
            "adjustment_type": "adjustmentType",
            "cool_down": "coolDown",
        },
    )
    class SimpleScalingPolicyConfigurationProperty:
        def __init__(
            self,
            *,
            scaling_adjustment: jsii.Number,
            adjustment_type: typing.Optional[builtins.str] = None,
            cool_down: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param scaling_adjustment: ``CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty.ScalingAdjustment``.
            :param adjustment_type: ``CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty.AdjustmentType``.
            :param cool_down: ``CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty.CoolDown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "scaling_adjustment": scaling_adjustment,
            }
            if adjustment_type is not None:
                self._values["adjustment_type"] = adjustment_type
            if cool_down is not None:
                self._values["cool_down"] = cool_down

        @builtins.property
        def scaling_adjustment(self) -> jsii.Number:
            '''``CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty.ScalingAdjustment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            assert result is not None, "Required property 'scaling_adjustment' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def adjustment_type(self) -> typing.Optional[builtins.str]:
            '''``CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty.AdjustmentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration-adjustmenttype
            '''
            result = self._values.get("adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cool_down(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceGroupConfig.SimpleScalingPolicyConfigurationProperty.CoolDown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration.html#cfn-elasticmapreduce-instancegroupconfig-simplescalingpolicyconfiguration-cooldown
            '''
            result = self._values.get("cool_down")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SimpleScalingPolicyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfig.VolumeSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "size_in_gb": "sizeInGb",
            "volume_type": "volumeType",
            "iops": "iops",
        },
    )
    class VolumeSpecificationProperty:
        def __init__(
            self,
            *,
            size_in_gb: jsii.Number,
            volume_type: builtins.str,
            iops: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param size_in_gb: ``CfnInstanceGroupConfig.VolumeSpecificationProperty.SizeInGB``.
            :param volume_type: ``CfnInstanceGroupConfig.VolumeSpecificationProperty.VolumeType``.
            :param iops: ``CfnInstanceGroupConfig.VolumeSpecificationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "size_in_gb": size_in_gb,
                "volume_type": volume_type,
            }
            if iops is not None:
                self._values["iops"] = iops

        @builtins.property
        def size_in_gb(self) -> jsii.Number:
            '''``CfnInstanceGroupConfig.VolumeSpecificationProperty.SizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification-sizeingb
            '''
            result = self._values.get("size_in_gb")
            assert result is not None, "Required property 'size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_type(self) -> builtins.str:
            '''``CfnInstanceGroupConfig.VolumeSpecificationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification-volumetype
            '''
            result = self._values.get("volume_type")
            assert result is not None, "Required property 'volume_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstanceGroupConfig.VolumeSpecificationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification.html#cfn-emr-ebsconfiguration-ebsblockdeviceconfig-volumespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-emr.CfnInstanceGroupConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_count": "instanceCount",
        "instance_role": "instanceRole",
        "instance_type": "instanceType",
        "job_flow_id": "jobFlowId",
        "auto_scaling_policy": "autoScalingPolicy",
        "bid_price": "bidPrice",
        "configurations": "configurations",
        "ebs_configuration": "ebsConfiguration",
        "market": "market",
        "name": "name",
    },
)
class CfnInstanceGroupConfigProps:
    def __init__(
        self,
        *,
        instance_count: jsii.Number,
        instance_role: builtins.str,
        instance_type: builtins.str,
        job_flow_id: builtins.str,
        auto_scaling_policy: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.AutoScalingPolicyProperty]] = None,
        bid_price: typing.Optional[builtins.str] = None,
        configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.ConfigurationProperty]]]] = None,
        ebs_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.EbsConfigurationProperty]] = None,
        market: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EMR::InstanceGroupConfig``.

        :param instance_count: ``AWS::EMR::InstanceGroupConfig.InstanceCount``.
        :param instance_role: ``AWS::EMR::InstanceGroupConfig.InstanceRole``.
        :param instance_type: ``AWS::EMR::InstanceGroupConfig.InstanceType``.
        :param job_flow_id: ``AWS::EMR::InstanceGroupConfig.JobFlowId``.
        :param auto_scaling_policy: ``AWS::EMR::InstanceGroupConfig.AutoScalingPolicy``.
        :param bid_price: ``AWS::EMR::InstanceGroupConfig.BidPrice``.
        :param configurations: ``AWS::EMR::InstanceGroupConfig.Configurations``.
        :param ebs_configuration: ``AWS::EMR::InstanceGroupConfig.EbsConfiguration``.
        :param market: ``AWS::EMR::InstanceGroupConfig.Market``.
        :param name: ``AWS::EMR::InstanceGroupConfig.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_count": instance_count,
            "instance_role": instance_role,
            "instance_type": instance_type,
            "job_flow_id": job_flow_id,
        }
        if auto_scaling_policy is not None:
            self._values["auto_scaling_policy"] = auto_scaling_policy
        if bid_price is not None:
            self._values["bid_price"] = bid_price
        if configurations is not None:
            self._values["configurations"] = configurations
        if ebs_configuration is not None:
            self._values["ebs_configuration"] = ebs_configuration
        if market is not None:
            self._values["market"] = market
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def instance_count(self) -> jsii.Number:
        '''``AWS::EMR::InstanceGroupConfig.InstanceCount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfiginstancecount-
        '''
        result = self._values.get("instance_count")
        assert result is not None, "Required property 'instance_count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance_role(self) -> builtins.str:
        '''``AWS::EMR::InstanceGroupConfig.InstanceRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancerole
        '''
        result = self._values.get("instance_role")
        assert result is not None, "Required property 'instance_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''``AWS::EMR::InstanceGroupConfig.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_flow_id(self) -> builtins.str:
        '''``AWS::EMR::InstanceGroupConfig.JobFlowId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-jobflowid
        '''
        result = self._values.get("job_flow_id")
        assert result is not None, "Required property 'job_flow_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.AutoScalingPolicyProperty]]:
        '''``AWS::EMR::InstanceGroupConfig.AutoScalingPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-elasticmapreduce-instancegroupconfig-autoscalingpolicy
        '''
        result = self._values.get("auto_scaling_policy")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.AutoScalingPolicyProperty]], result)

    @builtins.property
    def bid_price(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::InstanceGroupConfig.BidPrice``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-bidprice
        '''
        result = self._values.get("bid_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.ConfigurationProperty]]]]:
        '''``AWS::EMR::InstanceGroupConfig.Configurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-configurations
        '''
        result = self._values.get("configurations")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.ConfigurationProperty]]]], result)

    @builtins.property
    def ebs_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.EbsConfigurationProperty]]:
        '''``AWS::EMR::InstanceGroupConfig.EbsConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-ebsconfiguration
        '''
        result = self._values.get("ebs_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstanceGroupConfig.EbsConfigurationProperty]], result)

    @builtins.property
    def market(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::InstanceGroupConfig.Market``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-market
        '''
        result = self._values.get("market")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::InstanceGroupConfig.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html#cfn-emr-instancegroupconfig-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceGroupConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSecurityConfiguration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-emr.CfnSecurityConfiguration",
):
    '''A CloudFormation ``AWS::EMR::SecurityConfiguration``.

    :cloudformationResource: AWS::EMR::SecurityConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        security_configuration: typing.Any,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::EMR::SecurityConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param security_configuration: ``AWS::EMR::SecurityConfiguration.SecurityConfiguration``.
        :param name: ``AWS::EMR::SecurityConfiguration.Name``.
        '''
        props = CfnSecurityConfigurationProps(
            security_configuration=security_configuration, name=name
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
    @jsii.member(jsii_name="securityConfiguration")
    def security_configuration(self) -> typing.Any:
        '''``AWS::EMR::SecurityConfiguration.SecurityConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-securityconfiguration
        '''
        return typing.cast(typing.Any, jsii.get(self, "securityConfiguration"))

    @security_configuration.setter
    def security_configuration(self, value: typing.Any) -> None:
        jsii.set(self, "securityConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::SecurityConfiguration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-emr.CfnSecurityConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={"security_configuration": "securityConfiguration", "name": "name"},
)
class CfnSecurityConfigurationProps:
    def __init__(
        self,
        *,
        security_configuration: typing.Any,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EMR::SecurityConfiguration``.

        :param security_configuration: ``AWS::EMR::SecurityConfiguration.SecurityConfiguration``.
        :param name: ``AWS::EMR::SecurityConfiguration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "security_configuration": security_configuration,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def security_configuration(self) -> typing.Any:
        '''``AWS::EMR::SecurityConfiguration.SecurityConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-securityconfiguration
        '''
        result = self._values.get("security_configuration")
        assert result is not None, "Required property 'security_configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::SecurityConfiguration.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html#cfn-emr-securityconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStep(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-emr.CfnStep",
):
    '''A CloudFormation ``AWS::EMR::Step``.

    :cloudformationResource: AWS::EMR::Step
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        action_on_failure: builtins.str,
        hadoop_jar_step: typing.Union[aws_cdk.core.IResolvable, "CfnStep.HadoopJarStepConfigProperty"],
        job_flow_id: builtins.str,
        name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::EMR::Step``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action_on_failure: ``AWS::EMR::Step.ActionOnFailure``.
        :param hadoop_jar_step: ``AWS::EMR::Step.HadoopJarStep``.
        :param job_flow_id: ``AWS::EMR::Step.JobFlowId``.
        :param name: ``AWS::EMR::Step.Name``.
        '''
        props = CfnStepProps(
            action_on_failure=action_on_failure,
            hadoop_jar_step=hadoop_jar_step,
            job_flow_id=job_flow_id,
            name=name,
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
    @jsii.member(jsii_name="actionOnFailure")
    def action_on_failure(self) -> builtins.str:
        '''``AWS::EMR::Step.ActionOnFailure``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-elasticmapreduce-step-actiononfailure
        '''
        return typing.cast(builtins.str, jsii.get(self, "actionOnFailure"))

    @action_on_failure.setter
    def action_on_failure(self, value: builtins.str) -> None:
        jsii.set(self, "actionOnFailure", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hadoopJarStep")
    def hadoop_jar_step(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnStep.HadoopJarStepConfigProperty"]:
        '''``AWS::EMR::Step.HadoopJarStep``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-elasticmapreduce-step-hadoopjarstep
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnStep.HadoopJarStepConfigProperty"], jsii.get(self, "hadoopJarStep"))

    @hadoop_jar_step.setter
    def hadoop_jar_step(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnStep.HadoopJarStepConfigProperty"],
    ) -> None:
        jsii.set(self, "hadoopJarStep", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobFlowId")
    def job_flow_id(self) -> builtins.str:
        '''``AWS::EMR::Step.JobFlowId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-elasticmapreduce-step-jobflowid
        '''
        return typing.cast(builtins.str, jsii.get(self, "jobFlowId"))

    @job_flow_id.setter
    def job_flow_id(self, value: builtins.str) -> None:
        jsii.set(self, "jobFlowId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::EMR::Step.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-elasticmapreduce-step-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnStep.HadoopJarStepConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "jar": "jar",
            "args": "args",
            "main_class": "mainClass",
            "step_properties": "stepProperties",
        },
    )
    class HadoopJarStepConfigProperty:
        def __init__(
            self,
            *,
            jar: builtins.str,
            args: typing.Optional[typing.Sequence[builtins.str]] = None,
            main_class: typing.Optional[builtins.str] = None,
            step_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnStep.KeyValueProperty"]]]] = None,
        ) -> None:
            '''
            :param jar: ``CfnStep.HadoopJarStepConfigProperty.Jar``.
            :param args: ``CfnStep.HadoopJarStepConfigProperty.Args``.
            :param main_class: ``CfnStep.HadoopJarStepConfigProperty.MainClass``.
            :param step_properties: ``CfnStep.HadoopJarStepConfigProperty.StepProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-hadoopjarstepconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "jar": jar,
            }
            if args is not None:
                self._values["args"] = args
            if main_class is not None:
                self._values["main_class"] = main_class
            if step_properties is not None:
                self._values["step_properties"] = step_properties

        @builtins.property
        def jar(self) -> builtins.str:
            '''``CfnStep.HadoopJarStepConfigProperty.Jar``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-hadoopjarstepconfig.html#cfn-elasticmapreduce-step-hadoopjarstepconfig-jar
            '''
            result = self._values.get("jar")
            assert result is not None, "Required property 'jar' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def args(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnStep.HadoopJarStepConfigProperty.Args``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-hadoopjarstepconfig.html#cfn-elasticmapreduce-step-hadoopjarstepconfig-args
            '''
            result = self._values.get("args")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def main_class(self) -> typing.Optional[builtins.str]:
            '''``CfnStep.HadoopJarStepConfigProperty.MainClass``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-hadoopjarstepconfig.html#cfn-elasticmapreduce-step-hadoopjarstepconfig-mainclass
            '''
            result = self._values.get("main_class")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def step_properties(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStep.KeyValueProperty"]]]]:
            '''``CfnStep.HadoopJarStepConfigProperty.StepProperties``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-hadoopjarstepconfig.html#cfn-elasticmapreduce-step-hadoopjarstepconfig-stepproperties
            '''
            result = self._values.get("step_properties")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStep.KeyValueProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HadoopJarStepConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-emr.CfnStep.KeyValueProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class KeyValueProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: ``CfnStep.KeyValueProperty.Key``.
            :param value: ``CfnStep.KeyValueProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-keyvalue.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnStep.KeyValueProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-keyvalue.html#cfn-elasticmapreduce-step-keyvalue-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnStep.KeyValueProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticmapreduce-step-keyvalue.html#cfn-elasticmapreduce-step-keyvalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-emr.CfnStepProps",
    jsii_struct_bases=[],
    name_mapping={
        "action_on_failure": "actionOnFailure",
        "hadoop_jar_step": "hadoopJarStep",
        "job_flow_id": "jobFlowId",
        "name": "name",
    },
)
class CfnStepProps:
    def __init__(
        self,
        *,
        action_on_failure: builtins.str,
        hadoop_jar_step: typing.Union[aws_cdk.core.IResolvable, CfnStep.HadoopJarStepConfigProperty],
        job_flow_id: builtins.str,
        name: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::EMR::Step``.

        :param action_on_failure: ``AWS::EMR::Step.ActionOnFailure``.
        :param hadoop_jar_step: ``AWS::EMR::Step.HadoopJarStep``.
        :param job_flow_id: ``AWS::EMR::Step.JobFlowId``.
        :param name: ``AWS::EMR::Step.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_on_failure": action_on_failure,
            "hadoop_jar_step": hadoop_jar_step,
            "job_flow_id": job_flow_id,
            "name": name,
        }

    @builtins.property
    def action_on_failure(self) -> builtins.str:
        '''``AWS::EMR::Step.ActionOnFailure``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-elasticmapreduce-step-actiononfailure
        '''
        result = self._values.get("action_on_failure")
        assert result is not None, "Required property 'action_on_failure' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hadoop_jar_step(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnStep.HadoopJarStepConfigProperty]:
        '''``AWS::EMR::Step.HadoopJarStep``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-elasticmapreduce-step-hadoopjarstep
        '''
        result = self._values.get("hadoop_jar_step")
        assert result is not None, "Required property 'hadoop_jar_step' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnStep.HadoopJarStepConfigProperty], result)

    @builtins.property
    def job_flow_id(self) -> builtins.str:
        '''``AWS::EMR::Step.JobFlowId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-elasticmapreduce-step-jobflowid
        '''
        result = self._values.get("job_flow_id")
        assert result is not None, "Required property 'job_flow_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::EMR::Step.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html#cfn-elasticmapreduce-step-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStepProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStudio(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-emr.CfnStudio",
):
    '''A CloudFormation ``AWS::EMR::Studio``.

    :cloudformationResource: AWS::EMR::Studio
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        auth_mode: builtins.str,
        default_s3_location: builtins.str,
        engine_security_group_id: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        workspace_security_group_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        idp_auth_url: typing.Optional[builtins.str] = None,
        idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::EMR::Studio``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param auth_mode: ``AWS::EMR::Studio.AuthMode``.
        :param default_s3_location: ``AWS::EMR::Studio.DefaultS3Location``.
        :param engine_security_group_id: ``AWS::EMR::Studio.EngineSecurityGroupId``.
        :param name: ``AWS::EMR::Studio.Name``.
        :param service_role: ``AWS::EMR::Studio.ServiceRole``.
        :param subnet_ids: ``AWS::EMR::Studio.SubnetIds``.
        :param vpc_id: ``AWS::EMR::Studio.VpcId``.
        :param workspace_security_group_id: ``AWS::EMR::Studio.WorkspaceSecurityGroupId``.
        :param description: ``AWS::EMR::Studio.Description``.
        :param idp_auth_url: ``AWS::EMR::Studio.IdpAuthUrl``.
        :param idp_relay_state_parameter_name: ``AWS::EMR::Studio.IdpRelayStateParameterName``.
        :param tags: ``AWS::EMR::Studio.Tags``.
        :param user_role: ``AWS::EMR::Studio.UserRole``.
        '''
        props = CfnStudioProps(
            auth_mode=auth_mode,
            default_s3_location=default_s3_location,
            engine_security_group_id=engine_security_group_id,
            name=name,
            service_role=service_role,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            workspace_security_group_id=workspace_security_group_id,
            description=description,
            idp_auth_url=idp_auth_url,
            idp_relay_state_parameter_name=idp_relay_state_parameter_name,
            tags=tags,
            user_role=user_role,
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
    @jsii.member(jsii_name="attrStudioId")
    def attr_studio_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: StudioId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStudioId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: Url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::EMR::Studio.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="authMode")
    def auth_mode(self) -> builtins.str:
        '''``AWS::EMR::Studio.AuthMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-authmode
        '''
        return typing.cast(builtins.str, jsii.get(self, "authMode"))

    @auth_mode.setter
    def auth_mode(self, value: builtins.str) -> None:
        jsii.set(self, "authMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultS3Location")
    def default_s3_location(self) -> builtins.str:
        '''``AWS::EMR::Studio.DefaultS3Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-defaults3location
        '''
        return typing.cast(builtins.str, jsii.get(self, "defaultS3Location"))

    @default_s3_location.setter
    def default_s3_location(self, value: builtins.str) -> None:
        jsii.set(self, "defaultS3Location", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engineSecurityGroupId")
    def engine_security_group_id(self) -> builtins.str:
        '''``AWS::EMR::Studio.EngineSecurityGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-enginesecuritygroupid
        '''
        return typing.cast(builtins.str, jsii.get(self, "engineSecurityGroupId"))

    @engine_security_group_id.setter
    def engine_security_group_id(self, value: builtins.str) -> None:
        jsii.set(self, "engineSecurityGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::EMR::Studio.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        '''``AWS::EMR::Studio.ServiceRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-servicerole
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        jsii.set(self, "serviceRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::EMR::Studio.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "subnetIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''``AWS::EMR::Studio.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-vpcid
        '''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        jsii.set(self, "vpcId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workspaceSecurityGroupId")
    def workspace_security_group_id(self) -> builtins.str:
        '''``AWS::EMR::Studio.WorkspaceSecurityGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-workspacesecuritygroupid
        '''
        return typing.cast(builtins.str, jsii.get(self, "workspaceSecurityGroupId"))

    @workspace_security_group_id.setter
    def workspace_security_group_id(self, value: builtins.str) -> None:
        jsii.set(self, "workspaceSecurityGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Studio.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idpAuthUrl")
    def idp_auth_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Studio.IdpAuthUrl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idpauthurl
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpAuthUrl"))

    @idp_auth_url.setter
    def idp_auth_url(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "idpAuthUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="idpRelayStateParameterName")
    def idp_relay_state_parameter_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Studio.IdpRelayStateParameterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idprelaystateparametername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idpRelayStateParameterName"))

    @idp_relay_state_parameter_name.setter
    def idp_relay_state_parameter_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "idpRelayStateParameterName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userRole")
    def user_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Studio.UserRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-userrole
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userRole"))

    @user_role.setter
    def user_role(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "userRole", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-emr.CfnStudioProps",
    jsii_struct_bases=[],
    name_mapping={
        "auth_mode": "authMode",
        "default_s3_location": "defaultS3Location",
        "engine_security_group_id": "engineSecurityGroupId",
        "name": "name",
        "service_role": "serviceRole",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "workspace_security_group_id": "workspaceSecurityGroupId",
        "description": "description",
        "idp_auth_url": "idpAuthUrl",
        "idp_relay_state_parameter_name": "idpRelayStateParameterName",
        "tags": "tags",
        "user_role": "userRole",
    },
)
class CfnStudioProps:
    def __init__(
        self,
        *,
        auth_mode: builtins.str,
        default_s3_location: builtins.str,
        engine_security_group_id: builtins.str,
        name: builtins.str,
        service_role: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        workspace_security_group_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        idp_auth_url: typing.Optional[builtins.str] = None,
        idp_relay_state_parameter_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EMR::Studio``.

        :param auth_mode: ``AWS::EMR::Studio.AuthMode``.
        :param default_s3_location: ``AWS::EMR::Studio.DefaultS3Location``.
        :param engine_security_group_id: ``AWS::EMR::Studio.EngineSecurityGroupId``.
        :param name: ``AWS::EMR::Studio.Name``.
        :param service_role: ``AWS::EMR::Studio.ServiceRole``.
        :param subnet_ids: ``AWS::EMR::Studio.SubnetIds``.
        :param vpc_id: ``AWS::EMR::Studio.VpcId``.
        :param workspace_security_group_id: ``AWS::EMR::Studio.WorkspaceSecurityGroupId``.
        :param description: ``AWS::EMR::Studio.Description``.
        :param idp_auth_url: ``AWS::EMR::Studio.IdpAuthUrl``.
        :param idp_relay_state_parameter_name: ``AWS::EMR::Studio.IdpRelayStateParameterName``.
        :param tags: ``AWS::EMR::Studio.Tags``.
        :param user_role: ``AWS::EMR::Studio.UserRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "auth_mode": auth_mode,
            "default_s3_location": default_s3_location,
            "engine_security_group_id": engine_security_group_id,
            "name": name,
            "service_role": service_role,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
            "workspace_security_group_id": workspace_security_group_id,
        }
        if description is not None:
            self._values["description"] = description
        if idp_auth_url is not None:
            self._values["idp_auth_url"] = idp_auth_url
        if idp_relay_state_parameter_name is not None:
            self._values["idp_relay_state_parameter_name"] = idp_relay_state_parameter_name
        if tags is not None:
            self._values["tags"] = tags
        if user_role is not None:
            self._values["user_role"] = user_role

    @builtins.property
    def auth_mode(self) -> builtins.str:
        '''``AWS::EMR::Studio.AuthMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-authmode
        '''
        result = self._values.get("auth_mode")
        assert result is not None, "Required property 'auth_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_s3_location(self) -> builtins.str:
        '''``AWS::EMR::Studio.DefaultS3Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-defaults3location
        '''
        result = self._values.get("default_s3_location")
        assert result is not None, "Required property 'default_s3_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_security_group_id(self) -> builtins.str:
        '''``AWS::EMR::Studio.EngineSecurityGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-enginesecuritygroupid
        '''
        result = self._values.get("engine_security_group_id")
        assert result is not None, "Required property 'engine_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::EMR::Studio.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''``AWS::EMR::Studio.ServiceRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-servicerole
        '''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::EMR::Studio.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''``AWS::EMR::Studio.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_security_group_id(self) -> builtins.str:
        '''``AWS::EMR::Studio.WorkspaceSecurityGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-workspacesecuritygroupid
        '''
        result = self._values.get("workspace_security_group_id")
        assert result is not None, "Required property 'workspace_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Studio.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_auth_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Studio.IdpAuthUrl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idpauthurl
        '''
        result = self._values.get("idp_auth_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_relay_state_parameter_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Studio.IdpRelayStateParameterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-idprelaystateparametername
        '''
        result = self._values.get("idp_relay_state_parameter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::EMR::Studio.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def user_role(self) -> typing.Optional[builtins.str]:
        '''``AWS::EMR::Studio.UserRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studio.html#cfn-emr-studio-userrole
        '''
        result = self._values.get("user_role")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStudioProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStudioSessionMapping(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-emr.CfnStudioSessionMapping",
):
    '''A CloudFormation ``AWS::EMR::StudioSessionMapping``.

    :cloudformationResource: AWS::EMR::StudioSessionMapping
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        identity_name: builtins.str,
        identity_type: builtins.str,
        session_policy_arn: builtins.str,
        studio_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::EMR::StudioSessionMapping``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param identity_name: ``AWS::EMR::StudioSessionMapping.IdentityName``.
        :param identity_type: ``AWS::EMR::StudioSessionMapping.IdentityType``.
        :param session_policy_arn: ``AWS::EMR::StudioSessionMapping.SessionPolicyArn``.
        :param studio_id: ``AWS::EMR::StudioSessionMapping.StudioId``.
        '''
        props = CfnStudioSessionMappingProps(
            identity_name=identity_name,
            identity_type=identity_type,
            session_policy_arn=session_policy_arn,
            studio_id=studio_id,
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
    @jsii.member(jsii_name="identityName")
    def identity_name(self) -> builtins.str:
        '''``AWS::EMR::StudioSessionMapping.IdentityName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-identityname
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityName"))

    @identity_name.setter
    def identity_name(self, value: builtins.str) -> None:
        jsii.set(self, "identityName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identityType")
    def identity_type(self) -> builtins.str:
        '''``AWS::EMR::StudioSessionMapping.IdentityType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-identitytype
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityType"))

    @identity_type.setter
    def identity_type(self, value: builtins.str) -> None:
        jsii.set(self, "identityType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sessionPolicyArn")
    def session_policy_arn(self) -> builtins.str:
        '''``AWS::EMR::StudioSessionMapping.SessionPolicyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-sessionpolicyarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "sessionPolicyArn"))

    @session_policy_arn.setter
    def session_policy_arn(self, value: builtins.str) -> None:
        jsii.set(self, "sessionPolicyArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="studioId")
    def studio_id(self) -> builtins.str:
        '''``AWS::EMR::StudioSessionMapping.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-studioid
        '''
        return typing.cast(builtins.str, jsii.get(self, "studioId"))

    @studio_id.setter
    def studio_id(self, value: builtins.str) -> None:
        jsii.set(self, "studioId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-emr.CfnStudioSessionMappingProps",
    jsii_struct_bases=[],
    name_mapping={
        "identity_name": "identityName",
        "identity_type": "identityType",
        "session_policy_arn": "sessionPolicyArn",
        "studio_id": "studioId",
    },
)
class CfnStudioSessionMappingProps:
    def __init__(
        self,
        *,
        identity_name: builtins.str,
        identity_type: builtins.str,
        session_policy_arn: builtins.str,
        studio_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::EMR::StudioSessionMapping``.

        :param identity_name: ``AWS::EMR::StudioSessionMapping.IdentityName``.
        :param identity_type: ``AWS::EMR::StudioSessionMapping.IdentityType``.
        :param session_policy_arn: ``AWS::EMR::StudioSessionMapping.SessionPolicyArn``.
        :param studio_id: ``AWS::EMR::StudioSessionMapping.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "identity_name": identity_name,
            "identity_type": identity_type,
            "session_policy_arn": session_policy_arn,
            "studio_id": studio_id,
        }

    @builtins.property
    def identity_name(self) -> builtins.str:
        '''``AWS::EMR::StudioSessionMapping.IdentityName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-identityname
        '''
        result = self._values.get("identity_name")
        assert result is not None, "Required property 'identity_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_type(self) -> builtins.str:
        '''``AWS::EMR::StudioSessionMapping.IdentityType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-identitytype
        '''
        result = self._values.get("identity_type")
        assert result is not None, "Required property 'identity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def session_policy_arn(self) -> builtins.str:
        '''``AWS::EMR::StudioSessionMapping.SessionPolicyArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-sessionpolicyarn
        '''
        result = self._values.get("session_policy_arn")
        assert result is not None, "Required property 'session_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''``AWS::EMR::StudioSessionMapping.StudioId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-studiosessionmapping.html#cfn-emr-studiosessionmapping-studioid
        '''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStudioSessionMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
    "CfnInstanceFleetConfig",
    "CfnInstanceFleetConfigProps",
    "CfnInstanceGroupConfig",
    "CfnInstanceGroupConfigProps",
    "CfnSecurityConfiguration",
    "CfnSecurityConfigurationProps",
    "CfnStep",
    "CfnStepProps",
    "CfnStudio",
    "CfnStudioProps",
    "CfnStudioSessionMapping",
    "CfnStudioSessionMappingProps",
]

publication.publish()
