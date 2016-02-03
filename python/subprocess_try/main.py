#!/usr/bin/env python3

import subprocess

command = subprocess.Popen("./a.sh",
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
print(command.communicate())


command = subprocess.Popen("./a.sh",
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
print(command.communicate())
