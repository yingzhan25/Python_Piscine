#!/usr/bin/python3

def	my_func(pair):
	key, value = pair
	return int(value["date_of_birth"])
	 
def	famous_births(persons):
	sort_dict = dict(sorted(persons.items(), key=my_func))
	for x in sort_dict.values():
		data = dict(x)
		name = data["name"]
		year = data["date_of_birth"]
		print(f"{name} is a great scientist born in {year}.")

women_scientists = {
	"ada": {"name": "Ada Lovekace", "date_of_birth": "1815"},
	"cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
	"lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
	"grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)
