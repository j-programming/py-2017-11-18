#!/usr/bin/env python


class Person(object):
    def __init__(self, first, last=None):
        if not isinstance(first, str):
            raise ValueError('First name must have at least two characters.')
        if not len(first) >= 2:
            raise TypeError('First name must be a string or unicode.')

        if last is not None:
            if not isinstance(last, str):
                raise ValueError(
                    'Last name must have at least two characters.')
            if not len(last) >= 2:
                raise TypeError('Last name must be a string or unicode.')

        self._first_name = first
        self._last_name = last

    @property
    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)if self._last_name is not None else self._first_name


p = Person('Jan', 'Kowalski')
print p._first_name
print p._last_name

print p.full_name

p2 = Person('Jan')
print p2._first_name, p2._last_name

print p2.full_name

#Person(23, 'Kowalski')
#Person('J', 'Kowalski')
Person('Jan', 23)
Person('Jan', 'K')
