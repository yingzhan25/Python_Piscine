#!/usr/bin/python3

import sys

arg = sys.argv
if len(arg) < 2:
    print("none")
else:
    print(f"parameters: {len(arg) - 1}")
    for x in arg[1:]:
        print(f"{x}: {len(x)}")
