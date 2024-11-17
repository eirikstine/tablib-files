from tablib import Dataset

# Creating a dataset
data = Dataset()

# Adding headers
data.headers = ["Name", "Phone Number"]

data.append(["Eirik", "74937475 "])
data.append(["Stine", "75839478"])

# No data formatting - Whitespace is kept
print(data.dict)

def remove_whitespace(phone_num: str) -> str:
    """Removes whitespace from phone numbers."""
    return phone_num.strip()

data.add_formatter("Phone Number", remove_whitespace)

# Check that the formatter has been added
print(data._formatters)

data.append(["Eirik", "74937475 "])
data.append(["Stine", "75839478"])

# Data is automatically formatted on insertion.
print(data.dict)