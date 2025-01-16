import json
import os

from setuptools import setup

package_root = os.path.abspath(os.path.dirname(__file__))

# Read the version from the .release-please-manifest.json file
with open(os.path.join(package_root, ".release-please-manifest.json")) as release_please_manifest_file:
    release_please_manifest = json.load(release_please_manifest_file)
version = release_please_manifest["."]

setup(
    name="mihaly-farkas.aws-cdk-app-python-example",
    version=version,
    install_requires=[
        "aws-cdk-lib>=2.176.0",
        "constructs>=10.0.0,<11.0.0",
    ],
    author="Mihaly Farkas",
    description="An example AWS CDK application built with Python",
    license="MIT",
    keywords="aws aws-cdk",
)
