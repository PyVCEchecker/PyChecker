# Amazon Neptune Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. The core of Neptune is a purpose-built, high-performance graph database engine. This engine is optimized for storing billions of relationships and querying the graph with milliseconds latency. Neptune supports the popular graph query languages Apache TinkerPop Gremlin and W3C’s SPARQL, enabling you to build queries that efficiently navigate highly connected datasets.

The `@aws-cdk/aws-neptune` package contains primitives for setting up Neptune database clusters and instances.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_neptune as neptune
```

## Starting a Neptune Database

To set up a Neptune database, define a `DatabaseCluster`. You must always launch a database in a VPC.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE
)
```

By default only writer instance is provisioned with this construct.

## Connecting

To control who can access the cluster, use the `.connections` attribute. Neptune databases have a default port, so
you don't need to specify the port:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
cluster.connections.allow_default_port_from_any_ipv4("Open to the world")
```

The endpoints to access your database cluster will be available as the `.clusterEndpoint` and `.clusterReadEndpoint`
attributes:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
write_address = cluster.cluster_endpoint.socket_address
```

## IAM Authentication

You can also authenticate to a database cluster using AWS Identity and Access Management (IAM) database authentication;
See [https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html) for more information and a list of supported
versions and limitations.

The following example shows enabling IAM authentication for a database cluster and granting connection access to an IAM role.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
cluster = neptune.DatabaseCluster(self, "Cluster",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    iam_authentication=True
)
role = iam.Role(self, "DBRole", assumed_by=iam.AccountPrincipal(self.account))
cluster.grant_connect(role)
```

## Customizing parameters

Neptune allows configuring database behavior by supplying custom parameter groups.  For more details, refer to the
following link: [https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html](https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html)

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
    description="Cluster parameter group",
    parameters={
        "neptune_enable_audit_log": "1"
    }
)

db_params = neptune.ParameterGroup(self, "DbParams",
    description="Db parameter group",
    parameters={
        "neptune_query_timeout": "120000"
    }
)

cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    cluster_parameter_group=cluster_params,
    parameter_group=db_params
)
```

## Adding replicas

`DatabaseCluster` allows launching replicas along with the writer instance. This can be specified using the `instanceCount`
attribute.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    instances=2
)
```

Additionally it is also possible to add replicas using `DatabaseInstance` for an existing cluster.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
replica1 = neptune.DatabaseInstance(self, "Instance",
    cluster=cluster,
    instance_type=neptune.InstanceType.R5_LARGE
)
```
