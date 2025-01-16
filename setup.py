import json
import os

from setuptools import setup

package_root = os.path.abspath(os.path.dirname(__file__))

def get_version(file_path=os.path.join(package_root, ".release-please-manifest.json")):
    with open(file_path, 'r') as file:
        data = json.load(file)
        version = data.get(".")
        return version

setup(
    name="mihaly-farkas.aws-cdk-app-python-example",
    version=get_version(),
    description="An example AWS CDK application built with Python",
    author="Mihaly Farkas",
    python_requires=">=3.8",
    install_requires=[
        "aws-cdk-lib>=2.176.0",
        "constructs>=10.0.0,<11.0.0",
    ],
    include_package_data=True
)
