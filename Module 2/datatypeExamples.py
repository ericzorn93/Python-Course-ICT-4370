import Fraction

# Booleans
boolean_true = True
boolean_false = False 
x = True
boolean_function = bool(x) # Prints True

# Numbers
integer = 10
floating_point_number = 100.99
complex_number = (1+2j)
fraction = 1/4 or Fraction(0.25)

# Strings
first_name = "Eric"
last_name = "Zorn"
space = " "
full_name = first_name + space + last_name

# Lists
name = [first_name, last_name, full_name]
random_list = [12, "hello", 123.234, True]
len(random_list) # Prints length of random_list, which is 4. List combines any datatypes to different values

# Tuples
tup1 = ('Eric', 'Zorn', 1995, 234.123);
new_empty_tuple = ()
tup2 = "E", "r", "i", "c", 22

# Sets
set_one = {12, 453, 324, "Eric"}

# Dictionaries 
dictionary_one = {"first_name": "Eric", "last_name": "Zorn", "age": 22}
print(dictionary_one.keys())
print(dictionary_one.values())

# Bytes and Byte Arrays
string = "Hello World!"
arr = bytes(string, 'utf-8')

key = bytearray([0x15, 0x23, 0x00, 0x00, 0x15, 0x12])

