from setuptools import setup

setup(
    name="mihaly-farkas.aws-cdk-app-python-example",
    version="0.1.0b0",
    install_requires=[
        "aws-cdk-lib>=2.176.0",
        "constructs>=10.0.0,<11.0.0",
    ],
    author="Mihaly Farkas",
    description="An example AWS CDK application built with Python",
    license="MIT",
    keywords="aws aws-cdk",
)
