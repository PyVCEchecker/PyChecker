# Actions for AWS Elastic Load Balancing V2

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This package contains integration actions for ELBv2. See the README of the `@aws-cdk/aws-elasticloadbalancingv2` library.

## Cognito

ELB allows for requests to be authenticated against a Cognito user pool using
the `AuthenticateCognitoAction`. For details on the setup's requirements,
read [Prepare to use Amazon
Cognito](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html#cognito-requirements).
Here's an example:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_cognito as cognito
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_elasticloadbalancingv2 as elbv2
from aws_cdk.core import App, CfnOutput, Stack
from constructs import Construct
import ...lib as actions

Stack):

lb = elbv2.ApplicationLoadBalancer(self, "LB",
    vpc=vpc,
    internet_facing=True
)

user_pool = cognito.UserPool(self, "UserPool")
user_pool_client = cognito.UserPoolClient(self, "Client",
    user_pool=user_pool,

    # Required minimal configuration for use with an ELB
    generate_secret=True,
    auth_flows=AuthFlow(
        user_password=True
    ),
    o_auth=OAuthSettings(
        flows=OAuthFlows(
            authorization_code_grant=True
        ),
        scopes=[cognito.OAuthScope.EMAIL],
        callback_urls=[f"https://{lb.loadBalancerDnsName}/oauth2/idpresponse"
        ]
    )
)
cfn_client = user_pool_client.node.default_child
cfn_client.add_property_override("RefreshTokenValidity", 1)
cfn_client.add_property_override("SupportedIdentityProviders", ["COGNITO"])

user_pool_domain = cognito.UserPoolDomain(self, "Domain",
    user_pool=user_pool,
    cognito_domain=CognitoDomainOptions(
        domain_prefix="test-cdk-prefix"
    )
)

lb.add_listener("Listener",
    port=443,
    certificates=[certificate],
    default_action=actions.AuthenticateCognitoAction(
        user_pool=user_pool,
        user_pool_client=user_pool_client,
        user_pool_domain=user_pool_domain,
        next=elbv2.ListenerAction.fixed_response(200,
            content_type="text/plain",
            message_body="Authenticated"
        )
    )
)

CfnOutput(self, "DNS",
    value=lb.load_balancer_dns_name
)

app = App()
CognitoStack(app, "integ-cognito")
app.synth()
```

> NOTE: this example seems incomplete, I was not able to get the redirect back to the
> Load Balancer after authentication working. Would love some pointers on what a full working
> setup actually looks like!
