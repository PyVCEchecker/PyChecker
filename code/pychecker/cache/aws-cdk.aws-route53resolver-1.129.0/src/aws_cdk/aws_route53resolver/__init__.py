'''
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

import aws_cdk.aws_ec2
import aws_cdk.aws_s3
import aws_cdk.core
import constructs


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFirewallDomainList(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnFirewallDomainList",
):
    '''A CloudFormation ``AWS::Route53Resolver::FirewallDomainList``.

    :cloudformationResource: AWS::Route53Resolver::FirewallDomainList
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        domain_file_url: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::FirewallDomainList``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_file_url: ``AWS::Route53Resolver::FirewallDomainList.DomainFileUrl``.
        :param domains: ``AWS::Route53Resolver::FirewallDomainList.Domains``.
        :param name: ``AWS::Route53Resolver::FirewallDomainList.Name``.
        :param tags: ``AWS::Route53Resolver::FirewallDomainList.Tags``.
        '''
        props = CfnFirewallDomainListProps(
            domain_file_url=domain_file_url, domains=domains, name=name, tags=tags
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatorRequestId")
    def attr_creator_request_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatorRequestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatorRequestId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDomainCount")
    def attr_domain_count(self) -> jsii.Number:
        '''
        :cloudformationAttribute: DomainCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrDomainCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrManagedOwnerName")
    def attr_managed_owner_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ManagedOwnerName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagedOwnerName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModificationTime")
    def attr_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModificationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''
        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53Resolver::FirewallDomainList.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainFileUrl")
    def domain_file_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallDomainList.DomainFileUrl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domainfileurl
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainFileUrl"))

    @domain_file_url.setter
    def domain_file_url(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "domainFileUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Route53Resolver::FirewallDomainList.Domains``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domains
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domains"))

    @domains.setter
    def domains(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "domains", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallDomainList.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnFirewallDomainListProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_file_url": "domainFileUrl",
        "domains": "domains",
        "name": "name",
        "tags": "tags",
    },
)
class CfnFirewallDomainListProps:
    def __init__(
        self,
        *,
        domain_file_url: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::FirewallDomainList``.

        :param domain_file_url: ``AWS::Route53Resolver::FirewallDomainList.DomainFileUrl``.
        :param domains: ``AWS::Route53Resolver::FirewallDomainList.Domains``.
        :param name: ``AWS::Route53Resolver::FirewallDomainList.Name``.
        :param tags: ``AWS::Route53Resolver::FirewallDomainList.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if domain_file_url is not None:
            self._values["domain_file_url"] = domain_file_url
        if domains is not None:
            self._values["domains"] = domains
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_file_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallDomainList.DomainFileUrl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domainfileurl
        '''
        result = self._values.get("domain_file_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Route53Resolver::FirewallDomainList.Domains``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-domains
        '''
        result = self._values.get("domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallDomainList.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53Resolver::FirewallDomainList.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewalldomainlist.html#cfn-route53resolver-firewalldomainlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallDomainListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFirewallRuleGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnFirewallRuleGroup",
):
    '''A CloudFormation ``AWS::Route53Resolver::FirewallRuleGroup``.

    :cloudformationResource: AWS::Route53Resolver::FirewallRuleGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        firewall_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnFirewallRuleGroup.FirewallRuleProperty", aws_cdk.core.IResolvable]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::FirewallRuleGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param firewall_rules: ``AWS::Route53Resolver::FirewallRuleGroup.FirewallRules``.
        :param name: ``AWS::Route53Resolver::FirewallRuleGroup.Name``.
        :param tags: ``AWS::Route53Resolver::FirewallRuleGroup.Tags``.
        '''
        props = CfnFirewallRuleGroupProps(
            firewall_rules=firewall_rules, name=name, tags=tags
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatorRequestId")
    def attr_creator_request_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatorRequestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatorRequestId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModificationTime")
    def attr_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModificationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRuleCount")
    def attr_rule_count(self) -> jsii.Number:
        '''
        :cloudformationAttribute: RuleCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRuleCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrShareStatus")
    def attr_share_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ShareStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrShareStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''
        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53Resolver::FirewallRuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRules")
    def firewall_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnFirewallRuleGroup.FirewallRuleProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::Route53Resolver::FirewallRuleGroup.FirewallRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-firewallrules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnFirewallRuleGroup.FirewallRuleProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "firewallRules"))

    @firewall_rules.setter
    def firewall_rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnFirewallRuleGroup.FirewallRuleProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "firewallRules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallRuleGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53resolver.CfnFirewallRuleGroup.FirewallRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "firewall_domain_list_id": "firewallDomainListId",
            "priority": "priority",
            "block_override_dns_type": "blockOverrideDnsType",
            "block_override_domain": "blockOverrideDomain",
            "block_override_ttl": "blockOverrideTtl",
            "block_response": "blockResponse",
        },
    )
    class FirewallRuleProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            firewall_domain_list_id: builtins.str,
            priority: jsii.Number,
            block_override_dns_type: typing.Optional[builtins.str] = None,
            block_override_domain: typing.Optional[builtins.str] = None,
            block_override_ttl: typing.Optional[jsii.Number] = None,
            block_response: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param action: ``CfnFirewallRuleGroup.FirewallRuleProperty.Action``.
            :param firewall_domain_list_id: ``CfnFirewallRuleGroup.FirewallRuleProperty.FirewallDomainListId``.
            :param priority: ``CfnFirewallRuleGroup.FirewallRuleProperty.Priority``.
            :param block_override_dns_type: ``CfnFirewallRuleGroup.FirewallRuleProperty.BlockOverrideDnsType``.
            :param block_override_domain: ``CfnFirewallRuleGroup.FirewallRuleProperty.BlockOverrideDomain``.
            :param block_override_ttl: ``CfnFirewallRuleGroup.FirewallRuleProperty.BlockOverrideTtl``.
            :param block_response: ``CfnFirewallRuleGroup.FirewallRuleProperty.BlockResponse``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action": action,
                "firewall_domain_list_id": firewall_domain_list_id,
                "priority": priority,
            }
            if block_override_dns_type is not None:
                self._values["block_override_dns_type"] = block_override_dns_type
            if block_override_domain is not None:
                self._values["block_override_domain"] = block_override_domain
            if block_override_ttl is not None:
                self._values["block_override_ttl"] = block_override_ttl
            if block_response is not None:
                self._values["block_response"] = block_response

        @builtins.property
        def action(self) -> builtins.str:
            '''``CfnFirewallRuleGroup.FirewallRuleProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def firewall_domain_list_id(self) -> builtins.str:
            '''``CfnFirewallRuleGroup.FirewallRuleProperty.FirewallDomainListId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainlistid
            '''
            result = self._values.get("firewall_domain_list_id")
            assert result is not None, "Required property 'firewall_domain_list_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def priority(self) -> jsii.Number:
            '''``CfnFirewallRuleGroup.FirewallRuleProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def block_override_dns_type(self) -> typing.Optional[builtins.str]:
            '''``CfnFirewallRuleGroup.FirewallRuleProperty.BlockOverrideDnsType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridednstype
            '''
            result = self._values.get("block_override_dns_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def block_override_domain(self) -> typing.Optional[builtins.str]:
            '''``CfnFirewallRuleGroup.FirewallRuleProperty.BlockOverrideDomain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridedomain
            '''
            result = self._values.get("block_override_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def block_override_ttl(self) -> typing.Optional[jsii.Number]:
            '''``CfnFirewallRuleGroup.FirewallRuleProperty.BlockOverrideTtl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridettl
            '''
            result = self._values.get("block_override_ttl")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def block_response(self) -> typing.Optional[builtins.str]:
            '''``CfnFirewallRuleGroup.FirewallRuleProperty.BlockResponse``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-firewallrulegroup-firewallrule.html#cfn-route53resolver-firewallrulegroup-firewallrule-blockresponse
            '''
            result = self._values.get("block_response")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirewallRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFirewallRuleGroupAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnFirewallRuleGroupAssociation",
):
    '''A CloudFormation ``AWS::Route53Resolver::FirewallRuleGroupAssociation``.

    :cloudformationResource: AWS::Route53Resolver::FirewallRuleGroupAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        firewall_rule_group_id: builtins.str,
        priority: jsii.Number,
        vpc_id: builtins.str,
        mutation_protection: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::FirewallRuleGroupAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param firewall_rule_group_id: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.FirewallRuleGroupId``.
        :param priority: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.Priority``.
        :param vpc_id: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.VpcId``.
        :param mutation_protection: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.MutationProtection``.
        :param name: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.Name``.
        :param tags: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.Tags``.
        '''
        props = CfnFirewallRuleGroupAssociationProps(
            firewall_rule_group_id=firewall_rule_group_id,
            priority=priority,
            vpc_id=vpc_id,
            mutation_protection=mutation_protection,
            name=name,
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatorRequestId")
    def attr_creator_request_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatorRequestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatorRequestId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrManagedOwnerName")
    def attr_managed_owner_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ManagedOwnerName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagedOwnerName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModificationTime")
    def attr_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModificationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''
        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> builtins.str:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.FirewallRuleGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupId"))

    @firewall_rule_group_id.setter
    def firewall_rule_group_id(self, value: builtins.str) -> None:
        jsii.set(self, "firewallRuleGroupId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.Priority``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-priority
        '''
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        jsii.set(self, "priority", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-vpcid
        '''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        jsii.set(self, "vpcId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mutationProtection")
    def mutation_protection(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.MutationProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-mutationprotection
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mutationProtection"))

    @mutation_protection.setter
    def mutation_protection(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "mutationProtection", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnFirewallRuleGroupAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_rule_group_id": "firewallRuleGroupId",
        "priority": "priority",
        "vpc_id": "vpcId",
        "mutation_protection": "mutationProtection",
        "name": "name",
        "tags": "tags",
    },
)
class CfnFirewallRuleGroupAssociationProps:
    def __init__(
        self,
        *,
        firewall_rule_group_id: builtins.str,
        priority: jsii.Number,
        vpc_id: builtins.str,
        mutation_protection: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::FirewallRuleGroupAssociation``.

        :param firewall_rule_group_id: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.FirewallRuleGroupId``.
        :param priority: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.Priority``.
        :param vpc_id: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.VpcId``.
        :param mutation_protection: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.MutationProtection``.
        :param name: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.Name``.
        :param tags: ``AWS::Route53Resolver::FirewallRuleGroupAssociation.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "firewall_rule_group_id": firewall_rule_group_id,
            "priority": priority,
            "vpc_id": vpc_id,
        }
        if mutation_protection is not None:
            self._values["mutation_protection"] = mutation_protection
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firewall_rule_group_id(self) -> builtins.str:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.FirewallRuleGroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-firewallrulegroupid
        '''
        result = self._values.get("firewall_rule_group_id")
        assert result is not None, "Required property 'firewall_rule_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.Priority``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-priority
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mutation_protection(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.MutationProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-mutationprotection
        '''
        result = self._values.get("mutation_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53Resolver::FirewallRuleGroupAssociation.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroupassociation.html#cfn-route53resolver-firewallrulegroupassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallRuleGroupAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnFirewallRuleGroupProps",
    jsii_struct_bases=[],
    name_mapping={"firewall_rules": "firewallRules", "name": "name", "tags": "tags"},
)
class CfnFirewallRuleGroupProps:
    def __init__(
        self,
        *,
        firewall_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnFirewallRuleGroup.FirewallRuleProperty, aws_cdk.core.IResolvable]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::FirewallRuleGroup``.

        :param firewall_rules: ``AWS::Route53Resolver::FirewallRuleGroup.FirewallRules``.
        :param name: ``AWS::Route53Resolver::FirewallRuleGroup.Name``.
        :param tags: ``AWS::Route53Resolver::FirewallRuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if firewall_rules is not None:
            self._values["firewall_rules"] = firewall_rules
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firewall_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnFirewallRuleGroup.FirewallRuleProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::Route53Resolver::FirewallRuleGroup.FirewallRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-firewallrules
        '''
        result = self._values.get("firewall_rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnFirewallRuleGroup.FirewallRuleProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::FirewallRuleGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53Resolver::FirewallRuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-firewallrulegroup.html#cfn-route53resolver-firewallrulegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFirewallRuleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverDNSSECConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverDNSSECConfig",
):
    '''A CloudFormation ``AWS::Route53Resolver::ResolverDNSSECConfig``.

    :cloudformationResource: AWS::Route53Resolver::ResolverDNSSECConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resource_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::ResolverDNSSECConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_id: ``AWS::Route53Resolver::ResolverDNSSECConfig.ResourceId``.
        '''
        props = CfnResolverDNSSECConfigProps(resource_id=resource_id)

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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrValidationStatus")
    def attr_validation_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ValidationStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrValidationStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverDNSSECConfig.ResourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#cfn-route53resolver-resolverdnssecconfig-resourceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resourceId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverDNSSECConfigProps",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId"},
)
class CfnResolverDNSSECConfigProps:
    def __init__(self, *, resource_id: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::ResolverDNSSECConfig``.

        :param resource_id: ``AWS::Route53Resolver::ResolverDNSSECConfig.ResourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if resource_id is not None:
            self._values["resource_id"] = resource_id

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverDNSSECConfig.ResourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverdnssecconfig.html#cfn-route53resolver-resolverdnssecconfig-resourceid
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverDNSSECConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverEndpoint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverEndpoint",
):
    '''A CloudFormation ``AWS::Route53Resolver::ResolverEndpoint``.

    :cloudformationResource: AWS::Route53Resolver::ResolverEndpoint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        direction: builtins.str,
        ip_addresses: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnResolverEndpoint.IpAddressRequestProperty"]]],
        security_group_ids: typing.Sequence[builtins.str],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::ResolverEndpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param direction: ``AWS::Route53Resolver::ResolverEndpoint.Direction``.
        :param ip_addresses: ``AWS::Route53Resolver::ResolverEndpoint.IpAddresses``.
        :param security_group_ids: ``AWS::Route53Resolver::ResolverEndpoint.SecurityGroupIds``.
        :param name: ``AWS::Route53Resolver::ResolverEndpoint.Name``.
        :param tags: ``AWS::Route53Resolver::ResolverEndpoint.Tags``.
        '''
        props = CfnResolverEndpointProps(
            direction=direction,
            ip_addresses=ip_addresses,
            security_group_ids=security_group_ids,
            name=name,
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
    @jsii.member(jsii_name="attrDirection")
    def attr_direction(self) -> builtins.str:
        '''
        :cloudformationAttribute: Direction
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDirection"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHostVpcId")
    def attr_host_vpc_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: HostVPCId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHostVpcId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIpAddressCount")
    def attr_ip_address_count(self) -> builtins.str:
        '''
        :cloudformationAttribute: IpAddressCount
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAddressCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResolverEndpointId")
    def attr_resolver_endpoint_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResolverEndpointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverEndpointId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53Resolver::ResolverEndpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverEndpoint.Direction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-direction
        '''
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        jsii.set(self, "direction", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnResolverEndpoint.IpAddressRequestProperty"]]]:
        '''``AWS::Route53Resolver::ResolverEndpoint.IpAddresses``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-ipaddresses
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnResolverEndpoint.IpAddressRequestProperty"]]], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnResolverEndpoint.IpAddressRequestProperty"]]],
    ) -> None:
        jsii.set(self, "ipAddresses", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''``AWS::Route53Resolver::ResolverEndpoint.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-securitygroupids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverEndpoint.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53resolver.CfnResolverEndpoint.IpAddressRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_id": "subnetId", "ip": "ip"},
    )
    class IpAddressRequestProperty:
        def __init__(
            self,
            *,
            subnet_id: builtins.str,
            ip: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param subnet_id: ``CfnResolverEndpoint.IpAddressRequestProperty.SubnetId``.
            :param ip: ``CfnResolverEndpoint.IpAddressRequestProperty.Ip``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "subnet_id": subnet_id,
            }
            if ip is not None:
                self._values["ip"] = ip

        @builtins.property
        def subnet_id(self) -> builtins.str:
            '''``CfnResolverEndpoint.IpAddressRequestProperty.SubnetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-subnetid
            '''
            result = self._values.get("subnet_id")
            assert result is not None, "Required property 'subnet_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ip(self) -> typing.Optional[builtins.str]:
            '''``CfnResolverEndpoint.IpAddressRequestProperty.Ip``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverendpoint-ipaddressrequest.html#cfn-route53resolver-resolverendpoint-ipaddressrequest-ip
            '''
            result = self._values.get("ip")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpAddressRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "direction": "direction",
        "ip_addresses": "ipAddresses",
        "security_group_ids": "securityGroupIds",
        "name": "name",
        "tags": "tags",
    },
)
class CfnResolverEndpointProps:
    def __init__(
        self,
        *,
        direction: builtins.str,
        ip_addresses: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnResolverEndpoint.IpAddressRequestProperty]]],
        security_group_ids: typing.Sequence[builtins.str],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::ResolverEndpoint``.

        :param direction: ``AWS::Route53Resolver::ResolverEndpoint.Direction``.
        :param ip_addresses: ``AWS::Route53Resolver::ResolverEndpoint.IpAddresses``.
        :param security_group_ids: ``AWS::Route53Resolver::ResolverEndpoint.SecurityGroupIds``.
        :param name: ``AWS::Route53Resolver::ResolverEndpoint.Name``.
        :param tags: ``AWS::Route53Resolver::ResolverEndpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "direction": direction,
            "ip_addresses": ip_addresses,
            "security_group_ids": security_group_ids,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def direction(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverEndpoint.Direction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-direction
        '''
        result = self._values.get("direction")
        assert result is not None, "Required property 'direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_addresses(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnResolverEndpoint.IpAddressRequestProperty]]]:
        '''``AWS::Route53Resolver::ResolverEndpoint.IpAddresses``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-ipaddresses
        '''
        result = self._values.get("ip_addresses")
        assert result is not None, "Required property 'ip_addresses' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnResolverEndpoint.IpAddressRequestProperty]]], result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''``AWS::Route53Resolver::ResolverEndpoint.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverEndpoint.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53Resolver::ResolverEndpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html#cfn-route53resolver-resolverendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverQueryLoggingConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverQueryLoggingConfig",
):
    '''A CloudFormation ``AWS::Route53Resolver::ResolverQueryLoggingConfig``.

    :cloudformationResource: AWS::Route53Resolver::ResolverQueryLoggingConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        destination_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::ResolverQueryLoggingConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param destination_arn: ``AWS::Route53Resolver::ResolverQueryLoggingConfig.DestinationArn``.
        :param name: ``AWS::Route53Resolver::ResolverQueryLoggingConfig.Name``.
        '''
        props = CfnResolverQueryLoggingConfigProps(
            destination_arn=destination_arn, name=name
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
    @jsii.member(jsii_name="attrAssociationCount")
    def attr_association_count(self) -> jsii.Number:
        '''
        :cloudformationAttribute: AssociationCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAssociationCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCreatorRequestId")
    def attr_creator_request_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatorRequestId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatorRequestId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrShareStatus")
    def attr_share_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ShareStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrShareStatus"))

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
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverQueryLoggingConfig.DestinationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-destinationarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationArn"))

    @destination_arn.setter
    def destination_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "destinationArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverQueryLoggingConfig.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverQueryLoggingConfigAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverQueryLoggingConfigAssociation",
):
    '''A CloudFormation ``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation``.

    :cloudformationResource: AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resolver_query_log_config_id: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resolver_query_log_config_id: ``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.ResolverQueryLogConfigId``.
        :param resource_id: ``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.ResourceId``.
        '''
        props = CfnResolverQueryLoggingConfigAssociationProps(
            resolver_query_log_config_id=resolver_query_log_config_id,
            resource_id=resource_id,
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrError")
    def attr_error(self) -> builtins.str:
        '''
        :cloudformationAttribute: Error
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrError"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrErrorMessage")
    def attr_error_message(self) -> builtins.str:
        '''
        :cloudformationAttribute: ErrorMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrErrorMessage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.ResolverQueryLogConfigId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resolverquerylogconfigid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolverQueryLogConfigId"))

    @resolver_query_log_config_id.setter
    def resolver_query_log_config_id(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "resolverQueryLogConfigId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.ResourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resourceid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resourceId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverQueryLoggingConfigAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "resolver_query_log_config_id": "resolverQueryLogConfigId",
        "resource_id": "resourceId",
    },
)
class CfnResolverQueryLoggingConfigAssociationProps:
    def __init__(
        self,
        *,
        resolver_query_log_config_id: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation``.

        :param resolver_query_log_config_id: ``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.ResolverQueryLogConfigId``.
        :param resource_id: ``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.ResourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if resolver_query_log_config_id is not None:
            self._values["resolver_query_log_config_id"] = resolver_query_log_config_id
        if resource_id is not None:
            self._values["resource_id"] = resource_id

    @builtins.property
    def resolver_query_log_config_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.ResolverQueryLogConfigId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resolverquerylogconfigid
        '''
        result = self._values.get("resolver_query_log_config_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.ResourceId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfigassociation.html#cfn-route53resolver-resolverqueryloggingconfigassociation-resourceid
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverQueryLoggingConfigAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverQueryLoggingConfigProps",
    jsii_struct_bases=[],
    name_mapping={"destination_arn": "destinationArn", "name": "name"},
)
class CfnResolverQueryLoggingConfigProps:
    def __init__(
        self,
        *,
        destination_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::ResolverQueryLoggingConfig``.

        :param destination_arn: ``AWS::Route53Resolver::ResolverQueryLoggingConfig.DestinationArn``.
        :param name: ``AWS::Route53Resolver::ResolverQueryLoggingConfig.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if destination_arn is not None:
            self._values["destination_arn"] = destination_arn
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def destination_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverQueryLoggingConfig.DestinationArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-destinationarn
        '''
        result = self._values.get("destination_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverQueryLoggingConfig.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverqueryloggingconfig.html#cfn-route53resolver-resolverqueryloggingconfig-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverQueryLoggingConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverRule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRule",
):
    '''A CloudFormation ``AWS::Route53Resolver::ResolverRule``.

    :cloudformationResource: AWS::Route53Resolver::ResolverRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        rule_type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        resolver_endpoint_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        target_ips: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnResolverRule.TargetAddressProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::ResolverRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::Route53Resolver::ResolverRule.DomainName``.
        :param rule_type: ``AWS::Route53Resolver::ResolverRule.RuleType``.
        :param name: ``AWS::Route53Resolver::ResolverRule.Name``.
        :param resolver_endpoint_id: ``AWS::Route53Resolver::ResolverRule.ResolverEndpointId``.
        :param tags: ``AWS::Route53Resolver::ResolverRule.Tags``.
        :param target_ips: ``AWS::Route53Resolver::ResolverRule.TargetIps``.
        '''
        props = CfnResolverRuleProps(
            domain_name=domain_name,
            rule_type=rule_type,
            name=name,
            resolver_endpoint_id=resolver_endpoint_id,
            tags=tags,
            target_ips=target_ips,
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
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResolverEndpointId")
    def attr_resolver_endpoint_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResolverEndpointId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverEndpointId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResolverRuleId")
    def attr_resolver_rule_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResolverRuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverRuleId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTargetIps")
    def attr_target_ips(self) -> builtins.str:
        '''
        :cloudformationAttribute: TargetIps
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetIps"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Route53Resolver::ResolverRule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverRule.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleType")
    def rule_type(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverRule.RuleType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-ruletype
        '''
        return typing.cast(builtins.str, jsii.get(self, "ruleType"))

    @rule_type.setter
    def rule_type(self, value: builtins.str) -> None:
        jsii.set(self, "ruleType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverRule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resolverEndpointId")
    def resolver_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverRule.ResolverEndpointId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-resolverendpointid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolverEndpointId"))

    @resolver_endpoint_id.setter
    def resolver_endpoint_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resolverEndpointId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetIps")
    def target_ips(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnResolverRule.TargetAddressProperty"]]]]:
        '''``AWS::Route53Resolver::ResolverRule.TargetIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-targetips
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnResolverRule.TargetAddressProperty"]]]], jsii.get(self, "targetIps"))

    @target_ips.setter
    def target_ips(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnResolverRule.TargetAddressProperty"]]]],
    ) -> None:
        jsii.set(self, "targetIps", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRule.TargetAddressProperty",
        jsii_struct_bases=[],
        name_mapping={"ip": "ip", "port": "port"},
    )
    class TargetAddressProperty:
        def __init__(
            self,
            *,
            ip: builtins.str,
            port: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param ip: ``CfnResolverRule.TargetAddressProperty.Ip``.
            :param port: ``CfnResolverRule.TargetAddressProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "ip": ip,
            }
            if port is not None:
                self._values["port"] = port

        @builtins.property
        def ip(self) -> builtins.str:
            '''``CfnResolverRule.TargetAddressProperty.Ip``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-ip
            '''
            result = self._values.get("ip")
            assert result is not None, "Required property 'ip' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''``CfnResolverRule.TargetAddressProperty.Port``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53resolver-resolverrule-targetaddress.html#cfn-route53resolver-resolverrule-targetaddress-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetAddressProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResolverRuleAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRuleAssociation",
):
    '''A CloudFormation ``AWS::Route53Resolver::ResolverRuleAssociation``.

    :cloudformationResource: AWS::Route53Resolver::ResolverRuleAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resolver_rule_id: builtins.str,
        vpc_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Route53Resolver::ResolverRuleAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resolver_rule_id: ``AWS::Route53Resolver::ResolverRuleAssociation.ResolverRuleId``.
        :param vpc_id: ``AWS::Route53Resolver::ResolverRuleAssociation.VPCId``.
        :param name: ``AWS::Route53Resolver::ResolverRuleAssociation.Name``.
        '''
        props = CfnResolverRuleAssociationProps(
            resolver_rule_id=resolver_rule_id, vpc_id=vpc_id, name=name
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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResolverRuleAssociationId")
    def attr_resolver_rule_association_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResolverRuleAssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverRuleAssociationId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrResolverRuleId")
    def attr_resolver_rule_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResolverRuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResolverRuleId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVpcId")
    def attr_vpc_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: VPCId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resolverRuleId")
    def resolver_rule_id(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverRuleAssociation.ResolverRuleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-resolverruleid
        '''
        return typing.cast(builtins.str, jsii.get(self, "resolverRuleId"))

    @resolver_rule_id.setter
    def resolver_rule_id(self, value: builtins.str) -> None:
        jsii.set(self, "resolverRuleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverRuleAssociation.VPCId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-vpcid
        '''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        jsii.set(self, "vpcId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverRuleAssociation.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRuleAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "resolver_rule_id": "resolverRuleId",
        "vpc_id": "vpcId",
        "name": "name",
    },
)
class CfnResolverRuleAssociationProps:
    def __init__(
        self,
        *,
        resolver_rule_id: builtins.str,
        vpc_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::ResolverRuleAssociation``.

        :param resolver_rule_id: ``AWS::Route53Resolver::ResolverRuleAssociation.ResolverRuleId``.
        :param vpc_id: ``AWS::Route53Resolver::ResolverRuleAssociation.VPCId``.
        :param name: ``AWS::Route53Resolver::ResolverRuleAssociation.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resolver_rule_id": resolver_rule_id,
            "vpc_id": vpc_id,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def resolver_rule_id(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverRuleAssociation.ResolverRuleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-resolverruleid
        '''
        result = self._values.get("resolver_rule_id")
        assert result is not None, "Required property 'resolver_rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverRuleAssociation.VPCId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverRuleAssociation.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html#cfn-route53resolver-resolverruleassociation-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverRuleAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.CfnResolverRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "rule_type": "ruleType",
        "name": "name",
        "resolver_endpoint_id": "resolverEndpointId",
        "tags": "tags",
        "target_ips": "targetIps",
    },
)
class CfnResolverRuleProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        rule_type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        resolver_endpoint_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        target_ips: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnResolverRule.TargetAddressProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Route53Resolver::ResolverRule``.

        :param domain_name: ``AWS::Route53Resolver::ResolverRule.DomainName``.
        :param rule_type: ``AWS::Route53Resolver::ResolverRule.RuleType``.
        :param name: ``AWS::Route53Resolver::ResolverRule.Name``.
        :param resolver_endpoint_id: ``AWS::Route53Resolver::ResolverRule.ResolverEndpointId``.
        :param tags: ``AWS::Route53Resolver::ResolverRule.Tags``.
        :param target_ips: ``AWS::Route53Resolver::ResolverRule.TargetIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
            "rule_type": rule_type,
        }
        if name is not None:
            self._values["name"] = name
        if resolver_endpoint_id is not None:
            self._values["resolver_endpoint_id"] = resolver_endpoint_id
        if tags is not None:
            self._values["tags"] = tags
        if target_ips is not None:
            self._values["target_ips"] = target_ips

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverRule.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_type(self) -> builtins.str:
        '''``AWS::Route53Resolver::ResolverRule.RuleType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-ruletype
        '''
        result = self._values.get("rule_type")
        assert result is not None, "Required property 'rule_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverRule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolver_endpoint_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Route53Resolver::ResolverRule.ResolverEndpointId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-resolverendpointid
        '''
        result = self._values.get("resolver_endpoint_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Route53Resolver::ResolverRule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def target_ips(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnResolverRule.TargetAddressProperty]]]]:
        '''``AWS::Route53Resolver::ResolverRule.TargetIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html#cfn-route53resolver-resolverrule-targetips
        '''
        result = self._values.get("target_ips")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnResolverRule.TargetAddressProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DnsBlockResponse(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-route53resolver.DnsBlockResponse",
):
    '''(experimental) The way that you want DNS Firewall to block the request.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="noData") # type: ignore[misc]
    @builtins.classmethod
    def no_data(cls) -> "DnsBlockResponse":
        '''(experimental) Respond indicating that the query was successful, but no response is available for it.

        :stability: experimental
        '''
        return typing.cast("DnsBlockResponse", jsii.sinvoke(cls, "noData", []))

    @jsii.member(jsii_name="nxDomain") # type: ignore[misc]
    @builtins.classmethod
    def nx_domain(cls) -> "DnsBlockResponse":
        '''(experimental) Respond indicating that the domain name that's in the query doesn't exist.

        :stability: experimental
        '''
        return typing.cast("DnsBlockResponse", jsii.sinvoke(cls, "nxDomain", []))

    @jsii.member(jsii_name="override") # type: ignore[misc]
    @builtins.classmethod
    def override(
        cls,
        domain: builtins.str,
        ttl: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> "DnsBlockResponse":
        '''(experimental) Provides a custom override response to the query.

        :param domain: The custom DNS record to send back in response to the query.
        :param ttl: The recommended amount of time for the DNS resolver or web browser to cache the provided override record.

        :stability: experimental
        '''
        return typing.cast("DnsBlockResponse", jsii.sinvoke(cls, "override", [domain, ttl]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockOverrideDnsType")
    @abc.abstractmethod
    def block_override_dns_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) The DNS record's type.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockOverrideDomain")
    @abc.abstractmethod
    def block_override_domain(self) -> typing.Optional[builtins.str]:
        '''(experimental) The custom DNS record to send back in response to the query.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockOverrideTtl")
    @abc.abstractmethod
    def block_override_ttl(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''(experimental) The recommended amount of time for the DNS resolver or web browser to cache the provided override record.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockResponse")
    @abc.abstractmethod
    def block_response(self) -> typing.Optional[builtins.str]:
        '''(experimental) The way that you want DNS Firewall to block the request.

        :stability: experimental
        '''
        ...


class _DnsBlockResponseProxy(DnsBlockResponse):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockOverrideDnsType")
    def block_override_dns_type(self) -> typing.Optional[builtins.str]:
        '''(experimental) The DNS record's type.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockOverrideDnsType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockOverrideDomain")
    def block_override_domain(self) -> typing.Optional[builtins.str]:
        '''(experimental) The custom DNS record to send back in response to the query.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockOverrideDomain"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockOverrideTtl")
    def block_override_ttl(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''(experimental) The recommended amount of time for the DNS resolver or web browser to cache the provided override record.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.core.Duration], jsii.get(self, "blockOverrideTtl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockResponse")
    def block_response(self) -> typing.Optional[builtins.str]:
        '''(experimental) The way that you want DNS Firewall to block the request.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockResponse"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DnsBlockResponse).__jsii_proxy_class__ = lambda : _DnsBlockResponseProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.DomainsConfig",
    jsii_struct_bases=[],
    name_mapping={"domain_file_url": "domainFileUrl", "domains": "domains"},
)
class DomainsConfig:
    def __init__(
        self,
        *,
        domain_file_url: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Domains configuration.

        :param domain_file_url: (experimental) The fully qualified URL or URI of the file stored in Amazon S3 that contains the list of domains to import. The file must be a text file and must contain a single domain per line. The content type of the S3 object must be ``plain/text``. Default: - use ``domains``
        :param domains: (experimental) A list of domains. Default: - use ``domainFileUrl``

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if domain_file_url is not None:
            self._values["domain_file_url"] = domain_file_url
        if domains is not None:
            self._values["domains"] = domains

    @builtins.property
    def domain_file_url(self) -> typing.Optional[builtins.str]:
        '''(experimental) The fully qualified URL or URI of the file stored in Amazon S3 that contains the list of domains to import.

        The file must be a text file and must contain
        a single domain per line. The content type of the S3 object must be ``plain/text``.

        :default: - use ``domains``

        :stability: experimental
        '''
        result = self._values.get("domain_file_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) A list of domains.

        :default: - use ``domainFileUrl``

        :stability: experimental
        '''
        result = self._values.get("domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.FirewallDomainListProps",
    jsii_struct_bases=[],
    name_mapping={"domains": "domains", "name": "name"},
)
class FirewallDomainListProps:
    def __init__(
        self,
        *,
        domains: "FirewallDomains",
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for a Firewall Domain List.

        :param domains: (experimental) A list of domains.
        :param name: (experimental) A name for the domain list. Default: - a CloudFormation generated name

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domains": domains,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def domains(self) -> "FirewallDomains":
        '''(experimental) A list of domains.

        :stability: experimental
        '''
        result = self._values.get("domains")
        assert result is not None, "Required property 'domains' is missing"
        return typing.cast("FirewallDomains", result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the domain list.

        :default: - a CloudFormation generated name

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallDomainListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallDomains(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-route53resolver.FirewallDomains",
):
    '''(experimental) A list of domains.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset") # type: ignore[misc]
    @builtins.classmethod
    def from_asset(cls, asset_path: builtins.str) -> "FirewallDomains":
        '''(experimental) Firewall domains created from a local disk path to a text file.

        The file must be a text file (``.txt`` extension) and must contain a single
        domain per line. It will be uploaded to S3.

        :param asset_path: path to the text file.

        :stability: experimental
        '''
        return typing.cast("FirewallDomains", jsii.sinvoke(cls, "fromAsset", [asset_path]))

    @jsii.member(jsii_name="fromList") # type: ignore[misc]
    @builtins.classmethod
    def from_list(cls, list: typing.Sequence[builtins.str]) -> "FirewallDomains":
        '''(experimental) Firewall domains created from a list of domains.

        :param list: the list of domains.

        :stability: experimental
        '''
        return typing.cast("FirewallDomains", jsii.sinvoke(cls, "fromList", [list]))

    @jsii.member(jsii_name="fromS3") # type: ignore[misc]
    @builtins.classmethod
    def from_s3(
        cls,
        bucket: aws_cdk.aws_s3.IBucket,
        key: builtins.str,
    ) -> "FirewallDomains":
        '''(experimental) Firewall domains created from a file stored in Amazon S3.

        The file must be a text file and must contain a single domain per line.
        The content type of the S3 object must be ``plain/text``.

        :param bucket: S3 bucket.
        :param key: S3 key.

        :stability: experimental
        '''
        return typing.cast("FirewallDomains", jsii.sinvoke(cls, "fromS3", [bucket, key]))

    @jsii.member(jsii_name="fromS3Url") # type: ignore[misc]
    @builtins.classmethod
    def from_s3_url(cls, url: builtins.str) -> "FirewallDomains":
        '''(experimental) Firewall domains created from the URL of a file stored in Amazon S3.

        The file must be a text file and must contain a single domain per line.
        The content type of the S3 object must be ``plain/text``.

        :param url: S3 bucket url (s3://bucket/prefix/objet).

        :stability: experimental
        '''
        return typing.cast("FirewallDomains", jsii.sinvoke(cls, "fromS3Url", [url]))

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, scope: constructs.Construct) -> DomainsConfig:
        '''(experimental) Binds the domains to a domain list.

        :param scope: -

        :stability: experimental
        '''
        ...


class _FirewallDomainsProxy(FirewallDomains):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: constructs.Construct) -> DomainsConfig:
        '''(experimental) Binds the domains to a domain list.

        :param scope: -

        :stability: experimental
        '''
        return typing.cast(DomainsConfig, jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, FirewallDomains).__jsii_proxy_class__ = lambda : _FirewallDomainsProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.FirewallRule",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "firewall_domain_list": "firewallDomainList",
        "priority": "priority",
    },
)
class FirewallRule:
    def __init__(
        self,
        *,
        action: "FirewallRuleAction",
        firewall_domain_list: "IFirewallDomainList",
        priority: jsii.Number,
    ) -> None:
        '''(experimental) A Firewall Rule.

        :param action: (experimental) The action for this rule.
        :param firewall_domain_list: (experimental) The domain list for this rule.
        :param priority: (experimental) The priority of the rule in the rule group. This value must be unique within the rule group.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "firewall_domain_list": firewall_domain_list,
            "priority": priority,
        }

    @builtins.property
    def action(self) -> "FirewallRuleAction":
        '''(experimental) The action for this rule.

        :stability: experimental
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("FirewallRuleAction", result)

    @builtins.property
    def firewall_domain_list(self) -> "IFirewallDomainList":
        '''(experimental) The domain list for this rule.

        :stability: experimental
        '''
        result = self._values.get("firewall_domain_list")
        assert result is not None, "Required property 'firewall_domain_list' is missing"
        return typing.cast("IFirewallDomainList", result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''(experimental) The priority of the rule in the rule group.

        This value must be unique within
        the rule group.

        :stability: experimental
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FirewallRuleAction(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-route53resolver.FirewallRuleAction",
):
    '''(experimental) A Firewall Rule.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="alert") # type: ignore[misc]
    @builtins.classmethod
    def alert(cls) -> "FirewallRuleAction":
        '''(experimental) Permit the request to go through but send an alert to the logs.

        :stability: experimental
        '''
        return typing.cast("FirewallRuleAction", jsii.sinvoke(cls, "alert", []))

    @jsii.member(jsii_name="allow") # type: ignore[misc]
    @builtins.classmethod
    def allow(cls) -> "FirewallRuleAction":
        '''(experimental) Permit the request to go through.

        :stability: experimental
        '''
        return typing.cast("FirewallRuleAction", jsii.sinvoke(cls, "allow", []))

    @jsii.member(jsii_name="block") # type: ignore[misc]
    @builtins.classmethod
    def block(
        cls,
        response: typing.Optional[DnsBlockResponse] = None,
    ) -> "FirewallRuleAction":
        '''(experimental) Disallow the request.

        :param response: The way that you want DNS Firewall to block the request.

        :stability: experimental
        '''
        return typing.cast("FirewallRuleAction", jsii.sinvoke(cls, "block", [response]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="action")
    @abc.abstractmethod
    def action(self) -> builtins.str:
        '''(experimental) The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list.

        :stability: experimental
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockResponse")
    @abc.abstractmethod
    def block_response(self) -> typing.Optional[DnsBlockResponse]:
        '''(experimental) The way that you want DNS Firewall to block the request.

        :stability: experimental
        '''
        ...


class _FirewallRuleActionProxy(FirewallRuleAction):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        '''(experimental) The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockResponse")
    def block_response(self) -> typing.Optional[DnsBlockResponse]:
        '''(experimental) The way that you want DNS Firewall to block the request.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[DnsBlockResponse], jsii.get(self, "blockResponse"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, FirewallRuleAction).__jsii_proxy_class__ = lambda : _FirewallRuleActionProxy


class FirewallRuleGroupAssociation(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.FirewallRuleGroupAssociation",
):
    '''(experimental) A Firewall Rule Group Association.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        firewall_rule_group: "IFirewallRuleGroup",
        priority: jsii.Number,
        vpc: aws_cdk.aws_ec2.IVpc,
        mutation_protection: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param firewall_rule_group: (experimental) The firewall rule group which must be associated.
        :param priority: (experimental) The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. This value must be greater than 100 and less than 9,000
        :param vpc: (experimental) The VPC that to associate with the rule group.
        :param mutation_protection: (experimental) If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. Default: true
        :param name: (experimental) The name of the association. Default: - a CloudFormation generated name

        :stability: experimental
        '''
        props = FirewallRuleGroupAssociationProps(
            firewall_rule_group=firewall_rule_group,
            priority=priority,
            vpc=vpc,
            mutation_protection=mutation_protection,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupAssociationArn")
    def firewall_rule_group_association_arn(self) -> builtins.str:
        '''(experimental) The ARN (Amazon Resource Name) of the association.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupAssociationArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupAssociationCreationTime")
    def firewall_rule_group_association_creation_time(self) -> builtins.str:
        '''(experimental) The date and time that the association was created.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupAssociationCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupAssociationCreatorRequestId")
    def firewall_rule_group_association_creator_request_id(self) -> builtins.str:
        '''(experimental) The creator request ID.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupAssociationCreatorRequestId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupAssociationId")
    def firewall_rule_group_association_id(self) -> builtins.str:
        '''(experimental) The ID of the association.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupAssociationId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupAssociationManagedOwnerName")
    def firewall_rule_group_association_managed_owner_name(self) -> builtins.str:
        '''(experimental) The owner of the association, used only for lists that are not managed by you.

        If you use AWS Firewall Manager to manage your firewallls from DNS Firewall,
        then this reports Firewall Manager as the managed owner.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupAssociationManagedOwnerName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupAssociationModificationTime")
    def firewall_rule_group_association_modification_time(self) -> builtins.str:
        '''(experimental) The date and time that the association was last modified.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupAssociationModificationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupAssociationStatus")
    def firewall_rule_group_association_status(self) -> builtins.str:
        '''(experimental) The status of the association.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupAssociationStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupAssociationStatusMessage")
    def firewall_rule_group_association_status_message(self) -> builtins.str:
        '''(experimental) Additional information about the status of the association.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupAssociationStatusMessage"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.FirewallRuleGroupAssociationOptions",
    jsii_struct_bases=[],
    name_mapping={
        "priority": "priority",
        "vpc": "vpc",
        "mutation_protection": "mutationProtection",
        "name": "name",
    },
)
class FirewallRuleGroupAssociationOptions:
    def __init__(
        self,
        *,
        priority: jsii.Number,
        vpc: aws_cdk.aws_ec2.IVpc,
        mutation_protection: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options for a Firewall Rule Group Association.

        :param priority: (experimental) The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. This value must be greater than 100 and less than 9,000
        :param vpc: (experimental) The VPC that to associate with the rule group.
        :param mutation_protection: (experimental) If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. Default: true
        :param name: (experimental) The name of the association. Default: - a CloudFormation generated name

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "vpc": vpc,
        }
        if mutation_protection is not None:
            self._values["mutation_protection"] = mutation_protection
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def priority(self) -> jsii.Number:
        '''(experimental) The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC.

        DNS Firewall filters VPC
        traffic starting from rule group with the lowest numeric priority setting.

        This value must be greater than 100 and less than 9,000

        :stability: experimental
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(experimental) The VPC that to associate with the rule group.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    @builtins.property
    def mutation_protection(self) -> typing.Optional[builtins.bool]:
        '''(experimental) If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("mutation_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the association.

        :default: - a CloudFormation generated name

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRuleGroupAssociationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.FirewallRuleGroupAssociationProps",
    jsii_struct_bases=[FirewallRuleGroupAssociationOptions],
    name_mapping={
        "priority": "priority",
        "vpc": "vpc",
        "mutation_protection": "mutationProtection",
        "name": "name",
        "firewall_rule_group": "firewallRuleGroup",
    },
)
class FirewallRuleGroupAssociationProps(FirewallRuleGroupAssociationOptions):
    def __init__(
        self,
        *,
        priority: jsii.Number,
        vpc: aws_cdk.aws_ec2.IVpc,
        mutation_protection: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
        firewall_rule_group: "IFirewallRuleGroup",
    ) -> None:
        '''(experimental) Properties for a Firewall Rule Group Association.

        :param priority: (experimental) The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. This value must be greater than 100 and less than 9,000
        :param vpc: (experimental) The VPC that to associate with the rule group.
        :param mutation_protection: (experimental) If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. Default: true
        :param name: (experimental) The name of the association. Default: - a CloudFormation generated name
        :param firewall_rule_group: (experimental) The firewall rule group which must be associated.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "priority": priority,
            "vpc": vpc,
            "firewall_rule_group": firewall_rule_group,
        }
        if mutation_protection is not None:
            self._values["mutation_protection"] = mutation_protection
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def priority(self) -> jsii.Number:
        '''(experimental) The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC.

        DNS Firewall filters VPC
        traffic starting from rule group with the lowest numeric priority setting.

        This value must be greater than 100 and less than 9,000

        :stability: experimental
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(experimental) The VPC that to associate with the rule group.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    @builtins.property
    def mutation_protection(self) -> typing.Optional[builtins.bool]:
        '''(experimental) If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("mutation_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the association.

        :default: - a CloudFormation generated name

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firewall_rule_group(self) -> "IFirewallRuleGroup":
        '''(experimental) The firewall rule group which must be associated.

        :stability: experimental
        '''
        result = self._values.get("firewall_rule_group")
        assert result is not None, "Required property 'firewall_rule_group' is missing"
        return typing.cast("IFirewallRuleGroup", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRuleGroupAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-route53resolver.FirewallRuleGroupProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "rules": "rules"},
)
class FirewallRuleGroupProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Sequence[FirewallRule]] = None,
    ) -> None:
        '''(experimental) Properties for a Firewall Rule Group.

        :param name: (experimental) The name of the rule group. Default: - a CloudFormation generated name
        :param rules: (experimental) A list of rules for this group. Default: - no rules

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the rule group.

        :default: - a CloudFormation generated name

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[FirewallRule]]:
        '''(experimental) A list of rules for this group.

        :default: - no rules

        :stability: experimental
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[FirewallRule]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRuleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-route53resolver.IFirewallDomainList")
class IFirewallDomainList(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''(experimental) A Firewall Domain List.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListId")
    def firewall_domain_list_id(self) -> builtins.str:
        '''(experimental) The ID of the domain list.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IFirewallDomainListProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''(experimental) A Firewall Domain List.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-route53resolver.IFirewallDomainList"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListId")
    def firewall_domain_list_id(self) -> builtins.str:
        '''(experimental) The ID of the domain list.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallDomainList).__jsii_proxy_class__ = lambda : _IFirewallDomainListProxy


@jsii.interface(jsii_type="@aws-cdk/aws-route53resolver.IFirewallRuleGroup")
class IFirewallRuleGroup(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''(experimental) A Firewall Rule Group.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> builtins.str:
        '''(experimental) The ID of the rule group.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IFirewallRuleGroupProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''(experimental) A Firewall Rule Group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-route53resolver.IFirewallRuleGroup"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> builtins.str:
        '''(experimental) The ID of the rule group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallRuleGroup).__jsii_proxy_class__ = lambda : _IFirewallRuleGroupProxy


@jsii.implements(IFirewallDomainList)
class FirewallDomainList(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.FirewallDomainList",
):
    '''(experimental) A Firewall Domain List.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        domains: FirewallDomains,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domains: (experimental) A list of domains.
        :param name: (experimental) A name for the domain list. Default: - a CloudFormation generated name

        :stability: experimental
        '''
        props = FirewallDomainListProps(domains=domains, name=name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromFirewallDomainListId") # type: ignore[misc]
    @builtins.classmethod
    def from_firewall_domain_list_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        firewall_domain_list_id: builtins.str,
    ) -> IFirewallDomainList:
        '''(experimental) Import an existing Firewall Rule Group.

        :param scope: -
        :param id: -
        :param firewall_domain_list_id: -

        :stability: experimental
        '''
        return typing.cast(IFirewallDomainList, jsii.sinvoke(cls, "fromFirewallDomainListId", [scope, id, firewall_domain_list_id]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListArn")
    def firewall_domain_list_arn(self) -> builtins.str:
        '''(experimental) The ARN (Amazon Resource Name) of the domain list.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListCreationTime")
    def firewall_domain_list_creation_time(self) -> builtins.str:
        '''(experimental) The date and time that the domain list was created.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListCreatorRequestId")
    def firewall_domain_list_creator_request_id(self) -> builtins.str:
        '''(experimental) The creator request ID.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListCreatorRequestId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListDomainCount")
    def firewall_domain_list_domain_count(self) -> jsii.Number:
        '''(experimental) The number of domains in the list.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(jsii.Number, jsii.get(self, "firewallDomainListDomainCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListId")
    def firewall_domain_list_id(self) -> builtins.str:
        '''(experimental) The ID of the domain list.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListManagedOwnerName")
    def firewall_domain_list_managed_owner_name(self) -> builtins.str:
        '''(experimental) The owner of the list, used only for lists that are not managed by you.

        For example, the managed domain list ``AWSManagedDomainsMalwareDomainList``
        has the managed owner name ``Route 53 Resolver DNS Firewall``.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListManagedOwnerName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListModificationTime")
    def firewall_domain_list_modification_time(self) -> builtins.str:
        '''(experimental) The date and time that the domain list was last modified.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListModificationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListStatus")
    def firewall_domain_list_status(self) -> builtins.str:
        '''(experimental) The status of the domain list.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallDomainListStatusMessage")
    def firewall_domain_list_status_message(self) -> builtins.str:
        '''(experimental) Additional information about the status of the rule group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallDomainListStatusMessage"))


@jsii.implements(IFirewallRuleGroup)
class FirewallRuleGroup(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-route53resolver.FirewallRuleGroup",
):
    '''(experimental) A Firewall Rule Group.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Sequence[FirewallRule]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param name: (experimental) The name of the rule group. Default: - a CloudFormation generated name
        :param rules: (experimental) A list of rules for this group. Default: - no rules

        :stability: experimental
        '''
        props = FirewallRuleGroupProps(name=name, rules=rules)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromFirewallRuleGroupId") # type: ignore[misc]
    @builtins.classmethod
    def from_firewall_rule_group_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        firewall_rule_group_id: builtins.str,
    ) -> IFirewallRuleGroup:
        '''(experimental) Import an existing Firewall Rule Group.

        :param scope: -
        :param id: -
        :param firewall_rule_group_id: -

        :stability: experimental
        '''
        return typing.cast(IFirewallRuleGroup, jsii.sinvoke(cls, "fromFirewallRuleGroupId", [scope, id, firewall_rule_group_id]))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        *,
        action: FirewallRuleAction,
        firewall_domain_list: IFirewallDomainList,
        priority: jsii.Number,
    ) -> "FirewallRuleGroup":
        '''(experimental) Adds a rule to this group.

        :param action: (experimental) The action for this rule.
        :param firewall_domain_list: (experimental) The domain list for this rule.
        :param priority: (experimental) The priority of the rule in the rule group. This value must be unique within the rule group.

        :stability: experimental
        '''
        rule = FirewallRule(
            action=action, firewall_domain_list=firewall_domain_list, priority=priority
        )

        return typing.cast("FirewallRuleGroup", jsii.invoke(self, "addRule", [rule]))

    @jsii.member(jsii_name="associate")
    def associate(
        self,
        id: builtins.str,
        *,
        priority: jsii.Number,
        vpc: aws_cdk.aws_ec2.IVpc,
        mutation_protection: typing.Optional[builtins.bool] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> FirewallRuleGroupAssociation:
        '''(experimental) Associates this Firewall Rule Group with a VPC.

        :param id: -
        :param priority: (experimental) The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. This value must be greater than 100 and less than 9,000
        :param vpc: (experimental) The VPC that to associate with the rule group.
        :param mutation_protection: (experimental) If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. Default: true
        :param name: (experimental) The name of the association. Default: - a CloudFormation generated name

        :stability: experimental
        '''
        props = FirewallRuleGroupAssociationOptions(
            priority=priority,
            vpc=vpc,
            mutation_protection=mutation_protection,
            name=name,
        )

        return typing.cast(FirewallRuleGroupAssociation, jsii.invoke(self, "associate", [id, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupArn")
    def firewall_rule_group_arn(self) -> builtins.str:
        '''(experimental) The ARN (Amazon Resource Name) of the rule group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupCreationTime")
    def firewall_rule_group_creation_time(self) -> builtins.str:
        '''(experimental) The date and time that the rule group was created.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupCreatorRequestId")
    def firewall_rule_group_creator_request_id(self) -> builtins.str:
        '''(experimental) The creator request ID.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupCreatorRequestId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupId")
    def firewall_rule_group_id(self) -> builtins.str:
        '''(experimental) The ID of the rule group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupModificationTime")
    def firewall_rule_group_modification_time(self) -> builtins.str:
        '''(experimental) The date and time that the rule group was last modified.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupModificationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupOwnerId")
    def firewall_rule_group_owner_id(self) -> builtins.str:
        '''(experimental) The AWS account ID for the account that created the rule group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupOwnerId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupRuleCount")
    def firewall_rule_group_rule_count(self) -> jsii.Number:
        '''(experimental) The number of rules in the rule group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(jsii.Number, jsii.get(self, "firewallRuleGroupRuleCount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupShareStatus")
    def firewall_rule_group_share_status(self) -> builtins.str:
        '''(experimental) Whether the rule group is shared with other AWS accounts, or was shared with the current account by another AWS account.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupShareStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupStatus")
    def firewall_rule_group_status(self) -> builtins.str:
        '''(experimental) The status of the rule group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firewallRuleGroupStatusMessage")
    def firewall_rule_group_status_message(self) -> builtins.str:
        '''(experimental) Additional information about the status of the rule group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "firewallRuleGroupStatusMessage"))


__all__ = [
    "CfnFirewallDomainList",
    "CfnFirewallDomainListProps",
    "CfnFirewallRuleGroup",
    "CfnFirewallRuleGroupAssociation",
    "CfnFirewallRuleGroupAssociationProps",
    "CfnFirewallRuleGroupProps",
    "CfnResolverDNSSECConfig",
    "CfnResolverDNSSECConfigProps",
    "CfnResolverEndpoint",
    "CfnResolverEndpointProps",
    "CfnResolverQueryLoggingConfig",
    "CfnResolverQueryLoggingConfigAssociation",
    "CfnResolverQueryLoggingConfigAssociationProps",
    "CfnResolverQueryLoggingConfigProps",
    "CfnResolverRule",
    "CfnResolverRuleAssociation",
    "CfnResolverRuleAssociationProps",
    "CfnResolverRuleProps",
    "DnsBlockResponse",
    "DomainsConfig",
    "FirewallDomainList",
    "FirewallDomainListProps",
    "FirewallDomains",
    "FirewallRule",
    "FirewallRuleAction",
    "FirewallRuleGroup",
    "FirewallRuleGroupAssociation",
    "FirewallRuleGroupAssociationOptions",
    "FirewallRuleGroupAssociationProps",
    "FirewallRuleGroupProps",
    "IFirewallDomainList",
    "IFirewallRuleGroup",
]

publication.publish()
