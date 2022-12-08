# La palabra clave [def] sirve para definir funciones en Python, todo lo que este indentando
# dentro de este bloque será parte de la función
# Podemos definir parametros con nombre y ponerle un valor por defecto si se llama
# a la función sin argumentos 
def hello(to="world"):
	print("Hello,", to)


# Las funciones tienen que estar definidas antes de llamarlas, de no ser así obtendremos un error
hello()
name = input("What's your name? ")
hello(name)


# La funciones tambien pueden devolver un valor con la palabra reservada [return]
def main():
	x = int(input("What's x? "))
	print("x squared is", square(x))
	
# Aqui retornamos un valor que usa la función [main()]
def square(n):
	return n * n
	
main()