student1={"name":"nishant singh",
         "age":19,
         "class":"btech"
         }
student2={"name":"manshi singh",
         "age":19,
         "class":"btech"
         }
student3={"name":"ajay singh",
         "age":19,
         "class":"btech"
         }
student4={"name":"suman singh",
         "age":19,
         "class":"btech"
         }
for i in student1:
    print(i)
    
mark={"math":90,
      "science":90,
      "hindi":90,
      "English":90,
      }
for i in student1,mark:
    print(i)
# how to create the list
list1=[1,2,34,"nishant",90.1]
print(list1[3])
# # assingment question
# Create a list of 5 fruits:
# ["apple", "banana", "mango", 
#  "orange", "grapes"]

# Do these operations:
# 1.⁠ ⁠Print first 3 fruits
# 2.⁠ ⁠Add "pineapple" at end
# 3.⁠ ⁠Remove "banana"
# 4.⁠ ⁠Print final list
fruits=["apple", "banana", "mango", "orange", "grapes"]
# 1.⁠ ⁠Print first 3 fruits
print(fruits[2])
# 2.⁠ ⁠Add "pineapple" at end
fruits[0]="pineapple"
print(fruits)
# 3.⁠ ⁠Remove "banana"
fruits.remove("banana")
print(fruits)
# 4.⁠ ⁠Print final list
print(fruits)



# Create a tuple of student info:
# •⁠  ⁠name, age, city, course

# Unpack the tuple and print:

# Name  : Rahul
# Age   : 20
# City  : Pune
# Course: Python

tuple1=("name","Age","City")
print(tuple1)

# Create a set of students:
# ["Rahul", "Priya", "Rahul",
#  "Rohan", "Priya", "Sneha"]

# 1.⁠ ⁠Print set (duplicates remove!)
# 2.⁠ ⁠Add "Amit"
# 3.⁠ ⁠Remove "Rohan"
# 4.⁠ ⁠Print final set
students=["rahul","priya","rahul","Rohan","Rohan","Priya","Sneha"]
students.append("Amrit singh")
print(students)
students.remove("Rohan")
