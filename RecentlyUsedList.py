#!/usr/bin/env python

class RecentlyUsedList(object):
    def __init__(self, *args):
        self._lista = []
        for elem in args:
            self.insert(elem)

    @property
    def length(self):
        return len(self._lista)

    def get(self,index):
        return self._lista[index]
    
    def insert(self, value):
        try:
            self._lista.remove(value)
        except ValueError as identifier:
            pass
        finally:
            self._lista.insert(0,value)

    def to_string(self):
        return "RecentlyUsedList("+str(self._lista)+")"

rul = RecentlyUsedList('aa','bb','aa')
print rul.length

rul.insert('first')
rul.insert('second')

print rul.get(0)
print rul.get(1)
#rul.get(3)
print rul.to_string()
print rul.length

rul.insert('third')
print rul.to_string()

rul.insert('second')
print rul.to_string()
print rul.length
