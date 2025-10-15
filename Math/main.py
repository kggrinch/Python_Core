import math # import math library to get more math functions

# Basic Arithmetics
x = 5

# Addition
x = x + 1
print(x)

x += 1
print(x)

# Subtraction
x = x - 1
print(x)

x -= 1
print(x)

# Multiplication
x = x * 3
print(x)

x *= 3
print(3)

# Division
x = x / 3
print(x)

x /= 3
print(x)

# Exponents
x = x ** 2  # x^2
print(x)

x **= 2
print(x)

# Modulus
x = x % 2
print(x)

x %= 2
print(x)

# Built-in math functions
x = 3.14
y = -4
z = 5

# round
resultx = round(x)
print(resultx)

# absolute value
resulty = abs(y)
print(resulty)

# power function (base, exponent)
resultz = pow(z, 3)
print(resultz) 

# Max value out of a given set
result_max = max(x, y, z)
print(result_max)

# Min value out of a given set
result_min = min(x, y, z)
print(result_min)


# Math library functions
# To get pi function
pi = math.pi
print(pi)

# to get e function
e = math.e
print(e)

# sqrt function
x = 9
result_sqrt = math.sqrt(x)
print(result_sqrt)

# ceiling function (round always up)
x = 3.123
ceil_x = math.ceil(x)
print(ceil_x)

# floor function (round always down)
x = 3.989
floor_x = math.floor(x)
print(floor_x)