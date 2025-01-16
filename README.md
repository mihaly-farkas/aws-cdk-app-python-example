#   AWS CDK Application with Python Example

This very simple application is designed to show you how to manage an [AWS CDK](https://aws.amazon.com/cdk/) 
application written in [Python](https://www.python.org/.

It does not focus on the application itself, but I intend to present an  working continuous integration solution using 
[GitHub Actions](https://github.com/features/actions).

This app was generated using the 
[mihaly-farkas/copier-template-aws-cdk-app-python](https://github.com/mihaly-farkas/copier-template-aws-cdk-app-python) 
template using [Copier](https://copier.readthedocs.io/en/stable/).

## Prerequisites

1. You need to have an AWS account. If you don't have one, you can create one for free. Refer to the
   [Creating and activating an AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
   guide for more information.

2. Follow the instructions in the
   [Working with the AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html) guide to
   install the AWS CDK and Python in your development environment.

## Deployment

To deploy the AWS CDK application, first of all, you need to set up your AWS CLI with the necessary credentials.
You have many options to do this, please refer to the
[Configuring settings for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
documentation.

After setting up your AWS CLI, you can deploy the CDK application by running the following command:

```bash
cdk deploy
```

## License <a name="License"></a>

This application is licensed under the [MIT License](LICENSE).
