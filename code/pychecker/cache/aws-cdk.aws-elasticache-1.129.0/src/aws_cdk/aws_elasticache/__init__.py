'''
# Amazon ElastiCache Construct Library

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
class CfnCacheCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnCacheCluster",
):
    '''A CloudFormation ``AWS::ElastiCache::CacheCluster``.

    :cloudformationResource: AWS::ElastiCache::CacheCluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cache_node_type: builtins.str,
        engine: builtins.str,
        num_cache_nodes: jsii.Number,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        az_mode: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        log_delivery_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.LogDeliveryConfigurationRequestProperty"]]]] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_availability_zone: typing.Optional[builtins.str] = None,
        preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::CacheCluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cache_node_type: ``AWS::ElastiCache::CacheCluster.CacheNodeType``.
        :param engine: ``AWS::ElastiCache::CacheCluster.Engine``.
        :param num_cache_nodes: ``AWS::ElastiCache::CacheCluster.NumCacheNodes``.
        :param auto_minor_version_upgrade: ``AWS::ElastiCache::CacheCluster.AutoMinorVersionUpgrade``.
        :param az_mode: ``AWS::ElastiCache::CacheCluster.AZMode``.
        :param cache_parameter_group_name: ``AWS::ElastiCache::CacheCluster.CacheParameterGroupName``.
        :param cache_security_group_names: ``AWS::ElastiCache::CacheCluster.CacheSecurityGroupNames``.
        :param cache_subnet_group_name: ``AWS::ElastiCache::CacheCluster.CacheSubnetGroupName``.
        :param cluster_name: ``AWS::ElastiCache::CacheCluster.ClusterName``.
        :param engine_version: ``AWS::ElastiCache::CacheCluster.EngineVersion``.
        :param log_delivery_configurations: ``AWS::ElastiCache::CacheCluster.LogDeliveryConfigurations``.
        :param notification_topic_arn: ``AWS::ElastiCache::CacheCluster.NotificationTopicArn``.
        :param port: ``AWS::ElastiCache::CacheCluster.Port``.
        :param preferred_availability_zone: ``AWS::ElastiCache::CacheCluster.PreferredAvailabilityZone``.
        :param preferred_availability_zones: ``AWS::ElastiCache::CacheCluster.PreferredAvailabilityZones``.
        :param preferred_maintenance_window: ``AWS::ElastiCache::CacheCluster.PreferredMaintenanceWindow``.
        :param snapshot_arns: ``AWS::ElastiCache::CacheCluster.SnapshotArns``.
        :param snapshot_name: ``AWS::ElastiCache::CacheCluster.SnapshotName``.
        :param snapshot_retention_limit: ``AWS::ElastiCache::CacheCluster.SnapshotRetentionLimit``.
        :param snapshot_window: ``AWS::ElastiCache::CacheCluster.SnapshotWindow``.
        :param tags: ``AWS::ElastiCache::CacheCluster.Tags``.
        :param vpc_security_group_ids: ``AWS::ElastiCache::CacheCluster.VpcSecurityGroupIds``.
        '''
        props = CfnCacheClusterProps(
            cache_node_type=cache_node_type,
            engine=engine,
            num_cache_nodes=num_cache_nodes,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            az_mode=az_mode,
            cache_parameter_group_name=cache_parameter_group_name,
            cache_security_group_names=cache_security_group_names,
            cache_subnet_group_name=cache_subnet_group_name,
            cluster_name=cluster_name,
            engine_version=engine_version,
            log_delivery_configurations=log_delivery_configurations,
            notification_topic_arn=notification_topic_arn,
            port=port,
            preferred_availability_zone=preferred_availability_zone,
            preferred_availability_zones=preferred_availability_zones,
            preferred_maintenance_window=preferred_maintenance_window,
            snapshot_arns=snapshot_arns,
            snapshot_name=snapshot_name,
            snapshot_retention_limit=snapshot_retention_limit,
            snapshot_window=snapshot_window,
            tags=tags,
            vpc_security_group_ids=vpc_security_group_ids,
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
    @jsii.member(jsii_name="attrConfigurationEndpointAddress")
    def attr_configuration_endpoint_address(self) -> builtins.str:
        '''
        :cloudformationAttribute: ConfigurationEndpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationEndpointAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrConfigurationEndpointPort")
    def attr_configuration_endpoint_port(self) -> builtins.str:
        '''
        :cloudformationAttribute: ConfigurationEndpoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationEndpointPort"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRedisEndpointAddress")
    def attr_redis_endpoint_address(self) -> builtins.str:
        '''
        :cloudformationAttribute: RedisEndpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRedisEndpointAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRedisEndpointPort")
    def attr_redis_endpoint_port(self) -> builtins.str:
        '''
        :cloudformationAttribute: RedisEndpoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRedisEndpointPort"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ElastiCache::CacheCluster.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheNodeType")
    def cache_node_type(self) -> builtins.str:
        '''``AWS::ElastiCache::CacheCluster.CacheNodeType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachenodetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "cacheNodeType"))

    @cache_node_type.setter
    def cache_node_type(self, value: builtins.str) -> None:
        jsii.set(self, "cacheNodeType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        '''``AWS::ElastiCache::CacheCluster.Engine``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-engine
        '''
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        jsii.set(self, "engine", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="numCacheNodes")
    def num_cache_nodes(self) -> jsii.Number:
        '''``AWS::ElastiCache::CacheCluster.NumCacheNodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-numcachenodes
        '''
        return typing.cast(jsii.Number, jsii.get(self, "numCacheNodes"))

    @num_cache_nodes.setter
    def num_cache_nodes(self, value: jsii.Number) -> None:
        jsii.set(self, "numCacheNodes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::CacheCluster.AutoMinorVersionUpgrade``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-autominorversionupgrade
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="azMode")
    def az_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.AZMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-azmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azMode"))

    @az_mode.setter
    def az_mode(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "azMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheParameterGroupName")
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.CacheParameterGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cacheparametergroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheParameterGroupName"))

    @cache_parameter_group_name.setter
    def cache_parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cacheParameterGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheSecurityGroupNames")
    def cache_security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::CacheCluster.CacheSecurityGroupNames``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachesecuritygroupnames
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cacheSecurityGroupNames"))

    @cache_security_group_names.setter
    def cache_security_group_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "cacheSecurityGroupNames", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheSubnetGroupName")
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.CacheSubnetGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachesubnetgroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheSubnetGroupName"))

    @cache_subnet_group_name.setter
    def cache_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cacheSubnetGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.ClusterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-clustername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "clusterName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.EngineVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-engineversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "engineVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.LogDeliveryConfigurationRequestProperty"]]]]:
        '''``AWS::ElastiCache::CacheCluster.LogDeliveryConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-logdeliveryconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.LogDeliveryConfigurationRequestProperty"]]]], jsii.get(self, "logDeliveryConfigurations"))

    @log_delivery_configurations.setter
    def log_delivery_configurations(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.LogDeliveryConfigurationRequestProperty"]]]],
    ) -> None:
        jsii.set(self, "logDeliveryConfigurations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationTopicArn")
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.NotificationTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-notificationtopicarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTopicArn"))

    @notification_topic_arn.setter
    def notification_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "notificationTopicArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::CacheCluster.Port``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-port
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "port", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredAvailabilityZone")
    def preferred_availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.PreferredAvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredavailabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredAvailabilityZone"))

    @preferred_availability_zone.setter
    def preferred_availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "preferredAvailabilityZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredAvailabilityZones")
    def preferred_availability_zones(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::CacheCluster.PreferredAvailabilityZones``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredavailabilityzones
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preferredAvailabilityZones"))

    @preferred_availability_zones.setter
    def preferred_availability_zones(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "preferredAvailabilityZones", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.PreferredMaintenanceWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredmaintenancewindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotArns")
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::CacheCluster.SnapshotArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snapshotArns"))

    @snapshot_arns.setter
    def snapshot_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "snapshotArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.SnapshotName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snapshotName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::CacheCluster.SnapshotRetentionLimit``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotretentionlimit
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotRetentionLimit"))

    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "snapshotRetentionLimit", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotWindow")
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.SnapshotWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotwindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotWindow"))

    @snapshot_window.setter
    def snapshot_window(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snapshotWindow", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::CacheCluster.VpcSecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-vpcsecuritygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "vpcSecurityGroupIds", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group": "logGroup"},
    )
    class CloudWatchLogsDestinationDetailsProperty:
        def __init__(self, *, log_group: builtins.str) -> None:
            '''
            :param log_group: ``CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty.LogGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "log_group": log_group,
            }

        @builtins.property
        def log_group(self) -> builtins.str:
            '''``CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty.LogGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails.html#cfn-elasticache-cachecluster-cloudwatchlogsdestinationdetails-loggroup
            '''
            result = self._values.get("log_group")
            assert result is not None, "Required property 'log_group' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsDestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnCacheCluster.DestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_details": "cloudWatchLogsDetails",
            "kinesis_firehose_details": "kinesisFirehoseDetails",
        },
    )
    class DestinationDetailsProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty"]] = None,
            kinesis_firehose_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty"]] = None,
        ) -> None:
            '''
            :param cloud_watch_logs_details: ``CfnCacheCluster.DestinationDetailsProperty.CloudWatchLogsDetails``.
            :param kinesis_firehose_details: ``CfnCacheCluster.DestinationDetailsProperty.KinesisFirehoseDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_watch_logs_details is not None:
                self._values["cloud_watch_logs_details"] = cloud_watch_logs_details
            if kinesis_firehose_details is not None:
                self._values["kinesis_firehose_details"] = kinesis_firehose_details

        @builtins.property
        def cloud_watch_logs_details(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty"]]:
            '''``CfnCacheCluster.DestinationDetailsProperty.CloudWatchLogsDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html#cfn-elasticache-cachecluster-destinationdetails-cloudwatchlogsdetails
            '''
            result = self._values.get("cloud_watch_logs_details")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.CloudWatchLogsDestinationDetailsProperty"]], result)

        @builtins.property
        def kinesis_firehose_details(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty"]]:
            '''``CfnCacheCluster.DestinationDetailsProperty.KinesisFirehoseDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-destinationdetails.html#cfn-elasticache-cachecluster-destinationdetails-kinesisfirehosedetails
            '''
            result = self._values.get("kinesis_firehose_details")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"delivery_stream": "deliveryStream"},
    )
    class KinesisFirehoseDestinationDetailsProperty:
        def __init__(self, *, delivery_stream: builtins.str) -> None:
            '''
            :param delivery_stream: ``CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty.DeliveryStream``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "delivery_stream": delivery_stream,
            }

        @builtins.property
        def delivery_stream(self) -> builtins.str:
            '''``CfnCacheCluster.KinesisFirehoseDestinationDetailsProperty.DeliveryStream``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails.html#cfn-elasticache-cachecluster-kinesisfirehosedestinationdetails-deliverystream
            '''
            result = self._values.get("delivery_stream")
            assert result is not None, "Required property 'delivery_stream' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnCacheCluster.LogDeliveryConfigurationRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_details": "destinationDetails",
            "destination_type": "destinationType",
            "log_format": "logFormat",
            "log_type": "logType",
        },
    )
    class LogDeliveryConfigurationRequestProperty:
        def __init__(
            self,
            *,
            destination_details: typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.DestinationDetailsProperty"],
            destination_type: builtins.str,
            log_format: builtins.str,
            log_type: builtins.str,
        ) -> None:
            '''
            :param destination_details: ``CfnCacheCluster.LogDeliveryConfigurationRequestProperty.DestinationDetails``.
            :param destination_type: ``CfnCacheCluster.LogDeliveryConfigurationRequestProperty.DestinationType``.
            :param log_format: ``CfnCacheCluster.LogDeliveryConfigurationRequestProperty.LogFormat``.
            :param log_type: ``CfnCacheCluster.LogDeliveryConfigurationRequestProperty.LogType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "destination_details": destination_details,
                "destination_type": destination_type,
                "log_format": log_format,
                "log_type": log_type,
            }

        @builtins.property
        def destination_details(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.DestinationDetailsProperty"]:
            '''``CfnCacheCluster.LogDeliveryConfigurationRequestProperty.DestinationDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-destinationdetails
            '''
            result = self._values.get("destination_details")
            assert result is not None, "Required property 'destination_details' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCacheCluster.DestinationDetailsProperty"], result)

        @builtins.property
        def destination_type(self) -> builtins.str:
            '''``CfnCacheCluster.LogDeliveryConfigurationRequestProperty.DestinationType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-destinationtype
            '''
            result = self._values.get("destination_type")
            assert result is not None, "Required property 'destination_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_format(self) -> builtins.str:
            '''``CfnCacheCluster.LogDeliveryConfigurationRequestProperty.LogFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-logformat
            '''
            result = self._values.get("log_format")
            assert result is not None, "Required property 'log_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_type(self) -> builtins.str:
            '''``CfnCacheCluster.LogDeliveryConfigurationRequestProperty.LogType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cachecluster-logdeliveryconfigurationrequest.html#cfn-elasticache-cachecluster-logdeliveryconfigurationrequest-logtype
            '''
            result = self._values.get("log_type")
            assert result is not None, "Required property 'log_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDeliveryConfigurationRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnCacheClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "cache_node_type": "cacheNodeType",
        "engine": "engine",
        "num_cache_nodes": "numCacheNodes",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "az_mode": "azMode",
        "cache_parameter_group_name": "cacheParameterGroupName",
        "cache_security_group_names": "cacheSecurityGroupNames",
        "cache_subnet_group_name": "cacheSubnetGroupName",
        "cluster_name": "clusterName",
        "engine_version": "engineVersion",
        "log_delivery_configurations": "logDeliveryConfigurations",
        "notification_topic_arn": "notificationTopicArn",
        "port": "port",
        "preferred_availability_zone": "preferredAvailabilityZone",
        "preferred_availability_zones": "preferredAvailabilityZones",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "snapshot_arns": "snapshotArns",
        "snapshot_name": "snapshotName",
        "snapshot_retention_limit": "snapshotRetentionLimit",
        "snapshot_window": "snapshotWindow",
        "tags": "tags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnCacheClusterProps:
    def __init__(
        self,
        *,
        cache_node_type: builtins.str,
        engine: builtins.str,
        num_cache_nodes: jsii.Number,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        az_mode: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        cluster_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        log_delivery_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnCacheCluster.LogDeliveryConfigurationRequestProperty]]]] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_availability_zone: typing.Optional[builtins.str] = None,
        preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::CacheCluster``.

        :param cache_node_type: ``AWS::ElastiCache::CacheCluster.CacheNodeType``.
        :param engine: ``AWS::ElastiCache::CacheCluster.Engine``.
        :param num_cache_nodes: ``AWS::ElastiCache::CacheCluster.NumCacheNodes``.
        :param auto_minor_version_upgrade: ``AWS::ElastiCache::CacheCluster.AutoMinorVersionUpgrade``.
        :param az_mode: ``AWS::ElastiCache::CacheCluster.AZMode``.
        :param cache_parameter_group_name: ``AWS::ElastiCache::CacheCluster.CacheParameterGroupName``.
        :param cache_security_group_names: ``AWS::ElastiCache::CacheCluster.CacheSecurityGroupNames``.
        :param cache_subnet_group_name: ``AWS::ElastiCache::CacheCluster.CacheSubnetGroupName``.
        :param cluster_name: ``AWS::ElastiCache::CacheCluster.ClusterName``.
        :param engine_version: ``AWS::ElastiCache::CacheCluster.EngineVersion``.
        :param log_delivery_configurations: ``AWS::ElastiCache::CacheCluster.LogDeliveryConfigurations``.
        :param notification_topic_arn: ``AWS::ElastiCache::CacheCluster.NotificationTopicArn``.
        :param port: ``AWS::ElastiCache::CacheCluster.Port``.
        :param preferred_availability_zone: ``AWS::ElastiCache::CacheCluster.PreferredAvailabilityZone``.
        :param preferred_availability_zones: ``AWS::ElastiCache::CacheCluster.PreferredAvailabilityZones``.
        :param preferred_maintenance_window: ``AWS::ElastiCache::CacheCluster.PreferredMaintenanceWindow``.
        :param snapshot_arns: ``AWS::ElastiCache::CacheCluster.SnapshotArns``.
        :param snapshot_name: ``AWS::ElastiCache::CacheCluster.SnapshotName``.
        :param snapshot_retention_limit: ``AWS::ElastiCache::CacheCluster.SnapshotRetentionLimit``.
        :param snapshot_window: ``AWS::ElastiCache::CacheCluster.SnapshotWindow``.
        :param tags: ``AWS::ElastiCache::CacheCluster.Tags``.
        :param vpc_security_group_ids: ``AWS::ElastiCache::CacheCluster.VpcSecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cache_node_type": cache_node_type,
            "engine": engine,
            "num_cache_nodes": num_cache_nodes,
        }
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if az_mode is not None:
            self._values["az_mode"] = az_mode
        if cache_parameter_group_name is not None:
            self._values["cache_parameter_group_name"] = cache_parameter_group_name
        if cache_security_group_names is not None:
            self._values["cache_security_group_names"] = cache_security_group_names
        if cache_subnet_group_name is not None:
            self._values["cache_subnet_group_name"] = cache_subnet_group_name
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if log_delivery_configurations is not None:
            self._values["log_delivery_configurations"] = log_delivery_configurations
        if notification_topic_arn is not None:
            self._values["notification_topic_arn"] = notification_topic_arn
        if port is not None:
            self._values["port"] = port
        if preferred_availability_zone is not None:
            self._values["preferred_availability_zone"] = preferred_availability_zone
        if preferred_availability_zones is not None:
            self._values["preferred_availability_zones"] = preferred_availability_zones
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if snapshot_arns is not None:
            self._values["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if snapshot_retention_limit is not None:
            self._values["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshot_window is not None:
            self._values["snapshot_window"] = snapshot_window
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def cache_node_type(self) -> builtins.str:
        '''``AWS::ElastiCache::CacheCluster.CacheNodeType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachenodetype
        '''
        result = self._values.get("cache_node_type")
        assert result is not None, "Required property 'cache_node_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine(self) -> builtins.str:
        '''``AWS::ElastiCache::CacheCluster.Engine``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-engine
        '''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def num_cache_nodes(self) -> jsii.Number:
        '''``AWS::ElastiCache::CacheCluster.NumCacheNodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-numcachenodes
        '''
        result = self._values.get("num_cache_nodes")
        assert result is not None, "Required property 'num_cache_nodes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::CacheCluster.AutoMinorVersionUpgrade``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def az_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.AZMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-azmode
        '''
        result = self._values.get("az_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.CacheParameterGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cacheparametergroupname
        '''
        result = self._values.get("cache_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::CacheCluster.CacheSecurityGroupNames``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachesecuritygroupnames
        '''
        result = self._values.get("cache_security_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.CacheSubnetGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachesubnetgroupname
        '''
        result = self._values.get("cache_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.ClusterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-clustername
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.EngineVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCacheCluster.LogDeliveryConfigurationRequestProperty]]]]:
        '''``AWS::ElastiCache::CacheCluster.LogDeliveryConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-logdeliveryconfigurations
        '''
        result = self._values.get("log_delivery_configurations")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCacheCluster.LogDeliveryConfigurationRequestProperty]]]], result)

    @builtins.property
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.NotificationTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-notificationtopicarn
        '''
        result = self._values.get("notification_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::CacheCluster.Port``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.PreferredAvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredavailabilityzone
        '''
        result = self._values.get("preferred_availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_availability_zones(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::CacheCluster.PreferredAvailabilityZones``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredavailabilityzones
        '''
        result = self._values.get("preferred_availability_zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.PreferredMaintenanceWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::CacheCluster.SnapshotArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotarns
        '''
        result = self._values.get("snapshot_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.SnapshotName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotname
        '''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::CacheCluster.SnapshotRetentionLimit``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotretentionlimit
        '''
        result = self._values.get("snapshot_retention_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::CacheCluster.SnapshotWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-snapshotwindow
        '''
        result = self._values.get("snapshot_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ElastiCache::CacheCluster.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::CacheCluster.VpcSecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCacheClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnGlobalReplicationGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnGlobalReplicationGroup",
):
    '''A CloudFormation ``AWS::ElastiCache::GlobalReplicationGroup``.

    :cloudformationResource: AWS::ElastiCache::GlobalReplicationGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        members: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty", aws_cdk.core.IResolvable]]],
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        cache_node_type: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        global_node_group_count: typing.Optional[jsii.Number] = None,
        global_replication_group_description: typing.Optional[builtins.str] = None,
        global_replication_group_id_suffix: typing.Optional[builtins.str] = None,
        regional_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnGlobalReplicationGroup.RegionalConfigurationProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::GlobalReplicationGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param members: ``AWS::ElastiCache::GlobalReplicationGroup.Members``.
        :param automatic_failover_enabled: ``AWS::ElastiCache::GlobalReplicationGroup.AutomaticFailoverEnabled``.
        :param cache_node_type: ``AWS::ElastiCache::GlobalReplicationGroup.CacheNodeType``.
        :param cache_parameter_group_name: ``AWS::ElastiCache::GlobalReplicationGroup.CacheParameterGroupName``.
        :param engine_version: ``AWS::ElastiCache::GlobalReplicationGroup.EngineVersion``.
        :param global_node_group_count: ``AWS::ElastiCache::GlobalReplicationGroup.GlobalNodeGroupCount``.
        :param global_replication_group_description: ``AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupDescription``.
        :param global_replication_group_id_suffix: ``AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupIdSuffix``.
        :param regional_configurations: ``AWS::ElastiCache::GlobalReplicationGroup.RegionalConfigurations``.
        '''
        props = CfnGlobalReplicationGroupProps(
            members=members,
            automatic_failover_enabled=automatic_failover_enabled,
            cache_node_type=cache_node_type,
            cache_parameter_group_name=cache_parameter_group_name,
            engine_version=engine_version,
            global_node_group_count=global_node_group_count,
            global_replication_group_description=global_replication_group_description,
            global_replication_group_id_suffix=global_replication_group_id_suffix,
            regional_configurations=regional_configurations,
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
    @jsii.member(jsii_name="attrGlobalReplicationGroupId")
    def attr_global_replication_group_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: GlobalReplicationGroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGlobalReplicationGroupId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="members")
    def members(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty", aws_cdk.core.IResolvable]]]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.Members``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-members
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty", aws_cdk.core.IResolvable]]], jsii.get(self, "members"))

    @members.setter
    def members(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "members", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automaticFailoverEnabled")
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.AutomaticFailoverEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-automaticfailoverenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "automaticFailoverEnabled"))

    @automatic_failover_enabled.setter
    def automatic_failover_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "automaticFailoverEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheNodeType")
    def cache_node_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.CacheNodeType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-cachenodetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheNodeType"))

    @cache_node_type.setter
    def cache_node_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cacheNodeType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheParameterGroupName")
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.CacheParameterGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-cacheparametergroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheParameterGroupName"))

    @cache_parameter_group_name.setter
    def cache_parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cacheParameterGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.EngineVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-engineversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "engineVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalNodeGroupCount")
    def global_node_group_count(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.GlobalNodeGroupCount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalnodegroupcount
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "globalNodeGroupCount"))

    @global_node_group_count.setter
    def global_node_group_count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "globalNodeGroupCount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalReplicationGroupDescription")
    def global_replication_group_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupDescription"))

    @global_replication_group_description.setter
    def global_replication_group_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "globalReplicationGroupDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalReplicationGroupIdSuffix")
    def global_replication_group_id_suffix(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupIdSuffix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupidsuffix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupIdSuffix"))

    @global_replication_group_id_suffix.setter
    def global_replication_group_id_suffix(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "globalReplicationGroupIdSuffix", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="regionalConfigurations")
    def regional_configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGlobalReplicationGroup.RegionalConfigurationProperty"]]]]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.RegionalConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-regionalconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGlobalReplicationGroup.RegionalConfigurationProperty"]]]], jsii.get(self, "regionalConfigurations"))

    @regional_configurations.setter
    def regional_configurations(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGlobalReplicationGroup.RegionalConfigurationProperty"]]]],
    ) -> None:
        jsii.set(self, "regionalConfigurations", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty",
        jsii_struct_bases=[],
        name_mapping={
            "replication_group_id": "replicationGroupId",
            "replication_group_region": "replicationGroupRegion",
            "role": "role",
        },
    )
    class GlobalReplicationGroupMemberProperty:
        def __init__(
            self,
            *,
            replication_group_id: typing.Optional[builtins.str] = None,
            replication_group_region: typing.Optional[builtins.str] = None,
            role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param replication_group_id: ``CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty.ReplicationGroupId``.
            :param replication_group_region: ``CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty.ReplicationGroupRegion``.
            :param role: ``CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty.Role``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if replication_group_id is not None:
                self._values["replication_group_id"] = replication_group_id
            if replication_group_region is not None:
                self._values["replication_group_region"] = replication_group_region
            if role is not None:
                self._values["role"] = role

        @builtins.property
        def replication_group_id(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty.ReplicationGroupId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-replicationgroupid
            '''
            result = self._values.get("replication_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replication_group_region(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty.ReplicationGroupRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-replicationgroupregion
            '''
            result = self._values.get("replication_group_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty.Role``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-globalreplicationgroupmember.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupmember-role
            '''
            result = self._values.get("role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlobalReplicationGroupMemberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnGlobalReplicationGroup.RegionalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "replication_group_id": "replicationGroupId",
            "replication_group_region": "replicationGroupRegion",
            "resharding_configurations": "reshardingConfigurations",
        },
    )
    class RegionalConfigurationProperty:
        def __init__(
            self,
            *,
            replication_group_id: typing.Optional[builtins.str] = None,
            replication_group_region: typing.Optional[builtins.str] = None,
            resharding_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnGlobalReplicationGroup.ReshardingConfigurationProperty"]]]] = None,
        ) -> None:
            '''
            :param replication_group_id: ``CfnGlobalReplicationGroup.RegionalConfigurationProperty.ReplicationGroupId``.
            :param replication_group_region: ``CfnGlobalReplicationGroup.RegionalConfigurationProperty.ReplicationGroupRegion``.
            :param resharding_configurations: ``CfnGlobalReplicationGroup.RegionalConfigurationProperty.ReshardingConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if replication_group_id is not None:
                self._values["replication_group_id"] = replication_group_id
            if replication_group_region is not None:
                self._values["replication_group_region"] = replication_group_region
            if resharding_configurations is not None:
                self._values["resharding_configurations"] = resharding_configurations

        @builtins.property
        def replication_group_id(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalReplicationGroup.RegionalConfigurationProperty.ReplicationGroupId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-replicationgroupid
            '''
            result = self._values.get("replication_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replication_group_region(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalReplicationGroup.RegionalConfigurationProperty.ReplicationGroupRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-replicationgroupregion
            '''
            result = self._values.get("replication_group_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resharding_configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGlobalReplicationGroup.ReshardingConfigurationProperty"]]]]:
            '''``CfnGlobalReplicationGroup.RegionalConfigurationProperty.ReshardingConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-regionalconfiguration.html#cfn-elasticache-globalreplicationgroup-regionalconfiguration-reshardingconfigurations
            '''
            result = self._values.get("resharding_configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGlobalReplicationGroup.ReshardingConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegionalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnGlobalReplicationGroup.ReshardingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "node_group_id": "nodeGroupId",
            "preferred_availability_zones": "preferredAvailabilityZones",
        },
    )
    class ReshardingConfigurationProperty:
        def __init__(
            self,
            *,
            node_group_id: typing.Optional[builtins.str] = None,
            preferred_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param node_group_id: ``CfnGlobalReplicationGroup.ReshardingConfigurationProperty.NodeGroupId``.
            :param preferred_availability_zones: ``CfnGlobalReplicationGroup.ReshardingConfigurationProperty.PreferredAvailabilityZones``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if node_group_id is not None:
                self._values["node_group_id"] = node_group_id
            if preferred_availability_zones is not None:
                self._values["preferred_availability_zones"] = preferred_availability_zones

        @builtins.property
        def node_group_id(self) -> typing.Optional[builtins.str]:
            '''``CfnGlobalReplicationGroup.ReshardingConfigurationProperty.NodeGroupId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-nodegroupid
            '''
            result = self._values.get("node_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preferred_availability_zones(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnGlobalReplicationGroup.ReshardingConfigurationProperty.PreferredAvailabilityZones``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-globalreplicationgroup-reshardingconfiguration.html#cfn-elasticache-globalreplicationgroup-reshardingconfiguration-preferredavailabilityzones
            '''
            result = self._values.get("preferred_availability_zones")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReshardingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnGlobalReplicationGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "members": "members",
        "automatic_failover_enabled": "automaticFailoverEnabled",
        "cache_node_type": "cacheNodeType",
        "cache_parameter_group_name": "cacheParameterGroupName",
        "engine_version": "engineVersion",
        "global_node_group_count": "globalNodeGroupCount",
        "global_replication_group_description": "globalReplicationGroupDescription",
        "global_replication_group_id_suffix": "globalReplicationGroupIdSuffix",
        "regional_configurations": "regionalConfigurations",
    },
)
class CfnGlobalReplicationGroupProps:
    def __init__(
        self,
        *,
        members: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty, aws_cdk.core.IResolvable]]],
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        cache_node_type: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        global_node_group_count: typing.Optional[jsii.Number] = None,
        global_replication_group_description: typing.Optional[builtins.str] = None,
        global_replication_group_id_suffix: typing.Optional[builtins.str] = None,
        regional_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnGlobalReplicationGroup.RegionalConfigurationProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::GlobalReplicationGroup``.

        :param members: ``AWS::ElastiCache::GlobalReplicationGroup.Members``.
        :param automatic_failover_enabled: ``AWS::ElastiCache::GlobalReplicationGroup.AutomaticFailoverEnabled``.
        :param cache_node_type: ``AWS::ElastiCache::GlobalReplicationGroup.CacheNodeType``.
        :param cache_parameter_group_name: ``AWS::ElastiCache::GlobalReplicationGroup.CacheParameterGroupName``.
        :param engine_version: ``AWS::ElastiCache::GlobalReplicationGroup.EngineVersion``.
        :param global_node_group_count: ``AWS::ElastiCache::GlobalReplicationGroup.GlobalNodeGroupCount``.
        :param global_replication_group_description: ``AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupDescription``.
        :param global_replication_group_id_suffix: ``AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupIdSuffix``.
        :param regional_configurations: ``AWS::ElastiCache::GlobalReplicationGroup.RegionalConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "members": members,
        }
        if automatic_failover_enabled is not None:
            self._values["automatic_failover_enabled"] = automatic_failover_enabled
        if cache_node_type is not None:
            self._values["cache_node_type"] = cache_node_type
        if cache_parameter_group_name is not None:
            self._values["cache_parameter_group_name"] = cache_parameter_group_name
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if global_node_group_count is not None:
            self._values["global_node_group_count"] = global_node_group_count
        if global_replication_group_description is not None:
            self._values["global_replication_group_description"] = global_replication_group_description
        if global_replication_group_id_suffix is not None:
            self._values["global_replication_group_id_suffix"] = global_replication_group_id_suffix
        if regional_configurations is not None:
            self._values["regional_configurations"] = regional_configurations

    @builtins.property
    def members(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty, aws_cdk.core.IResolvable]]]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.Members``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-members
        '''
        result = self._values.get("members")
        assert result is not None, "Required property 'members' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnGlobalReplicationGroup.GlobalReplicationGroupMemberProperty, aws_cdk.core.IResolvable]]], result)

    @builtins.property
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.AutomaticFailoverEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-automaticfailoverenabled
        '''
        result = self._values.get("automatic_failover_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def cache_node_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.CacheNodeType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-cachenodetype
        '''
        result = self._values.get("cache_node_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.CacheParameterGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-cacheparametergroupname
        '''
        result = self._values.get("cache_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.EngineVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_node_group_count(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.GlobalNodeGroupCount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalnodegroupcount
        '''
        result = self._values.get("global_node_group_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def global_replication_group_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupdescription
        '''
        result = self._values.get("global_replication_group_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_replication_group_id_suffix(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.GlobalReplicationGroupIdSuffix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-globalreplicationgroupidsuffix
        '''
        result = self._values.get("global_replication_group_id_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regional_configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnGlobalReplicationGroup.RegionalConfigurationProperty]]]]:
        '''``AWS::ElastiCache::GlobalReplicationGroup.RegionalConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-globalreplicationgroup.html#cfn-elasticache-globalreplicationgroup-regionalconfigurations
        '''
        result = self._values.get("regional_configurations")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnGlobalReplicationGroup.RegionalConfigurationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGlobalReplicationGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnParameterGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnParameterGroup",
):
    '''A CloudFormation ``AWS::ElastiCache::ParameterGroup``.

    :cloudformationResource: AWS::ElastiCache::ParameterGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cache_parameter_group_family: builtins.str,
        description: builtins.str,
        properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::ParameterGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cache_parameter_group_family: ``AWS::ElastiCache::ParameterGroup.CacheParameterGroupFamily``.
        :param description: ``AWS::ElastiCache::ParameterGroup.Description``.
        :param properties: ``AWS::ElastiCache::ParameterGroup.Properties``.
        :param tags: ``AWS::ElastiCache::ParameterGroup.Tags``.
        '''
        props = CfnParameterGroupProps(
            cache_parameter_group_family=cache_parameter_group_family,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ElastiCache::ParameterGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheParameterGroupFamily")
    def cache_parameter_group_family(self) -> builtins.str:
        '''``AWS::ElastiCache::ParameterGroup.CacheParameterGroupFamily``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-cacheparametergroupfamily
        '''
        return typing.cast(builtins.str, jsii.get(self, "cacheParameterGroupFamily"))

    @cache_parameter_group_family.setter
    def cache_parameter_group_family(self, value: builtins.str) -> None:
        jsii.set(self, "cacheParameterGroupFamily", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''``AWS::ElastiCache::ParameterGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="properties")
    def properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::ElastiCache::ParameterGroup.Properties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-properties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "properties"))

    @properties.setter
    def properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "properties", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "cache_parameter_group_family": "cacheParameterGroupFamily",
        "description": "description",
        "properties": "properties",
        "tags": "tags",
    },
)
class CfnParameterGroupProps:
    def __init__(
        self,
        *,
        cache_parameter_group_family: builtins.str,
        description: builtins.str,
        properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::ParameterGroup``.

        :param cache_parameter_group_family: ``AWS::ElastiCache::ParameterGroup.CacheParameterGroupFamily``.
        :param description: ``AWS::ElastiCache::ParameterGroup.Description``.
        :param properties: ``AWS::ElastiCache::ParameterGroup.Properties``.
        :param tags: ``AWS::ElastiCache::ParameterGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cache_parameter_group_family": cache_parameter_group_family,
            "description": description,
        }
        if properties is not None:
            self._values["properties"] = properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cache_parameter_group_family(self) -> builtins.str:
        '''``AWS::ElastiCache::ParameterGroup.CacheParameterGroupFamily``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-cacheparametergroupfamily
        '''
        result = self._values.get("cache_parameter_group_family")
        assert result is not None, "Required property 'cache_parameter_group_family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''``AWS::ElastiCache::ParameterGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::ElastiCache::ParameterGroup.Properties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ElastiCache::ParameterGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html#cfn-elasticache-parametergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnReplicationGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnReplicationGroup",
):
    '''A CloudFormation ``AWS::ElastiCache::ReplicationGroup``.

    :cloudformationResource: AWS::ElastiCache::ReplicationGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        replication_group_description: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        cache_node_type: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        global_replication_group_id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_delivery_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.LogDeliveryConfigurationRequestProperty"]]]] = None,
        multi_az_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        node_group_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.NodeGroupConfigurationProperty"]]]] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        num_cache_clusters: typing.Optional[jsii.Number] = None,
        num_node_groups: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_cache_cluster_a_zs: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        primary_cluster_id: typing.Optional[builtins.str] = None,
        replicas_per_node_group: typing.Optional[jsii.Number] = None,
        replication_group_id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshotting_cluster_id: typing.Optional[builtins.str] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::ReplicationGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param replication_group_description: ``AWS::ElastiCache::ReplicationGroup.ReplicationGroupDescription``.
        :param at_rest_encryption_enabled: ``AWS::ElastiCache::ReplicationGroup.AtRestEncryptionEnabled``.
        :param auth_token: ``AWS::ElastiCache::ReplicationGroup.AuthToken``.
        :param automatic_failover_enabled: ``AWS::ElastiCache::ReplicationGroup.AutomaticFailoverEnabled``.
        :param auto_minor_version_upgrade: ``AWS::ElastiCache::ReplicationGroup.AutoMinorVersionUpgrade``.
        :param cache_node_type: ``AWS::ElastiCache::ReplicationGroup.CacheNodeType``.
        :param cache_parameter_group_name: ``AWS::ElastiCache::ReplicationGroup.CacheParameterGroupName``.
        :param cache_security_group_names: ``AWS::ElastiCache::ReplicationGroup.CacheSecurityGroupNames``.
        :param cache_subnet_group_name: ``AWS::ElastiCache::ReplicationGroup.CacheSubnetGroupName``.
        :param engine: ``AWS::ElastiCache::ReplicationGroup.Engine``.
        :param engine_version: ``AWS::ElastiCache::ReplicationGroup.EngineVersion``.
        :param global_replication_group_id: ``AWS::ElastiCache::ReplicationGroup.GlobalReplicationGroupId``.
        :param kms_key_id: ``AWS::ElastiCache::ReplicationGroup.KmsKeyId``.
        :param log_delivery_configurations: ``AWS::ElastiCache::ReplicationGroup.LogDeliveryConfigurations``.
        :param multi_az_enabled: ``AWS::ElastiCache::ReplicationGroup.MultiAZEnabled``.
        :param node_group_configuration: ``AWS::ElastiCache::ReplicationGroup.NodeGroupConfiguration``.
        :param notification_topic_arn: ``AWS::ElastiCache::ReplicationGroup.NotificationTopicArn``.
        :param num_cache_clusters: ``AWS::ElastiCache::ReplicationGroup.NumCacheClusters``.
        :param num_node_groups: ``AWS::ElastiCache::ReplicationGroup.NumNodeGroups``.
        :param port: ``AWS::ElastiCache::ReplicationGroup.Port``.
        :param preferred_cache_cluster_a_zs: ``AWS::ElastiCache::ReplicationGroup.PreferredCacheClusterAZs``.
        :param preferred_maintenance_window: ``AWS::ElastiCache::ReplicationGroup.PreferredMaintenanceWindow``.
        :param primary_cluster_id: ``AWS::ElastiCache::ReplicationGroup.PrimaryClusterId``.
        :param replicas_per_node_group: ``AWS::ElastiCache::ReplicationGroup.ReplicasPerNodeGroup``.
        :param replication_group_id: ``AWS::ElastiCache::ReplicationGroup.ReplicationGroupId``.
        :param security_group_ids: ``AWS::ElastiCache::ReplicationGroup.SecurityGroupIds``.
        :param snapshot_arns: ``AWS::ElastiCache::ReplicationGroup.SnapshotArns``.
        :param snapshot_name: ``AWS::ElastiCache::ReplicationGroup.SnapshotName``.
        :param snapshot_retention_limit: ``AWS::ElastiCache::ReplicationGroup.SnapshotRetentionLimit``.
        :param snapshotting_cluster_id: ``AWS::ElastiCache::ReplicationGroup.SnapshottingClusterId``.
        :param snapshot_window: ``AWS::ElastiCache::ReplicationGroup.SnapshotWindow``.
        :param tags: ``AWS::ElastiCache::ReplicationGroup.Tags``.
        :param transit_encryption_enabled: ``AWS::ElastiCache::ReplicationGroup.TransitEncryptionEnabled``.
        :param user_group_ids: ``AWS::ElastiCache::ReplicationGroup.UserGroupIds``.
        '''
        props = CfnReplicationGroupProps(
            replication_group_description=replication_group_description,
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            auth_token=auth_token,
            automatic_failover_enabled=automatic_failover_enabled,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            cache_node_type=cache_node_type,
            cache_parameter_group_name=cache_parameter_group_name,
            cache_security_group_names=cache_security_group_names,
            cache_subnet_group_name=cache_subnet_group_name,
            engine=engine,
            engine_version=engine_version,
            global_replication_group_id=global_replication_group_id,
            kms_key_id=kms_key_id,
            log_delivery_configurations=log_delivery_configurations,
            multi_az_enabled=multi_az_enabled,
            node_group_configuration=node_group_configuration,
            notification_topic_arn=notification_topic_arn,
            num_cache_clusters=num_cache_clusters,
            num_node_groups=num_node_groups,
            port=port,
            preferred_cache_cluster_a_zs=preferred_cache_cluster_a_zs,
            preferred_maintenance_window=preferred_maintenance_window,
            primary_cluster_id=primary_cluster_id,
            replicas_per_node_group=replicas_per_node_group,
            replication_group_id=replication_group_id,
            security_group_ids=security_group_ids,
            snapshot_arns=snapshot_arns,
            snapshot_name=snapshot_name,
            snapshot_retention_limit=snapshot_retention_limit,
            snapshotting_cluster_id=snapshotting_cluster_id,
            snapshot_window=snapshot_window,
            tags=tags,
            transit_encryption_enabled=transit_encryption_enabled,
            user_group_ids=user_group_ids,
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
    @jsii.member(jsii_name="attrConfigurationEndPointAddress")
    def attr_configuration_end_point_address(self) -> builtins.str:
        '''
        :cloudformationAttribute: ConfigurationEndPoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationEndPointAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrConfigurationEndPointPort")
    def attr_configuration_end_point_port(self) -> builtins.str:
        '''
        :cloudformationAttribute: ConfigurationEndPoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationEndPointPort"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPrimaryEndPointAddress")
    def attr_primary_end_point_address(self) -> builtins.str:
        '''
        :cloudformationAttribute: PrimaryEndPoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrimaryEndPointAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPrimaryEndPointPort")
    def attr_primary_end_point_port(self) -> builtins.str:
        '''
        :cloudformationAttribute: PrimaryEndPoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrimaryEndPointPort"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrReadEndPointAddresses")
    def attr_read_end_point_addresses(self) -> builtins.str:
        '''
        :cloudformationAttribute: ReadEndPoint.Addresses
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReadEndPointAddresses"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrReadEndPointAddressesList")
    def attr_read_end_point_addresses_list(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: ReadEndPoint.Addresses.List
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrReadEndPointAddressesList"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrReadEndPointPorts")
    def attr_read_end_point_ports(self) -> builtins.str:
        '''
        :cloudformationAttribute: ReadEndPoint.Ports
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReadEndPointPorts"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrReadEndPointPortsList")
    def attr_read_end_point_ports_list(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: ReadEndPoint.Ports.List
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrReadEndPointPortsList"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrReaderEndPointAddress")
    def attr_reader_end_point_address(self) -> builtins.str:
        '''
        :cloudformationAttribute: ReaderEndPoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReaderEndPointAddress"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrReaderEndPointPort")
    def attr_reader_end_point_port(self) -> builtins.str:
        '''
        :cloudformationAttribute: ReaderEndPoint.Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReaderEndPointPort"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ElastiCache::ReplicationGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicationGroupDescription")
    def replication_group_description(self) -> builtins.str:
        '''``AWS::ElastiCache::ReplicationGroup.ReplicationGroupDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicationgroupdescription
        '''
        return typing.cast(builtins.str, jsii.get(self, "replicationGroupDescription"))

    @replication_group_description.setter
    def replication_group_description(self, value: builtins.str) -> None:
        jsii.set(self, "replicationGroupDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.AtRestEncryptionEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-atrestencryptionenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "atRestEncryptionEnabled"))

    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "atRestEncryptionEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.AuthToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-authtoken
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "authToken", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automaticFailoverEnabled")
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.AutomaticFailoverEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-automaticfailoverenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "automaticFailoverEnabled"))

    @automatic_failover_enabled.setter
    def automatic_failover_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "automaticFailoverEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.AutoMinorVersionUpgrade``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-autominorversionupgrade
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheNodeType")
    def cache_node_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.CacheNodeType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachenodetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheNodeType"))

    @cache_node_type.setter
    def cache_node_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cacheNodeType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheParameterGroupName")
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.CacheParameterGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cacheparametergroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheParameterGroupName"))

    @cache_parameter_group_name.setter
    def cache_parameter_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cacheParameterGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheSecurityGroupNames")
    def cache_security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.CacheSecurityGroupNames``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachesecuritygroupnames
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cacheSecurityGroupNames"))

    @cache_security_group_names.setter
    def cache_security_group_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "cacheSecurityGroupNames", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheSubnetGroupName")
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.CacheSubnetGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachesubnetgroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheSubnetGroupName"))

    @cache_subnet_group_name.setter
    def cache_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cacheSubnetGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engine")
    def engine(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.Engine``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-engine
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "engine", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.EngineVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-engineversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "engineVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="globalReplicationGroupId")
    def global_replication_group_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.GlobalReplicationGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-globalreplicationgroupid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "globalReplicationGroupId"))

    @global_replication_group_id.setter
    def global_replication_group_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "globalReplicationGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.LogDeliveryConfigurationRequestProperty"]]]]:
        '''``AWS::ElastiCache::ReplicationGroup.LogDeliveryConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-logdeliveryconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.LogDeliveryConfigurationRequestProperty"]]]], jsii.get(self, "logDeliveryConfigurations"))

    @log_delivery_configurations.setter
    def log_delivery_configurations(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.LogDeliveryConfigurationRequestProperty"]]]],
    ) -> None:
        jsii.set(self, "logDeliveryConfigurations", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="multiAzEnabled")
    def multi_az_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.MultiAZEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-multiazenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "multiAzEnabled"))

    @multi_az_enabled.setter
    def multi_az_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "multiAzEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nodeGroupConfiguration")
    def node_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.NodeGroupConfigurationProperty"]]]]:
        '''``AWS::ElastiCache::ReplicationGroup.NodeGroupConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-nodegroupconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.NodeGroupConfigurationProperty"]]]], jsii.get(self, "nodeGroupConfiguration"))

    @node_group_configuration.setter
    def node_group_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.NodeGroupConfigurationProperty"]]]],
    ) -> None:
        jsii.set(self, "nodeGroupConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationTopicArn")
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.NotificationTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-notificationtopicarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTopicArn"))

    @notification_topic_arn.setter
    def notification_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "notificationTopicArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="numCacheClusters")
    def num_cache_clusters(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.NumCacheClusters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-numcacheclusters
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numCacheClusters"))

    @num_cache_clusters.setter
    def num_cache_clusters(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "numCacheClusters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="numNodeGroups")
    def num_node_groups(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.NumNodeGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-numnodegroups
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numNodeGroups"))

    @num_node_groups.setter
    def num_node_groups(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "numNodeGroups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.Port``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-port
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "port", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredCacheClusterAZs")
    def preferred_cache_cluster_a_zs(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.PreferredCacheClusterAZs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-preferredcacheclusterazs
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "preferredCacheClusterAZs"))

    @preferred_cache_cluster_a_zs.setter
    def preferred_cache_cluster_a_zs(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "preferredCacheClusterAZs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.PreferredMaintenanceWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-preferredmaintenancewindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="primaryClusterId")
    def primary_cluster_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.PrimaryClusterId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-primaryclusterid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryClusterId"))

    @primary_cluster_id.setter
    def primary_cluster_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "primaryClusterId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.ReplicasPerNodeGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicaspernodegroup
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicasPerNodeGroup"))

    @replicas_per_node_group.setter
    def replicas_per_node_group(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "replicasPerNodeGroup", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicationGroupId")
    def replication_group_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.ReplicationGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicationgroupid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationGroupId"))

    @replication_group_id.setter
    def replication_group_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "replicationGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-securitygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotArns")
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshotArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snapshotArns"))

    @snapshot_arns.setter
    def snapshot_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "snapshotArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshotName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snapshotName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshotRetentionLimit``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotretentionlimit
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotRetentionLimit"))

    @snapshot_retention_limit.setter
    def snapshot_retention_limit(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "snapshotRetentionLimit", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshottingClusterId")
    def snapshotting_cluster_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshottingClusterId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshottingclusterid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshottingClusterId"))

    @snapshotting_cluster_id.setter
    def snapshotting_cluster_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snapshottingClusterId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snapshotWindow")
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshotWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotwindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotWindow"))

    @snapshot_window.setter
    def snapshot_window(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snapshotWindow", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.TransitEncryptionEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-transitencryptionenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "transitEncryptionEnabled"))

    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "transitEncryptionEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userGroupIds")
    def user_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.UserGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-usergroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "userGroupIds"))

    @user_group_ids.setter
    def user_group_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "userGroupIds", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group": "logGroup"},
    )
    class CloudWatchLogsDestinationDetailsProperty:
        def __init__(self, *, log_group: builtins.str) -> None:
            '''
            :param log_group: ``CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty.LogGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-cloudwatchlogsdestinationdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "log_group": log_group,
            }

        @builtins.property
        def log_group(self) -> builtins.str:
            '''``CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty.LogGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-cloudwatchlogsdestinationdetails.html#cfn-elasticache-replicationgroup-cloudwatchlogsdestinationdetails-loggroup
            '''
            result = self._values.get("log_group")
            assert result is not None, "Required property 'log_group' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsDestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnReplicationGroup.DestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_details": "cloudWatchLogsDetails",
            "kinesis_firehose_details": "kinesisFirehoseDetails",
        },
    )
    class DestinationDetailsProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty"]] = None,
            kinesis_firehose_details: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty"]] = None,
        ) -> None:
            '''
            :param cloud_watch_logs_details: ``CfnReplicationGroup.DestinationDetailsProperty.CloudWatchLogsDetails``.
            :param kinesis_firehose_details: ``CfnReplicationGroup.DestinationDetailsProperty.KinesisFirehoseDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_watch_logs_details is not None:
                self._values["cloud_watch_logs_details"] = cloud_watch_logs_details
            if kinesis_firehose_details is not None:
                self._values["kinesis_firehose_details"] = kinesis_firehose_details

        @builtins.property
        def cloud_watch_logs_details(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty"]]:
            '''``CfnReplicationGroup.DestinationDetailsProperty.CloudWatchLogsDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html#cfn-elasticache-replicationgroup-destinationdetails-cloudwatchlogsdetails
            '''
            result = self._values.get("cloud_watch_logs_details")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.CloudWatchLogsDestinationDetailsProperty"]], result)

        @builtins.property
        def kinesis_firehose_details(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty"]]:
            '''``CfnReplicationGroup.DestinationDetailsProperty.KinesisFirehoseDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-destinationdetails.html#cfn-elasticache-replicationgroup-destinationdetails-kinesisfirehosedetails
            '''
            result = self._values.get("kinesis_firehose_details")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"delivery_stream": "deliveryStream"},
    )
    class KinesisFirehoseDestinationDetailsProperty:
        def __init__(self, *, delivery_stream: builtins.str) -> None:
            '''
            :param delivery_stream: ``CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty.DeliveryStream``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-kinesisfirehosedestinationdetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "delivery_stream": delivery_stream,
            }

        @builtins.property
        def delivery_stream(self) -> builtins.str:
            '''``CfnReplicationGroup.KinesisFirehoseDestinationDetailsProperty.DeliveryStream``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-kinesisfirehosedestinationdetails.html#cfn-elasticache-replicationgroup-kinesisfirehosedestinationdetails-deliverystream
            '''
            result = self._values.get("delivery_stream")
            assert result is not None, "Required property 'delivery_stream' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnReplicationGroup.LogDeliveryConfigurationRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_details": "destinationDetails",
            "destination_type": "destinationType",
            "log_format": "logFormat",
            "log_type": "logType",
        },
    )
    class LogDeliveryConfigurationRequestProperty:
        def __init__(
            self,
            *,
            destination_details: typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.DestinationDetailsProperty"],
            destination_type: builtins.str,
            log_format: builtins.str,
            log_type: builtins.str,
        ) -> None:
            '''
            :param destination_details: ``CfnReplicationGroup.LogDeliveryConfigurationRequestProperty.DestinationDetails``.
            :param destination_type: ``CfnReplicationGroup.LogDeliveryConfigurationRequestProperty.DestinationType``.
            :param log_format: ``CfnReplicationGroup.LogDeliveryConfigurationRequestProperty.LogFormat``.
            :param log_type: ``CfnReplicationGroup.LogDeliveryConfigurationRequestProperty.LogType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "destination_details": destination_details,
                "destination_type": destination_type,
                "log_format": log_format,
                "log_type": log_type,
            }

        @builtins.property
        def destination_details(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.DestinationDetailsProperty"]:
            '''``CfnReplicationGroup.LogDeliveryConfigurationRequestProperty.DestinationDetails``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationdetails
            '''
            result = self._values.get("destination_details")
            assert result is not None, "Required property 'destination_details' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnReplicationGroup.DestinationDetailsProperty"], result)

        @builtins.property
        def destination_type(self) -> builtins.str:
            '''``CfnReplicationGroup.LogDeliveryConfigurationRequestProperty.DestinationType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-destinationtype
            '''
            result = self._values.get("destination_type")
            assert result is not None, "Required property 'destination_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_format(self) -> builtins.str:
            '''``CfnReplicationGroup.LogDeliveryConfigurationRequestProperty.LogFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logformat
            '''
            result = self._values.get("log_format")
            assert result is not None, "Required property 'log_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_type(self) -> builtins.str:
            '''``CfnReplicationGroup.LogDeliveryConfigurationRequestProperty.LogType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.html#cfn-elasticache-replicationgroup-logdeliveryconfigurationrequest-logtype
            '''
            result = self._values.get("log_type")
            assert result is not None, "Required property 'log_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDeliveryConfigurationRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-elasticache.CfnReplicationGroup.NodeGroupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "node_group_id": "nodeGroupId",
            "primary_availability_zone": "primaryAvailabilityZone",
            "replica_availability_zones": "replicaAvailabilityZones",
            "replica_count": "replicaCount",
            "slots": "slots",
        },
    )
    class NodeGroupConfigurationProperty:
        def __init__(
            self,
            *,
            node_group_id: typing.Optional[builtins.str] = None,
            primary_availability_zone: typing.Optional[builtins.str] = None,
            replica_availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
            replica_count: typing.Optional[jsii.Number] = None,
            slots: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param node_group_id: ``CfnReplicationGroup.NodeGroupConfigurationProperty.NodeGroupId``.
            :param primary_availability_zone: ``CfnReplicationGroup.NodeGroupConfigurationProperty.PrimaryAvailabilityZone``.
            :param replica_availability_zones: ``CfnReplicationGroup.NodeGroupConfigurationProperty.ReplicaAvailabilityZones``.
            :param replica_count: ``CfnReplicationGroup.NodeGroupConfigurationProperty.ReplicaCount``.
            :param slots: ``CfnReplicationGroup.NodeGroupConfigurationProperty.Slots``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if node_group_id is not None:
                self._values["node_group_id"] = node_group_id
            if primary_availability_zone is not None:
                self._values["primary_availability_zone"] = primary_availability_zone
            if replica_availability_zones is not None:
                self._values["replica_availability_zones"] = replica_availability_zones
            if replica_count is not None:
                self._values["replica_count"] = replica_count
            if slots is not None:
                self._values["slots"] = slots

        @builtins.property
        def node_group_id(self) -> typing.Optional[builtins.str]:
            '''``CfnReplicationGroup.NodeGroupConfigurationProperty.NodeGroupId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-nodegroupid
            '''
            result = self._values.get("node_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary_availability_zone(self) -> typing.Optional[builtins.str]:
            '''``CfnReplicationGroup.NodeGroupConfigurationProperty.PrimaryAvailabilityZone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-primaryavailabilityzone
            '''
            result = self._values.get("primary_availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replica_availability_zones(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnReplicationGroup.NodeGroupConfigurationProperty.ReplicaAvailabilityZones``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-replicaavailabilityzones
            '''
            result = self._values.get("replica_availability_zones")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def replica_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnReplicationGroup.NodeGroupConfigurationProperty.ReplicaCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-replicacount
            '''
            result = self._values.get("replica_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def slots(self) -> typing.Optional[builtins.str]:
            '''``CfnReplicationGroup.NodeGroupConfigurationProperty.Slots``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-replicationgroup-nodegroupconfiguration.html#cfn-elasticache-replicationgroup-nodegroupconfiguration-slots
            '''
            result = self._values.get("slots")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeGroupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnReplicationGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "replication_group_description": "replicationGroupDescription",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "auth_token": "authToken",
        "automatic_failover_enabled": "automaticFailoverEnabled",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "cache_node_type": "cacheNodeType",
        "cache_parameter_group_name": "cacheParameterGroupName",
        "cache_security_group_names": "cacheSecurityGroupNames",
        "cache_subnet_group_name": "cacheSubnetGroupName",
        "engine": "engine",
        "engine_version": "engineVersion",
        "global_replication_group_id": "globalReplicationGroupId",
        "kms_key_id": "kmsKeyId",
        "log_delivery_configurations": "logDeliveryConfigurations",
        "multi_az_enabled": "multiAzEnabled",
        "node_group_configuration": "nodeGroupConfiguration",
        "notification_topic_arn": "notificationTopicArn",
        "num_cache_clusters": "numCacheClusters",
        "num_node_groups": "numNodeGroups",
        "port": "port",
        "preferred_cache_cluster_a_zs": "preferredCacheClusterAZs",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "primary_cluster_id": "primaryClusterId",
        "replicas_per_node_group": "replicasPerNodeGroup",
        "replication_group_id": "replicationGroupId",
        "security_group_ids": "securityGroupIds",
        "snapshot_arns": "snapshotArns",
        "snapshot_name": "snapshotName",
        "snapshot_retention_limit": "snapshotRetentionLimit",
        "snapshotting_cluster_id": "snapshottingClusterId",
        "snapshot_window": "snapshotWindow",
        "tags": "tags",
        "transit_encryption_enabled": "transitEncryptionEnabled",
        "user_group_ids": "userGroupIds",
    },
)
class CfnReplicationGroupProps:
    def __init__(
        self,
        *,
        replication_group_description: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        auth_token: typing.Optional[builtins.str] = None,
        automatic_failover_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        cache_node_type: typing.Optional[builtins.str] = None,
        cache_parameter_group_name: typing.Optional[builtins.str] = None,
        cache_security_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        global_replication_group_id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_delivery_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnReplicationGroup.LogDeliveryConfigurationRequestProperty]]]] = None,
        multi_az_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        node_group_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnReplicationGroup.NodeGroupConfigurationProperty]]]] = None,
        notification_topic_arn: typing.Optional[builtins.str] = None,
        num_cache_clusters: typing.Optional[jsii.Number] = None,
        num_node_groups: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_cache_cluster_a_zs: typing.Optional[typing.Sequence[builtins.str]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        primary_cluster_id: typing.Optional[builtins.str] = None,
        replicas_per_node_group: typing.Optional[jsii.Number] = None,
        replication_group_id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_retention_limit: typing.Optional[jsii.Number] = None,
        snapshotting_cluster_id: typing.Optional[builtins.str] = None,
        snapshot_window: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        user_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::ReplicationGroup``.

        :param replication_group_description: ``AWS::ElastiCache::ReplicationGroup.ReplicationGroupDescription``.
        :param at_rest_encryption_enabled: ``AWS::ElastiCache::ReplicationGroup.AtRestEncryptionEnabled``.
        :param auth_token: ``AWS::ElastiCache::ReplicationGroup.AuthToken``.
        :param automatic_failover_enabled: ``AWS::ElastiCache::ReplicationGroup.AutomaticFailoverEnabled``.
        :param auto_minor_version_upgrade: ``AWS::ElastiCache::ReplicationGroup.AutoMinorVersionUpgrade``.
        :param cache_node_type: ``AWS::ElastiCache::ReplicationGroup.CacheNodeType``.
        :param cache_parameter_group_name: ``AWS::ElastiCache::ReplicationGroup.CacheParameterGroupName``.
        :param cache_security_group_names: ``AWS::ElastiCache::ReplicationGroup.CacheSecurityGroupNames``.
        :param cache_subnet_group_name: ``AWS::ElastiCache::ReplicationGroup.CacheSubnetGroupName``.
        :param engine: ``AWS::ElastiCache::ReplicationGroup.Engine``.
        :param engine_version: ``AWS::ElastiCache::ReplicationGroup.EngineVersion``.
        :param global_replication_group_id: ``AWS::ElastiCache::ReplicationGroup.GlobalReplicationGroupId``.
        :param kms_key_id: ``AWS::ElastiCache::ReplicationGroup.KmsKeyId``.
        :param log_delivery_configurations: ``AWS::ElastiCache::ReplicationGroup.LogDeliveryConfigurations``.
        :param multi_az_enabled: ``AWS::ElastiCache::ReplicationGroup.MultiAZEnabled``.
        :param node_group_configuration: ``AWS::ElastiCache::ReplicationGroup.NodeGroupConfiguration``.
        :param notification_topic_arn: ``AWS::ElastiCache::ReplicationGroup.NotificationTopicArn``.
        :param num_cache_clusters: ``AWS::ElastiCache::ReplicationGroup.NumCacheClusters``.
        :param num_node_groups: ``AWS::ElastiCache::ReplicationGroup.NumNodeGroups``.
        :param port: ``AWS::ElastiCache::ReplicationGroup.Port``.
        :param preferred_cache_cluster_a_zs: ``AWS::ElastiCache::ReplicationGroup.PreferredCacheClusterAZs``.
        :param preferred_maintenance_window: ``AWS::ElastiCache::ReplicationGroup.PreferredMaintenanceWindow``.
        :param primary_cluster_id: ``AWS::ElastiCache::ReplicationGroup.PrimaryClusterId``.
        :param replicas_per_node_group: ``AWS::ElastiCache::ReplicationGroup.ReplicasPerNodeGroup``.
        :param replication_group_id: ``AWS::ElastiCache::ReplicationGroup.ReplicationGroupId``.
        :param security_group_ids: ``AWS::ElastiCache::ReplicationGroup.SecurityGroupIds``.
        :param snapshot_arns: ``AWS::ElastiCache::ReplicationGroup.SnapshotArns``.
        :param snapshot_name: ``AWS::ElastiCache::ReplicationGroup.SnapshotName``.
        :param snapshot_retention_limit: ``AWS::ElastiCache::ReplicationGroup.SnapshotRetentionLimit``.
        :param snapshotting_cluster_id: ``AWS::ElastiCache::ReplicationGroup.SnapshottingClusterId``.
        :param snapshot_window: ``AWS::ElastiCache::ReplicationGroup.SnapshotWindow``.
        :param tags: ``AWS::ElastiCache::ReplicationGroup.Tags``.
        :param transit_encryption_enabled: ``AWS::ElastiCache::ReplicationGroup.TransitEncryptionEnabled``.
        :param user_group_ids: ``AWS::ElastiCache::ReplicationGroup.UserGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "replication_group_description": replication_group_description,
        }
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if auth_token is not None:
            self._values["auth_token"] = auth_token
        if automatic_failover_enabled is not None:
            self._values["automatic_failover_enabled"] = automatic_failover_enabled
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if cache_node_type is not None:
            self._values["cache_node_type"] = cache_node_type
        if cache_parameter_group_name is not None:
            self._values["cache_parameter_group_name"] = cache_parameter_group_name
        if cache_security_group_names is not None:
            self._values["cache_security_group_names"] = cache_security_group_names
        if cache_subnet_group_name is not None:
            self._values["cache_subnet_group_name"] = cache_subnet_group_name
        if engine is not None:
            self._values["engine"] = engine
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if global_replication_group_id is not None:
            self._values["global_replication_group_id"] = global_replication_group_id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_delivery_configurations is not None:
            self._values["log_delivery_configurations"] = log_delivery_configurations
        if multi_az_enabled is not None:
            self._values["multi_az_enabled"] = multi_az_enabled
        if node_group_configuration is not None:
            self._values["node_group_configuration"] = node_group_configuration
        if notification_topic_arn is not None:
            self._values["notification_topic_arn"] = notification_topic_arn
        if num_cache_clusters is not None:
            self._values["num_cache_clusters"] = num_cache_clusters
        if num_node_groups is not None:
            self._values["num_node_groups"] = num_node_groups
        if port is not None:
            self._values["port"] = port
        if preferred_cache_cluster_a_zs is not None:
            self._values["preferred_cache_cluster_a_zs"] = preferred_cache_cluster_a_zs
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if primary_cluster_id is not None:
            self._values["primary_cluster_id"] = primary_cluster_id
        if replicas_per_node_group is not None:
            self._values["replicas_per_node_group"] = replicas_per_node_group
        if replication_group_id is not None:
            self._values["replication_group_id"] = replication_group_id
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if snapshot_arns is not None:
            self._values["snapshot_arns"] = snapshot_arns
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if snapshot_retention_limit is not None:
            self._values["snapshot_retention_limit"] = snapshot_retention_limit
        if snapshotting_cluster_id is not None:
            self._values["snapshotting_cluster_id"] = snapshotting_cluster_id
        if snapshot_window is not None:
            self._values["snapshot_window"] = snapshot_window
        if tags is not None:
            self._values["tags"] = tags
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled
        if user_group_ids is not None:
            self._values["user_group_ids"] = user_group_ids

    @builtins.property
    def replication_group_description(self) -> builtins.str:
        '''``AWS::ElastiCache::ReplicationGroup.ReplicationGroupDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicationgroupdescription
        '''
        result = self._values.get("replication_group_description")
        assert result is not None, "Required property 'replication_group_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.AtRestEncryptionEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-atrestencryptionenabled
        '''
        result = self._values.get("at_rest_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def auth_token(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.AuthToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-authtoken
        '''
        result = self._values.get("auth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automatic_failover_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.AutomaticFailoverEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-automaticfailoverenabled
        '''
        result = self._values.get("automatic_failover_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.AutoMinorVersionUpgrade``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def cache_node_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.CacheNodeType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachenodetype
        '''
        result = self._values.get("cache_node_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.CacheParameterGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cacheparametergroupname
        '''
        result = self._values.get("cache_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_security_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.CacheSecurityGroupNames``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachesecuritygroupnames
        '''
        result = self._values.get("cache_security_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.CacheSubnetGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-cachesubnetgroupname
        '''
        result = self._values.get("cache_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.Engine``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-engine
        '''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.EngineVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def global_replication_group_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.GlobalReplicationGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-globalreplicationgroupid
        '''
        result = self._values.get("global_replication_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery_configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnReplicationGroup.LogDeliveryConfigurationRequestProperty]]]]:
        '''``AWS::ElastiCache::ReplicationGroup.LogDeliveryConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-logdeliveryconfigurations
        '''
        result = self._values.get("log_delivery_configurations")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnReplicationGroup.LogDeliveryConfigurationRequestProperty]]]], result)

    @builtins.property
    def multi_az_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.MultiAZEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-multiazenabled
        '''
        result = self._values.get("multi_az_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def node_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnReplicationGroup.NodeGroupConfigurationProperty]]]]:
        '''``AWS::ElastiCache::ReplicationGroup.NodeGroupConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-nodegroupconfiguration
        '''
        result = self._values.get("node_group_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnReplicationGroup.NodeGroupConfigurationProperty]]]], result)

    @builtins.property
    def notification_topic_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.NotificationTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-notificationtopicarn
        '''
        result = self._values.get("notification_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_cache_clusters(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.NumCacheClusters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-numcacheclusters
        '''
        result = self._values.get("num_cache_clusters")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def num_node_groups(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.NumNodeGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-numnodegroups
        '''
        result = self._values.get("num_node_groups")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.Port``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_cache_cluster_a_zs(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.PreferredCacheClusterAZs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-preferredcacheclusterazs
        '''
        result = self._values.get("preferred_cache_cluster_a_zs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.PreferredMaintenanceWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_cluster_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.PrimaryClusterId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-primaryclusterid
        '''
        result = self._values.get("primary_cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replicas_per_node_group(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.ReplicasPerNodeGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicaspernodegroup
        '''
        result = self._values.get("replicas_per_node_group")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def replication_group_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.ReplicationGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-replicationgroupid
        '''
        result = self._values.get("replication_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshotArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotarns
        '''
        result = self._values.get("snapshot_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshotName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotname
        '''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_retention_limit(self) -> typing.Optional[jsii.Number]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshotRetentionLimit``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotretentionlimit
        '''
        result = self._values.get("snapshot_retention_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshotting_cluster_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshottingClusterId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshottingclusterid
        '''
        result = self._values.get("snapshotting_cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_window(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::ReplicationGroup.SnapshotWindow``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-snapshotwindow
        '''
        result = self._values.get("snapshot_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ElastiCache::ReplicationGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::ReplicationGroup.TransitEncryptionEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-transitencryptionenabled
        '''
        result = self._values.get("transit_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def user_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::ReplicationGroup.UserGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-usergroupids
        '''
        result = self._values.get("user_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSecurityGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnSecurityGroup",
):
    '''A CloudFormation ``AWS::ElastiCache::SecurityGroup``.

    :cloudformationResource: AWS::ElastiCache::SecurityGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::SecurityGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::ElastiCache::SecurityGroup.Description``.
        :param tags: ``AWS::ElastiCache::SecurityGroup.Tags``.
        '''
        props = CfnSecurityGroupProps(description=description, tags=tags)

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ElastiCache::SecurityGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html#cfn-elasticache-securitygroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''``AWS::ElastiCache::SecurityGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html#cfn-elasticache-securitygroup-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSecurityGroupIngress(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnSecurityGroupIngress",
):
    '''A CloudFormation ``AWS::ElastiCache::SecurityGroupIngress``.

    :cloudformationResource: AWS::ElastiCache::SecurityGroupIngress
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cache_security_group_name: builtins.str,
        ec2_security_group_name: builtins.str,
        ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::SecurityGroupIngress``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cache_security_group_name: ``AWS::ElastiCache::SecurityGroupIngress.CacheSecurityGroupName``.
        :param ec2_security_group_name: ``AWS::ElastiCache::SecurityGroupIngress.EC2SecurityGroupName``.
        :param ec2_security_group_owner_id: ``AWS::ElastiCache::SecurityGroupIngress.EC2SecurityGroupOwnerId``.
        '''
        props = CfnSecurityGroupIngressProps(
            cache_security_group_name=cache_security_group_name,
            ec2_security_group_name=ec2_security_group_name,
            ec2_security_group_owner_id=ec2_security_group_owner_id,
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
    @jsii.member(jsii_name="cacheSecurityGroupName")
    def cache_security_group_name(self) -> builtins.str:
        '''``AWS::ElastiCache::SecurityGroupIngress.CacheSecurityGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-cachesecuritygroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "cacheSecurityGroupName"))

    @cache_security_group_name.setter
    def cache_security_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "cacheSecurityGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2SecurityGroupName")
    def ec2_security_group_name(self) -> builtins.str:
        '''``AWS::ElastiCache::SecurityGroupIngress.EC2SecurityGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-ec2securitygroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "ec2SecurityGroupName"))

    @ec2_security_group_name.setter
    def ec2_security_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "ec2SecurityGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2SecurityGroupOwnerId")
    def ec2_security_group_owner_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::SecurityGroupIngress.EC2SecurityGroupOwnerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-ec2securitygroupownerid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2SecurityGroupOwnerId"))

    @ec2_security_group_owner_id.setter
    def ec2_security_group_owner_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ec2SecurityGroupOwnerId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnSecurityGroupIngressProps",
    jsii_struct_bases=[],
    name_mapping={
        "cache_security_group_name": "cacheSecurityGroupName",
        "ec2_security_group_name": "ec2SecurityGroupName",
        "ec2_security_group_owner_id": "ec2SecurityGroupOwnerId",
    },
)
class CfnSecurityGroupIngressProps:
    def __init__(
        self,
        *,
        cache_security_group_name: builtins.str,
        ec2_security_group_name: builtins.str,
        ec2_security_group_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::SecurityGroupIngress``.

        :param cache_security_group_name: ``AWS::ElastiCache::SecurityGroupIngress.CacheSecurityGroupName``.
        :param ec2_security_group_name: ``AWS::ElastiCache::SecurityGroupIngress.EC2SecurityGroupName``.
        :param ec2_security_group_owner_id: ``AWS::ElastiCache::SecurityGroupIngress.EC2SecurityGroupOwnerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cache_security_group_name": cache_security_group_name,
            "ec2_security_group_name": ec2_security_group_name,
        }
        if ec2_security_group_owner_id is not None:
            self._values["ec2_security_group_owner_id"] = ec2_security_group_owner_id

    @builtins.property
    def cache_security_group_name(self) -> builtins.str:
        '''``AWS::ElastiCache::SecurityGroupIngress.CacheSecurityGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-cachesecuritygroupname
        '''
        result = self._values.get("cache_security_group_name")
        assert result is not None, "Required property 'cache_security_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ec2_security_group_name(self) -> builtins.str:
        '''``AWS::ElastiCache::SecurityGroupIngress.EC2SecurityGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-ec2securitygroupname
        '''
        result = self._values.get("ec2_security_group_name")
        assert result is not None, "Required property 'ec2_security_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ec2_security_group_owner_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::SecurityGroupIngress.EC2SecurityGroupOwnerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html#cfn-elasticache-securitygroupingress-ec2securitygroupownerid
        '''
        result = self._values.get("ec2_security_group_owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityGroupIngressProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnSecurityGroupProps",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "tags": "tags"},
)
class CfnSecurityGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::SecurityGroup``.

        :param description: ``AWS::ElastiCache::SecurityGroup.Description``.
        :param tags: ``AWS::ElastiCache::SecurityGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''``AWS::ElastiCache::SecurityGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html#cfn-elasticache-securitygroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ElastiCache::SecurityGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html#cfn-elasticache-securitygroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSubnetGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnSubnetGroup",
):
    '''A CloudFormation ``AWS::ElastiCache::SubnetGroup``.

    :cloudformationResource: AWS::ElastiCache::SubnetGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::SubnetGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::ElastiCache::SubnetGroup.Description``.
        :param subnet_ids: ``AWS::ElastiCache::SubnetGroup.SubnetIds``.
        :param cache_subnet_group_name: ``AWS::ElastiCache::SubnetGroup.CacheSubnetGroupName``.
        :param tags: ``AWS::ElastiCache::SubnetGroup.Tags``.
        '''
        props = CfnSubnetGroupProps(
            description=description,
            subnet_ids=subnet_ids,
            cache_subnet_group_name=cache_subnet_group_name,
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ElastiCache::SubnetGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''``AWS::ElastiCache::SubnetGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::ElastiCache::SubnetGroup.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "subnetIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cacheSubnetGroupName")
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::SubnetGroup.CacheSubnetGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-cachesubnetgroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheSubnetGroupName"))

    @cache_subnet_group_name.setter
    def cache_subnet_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cacheSubnetGroupName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "subnet_ids": "subnetIds",
        "cache_subnet_group_name": "cacheSubnetGroupName",
        "tags": "tags",
    },
)
class CfnSubnetGroupProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        cache_subnet_group_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::SubnetGroup``.

        :param description: ``AWS::ElastiCache::SubnetGroup.Description``.
        :param subnet_ids: ``AWS::ElastiCache::SubnetGroup.SubnetIds``.
        :param cache_subnet_group_name: ``AWS::ElastiCache::SubnetGroup.CacheSubnetGroupName``.
        :param tags: ``AWS::ElastiCache::SubnetGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "description": description,
            "subnet_ids": subnet_ids,
        }
        if cache_subnet_group_name is not None:
            self._values["cache_subnet_group_name"] = cache_subnet_group_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''``AWS::ElastiCache::SubnetGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::ElastiCache::SubnetGroup.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def cache_subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::SubnetGroup.CacheSubnetGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-cachesubnetgroupname
        '''
        result = self._values.get("cache_subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ElastiCache::SubnetGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html#cfn-elasticache-subnetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnUser(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnUser",
):
    '''A CloudFormation ``AWS::ElastiCache::User``.

    :cloudformationResource: AWS::ElastiCache::User
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        engine: builtins.str,
        user_id: builtins.str,
        user_name: builtins.str,
        access_string: typing.Optional[builtins.str] = None,
        no_password_required: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::User``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param engine: ``AWS::ElastiCache::User.Engine``.
        :param user_id: ``AWS::ElastiCache::User.UserId``.
        :param user_name: ``AWS::ElastiCache::User.UserName``.
        :param access_string: ``AWS::ElastiCache::User.AccessString``.
        :param no_password_required: ``AWS::ElastiCache::User.NoPasswordRequired``.
        :param passwords: ``AWS::ElastiCache::User.Passwords``.
        '''
        props = CfnUserProps(
            engine=engine,
            user_id=user_id,
            user_name=user_name,
            access_string=access_string,
            no_password_required=no_password_required,
            passwords=passwords,
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
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        '''``AWS::ElastiCache::User.Engine``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-engine
        '''
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        jsii.set(self, "engine", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        '''``AWS::ElastiCache::User.UserId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-userid
        '''
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: builtins.str) -> None:
        jsii.set(self, "userId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''``AWS::ElastiCache::User.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-username
        '''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        jsii.set(self, "userName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessString")
    def access_string(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::User.AccessString``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-accessstring
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessString"))

    @access_string.setter
    def access_string(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "accessString", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="noPasswordRequired")
    def no_password_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::User.NoPasswordRequired``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-nopasswordrequired
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "noPasswordRequired"))

    @no_password_required.setter
    def no_password_required(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "noPasswordRequired", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="passwords")
    def passwords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::User.Passwords``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-passwords
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "passwords"))

    @passwords.setter
    def passwords(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "passwords", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnUserGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticache.CfnUserGroup",
):
    '''A CloudFormation ``AWS::ElastiCache::UserGroup``.

    :cloudformationResource: AWS::ElastiCache::UserGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        engine: builtins.str,
        user_group_id: builtins.str,
        user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::ElastiCache::UserGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param engine: ``AWS::ElastiCache::UserGroup.Engine``.
        :param user_group_id: ``AWS::ElastiCache::UserGroup.UserGroupId``.
        :param user_ids: ``AWS::ElastiCache::UserGroup.UserIds``.
        '''
        props = CfnUserGroupProps(
            engine=engine, user_group_id=user_group_id, user_ids=user_ids
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
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        '''``AWS::ElastiCache::UserGroup.Engine``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-engine
        '''
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        jsii.set(self, "engine", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userGroupId")
    def user_group_id(self) -> builtins.str:
        '''``AWS::ElastiCache::UserGroup.UserGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-usergroupid
        '''
        return typing.cast(builtins.str, jsii.get(self, "userGroupId"))

    @user_group_id.setter
    def user_group_id(self, value: builtins.str) -> None:
        jsii.set(self, "userGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userIds")
    def user_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::UserGroup.UserIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-userids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "userIds"))

    @user_ids.setter
    def user_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "userIds", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnUserGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "engine": "engine",
        "user_group_id": "userGroupId",
        "user_ids": "userIds",
    },
)
class CfnUserGroupProps:
    def __init__(
        self,
        *,
        engine: builtins.str,
        user_group_id: builtins.str,
        user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::UserGroup``.

        :param engine: ``AWS::ElastiCache::UserGroup.Engine``.
        :param user_group_id: ``AWS::ElastiCache::UserGroup.UserGroupId``.
        :param user_ids: ``AWS::ElastiCache::UserGroup.UserIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "engine": engine,
            "user_group_id": user_group_id,
        }
        if user_ids is not None:
            self._values["user_ids"] = user_ids

    @builtins.property
    def engine(self) -> builtins.str:
        '''``AWS::ElastiCache::UserGroup.Engine``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-engine
        '''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_group_id(self) -> builtins.str:
        '''``AWS::ElastiCache::UserGroup.UserGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-usergroupid
        '''
        result = self._values.get("user_group_id")
        assert result is not None, "Required property 'user_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::UserGroup.UserIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-usergroup.html#cfn-elasticache-usergroup-userids
        '''
        result = self._values.get("user_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticache.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "engine": "engine",
        "user_id": "userId",
        "user_name": "userName",
        "access_string": "accessString",
        "no_password_required": "noPasswordRequired",
        "passwords": "passwords",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        engine: builtins.str,
        user_id: builtins.str,
        user_name: builtins.str,
        access_string: typing.Optional[builtins.str] = None,
        no_password_required: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        passwords: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ElastiCache::User``.

        :param engine: ``AWS::ElastiCache::User.Engine``.
        :param user_id: ``AWS::ElastiCache::User.UserId``.
        :param user_name: ``AWS::ElastiCache::User.UserName``.
        :param access_string: ``AWS::ElastiCache::User.AccessString``.
        :param no_password_required: ``AWS::ElastiCache::User.NoPasswordRequired``.
        :param passwords: ``AWS::ElastiCache::User.Passwords``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "engine": engine,
            "user_id": user_id,
            "user_name": user_name,
        }
        if access_string is not None:
            self._values["access_string"] = access_string
        if no_password_required is not None:
            self._values["no_password_required"] = no_password_required
        if passwords is not None:
            self._values["passwords"] = passwords

    @builtins.property
    def engine(self) -> builtins.str:
        '''``AWS::ElastiCache::User.Engine``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-engine
        '''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_id(self) -> builtins.str:
        '''``AWS::ElastiCache::User.UserId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-userid
        '''
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''``AWS::ElastiCache::User.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_string(self) -> typing.Optional[builtins.str]:
        '''``AWS::ElastiCache::User.AccessString``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-accessstring
        '''
        result = self._values.get("access_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_password_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::ElastiCache::User.NoPasswordRequired``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-nopasswordrequired
        '''
        result = self._values.get("no_password_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def passwords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ElastiCache::User.Passwords``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-user.html#cfn-elasticache-user-passwords
        '''
        result = self._values.get("passwords")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCacheCluster",
    "CfnCacheClusterProps",
    "CfnGlobalReplicationGroup",
    "CfnGlobalReplicationGroupProps",
    "CfnParameterGroup",
    "CfnParameterGroupProps",
    "CfnReplicationGroup",
    "CfnReplicationGroupProps",
    "CfnSecurityGroup",
    "CfnSecurityGroupIngress",
    "CfnSecurityGroupIngressProps",
    "CfnSecurityGroupProps",
    "CfnSubnetGroup",
    "CfnSubnetGroupProps",
    "CfnUser",
    "CfnUserGroup",
    "CfnUserGroupProps",
    "CfnUserProps",
]

publication.publish()
