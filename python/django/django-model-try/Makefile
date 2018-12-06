NERU_ENV ?= local
NERU_PORT ?= 9099
NERU_HOST ?= 0.0.0.0

MAKEFLAGS += --no-builtin-rules --no-builtin-variable

app := app
project := proj

poetry := poetry

python3 := ${poetry} run env NERU_ENV=${NERU_ENV} python3
manage_py := ${python3} manage.py

# Make all targets phony
.PHONY: $(MAKECMDGOALS)

check: app-test

env:
	env

installdeps:
	${poetry} install

runserver:
	${manage_py} $@ '${NERU_HOST}:${NERU_PORT}'

# https://docs.djangoproject.com/en/1.10/intro/tutorial02/#database-setup
migrate:
	${manage_py} $@

# https://docs.djangoproject.com/en/1.10/intro/tutorial02/#activating-models
makemigrations:
	${manage_py} $@ ${app}

# Print sql query for migration
sqlmigrate:
	${manage_py} $@ ${app} ${target}

createsuperuser create_admin_user create_local_user:
	${manage_py} $@

shell:
	${manage_py} shell

manage_py:
	${manage_py} ${command}

app-test:
	${manage_py} makemigrations --dry-run --check
	${python3} -Wa manage.py test

#########
# mypy

mypy:
	${poetry} run mypy --config-file .mypy.ini -p app -p proj -p tests
