from tablib import Dataset
from pathlib import Path

# Import a single CSV file
with open('artifacts/simple_example.csv', 'r') as file:
    imported_data = Dataset().load(file)
#print(imported_data)

# CSV files with no headers
with open('artifacts/no_header.csv', 'r') as file:
    no_header_data = Dataset().load(file, headers=False)
no_header_data.headers = ['Name', 'Age']
#print(no_header_data)

# JSON files
with open('artifacts/standard.json', 'r') as file:
    json_file = Dataset().load(file)
#print(json_file)

# Work with multiple files
combined_data = Dataset(headers=('first_name', 'last_name'))
for path in Path('artifacts/multiple/').iterdir():
    with open(path, 'r') as file:
        temp_data = Dataset().load(file)
        combined_data.extend(temp_data)
print(combined_data)