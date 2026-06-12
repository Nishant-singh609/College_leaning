
# Q7. Create an Employee File System: (3 Marks) • Create 'employees.txt' with 3 employees
# • Read the file and print
# • Append 2 more employees
# • Read updated file
# • Delete the file and verify using os.path.exists()


import os

# Create file
with open("employees.txt", "w") as f:
    f.write("Rahul\n")
    f.write("Priya\n")
    f.write("Rohan\n")

# Read file
print("Employees:")
with open("employees.txt", "r") as f:
    print(f.read())

# Append 2 employees
with open("employees.txt", "a") as f:
    f.write("Sneha\n")
    f.write("Amit\n")

# Read updated file
print("Updated Employees:")
with open("employees.txt", "r") as f:
    print(f.read())

# Delete file
os.remove("employees.txt")

# Verify deletion
if not os.path.exists("employees.txt"):
    print("File deleted successfully")
else:
    print("File still exists")