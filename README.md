[![Continuous Integration](https://github.com/mihaly-farkas/aws-cdk-app-python-example/actions/workflows/continuous-integration.yaml/badge.svg)](https://github.com/mihaly-farkas/aws-cdk-app-python-example/actions/workflows/continuous-integration.yaml)

# AWS CDK Application with Python Example

This very simple application is designed to show you how to manage an [AWS CDK](https://aws.amazon.com/cdk/)
application written in [Python](https://www.python.org/.

It does not focus on the application itself, but I intend to present an working continuous integration solution using
[GitHub Actions](https://github.com/features/actions).

This app was generated from the
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

## Continuous Integration

### Release Please Action

This repository implements a release workflow using [Google APIs'](https://github.com/googleapis)
[Release Please Action](https://github.com/googleapis/release-please-action). This action automatically maintains a
[release branch](https://github.com/mihaly-farkas/aws-cdk-app-python-example/tree/release-please--branches--main)
and opens a [pull request](https://github.com/mihaly-farkas/aws-cdk-app-python-example/pulls) if there are releasable
changes in the `main` branch.

To release the prepared changes, you need to do nothing, just merge the release pull request. The workflows will
take care of the rest.

For the Release Please action to work, it will be necessary to configure the environment with a (service) user
token.<br>
See the `${{ secrets.SERVICE_USER_CI_TOKEN }}` setting in the
[Continuous Integration](.github/workflows/continuous-integration.yaml) workflow file.

You can generate a personal access token (PAT) for the service user in the GitHub web UI under your account
settings.<br>
See: [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

Required scopes:

* `repo`
* `write:packages`

Once you have the token, you can set up the repository. <br>
See [Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)

## License <a name="License"></a>

This application is licensed under the [MIT License](LICENSE).
