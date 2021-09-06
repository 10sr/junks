# -*- coding: utf-8 -*-

from ansible import errors

def undefined():
    raise Exception("Undefined")


class FilterModule(object):
    def filters(self):
        return {
            "undefined": undefined
        }
