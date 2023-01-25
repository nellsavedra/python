x = int(input("What's x? "))

# Modulo operator % returns the remainder of a division
if x % 2 == 0:
	print(x," is Even")
else:
	print(x, "is Odd")
	

# With a function
def main():
	x = int(input("What's x? "))
	if is_even(x):
		print(x," is Even")
	else:
		print(x, "is Odd")

def is_even(x):
	return x % 2 == 0
	
main()