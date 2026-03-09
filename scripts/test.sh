#!/usr/bin/env bash

set -e
set -x

export PYTHONPATH=./examples
pytest -n auto --dist loadgroup  tests scripts/tests/ ${@}
