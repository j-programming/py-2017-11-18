#!/usr/bin/env python
import sys

filename = sys.argv[1]
with open(filename) as s:
    lines, words, characters = 0, 0, 0
    for line in s:
        lines +=1 
        words += len(line.split(' '))
        characters += len(line)
    print(lines, words, characters, sys.argv[1])

