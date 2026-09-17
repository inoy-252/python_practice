person = {"name": "Yasir", "age": 23, "city": "Pulwama", "skills": ["Python", "AI"]}
print(person)
dog = {}
dog["name"] = "Luna"
dog["color"] = "golden brown"
dog["breed"] = "German Shepherd"
dog["legs"] = 4
dog["age"] = 8
print(dog)
student = {
    "first_name": "Basit",
    "last_name": "Nasir",
    "gender": "female",
    "age": 22,
    "skills": ["Pyhton", "Git"],
    "state": "Kashmir",
    "city": "Pulwama",
    "address": {"street": "main street", "zip": "192306"},
}
print(student)
print(len(student))
print(type(student["skills"]))
student["skills"].append("Data Analysis")
print(student)
keys_list = list(student.keys())
print(keys_list)
values_list = list(student.values())
print(values_list)
items_list = list(student.items())
print(items_list)
del student["state"]
print(student)
student.pop("address")
print(student)
del dog
