#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, 10sr <8.slashes () gmail.com>
#
# This file is part of Ansible
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

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

# import module snippets
from ansible.module_utils.basic import AnsibleModule

# ==============================================================
# main

def main():

    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True, aliases=['dest'], type='path'),
            data = dict(required=True, aliases=['content'], type='raw'),
            indent_size = dict(default=2, type='int'),
            backup = dict(default='no', type='bool'),
            create=dict(default=True, type='bool')
        ),
        add_file_common_args = True,
        supports_check_mode = True
    )

    path = module.params['path']
    data = module.params['data']
    indent_size = module.params['indent_size']
    backup = module.params['backup']
    create = module.params['create']

    (changed, backup_file, diff, msg) = do_yaml(
        module=module,
        path=path,
        data=data,
        indent_size=indent_size,
        backup=backup,
        create=create
    )

    if not module.check_mode and os.path.exists(path):
        file_args = module.load_file_common_arguments(module.params)
        changed = module.set_fs_attributes_if_different(file_args, changed)

    result = {
        'changed': changed,
        'msg': msg,
        'path': path,
        'diff': diff,
        'backup_file': backup_file
    }

    module.exit_json(**result)

if __name__ == '__main__':
    main()
