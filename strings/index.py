# in python strings are immutable  
animal = "snake"
# animal[0] = "p" -> this will throw an error

# string interpolation 

print(f"this animal is {animal}")

print("this animal is {a}".format(a=animal))

# upper case method 
print(animal.upper())

# lower case method 
print(animal.lower())

# split method
hello = "Hello World"
# split method creates a list and splits the strings after each each space
print(hello.split())

# string indexing and slicing
print(hello[::-1])
print(hello[1:5])

