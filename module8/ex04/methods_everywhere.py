#!/usr/bin/python3

def shrink(word):
    print(word[:8])
def enlarge(word):
    padding = 8 - len(word)
    for x in range(padding):
        word += "Z"
    print(word)

import sys

arg = sys.argv
if len(arg) < 2:
    print("none")
else:
    for x in arg[1:]:
        if len(x) > 8:
            shrink(x)
        elif len(x) < 8:
            enlarge(x)
        else:
            print(x)
