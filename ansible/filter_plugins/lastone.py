# -*- coding: utf-8 -*-

from ansible import errors

def lastone(data):
    return data[-1];


class FilterModule(object):
    def filters(self):
        return {
            "lastone": lastone
        }
