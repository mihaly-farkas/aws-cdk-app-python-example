#!/usr/bin/env python3
import json
from typing import Optional

import aws_cdk as cdk
from caseconverter import pascalcase, kebabcase
from constructs import Construct

from aws_cdk_app_python_example.stacks.log_group_stack import LogGroupStack


def create_environment(scope: Construct) -> cdk.Environment:
    """
    Create the environment (account and region) for the CDK app.

    :param scope: Any CDK construct is a valid scope, but usually the CDK App object is passed
    :return: the CDK environment
    """
    return cdk.Environment(
        account=try_get_context(scope, "aws.account.id"),
        region=try_get_context(scope, "aws.region")
    )


def get_stack_prefix(scope: Construct) -> str:
    """
    Get the stack prefix from the context.

    To make the AWS CloudFormation stacks of the Application identifiable (as a group), and unique (make it possible
    that an application can be deployed multiple times in the same AWS account), we will use a stack prefix for all the
    stacks coming from configuration.

    The precedence order for the stack prefix configuration options is as follows:

    1. `aws.cloudformation.stack.prefix`

       If the prefix is configured explicitly, it will be used.

    2. `application.name.pascal-case`

        The next preference is to use the application name in PascalCase.

    3. `application.name.human-readable`

        The next preference is to use the application name in human-readable format. This will be converted to
        PascalCase.

    3. `application.name`

        The last preference is to use the application name and this function will convert it to PascalCase.


    If no stack prefix is found in the context, a ValueError will be raised.

    :param scope: Any CDK construct is a valid scope, but usually the CDK App object is passed
    :return: the stack prefix as a string
    """

    prefix = try_get_context(scope, "aws.cloudformation.stack.prefix") or \
             try_get_context(scope, "application.name.pascal-case")

    if prefix is None:
        human_readable_name = try_get_context(scope, "application.name.human-readable")
        if human_readable_name is not None:
            prefix = pascalcase(kebabcase(human_readable_name))

    if prefix is None:
        name = try_get_context(scope, "application.name")
        if name is not None:
            prefix = pascalcase(kebabcase(name))

    if prefix is None:
        raise ValueError("No stack prefix found in the context")

    return prefix


def try_get_context(scope: Construct, key: str) -> Optional[str]:
    # With the first preference, try to get the value from the context
    value = scope.node.try_get_context(key)

    # If the value is not found in the context, try to get it from the preloaded config JSON
    if value is None:
        preloaded_config = scope.node.try_get_context("config@python-dict")
        if preloaded_config is not None:
            value = preloaded_config.get(key)

    return value


def load_config_json(scope: Construct) -> None:
    """
    Load a config JSON file into the context.

    If the context contains a key `config.json.file-path`, the file will be read and its contents will be loaded into
    the context under the key `config@python-dict`.

    The file is expected to be a JSON file, and the Python dictionary will be a flattened dictionary.

    :param scope: Any CDK construct is a valid scope, but usually the CDK App object is passed
    :return: None
    """

    config_json_path = scope.node.try_get_context("config.json.file-path")
    if config_json_path is not None:
        with open(config_json_path) as config_json_file:
            config_json = json.load(config_json_file)

        scope.node.set_context("config@python-dict", flatten_dict(config_json))


def flatten_dict(dictionary: str, separator='.', prefix=''):
    return {
        prefix + separator + k if prefix else k: v
        for kk, vv in dictionary.items()
        for k, v in flatten_dict(vv, separator, kk).items()
    } if isinstance(dictionary, dict) else {prefix: dictionary}


app = cdk.App()
load_config_json(app)

env = create_environment(app)
stack_prefix = get_stack_prefix(app)

# Creates the Log Group stack
LogGroupStack(app, f"{stack_prefix}-LogGroup", env=env)

# Synthesize the CloudFormation template
app.synth()
