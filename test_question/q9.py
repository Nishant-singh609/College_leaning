
# Q9. Perform the following Set and Tuple operations: (2 Marks)
# • Create a set of 5 programming languages (include 2 duplicates) — print to show uniqueness • Create another set of 3 languages and perform: union, intersection, difference
# • Create a tuple of 5 city names
# • Count occurrences of a city, find its index, and check if a city exists in the tuple
# • Try to modify the tuple and handle the error with a proper message



# Set Operations
lang1 = {"Python", "Java", "C++", "Python", "Java", "C"}

print("Set 1:", lang1)

lang2 = {"Python", "JavaScript", "C"}

print("Union:", lang1.union(lang2))
print("Intersection:", lang1.intersection(lang2))
print("Difference:", lang1.difference(lang2))

# Tuple Operations
cities = ("Bhopal", "Delhi", "Mumbai", "Delhi", "Indore")

print("Count of Delhi:", cities.count("Delhi"))
print("Index of Mumbai:", cities.index("Mumbai"))

if "Bhopal" in cities:
    print("Bhopal exists in tuple")

# Modify tuple
try:
    cities[0] = "Pune"
except TypeError:
    print("Tuple cannot be modified")