#!/usr/bin/env python

def sort(args, reverse=False, limit=True):
    if not reverse:
        lista= list(sorted(args))
    else:
        lista= list(reversed(sorted(args)))
    if limit:
        return lista[:5]
    else:
        return lista

print(sort([3,2,4,6,3,56,2]))
print(sort([3,2,2]))