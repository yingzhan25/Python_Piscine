#!/usr/bin/python3

def	my_func(pair):
	name, color = pair
	if color == "red":
		return True
	else:
		return False

def	find_the_redheads(family):
	array = dict(filter(my_func, family.items())).keys()
	return list(array)

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

print(find_the_redheads(dupont_family))
