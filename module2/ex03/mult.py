#!/usr/bin/python3
first_num = int(input("Enter the first number:\n"))
second_num = int(input("Enter the second number:\n"))
mult = first_num * second_num
print(f"{first_num} x {second_num} = {mult}")
if mult > 0:
    sign = "positive"
elif mult < 0:
    sign = "negative"
else:
    sign = "positive and negative"
print(f"The result is {sign}.")
