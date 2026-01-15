#!/usr/bin/python3

def downcase_it(word):
    return (word.lower())

import sys

arg = sys.argv
if len(arg) < 2:
    print("none")
else:
    for x in arg[1:]:
        print(downcase_it(x))
