#!/bin/bash

uv venv .venv
source .venv/bin/activate
uv pip sync uv.lock
uv pip install -e ./transformers
