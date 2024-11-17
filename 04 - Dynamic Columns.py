from tablib import Dataset

# Import a single CSV file
with open('artifacts/students.csv', 'r') as file:
    student_data = Dataset().load(file)

# Write a dynamic column
def calculate_grade(row):
    """Calculates the grade of a student based on the score."""
    score = int(row[1])
    if score > 93:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 66:
        return 'C'
    elif score >= 55:
        return 'D'
    elif score >= 40:
        return 'E'
    else:
        return 'F'

# Add the dynamically calculated column
student_data.append_col(calculate_grade, header="grade")

print(student_data)

# Add more rows
student_data.append(['81237', '86'])
print(student_data)

# Can add the dynamic column myself
student_data.append(['81237', '56', 'D'])
print(student_data)