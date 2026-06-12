# Q6. Create a Student Report System: (3 Marks)
# • Create 'report.txt' with 5 students and marks:
# Rahul-85, Priya-90, Rohan-78, Sneha-92, Amit-65 • Read file and print only students with marks > 80 • Handle FileNotFoundError with finally block.

with open("report.txt", "w") as f:
    f.write("Rahul-85\n")
    f.write("Priya-90\n")
    f.write("Rohan-78\n")
    f.write("Sneha-92\n")
    f.write("Amit-65\n")

try:
    f = open("report.txt", "r")

    for line in f:
        name, marks = line.split("-")
        if int(marks) > 80:
            print(name, marks)

    f.close()

except FileNotFoundError:
    print("File not found")

finally:
    print("Program End")