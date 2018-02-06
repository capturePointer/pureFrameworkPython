# -*- coding: utf-8 -*-
#初始化
def _init():
    global _global_dict
    _global_dict = {}


def setValue(key,value):
    _global_dict[key] = value


def getValue(key,defaultValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defaultValue