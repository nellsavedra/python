name = input("What's your name? ")

# Match function
match name:
	case "Harry" | "Ron" | "Hermione":
		print("Gryffindor")
	case "Draco":
		print("Slytherin")
	case _:
		print("Who?")
		