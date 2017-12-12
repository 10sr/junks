from paramiko import SSHClient, AutoAddPolicy

import os
import sys


HOST = "v133-130-91-27.a020.g.tyo1.static.cnode.io"
PORT = 22
USER = os.environ["USERNAME"]

COMMAND = "hostname; sleep 1; echo 1; echo 2 1>&2; sleep 1; echo 3"


def main():
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())

    ssh.connect(HOST, PORT, USER)

    chan = ssh.get_transport().open_session()
    chan.set_combine_stderr(True)

    chan.exec_command(COMMAND)

    data = chan.recv(1)
    while data:
        sys.stdout.write(data)
        data = chan.recv(1)

    exit_status = chan.recv_exit_status()
    print("Exit: {}".format(exit_status))

    ssh.close()
    return


if __name__ == "__main__":
    sys.exit(main())
