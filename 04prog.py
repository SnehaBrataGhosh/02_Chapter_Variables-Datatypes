# Here in this programme you're going to learn all the different types of operators in python

print("📘 All Types of Python Operators with Examples:\n")

# 1. Arithmetic Operators
a = 10
b = 3
print("1️⃣ Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# 2. Comparison Operators
print("\n2️⃣ Comparison Operators:")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal:", a >= b)
print("Less than or equal:", a <= b)

# 3. Assignment Operators
print("\n3️⃣ Assignment Operators:")
x = 5
print("Initial x =", x)
x += 2
print("x += 2 =>", x)
x *= 3
print("x *= 3 =>", x)
x -= 1
print("x -= 1 =>", x)
x /= 2
print("x /= 2 =>", x)

# 4. Logical Operators
print("\n4️⃣ Logical Operators:")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

# 5. Bitwise Operators
print("\n5️⃣ Bitwise Operators:")
print("5 & 3:", 5 & 3)   # AND
print("5 | 3:", 5 | 3)   # OR
print("5 ^ 3:", 5 ^ 3)   # XOR
print("~5:", ~5)         # NOT
print("5 << 1:", 5 << 1) # Left Shift
print("5 >> 1:", 5 >> 1) # Right Shift

# 6. Membership Operators
print("\n6️⃣ Membership Operators:")
lst = [1, 2, 3]
print("2 in list:", 2 in lst)
print("5 not in list:", 5 not in lst)

# 7. Identity Operators
print("\n7️⃣ Identity Operators:")
x = [1, 2]
y = x
z = [1, 2]
print("x is y:", x is y)
print("x is z:", x is z)
print("x == z:", x == z)
