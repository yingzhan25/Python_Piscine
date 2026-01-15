#!/usr/bin/python3

import sys

arg = sys.argv
if len(arg) < 2:
    print("none")
else:
    for x in arg[1:]:
        if x.find("ism") != -1:
            continue
        else:
            print(x+"ism")
