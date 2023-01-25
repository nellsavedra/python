score = int(input("Score: "))

# Operator and  
if score >= 90 and score <= 100:
	print("Your grade is A")
	
# And alternative to and, nesting the evaluation whitout using and
if 90 <= score <= 100:
	print("Your grade is A")