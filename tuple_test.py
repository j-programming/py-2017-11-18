#!/usr/bin/env python
import sys
if __name__ == "__main__":
    a='aaaa'
    b='bbbb'
    b,a=a,b #zamiast b,a=t=a,b
    print(a,b)

    c='cccc'
    d='dddd'
    swap=c
    c=d
    d=swap
    print(c,d)