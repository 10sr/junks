#!/usr/bin/env python2
# ansible module boilerplate example
# http://docs.ansible.com/developing_modules.html#common-module-boilerplate


def main():
    module = AnsibleModule(argument_spec={
        "arg1": {
            "required": True,
            "choices": BOOLEANS
        },
        "arg2": {
            "default": "abc",
            "choices": ["abc", "def"]
        }
    })

    msg = "ARGS: " + str(module.params)

    result = dict()
    result["msg"] = msg
    if module.boolean(module.params["arg1"]):
        result["changed"] = False
        module.exit_json(**result)
    else:
        module.fail_json(**result)
    return 0


# *Must* use astarisk, or fail when test-module with
# "this module requires key=value arguments (['<<INCLUDE_ANSIBLE_MODULE_ARGS>>'])"

# http://www.backlog.jp/blog/2013/12/ansible-module-2.html
# Python import does not actually occur, instead ansible runtime replaces this
# line with contents in ansible.module_utils.basic.py .
# Replacing code appears in this file:
# https://github.com/ansible/ansible/blob/devel/lib/ansible/module_common.py
from ansible.module_utils.basic import *
# https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/basic.py
main()
