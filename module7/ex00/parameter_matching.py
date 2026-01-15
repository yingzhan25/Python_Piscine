#!/usr/bin/python3

import sys

arg = sys.argv
if len(arg) != 2:
    print("none")
else:
    param = input("What was the parameter? ")
    if param == arg[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
