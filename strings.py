# Definimos la variable [name] y usamos la función [input()] para solicitar texto al usuario
name = input("What's your name? ")

# Los datos tipo string tiene el método [strip()] que permite borrar espacios en blanco
name = name.strip()

# Capitaliza la primera letra de la primera palabra del string
name = name.capitalize()

# Capitaliza cada palabra del string
name = name.title()

# También es posible encadenar los métodos, la definición de la variable [name] quedaría de esta manera
name = input("What's your name? ").strip().title()

# También es posible dividir los string con el metodo [split()] y asignarlos 
# a dos variables en orden respectivamente
first, last = name.split(" ")

# También es posible hacer una interpolación del string y la variable añadiendo una f al principio 
# del string, de esta manera Python sabe que es un string especial
print(f"Hello, {name}")