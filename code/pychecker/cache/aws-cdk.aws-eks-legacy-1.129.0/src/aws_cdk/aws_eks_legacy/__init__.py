'''
# Amazon EKS Construct Library

<!--BEGIN STABILITY BANNER-->---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This API may emit warnings. Backward compatibility is not guaranteed.

---
<!--END STABILITY BANNER-->

**This module is available for backwards compatibility purposes only ([details](https://github.com/aws/aws-cdk/pull/5540)). It will
no longer be released with the CDK starting March 1st, 2020. See [issue

## 5544](https://github.com/aws/aws-cdk/issues/5544) for upgrade instructions.**

---


This construct library allows you to define [Amazon Elastic Container Service
for Kubernetes (EKS)](https://aws.amazon.com/eks/) clusters programmatically.
This library also supports programmatically defining Kubernetes resource
manifests within EKS clusters.

This example defines an Amazon EKS cluster with the following configuration:

* 2x **m5.large** instances (this instance type suits most common use-cases, and is good value for money)
* Dedicated VPC with default configuration (see [ec2.Vpc](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-ec2-readme.html#vpc))
* A Kubernetes pod with a container based on the [paulbouwer/hello-kubernetes](https://github.com/paulbouwer/hello-kubernetes) image.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster = eks.Cluster(self, "hello-eks")

cluster.add_resource("mypod",
    api_version="v1",
    kind="Pod",
    metadata={"name": "mypod"},
    spec={
        "containers": [{
            "name": "hello",
            "image": "paulbouwer/hello-kubernetes:1.5",
            "ports": [{"container_port": 8080}]
        }
        ]
    }
)
```

Here is a [complete sample](https://github.com/aws/aws-cdk/blob/master/packages/%40aws-cdk/aws-eks/test/integ.eks-kubectl.lit.ts).

### Capacity

By default, `eks.Cluster` is created with x2 `m5.large` instances.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
eks.Cluster(self, "cluster-two-m5-large")
```

The quantity and instance type for the default capacity can be specified through
the `defaultCapacity` and `defaultCapacityInstance` props:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
eks.Cluster(self, "cluster",
    default_capacity=10,
    default_capacity_instance=ec2.InstanceType("m2.xlarge")
)
```

To disable the default capacity, simply set `defaultCapacity` to `0`:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
eks.Cluster(self, "cluster-with-no-capacity", default_capacity=0)
```

The `cluster.defaultCapacity` property will reference the `AutoScalingGroup`
resource for the default capacity. It will be `undefined` if `defaultCapacity`
is set to `0`:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster = eks.Cluster(self, "my-cluster")
cluster.default_capacity.scale_on_cpu_utilization("up",
    target_utilization_percent=80
)
```

You can add customized capacity through `cluster.addCapacity()` or
`cluster.addAutoScalingGroup()`:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster.add_capacity("frontend-nodes",
    instance_type=ec2.InstanceType("t2.medium"),
    desired_capacity=3,
    vpc_subnets={"subnet_type": ec2.SubnetType.PUBLIC}
)
```

### Spot Capacity

If `spotPrice` is specified, the capacity will be purchased from spot instances:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster.add_capacity("spot",
    spot_price="0.1094",
    instance_type=ec2.InstanceType("t3.large"),
    max_capacity=10
)
```

Spot instance nodes will be labeled with `lifecycle=Ec2Spot` and tainted with `PreferNoSchedule`.

The [Spot Termination Handler](https://github.com/awslabs/ec2-spot-labs/tree/master/ec2-spot-eks-solution/spot-termination-handler)
DaemonSet will be installed on these nodes. The termination handler leverages
[EC2 Spot Instance Termination Notices](https://aws.amazon.com/blogs/aws/new-ec2-spot-instance-termination-notices/)
to gracefully stop all pods running on spot nodes that are about to be
terminated.

### Bootstrapping

When adding capacity, you can specify options for
[/etc/eks/boostrap.sh](https://github.com/awslabs/amazon-eks-ami/blob/master/files/bootstrap.sh)
which is responsible for associating the node to the EKS cluster. For example,
you can use `kubeletExtraArgs` to add custom node labels or taints.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# up to ten spot instances
cluster.add_capacity("spot",
    instance_type=ec2.InstanceType("t3.large"),
    desired_capacity=2,
    bootstrap_options={
        "kubelet_extra_args": "--node-labels foo=bar,goo=far",
        "aws_api_retry_attempts": 5
    }
)
```

To disable bootstrapping altogether (i.e. to fully customize user-data), set `bootstrapEnabled` to `false` when you add
the capacity.

### Masters Role

The Amazon EKS construct library allows you to specify an IAM role that will be
granted `system:masters` privileges on your cluster.

Without specifying a `mastersRole`, you will not be able to interact manually
with the cluster.

The following example defines an IAM role that can be assumed by all users
in the account and shows how to use the `mastersRole` property to map this
role to the Kubernetes `system:masters` group:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# first define the role
cluster_admin = iam.Role(self, "AdminRole",
    assumed_by=iam.AccountRootPrincipal()
)

# now define the cluster and map role to "masters" RBAC group
eks.Cluster(self, "Cluster",
    masters_role=cluster_admin
)
```

When you `cdk deploy` this CDK app, you will notice that an output will be printed
with the `update-kubeconfig` command.

Something like this:

```plaintext
Outputs:
eks-integ-defaults.ClusterConfigCommand43AAE40F = aws eks update-kubeconfig --name cluster-ba7c166b-c4f3-421c-bf8a-6812e4036a33 --role-arn arn:aws:iam::112233445566:role/eks-integ-defaults-Role1ABCC5F0-1EFK2W5ZJD98Y
```

Copy & paste the "`aws eks update-kubeconfig ...`" command to your shell in
order to connect to your EKS cluster with the "masters" role.

Now, given [AWS CLI](https://aws.amazon.com/cli/) is configured to use AWS
credentials for a user that is trusted by the masters role, you should be able
to interact with your cluster through `kubectl` (the above example will trust
all users in the account).

For example:

```console
$ aws eks update-kubeconfig --name cluster-ba7c166b-c4f3-421c-bf8a-6812e4036a33 --role-arn arn:aws:iam::112233445566:role/eks-integ-defaults-Role1ABCC5F0-1EFK2W5ZJD98Y
Added new context arn:aws:eks:eu-west-2:112233445566:cluster/cluster-ba7c166b-c4f3-421c-bf8a-6812e4036a33 to /Users/boom/.kube/config

$ kubectl get nodes # list all nodes
NAME                                         STATUS   ROLES    AGE   VERSION
ip-10-0-147-66.eu-west-2.compute.internal    Ready    <none>   21m   v1.13.7-eks-c57ff8
ip-10-0-169-151.eu-west-2.compute.internal   Ready    <none>   21m   v1.13.7-eks-c57ff8

$ kubectl get all -n kube-system
NAME                           READY   STATUS    RESTARTS   AGE
pod/aws-node-fpmwv             1/1     Running   0          21m
pod/aws-node-m9htf             1/1     Running   0          21m
pod/coredns-5cb4fb54c7-q222j   1/1     Running   0          23m
pod/coredns-5cb4fb54c7-v9nxx   1/1     Running   0          23m
pod/kube-proxy-d4jrh           1/1     Running   0          21m
pod/kube-proxy-q7hh7           1/1     Running   0          21m

NAME               TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)         AGE
service/kube-dns   ClusterIP   172.20.0.10   <none>        53/UDP,53/TCP   23m

NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
daemonset.apps/aws-node     2         2         2       2            2           <none>          23m
daemonset.apps/kube-proxy   2         2         2       2            2           <none>          23m

NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/coredns   2/2     2            2           23m

NAME                                 DESIRED   CURRENT   READY   AGE
replicaset.apps/coredns-5cb4fb54c7   2         2         2       23m
```

For your convenience, an AWS CloudFormation output will automatically be
included in your template and will be printed when running `cdk deploy`.

**NOTE**: if the cluster is configured with `kubectlEnabled: false`, it
will be created with the role/user that created the AWS CloudFormation
stack. See [Kubectl Support](#kubectl-support) for details.

### Kubernetes Resources

The `KubernetesResource` construct or `cluster.addResource` method can be used
to apply Kubernetes resource manifests to this cluster.

The following examples will deploy the [paulbouwer/hello-kubernetes](https://github.com/paulbouwer/hello-kubernetes)
service on the cluster:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
app_label = {"app": "hello-kubernetes"}

deployment = {
    "api_version": "apps/v1",
    "kind": "Deployment",
    "metadata": {"name": "hello-kubernetes"},
    "spec": {
        "replicas": 3,
        "selector": {"match_labels": app_label},
        "template": {
            "metadata": {"labels": app_label},
            "spec": {
                "containers": [{
                    "name": "hello-kubernetes",
                    "image": "paulbouwer/hello-kubernetes:1.5",
                    "ports": [{"container_port": 8080}]
                }
                ]
            }
        }
    }
}

service = {
    "api_version": "v1",
    "kind": "Service",
    "metadata": {"name": "hello-kubernetes"},
    "spec": {
        "type": "LoadBalancer",
        "ports": [{"port": 80, "target_port": 8080}],
        "selector": app_label
    }
}

# option 1: use a construct
KubernetesResource(self, "hello-kub",
    cluster=cluster,
    manifest=[deployment, service]
)

# or, option2: use `addResource`
cluster.add_resource("hello-kub", service, deployment)
```

Since Kubernetes resources are implemented as CloudFormation resources in the
CDK. This means that if the resource is deleted from your code (or the stack is
deleted), the next `cdk deploy` will issue a `kubectl delete` command and the
Kubernetes resources will be deleted.

### AWS IAM Mapping

As described in the [Amazon EKS User Guide](https://docs.aws.amazon.com/en_us/eks/latest/userguide/add-user-role.html),
you can map AWS IAM users and roles to [Kubernetes Role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac).

The Amazon EKS construct manages the **aws-auth ConfigMap** Kubernetes resource
on your behalf and exposes an API through the `cluster.awsAuth` for mapping
users, roles and accounts.

Furthermore, when auto-scaling capacity is added to the cluster (through
`cluster.addCapacity` or `cluster.addAutoScalingGroup`), the IAM instance role
of the auto-scaling group will be automatically mapped to RBAC so nodes can
connect to the cluster. No manual mapping is required any longer.

> NOTE: `cluster.awsAuth` will throw an error if your cluster is created with `kubectlEnabled: false`.

For example, let's say you want to grant an IAM user administrative privileges
on your cluster:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
admin_user = iam.User(self, "Admin")
cluster.aws_auth.add_user_mapping(admin_user, groups=["system:masters"])
```

A convenience method for mapping a role to the `system:masters` group is also available:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cluster.aws_auth.add_masters_role(role)
```

### Node ssh Access

If you want to be able to SSH into your worker nodes, you must already
have an SSH key in the region you're connecting to and pass it, and you must
be able to connect to the hosts (meaning they must have a public IP and you
should be allowed to connect to them on port 22):

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
asg = cluster.add_capacity("Nodes",
    instance_type=ec2.InstanceType("t2.medium"),
    vpc_subnets=SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
    key_name="my-key-name"
)

# Replace with desired IP
asg.connections.allow_from(ec2.Peer.ipv4("1.2.3.4/32"), ec2.Port.tcp(22))
```

If you want to SSH into nodes in a private subnet, you should set up a
bastion host in a public subnet. That setup is recommended, but is
unfortunately beyond the scope of this documentation.

### kubectl Support

When you create an Amazon EKS cluster, the IAM entity user or role, such as a
[federated user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
that creates the cluster, is automatically granted `system:masters` permissions
in the cluster's RBAC configuration.

In order to allow programmatically defining **Kubernetes resources** in your AWS
CDK app and provisioning them through AWS CloudFormation, we will need to assume
this "masters" role every time we want to issue `kubectl` operations against your
cluster.

At the moment, the [AWS::EKS::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html)
AWS CloudFormation resource does not support this behavior, so in order to
support "programmatic kubectl", such as applying manifests
and mapping IAM roles from within your CDK application, the Amazon EKS
construct library uses a custom resource for provisioning the cluster.
This custom resource is executed with an IAM role that we can then use
to issue `kubectl` commands.

The default behavior of this library is to use this custom resource in order
to retain programmatic control over the cluster. In other words: to allow
you to define Kubernetes resources in your CDK code instead of having to
manage your Kubernetes applications through a separate system.

One of the implications of this design is that, by default, the user who
provisioned the AWS CloudFormation stack (executed `cdk deploy`) will
not have administrative privileges on the EKS cluster.

1. Additional resources will be synthesized into your template (the AWS Lambda
   function, the role and policy).
2. As described in [Interacting with Your Cluster](#interacting-with-your-cluster),
   if you wish to be able to manually interact with your cluster, you will need
   to map an IAM role or user to the `system:masters` group. This can be either
   done by specifying a `mastersRole` when the cluster is defined, calling
   `cluster.awsAuth.addMastersRole` or explicitly mapping an IAM role or IAM user to the
   relevant Kubernetes RBAC groups using `cluster.addRoleMapping` and/or
   `cluster.addUserMapping`.

If you wish to disable the programmatic kubectl behavior and use the standard
AWS::EKS::Cluster resource, you can specify `kubectlEnabled: false` when you define
the cluster:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
eks.Cluster(self, "cluster",
    kubectl_enabled=False
)
```

**Take care**: a change in this property will cause the cluster to be destroyed
and a new cluster to be created.

When kubectl is disabled, you should be aware of the following:

1. When you log-in to your cluster, you don't need to specify `--role-arn` as
   long as you are using the same user that created the cluster.
2. As described in the Amazon EKS User Guide, you will need to manually
   edit the [aws-auth ConfigMap](https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html)
   when you add capacity in order to map the IAM instance role to RBAC to allow nodes to join the cluster.
3. Any `eks.Cluster` APIs that depend on programmatic kubectl support will fail
   with an error: `cluster.addResource`, `cluster.addChart`, `cluster.awsAuth`, `props.mastersRole`.

### Helm Charts

The `HelmChart` construct or `cluster.addChart` method can be used
to add Kubernetes resources to this cluster using Helm.

The following example will install the [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/)
to you cluster using Helm.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# option 1: use a construct
HelmChart(self, "NginxIngress",
    cluster=cluster,
    chart="nginx-ingress",
    repository="https://helm.nginx.com/stable",
    namespace="kube-system"
)

# or, option2: use `addChart`
cluster.add_chart("NginxIngress",
    chart="nginx-ingress",
    repository="https://helm.nginx.com/stable",
    namespace="kube-system"
)
```

Helm charts will be installed and updated using `helm upgrade --install`.
This means that if the chart is added to CDK with the same release name, it will try to update
the chart in the cluster. The chart will exists as CloudFormation resource.

Helm charts are implemented as CloudFormation resources in CDK.
This means that if the chart is deleted from your code (or the stack is
deleted), the next `cdk deploy` will issue a `helm uninstall` command and the
Helm chart will be deleted.

When there is no `release` defined, the chart will be installed with a unique name allocated
based on the construct path.

### Roadmap

* [ ] AutoScaling (combine EC2 and Kubernetes scaling)
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

import aws_cdk.aws_autoscaling
import aws_cdk.aws_ec2
import aws_cdk.aws_iam
import aws_cdk.aws_sns
import aws_cdk.core


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.AutoScalingGroupOptions",
    jsii_struct_bases=[],
    name_mapping={
        "bootstrap_enabled": "bootstrapEnabled",
        "bootstrap_options": "bootstrapOptions",
        "map_role": "mapRole",
    },
)
class AutoScalingGroupOptions:
    def __init__(
        self,
        *,
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional["BootstrapOptions"] = None,
        map_role: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(deprecated) Options for adding an AutoScalingGroup as capacity.

        :param bootstrap_enabled: (deprecated) Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: (deprecated) Allows options for node bootstrapping through EC2 user data.
        :param map_role: (deprecated) Will automatically update the aws-auth ConfigMap to map the IAM instance role to RBAC. This cannot be explicitly set to ``true`` if the cluster has kubectl disabled. Default: - true if the cluster has kubectl enabled (which is the default).

        :stability: deprecated
        '''
        if isinstance(bootstrap_options, dict):
            bootstrap_options = BootstrapOptions(**bootstrap_options)
        self._values: typing.Dict[str, typing.Any] = {}
        if bootstrap_enabled is not None:
            self._values["bootstrap_enabled"] = bootstrap_enabled
        if bootstrap_options is not None:
            self._values["bootstrap_options"] = bootstrap_options
        if map_role is not None:
            self._values["map_role"] = map_role

    @builtins.property
    def bootstrap_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster.

        If you wish to provide a custom user data script, set this to ``false`` and
        manually invoke ``autoscalingGroup.addUserData()``.

        :default: true

        :stability: deprecated
        '''
        result = self._values.get("bootstrap_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bootstrap_options(self) -> typing.Optional["BootstrapOptions"]:
        '''(deprecated) Allows options for node bootstrapping through EC2 user data.

        :stability: deprecated
        '''
        result = self._values.get("bootstrap_options")
        return typing.cast(typing.Optional["BootstrapOptions"], result)

    @builtins.property
    def map_role(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Will automatically update the aws-auth ConfigMap to map the IAM instance role to RBAC.

        This cannot be explicitly set to ``true`` if the cluster has kubectl disabled.

        :default: - true if the cluster has kubectl enabled (which is the default).

        :stability: deprecated
        '''
        result = self._values.get("map_role")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScalingGroupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AwsAuth(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.AwsAuth",
):
    '''(deprecated) Manages mapping between IAM users and roles to Kubernetes RBAC configuration.

    :see: https://docs.aws.amazon.com/en_us/eks/latest/userguide/add-user-role.html
    :stability: deprecated
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster: "Cluster",
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: (deprecated) The EKS cluster to apply this configuration to. [disable-awslint:ref-via-interface]

        :stability: deprecated
        '''
        props = AwsAuthProps(cluster=cluster)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addAccount")
    def add_account(self, account_id: builtins.str) -> None:
        '''(deprecated) Additional AWS account to add to the aws-auth configmap.

        :param account_id: account number.

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "addAccount", [account_id]))

    @jsii.member(jsii_name="addMastersRole")
    def add_masters_role(
        self,
        role: aws_cdk.aws_iam.IRole,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Adds the specified IAM role to the ``system:masters`` RBAC group, which means that anyone that can assume it will be able to administer this Kubernetes system.

        :param role: The IAM role to add.
        :param username: Optional user (defaults to the role ARN).

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "addMastersRole", [role, username]))

    @jsii.member(jsii_name="addRoleMapping")
    def add_role_mapping(
        self,
        role: aws_cdk.aws_iam.IRole,
        *,
        groups: typing.Sequence[builtins.str],
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Adds a mapping between an IAM role to a Kubernetes user and groups.

        :param role: The IAM role to map.
        :param groups: (deprecated) A list of groups within Kubernetes to which the role is mapped.
        :param username: (deprecated) The user name within Kubernetes to map to the IAM role. Default: - By default, the user name is the ARN of the IAM role.

        :stability: deprecated
        '''
        mapping = Mapping(groups=groups, username=username)

        return typing.cast(None, jsii.invoke(self, "addRoleMapping", [role, mapping]))

    @jsii.member(jsii_name="addUserMapping")
    def add_user_mapping(
        self,
        user: aws_cdk.aws_iam.IUser,
        *,
        groups: typing.Sequence[builtins.str],
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Adds a mapping between an IAM user to a Kubernetes user and groups.

        :param user: The IAM user to map.
        :param groups: (deprecated) A list of groups within Kubernetes to which the role is mapped.
        :param username: (deprecated) The user name within Kubernetes to map to the IAM role. Default: - By default, the user name is the ARN of the IAM role.

        :stability: deprecated
        '''
        mapping = Mapping(groups=groups, username=username)

        return typing.cast(None, jsii.invoke(self, "addUserMapping", [user, mapping]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.AwsAuthProps",
    jsii_struct_bases=[],
    name_mapping={"cluster": "cluster"},
)
class AwsAuthProps:
    def __init__(self, *, cluster: "Cluster") -> None:
        '''
        :param cluster: (deprecated) The EKS cluster to apply this configuration to. [disable-awslint:ref-via-interface]

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cluster": cluster,
        }

    @builtins.property
    def cluster(self) -> "Cluster":
        '''(deprecated) The EKS cluster to apply this configuration to.

        [disable-awslint:ref-via-interface]

        :stability: deprecated
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("Cluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsAuthProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.BootstrapOptions",
    jsii_struct_bases=[],
    name_mapping={
        "additional_args": "additionalArgs",
        "aws_api_retry_attempts": "awsApiRetryAttempts",
        "docker_config_json": "dockerConfigJson",
        "enable_docker_bridge": "enableDockerBridge",
        "kubelet_extra_args": "kubeletExtraArgs",
        "use_max_pods": "useMaxPods",
    },
)
class BootstrapOptions:
    def __init__(
        self,
        *,
        additional_args: typing.Optional[builtins.str] = None,
        aws_api_retry_attempts: typing.Optional[jsii.Number] = None,
        docker_config_json: typing.Optional[builtins.str] = None,
        enable_docker_bridge: typing.Optional[builtins.bool] = None,
        kubelet_extra_args: typing.Optional[builtins.str] = None,
        use_max_pods: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param additional_args: (deprecated) Additional command line arguments to pass to the ``/etc/eks/bootstrap.sh`` command. Default: - none
        :param aws_api_retry_attempts: (deprecated) Number of retry attempts for AWS API call (DescribeCluster). Default: 3
        :param docker_config_json: (deprecated) The contents of the ``/etc/docker/daemon.json`` file. Useful if you want a custom config differing from the default one in the EKS AMI. Default: - none
        :param enable_docker_bridge: (deprecated) Restores the docker default bridge network. Default: false
        :param kubelet_extra_args: (deprecated) Extra arguments to add to the kubelet. Useful for adding labels or taints. Default: - none
        :param use_max_pods: (deprecated) Sets ``--max-pods`` for the kubelet based on the capacity of the EC2 instance. Default: true

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_args is not None:
            self._values["additional_args"] = additional_args
        if aws_api_retry_attempts is not None:
            self._values["aws_api_retry_attempts"] = aws_api_retry_attempts
        if docker_config_json is not None:
            self._values["docker_config_json"] = docker_config_json
        if enable_docker_bridge is not None:
            self._values["enable_docker_bridge"] = enable_docker_bridge
        if kubelet_extra_args is not None:
            self._values["kubelet_extra_args"] = kubelet_extra_args
        if use_max_pods is not None:
            self._values["use_max_pods"] = use_max_pods

    @builtins.property
    def additional_args(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Additional command line arguments to pass to the ``/etc/eks/bootstrap.sh`` command.

        :default: - none

        :see: https://github.com/awslabs/amazon-eks-ami/blob/master/files/bootstrap.sh
        :stability: deprecated
        '''
        result = self._values.get("additional_args")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_api_retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) Number of retry attempts for AWS API call (DescribeCluster).

        :default: 3

        :stability: deprecated
        '''
        result = self._values.get("aws_api_retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def docker_config_json(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The contents of the ``/etc/docker/daemon.json`` file. Useful if you want a custom config differing from the default one in the EKS AMI.

        :default: - none

        :stability: deprecated
        '''
        result = self._values.get("docker_config_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_docker_bridge(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Restores the docker default bridge network.

        :default: false

        :stability: deprecated
        '''
        result = self._values.get("enable_docker_bridge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def kubelet_extra_args(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Extra arguments to add to the kubelet.

        Useful for adding labels or taints.

        :default: - none

        :stability: deprecated

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            --node - labelsfoo = bar , goo = far
        '''
        result = self._values.get("kubelet_extra_args")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_max_pods(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Sets ``--max-pods`` for the kubelet based on the capacity of the EC2 instance.

        :default: true

        :stability: deprecated
        '''
        result = self._values.get("use_max_pods")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BootstrapOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.CapacityOptions",
    jsii_struct_bases=[aws_cdk.aws_autoscaling.CommonAutoScalingGroupProps],
    name_mapping={
        "allow_all_outbound": "allowAllOutbound",
        "associate_public_ip_address": "associatePublicIpAddress",
        "auto_scaling_group_name": "autoScalingGroupName",
        "block_devices": "blockDevices",
        "cooldown": "cooldown",
        "desired_capacity": "desiredCapacity",
        "group_metrics": "groupMetrics",
        "health_check": "healthCheck",
        "ignore_unmodified_size_properties": "ignoreUnmodifiedSizeProperties",
        "instance_monitoring": "instanceMonitoring",
        "key_name": "keyName",
        "max_capacity": "maxCapacity",
        "max_instance_lifetime": "maxInstanceLifetime",
        "min_capacity": "minCapacity",
        "new_instances_protected_from_scale_in": "newInstancesProtectedFromScaleIn",
        "notifications": "notifications",
        "notifications_topic": "notificationsTopic",
        "replacing_update_min_successful_instances_percent": "replacingUpdateMinSuccessfulInstancesPercent",
        "resource_signal_count": "resourceSignalCount",
        "resource_signal_timeout": "resourceSignalTimeout",
        "rolling_update_configuration": "rollingUpdateConfiguration",
        "signals": "signals",
        "spot_price": "spotPrice",
        "update_policy": "updatePolicy",
        "update_type": "updateType",
        "vpc_subnets": "vpcSubnets",
        "instance_type": "instanceType",
        "bootstrap_enabled": "bootstrapEnabled",
        "bootstrap_options": "bootstrapOptions",
        "map_role": "mapRole",
    },
)
class CapacityOptions(aws_cdk.aws_autoscaling.CommonAutoScalingGroupProps):
    def __init__(
        self,
        *,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        associate_public_ip_address: typing.Optional[builtins.bool] = None,
        auto_scaling_group_name: typing.Optional[builtins.str] = None,
        block_devices: typing.Optional[typing.Sequence[aws_cdk.aws_autoscaling.BlockDevice]] = None,
        cooldown: typing.Optional[aws_cdk.core.Duration] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        group_metrics: typing.Optional[typing.Sequence[aws_cdk.aws_autoscaling.GroupMetrics]] = None,
        health_check: typing.Optional[aws_cdk.aws_autoscaling.HealthCheck] = None,
        ignore_unmodified_size_properties: typing.Optional[builtins.bool] = None,
        instance_monitoring: typing.Optional[aws_cdk.aws_autoscaling.Monitoring] = None,
        key_name: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_instance_lifetime: typing.Optional[aws_cdk.core.Duration] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        new_instances_protected_from_scale_in: typing.Optional[builtins.bool] = None,
        notifications: typing.Optional[typing.Sequence[aws_cdk.aws_autoscaling.NotificationConfiguration]] = None,
        notifications_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
        replacing_update_min_successful_instances_percent: typing.Optional[jsii.Number] = None,
        resource_signal_count: typing.Optional[jsii.Number] = None,
        resource_signal_timeout: typing.Optional[aws_cdk.core.Duration] = None,
        rolling_update_configuration: typing.Optional[aws_cdk.aws_autoscaling.RollingUpdateConfiguration] = None,
        signals: typing.Optional[aws_cdk.aws_autoscaling.Signals] = None,
        spot_price: typing.Optional[builtins.str] = None,
        update_policy: typing.Optional[aws_cdk.aws_autoscaling.UpdatePolicy] = None,
        update_type: typing.Optional[aws_cdk.aws_autoscaling.UpdateType] = None,
        vpc_subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection] = None,
        instance_type: aws_cdk.aws_ec2.InstanceType,
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[BootstrapOptions] = None,
        map_role: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(deprecated) Options for adding worker nodes.

        :param allow_all_outbound: Whether the instances can initiate connections to anywhere by default. Default: true
        :param associate_public_ip_address: Whether instances in the Auto Scaling Group should have public IP addresses associated with them. Default: - Use subnet setting.
        :param auto_scaling_group_name: The name of the Auto Scaling group. This name must be unique per Region per account. Default: - Auto generated by CloudFormation
        :param block_devices: Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes. Each instance that is launched has an associated root device volume, either an Amazon EBS volume or an instance store volume. You can use block device mappings to specify additional EBS volumes or instance store volumes to attach to an instance when it is launched. Default: - Uses the block device mapping of the AMI
        :param cooldown: Default scaling cooldown for this AutoScalingGroup. Default: Duration.minutes(5)
        :param desired_capacity: Initial amount of instances in the fleet. If this is set to a number, every deployment will reset the amount of instances to this number. It is recommended to leave this value blank. Default: minCapacity, and leave unchanged during deployment
        :param group_metrics: Enable monitoring for group metrics, these metrics describe the group rather than any of its instances. To report all group metrics use ``GroupMetrics.all()`` Group metrics are reported in a granularity of 1 minute at no additional charge. Default: - no group metrics will be reported
        :param health_check: Configuration for health checks. Default: - HealthCheck.ec2 with no grace period
        :param ignore_unmodified_size_properties: If the ASG has scheduled actions, don't reset unchanged group sizes. Only used if the ASG has scheduled actions (which may scale your ASG up or down regardless of cdk deployments). If true, the size of the group will only be reset if it has been changed in the CDK app. If false, the sizes will always be changed back to what they were in the CDK app on deployment. Default: true
        :param instance_monitoring: Controls whether instances in this group are launched with detailed or basic monitoring. When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes. Default: - Monitoring.DETAILED
        :param key_name: Name of SSH keypair to grant access to instances. Default: - No SSH access will be possible.
        :param max_capacity: Maximum number of instances in the fleet. Default: desiredCapacity
        :param max_instance_lifetime: The maximum amount of time that an instance can be in service. The maximum duration applies to all current and future instances in the group. As an instance approaches its maximum duration, it is terminated and replaced, and cannot be used again. You must specify a value of at least 604,800 seconds (7 days). To clear a previously set value, leave this property undefined. Default: none
        :param min_capacity: Minimum number of instances in the fleet. Default: 1
        :param new_instances_protected_from_scale_in: Whether newly-launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. By default, Auto Scaling can terminate an instance at any time after launch when scaling in an Auto Scaling Group, subject to the group's termination policy. However, you may wish to protect newly-launched instances from being scaled in if they are going to run critical applications that should not be prematurely terminated. This flag must be enabled if the Auto Scaling Group will be associated with an ECS Capacity Provider with managed termination protection. Default: false
        :param notifications: Configure autoscaling group to send notifications about fleet changes to an SNS topic(s). Default: - No fleet change notifications will be sent.
        :param notifications_topic: (deprecated) SNS topic to send notifications about fleet changes. Default: - No fleet change notifications will be sent.
        :param replacing_update_min_successful_instances_percent: (deprecated) Configuration for replacing updates. Only used if updateType == UpdateType.ReplacingUpdate. Specifies how many instances must signal success for the update to succeed. Default: minSuccessfulInstancesPercent
        :param resource_signal_count: (deprecated) How many ResourceSignal calls CloudFormation expects before the resource is considered created. Default: 1 if resourceSignalTimeout is set, 0 otherwise
        :param resource_signal_timeout: (deprecated) The length of time to wait for the resourceSignalCount. The maximum value is 43200 (12 hours). Default: Duration.minutes(5) if resourceSignalCount is set, N/A otherwise
        :param rolling_update_configuration: (deprecated) Configuration for rolling updates. Only used if updateType == UpdateType.RollingUpdate. Default: - RollingUpdateConfiguration with defaults.
        :param signals: Configure waiting for signals during deployment. Use this to pause the CloudFormation deployment to wait for the instances in the AutoScalingGroup to report successful startup during creation and updates. The UserData script needs to invoke ``cfn-signal`` with a success or failure code after it is done setting up the instance. Without waiting for signals, the CloudFormation deployment will proceed as soon as the AutoScalingGroup has been created or updated but before the instances in the group have been started. For example, to have instances wait for an Elastic Load Balancing health check before they signal success, add a health-check verification by using the cfn-init helper script. For an example, see the verify_instance_health command in the Auto Scaling rolling updates sample template: https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/AutoScaling/AutoScalingRollingUpdates.yaml Default: - Do not wait for signals
        :param spot_price: The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. Default: none
        :param update_policy: What to do when an AutoScalingGroup's instance configuration is changed. This is applied when any of the settings on the ASG are changed that affect how the instances should be created (VPC, instance type, startup scripts, etc.). It indicates how the existing instances should be replaced with new instances matching the new config. By default, nothing is done and only new instances are launched with the new config. Default: - ``UpdatePolicy.rollingUpdate()`` if using ``init``, ``UpdatePolicy.none()`` otherwise
        :param update_type: (deprecated) What to do when an AutoScalingGroup's instance configuration is changed. This is applied when any of the settings on the ASG are changed that affect how the instances should be created (VPC, instance type, startup scripts, etc.). It indicates how the existing instances should be replaced with new instances matching the new config. By default, nothing is done and only new instances are launched with the new config. Default: UpdateType.None
        :param vpc_subnets: Where to place instances within the VPC. Default: - All Private subnets.
        :param instance_type: (deprecated) Instance type of the instances to start.
        :param bootstrap_enabled: (deprecated) Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: (deprecated) EKS node bootstrapping options. Default: - none
        :param map_role: (deprecated) Will automatically update the aws-auth ConfigMap to map the IAM instance role to RBAC. This cannot be explicitly set to ``true`` if the cluster has kubectl disabled. Default: - true if the cluster has kubectl enabled (which is the default).

        :stability: deprecated
        '''
        if isinstance(rolling_update_configuration, dict):
            rolling_update_configuration = aws_cdk.aws_autoscaling.RollingUpdateConfiguration(**rolling_update_configuration)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if isinstance(bootstrap_options, dict):
            bootstrap_options = BootstrapOptions(**bootstrap_options)
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
        }
        if allow_all_outbound is not None:
            self._values["allow_all_outbound"] = allow_all_outbound
        if associate_public_ip_address is not None:
            self._values["associate_public_ip_address"] = associate_public_ip_address
        if auto_scaling_group_name is not None:
            self._values["auto_scaling_group_name"] = auto_scaling_group_name
        if block_devices is not None:
            self._values["block_devices"] = block_devices
        if cooldown is not None:
            self._values["cooldown"] = cooldown
        if desired_capacity is not None:
            self._values["desired_capacity"] = desired_capacity
        if group_metrics is not None:
            self._values["group_metrics"] = group_metrics
        if health_check is not None:
            self._values["health_check"] = health_check
        if ignore_unmodified_size_properties is not None:
            self._values["ignore_unmodified_size_properties"] = ignore_unmodified_size_properties
        if instance_monitoring is not None:
            self._values["instance_monitoring"] = instance_monitoring
        if key_name is not None:
            self._values["key_name"] = key_name
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if max_instance_lifetime is not None:
            self._values["max_instance_lifetime"] = max_instance_lifetime
        if min_capacity is not None:
            self._values["min_capacity"] = min_capacity
        if new_instances_protected_from_scale_in is not None:
            self._values["new_instances_protected_from_scale_in"] = new_instances_protected_from_scale_in
        if notifications is not None:
            self._values["notifications"] = notifications
        if notifications_topic is not None:
            self._values["notifications_topic"] = notifications_topic
        if replacing_update_min_successful_instances_percent is not None:
            self._values["replacing_update_min_successful_instances_percent"] = replacing_update_min_successful_instances_percent
        if resource_signal_count is not None:
            self._values["resource_signal_count"] = resource_signal_count
        if resource_signal_timeout is not None:
            self._values["resource_signal_timeout"] = resource_signal_timeout
        if rolling_update_configuration is not None:
            self._values["rolling_update_configuration"] = rolling_update_configuration
        if signals is not None:
            self._values["signals"] = signals
        if spot_price is not None:
            self._values["spot_price"] = spot_price
        if update_policy is not None:
            self._values["update_policy"] = update_policy
        if update_type is not None:
            self._values["update_type"] = update_type
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if bootstrap_enabled is not None:
            self._values["bootstrap_enabled"] = bootstrap_enabled
        if bootstrap_options is not None:
            self._values["bootstrap_options"] = bootstrap_options
        if map_role is not None:
            self._values["map_role"] = map_role

    @builtins.property
    def allow_all_outbound(self) -> typing.Optional[builtins.bool]:
        '''Whether the instances can initiate connections to anywhere by default.

        :default: true
        '''
        result = self._values.get("allow_all_outbound")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def associate_public_ip_address(self) -> typing.Optional[builtins.bool]:
        '''Whether instances in the Auto Scaling Group should have public IP addresses associated with them.

        :default: - Use subnet setting.
        '''
        result = self._values.get("associate_public_ip_address")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def auto_scaling_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Auto Scaling group.

        This name must be unique per Region per account.

        :default: - Auto generated by CloudFormation
        '''
        result = self._values.get("auto_scaling_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_devices(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_autoscaling.BlockDevice]]:
        '''Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes.

        Each instance that is launched has an associated root device volume,
        either an Amazon EBS volume or an instance store volume.
        You can use block device mappings to specify additional EBS volumes or
        instance store volumes to attach to an instance when it is launched.

        :default: - Uses the block device mapping of the AMI

        :see: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html
        '''
        result = self._values.get("block_devices")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_autoscaling.BlockDevice]], result)

    @builtins.property
    def cooldown(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''Default scaling cooldown for this AutoScalingGroup.

        :default: Duration.minutes(5)
        '''
        result = self._values.get("cooldown")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        '''Initial amount of instances in the fleet.

        If this is set to a number, every deployment will reset the amount of
        instances to this number. It is recommended to leave this value blank.

        :default: minCapacity, and leave unchanged during deployment

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-desiredcapacity
        '''
        result = self._values.get("desired_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def group_metrics(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_autoscaling.GroupMetrics]]:
        '''Enable monitoring for group metrics, these metrics describe the group rather than any of its instances.

        To report all group metrics use ``GroupMetrics.all()``
        Group metrics are reported in a granularity of 1 minute at no additional charge.

        :default: - no group metrics will be reported
        '''
        result = self._values.get("group_metrics")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_autoscaling.GroupMetrics]], result)

    @builtins.property
    def health_check(self) -> typing.Optional[aws_cdk.aws_autoscaling.HealthCheck]:
        '''Configuration for health checks.

        :default: - HealthCheck.ec2 with no grace period
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional[aws_cdk.aws_autoscaling.HealthCheck], result)

    @builtins.property
    def ignore_unmodified_size_properties(self) -> typing.Optional[builtins.bool]:
        '''If the ASG has scheduled actions, don't reset unchanged group sizes.

        Only used if the ASG has scheduled actions (which may scale your ASG up
        or down regardless of cdk deployments). If true, the size of the group
        will only be reset if it has been changed in the CDK app. If false, the
        sizes will always be changed back to what they were in the CDK app
        on deployment.

        :default: true
        '''
        result = self._values.get("ignore_unmodified_size_properties")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_monitoring(
        self,
    ) -> typing.Optional[aws_cdk.aws_autoscaling.Monitoring]:
        '''Controls whether instances in this group are launched with detailed or basic monitoring.

        When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account
        is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes.

        :default: - Monitoring.DETAILED

        :see: https://docs.aws.amazon.com/autoscaling/latest/userguide/as-instance-monitoring.html#enable-as-instance-metrics
        '''
        result = self._values.get("instance_monitoring")
        return typing.cast(typing.Optional[aws_cdk.aws_autoscaling.Monitoring], result)

    @builtins.property
    def key_name(self) -> typing.Optional[builtins.str]:
        '''Name of SSH keypair to grant access to instances.

        :default: - No SSH access will be possible.
        '''
        result = self._values.get("key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of instances in the fleet.

        :default: desiredCapacity
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_instance_lifetime(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum amount of time that an instance can be in service.

        The maximum duration applies
        to all current and future instances in the group. As an instance approaches its maximum duration,
        it is terminated and replaced, and cannot be used again.

        You must specify a value of at least 604,800 seconds (7 days). To clear a previously set value,
        leave this property undefined.

        :default: none

        :see: https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-max-instance-lifetime.html
        '''
        result = self._values.get("max_instance_lifetime")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def min_capacity(self) -> typing.Optional[jsii.Number]:
        '''Minimum number of instances in the fleet.

        :default: 1
        '''
        result = self._values.get("min_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def new_instances_protected_from_scale_in(self) -> typing.Optional[builtins.bool]:
        '''Whether newly-launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in.

        By default, Auto Scaling can terminate an instance at any time after launch
        when scaling in an Auto Scaling Group, subject to the group's termination
        policy. However, you may wish to protect newly-launched instances from
        being scaled in if they are going to run critical applications that should
        not be prematurely terminated.

        This flag must be enabled if the Auto Scaling Group will be associated with
        an ECS Capacity Provider with managed termination protection.

        :default: false
        '''
        result = self._values.get("new_instances_protected_from_scale_in")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notifications(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_autoscaling.NotificationConfiguration]]:
        '''Configure autoscaling group to send notifications about fleet changes to an SNS topic(s).

        :default: - No fleet change notifications will be sent.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-notificationconfigurations
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_autoscaling.NotificationConfiguration]], result)

    @builtins.property
    def notifications_topic(self) -> typing.Optional[aws_cdk.aws_sns.ITopic]:
        '''(deprecated) SNS topic to send notifications about fleet changes.

        :default: - No fleet change notifications will be sent.

        :deprecated: use ``notifications``

        :stability: deprecated
        '''
        result = self._values.get("notifications_topic")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.ITopic], result)

    @builtins.property
    def replacing_update_min_successful_instances_percent(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''(deprecated) Configuration for replacing updates.

        Only used if updateType == UpdateType.ReplacingUpdate. Specifies how
        many instances must signal success for the update to succeed.

        :default: minSuccessfulInstancesPercent

        :deprecated: Use ``signals`` instead

        :stability: deprecated
        '''
        result = self._values.get("replacing_update_min_successful_instances_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_signal_count(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) How many ResourceSignal calls CloudFormation expects before the resource is considered created.

        :default: 1 if resourceSignalTimeout is set, 0 otherwise

        :deprecated: Use ``signals`` instead.

        :stability: deprecated
        '''
        result = self._values.get("resource_signal_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def resource_signal_timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''(deprecated) The length of time to wait for the resourceSignalCount.

        The maximum value is 43200 (12 hours).

        :default: Duration.minutes(5) if resourceSignalCount is set, N/A otherwise

        :deprecated: Use ``signals`` instead.

        :stability: deprecated
        '''
        result = self._values.get("resource_signal_timeout")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def rolling_update_configuration(
        self,
    ) -> typing.Optional[aws_cdk.aws_autoscaling.RollingUpdateConfiguration]:
        '''(deprecated) Configuration for rolling updates.

        Only used if updateType == UpdateType.RollingUpdate.

        :default: - RollingUpdateConfiguration with defaults.

        :deprecated: Use ``updatePolicy`` instead

        :stability: deprecated
        '''
        result = self._values.get("rolling_update_configuration")
        return typing.cast(typing.Optional[aws_cdk.aws_autoscaling.RollingUpdateConfiguration], result)

    @builtins.property
    def signals(self) -> typing.Optional[aws_cdk.aws_autoscaling.Signals]:
        '''Configure waiting for signals during deployment.

        Use this to pause the CloudFormation deployment to wait for the instances
        in the AutoScalingGroup to report successful startup during
        creation and updates. The UserData script needs to invoke ``cfn-signal``
        with a success or failure code after it is done setting up the instance.

        Without waiting for signals, the CloudFormation deployment will proceed as
        soon as the AutoScalingGroup has been created or updated but before the
        instances in the group have been started.

        For example, to have instances wait for an Elastic Load Balancing health check before
        they signal success, add a health-check verification by using the
        cfn-init helper script. For an example, see the verify_instance_health
        command in the Auto Scaling rolling updates sample template:

        https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/AutoScaling/AutoScalingRollingUpdates.yaml

        :default: - Do not wait for signals
        '''
        result = self._values.get("signals")
        return typing.cast(typing.Optional[aws_cdk.aws_autoscaling.Signals], result)

    @builtins.property
    def spot_price(self) -> typing.Optional[builtins.str]:
        '''The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request.

        Spot Instances are
        launched when the price you specify exceeds the current Spot market price.

        :default: none
        '''
        result = self._values.get("spot_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_policy(self) -> typing.Optional[aws_cdk.aws_autoscaling.UpdatePolicy]:
        '''What to do when an AutoScalingGroup's instance configuration is changed.

        This is applied when any of the settings on the ASG are changed that
        affect how the instances should be created (VPC, instance type, startup
        scripts, etc.). It indicates how the existing instances should be
        replaced with new instances matching the new config. By default, nothing
        is done and only new instances are launched with the new config.

        :default: - ``UpdatePolicy.rollingUpdate()`` if using ``init``, ``UpdatePolicy.none()`` otherwise
        '''
        result = self._values.get("update_policy")
        return typing.cast(typing.Optional[aws_cdk.aws_autoscaling.UpdatePolicy], result)

    @builtins.property
    def update_type(self) -> typing.Optional[aws_cdk.aws_autoscaling.UpdateType]:
        '''(deprecated) What to do when an AutoScalingGroup's instance configuration is changed.

        This is applied when any of the settings on the ASG are changed that
        affect how the instances should be created (VPC, instance type, startup
        scripts, etc.). It indicates how the existing instances should be
        replaced with new instances matching the new config. By default, nothing
        is done and only new instances are launched with the new config.

        :default: UpdateType.None

        :deprecated: Use ``updatePolicy`` instead

        :stability: deprecated
        '''
        result = self._values.get("update_type")
        return typing.cast(typing.Optional[aws_cdk.aws_autoscaling.UpdateType], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''Where to place instances within the VPC.

        :default: - All Private subnets.
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def instance_type(self) -> aws_cdk.aws_ec2.InstanceType:
        '''(deprecated) Instance type of the instances to start.

        :stability: deprecated
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(aws_cdk.aws_ec2.InstanceType, result)

    @builtins.property
    def bootstrap_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster.

        If you wish to provide a custom user data script, set this to ``false`` and
        manually invoke ``autoscalingGroup.addUserData()``.

        :default: true

        :stability: deprecated
        '''
        result = self._values.get("bootstrap_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def bootstrap_options(self) -> typing.Optional[BootstrapOptions]:
        '''(deprecated) EKS node bootstrapping options.

        :default: - none

        :stability: deprecated
        '''
        result = self._values.get("bootstrap_options")
        return typing.cast(typing.Optional[BootstrapOptions], result)

    @builtins.property
    def map_role(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Will automatically update the aws-auth ConfigMap to map the IAM instance role to RBAC.

        This cannot be explicitly set to ``true`` if the cluster has kubectl disabled.

        :default: - true if the cluster has kubectl enabled (which is the default).

        :stability: deprecated
        '''
        result = self._values.get("map_role")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapacityOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAddon(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.CfnAddon",
):
    '''A CloudFormation ``AWS::EKS::Addon``.

    :cloudformationResource: AWS::EKS::Addon
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        addon_name: builtins.str,
        cluster_name: builtins.str,
        addon_version: typing.Optional[builtins.str] = None,
        resolve_conflicts: typing.Optional[builtins.str] = None,
        service_account_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::EKS::Addon``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param addon_name: ``AWS::EKS::Addon.AddonName``.
        :param cluster_name: ``AWS::EKS::Addon.ClusterName``.
        :param addon_version: ``AWS::EKS::Addon.AddonVersion``.
        :param resolve_conflicts: ``AWS::EKS::Addon.ResolveConflicts``.
        :param service_account_role_arn: ``AWS::EKS::Addon.ServiceAccountRoleArn``.
        :param tags: ``AWS::EKS::Addon.Tags``.
        '''
        props = CfnAddonProps(
            addon_name=addon_name,
            cluster_name=cluster_name,
            addon_version=addon_version,
            resolve_conflicts=resolve_conflicts,
            service_account_role_arn=service_account_role_arn,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::EKS::Addon.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="addonName")
    def addon_name(self) -> builtins.str:
        '''``AWS::EKS::Addon.AddonName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-addonname
        '''
        return typing.cast(builtins.str, jsii.get(self, "addonName"))

    @addon_name.setter
    def addon_name(self, value: builtins.str) -> None:
        jsii.set(self, "addonName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''``AWS::EKS::Addon.ClusterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-clustername
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        jsii.set(self, "clusterName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="addonVersion")
    def addon_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Addon.AddonVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-addonversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addonVersion"))

    @addon_version.setter
    def addon_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "addonVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resolveConflicts")
    def resolve_conflicts(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Addon.ResolveConflicts``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-resolveconflicts
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolveConflicts"))

    @resolve_conflicts.setter
    def resolve_conflicts(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resolveConflicts", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Addon.ServiceAccountRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-serviceaccountrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountRoleArn"))

    @service_account_role_arn.setter
    def service_account_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serviceAccountRoleArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.CfnAddonProps",
    jsii_struct_bases=[],
    name_mapping={
        "addon_name": "addonName",
        "cluster_name": "clusterName",
        "addon_version": "addonVersion",
        "resolve_conflicts": "resolveConflicts",
        "service_account_role_arn": "serviceAccountRoleArn",
        "tags": "tags",
    },
)
class CfnAddonProps:
    def __init__(
        self,
        *,
        addon_name: builtins.str,
        cluster_name: builtins.str,
        addon_version: typing.Optional[builtins.str] = None,
        resolve_conflicts: typing.Optional[builtins.str] = None,
        service_account_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EKS::Addon``.

        :param addon_name: ``AWS::EKS::Addon.AddonName``.
        :param cluster_name: ``AWS::EKS::Addon.ClusterName``.
        :param addon_version: ``AWS::EKS::Addon.AddonVersion``.
        :param resolve_conflicts: ``AWS::EKS::Addon.ResolveConflicts``.
        :param service_account_role_arn: ``AWS::EKS::Addon.ServiceAccountRoleArn``.
        :param tags: ``AWS::EKS::Addon.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "addon_name": addon_name,
            "cluster_name": cluster_name,
        }
        if addon_version is not None:
            self._values["addon_version"] = addon_version
        if resolve_conflicts is not None:
            self._values["resolve_conflicts"] = resolve_conflicts
        if service_account_role_arn is not None:
            self._values["service_account_role_arn"] = service_account_role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def addon_name(self) -> builtins.str:
        '''``AWS::EKS::Addon.AddonName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-addonname
        '''
        result = self._values.get("addon_name")
        assert result is not None, "Required property 'addon_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''``AWS::EKS::Addon.ClusterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addon_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Addon.AddonVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-addonversion
        '''
        result = self._values.get("addon_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolve_conflicts(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Addon.ResolveConflicts``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-resolveconflicts
        '''
        result = self._values.get("resolve_conflicts")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Addon.ServiceAccountRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-serviceaccountrolearn
        '''
        result = self._values.get("service_account_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::EKS::Addon.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-addon.html#cfn-eks-addon-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAddonProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.CfnCluster",
):
    '''A CloudFormation ``AWS::EKS::Cluster``.

    :cloudformationResource: AWS::EKS::Cluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resources_vpc_config: typing.Union["CfnCluster.ResourcesVpcConfigProperty", aws_cdk.core.IResolvable],
        role_arn: builtins.str,
        encryption_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionConfigProperty"]]]] = None,
        kubernetes_network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KubernetesNetworkConfigProperty"]] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::EKS::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resources_vpc_config: ``AWS::EKS::Cluster.ResourcesVpcConfig``.
        :param role_arn: ``AWS::EKS::Cluster.RoleArn``.
        :param encryption_config: ``AWS::EKS::Cluster.EncryptionConfig``.
        :param kubernetes_network_config: ``AWS::EKS::Cluster.KubernetesNetworkConfig``.
        :param name: ``AWS::EKS::Cluster.Name``.
        :param version: ``AWS::EKS::Cluster.Version``.
        '''
        props = CfnClusterProps(
            resources_vpc_config=resources_vpc_config,
            role_arn=role_arn,
            encryption_config=encryption_config,
            kubernetes_network_config=kubernetes_network_config,
            name=name,
            version=version,
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
    @jsii.member(jsii_name="attrCertificateAuthorityData")
    def attr_certificate_authority_data(self) -> builtins.str:
        '''
        :cloudformationAttribute: CertificateAuthorityData
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificateAuthorityData"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrClusterSecurityGroupId")
    def attr_cluster_security_group_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ClusterSecurityGroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterSecurityGroupId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEncryptionConfigKeyArn")
    def attr_encryption_config_key_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: EncryptionConfigKeyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEncryptionConfigKeyArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''
        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOpenIdConnectIssuerUrl")
    def attr_open_id_connect_issuer_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: OpenIdConnectIssuerUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOpenIdConnectIssuerUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourcesVpcConfig")
    def resources_vpc_config(
        self,
    ) -> typing.Union["CfnCluster.ResourcesVpcConfigProperty", aws_cdk.core.IResolvable]:
        '''``AWS::EKS::Cluster.ResourcesVpcConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-resourcesvpcconfig
        '''
        return typing.cast(typing.Union["CfnCluster.ResourcesVpcConfigProperty", aws_cdk.core.IResolvable], jsii.get(self, "resourcesVpcConfig"))

    @resources_vpc_config.setter
    def resources_vpc_config(
        self,
        value: typing.Union["CfnCluster.ResourcesVpcConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "resourcesVpcConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::EKS::Cluster.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionConfigProperty"]]]]:
        '''``AWS::EKS::Cluster.EncryptionConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-encryptionconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionConfigProperty"]]]], jsii.get(self, "encryptionConfig"))

    @encryption_config.setter
    def encryption_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionConfigProperty"]]]],
    ) -> None:
        jsii.set(self, "encryptionConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kubernetesNetworkConfig")
    def kubernetes_network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KubernetesNetworkConfigProperty"]]:
        '''``AWS::EKS::Cluster.KubernetesNetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-kubernetesnetworkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KubernetesNetworkConfigProperty"]], jsii.get(self, "kubernetesNetworkConfig"))

    @kubernetes_network_config.setter
    def kubernetes_network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.KubernetesNetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "kubernetesNetworkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Cluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Cluster.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-version
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "version", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnCluster.EncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"provider": "provider", "resources": "resources"},
    )
    class EncryptionConfigProperty:
        def __init__(
            self,
            *,
            provider: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ProviderProperty"]] = None,
            resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param provider: ``CfnCluster.EncryptionConfigProperty.Provider``.
            :param resources: ``CfnCluster.EncryptionConfigProperty.Resources``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if provider is not None:
                self._values["provider"] = provider
            if resources is not None:
                self._values["resources"] = resources

        @builtins.property
        def provider(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ProviderProperty"]]:
            '''``CfnCluster.EncryptionConfigProperty.Provider``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html#cfn-eks-cluster-encryptionconfig-provider
            '''
            result = self._values.get("provider")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ProviderProperty"]], result)

        @builtins.property
        def resources(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCluster.EncryptionConfigProperty.Resources``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-encryptionconfig.html#cfn-eks-cluster-encryptionconfig-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnCluster.KubernetesNetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"service_ipv4_cidr": "serviceIpv4Cidr"},
    )
    class KubernetesNetworkConfigProperty:
        def __init__(
            self,
            *,
            service_ipv4_cidr: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param service_ipv4_cidr: ``CfnCluster.KubernetesNetworkConfigProperty.ServiceIpv4Cidr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if service_ipv4_cidr is not None:
                self._values["service_ipv4_cidr"] = service_ipv4_cidr

        @builtins.property
        def service_ipv4_cidr(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.KubernetesNetworkConfigProperty.ServiceIpv4Cidr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-kubernetesnetworkconfig.html#cfn-eks-cluster-kubernetesnetworkconfig-serviceipv4cidr
            '''
            result = self._values.get("service_ipv4_cidr")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KubernetesNetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnCluster.ProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"key_arn": "keyArn"},
    )
    class ProviderProperty:
        def __init__(self, *, key_arn: typing.Optional[builtins.str] = None) -> None:
            '''
            :param key_arn: ``CfnCluster.ProviderProperty.KeyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnCluster.ProviderProperty.KeyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-provider.html#cfn-eks-cluster-provider-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnCluster.ResourcesVpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "subnet_ids": "subnetIds",
            "security_group_ids": "securityGroupIds",
        },
    )
    class ResourcesVpcConfigProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param subnet_ids: ``CfnCluster.ResourcesVpcConfigProperty.SubnetIds``.
            :param security_group_ids: ``CfnCluster.ResourcesVpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "subnet_ids": subnet_ids,
            }
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''``CfnCluster.ResourcesVpcConfigProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html#cfn-eks-cluster-resourcesvpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCluster.ResourcesVpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-cluster-resourcesvpcconfig.html#cfn-eks-cluster-resourcesvpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourcesVpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "resources_vpc_config": "resourcesVpcConfig",
        "role_arn": "roleArn",
        "encryption_config": "encryptionConfig",
        "kubernetes_network_config": "kubernetesNetworkConfig",
        "name": "name",
        "version": "version",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        resources_vpc_config: typing.Union[CfnCluster.ResourcesVpcConfigProperty, aws_cdk.core.IResolvable],
        role_arn: builtins.str,
        encryption_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnCluster.EncryptionConfigProperty]]]] = None,
        kubernetes_network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.KubernetesNetworkConfigProperty]] = None,
        name: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EKS::Cluster``.

        :param resources_vpc_config: ``AWS::EKS::Cluster.ResourcesVpcConfig``.
        :param role_arn: ``AWS::EKS::Cluster.RoleArn``.
        :param encryption_config: ``AWS::EKS::Cluster.EncryptionConfig``.
        :param kubernetes_network_config: ``AWS::EKS::Cluster.KubernetesNetworkConfig``.
        :param name: ``AWS::EKS::Cluster.Name``.
        :param version: ``AWS::EKS::Cluster.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resources_vpc_config": resources_vpc_config,
            "role_arn": role_arn,
        }
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config
        if kubernetes_network_config is not None:
            self._values["kubernetes_network_config"] = kubernetes_network_config
        if name is not None:
            self._values["name"] = name
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def resources_vpc_config(
        self,
    ) -> typing.Union[CfnCluster.ResourcesVpcConfigProperty, aws_cdk.core.IResolvable]:
        '''``AWS::EKS::Cluster.ResourcesVpcConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-resourcesvpcconfig
        '''
        result = self._values.get("resources_vpc_config")
        assert result is not None, "Required property 'resources_vpc_config' is missing"
        return typing.cast(typing.Union[CfnCluster.ResourcesVpcConfigProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::EKS::Cluster.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.EncryptionConfigProperty]]]]:
        '''``AWS::EKS::Cluster.EncryptionConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-encryptionconfig
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCluster.EncryptionConfigProperty]]]], result)

    @builtins.property
    def kubernetes_network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.KubernetesNetworkConfigProperty]]:
        '''``AWS::EKS::Cluster.KubernetesNetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-kubernetesnetworkconfig
        '''
        result = self._values.get("kubernetes_network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.KubernetesNetworkConfigProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Cluster.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Cluster.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html#cfn-eks-cluster-version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFargateProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.CfnFargateProfile",
):
    '''A CloudFormation ``AWS::EKS::FargateProfile``.

    :cloudformationResource: AWS::EKS::FargateProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        pod_execution_role_arn: builtins.str,
        selectors: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFargateProfile.SelectorProperty"]]],
        fargate_profile_name: typing.Optional[builtins.str] = None,
        subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::EKS::FargateProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: ``AWS::EKS::FargateProfile.ClusterName``.
        :param pod_execution_role_arn: ``AWS::EKS::FargateProfile.PodExecutionRoleArn``.
        :param selectors: ``AWS::EKS::FargateProfile.Selectors``.
        :param fargate_profile_name: ``AWS::EKS::FargateProfile.FargateProfileName``.
        :param subnets: ``AWS::EKS::FargateProfile.Subnets``.
        :param tags: ``AWS::EKS::FargateProfile.Tags``.
        '''
        props = CfnFargateProfileProps(
            cluster_name=cluster_name,
            pod_execution_role_arn=pod_execution_role_arn,
            selectors=selectors,
            fargate_profile_name=fargate_profile_name,
            subnets=subnets,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::EKS::FargateProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''``AWS::EKS::FargateProfile.ClusterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-clustername
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        jsii.set(self, "clusterName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="podExecutionRoleArn")
    def pod_execution_role_arn(self) -> builtins.str:
        '''``AWS::EKS::FargateProfile.PodExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-podexecutionrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "podExecutionRoleArn"))

    @pod_execution_role_arn.setter
    def pod_execution_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "podExecutionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="selectors")
    def selectors(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFargateProfile.SelectorProperty"]]]:
        '''``AWS::EKS::FargateProfile.Selectors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-selectors
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFargateProfile.SelectorProperty"]]], jsii.get(self, "selectors"))

    @selectors.setter
    def selectors(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFargateProfile.SelectorProperty"]]],
    ) -> None:
        jsii.set(self, "selectors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fargateProfileName")
    def fargate_profile_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::FargateProfile.FargateProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-fargateprofilename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fargateProfileName"))

    @fargate_profile_name.setter
    def fargate_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "fargateProfileName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::EKS::FargateProfile.Subnets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-subnets
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "subnets", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnFargateProfile.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class LabelProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnFargateProfile.LabelProperty.Key``.
            :param value: ``CfnFargateProfile.LabelProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnFargateProfile.LabelProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html#cfn-eks-fargateprofile-label-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnFargateProfile.LabelProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-label.html#cfn-eks-fargateprofile-label-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnFargateProfile.SelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace", "labels": "labels"},
    )
    class SelectorProperty:
        def __init__(
            self,
            *,
            namespace: builtins.str,
            labels: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFargateProfile.LabelProperty"]]]] = None,
        ) -> None:
            '''
            :param namespace: ``CfnFargateProfile.SelectorProperty.Namespace``.
            :param labels: ``CfnFargateProfile.SelectorProperty.Labels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "namespace": namespace,
            }
            if labels is not None:
                self._values["labels"] = labels

        @builtins.property
        def namespace(self) -> builtins.str:
            '''``CfnFargateProfile.SelectorProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html#cfn-eks-fargateprofile-selector-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def labels(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFargateProfile.LabelProperty"]]]]:
            '''``CfnFargateProfile.SelectorProperty.Labels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-fargateprofile-selector.html#cfn-eks-fargateprofile-selector-labels
            '''
            result = self._values.get("labels")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFargateProfile.LabelProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.CfnFargateProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "pod_execution_role_arn": "podExecutionRoleArn",
        "selectors": "selectors",
        "fargate_profile_name": "fargateProfileName",
        "subnets": "subnets",
        "tags": "tags",
    },
)
class CfnFargateProfileProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        pod_execution_role_arn: builtins.str,
        selectors: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnFargateProfile.SelectorProperty]]],
        fargate_profile_name: typing.Optional[builtins.str] = None,
        subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EKS::FargateProfile``.

        :param cluster_name: ``AWS::EKS::FargateProfile.ClusterName``.
        :param pod_execution_role_arn: ``AWS::EKS::FargateProfile.PodExecutionRoleArn``.
        :param selectors: ``AWS::EKS::FargateProfile.Selectors``.
        :param fargate_profile_name: ``AWS::EKS::FargateProfile.FargateProfileName``.
        :param subnets: ``AWS::EKS::FargateProfile.Subnets``.
        :param tags: ``AWS::EKS::FargateProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
            "pod_execution_role_arn": pod_execution_role_arn,
            "selectors": selectors,
        }
        if fargate_profile_name is not None:
            self._values["fargate_profile_name"] = fargate_profile_name
        if subnets is not None:
            self._values["subnets"] = subnets
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''``AWS::EKS::FargateProfile.ClusterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pod_execution_role_arn(self) -> builtins.str:
        '''``AWS::EKS::FargateProfile.PodExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-podexecutionrolearn
        '''
        result = self._values.get("pod_execution_role_arn")
        assert result is not None, "Required property 'pod_execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selectors(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnFargateProfile.SelectorProperty]]]:
        '''``AWS::EKS::FargateProfile.Selectors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-selectors
        '''
        result = self._values.get("selectors")
        assert result is not None, "Required property 'selectors' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnFargateProfile.SelectorProperty]]], result)

    @builtins.property
    def fargate_profile_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::FargateProfile.FargateProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-fargateprofilename
        '''
        result = self._values.get("fargate_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::EKS::FargateProfile.Subnets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-subnets
        '''
        result = self._values.get("subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::EKS::FargateProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-fargateprofile.html#cfn-eks-fargateprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFargateProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNodegroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.CfnNodegroup",
):
    '''A CloudFormation ``AWS::EKS::Nodegroup``.

    :cloudformationResource: AWS::EKS::Nodegroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        node_role: builtins.str,
        subnets: typing.Sequence[builtins.str],
        ami_type: typing.Optional[builtins.str] = None,
        capacity_type: typing.Optional[builtins.str] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        force_update_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        labels: typing.Any = None,
        launch_template: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.LaunchTemplateSpecificationProperty"]] = None,
        nodegroup_name: typing.Optional[builtins.str] = None,
        release_version: typing.Optional[builtins.str] = None,
        remote_access: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.RemoteAccessProperty"]] = None,
        scaling_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.ScalingConfigProperty"]] = None,
        tags: typing.Any = None,
        taints: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.TaintProperty"]]]] = None,
        update_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.UpdateConfigProperty"]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::EKS::Nodegroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_name: ``AWS::EKS::Nodegroup.ClusterName``.
        :param node_role: ``AWS::EKS::Nodegroup.NodeRole``.
        :param subnets: ``AWS::EKS::Nodegroup.Subnets``.
        :param ami_type: ``AWS::EKS::Nodegroup.AmiType``.
        :param capacity_type: ``AWS::EKS::Nodegroup.CapacityType``.
        :param disk_size: ``AWS::EKS::Nodegroup.DiskSize``.
        :param force_update_enabled: ``AWS::EKS::Nodegroup.ForceUpdateEnabled``.
        :param instance_types: ``AWS::EKS::Nodegroup.InstanceTypes``.
        :param labels: ``AWS::EKS::Nodegroup.Labels``.
        :param launch_template: ``AWS::EKS::Nodegroup.LaunchTemplate``.
        :param nodegroup_name: ``AWS::EKS::Nodegroup.NodegroupName``.
        :param release_version: ``AWS::EKS::Nodegroup.ReleaseVersion``.
        :param remote_access: ``AWS::EKS::Nodegroup.RemoteAccess``.
        :param scaling_config: ``AWS::EKS::Nodegroup.ScalingConfig``.
        :param tags: ``AWS::EKS::Nodegroup.Tags``.
        :param taints: ``AWS::EKS::Nodegroup.Taints``.
        :param update_config: ``AWS::EKS::Nodegroup.UpdateConfig``.
        :param version: ``AWS::EKS::Nodegroup.Version``.
        '''
        props = CfnNodegroupProps(
            cluster_name=cluster_name,
            node_role=node_role,
            subnets=subnets,
            ami_type=ami_type,
            capacity_type=capacity_type,
            disk_size=disk_size,
            force_update_enabled=force_update_enabled,
            instance_types=instance_types,
            labels=labels,
            launch_template=launch_template,
            nodegroup_name=nodegroup_name,
            release_version=release_version,
            remote_access=remote_access,
            scaling_config=scaling_config,
            tags=tags,
            taints=taints,
            update_config=update_config,
            version=version,
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
    @jsii.member(jsii_name="attrClusterName")
    def attr_cluster_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ClusterName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrClusterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrNodegroupName")
    def attr_nodegroup_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: NodegroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNodegroupName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::EKS::Nodegroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''``AWS::EKS::Nodegroup.ClusterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-clustername
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        jsii.set(self, "clusterName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Any:
        '''``AWS::EKS::Nodegroup.Labels``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-labels
        '''
        return typing.cast(typing.Any, jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Any) -> None:
        jsii.set(self, "labels", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nodeRole")
    def node_role(self) -> builtins.str:
        '''``AWS::EKS::Nodegroup.NodeRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-noderole
        '''
        return typing.cast(builtins.str, jsii.get(self, "nodeRole"))

    @node_role.setter
    def node_role(self, value: builtins.str) -> None:
        jsii.set(self, "nodeRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        '''``AWS::EKS::Nodegroup.Subnets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-subnets
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "subnets", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="amiType")
    def ami_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.AmiType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-amitype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amiType"))

    @ami_type.setter
    def ami_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "amiType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="capacityType")
    def capacity_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.CapacityType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-capacitytype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityType"))

    @capacity_type.setter
    def capacity_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "capacityType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="diskSize")
    def disk_size(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EKS::Nodegroup.DiskSize``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-disksize
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSize"))

    @disk_size.setter
    def disk_size(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "diskSize", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="forceUpdateEnabled")
    def force_update_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::EKS::Nodegroup.ForceUpdateEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-forceupdateenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "forceUpdateEnabled"))

    @force_update_enabled.setter
    def force_update_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "forceUpdateEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceTypes")
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::EKS::Nodegroup.InstanceTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-instancetypes
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceTypes"))

    @instance_types.setter
    def instance_types(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "instanceTypes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.LaunchTemplateSpecificationProperty"]]:
        '''``AWS::EKS::Nodegroup.LaunchTemplate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-launchtemplate
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.LaunchTemplateSpecificationProperty"]], jsii.get(self, "launchTemplate"))

    @launch_template.setter
    def launch_template(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.LaunchTemplateSpecificationProperty"]],
    ) -> None:
        jsii.set(self, "launchTemplate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nodegroupName")
    def nodegroup_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.NodegroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-nodegroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodegroupName"))

    @nodegroup_name.setter
    def nodegroup_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "nodegroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="releaseVersion")
    def release_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.ReleaseVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-releaseversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "releaseVersion"))

    @release_version.setter
    def release_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "releaseVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="remoteAccess")
    def remote_access(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.RemoteAccessProperty"]]:
        '''``AWS::EKS::Nodegroup.RemoteAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-remoteaccess
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.RemoteAccessProperty"]], jsii.get(self, "remoteAccess"))

    @remote_access.setter
    def remote_access(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.RemoteAccessProperty"]],
    ) -> None:
        jsii.set(self, "remoteAccess", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalingConfig")
    def scaling_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.ScalingConfigProperty"]]:
        '''``AWS::EKS::Nodegroup.ScalingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-scalingconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.ScalingConfigProperty"]], jsii.get(self, "scalingConfig"))

    @scaling_config.setter
    def scaling_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.ScalingConfigProperty"]],
    ) -> None:
        jsii.set(self, "scalingConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="taints")
    def taints(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.TaintProperty"]]]]:
        '''``AWS::EKS::Nodegroup.Taints``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-taints
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.TaintProperty"]]]], jsii.get(self, "taints"))

    @taints.setter
    def taints(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.TaintProperty"]]]],
    ) -> None:
        jsii.set(self, "taints", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updateConfig")
    def update_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.UpdateConfigProperty"]]:
        '''``AWS::EKS::Nodegroup.UpdateConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-updateconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.UpdateConfigProperty"]], jsii.get(self, "updateConfig"))

    @update_config.setter
    def update_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnNodegroup.UpdateConfigProperty"]],
    ) -> None:
        jsii.set(self, "updateConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-version
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "version", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnNodegroup.LaunchTemplateSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "name": "name", "version": "version"},
    )
    class LaunchTemplateSpecificationProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param id: ``CfnNodegroup.LaunchTemplateSpecificationProperty.Id``.
            :param name: ``CfnNodegroup.LaunchTemplateSpecificationProperty.Name``.
            :param version: ``CfnNodegroup.LaunchTemplateSpecificationProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if name is not None:
                self._values["name"] = name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnNodegroup.LaunchTemplateSpecificationProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html#cfn-eks-nodegroup-launchtemplatespecification-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnNodegroup.LaunchTemplateSpecificationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html#cfn-eks-nodegroup-launchtemplatespecification-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''``CfnNodegroup.LaunchTemplateSpecificationProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-launchtemplatespecification.html#cfn-eks-nodegroup-launchtemplatespecification-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchTemplateSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnNodegroup.RemoteAccessProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ec2_ssh_key": "ec2SshKey",
            "source_security_groups": "sourceSecurityGroups",
        },
    )
    class RemoteAccessProperty:
        def __init__(
            self,
            *,
            ec2_ssh_key: builtins.str,
            source_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param ec2_ssh_key: ``CfnNodegroup.RemoteAccessProperty.Ec2SshKey``.
            :param source_security_groups: ``CfnNodegroup.RemoteAccessProperty.SourceSecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "ec2_ssh_key": ec2_ssh_key,
            }
            if source_security_groups is not None:
                self._values["source_security_groups"] = source_security_groups

        @builtins.property
        def ec2_ssh_key(self) -> builtins.str:
            '''``CfnNodegroup.RemoteAccessProperty.Ec2SshKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html#cfn-eks-nodegroup-remoteaccess-ec2sshkey
            '''
            result = self._values.get("ec2_ssh_key")
            assert result is not None, "Required property 'ec2_ssh_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnNodegroup.RemoteAccessProperty.SourceSecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-remoteaccess.html#cfn-eks-nodegroup-remoteaccess-sourcesecuritygroups
            '''
            result = self._values.get("source_security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RemoteAccessProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnNodegroup.ScalingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "desired_size": "desiredSize",
            "max_size": "maxSize",
            "min_size": "minSize",
        },
    )
    class ScalingConfigProperty:
        def __init__(
            self,
            *,
            desired_size: typing.Optional[jsii.Number] = None,
            max_size: typing.Optional[jsii.Number] = None,
            min_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param desired_size: ``CfnNodegroup.ScalingConfigProperty.DesiredSize``.
            :param max_size: ``CfnNodegroup.ScalingConfigProperty.MaxSize``.
            :param min_size: ``CfnNodegroup.ScalingConfigProperty.MinSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if desired_size is not None:
                self._values["desired_size"] = desired_size
            if max_size is not None:
                self._values["max_size"] = max_size
            if min_size is not None:
                self._values["min_size"] = min_size

        @builtins.property
        def desired_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnNodegroup.ScalingConfigProperty.DesiredSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-desiredsize
            '''
            result = self._values.get("desired_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnNodegroup.ScalingConfigProperty.MaxSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-maxsize
            '''
            result = self._values.get("max_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnNodegroup.ScalingConfigProperty.MinSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-scalingconfig.html#cfn-eks-nodegroup-scalingconfig-minsize
            '''
            result = self._values.get("min_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnNodegroup.TaintProperty",
        jsii_struct_bases=[],
        name_mapping={"effect": "effect", "key": "key", "value": "value"},
    )
    class TaintProperty:
        def __init__(
            self,
            *,
            effect: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param effect: ``CfnNodegroup.TaintProperty.Effect``.
            :param key: ``CfnNodegroup.TaintProperty.Key``.
            :param value: ``CfnNodegroup.TaintProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if effect is not None:
                self._values["effect"] = effect
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def effect(self) -> typing.Optional[builtins.str]:
            '''``CfnNodegroup.TaintProperty.Effect``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html#cfn-eks-nodegroup-taint-effect
            '''
            result = self._values.get("effect")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnNodegroup.TaintProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html#cfn-eks-nodegroup-taint-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnNodegroup.TaintProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-taint.html#cfn-eks-nodegroup-taint-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eks-legacy.CfnNodegroup.UpdateConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_unavailable": "maxUnavailable",
            "max_unavailable_percentage": "maxUnavailablePercentage",
        },
    )
    class UpdateConfigProperty:
        def __init__(
            self,
            *,
            max_unavailable: typing.Optional[jsii.Number] = None,
            max_unavailable_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param max_unavailable: ``CfnNodegroup.UpdateConfigProperty.MaxUnavailable``.
            :param max_unavailable_percentage: ``CfnNodegroup.UpdateConfigProperty.MaxUnavailablePercentage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if max_unavailable is not None:
                self._values["max_unavailable"] = max_unavailable
            if max_unavailable_percentage is not None:
                self._values["max_unavailable_percentage"] = max_unavailable_percentage

        @builtins.property
        def max_unavailable(self) -> typing.Optional[jsii.Number]:
            '''``CfnNodegroup.UpdateConfigProperty.MaxUnavailable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html#cfn-eks-nodegroup-updateconfig-maxunavailable
            '''
            result = self._values.get("max_unavailable")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_unavailable_percentage(self) -> typing.Optional[jsii.Number]:
            '''``CfnNodegroup.UpdateConfigProperty.MaxUnavailablePercentage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eks-nodegroup-updateconfig.html#cfn-eks-nodegroup-updateconfig-maxunavailablepercentage
            '''
            result = self._values.get("max_unavailable_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.CfnNodegroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "node_role": "nodeRole",
        "subnets": "subnets",
        "ami_type": "amiType",
        "capacity_type": "capacityType",
        "disk_size": "diskSize",
        "force_update_enabled": "forceUpdateEnabled",
        "instance_types": "instanceTypes",
        "labels": "labels",
        "launch_template": "launchTemplate",
        "nodegroup_name": "nodegroupName",
        "release_version": "releaseVersion",
        "remote_access": "remoteAccess",
        "scaling_config": "scalingConfig",
        "tags": "tags",
        "taints": "taints",
        "update_config": "updateConfig",
        "version": "version",
    },
)
class CfnNodegroupProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        node_role: builtins.str,
        subnets: typing.Sequence[builtins.str],
        ami_type: typing.Optional[builtins.str] = None,
        capacity_type: typing.Optional[builtins.str] = None,
        disk_size: typing.Optional[jsii.Number] = None,
        force_update_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        labels: typing.Any = None,
        launch_template: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.LaunchTemplateSpecificationProperty]] = None,
        nodegroup_name: typing.Optional[builtins.str] = None,
        release_version: typing.Optional[builtins.str] = None,
        remote_access: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.RemoteAccessProperty]] = None,
        scaling_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.ScalingConfigProperty]] = None,
        tags: typing.Any = None,
        taints: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.TaintProperty]]]] = None,
        update_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.UpdateConfigProperty]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EKS::Nodegroup``.

        :param cluster_name: ``AWS::EKS::Nodegroup.ClusterName``.
        :param node_role: ``AWS::EKS::Nodegroup.NodeRole``.
        :param subnets: ``AWS::EKS::Nodegroup.Subnets``.
        :param ami_type: ``AWS::EKS::Nodegroup.AmiType``.
        :param capacity_type: ``AWS::EKS::Nodegroup.CapacityType``.
        :param disk_size: ``AWS::EKS::Nodegroup.DiskSize``.
        :param force_update_enabled: ``AWS::EKS::Nodegroup.ForceUpdateEnabled``.
        :param instance_types: ``AWS::EKS::Nodegroup.InstanceTypes``.
        :param labels: ``AWS::EKS::Nodegroup.Labels``.
        :param launch_template: ``AWS::EKS::Nodegroup.LaunchTemplate``.
        :param nodegroup_name: ``AWS::EKS::Nodegroup.NodegroupName``.
        :param release_version: ``AWS::EKS::Nodegroup.ReleaseVersion``.
        :param remote_access: ``AWS::EKS::Nodegroup.RemoteAccess``.
        :param scaling_config: ``AWS::EKS::Nodegroup.ScalingConfig``.
        :param tags: ``AWS::EKS::Nodegroup.Tags``.
        :param taints: ``AWS::EKS::Nodegroup.Taints``.
        :param update_config: ``AWS::EKS::Nodegroup.UpdateConfig``.
        :param version: ``AWS::EKS::Nodegroup.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
            "node_role": node_role,
            "subnets": subnets,
        }
        if ami_type is not None:
            self._values["ami_type"] = ami_type
        if capacity_type is not None:
            self._values["capacity_type"] = capacity_type
        if disk_size is not None:
            self._values["disk_size"] = disk_size
        if force_update_enabled is not None:
            self._values["force_update_enabled"] = force_update_enabled
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if labels is not None:
            self._values["labels"] = labels
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if nodegroup_name is not None:
            self._values["nodegroup_name"] = nodegroup_name
        if release_version is not None:
            self._values["release_version"] = release_version
        if remote_access is not None:
            self._values["remote_access"] = remote_access
        if scaling_config is not None:
            self._values["scaling_config"] = scaling_config
        if tags is not None:
            self._values["tags"] = tags
        if taints is not None:
            self._values["taints"] = taints
        if update_config is not None:
            self._values["update_config"] = update_config
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''``AWS::EKS::Nodegroup.ClusterName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_role(self) -> builtins.str:
        '''``AWS::EKS::Nodegroup.NodeRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-noderole
        '''
        result = self._values.get("node_role")
        assert result is not None, "Required property 'node_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''``AWS::EKS::Nodegroup.Subnets``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-subnets
        '''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ami_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.AmiType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-amitype
        '''
        result = self._values.get("ami_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.CapacityType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-capacitytype
        '''
        result = self._values.get("capacity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size(self) -> typing.Optional[jsii.Number]:
        '''``AWS::EKS::Nodegroup.DiskSize``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-disksize
        '''
        result = self._values.get("disk_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def force_update_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::EKS::Nodegroup.ForceUpdateEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-forceupdateenabled
        '''
        result = self._values.get("force_update_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::EKS::Nodegroup.InstanceTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-instancetypes
        '''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Any:
        '''``AWS::EKS::Nodegroup.Labels``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Any, result)

    @builtins.property
    def launch_template(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.LaunchTemplateSpecificationProperty]]:
        '''``AWS::EKS::Nodegroup.LaunchTemplate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-launchtemplate
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.LaunchTemplateSpecificationProperty]], result)

    @builtins.property
    def nodegroup_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.NodegroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-nodegroupname
        '''
        result = self._values.get("nodegroup_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.ReleaseVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-releaseversion
        '''
        result = self._values.get("release_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_access(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.RemoteAccessProperty]]:
        '''``AWS::EKS::Nodegroup.RemoteAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-remoteaccess
        '''
        result = self._values.get("remote_access")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.RemoteAccessProperty]], result)

    @builtins.property
    def scaling_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.ScalingConfigProperty]]:
        '''``AWS::EKS::Nodegroup.ScalingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-scalingconfig
        '''
        result = self._values.get("scaling_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.ScalingConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::EKS::Nodegroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def taints(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.TaintProperty]]]]:
        '''``AWS::EKS::Nodegroup.Taints``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-taints
        '''
        result = self._values.get("taints")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.TaintProperty]]]], result)

    @builtins.property
    def update_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.UpdateConfigProperty]]:
        '''``AWS::EKS::Nodegroup.UpdateConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-updateconfig
        '''
        result = self._values.get("update_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnNodegroup.UpdateConfigProperty]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''``AWS::EKS::Nodegroup.Version``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html#cfn-eks-nodegroup-version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNodegroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.ClusterAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_arn": "clusterArn",
        "cluster_certificate_authority_data": "clusterCertificateAuthorityData",
        "cluster_endpoint": "clusterEndpoint",
        "cluster_name": "clusterName",
        "security_groups": "securityGroups",
        "vpc": "vpc",
    },
)
class ClusterAttributes:
    def __init__(
        self,
        *,
        cluster_arn: builtins.str,
        cluster_certificate_authority_data: builtins.str,
        cluster_endpoint: builtins.str,
        cluster_name: builtins.str,
        security_groups: typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup],
        vpc: aws_cdk.aws_ec2.IVpc,
    ) -> None:
        '''
        :param cluster_arn: (deprecated) The unique ARN assigned to the service by AWS in the form of arn:aws:eks:.
        :param cluster_certificate_authority_data: (deprecated) The certificate-authority-data for your cluster.
        :param cluster_endpoint: (deprecated) The API Server endpoint URL.
        :param cluster_name: (deprecated) The physical name of the Cluster.
        :param security_groups: (deprecated) The security groups associated with this cluster.
        :param vpc: (deprecated) The VPC in which this Cluster was created.

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_arn": cluster_arn,
            "cluster_certificate_authority_data": cluster_certificate_authority_data,
            "cluster_endpoint": cluster_endpoint,
            "cluster_name": cluster_name,
            "security_groups": security_groups,
            "vpc": vpc,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''(deprecated) The unique ARN assigned to the service by AWS in the form of arn:aws:eks:.

        :stability: deprecated
        '''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_certificate_authority_data(self) -> builtins.str:
        '''(deprecated) The certificate-authority-data for your cluster.

        :stability: deprecated
        '''
        result = self._values.get("cluster_certificate_authority_data")
        assert result is not None, "Required property 'cluster_certificate_authority_data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_endpoint(self) -> builtins.str:
        '''(deprecated) The API Server endpoint URL.

        :stability: deprecated
        '''
        result = self._values.get("cluster_endpoint")
        assert result is not None, "Required property 'cluster_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''(deprecated) The physical name of the Cluster.

        :stability: deprecated
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_groups(self) -> typing.List[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) The security groups associated with this cluster.

        :stability: deprecated
        '''
        result = self._values.get("security_groups")
        assert result is not None, "Required property 'security_groups' is missing"
        return typing.cast(typing.List[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(deprecated) The VPC in which this Cluster was created.

        :stability: deprecated
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.ClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "default_capacity": "defaultCapacity",
        "default_capacity_instance": "defaultCapacityInstance",
        "kubectl_enabled": "kubectlEnabled",
        "masters_role": "mastersRole",
        "output_cluster_name": "outputClusterName",
        "output_config_command": "outputConfigCommand",
        "output_masters_role_arn": "outputMastersRoleArn",
        "role": "role",
        "security_group": "securityGroup",
        "version": "version",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class ClusterProps:
    def __init__(
        self,
        *,
        cluster_name: typing.Optional[builtins.str] = None,
        default_capacity: typing.Optional[jsii.Number] = None,
        default_capacity_instance: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        kubectl_enabled: typing.Optional[builtins.bool] = None,
        masters_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        output_cluster_name: typing.Optional[builtins.bool] = None,
        output_config_command: typing.Optional[builtins.bool] = None,
        output_masters_role_arn: typing.Optional[builtins.bool] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        version: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.SubnetSelection]] = None,
    ) -> None:
        '''(deprecated) Properties to instantiate the Cluster.

        :param cluster_name: (deprecated) Name for the cluster. Default: - Automatically generated name
        :param default_capacity: (deprecated) Number of instances to allocate as an initial capacity for this cluster. Instance type can be configured through ``defaultCapacityInstanceType``, which defaults to ``m5.large``. Use ``cluster.addCapacity`` to add additional customized capacity. Set this to ``0`` is you wish to avoid the initial capacity allocation. Default: 2
        :param default_capacity_instance: (deprecated) The instance type to use for the default capacity. This will only be taken into account if ``defaultCapacity`` is > 0. Default: m5.large
        :param kubectl_enabled: (deprecated) Allows defining ``kubectrl``-related resources on this cluster. If this is disabled, it will not be possible to use the following capabilities: - ``addResource`` - ``addRoleMapping`` - ``addUserMapping`` - ``addMastersRole`` and ``props.mastersRole`` If this is disabled, the cluster can only be managed by issuing ``kubectl`` commands from a session that uses the IAM role/user that created the account. *NOTE*: changing this value will destoy the cluster. This is because a managable cluster must be created using an AWS CloudFormation custom resource which executes with an IAM role owned by the CDK app. Default: true The cluster can be managed by the AWS CDK application.
        :param masters_role: (deprecated) An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group. Default: - By default, it will only possible to update this Kubernetes system by adding resources to this cluster via ``addResource`` or by defining ``KubernetesResource`` resources in your AWS CDK app. Use this if you wish to grant cluster administration privileges to another role.
        :param output_cluster_name: (deprecated) Determines whether a CloudFormation output with the name of the cluster will be synthesized. Default: false
        :param output_config_command: (deprecated) Determines whether a CloudFormation output with the ``aws eks update-kubeconfig`` command will be synthesized. This command will include the cluster name and, if applicable, the ARN of the masters IAM role. Default: true
        :param output_masters_role_arn: (deprecated) Determines whether a CloudFormation output with the ARN of the "masters" IAM role will be synthesized (if ``mastersRole`` is specified). Default: false
        :param role: (deprecated) Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Default: - A role is automatically created for you
        :param security_group: (deprecated) Security Group to use for Control Plane ENIs. Default: - A security group is automatically created
        :param version: (deprecated) The Kubernetes version to run in the cluster. Default: - If not supplied, will use Amazon default version
        :param vpc: (deprecated) The VPC in which to create the Cluster. Default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        :param vpc_subnets: (deprecated) Where to place EKS Control Plane ENIs. If you want to create public load balancers, this must include public subnets. For example, to only select private subnets, supply the following:: vpcSubnets: [ { subnetType: ec2.SubnetType.Private } ] Default: - All public and private subnets

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if default_capacity is not None:
            self._values["default_capacity"] = default_capacity
        if default_capacity_instance is not None:
            self._values["default_capacity_instance"] = default_capacity_instance
        if kubectl_enabled is not None:
            self._values["kubectl_enabled"] = kubectl_enabled
        if masters_role is not None:
            self._values["masters_role"] = masters_role
        if output_cluster_name is not None:
            self._values["output_cluster_name"] = output_cluster_name
        if output_config_command is not None:
            self._values["output_config_command"] = output_config_command
        if output_masters_role_arn is not None:
            self._values["output_masters_role_arn"] = output_masters_role_arn
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group
        if version is not None:
            self._values["version"] = version
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Name for the cluster.

        :default: - Automatically generated name

        :stability: deprecated
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_capacity(self) -> typing.Optional[jsii.Number]:
        '''(deprecated) Number of instances to allocate as an initial capacity for this cluster.

        Instance type can be configured through ``defaultCapacityInstanceType``,
        which defaults to ``m5.large``.

        Use ``cluster.addCapacity`` to add additional customized capacity. Set this
        to ``0`` is you wish to avoid the initial capacity allocation.

        :default: 2

        :stability: deprecated
        '''
        result = self._values.get("default_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def default_capacity_instance(
        self,
    ) -> typing.Optional[aws_cdk.aws_ec2.InstanceType]:
        '''(deprecated) The instance type to use for the default capacity.

        This will only be taken
        into account if ``defaultCapacity`` is > 0.

        :default: m5.large

        :stability: deprecated
        '''
        result = self._values.get("default_capacity_instance")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.InstanceType], result)

    @builtins.property
    def kubectl_enabled(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Allows defining ``kubectrl``-related resources on this cluster.

        If this is disabled, it will not be possible to use the following
        capabilities:

        - ``addResource``
        - ``addRoleMapping``
        - ``addUserMapping``
        - ``addMastersRole`` and ``props.mastersRole``

        If this is disabled, the cluster can only be managed by issuing ``kubectl``
        commands from a session that uses the IAM role/user that created the
        account.

        *NOTE*: changing this value will destoy the cluster. This is because a
        managable cluster must be created using an AWS CloudFormation custom
        resource which executes with an IAM role owned by the CDK app.

        :default: true The cluster can be managed by the AWS CDK application.

        :stability: deprecated
        '''
        result = self._values.get("kubectl_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def masters_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(deprecated) An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group.

        :default:

        - By default, it will only possible to update this Kubernetes
        system by adding resources to this cluster via ``addResource`` or
        by defining ``KubernetesResource`` resources in your AWS CDK app.
        Use this if you wish to grant cluster administration privileges
        to another role.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings
        :stability: deprecated
        '''
        result = self._values.get("masters_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def output_cluster_name(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Determines whether a CloudFormation output with the name of the cluster will be synthesized.

        :default: false

        :stability: deprecated
        '''
        result = self._values.get("output_cluster_name")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def output_config_command(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Determines whether a CloudFormation output with the ``aws eks update-kubeconfig`` command will be synthesized.

        This command will include
        the cluster name and, if applicable, the ARN of the masters IAM role.

        :default: true

        :stability: deprecated
        '''
        result = self._values.get("output_config_command")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def output_masters_role_arn(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Determines whether a CloudFormation output with the ARN of the "masters" IAM role will be synthesized (if ``mastersRole`` is specified).

        :default: false

        :stability: deprecated
        '''
        result = self._values.get("output_masters_role_arn")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(deprecated) Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.

        :default: - A role is automatically created for you

        :stability: deprecated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) Security Group to use for Control Plane ENIs.

        :default: - A security group is automatically created

        :stability: deprecated
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The Kubernetes version to run in the cluster.

        :default: - If not supplied, will use Amazon default version

        :stability: deprecated
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(deprecated) The VPC in which to create the Cluster.

        :default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.

        :stability: deprecated
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def vpc_subnets(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.SubnetSelection]]:
        '''(deprecated) Where to place EKS Control Plane ENIs.

        If you want to create public load balancers, this must include public subnets.

        For example, to only select private subnets, supply the following::

           # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
           vpcSubnets: [
              { subnetType: ec2.SubnetType.Private }
           ]

        :default: - All public and private subnets

        :stability: deprecated
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.SubnetSelection]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_ec2.IMachineImage)
class EksOptimizedImage(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.EksOptimizedImage",
):
    '''(deprecated) Construct an Amazon Linux 2 image from the latest EKS Optimized AMI published in SSM.

    :stability: deprecated
    '''

    def __init__(
        self,
        *,
        kubernetes_version: typing.Optional[builtins.str] = None,
        node_type: typing.Optional["NodeType"] = None,
    ) -> None:
        '''(deprecated) Constructs a new instance of the EcsOptimizedAmi class.

        :param kubernetes_version: (deprecated) The Kubernetes version to use. Default: - The latest version
        :param node_type: (deprecated) What instance type to retrieve the image for (standard or GPU-optimized). Default: NodeType.STANDARD

        :stability: deprecated
        '''
        props = EksOptimizedImageProps(
            kubernetes_version=kubernetes_version, node_type=node_type
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="getImage")
    def get_image(
        self,
        scope: aws_cdk.core.Construct,
    ) -> aws_cdk.aws_ec2.MachineImageConfig:
        '''(deprecated) Return the correct image.

        :param scope: -

        :stability: deprecated
        '''
        return typing.cast(aws_cdk.aws_ec2.MachineImageConfig, jsii.invoke(self, "getImage", [scope]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.EksOptimizedImageProps",
    jsii_struct_bases=[],
    name_mapping={"kubernetes_version": "kubernetesVersion", "node_type": "nodeType"},
)
class EksOptimizedImageProps:
    def __init__(
        self,
        *,
        kubernetes_version: typing.Optional[builtins.str] = None,
        node_type: typing.Optional["NodeType"] = None,
    ) -> None:
        '''(deprecated) Properties for EksOptimizedImage.

        :param kubernetes_version: (deprecated) The Kubernetes version to use. Default: - The latest version
        :param node_type: (deprecated) What instance type to retrieve the image for (standard or GPU-optimized). Default: NodeType.STANDARD

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if kubernetes_version is not None:
            self._values["kubernetes_version"] = kubernetes_version
        if node_type is not None:
            self._values["node_type"] = node_type

    @builtins.property
    def kubernetes_version(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The Kubernetes version to use.

        :default: - The latest version

        :stability: deprecated
        '''
        result = self._values.get("kubernetes_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_type(self) -> typing.Optional["NodeType"]:
        '''(deprecated) What instance type to retrieve the image for (standard or GPU-optimized).

        :default: NodeType.STANDARD

        :stability: deprecated
        '''
        result = self._values.get("node_type")
        return typing.cast(typing.Optional["NodeType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EksOptimizedImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HelmChart(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.HelmChart",
):
    '''(deprecated) Represents a helm chart within the Kubernetes system.

    Applies/deletes the resources using ``kubectl`` in sync with the resource.

    :stability: deprecated
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster: "Cluster",
        chart: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: (deprecated) The EKS cluster to apply this configuration to. [disable-awslint:ref-via-interface]
        :param chart: (deprecated) The name of the chart.
        :param namespace: (deprecated) The Kubernetes namespace scope of the requests. Default: default
        :param release: (deprecated) The name of the release. Default: - If no release name is given, it will use the last 63 characters of the node's unique id.
        :param repository: (deprecated) The repository which contains the chart. For example: https://kubernetes-charts.storage.googleapis.com/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param values: (deprecated) The values to be used by the chart. Default: - No values are provided to the chart.
        :param version: (deprecated) The chart version to install. Default: - If this is not specified, the latest version is installed

        :stability: deprecated
        '''
        props = HelmChartProps(
            cluster=cluster,
            chart=chart,
            namespace=namespace,
            release=release,
            repository=repository,
            values=values,
            version=version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="RESOURCE_TYPE")
    def RESOURCE_TYPE(cls) -> builtins.str:
        '''(deprecated) The CloudFormation reosurce type.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RESOURCE_TYPE"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.HelmChartOptions",
    jsii_struct_bases=[],
    name_mapping={
        "chart": "chart",
        "namespace": "namespace",
        "release": "release",
        "repository": "repository",
        "values": "values",
        "version": "version",
    },
)
class HelmChartOptions:
    def __init__(
        self,
        *,
        chart: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Helm Chart options.

        :param chart: (deprecated) The name of the chart.
        :param namespace: (deprecated) The Kubernetes namespace scope of the requests. Default: default
        :param release: (deprecated) The name of the release. Default: - If no release name is given, it will use the last 63 characters of the node's unique id.
        :param repository: (deprecated) The repository which contains the chart. For example: https://kubernetes-charts.storage.googleapis.com/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param values: (deprecated) The values to be used by the chart. Default: - No values are provided to the chart.
        :param version: (deprecated) The chart version to install. Default: - If this is not specified, the latest version is installed

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "chart": chart,
        }
        if namespace is not None:
            self._values["namespace"] = namespace
        if release is not None:
            self._values["release"] = release
        if repository is not None:
            self._values["repository"] = repository
        if values is not None:
            self._values["values"] = values
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def chart(self) -> builtins.str:
        '''(deprecated) The name of the chart.

        :stability: deprecated
        '''
        result = self._values.get("chart")
        assert result is not None, "Required property 'chart' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The Kubernetes namespace scope of the requests.

        :default: default

        :stability: deprecated
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The name of the release.

        :default: - If no release name is given, it will use the last 63 characters of the node's unique id.

        :stability: deprecated
        '''
        result = self._values.get("release")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The repository which contains the chart.

        For example: https://kubernetes-charts.storage.googleapis.com/

        :default: - No repository will be used, which means that the chart needs to be an absolute URL.

        :stability: deprecated
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(deprecated) The values to be used by the chart.

        :default: - No values are provided to the chart.

        :stability: deprecated
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The chart version to install.

        :default: - If this is not specified, the latest version is installed

        :stability: deprecated
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmChartOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.HelmChartProps",
    jsii_struct_bases=[HelmChartOptions],
    name_mapping={
        "chart": "chart",
        "namespace": "namespace",
        "release": "release",
        "repository": "repository",
        "values": "values",
        "version": "version",
        "cluster": "cluster",
    },
)
class HelmChartProps(HelmChartOptions):
    def __init__(
        self,
        *,
        chart: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
        cluster: "Cluster",
    ) -> None:
        '''(deprecated) Helm Chart properties.

        :param chart: (deprecated) The name of the chart.
        :param namespace: (deprecated) The Kubernetes namespace scope of the requests. Default: default
        :param release: (deprecated) The name of the release. Default: - If no release name is given, it will use the last 63 characters of the node's unique id.
        :param repository: (deprecated) The repository which contains the chart. For example: https://kubernetes-charts.storage.googleapis.com/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param values: (deprecated) The values to be used by the chart. Default: - No values are provided to the chart.
        :param version: (deprecated) The chart version to install. Default: - If this is not specified, the latest version is installed
        :param cluster: (deprecated) The EKS cluster to apply this configuration to. [disable-awslint:ref-via-interface]

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "chart": chart,
            "cluster": cluster,
        }
        if namespace is not None:
            self._values["namespace"] = namespace
        if release is not None:
            self._values["release"] = release
        if repository is not None:
            self._values["repository"] = repository
        if values is not None:
            self._values["values"] = values
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def chart(self) -> builtins.str:
        '''(deprecated) The name of the chart.

        :stability: deprecated
        '''
        result = self._values.get("chart")
        assert result is not None, "Required property 'chart' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The Kubernetes namespace scope of the requests.

        :default: default

        :stability: deprecated
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def release(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The name of the release.

        :default: - If no release name is given, it will use the last 63 characters of the node's unique id.

        :stability: deprecated
        '''
        result = self._values.get("release")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The repository which contains the chart.

        For example: https://kubernetes-charts.storage.googleapis.com/

        :default: - No repository will be used, which means that the chart needs to be an absolute URL.

        :stability: deprecated
        '''
        result = self._values.get("repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(deprecated) The values to be used by the chart.

        :default: - No values are provided to the chart.

        :stability: deprecated
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The chart version to install.

        :default: - If this is not specified, the latest version is installed

        :stability: deprecated
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cluster(self) -> "Cluster":
        '''(deprecated) The EKS cluster to apply this configuration to.

        [disable-awslint:ref-via-interface]

        :stability: deprecated
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("Cluster", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HelmChartProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-eks-legacy.ICluster")
class ICluster(
    aws_cdk.core.IResource,
    aws_cdk.aws_ec2.IConnectable,
    typing_extensions.Protocol,
):
    '''(deprecated) An EKS cluster.

    :stability: deprecated
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''(deprecated) The unique ARN assigned to the service by AWS in the form of arn:aws:eks:.

        :stability: deprecated
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterCertificateAuthorityData")
    def cluster_certificate_authority_data(self) -> builtins.str:
        '''(deprecated) The certificate-authority-data for your cluster.

        :stability: deprecated
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        '''(deprecated) The API Server endpoint URL.

        :stability: deprecated
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''(deprecated) The physical name of the Cluster.

        :stability: deprecated
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(deprecated) The VPC in which this Cluster was created.

        :stability: deprecated
        '''
        ...


class _IClusterProxy(
    jsii.proxy_for(aws_cdk.core.IResource), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_ec2.IConnectable), # type: ignore[misc]
):
    '''(deprecated) An EKS cluster.

    :stability: deprecated
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-eks-legacy.ICluster"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''(deprecated) The unique ARN assigned to the service by AWS in the form of arn:aws:eks:.

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterCertificateAuthorityData")
    def cluster_certificate_authority_data(self) -> builtins.str:
        '''(deprecated) The certificate-authority-data for your cluster.

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterCertificateAuthorityData"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        '''(deprecated) The API Server endpoint URL.

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterEndpoint"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''(deprecated) The physical name of the Cluster.

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(deprecated) The VPC in which this Cluster was created.

        :stability: deprecated
        '''
        return typing.cast(aws_cdk.aws_ec2.IVpc, jsii.get(self, "vpc"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICluster).__jsii_proxy_class__ = lambda : _IClusterProxy


class KubernetesResource(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.KubernetesResource",
):
    '''(deprecated) Represents a resource within the Kubernetes system.

    Alternatively, you can use ``cluster.addResource(resource[, resource, ...])``
    to define resources on this cluster.

    Applies/deletes the resources using ``kubectl`` in sync with the resource.

    :stability: deprecated
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster: "Cluster",
        manifest: typing.Sequence[typing.Any],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: (deprecated) The EKS cluster to apply this configuration to. [disable-awslint:ref-via-interface]
        :param manifest: (deprecated) The resource manifest. Consists of any number of child resources. When the resource is created/updated, this manifest will be applied to the cluster through ``kubectl apply`` and when the resource or the stack is deleted, the manifest will be deleted through ``kubectl delete``.

        :stability: deprecated
        '''
        props = KubernetesResourceProps(cluster=cluster, manifest=manifest)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="RESOURCE_TYPE")
    def RESOURCE_TYPE(cls) -> builtins.str:
        '''(deprecated) The CloudFormation reosurce type.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RESOURCE_TYPE"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.KubernetesResourceProps",
    jsii_struct_bases=[],
    name_mapping={"cluster": "cluster", "manifest": "manifest"},
)
class KubernetesResourceProps:
    def __init__(
        self,
        *,
        cluster: "Cluster",
        manifest: typing.Sequence[typing.Any],
    ) -> None:
        '''
        :param cluster: (deprecated) The EKS cluster to apply this configuration to. [disable-awslint:ref-via-interface]
        :param manifest: (deprecated) The resource manifest. Consists of any number of child resources. When the resource is created/updated, this manifest will be applied to the cluster through ``kubectl apply`` and when the resource or the stack is deleted, the manifest will be deleted through ``kubectl delete``.

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cluster": cluster,
            "manifest": manifest,
        }

    @builtins.property
    def cluster(self) -> "Cluster":
        '''(deprecated) The EKS cluster to apply this configuration to.

        [disable-awslint:ref-via-interface]

        :stability: deprecated
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("Cluster", result)

    @builtins.property
    def manifest(self) -> typing.List[typing.Any]:
        '''(deprecated) The resource manifest.

        Consists of any number of child resources.

        When the resource is created/updated, this manifest will be applied to the
        cluster through ``kubectl apply`` and when the resource or the stack is
        deleted, the manifest will be deleted through ``kubectl delete``.

        :stability: deprecated

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            apiVersion: 'v1',
                  kind"Pod" , metadataname: 'mypod'spec: {
                    containers: [ { name: 'hello', image: 'paulbouwer/hello-kubernetes:1.5', ports: [ { containerPort: 8080 } ] } ]
                  }
        '''
        result = self._values.get("manifest")
        assert result is not None, "Required property 'manifest' is missing"
        return typing.cast(typing.List[typing.Any], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eks-legacy.Mapping",
    jsii_struct_bases=[],
    name_mapping={"groups": "groups", "username": "username"},
)
class Mapping:
    def __init__(
        self,
        *,
        groups: typing.Sequence[builtins.str],
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param groups: (deprecated) A list of groups within Kubernetes to which the role is mapped.
        :param username: (deprecated) The user name within Kubernetes to map to the IAM role. Default: - By default, the user name is the ARN of the IAM role.

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "groups": groups,
        }
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def groups(self) -> typing.List[builtins.str]:
        '''(deprecated) A list of groups within Kubernetes to which the role is mapped.

        :see: https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings
        :stability: deprecated
        '''
        result = self._values.get("groups")
        assert result is not None, "Required property 'groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The user name within Kubernetes to map to the IAM role.

        :default: - By default, the user name is the ARN of the IAM role.

        :stability: deprecated
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Mapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-eks-legacy.NodeType")
class NodeType(enum.Enum):
    '''(deprecated) Whether the worker nodes should support GPU or just standard instances.

    :stability: deprecated
    '''

    STANDARD = "STANDARD"
    '''(deprecated) Standard instances.

    :stability: deprecated
    '''
    GPU = "GPU"
    '''(deprecated) GPU instances.

    :stability: deprecated
    '''


@jsii.implements(ICluster)
class Cluster(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eks-legacy.Cluster",
):
    '''(deprecated) A Cluster represents a managed Kubernetes Service (EKS).

    This is a fully managed cluster of API Servers (control-plane)
    The user is still required to create the worker nodes.

    :stability: deprecated
    :resource: AWS::EKS::Cluster
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster_name: typing.Optional[builtins.str] = None,
        default_capacity: typing.Optional[jsii.Number] = None,
        default_capacity_instance: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        kubectl_enabled: typing.Optional[builtins.bool] = None,
        masters_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        output_cluster_name: typing.Optional[builtins.bool] = None,
        output_config_command: typing.Optional[builtins.bool] = None,
        output_masters_role_arn: typing.Optional[builtins.bool] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        version: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.SubnetSelection]] = None,
    ) -> None:
        '''(deprecated) Initiates an EKS Cluster with the supplied arguments.

        :param scope: a Construct, most likely a cdk.Stack created.
        :param id: -
        :param cluster_name: (deprecated) Name for the cluster. Default: - Automatically generated name
        :param default_capacity: (deprecated) Number of instances to allocate as an initial capacity for this cluster. Instance type can be configured through ``defaultCapacityInstanceType``, which defaults to ``m5.large``. Use ``cluster.addCapacity`` to add additional customized capacity. Set this to ``0`` is you wish to avoid the initial capacity allocation. Default: 2
        :param default_capacity_instance: (deprecated) The instance type to use for the default capacity. This will only be taken into account if ``defaultCapacity`` is > 0. Default: m5.large
        :param kubectl_enabled: (deprecated) Allows defining ``kubectrl``-related resources on this cluster. If this is disabled, it will not be possible to use the following capabilities: - ``addResource`` - ``addRoleMapping`` - ``addUserMapping`` - ``addMastersRole`` and ``props.mastersRole`` If this is disabled, the cluster can only be managed by issuing ``kubectl`` commands from a session that uses the IAM role/user that created the account. *NOTE*: changing this value will destoy the cluster. This is because a managable cluster must be created using an AWS CloudFormation custom resource which executes with an IAM role owned by the CDK app. Default: true The cluster can be managed by the AWS CDK application.
        :param masters_role: (deprecated) An IAM role that will be added to the ``system:masters`` Kubernetes RBAC group. Default: - By default, it will only possible to update this Kubernetes system by adding resources to this cluster via ``addResource`` or by defining ``KubernetesResource`` resources in your AWS CDK app. Use this if you wish to grant cluster administration privileges to another role.
        :param output_cluster_name: (deprecated) Determines whether a CloudFormation output with the name of the cluster will be synthesized. Default: false
        :param output_config_command: (deprecated) Determines whether a CloudFormation output with the ``aws eks update-kubeconfig`` command will be synthesized. This command will include the cluster name and, if applicable, the ARN of the masters IAM role. Default: true
        :param output_masters_role_arn: (deprecated) Determines whether a CloudFormation output with the ARN of the "masters" IAM role will be synthesized (if ``mastersRole`` is specified). Default: false
        :param role: (deprecated) Role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Default: - A role is automatically created for you
        :param security_group: (deprecated) Security Group to use for Control Plane ENIs. Default: - A security group is automatically created
        :param version: (deprecated) The Kubernetes version to run in the cluster. Default: - If not supplied, will use Amazon default version
        :param vpc: (deprecated) The VPC in which to create the Cluster. Default: - a VPC with default configuration will be created and can be accessed through ``cluster.vpc``.
        :param vpc_subnets: (deprecated) Where to place EKS Control Plane ENIs. If you want to create public load balancers, this must include public subnets. For example, to only select private subnets, supply the following:: vpcSubnets: [ { subnetType: ec2.SubnetType.Private } ] Default: - All public and private subnets

        :stability: deprecated
        '''
        props = ClusterProps(
            cluster_name=cluster_name,
            default_capacity=default_capacity,
            default_capacity_instance=default_capacity_instance,
            kubectl_enabled=kubectl_enabled,
            masters_role=masters_role,
            output_cluster_name=output_cluster_name,
            output_config_command=output_config_command,
            output_masters_role_arn=output_masters_role_arn,
            role=role,
            security_group=security_group,
            version=version,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromClusterAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_cluster_attributes(
        cls,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster_arn: builtins.str,
        cluster_certificate_authority_data: builtins.str,
        cluster_endpoint: builtins.str,
        cluster_name: builtins.str,
        security_groups: typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup],
        vpc: aws_cdk.aws_ec2.IVpc,
    ) -> ICluster:
        '''(deprecated) Import an existing cluster.

        :param scope: the construct scope, in most cases 'this'.
        :param id: the id or name to import as.
        :param cluster_arn: (deprecated) The unique ARN assigned to the service by AWS in the form of arn:aws:eks:.
        :param cluster_certificate_authority_data: (deprecated) The certificate-authority-data for your cluster.
        :param cluster_endpoint: (deprecated) The API Server endpoint URL.
        :param cluster_name: (deprecated) The physical name of the Cluster.
        :param security_groups: (deprecated) The security groups associated with this cluster.
        :param vpc: (deprecated) The VPC in which this Cluster was created.

        :stability: deprecated
        '''
        attrs = ClusterAttributes(
            cluster_arn=cluster_arn,
            cluster_certificate_authority_data=cluster_certificate_authority_data,
            cluster_endpoint=cluster_endpoint,
            cluster_name=cluster_name,
            security_groups=security_groups,
            vpc=vpc,
        )

        return typing.cast(ICluster, jsii.sinvoke(cls, "fromClusterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addAutoScalingGroup")
    def add_auto_scaling_group(
        self,
        auto_scaling_group: aws_cdk.aws_autoscaling.AutoScalingGroup,
        *,
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[BootstrapOptions] = None,
        map_role: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(deprecated) Add compute capacity to this EKS cluster in the form of an AutoScalingGroup.

        The AutoScalingGroup must be running an EKS-optimized AMI containing the
        /etc/eks/bootstrap.sh script. This method will configure Security Groups,
        add the right policies to the instance role, apply the right tags, and add
        the required user data to the instance's launch configuration.

        Spot instances will be labeled ``lifecycle=Ec2Spot`` and tainted with ``PreferNoSchedule``.
        If kubectl is enabled, the
        `spot interrupt handler <https://github.com/awslabs/ec2-spot-labs/tree/master/ec2-spot-eks-solution/spot-termination-handler>`_
        daemon will be installed on all spot instances to handle
        `EC2 Spot Instance Termination Notices <https://aws.amazon.com/blogs/aws/new-ec2-spot-instance-termination-notices/>`_.

        Prefer to use ``addCapacity`` if possible.

        :param auto_scaling_group: [disable-awslint:ref-via-interface].
        :param bootstrap_enabled: (deprecated) Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: (deprecated) Allows options for node bootstrapping through EC2 user data.
        :param map_role: (deprecated) Will automatically update the aws-auth ConfigMap to map the IAM instance role to RBAC. This cannot be explicitly set to ``true`` if the cluster has kubectl disabled. Default: - true if the cluster has kubectl enabled (which is the default).

        :see: https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html
        :stability: deprecated
        '''
        options = AutoScalingGroupOptions(
            bootstrap_enabled=bootstrap_enabled,
            bootstrap_options=bootstrap_options,
            map_role=map_role,
        )

        return typing.cast(None, jsii.invoke(self, "addAutoScalingGroup", [auto_scaling_group, options]))

    @jsii.member(jsii_name="addCapacity")
    def add_capacity(
        self,
        id: builtins.str,
        *,
        instance_type: aws_cdk.aws_ec2.InstanceType,
        bootstrap_enabled: typing.Optional[builtins.bool] = None,
        bootstrap_options: typing.Optional[BootstrapOptions] = None,
        map_role: typing.Optional[builtins.bool] = None,
        allow_all_outbound: typing.Optional[builtins.bool] = None,
        associate_public_ip_address: typing.Optional[builtins.bool] = None,
        auto_scaling_group_name: typing.Optional[builtins.str] = None,
        block_devices: typing.Optional[typing.Sequence[aws_cdk.aws_autoscaling.BlockDevice]] = None,
        cooldown: typing.Optional[aws_cdk.core.Duration] = None,
        desired_capacity: typing.Optional[jsii.Number] = None,
        group_metrics: typing.Optional[typing.Sequence[aws_cdk.aws_autoscaling.GroupMetrics]] = None,
        health_check: typing.Optional[aws_cdk.aws_autoscaling.HealthCheck] = None,
        ignore_unmodified_size_properties: typing.Optional[builtins.bool] = None,
        instance_monitoring: typing.Optional[aws_cdk.aws_autoscaling.Monitoring] = None,
        key_name: typing.Optional[builtins.str] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        max_instance_lifetime: typing.Optional[aws_cdk.core.Duration] = None,
        min_capacity: typing.Optional[jsii.Number] = None,
        new_instances_protected_from_scale_in: typing.Optional[builtins.bool] = None,
        notifications: typing.Optional[typing.Sequence[aws_cdk.aws_autoscaling.NotificationConfiguration]] = None,
        notifications_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
        replacing_update_min_successful_instances_percent: typing.Optional[jsii.Number] = None,
        resource_signal_count: typing.Optional[jsii.Number] = None,
        resource_signal_timeout: typing.Optional[aws_cdk.core.Duration] = None,
        rolling_update_configuration: typing.Optional[aws_cdk.aws_autoscaling.RollingUpdateConfiguration] = None,
        signals: typing.Optional[aws_cdk.aws_autoscaling.Signals] = None,
        spot_price: typing.Optional[builtins.str] = None,
        update_policy: typing.Optional[aws_cdk.aws_autoscaling.UpdatePolicy] = None,
        update_type: typing.Optional[aws_cdk.aws_autoscaling.UpdateType] = None,
        vpc_subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection] = None,
    ) -> aws_cdk.aws_autoscaling.AutoScalingGroup:
        '''(deprecated) Add nodes to this EKS cluster.

        The nodes will automatically be configured with the right VPC and AMI
        for the instance type and Kubernetes version.

        Spot instances will be labeled ``lifecycle=Ec2Spot`` and tainted with ``PreferNoSchedule``.
        If kubectl is enabled, the
        `spot interrupt handler <https://github.com/awslabs/ec2-spot-labs/tree/master/ec2-spot-eks-solution/spot-termination-handler>`_
        daemon will be installed on all spot instances to handle
        `EC2 Spot Instance Termination Notices <https://aws.amazon.com/blogs/aws/new-ec2-spot-instance-termination-notices/>`_.

        :param id: -
        :param instance_type: (deprecated) Instance type of the instances to start.
        :param bootstrap_enabled: (deprecated) Configures the EC2 user-data script for instances in this autoscaling group to bootstrap the node (invoke ``/etc/eks/bootstrap.sh``) and associate it with the EKS cluster. If you wish to provide a custom user data script, set this to ``false`` and manually invoke ``autoscalingGroup.addUserData()``. Default: true
        :param bootstrap_options: (deprecated) EKS node bootstrapping options. Default: - none
        :param map_role: (deprecated) Will automatically update the aws-auth ConfigMap to map the IAM instance role to RBAC. This cannot be explicitly set to ``true`` if the cluster has kubectl disabled. Default: - true if the cluster has kubectl enabled (which is the default).
        :param allow_all_outbound: Whether the instances can initiate connections to anywhere by default. Default: true
        :param associate_public_ip_address: Whether instances in the Auto Scaling Group should have public IP addresses associated with them. Default: - Use subnet setting.
        :param auto_scaling_group_name: The name of the Auto Scaling group. This name must be unique per Region per account. Default: - Auto generated by CloudFormation
        :param block_devices: Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes. Each instance that is launched has an associated root device volume, either an Amazon EBS volume or an instance store volume. You can use block device mappings to specify additional EBS volumes or instance store volumes to attach to an instance when it is launched. Default: - Uses the block device mapping of the AMI
        :param cooldown: Default scaling cooldown for this AutoScalingGroup. Default: Duration.minutes(5)
        :param desired_capacity: Initial amount of instances in the fleet. If this is set to a number, every deployment will reset the amount of instances to this number. It is recommended to leave this value blank. Default: minCapacity, and leave unchanged during deployment
        :param group_metrics: Enable monitoring for group metrics, these metrics describe the group rather than any of its instances. To report all group metrics use ``GroupMetrics.all()`` Group metrics are reported in a granularity of 1 minute at no additional charge. Default: - no group metrics will be reported
        :param health_check: Configuration for health checks. Default: - HealthCheck.ec2 with no grace period
        :param ignore_unmodified_size_properties: If the ASG has scheduled actions, don't reset unchanged group sizes. Only used if the ASG has scheduled actions (which may scale your ASG up or down regardless of cdk deployments). If true, the size of the group will only be reset if it has been changed in the CDK app. If false, the sizes will always be changed back to what they were in the CDK app on deployment. Default: true
        :param instance_monitoring: Controls whether instances in this group are launched with detailed or basic monitoring. When detailed monitoring is enabled, Amazon CloudWatch generates metrics every minute and your account is charged a fee. When you disable detailed monitoring, CloudWatch generates metrics every 5 minutes. Default: - Monitoring.DETAILED
        :param key_name: Name of SSH keypair to grant access to instances. Default: - No SSH access will be possible.
        :param max_capacity: Maximum number of instances in the fleet. Default: desiredCapacity
        :param max_instance_lifetime: The maximum amount of time that an instance can be in service. The maximum duration applies to all current and future instances in the group. As an instance approaches its maximum duration, it is terminated and replaced, and cannot be used again. You must specify a value of at least 604,800 seconds (7 days). To clear a previously set value, leave this property undefined. Default: none
        :param min_capacity: Minimum number of instances in the fleet. Default: 1
        :param new_instances_protected_from_scale_in: Whether newly-launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. By default, Auto Scaling can terminate an instance at any time after launch when scaling in an Auto Scaling Group, subject to the group's termination policy. However, you may wish to protect newly-launched instances from being scaled in if they are going to run critical applications that should not be prematurely terminated. This flag must be enabled if the Auto Scaling Group will be associated with an ECS Capacity Provider with managed termination protection. Default: false
        :param notifications: Configure autoscaling group to send notifications about fleet changes to an SNS topic(s). Default: - No fleet change notifications will be sent.
        :param notifications_topic: (deprecated) SNS topic to send notifications about fleet changes. Default: - No fleet change notifications will be sent.
        :param replacing_update_min_successful_instances_percent: (deprecated) Configuration for replacing updates. Only used if updateType == UpdateType.ReplacingUpdate. Specifies how many instances must signal success for the update to succeed. Default: minSuccessfulInstancesPercent
        :param resource_signal_count: (deprecated) How many ResourceSignal calls CloudFormation expects before the resource is considered created. Default: 1 if resourceSignalTimeout is set, 0 otherwise
        :param resource_signal_timeout: (deprecated) The length of time to wait for the resourceSignalCount. The maximum value is 43200 (12 hours). Default: Duration.minutes(5) if resourceSignalCount is set, N/A otherwise
        :param rolling_update_configuration: (deprecated) Configuration for rolling updates. Only used if updateType == UpdateType.RollingUpdate. Default: - RollingUpdateConfiguration with defaults.
        :param signals: Configure waiting for signals during deployment. Use this to pause the CloudFormation deployment to wait for the instances in the AutoScalingGroup to report successful startup during creation and updates. The UserData script needs to invoke ``cfn-signal`` with a success or failure code after it is done setting up the instance. Without waiting for signals, the CloudFormation deployment will proceed as soon as the AutoScalingGroup has been created or updated but before the instances in the group have been started. For example, to have instances wait for an Elastic Load Balancing health check before they signal success, add a health-check verification by using the cfn-init helper script. For an example, see the verify_instance_health command in the Auto Scaling rolling updates sample template: https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/AutoScaling/AutoScalingRollingUpdates.yaml Default: - Do not wait for signals
        :param spot_price: The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. Default: none
        :param update_policy: What to do when an AutoScalingGroup's instance configuration is changed. This is applied when any of the settings on the ASG are changed that affect how the instances should be created (VPC, instance type, startup scripts, etc.). It indicates how the existing instances should be replaced with new instances matching the new config. By default, nothing is done and only new instances are launched with the new config. Default: - ``UpdatePolicy.rollingUpdate()`` if using ``init``, ``UpdatePolicy.none()`` otherwise
        :param update_type: (deprecated) What to do when an AutoScalingGroup's instance configuration is changed. This is applied when any of the settings on the ASG are changed that affect how the instances should be created (VPC, instance type, startup scripts, etc.). It indicates how the existing instances should be replaced with new instances matching the new config. By default, nothing is done and only new instances are launched with the new config. Default: UpdateType.None
        :param vpc_subnets: Where to place instances within the VPC. Default: - All Private subnets.

        :stability: deprecated
        '''
        options = CapacityOptions(
            instance_type=instance_type,
            bootstrap_enabled=bootstrap_enabled,
            bootstrap_options=bootstrap_options,
            map_role=map_role,
            allow_all_outbound=allow_all_outbound,
            associate_public_ip_address=associate_public_ip_address,
            auto_scaling_group_name=auto_scaling_group_name,
            block_devices=block_devices,
            cooldown=cooldown,
            desired_capacity=desired_capacity,
            group_metrics=group_metrics,
            health_check=health_check,
            ignore_unmodified_size_properties=ignore_unmodified_size_properties,
            instance_monitoring=instance_monitoring,
            key_name=key_name,
            max_capacity=max_capacity,
            max_instance_lifetime=max_instance_lifetime,
            min_capacity=min_capacity,
            new_instances_protected_from_scale_in=new_instances_protected_from_scale_in,
            notifications=notifications,
            notifications_topic=notifications_topic,
            replacing_update_min_successful_instances_percent=replacing_update_min_successful_instances_percent,
            resource_signal_count=resource_signal_count,
            resource_signal_timeout=resource_signal_timeout,
            rolling_update_configuration=rolling_update_configuration,
            signals=signals,
            spot_price=spot_price,
            update_policy=update_policy,
            update_type=update_type,
            vpc_subnets=vpc_subnets,
        )

        return typing.cast(aws_cdk.aws_autoscaling.AutoScalingGroup, jsii.invoke(self, "addCapacity", [id, options]))

    @jsii.member(jsii_name="addChart")
    def add_chart(
        self,
        id: builtins.str,
        *,
        chart: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
        release: typing.Optional[builtins.str] = None,
        repository: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> HelmChart:
        '''(deprecated) Defines a Helm chart in this cluster.

        :param id: logical id of this chart.
        :param chart: (deprecated) The name of the chart.
        :param namespace: (deprecated) The Kubernetes namespace scope of the requests. Default: default
        :param release: (deprecated) The name of the release. Default: - If no release name is given, it will use the last 63 characters of the node's unique id.
        :param repository: (deprecated) The repository which contains the chart. For example: https://kubernetes-charts.storage.googleapis.com/ Default: - No repository will be used, which means that the chart needs to be an absolute URL.
        :param values: (deprecated) The values to be used by the chart. Default: - No values are provided to the chart.
        :param version: (deprecated) The chart version to install. Default: - If this is not specified, the latest version is installed

        :return: a ``HelmChart`` object

        :stability: deprecated
        :throws: If ``kubectlEnabled`` is ``false``
        '''
        options = HelmChartOptions(
            chart=chart,
            namespace=namespace,
            release=release,
            repository=repository,
            values=values,
            version=version,
        )

        return typing.cast(HelmChart, jsii.invoke(self, "addChart", [id, options]))

    @jsii.member(jsii_name="addResource")
    def add_resource(
        self,
        id: builtins.str,
        *manifest: typing.Any,
    ) -> KubernetesResource:
        '''(deprecated) Defines a Kubernetes resource in this cluster.

        The manifest will be applied/deleted using kubectl as needed.

        :param id: logical id of this manifest.
        :param manifest: a list of Kubernetes resource specifications.

        :return: a ``KubernetesResource`` object.

        :stability: deprecated
        :throws: If ``kubectlEnabled`` is ``false``
        '''
        return typing.cast(KubernetesResource, jsii.invoke(self, "addResource", [id, *manifest]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="awsAuth")
    def aws_auth(self) -> AwsAuth:
        '''(deprecated) Lazily creates the AwsAuth resource, which manages AWS authentication mapping.

        :stability: deprecated
        '''
        return typing.cast(AwsAuth, jsii.get(self, "awsAuth"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''(deprecated) The AWS generated ARN for the Cluster resource.

        :stability: deprecated

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            arn:aws:eks:us-west-2666666666666cluster / prod
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterCertificateAuthorityData")
    def cluster_certificate_authority_data(self) -> builtins.str:
        '''(deprecated) The certificate-authority-data for your cluster.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterCertificateAuthorityData"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> builtins.str:
        '''(deprecated) The endpoint URL for the Cluster.

        This is the URL inside the kubeconfig file to use with kubectl

        :stability: deprecated

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            https:
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterEndpoint"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''(deprecated) The Name of the created EKS Cluster.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(deprecated) Manages connection rules (Security Group Rules) for the cluster.

        :stability: deprecated
        :memberof: Cluster
        :type: {ec2.Connections}
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kubectlEnabled")
    def kubectl_enabled(self) -> builtins.bool:
        '''(deprecated) Indicates if ``kubectl`` related operations can be performed on this cluster.

        :stability: deprecated
        '''
        return typing.cast(builtins.bool, jsii.get(self, "kubectlEnabled"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        '''(deprecated) IAM role assumed by the EKS Control Plane.

        :stability: deprecated
        '''
        return typing.cast(aws_cdk.aws_iam.IRole, jsii.get(self, "role"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(deprecated) The VPC in which this Cluster was created.

        :stability: deprecated
        '''
        return typing.cast(aws_cdk.aws_ec2.IVpc, jsii.get(self, "vpc"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultCapacity")
    def default_capacity(
        self,
    ) -> typing.Optional[aws_cdk.aws_autoscaling.AutoScalingGroup]:
        '''(deprecated) The auto scaling group that hosts the default capacity for this cluster.

        This will be ``undefined`` if the default capacity is set to 0.

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_autoscaling.AutoScalingGroup], jsii.get(self, "defaultCapacity"))


__all__ = [
    "AutoScalingGroupOptions",
    "AwsAuth",
    "AwsAuthProps",
    "BootstrapOptions",
    "CapacityOptions",
    "CfnAddon",
    "CfnAddonProps",
    "CfnCluster",
    "CfnClusterProps",
    "CfnFargateProfile",
    "CfnFargateProfileProps",
    "CfnNodegroup",
    "CfnNodegroupProps",
    "Cluster",
    "ClusterAttributes",
    "ClusterProps",
    "EksOptimizedImage",
    "EksOptimizedImageProps",
    "HelmChart",
    "HelmChartOptions",
    "HelmChartProps",
    "ICluster",
    "KubernetesResource",
    "KubernetesResourceProps",
    "Mapping",
    "NodeType",
]

publication.publish()
