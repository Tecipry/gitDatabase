import json

print("Started write_data.py")
file = "database/test.json"
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open(file, 'r') as f:
    file_content = json.load(f)

file_content.append(data)
with open(file, 'w') as f:
    json.dump(file_content, f)
