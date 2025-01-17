#!/usr/bin/env python3
import json
import os
from typing import TYPE_CHECKING

from packaging.version import Version

if TYPE_CHECKING:
    from _typeshed import SupportsWrite

package = os.environ.get("PACKAGE")
package_version = Version(os.environ.get("PACKAGE_VERSION"))
release_please_output_json_string = os.environ.get("RELEASE_PLEASE_OUTPUT_JSON_STRING")
deployment_environment_mapping_json_string = os.environ.get("DEPLOYMENT_ENVIRONMENT_MAPPING_JSON_STRING")

release_please_output = json.loads(release_please_output_json_string)
deployment_environment_mapping = json.loads(deployment_environment_mapping_json_string)

release_created = release_please_output["releases_created"] == "true"

if release_created:
    package_version_reference = package_version
else:
    package_version_reference = os.environ.get("GITHUB_SHA")

if package_version.is_prerelease:
    if package_version.pre[0] == "a":
        package_stability = "alpha"
    elif package_version.pre[0] == "b":
        package_stability = "beta"
    elif package_version.pre[0] == "rc":
        package_stability = "release-candidate"
    else:
        raise ValueError(f"Unknown pre-release type: {package_version.pre[0]}")
else:
    package_stability = "final"

deployment_environment = deployment_environment_mapping.get(package_stability, "")

print(f"Package:         {package}")
print(f"Version:         {package_version}")
print(f"Stability:       {package_stability}")
print(f"Release created: {release_created}")
print(f"Environment:     {deployment_environment}")

with open(os.environ["GITHUB_OUTPUT"], "a") as github_output:  # type: SupportsWrite[str]
    print(f"release-created={release_created}", file=github_output)
    print(f"package={package}", file=github_output)
    print(f"package-version={package_version}", file=github_output)
    print(f"package-version-reference={package_version_reference}", file=github_output)
    print(f"package-stability={package_stability}", file=github_output)
    print(f"environment={deployment_environment}", file=github_output)
