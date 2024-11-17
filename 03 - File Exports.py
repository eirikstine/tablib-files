from tablib import Dataset
from pandas import DataFrame

# Import a single CSV file
with open('artifacts/simple_example.csv', 'r') as file:
    imported_data = Dataset().load(file)

# Write as a CSV file
print(imported_data.export('csv'))

# Or as JSON
print(imported_data.export('json'))

# Or as YAML
print(imported_data.export('yaml'))

# Or as HTML
print(imported_data.export('html'))

# Or as Excel
print(imported_data.export('xls'))

# Have to have the newline='' argument to write it
with open('artifacts/new_file.csv', 'w', newline='') as file:
    file.write(imported_data.export('csv'))

# Write excel - Have to use the mode wb for write binary
with open('artifacts/new_file.xls', 'wb') as file:
    file.write(imported_data.export('xls'))

# Can also transform a Dataset to a Pandas dataframe
# This is useful when more data processing is needed
df = DataFrame(imported_data.dict)
print(df.head())