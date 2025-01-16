import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_app_python_example.cdk_app_stack import CdkAppStack


# example tests. To run these tests, uncomment this file along with the example
# resource in

# Test if the cdk_app/cdk_app_stack.py stack creates the log group with the expected properties
def test_log_group_created():
    app = core.App()
    stack = CdkAppStack(app, "cdk-app")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::Logs::LogGroup", 1)

    template.has_resource_properties("AWS::Logs::LogGroup", {
        "RetentionInDays": 1
    })
