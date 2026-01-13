#!/usr/bin/python3
i = 0
while i < 11:
    j = 0
    print(f"Table of {i}:", end=" ")
    while j < 11:
        if j != 10:
            print(f"{i * j}", end=" ")
        else:
            print(f"{i * j}")
        j += 1
    i += 1
