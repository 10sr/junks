#!/usr/bin/env python2
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


# *Must* use astarisk, or fail with
# "this module requires key=value arguments (['<<INCLUDE_ANSIBLE_MODULE_ARGS>>'])"
# http://www.backlog.jp/blog/2013/12/ansible-module-2.html
from ansible.module_utils.basic import *
main()
