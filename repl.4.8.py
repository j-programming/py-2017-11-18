#!/usr/bin/env python
import sys

def exit(arg):
    print ("Goodbye")
    sys.exit()

def myEval(rest):
    try:
        value = eval(rest)
    except Exception as e:
        print(type(e).__name__)
    else:
        print(value)

def empty(arg):
    print ("Enter Command")

def splitLine(line):
    tokens = line.split(None, 1)
    try:
        command = tokens[0]
    except IndexError:
        command=''
    try:
        rest = tokens[1]
    except IndexError:
        rest = ''
    return command.lower(), rest

def repl():
    comm= {"exit": exit, "eval": myEval, '': empty, "exit": exit}
    try:
        while True:
            line = raw_input(">>> ")
            command, rest=splitLine(line)
            try:
                func=comm[command]
            except KeyError as identifier:
                print("Unknown command")
            else:
                func(rest)
    except KeyboardInterrupt:
        print("Bye!")

repl()
