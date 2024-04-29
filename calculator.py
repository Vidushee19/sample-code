

def add(a, b):
	return a + b

def subtract(a,b):
	return a - b


def multiply(a,b):
	return a * b


def divide(a, b):
	return a / b

def absolutedivide(a, b):
	return a // b
print("Please select operation -\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Absolute division\n")

z = int(input("Select operations form 1, 2, 3, 4, 5 :"))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if z == 1:
	print(n1, "+", n2, "=",add(n1, n2))

elif z == 2:
	print(n1, "-", n2, "=",subtract(n1, n2))

elif z == 3:
	print(n1, "*", n2, "=",multiply(n1, n2))

elif z == 4:
	print(n1, "/", n2, "=",divide(n1, n2))
elif z == 5:
	print(n1, "//", n2, "=",absolutedivide(n1, n2))
	
else:
	print("Invalid input")
