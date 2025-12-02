# In this programme, this programme ,its going to show all the data types which are there in python

print("📘 All Main Python Data Types with Examples:\n")

# Numeric types
int_var = 10
float_var = 10.5
complex_var = 2 + 3j

print("Numeric Types:")
print("Integer:", int_var, type(int_var))
print("Float:", float_var, type(float_var))
print("Complex:", complex_var, type(complex_var))

# Sequence types
str_var = "Hello"
list_var = [1, 2, 3]
tuple_var = (1, 2, 3)

print("\nSequence Types:")
print("String:", str_var, type(str_var))
print("List:", list_var, type(list_var))
print("Tuple:", tuple_var, type(tuple_var))

# Set types
set_var = {1, 2, 3}
frozenset_var = frozenset([1, 2, 3])

print("\nSet Types:")
print("Set:", set_var, type(set_var))
print("Frozenset:", frozenset_var, type(frozenset_var))

# Mapping type
dict_var = {"a": 1, "b": 2}

print("\nMapping Type:")
print("Dictionary:", dict_var, type(dict_var))

# Boolean type
bool_var = True

print("\nBoolean Type:")
print("Boolean:", bool_var, type(bool_var))

# Binary types
bytes_var = b"hello"
bytearray_var = bytearray(5)
memoryview_var = memoryview(bytes(5))

print("\nBinary Types:")
print("Bytes:", bytes_var, type(bytes_var))
print("Bytearray:", bytearray_var, type(bytearray_var))
print("Memoryview:", memoryview_var, type(memoryview_var))

# None type
none_var = None

print("\nNone Type:")
print("None:", none_var, type(none_var))
