#!/usr/bin/env python

def dict_without_NonesFor(**b):
    if len(kwargs) == 0:
        raise ValueError("Err, give at least one arg")
    dic={}
    for k,v in kwargs.iteritems():
        if v is not None:
            dic[k]=v
    return dic

print(dict_without_NonesFor(a=2,b=3,c=None,d=5))

def dict_without_NonesDict(**kwargs):
    if len(kwargs) == 0:
        raise ValueError("Err, give at least one arg")
    return {key: value for key,value in kwargs.iteritems() if value is not None}

print(dict_without_NonesDict(a=2,b=3,c=None,d=5))