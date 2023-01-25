x = int(input("What's x? "))
y = int(input("What's y? "))

# Operator or to chain conditions
if x < y or x > y:
	print("x is not equal to y")
else:
	print("x is equal to y")

# This next two examples are equal with different aproach

# Operator != to check if not equal
if x != y:
	print("x is not equal to y")
else:
	print("x is equal to y")
	
# Operator == to check if equal
if x == y:
	print("x is equal to y")
else:
	print("x is not equal to y")