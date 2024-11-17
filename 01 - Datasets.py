from tablib import Dataset

# Creating a dataset
data = Dataset()

# Adding headers
data.headers = ["Name", "Phone Number"]

# Adding rows
data.append(["Eirik", "74937475"])
data.append(["Stine", "75839478"])

# There is a method .extend that appends multiple rows. 

# Have nice printing
print(data)

# Get a standard Python representation
print(data.dict)

# Add a new column
data.append_col([8, 15], header="Age")
print(data)

# Selecting columns and rows
print(data["Age"])
print(f"Average age: {sum(data["Age"]) / len(data["Age"])}")
print(data[0])
print(data[0:2])

# Delete columns and rows
del data["Age"]
print(data)
del data[1]
print(data)