# Amazon Route53 Resolver Construct Library

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

## DNS Firewall

With Route 53 Resolver DNS Firewall, you can filter and regulate outbound DNS traffic for your
virtual private connections (VPCs). To do this, you create reusable collections of filtering rules
in DNS Firewall rule groups and associate the rule groups to your VPC.

DNS Firewall provides protection for outbound DNS requests from your VPCs. These requests route
through Resolver for domain name resolution. A primary use of DNS Firewall protections is to help
prevent DNS exfiltration of your data. DNS exfiltration can happen when a bad actor compromises
an application instance in your VPC and then uses DNS lookup to send data out of the VPC to a domain
that they control. With DNS Firewall, you can monitor and control the domains that your applications
can query. You can deny access to the domains that you know to be bad and allow all other queries
to pass through. Alternately, you can deny access to all domains except for the ones that you
explicitly trust.

### Domain lists

Domain lists can be created using a list of strings, a text file stored in Amazon S3 or a local
text file:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
block_list = route53resolver.FirewallDomainList(self, "BlockList",
    domains=route53resolver.FirewallDomains.from_list(["bad-domain.com", "bot-domain.net"])
)

s3_list = route53resolver.FirewallDomainList(self, "S3List",
    domains=route53resolver.FirewallDomains.from_s3_url("s3://bucket/prefix/object")
)

asset_list = route53resolver.FirewallDomainList(self, "AssetList",
    domains=route53resolver.FirewallDomains.from_asset("/path/to/domains.txt")
)
```

The file must be a text file and must contain a single domain per line.

Use `FirewallDomainList.fromFirewallDomainListId()` to import an existing or [AWS managed domain list](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-managed-domain-lists.html):

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# AWSManagedDomainsMalwareDomainList in us-east-1
malware_list = route53resolver.FirewallDomainList.from_firewall_domain_list_id(self, "Malware", "rslvr-fdl-2c46f2ecbfec4dcc")
```

### Rule group

Create a rule group:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
route53resolver.FirewallRuleGroup(self, "RuleGroup",
    rules=[{
        "priority": 10,
        "firewall_domain_list": my_block_list,
        # block and reply with NODATA
        "action": route53resolver.FirewallRuleAction.block()
    }
    ]
)
```

Rules can be added at construction time or using `addRule()`:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
rule_group.add_rule(
    priority=10,
    firewall_domain_list=block_list,
    # block and reply with NXDOMAIN
    action=route53resolver.FirewallRuleAction.block(route53resolver.DnsBlockResponse.nx_domain())
)

rule_group.add_rule(
    priority=20,
    firewall_domain_list=block_list,
    # block and override DNS response with a custom domain
    action=route53resolver.FirewallRuleAction.block(route53resolver.DnsBlockResponse.override("amazon.com"))
)
```

Use `associate()` to associate a rule group with a VPC:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
rule_group.associate(
    priority=101,
    vpc=my_vpc
)
```
