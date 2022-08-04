import json

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = "my_file.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj, indent=2, sort_keys=True)

with open(json_file) as f:
    my_family = json.load(f)
    print(my_family)
    print(my_family['children'])


my_family_as_str = json.dumps(my_family)
print(my_family_as_str)
print(type(my_family_as_str))

my_family_as_dict = json.loads(my_family_as_str)
print(my_family_as_dict)
print(type(my_family_as_dict))