pipenv := env PIPENV_VENV_IN_PROJECT=1 pipenv

TARGET := $(wildcard *.yml) $(wildcard *.yaml)

.PHONY: $(TARGET)

$(TARGET): .venv  ## Invoke ansible-playbook
	${pipenv} run ansible-playbook -vvv $@

facts: .venv  ## Show fact
	${pipenv} run ansible -m setup localhost


.venv:
	${pipenv} install
