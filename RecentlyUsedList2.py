#!/usr/bin/env python

class RecentlyUsedList(object):
    def __init__(self, *args):
        self._lista = []
        for elem in args:
            self.insert(elem)


    def __len__(self):
        return len(self._lista)

    def __getitem__(self,index):
        return self._lista[index]
    
    def insert(self, value):
        try:
            self._lista.remove(value)
        except ValueError as identifier:
            pass
        finally:
            self._lista.insert(0,value)

    def __str__(self):
        return "RecentlyUsedList("+str(self._lista)+")"
    
    def __repr__(self):
        return "\"RecentlyUsedList("+str(self._lista)+")\""

rul = RecentlyUsedList('aa','bb','aa')
print len(rul)

rul.insert('first')
rul.insert('second')

print rul[0]
print rul[1]

print rul
print repr(rul)
