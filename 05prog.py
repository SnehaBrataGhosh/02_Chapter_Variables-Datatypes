# This programme shows us how to do type costing and what is type function
print("📘 type() Function and Type Casting in Python\n")

# Using type() to check data types
a = 10
b = 3.14
c = "25"
d = True

print("a =", a, "| type:", type(a))
print("b =", b, "| type:", type(b))
print("c =", c, "| type:", type(c))
print("d =", d, "| type:", type(d))

# Type casting examples
print("\n🔄 Type Casting Examples:")

# str to int
c_int = int(c)
print("int('25') =", c_int, "| type:", type(c_int))

# int to float
a_float = float(a)
print("float(10) =", a_float, "| type:", type(a_float))

# float to int (decimal part removed)
b_int = int(b)
print("int(3.14) =", b_int, "| type:", type(b_int))

# int to string
a_str = str(a)
print("str(10) =", a_str, "| type:", type(a_str))

# boolean to int
d_int = int(d)
print("int(True) =", d_int, "| type:", type(d_int))

# int to boolean
zero_bool = bool(0)
print("bool(0) =", zero_bool, "| type:", type(zero_bool))
