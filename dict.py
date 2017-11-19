#!/usr/bin/env python
import sys
if __name__ == "__main__":
    text = 'Ala ma kota ala ala ala'
    dic={}
    for txt in text.lower().split():
        if (txt not in dic):
            dic[txt]=1
        else:
            dic[txt]+=1

    for k, v in dic.iteritems():
        print(k+" -> "+str(v))




#a = '123' if b else '456'

