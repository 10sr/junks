NERU_ENV ?= local
NERU_PORT ?= 9099
NERU_HOST ?= 0.0.0.0

MAKEFLAGS += --no-builtin-rules --no-builtin-variable

# https://stackoverflow.com/questions/10859916/how-to-treat-a-warning-as-an-error-in-a-makefile/29800774#29800774
MAKECMDGOALS ?= check
${MAKECMDGOALS}: fatal-on-warning
fatal-on-warning:
	@! (${MAKE} -n --warn-undefined-variables ${MAKECMDGOALS} 2>&1 >/dev/null | grep 'warning:')


app := app
project := proj

poetry := poetry

python3 := ${poetry} run env NERU_ENV=${NERU_ENV} python3
manage_py := ${python3} manage.py

# Make all targets phony
.PHONY: $(MAKECMDGOALS)

check: poetry-check app-test mypy black-check

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

poetry-check:
	${poetry} check

app-test:
	${manage_py} makemigrations --dry-run --check
	${python3} -Wa manage.py test


###########
# Docker

docker-build:
	docker build . -t local/neru

# TODO: Add file like docker_local.env
docker-run:
	docker run -p '9099:9099' local/neru


#########
# mypy

mypy:
	${poetry} run mypy --config-file .mypy.ini -p app -p proj -p tests
# TODO: This really works?
#	${poetry} run mypy --config-file .mypy.ini .


#########
# black

black:
	${poetry} run black .

black-check:
	${poetry} run black --check .
