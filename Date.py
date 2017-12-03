#!/usr/bin/env python


class Date(object):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date):
        elems = date.split('-')
        return cls(int(elems[0]), int(elems[1]), int(elems[2]))


d1 = Date(20, 1, 2016)
print d1.day, d1.month, d1.year

d2 = Date.from_string('20-01-2016')
print d2.day, d2.month, d2.year
