# Task1 - Datatypes in Python

# Subscripting
print("Hello"[0])
print("Hello"[len("Hello")-1])
print("Hello"[-1])

# String
print("1234" + "5678")

# Integer
print(123 + 456)

# Large Integer
print(123_456_789)

# Float
print(3.14159)

# Boolean = True or False
print(True)
print(False)


# Task2 - Type Error Checking and Conversion
print(type("string"))
print(type(123))
print(type(123.13))
print(type(True))

print(int("1234") + int("5678"))
# print(int("ABC")) -> ValueError

# Task3- f-string
age = 33
height = 178.3
is_winnning = True

print(f"Your age is {age} , your height is {height} and you are winning is {is_winnning}")
print(6 + 4 / 2 - (1 * 2))

a = int("5") / int(2.7)
print(type(a))
