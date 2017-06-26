#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, 10sr <8.slashes () gmail.com>
#
# This file is not part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import yaml
# import module snippets
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}


class _TaskFailedException(Exception):
    def __init__(self, rc, msg):
        self.rc = rc
        self.msg = msg
        return


def do_yaml(module, filename, data, indent_size=2, backup=False, create=False):
    orig_data = None
    if not os.path.exists(filename):
        if not create:
            raise _TaskFailedException(
                257, 'Destination {} does not exist !'.format(filename)
            )
        destdir = os.path.dirname(filename)
        if not os.path.exists(destdir) and not module.check_mode:
            os.makedirs(destdir)
    else:
        try:
            with open(filename) as f:
                orig_data = yaml.safe_load(f)
        except yaml.error.YAMLError:
            # Ignore parse error (and possibly overwrite its content)
            pass

    if orig_data == data:
        changed = False
        msg = "OK"
    else:
        changed = True
        msg = "Data changed"

    backup_file = None
    if changed and not module.check_mode:
        if backup:
            backup_file = module.backup_local(filename)
        with open(filename, "w") as f:
            yaml.dump(
                data, f,
                explicit_start=True,
                default_flow_style=False,
                indent=indent_size
            )

    return {
        'changed': changed,
        'msg': msg,
        'backup_file': backup_file
    }

# ==============================================================
# main


def main():
    module = AnsibleModule(
        argument_spec=dict(
            config=dict(type='path'),
            script=dict(type='path'),
            chdir=dict(default='/', type='path'),
            state=dict(choices=['running', 'started', 'stopped', 'restarted', 'reloaded']),
            name=dict(required=False)
        ),
        supports_check_mode=True,
        required_one_of=[['config', 'script']],
    )

    config = module.params['config']
    script = module.params['script']
    chdir = module.params['chdir']
    state = module.params['state']
    name = module.params['name']

    try:
        result = do_yaml(
            module=module,
            filename=path,
            data=data,
            indent_size=indent_size,
            backup=backup,
            create=create
        )
        if not module.check_mode and os.path.exists(path):
            file_args = module.load_file_common_arguments(module.params)
            result['changed'] = module.set_fs_attributes_if_different(
                file_args, result['changed']
            )

    except _TaskFailedException as e:
        module.fail_json(
            rc=e.rc,
            msg=e.msg
        )
        return

    module.exit_json(
        changed=result['changed'],
        msg=result['msg'],
        path=path,
        backup_file=result['backup_file']
    )
    return

if __name__ == '__main__':
    main()
