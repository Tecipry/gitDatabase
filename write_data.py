import json
import argparse

print("Started write_data.py")

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, help="filename")
parser.add_argument("--data", type=str, help="data to write")

args = parser.parse_args()

file = f"database/{args.file}"
data = args.data

data_json = json.loads(data)

with open(file, 'r') as f:
    file_content = json.load(f)

file_content.append(data_json)
with open(file, 'w') as f:
    json.dump(file_content, f)
