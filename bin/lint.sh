#!/bin/bash

PROJECT_DIR=$(git rev-parse --show-toplevel)

${PROJECT_DIR}/.venv/bin/mypy ${PROJECT_DIR}
