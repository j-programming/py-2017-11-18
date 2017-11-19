#!/usr/bin/env python

def sumall(*args):
    if args ==():
        raise ValueError("Err, give at least one arg")
    #assert len(args) == 0, "Err"
    sum=0
    for nmb in args:
        sum+=nmb
    return sum

print(sumall(3,2,4,6,3,56,2))
print(sumall())