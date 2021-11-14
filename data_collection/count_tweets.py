import os, json
json_files = [pos_json for pos_json in os.listdir() if pos_json.endswith('.json')]
count = 0
for file in json_files:
	file = open(file)
	data = json.load(file)
	count+=len(data)

print(count," tweets")