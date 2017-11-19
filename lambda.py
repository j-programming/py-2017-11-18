#!/usr/bin/env python

#f= lambda x: x%2 == 0

print(sum(filter(lambda x: ( x%3==0 or x%5==0 ),range(1001) ) ))


print(sum(map(lambda x: int(x), list(str(2**1000)) ) ))
# sum(map(lambda: int, str(2**1000)))


print(sum(map(lambda x: int(x), filter(lambda y: int(y)%2==0,list(str(2**1000))) ) ))
#sum(filter(lambda x: x%2==0, map(int, str(2**1000))))
