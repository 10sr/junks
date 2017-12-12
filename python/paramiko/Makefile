PYTHON := python2
PIP := pip2

ACTIVATE := . venv/bin/activate

venv:
	virtualenv -p ${PYTHON} venv

install:
	${ACTIVATE} && ${PIP} install -r requirements.txt


main:
	${ACTIVATE} && ${PYTHON} main.py
