print("hello Github!")
print("Learning to use Git")
print("Using branches")
print("Making changes in the branch")
print("Goodbye from farewell branch")
print("Hello from the second branch")

print("-- SIMPLE MATHS")
print(5 - 3)
print(4 * 6)

print("-- MATRIX MULTIPLICATION")
import numpy as np
A = np.array([[1, 2, 3],
    [0, 1, 0],
    [1, 1, 1]])

B = np.array([[3], [3], [0]])
print(A @B)

print("--MATRIX ADDITION")
C = np.array([[1, 2, 3],
    [0, 1, 0],
    [1, 1, 1]])
print(A + C)

print("-- Looping")
for i in range(4):
    print("simple loop iteration", i)

print("-- Some other maths")

for i in range(5):
    ar = i * 2
    br = np.round(np.log(ar + 1) + i,4)
    print("The value is", br)

print("-- This change is just to see how to create a conflict and solve it")
a = 0.9
b = 1.9
print ("a is", a, "; and b is", b)
for i in range(3):
    if i < a and i <= b:
        print(i," is less than both a and b")
    elif i > a and i > b:
        print(i, " is greater than both a and b")
    else:
        print(i, " is between a and b")


print("-- More maths")
print("The product from previous values is: ", a * b)
print("-- Automatic merge")
ac = np.array([1,2,0])
bc = np.array([2,0,1])
print("The sum is", ac + bc)

