x = input("What's x?")
y = input("What's y?")

# La función [float()] convierte los valores en datos float, números con decimales
z = float(x) + float(y)

# La función [round()] redondea el float al int más cercano
print(round(z))

# La función [round()] tiene un segundo parametro opcional para definir el número de decimales que queremos
print(round(z, 2))

# Usando una interpolación del string podemos formatear números con separadores de miles por ejemplo,
# esto nos permite formatear el número según las normas de escritura de otros paises
print(f"{z:,}")

# Tambien podemos definir el numero de decimales que queremos con la interpolacion de string
# Nota: la sintaxis es bastante criptica
print(f"{z:.2f}")