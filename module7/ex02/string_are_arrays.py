#!/usr/bin/python3

import sys

arg = sys.argv
if len(arg) != 2:
    print("none")
else:
    count = 0;
    for word in arg:
        for char in word:
            if char == "z":
                count += 1
    if count == 0:
        print("none")
    else:
        for x in range(count -1):
            print("z", end="")
        else:
            print("z")
