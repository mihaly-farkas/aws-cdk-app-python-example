import json
import os

from setuptools import setup

package_root = os.path.abspath(os.path.dirname(__file__))
version = {}
with open(os.path.join(package_root, "version.py")) as fp:
    exec(fp.read(), version)
version = version["__version__"]

setup(
    name="mihaly-farkas.aws-cdk-app-python-example",
    version=version,
    description="An example AWS CDK application built with Python",
    author="Mihaly Farkas",
    python_requires=">=3.8",
    install_requires=[
        "aws-cdk-lib>=2.176.0",
        "constructs>=10.0.0,<11.0.0",
    ],
    include_package_data=True
)
