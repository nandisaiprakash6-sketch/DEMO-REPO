# STRING SLICING
a ="SAI PRAKASH"
#print(a[0:3])
#print(a[0:4])
#print(a[0:5])
#print(a[0:6])
#print(a[0:7])
#print(a[0:8])
#print(a[0:9])

print(a[0:-1])
print(a[0:-2])#  add string length to -(negative) index so it give simple digit 


# slicing rannge concept
b = "freedom"
print(b[0:4]) # [0:n] means it prints string from 0 to n-1 index.
c = "international"
print(c[0:]) # by default it replaces 2nd  empty element as length of string.
print(c[:4]) # by default it replaces 1st empty element as 0.

print(c[0:13:1])  # in this print(a:b:n) it means it skips n-1 elements of the string 
print(c[0:13:2])# here it skips 2-1 = 1 elememt an d prints
