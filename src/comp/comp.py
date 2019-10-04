# The following list comprehension exercises will make use of the
# defined Human class.
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [x.getName() for x in humans if list(x.getName())[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [x.getName() for x in humans if list(x.getName())[len(list(x.getName())) - 1] == "e"]
print(b)
# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
alpha = ['C','D','E','F','G']
c = [x.getName()  for x in humans for v in alpha if list(x.getName())[0] == v]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [x.getAge() + 10 for x in humans]

print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [x.getName() + '-' + str(x.getAge()) for x in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [( x.getName(),x.getAge()) for x in humans for v in range(27,33) if x.getAge() == v]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [{'name':x.getName().upper(),'age':x.getAge() + 5} for x in humans]

print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(x.getAge()) for x in humans]

print(h)
