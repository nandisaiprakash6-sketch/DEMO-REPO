#Typecasting is the process of converting one data type to another.
#Python provides built-in functions for typecasting:
#int(): Converts to integer.
#float(): Converts to float.
#str(): Converts to string.
#bool(): Converts to boolean.
a=20
print(a)
print(type(a))
s= str(a)
print(s)
print(type(s))
# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int)
print(type(num_int))  # Output: 10

# Convert integer to string
num = 25
num_str = str(num)
print(num_str) 
print(type(num_str)) # Output: "25"

# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int)
print(type(pi_int))   # Output: 3