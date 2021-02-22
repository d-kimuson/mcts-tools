#!/bin/bash

$(git rev-parse --show-toplevel)/.venv/bin/stubgen -o generated-stubs -p $1
