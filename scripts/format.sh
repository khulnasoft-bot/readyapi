#!/usr/bin/env bash
set -x

ruff check readyapi tests examples scripts --fix --unsafe-fixes
ruff format readyapi tests examples scripts
