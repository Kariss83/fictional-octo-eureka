import csv
import json

json_ouput = {}

with open(
    "input_file.csv", "r", encoding="utf-8"
) as file:
    csv_reader = csv.reader(file, delimiter=";")
    for row in csv_reader:
        json_output[row[0]] = row[1]
        
with open("ouput_file.json", "w", encoding="utf-8" as f:
    json.dump(json_output, f, ensure_ascii=False, indent=4)
