#!/usr/bin/env python
import sys
if __name__ == "__main__":
    #print(sys.argv)
    for line in sys.argv[1:]:
        print(line.upper())

if __name__ == "__main__":
    #print(sys.argv)
    print[(line.upper()) for line in sys.argv[1:]]