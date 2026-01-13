#!/usr/bin/python3

#Python without list comprehension
#num_array = [2, 8, 9, 48, 8, 22, -12, 2]
#new_array = []
#for x in num_array:
#    if x > 5:
#        new_array.append(x + 2)
#print(num_array)
#print(new_array)

#Python with list comprehension
num_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [ x + 2 for x in num_array if x > 5]
print(num_array)
print(new_array)

