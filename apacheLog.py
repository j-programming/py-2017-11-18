#!/usr/bin/env python
import sys
if __name__ == "__main__":
    filename = sys.argv[1]
    suma=0
    with open(filename) as s:
        for line in s:
            last=line.split(' ')[-1]
            try:
                suma+=int(last)
            except Exception as identifier:
                pass
    print(suma)

    total=0
    with open(filename) as s:
        bytescolumn = [record.split(' ')[-1].strip() for record in s]
        byteslist = [int(data) for data in data!='-'] # 7587, 133 itd., `-` sa pomijane
        total = sum(byteslist)
    
    print(total)