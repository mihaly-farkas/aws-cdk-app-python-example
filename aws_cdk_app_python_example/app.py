#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_app_python_example.stacks.log_group_stack import LogGroupStack

# `app` is the CDK application
app = cdk.App()

# Get the target region from the context
region = app.node.try_get_context("region") or "eu-west-1"

# Create the main environment
env = cdk.Environment(region=region)

# Create a new "Log Group" stack
LogGroupStack(app, "LogGroup", env=env)

# Synthesize the CloudFormation template
app.synth()
