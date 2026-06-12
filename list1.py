list=[]
for i in range(0,10):
    list.append(i)
print(list)
# the secound methode in the list craton

number=[i for i in range(0,5)]
print(number)
# shoret 
even=[i for i in range(0,89) if i%2==0 ]
print(even)
# to find the odd number the shor cut row
odd=[i for i in range(0,90) if i%2!=0]
print(odd)





# Create a list of 10 students:
# ["Rahul", "Priya", "Rohan", "Sneha", 
# "Amit", "Pooja", "Vikas", "Neha", 
# "Raj", "Anita"]

# Do these operations:
# 1.⁠ ⁠Print first 5 students
# 2.⁠ ⁠Print last 5 students
# 3.⁠ ⁠Print every 2nd student
# 4.⁠ ⁠Add "Riya" at end
# 5.⁠ ⁠Remove "Rahul"
student=["Rahul", "Priya", "Rohan", "Sneha", 
"Amit", "Pooja", "Vikas", "Neha", 
"Raj", "Anita"]
print(student[0:5])
print(student[-5:])
print(student[::2])
print(student.append("Riya singh"))
student.pop("rahul")
# that is the solve the problem