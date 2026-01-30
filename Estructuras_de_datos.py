### Listas ###

# (estructura de datos mutable y ordenada que permite almacenar una colección de elementos.
# Los elementos de una lista pueden ser de diferentes tipos de datos y se encierran entre corchetes [], separados por comas)

frutas = ["manzana", "banana", "naranja"]

print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

# Metodos de listas

frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

# lista por comprension (crear nuevas listas basadas en una secuencia existente. Permiten filtrar y transformar los elementos de una lista en una sola línea de código.)

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

### Tuplas ###
# estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. Los elementos de una tupla se encierran entre paréntesis (), separados por comas.

punto = (3, 4)
print(punto[0])  # Imprime 3
print(punto[1])  # Imprime 4

# Metodos de tuplas
mi_tupla = (1, 2, 3, 2, 4, 2)

print(mi_tupla.count(2))   # Salida: 3
print(mi_tupla.index(2))  # Salida: 1
print(len(mi_tupla))  # Salida: 6


### Diccionarios ###
# estructura de datos mutable y desordenada que permite almacenar pares clave-valor. Los diccionarios se encierran entre llaves {}, y cada par clave-valor se separa por dos puntos (:).

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"

# Metodos de diccionarios
print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
# Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])
print(persona.items())
persona.update({"profesion": "Ingeniero"})
# Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}
print(persona)

### Conjuntos - Sets ###
# estructura de datos mutable y desordenada que permite almacenar una colección de elementos únicos. Los conjuntos se encierran entre llaves {} o se pueden crear usando la función set().

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Operaciones con conjuntos
union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}


# Metodos de conjuntos
frutas = {"manzana", "banana", "naranja"}

frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()
