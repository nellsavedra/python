# Definimos la variable [name] y usamos la función [input()] para solicitar texto al usuario
name = input("What's your name? ")

# Imprimimos en la consola
# [print()] acepta como primer parametro posicional multiples objetos, y como parametros
# con nombre [sep] que establece el separado entre parametros
# y [end] que establece el final de linea
print("Hello,", name)

# También es posible hacer una interpolación del string y la variable añadiendo una f al principio 
# del string, de esta manera Python sabe que es un string especial
print(f"Hello, {name}")