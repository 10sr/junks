play: venv
	. venv/bin/activate && ansible-playbook -vvv main.yml --diff


venv:
	virtualenv venv -p python2.7
	. venv/bin/activate && pip2 install -r requirements.txt
