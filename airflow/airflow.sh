#!/bin/bash
set -eux
set -o pipefail

export AIRFLOW_HOME=./airflow_home

exec pipenv run airflow "$@"
