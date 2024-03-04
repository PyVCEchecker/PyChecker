'''
# AWS::Detective Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_detective as detective
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
class CfnGraph(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-detective.CfnGraph",
):
    '''A CloudFormation ``AWS::Detective::Graph``.

    :cloudformationResource: AWS::Detective::Graph
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Detective::Graph``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param tags: ``AWS::Detective::Graph.Tags``.
        '''
        props = CfnGraphProps(tags=tags)

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
        '''``AWS::Detective::Graph.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html#cfn-detective-graph-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-detective.CfnGraphProps",
    jsii_struct_bases=[],
    name_mapping={"tags": "tags"},
)
class CfnGraphProps:
    def __init__(
        self,
        *,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Detective::Graph``.

        :param tags: ``AWS::Detective::Graph.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Detective::Graph.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html#cfn-detective-graph-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMemberInvitation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-detective.CfnMemberInvitation",
):
    '''A CloudFormation ``AWS::Detective::MemberInvitation``.

    :cloudformationResource: AWS::Detective::MemberInvitation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        graph_arn: builtins.str,
        member_email_address: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Detective::MemberInvitation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param graph_arn: ``AWS::Detective::MemberInvitation.GraphArn``.
        :param member_email_address: ``AWS::Detective::MemberInvitation.MemberEmailAddress``.
        :param member_id: ``AWS::Detective::MemberInvitation.MemberId``.
        :param disable_email_notification: ``AWS::Detective::MemberInvitation.DisableEmailNotification``.
        :param message: ``AWS::Detective::MemberInvitation.Message``.
        '''
        props = CfnMemberInvitationProps(
            graph_arn=graph_arn,
            member_email_address=member_email_address,
            member_id=member_id,
            disable_email_notification=disable_email_notification,
            message=message,
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
    @jsii.member(jsii_name="graphArn")
    def graph_arn(self) -> builtins.str:
        '''``AWS::Detective::MemberInvitation.GraphArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-grapharn
        '''
        return typing.cast(builtins.str, jsii.get(self, "graphArn"))

    @graph_arn.setter
    def graph_arn(self, value: builtins.str) -> None:
        jsii.set(self, "graphArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memberEmailAddress")
    def member_email_address(self) -> builtins.str:
        '''``AWS::Detective::MemberInvitation.MemberEmailAddress``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberemailaddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "memberEmailAddress"))

    @member_email_address.setter
    def member_email_address(self, value: builtins.str) -> None:
        jsii.set(self, "memberEmailAddress", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> builtins.str:
        '''``AWS::Detective::MemberInvitation.MemberId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberid
        '''
        return typing.cast(builtins.str, jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(self, value: builtins.str) -> None:
        jsii.set(self, "memberId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="disableEmailNotification")
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Detective::MemberInvitation.DisableEmailNotification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-disableemailnotification
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "disableEmailNotification"))

    @disable_email_notification.setter
    def disable_email_notification(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "disableEmailNotification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Optional[builtins.str]:
        '''``AWS::Detective::MemberInvitation.Message``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-message
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "message"))

    @message.setter
    def message(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "message", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-detective.CfnMemberInvitationProps",
    jsii_struct_bases=[],
    name_mapping={
        "graph_arn": "graphArn",
        "member_email_address": "memberEmailAddress",
        "member_id": "memberId",
        "disable_email_notification": "disableEmailNotification",
        "message": "message",
    },
)
class CfnMemberInvitationProps:
    def __init__(
        self,
        *,
        graph_arn: builtins.str,
        member_email_address: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Detective::MemberInvitation``.

        :param graph_arn: ``AWS::Detective::MemberInvitation.GraphArn``.
        :param member_email_address: ``AWS::Detective::MemberInvitation.MemberEmailAddress``.
        :param member_id: ``AWS::Detective::MemberInvitation.MemberId``.
        :param disable_email_notification: ``AWS::Detective::MemberInvitation.DisableEmailNotification``.
        :param message: ``AWS::Detective::MemberInvitation.Message``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "graph_arn": graph_arn,
            "member_email_address": member_email_address,
            "member_id": member_id,
        }
        if disable_email_notification is not None:
            self._values["disable_email_notification"] = disable_email_notification
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def graph_arn(self) -> builtins.str:
        '''``AWS::Detective::MemberInvitation.GraphArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-grapharn
        '''
        result = self._values.get("graph_arn")
        assert result is not None, "Required property 'graph_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_email_address(self) -> builtins.str:
        '''``AWS::Detective::MemberInvitation.MemberEmailAddress``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberemailaddress
        '''
        result = self._values.get("member_email_address")
        assert result is not None, "Required property 'member_email_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(self) -> builtins.str:
        '''``AWS::Detective::MemberInvitation.MemberId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Detective::MemberInvitation.DisableEmailNotification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-disableemailnotification
        '''
        result = self._values.get("disable_email_notification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''``AWS::Detective::MemberInvitation.Message``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemberInvitationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGraph",
    "CfnGraphProps",
    "CfnMemberInvitation",
    "CfnMemberInvitationProps",
]

publication.publish()
