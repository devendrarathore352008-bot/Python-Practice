data = {
    "name":"Devendra Rathore",
    "course": "BCA",
    "age": 18,
    "height": 5.9,
    "color": "Fair",
    "percentage": 94
}

print(data["name"])
print(data.get("height"))
print(data.keys())
print(data.values())
data["color"] = "Quite Fair"
print(data)
data.pop("percentage")
print(data)


print()

for k in data:
    print(k,":",data[k])