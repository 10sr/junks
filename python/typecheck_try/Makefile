pipenv := pipenv
python3 := $(pipenv) run python3

export PIPENV_VENV_IN_PROJECT = 1

npm := npm


check: app-test check-format check-type

installdeps:
	$(pipenv) install --dev --deploy
	# $(pipenv) run pip install mypy --install-types
	$(npm) install --include=dev


# Type Checks #################

# check-type: mypy
check-type: mypy pyright pyre pytype

mypy:
	$(pipenv) run mypy --strict -p typecheck_try
# TODO: This really works?
#	$(poetry) run mypy --config-file .mypy.ini .

pyright:
	$(pipenv) run $(npm) run -- pyright -p .

# 2021-09-28 10:23:59,478 [PID 64338] DEBUG dyld: lazy symbol binding failed: Symbol not found: ____chkstk_darwin
# 2021-09-28 10:23:59,479 [PID 64338] ERROR Check command exited with non-zero return code: -6.
# 2021-09-28 10:23:59,479 [PID 64338] DEBUG   Referenced from: /home/10sr/my/junks/python/typecheck_try/.venv/bin/pyre.bin
pyre:
	# $(pipenv) run pyre --search-path .venv/lib --sequential --strict --noninteractive check

pytype:
	$(pipenv) run pytype --config=./.pytype.cfg typecheck_try
