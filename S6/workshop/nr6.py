"""
6.	Read again the information from the csv file above, store it all in a list of data, and then write a new file,
called “students.json”, which will contain a valid JSON object. Use the following format for each student
(and use Python’s standard JSON module):
[{
"id": 1,
"fname": "Maria",
"lname": "Popescu",
"age": 31,
"grade": 7.5
},
...
]
"""
import csv
import json

filename = 'students.csv'
output_file = 'students.json'

# Read the file and store the data in a list of dictionaries
data = []

with open(filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Write thge data to the JSON file
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f'Data has been written to {output_file} in JSON format.')
