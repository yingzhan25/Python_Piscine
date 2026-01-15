#!/usr/bin/python3

import sys

arg = sys.argv
if len(arg) != 3:
    print("none")
else:
    if int(arg[1]) >= int(arg[2]):
        print("Number 1 must be smaller than number 2")
    else:
        array = range(int(arg[1]), int(arg[2]) + 1)
        print(list(array))
