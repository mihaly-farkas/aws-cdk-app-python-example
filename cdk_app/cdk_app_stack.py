from aws_cdk import (
    Stack,
    aws_logs,
)
from constructs import Construct


# An AWS CDK stack that creates a CloudWatch Log Group
class CdkAppStack(Stack):

    # Init method for the stack
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # This is just a simple example of creating an AWS CDK construct.
        aws_logs.LogGroup(
            self, "LogGroup",
            retention=aws_logs.RetentionDays.ONE_DAY,
        )
