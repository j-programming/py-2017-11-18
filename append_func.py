#!/usr/bin/env python

def append_func(el, lista=[]):
    lista2=[]
    for ele in lista:
        lista2.append(ele)
    lista2.append(el)
    return lista2
    

#or rozwiazanie z repo


print(append_func(45,[3,56,2]))
print(append_func(2,[3,2,2]))


print(append_func(3, [1, 2]))
#[1, 2, 3]


print(append_func('c', ['a', 'b']))
#['a', 'b', 'c']


print(append_func('e'))
#['e']


print(append_func('f'))
#['f']

l = [1, 2]

print(append_func(3, l))
#[1, 2, 3]
print(l)
#[1, 2, 3]