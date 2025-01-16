#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_app.cdk_app_stack import CdkAppStack

# `app` is the CDK application
app = cdk.App()

# Get the target region from the context
region = app.node.try_get_context("region") or "eu-west-1"

# Create the main environment
env = cdk.Environment(region=region)

# Create a new "CDK App" stack
CdkAppStack(app, "CdkAppStack", env=env)

# Synthesize the CloudFormation template
app.synth()
