
# Q10. Perform the following Dictionary operations: (2 Marks)
# • Create a dictionary of 3 students: {'name': ..., 'age': ..., 'marks': ...}
# • Add a new student and update marks of an existing student
# • Delete a student using del and check if a key exists using 'in'
# • Loop through the dictionary and print all keys, values, and items • Convert all student names to a list using dict.keys()


# Dictionary of students
students = {
    "Rahul": {"age": 20, "marks": 85},
    "Priya": {"age": 21, "marks": 90},
    "Rohan": {"age": 19, "marks": 78}
}

# Add new student
students["Sneha"] = {"age": 22, "marks": 92}

# Update marks
students["Rahul"]["marks"] = 95

# Delete a student
del students["Rohan"]

# Check key exists
if "Priya" in students:
    print("Priya exists")

# Print keys
print("Keys:", students.keys())

# Print values
print("Values:", students.values())

# Print items
print("Items:", students.items())

# Loop through dictionary
for key, value in students.items():
    print(key, value)

# Convert names to list
names = list(students.keys())
print("Student Names:", names)