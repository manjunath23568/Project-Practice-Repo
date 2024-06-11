import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open ("person1.json",'w') as fp:
    json.dump(person_dict, fp)


