#!/usr/bin/env python
import sys
if __name__ == "__main__":
    suma=0
    for nmb in range(1001):
        if nmb%3==0 or nmb%5==0:
            suma+=nmb
    print(suma)
if __name__ == "__main__":
    #print(sys.argv)
    print(sum([nmb2 for nmb2 in range(1001) if nmb2%3==0 or nmb2%5==0]))
 
