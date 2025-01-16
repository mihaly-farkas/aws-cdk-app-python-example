#!/usr/bin/env bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
cd "$REPO_DIR" || exit 1

pip-upgrade requirements.txt -p all --skip-package-installation
pip-upgrade requirements-dev.txt -p all --skip-package-installation

source .venv/bin/activate
pip install -r requirements.txt --break-system-packages
pip install -r requirements-dev.txt --break-system-packages
deactivate
