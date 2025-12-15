#!/bin/bash

source /opt/venv/bin/activate

cd /code
RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

uvicorn main:app --host $RUN_HOST --port $RUN_PORT --reload 