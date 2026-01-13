#!/usr/bin/python3

#C-style
#num_array = [2, 8, 9, 48, 8, 22, -12, 2]
#new_array = list(num_array)
#for x in range(len(new_array)):
#    new_array[x] += 2
#print(f"""Original array: {num_array}
#New array: {new_array}""")

#Python without list comprehension
#num_array = [2, 8, 9, 48, 8, 22, -12, 2]
#new_array = []
#for x in num_array:
#    new_array.append(x + 2)
#print(f"""Original array: {num_array}
#New array: {new_array}""")

#Python with list comprehension
num_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [ x + 2 for x in num_array ]
print(f"""Original array: {num_array}
New array: {new_array}""")
