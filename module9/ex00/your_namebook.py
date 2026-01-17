#!/usr/bin/python3

def	array_of_names(namebook):
	array = []
	for x,y in namebook.items():
		array.append(f'{x.capitalize()} {y.capitalize()}')
	return (array)

persons = {
	"jeans": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}
print(array_of_names(persons))
