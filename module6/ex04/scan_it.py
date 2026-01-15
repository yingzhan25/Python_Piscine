#!/usr/bin/python3

import sys, re

arg = sys.argv
if len(arg) != 3:
    print("none")
else:
    num = len(re.findall(arg[1], arg[2]))
    if num == 0:
        print("none")
    else:
        print(num)
