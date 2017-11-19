#!/usr/bin/env python

#for
suma=0
for char in str(2**1000):
    suma+=int(char)
print(suma)

#lista
l=[]
for char in str(2**1000):
    l.append(int(char))
print(sum(l))
