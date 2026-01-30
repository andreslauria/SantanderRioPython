# la entrada y salida de datos nos permite interactuar con el usuario y manipular archivos

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

# La función input() siempre devuelve una cadena de texto. Si deseas trabajar con otros tipos de datos, como números enteros o flotantes,
# debes realizar una conversión explícita utilizando funciones como int() o float().

if int(edad) >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Formateo de cadenas f-strings

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# Escritura y lectura de archivos

# Lectura de un archivo
# Siempre cerrar el archivo después de usarlo para liberar recursos del sistema.!!!!

archivo = open("datos.txt", "r")  # modo de lectura ("r").
contenido = archivo.read()
print(contenido)
archivo.close()

# Escritura en un archivo

archivo = open("datos.txt", "w")  # modo de escritura ("w").
archivo.write("Hola, mundo! escrito desde python.")
archivo.close()

# apertura y cierre de archivos usando with

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)