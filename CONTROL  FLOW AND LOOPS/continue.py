i=20 # doubt if i declare i =20 here  and i performed many oprations in in for loop code it changed and at last  it remains same value python checks line by line na so how is it possible  (may be it is not static variable) 

print(i)
for i in range (1, 21):
    print(i)
    if i == 15:
        continue
    print("water")
print (i)
# The continue statement skips the rest of the code in the current iteration and moves to the next iteration.
