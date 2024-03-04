'''
# AWS Budgets Construct Library

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
class CfnBudget(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-budgets.CfnBudget",
):
    '''A CloudFormation ``AWS::Budgets::Budget``.

    :cloudformationResource: AWS::Budgets::Budget
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        budget: typing.Union["CfnBudget.BudgetDataProperty", aws_cdk.core.IResolvable],
        notifications_with_subscribers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.NotificationWithSubscribersProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Budgets::Budget``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param budget: ``AWS::Budgets::Budget.Budget``.
        :param notifications_with_subscribers: ``AWS::Budgets::Budget.NotificationsWithSubscribers``.
        '''
        props = CfnBudgetProps(
            budget=budget,
            notifications_with_subscribers=notifications_with_subscribers,
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
    @jsii.member(jsii_name="budget")
    def budget(
        self,
    ) -> typing.Union["CfnBudget.BudgetDataProperty", aws_cdk.core.IResolvable]:
        '''``AWS::Budgets::Budget.Budget``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-budget
        '''
        return typing.cast(typing.Union["CfnBudget.BudgetDataProperty", aws_cdk.core.IResolvable], jsii.get(self, "budget"))

    @budget.setter
    def budget(
        self,
        value: typing.Union["CfnBudget.BudgetDataProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "budget", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationsWithSubscribers")
    def notifications_with_subscribers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.NotificationWithSubscribersProperty"]]]]:
        '''``AWS::Budgets::Budget.NotificationsWithSubscribers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-notificationswithsubscribers
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.NotificationWithSubscribersProperty"]]]], jsii.get(self, "notificationsWithSubscribers"))

    @notifications_with_subscribers.setter
    def notifications_with_subscribers(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.NotificationWithSubscribersProperty"]]]],
    ) -> None:
        jsii.set(self, "notificationsWithSubscribers", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudget.BudgetDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "budget_type": "budgetType",
            "time_unit": "timeUnit",
            "budget_limit": "budgetLimit",
            "budget_name": "budgetName",
            "cost_filters": "costFilters",
            "cost_types": "costTypes",
            "planned_budget_limits": "plannedBudgetLimits",
            "time_period": "timePeriod",
        },
    )
    class BudgetDataProperty:
        def __init__(
            self,
            *,
            budget_type: builtins.str,
            time_unit: builtins.str,
            budget_limit: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.SpendProperty"]] = None,
            budget_name: typing.Optional[builtins.str] = None,
            cost_filters: typing.Any = None,
            cost_types: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.CostTypesProperty"]] = None,
            planned_budget_limits: typing.Any = None,
            time_period: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.TimePeriodProperty"]] = None,
        ) -> None:
            '''
            :param budget_type: ``CfnBudget.BudgetDataProperty.BudgetType``.
            :param time_unit: ``CfnBudget.BudgetDataProperty.TimeUnit``.
            :param budget_limit: ``CfnBudget.BudgetDataProperty.BudgetLimit``.
            :param budget_name: ``CfnBudget.BudgetDataProperty.BudgetName``.
            :param cost_filters: ``CfnBudget.BudgetDataProperty.CostFilters``.
            :param cost_types: ``CfnBudget.BudgetDataProperty.CostTypes``.
            :param planned_budget_limits: ``CfnBudget.BudgetDataProperty.PlannedBudgetLimits``.
            :param time_period: ``CfnBudget.BudgetDataProperty.TimePeriod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "budget_type": budget_type,
                "time_unit": time_unit,
            }
            if budget_limit is not None:
                self._values["budget_limit"] = budget_limit
            if budget_name is not None:
                self._values["budget_name"] = budget_name
            if cost_filters is not None:
                self._values["cost_filters"] = cost_filters
            if cost_types is not None:
                self._values["cost_types"] = cost_types
            if planned_budget_limits is not None:
                self._values["planned_budget_limits"] = planned_budget_limits
            if time_period is not None:
                self._values["time_period"] = time_period

        @builtins.property
        def budget_type(self) -> builtins.str:
            '''``CfnBudget.BudgetDataProperty.BudgetType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgettype
            '''
            result = self._values.get("budget_type")
            assert result is not None, "Required property 'budget_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_unit(self) -> builtins.str:
            '''``CfnBudget.BudgetDataProperty.TimeUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeunit
            '''
            result = self._values.get("time_unit")
            assert result is not None, "Required property 'time_unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def budget_limit(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.SpendProperty"]]:
            '''``CfnBudget.BudgetDataProperty.BudgetLimit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetlimit
            '''
            result = self._values.get("budget_limit")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.SpendProperty"]], result)

        @builtins.property
        def budget_name(self) -> typing.Optional[builtins.str]:
            '''``CfnBudget.BudgetDataProperty.BudgetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetname
            '''
            result = self._values.get("budget_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cost_filters(self) -> typing.Any:
            '''``CfnBudget.BudgetDataProperty.CostFilters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costfilters
            '''
            result = self._values.get("cost_filters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def cost_types(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.CostTypesProperty"]]:
            '''``CfnBudget.BudgetDataProperty.CostTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costtypes
            '''
            result = self._values.get("cost_types")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.CostTypesProperty"]], result)

        @builtins.property
        def planned_budget_limits(self) -> typing.Any:
            '''``CfnBudget.BudgetDataProperty.PlannedBudgetLimits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-plannedbudgetlimits
            '''
            result = self._values.get("planned_budget_limits")
            return typing.cast(typing.Any, result)

        @builtins.property
        def time_period(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.TimePeriodProperty"]]:
            '''``CfnBudget.BudgetDataProperty.TimePeriod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeperiod
            '''
            result = self._values.get("time_period")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.TimePeriodProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BudgetDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudget.CostTypesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "include_credit": "includeCredit",
            "include_discount": "includeDiscount",
            "include_other_subscription": "includeOtherSubscription",
            "include_recurring": "includeRecurring",
            "include_refund": "includeRefund",
            "include_subscription": "includeSubscription",
            "include_support": "includeSupport",
            "include_tax": "includeTax",
            "include_upfront": "includeUpfront",
            "use_amortized": "useAmortized",
            "use_blended": "useBlended",
        },
    )
    class CostTypesProperty:
        def __init__(
            self,
            *,
            include_credit: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_discount: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_other_subscription: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_recurring: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_refund: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_subscription: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_support: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_tax: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            include_upfront: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            use_amortized: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            use_blended: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param include_credit: ``CfnBudget.CostTypesProperty.IncludeCredit``.
            :param include_discount: ``CfnBudget.CostTypesProperty.IncludeDiscount``.
            :param include_other_subscription: ``CfnBudget.CostTypesProperty.IncludeOtherSubscription``.
            :param include_recurring: ``CfnBudget.CostTypesProperty.IncludeRecurring``.
            :param include_refund: ``CfnBudget.CostTypesProperty.IncludeRefund``.
            :param include_subscription: ``CfnBudget.CostTypesProperty.IncludeSubscription``.
            :param include_support: ``CfnBudget.CostTypesProperty.IncludeSupport``.
            :param include_tax: ``CfnBudget.CostTypesProperty.IncludeTax``.
            :param include_upfront: ``CfnBudget.CostTypesProperty.IncludeUpfront``.
            :param use_amortized: ``CfnBudget.CostTypesProperty.UseAmortized``.
            :param use_blended: ``CfnBudget.CostTypesProperty.UseBlended``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if include_credit is not None:
                self._values["include_credit"] = include_credit
            if include_discount is not None:
                self._values["include_discount"] = include_discount
            if include_other_subscription is not None:
                self._values["include_other_subscription"] = include_other_subscription
            if include_recurring is not None:
                self._values["include_recurring"] = include_recurring
            if include_refund is not None:
                self._values["include_refund"] = include_refund
            if include_subscription is not None:
                self._values["include_subscription"] = include_subscription
            if include_support is not None:
                self._values["include_support"] = include_support
            if include_tax is not None:
                self._values["include_tax"] = include_tax
            if include_upfront is not None:
                self._values["include_upfront"] = include_upfront
            if use_amortized is not None:
                self._values["use_amortized"] = use_amortized
            if use_blended is not None:
                self._values["use_blended"] = use_blended

        @builtins.property
        def include_credit(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeCredit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includecredit
            '''
            result = self._values.get("include_credit")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_discount(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeDiscount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includediscount
            '''
            result = self._values.get("include_discount")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_other_subscription(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeOtherSubscription``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeothersubscription
            '''
            result = self._values.get("include_other_subscription")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_recurring(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeRecurring``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerecurring
            '''
            result = self._values.get("include_recurring")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_refund(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeRefund``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerefund
            '''
            result = self._values.get("include_refund")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_subscription(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeSubscription``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesubscription
            '''
            result = self._values.get("include_subscription")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_support(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeSupport``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesupport
            '''
            result = self._values.get("include_support")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_tax(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeTax``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includetax
            '''
            result = self._values.get("include_tax")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def include_upfront(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.IncludeUpfront``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeupfront
            '''
            result = self._values.get("include_upfront")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def use_amortized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.UseAmortized``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useamortized
            '''
            result = self._values.get("use_amortized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def use_blended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnBudget.CostTypesProperty.UseBlended``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useblended
            '''
            result = self._values.get("use_blended")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CostTypesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudget.NotificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "notification_type": "notificationType",
            "threshold": "threshold",
            "threshold_type": "thresholdType",
        },
    )
    class NotificationProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            notification_type: builtins.str,
            threshold: jsii.Number,
            threshold_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param comparison_operator: ``CfnBudget.NotificationProperty.ComparisonOperator``.
            :param notification_type: ``CfnBudget.NotificationProperty.NotificationType``.
            :param threshold: ``CfnBudget.NotificationProperty.Threshold``.
            :param threshold_type: ``CfnBudget.NotificationProperty.ThresholdType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "notification_type": notification_type,
                "threshold": threshold,
            }
            if threshold_type is not None:
                self._values["threshold_type"] = threshold_type

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''``CfnBudget.NotificationProperty.ComparisonOperator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def notification_type(self) -> builtins.str:
            '''``CfnBudget.NotificationProperty.NotificationType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-notificationtype
            '''
            result = self._values.get("notification_type")
            assert result is not None, "Required property 'notification_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''``CfnBudget.NotificationProperty.Threshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def threshold_type(self) -> typing.Optional[builtins.str]:
            '''``CfnBudget.NotificationProperty.ThresholdType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-thresholdtype
            '''
            result = self._values.get("threshold_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudget.NotificationWithSubscribersProperty",
        jsii_struct_bases=[],
        name_mapping={"notification": "notification", "subscribers": "subscribers"},
    )
    class NotificationWithSubscribersProperty:
        def __init__(
            self,
            *,
            notification: typing.Union[aws_cdk.core.IResolvable, "CfnBudget.NotificationProperty"],
            subscribers: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.SubscriberProperty"]]],
        ) -> None:
            '''
            :param notification: ``CfnBudget.NotificationWithSubscribersProperty.Notification``.
            :param subscribers: ``CfnBudget.NotificationWithSubscribersProperty.Subscribers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "notification": notification,
                "subscribers": subscribers,
            }

        @builtins.property
        def notification(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnBudget.NotificationProperty"]:
            '''``CfnBudget.NotificationWithSubscribersProperty.Notification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-notification
            '''
            result = self._values.get("notification")
            assert result is not None, "Required property 'notification' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnBudget.NotificationProperty"], result)

        @builtins.property
        def subscribers(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.SubscriberProperty"]]]:
            '''``CfnBudget.NotificationWithSubscribersProperty.Subscribers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-subscribers
            '''
            result = self._values.get("subscribers")
            assert result is not None, "Required property 'subscribers' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBudget.SubscriberProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationWithSubscribersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudget.SpendProperty",
        jsii_struct_bases=[],
        name_mapping={"amount": "amount", "unit": "unit"},
    )
    class SpendProperty:
        def __init__(self, *, amount: jsii.Number, unit: builtins.str) -> None:
            '''
            :param amount: ``CfnBudget.SpendProperty.Amount``.
            :param unit: ``CfnBudget.SpendProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "amount": amount,
                "unit": unit,
            }

        @builtins.property
        def amount(self) -> jsii.Number:
            '''``CfnBudget.SpendProperty.Amount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-amount
            '''
            result = self._values.get("amount")
            assert result is not None, "Required property 'amount' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unit(self) -> builtins.str:
            '''``CfnBudget.SpendProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpendProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudget.SubscriberProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "subscription_type": "subscriptionType"},
    )
    class SubscriberProperty:
        def __init__(
            self,
            *,
            address: builtins.str,
            subscription_type: builtins.str,
        ) -> None:
            '''
            :param address: ``CfnBudget.SubscriberProperty.Address``.
            :param subscription_type: ``CfnBudget.SubscriberProperty.SubscriptionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "address": address,
                "subscription_type": subscription_type,
            }

        @builtins.property
        def address(self) -> builtins.str:
            '''``CfnBudget.SubscriberProperty.Address``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-address
            '''
            result = self._values.get("address")
            assert result is not None, "Required property 'address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subscription_type(self) -> builtins.str:
            '''``CfnBudget.SubscriberProperty.SubscriptionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-subscriptiontype
            '''
            result = self._values.get("subscription_type")
            assert result is not None, "Required property 'subscription_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudget.TimePeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class TimePeriodProperty:
        def __init__(
            self,
            *,
            end: typing.Optional[builtins.str] = None,
            start: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param end: ``CfnBudget.TimePeriodProperty.End``.
            :param start: ``CfnBudget.TimePeriodProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if end is not None:
                self._values["end"] = end
            if start is not None:
                self._values["start"] = start

        @builtins.property
        def end(self) -> typing.Optional[builtins.str]:
            '''``CfnBudget.TimePeriodProperty.End``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-end
            '''
            result = self._values.get("end")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start(self) -> typing.Optional[builtins.str]:
            '''``CfnBudget.TimePeriodProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-start
            '''
            result = self._values.get("start")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimePeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-budgets.CfnBudgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "budget": "budget",
        "notifications_with_subscribers": "notificationsWithSubscribers",
    },
)
class CfnBudgetProps:
    def __init__(
        self,
        *,
        budget: typing.Union[CfnBudget.BudgetDataProperty, aws_cdk.core.IResolvable],
        notifications_with_subscribers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnBudget.NotificationWithSubscribersProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Budgets::Budget``.

        :param budget: ``AWS::Budgets::Budget.Budget``.
        :param notifications_with_subscribers: ``AWS::Budgets::Budget.NotificationsWithSubscribers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "budget": budget,
        }
        if notifications_with_subscribers is not None:
            self._values["notifications_with_subscribers"] = notifications_with_subscribers

    @builtins.property
    def budget(
        self,
    ) -> typing.Union[CfnBudget.BudgetDataProperty, aws_cdk.core.IResolvable]:
        '''``AWS::Budgets::Budget.Budget``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-budget
        '''
        result = self._values.get("budget")
        assert result is not None, "Required property 'budget' is missing"
        return typing.cast(typing.Union[CfnBudget.BudgetDataProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def notifications_with_subscribers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnBudget.NotificationWithSubscribersProperty]]]]:
        '''``AWS::Budgets::Budget.NotificationsWithSubscribers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-notificationswithsubscribers
        '''
        result = self._values.get("notifications_with_subscribers")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnBudget.NotificationWithSubscribersProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBudgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnBudgetsAction(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-budgets.CfnBudgetsAction",
):
    '''A CloudFormation ``AWS::Budgets::BudgetsAction``.

    :cloudformationResource: AWS::Budgets::BudgetsAction
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        action_threshold: typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.ActionThresholdProperty"],
        action_type: builtins.str,
        budget_name: builtins.str,
        definition: typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.DefinitionProperty"],
        execution_role_arn: builtins.str,
        notification_type: builtins.str,
        approval_model: typing.Optional[builtins.str] = None,
        subscribers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.SubscriberProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Budgets::BudgetsAction``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action_threshold: ``AWS::Budgets::BudgetsAction.ActionThreshold``.
        :param action_type: ``AWS::Budgets::BudgetsAction.ActionType``.
        :param budget_name: ``AWS::Budgets::BudgetsAction.BudgetName``.
        :param definition: ``AWS::Budgets::BudgetsAction.Definition``.
        :param execution_role_arn: ``AWS::Budgets::BudgetsAction.ExecutionRoleArn``.
        :param notification_type: ``AWS::Budgets::BudgetsAction.NotificationType``.
        :param approval_model: ``AWS::Budgets::BudgetsAction.ApprovalModel``.
        :param subscribers: ``AWS::Budgets::BudgetsAction.Subscribers``.
        '''
        props = CfnBudgetsActionProps(
            action_threshold=action_threshold,
            action_type=action_type,
            budget_name=budget_name,
            definition=definition,
            execution_role_arn=execution_role_arn,
            notification_type=notification_type,
            approval_model=approval_model,
            subscribers=subscribers,
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
    @jsii.member(jsii_name="attrActionId")
    def attr_action_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ActionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrActionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="actionThreshold")
    def action_threshold(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.ActionThresholdProperty"]:
        '''``AWS::Budgets::BudgetsAction.ActionThreshold``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actionthreshold
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.ActionThresholdProperty"], jsii.get(self, "actionThreshold"))

    @action_threshold.setter
    def action_threshold(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.ActionThresholdProperty"],
    ) -> None:
        jsii.set(self, "actionThreshold", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        '''``AWS::Budgets::BudgetsAction.ActionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actiontype
        '''
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        jsii.set(self, "actionType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="budgetName")
    def budget_name(self) -> builtins.str:
        '''``AWS::Budgets::BudgetsAction.BudgetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-budgetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "budgetName"))

    @budget_name.setter
    def budget_name(self, value: builtins.str) -> None:
        jsii.set(self, "budgetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="definition")
    def definition(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.DefinitionProperty"]:
        '''``AWS::Budgets::BudgetsAction.Definition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-definition
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.DefinitionProperty"], jsii.get(self, "definition"))

    @definition.setter
    def definition(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.DefinitionProperty"],
    ) -> None:
        jsii.set(self, "definition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        '''``AWS::Budgets::BudgetsAction.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-executionrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationType")
    def notification_type(self) -> builtins.str:
        '''``AWS::Budgets::BudgetsAction.NotificationType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-notificationtype
        '''
        return typing.cast(builtins.str, jsii.get(self, "notificationType"))

    @notification_type.setter
    def notification_type(self, value: builtins.str) -> None:
        jsii.set(self, "notificationType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="approvalModel")
    def approval_model(self) -> typing.Optional[builtins.str]:
        '''``AWS::Budgets::BudgetsAction.ApprovalModel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-approvalmodel
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approvalModel"))

    @approval_model.setter
    def approval_model(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "approvalModel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subscribers")
    def subscribers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.SubscriberProperty"]]]]:
        '''``AWS::Budgets::BudgetsAction.Subscribers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-subscribers
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.SubscriberProperty"]]]], jsii.get(self, "subscribers"))

    @subscribers.setter
    def subscribers(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.SubscriberProperty"]]]],
    ) -> None:
        jsii.set(self, "subscribers", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudgetsAction.ActionThresholdProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class ActionThresholdProperty:
        def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
            '''
            :param type: ``CfnBudgetsAction.ActionThresholdProperty.Type``.
            :param value: ``CfnBudgetsAction.ActionThresholdProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnBudgetsAction.ActionThresholdProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''``CfnBudgetsAction.ActionThresholdProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionThresholdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudgetsAction.DefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iam_action_definition": "iamActionDefinition",
            "scp_action_definition": "scpActionDefinition",
            "ssm_action_definition": "ssmActionDefinition",
        },
    )
    class DefinitionProperty:
        def __init__(
            self,
            *,
            iam_action_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.IamActionDefinitionProperty"]] = None,
            scp_action_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.ScpActionDefinitionProperty"]] = None,
            ssm_action_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.SsmActionDefinitionProperty"]] = None,
        ) -> None:
            '''
            :param iam_action_definition: ``CfnBudgetsAction.DefinitionProperty.IamActionDefinition``.
            :param scp_action_definition: ``CfnBudgetsAction.DefinitionProperty.ScpActionDefinition``.
            :param ssm_action_definition: ``CfnBudgetsAction.DefinitionProperty.SsmActionDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if iam_action_definition is not None:
                self._values["iam_action_definition"] = iam_action_definition
            if scp_action_definition is not None:
                self._values["scp_action_definition"] = scp_action_definition
            if ssm_action_definition is not None:
                self._values["ssm_action_definition"] = ssm_action_definition

        @builtins.property
        def iam_action_definition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.IamActionDefinitionProperty"]]:
            '''``CfnBudgetsAction.DefinitionProperty.IamActionDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-iamactiondefinition
            '''
            result = self._values.get("iam_action_definition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.IamActionDefinitionProperty"]], result)

        @builtins.property
        def scp_action_definition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.ScpActionDefinitionProperty"]]:
            '''``CfnBudgetsAction.DefinitionProperty.ScpActionDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-scpactiondefinition
            '''
            result = self._values.get("scp_action_definition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.ScpActionDefinitionProperty"]], result)

        @builtins.property
        def ssm_action_definition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.SsmActionDefinitionProperty"]]:
            '''``CfnBudgetsAction.DefinitionProperty.SsmActionDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-ssmactiondefinition
            '''
            result = self._values.get("ssm_action_definition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnBudgetsAction.SsmActionDefinitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudgetsAction.IamActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_arn": "policyArn",
            "groups": "groups",
            "roles": "roles",
            "users": "users",
        },
    )
    class IamActionDefinitionProperty:
        def __init__(
            self,
            *,
            policy_arn: builtins.str,
            groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            roles: typing.Optional[typing.Sequence[builtins.str]] = None,
            users: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param policy_arn: ``CfnBudgetsAction.IamActionDefinitionProperty.PolicyArn``.
            :param groups: ``CfnBudgetsAction.IamActionDefinitionProperty.Groups``.
            :param roles: ``CfnBudgetsAction.IamActionDefinitionProperty.Roles``.
            :param users: ``CfnBudgetsAction.IamActionDefinitionProperty.Users``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "policy_arn": policy_arn,
            }
            if groups is not None:
                self._values["groups"] = groups
            if roles is not None:
                self._values["roles"] = roles
            if users is not None:
                self._values["users"] = users

        @builtins.property
        def policy_arn(self) -> builtins.str:
            '''``CfnBudgetsAction.IamActionDefinitionProperty.PolicyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-policyarn
            '''
            result = self._values.get("policy_arn")
            assert result is not None, "Required property 'policy_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnBudgetsAction.IamActionDefinitionProperty.Groups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-groups
            '''
            result = self._values.get("groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def roles(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnBudgetsAction.IamActionDefinitionProperty.Roles``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-roles
            '''
            result = self._values.get("roles")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def users(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnBudgetsAction.IamActionDefinitionProperty.Users``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-users
            '''
            result = self._values.get("users")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudgetsAction.ScpActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"policy_id": "policyId", "target_ids": "targetIds"},
    )
    class ScpActionDefinitionProperty:
        def __init__(
            self,
            *,
            policy_id: builtins.str,
            target_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param policy_id: ``CfnBudgetsAction.ScpActionDefinitionProperty.PolicyId``.
            :param target_ids: ``CfnBudgetsAction.ScpActionDefinitionProperty.TargetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "policy_id": policy_id,
                "target_ids": target_ids,
            }

        @builtins.property
        def policy_id(self) -> builtins.str:
            '''``CfnBudgetsAction.ScpActionDefinitionProperty.PolicyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-policyid
            '''
            result = self._values.get("policy_id")
            assert result is not None, "Required property 'policy_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_ids(self) -> typing.List[builtins.str]:
            '''``CfnBudgetsAction.ScpActionDefinitionProperty.TargetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-targetids
            '''
            result = self._values.get("target_ids")
            assert result is not None, "Required property 'target_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScpActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudgetsAction.SsmActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_ids": "instanceIds",
            "region": "region",
            "subtype": "subtype",
        },
    )
    class SsmActionDefinitionProperty:
        def __init__(
            self,
            *,
            instance_ids: typing.Sequence[builtins.str],
            region: builtins.str,
            subtype: builtins.str,
        ) -> None:
            '''
            :param instance_ids: ``CfnBudgetsAction.SsmActionDefinitionProperty.InstanceIds``.
            :param region: ``CfnBudgetsAction.SsmActionDefinitionProperty.Region``.
            :param subtype: ``CfnBudgetsAction.SsmActionDefinitionProperty.Subtype``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_ids": instance_ids,
                "region": region,
                "subtype": subtype,
            }

        @builtins.property
        def instance_ids(self) -> typing.List[builtins.str]:
            '''``CfnBudgetsAction.SsmActionDefinitionProperty.InstanceIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-instanceids
            '''
            result = self._values.get("instance_ids")
            assert result is not None, "Required property 'instance_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def region(self) -> builtins.str:
            '''``CfnBudgetsAction.SsmActionDefinitionProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subtype(self) -> builtins.str:
            '''``CfnBudgetsAction.SsmActionDefinitionProperty.Subtype``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-subtype
            '''
            result = self._values.get("subtype")
            assert result is not None, "Required property 'subtype' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsmActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-budgets.CfnBudgetsAction.SubscriberProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "type": "type"},
    )
    class SubscriberProperty:
        def __init__(self, *, address: builtins.str, type: builtins.str) -> None:
            '''
            :param address: ``CfnBudgetsAction.SubscriberProperty.Address``.
            :param type: ``CfnBudgetsAction.SubscriberProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "address": address,
                "type": type,
            }

        @builtins.property
        def address(self) -> builtins.str:
            '''``CfnBudgetsAction.SubscriberProperty.Address``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-address
            '''
            result = self._values.get("address")
            assert result is not None, "Required property 'address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnBudgetsAction.SubscriberProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-budgets.CfnBudgetsActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action_threshold": "actionThreshold",
        "action_type": "actionType",
        "budget_name": "budgetName",
        "definition": "definition",
        "execution_role_arn": "executionRoleArn",
        "notification_type": "notificationType",
        "approval_model": "approvalModel",
        "subscribers": "subscribers",
    },
)
class CfnBudgetsActionProps:
    def __init__(
        self,
        *,
        action_threshold: typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.ActionThresholdProperty],
        action_type: builtins.str,
        budget_name: builtins.str,
        definition: typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.DefinitionProperty],
        execution_role_arn: builtins.str,
        notification_type: builtins.str,
        approval_model: typing.Optional[builtins.str] = None,
        subscribers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.SubscriberProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Budgets::BudgetsAction``.

        :param action_threshold: ``AWS::Budgets::BudgetsAction.ActionThreshold``.
        :param action_type: ``AWS::Budgets::BudgetsAction.ActionType``.
        :param budget_name: ``AWS::Budgets::BudgetsAction.BudgetName``.
        :param definition: ``AWS::Budgets::BudgetsAction.Definition``.
        :param execution_role_arn: ``AWS::Budgets::BudgetsAction.ExecutionRoleArn``.
        :param notification_type: ``AWS::Budgets::BudgetsAction.NotificationType``.
        :param approval_model: ``AWS::Budgets::BudgetsAction.ApprovalModel``.
        :param subscribers: ``AWS::Budgets::BudgetsAction.Subscribers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action_threshold": action_threshold,
            "action_type": action_type,
            "budget_name": budget_name,
            "definition": definition,
            "execution_role_arn": execution_role_arn,
            "notification_type": notification_type,
        }
        if approval_model is not None:
            self._values["approval_model"] = approval_model
        if subscribers is not None:
            self._values["subscribers"] = subscribers

    @builtins.property
    def action_threshold(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.ActionThresholdProperty]:
        '''``AWS::Budgets::BudgetsAction.ActionThreshold``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actionthreshold
        '''
        result = self._values.get("action_threshold")
        assert result is not None, "Required property 'action_threshold' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.ActionThresholdProperty], result)

    @builtins.property
    def action_type(self) -> builtins.str:
        '''``AWS::Budgets::BudgetsAction.ActionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actiontype
        '''
        result = self._values.get("action_type")
        assert result is not None, "Required property 'action_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def budget_name(self) -> builtins.str:
        '''``AWS::Budgets::BudgetsAction.BudgetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-budgetname
        '''
        result = self._values.get("budget_name")
        assert result is not None, "Required property 'budget_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def definition(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.DefinitionProperty]:
        '''``AWS::Budgets::BudgetsAction.Definition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-definition
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.DefinitionProperty], result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''``AWS::Budgets::BudgetsAction.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_type(self) -> builtins.str:
        '''``AWS::Budgets::BudgetsAction.NotificationType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-notificationtype
        '''
        result = self._values.get("notification_type")
        assert result is not None, "Required property 'notification_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def approval_model(self) -> typing.Optional[builtins.str]:
        '''``AWS::Budgets::BudgetsAction.ApprovalModel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-approvalmodel
        '''
        result = self._values.get("approval_model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscribers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.SubscriberProperty]]]]:
        '''``AWS::Budgets::BudgetsAction.Subscribers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-subscribers
        '''
        result = self._values.get("subscribers")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnBudgetsAction.SubscriberProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBudgetsActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBudget",
    "CfnBudgetProps",
    "CfnBudgetsAction",
    "CfnBudgetsActionProps",
]

publication.publish()
