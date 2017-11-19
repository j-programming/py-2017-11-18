#!/usr/bin/env python

try:
    while True:
        input=raw_input(">>> ").lower()
        if input=="":
            print("Enter command")
            pass
        elif input=="exit":
            print("Goodbye")
            break
        elif input.split(' ', 1)[0]=="eval":
            try:
                print(eval(input[5:]))
            except Exception as e:
                print (type(e).__name__)
                pass
        else:
            print("Invalid command")
except KeyboardInterrupt:
    pass
print("Bye")
