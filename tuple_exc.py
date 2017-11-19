#!/usr/bin/env python
import sys
if __name__ == "__main__":
    tup=[("adam","smith"),("william","goty"),("code","pythonic")]
    for a,b in tup:
        print(b)


    print([record[1] for record in tup])
    print([b for a,b in tup])