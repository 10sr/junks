# -*- coding: utf-8 -*-

from ansible import errors

def idx(data, idx):
    return data[idx];


class FilterModule(object):
    def filters(self):
        return {
            "idx": idx
        }
