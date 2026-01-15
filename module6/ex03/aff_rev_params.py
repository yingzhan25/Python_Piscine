#!/usr/bin/python3

import sys

length = len(sys.argv)
if length < 3:
    print("none")
else:
    for x in range(length - 1):
        print(sys.argv[length - 1 -x])
