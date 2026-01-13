#!/usr/bin/python3
start_num = int(input("Enter a number less than 25\n"))
if start_num > 25:
    print("Error")
else:
    while start_num <= 25:
        print(f"Inside the loop, my variable is {start_num}")
        start_num += 1
