#!/bin/sh
set -eux

export AIRFLOW_HOME=./airflow_home

exec pipenv run airflow "$@"
