# Amazon Elastic Load Balancing Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

The `@aws-cdk/aws-elasticloadbalancing` package provides constructs for configuring
classic load balancers.

## Configuring a Load Balancer

Load balancers send traffic to one or more AutoScalingGroups. Create a load
balancer, set up listeners and a health check, and supply the fleet(s) you want
to load balance to in the `targets` property.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
lb = elb.LoadBalancer(self, "LB",
    vpc=vpc,
    internet_facing=True,
    health_check={
        "port": 80
    }
)

lb.add_target(my_auto_scaling_group)
lb.add_listener(
    external_port=80
)
```

The load balancer allows all connections by default. If you want to change that,
pass the `allowConnectionsFrom` property while setting up the listener:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
lb.add_listener(
    external_port=80,
    allow_connections_from=[my_security_group]
)
```
