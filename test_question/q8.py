

# Q8. Perform the following List operations: (2 Marks)
# • Create a list of 5 student names
# • Add 2 more names using append() and insert()
# • Remove a name using remove() and delete by index using pop() • Sort the list alphabetically and print it in reverse order
# • Slice the list to print only the first 3 elements



# Create list
students = ["Rahul", "Priya", "Rohan", "Sneha", "Amit"]

# Add names
students.append("Neha")
students.insert(2, "Karan")

# Remove names
students.remove("Rohan")
students.pop(1)

# Sort list
students.sort()

# Print reverse order
print("Reverse Order:")
print(students[::-1])

# Print first 3 elements
print("First 3 Elements:")
print(students[:3])