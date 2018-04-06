pipenv := env PIPENV_VENV_IN_PROJECT=1 pipenv

play: .venv  ## Invoke ansible-playbook
	${pipenv} run ansible-playbook -vvv main.yml

facts: .venv  ## Show fact
	${pipenv} run ansible -m setup localhost


.venv:
	${pipenv} install
