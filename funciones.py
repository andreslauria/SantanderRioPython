### Funciones ###
# son bloques de código reutilizables que nos permiten encapsular tareas específicas y ejecutarlas cuando sea necesario.

def saludo():
    print("¡Hola, mundo!")


saludo()  # Imprime "¡Hola, mundo!"

# Parametros y argumentos
# Parámetros son los valores que se pasan a la función cuando se la llama.


def saludo_particular(nombre):
    print(f"¡Hola, {nombre}!")


saludo_particular("Ana")  # Imprime "¡Hola, Ana!"

# Parametros por defecto
# Podemos definir valores predeterminados para los parámetros de una función.


def saludo_personalizado(nombre="Amigo"):
    print(f"¡Hola, {nombre}!")


saludo_personalizado()         # Imprime "¡Hola, Amigo!"
saludo_personalizado("Luis")  # Imprime "¡Hola, Luis!"


# Valor de retorno
# Las funciones pueden devolver valores utilizando la palabra clave return.


def suma(a, b):
    return a + b


resultado = suma(3, 4)
print(resultado)  # Imprime 7

# Funciones anónimas (lambda)
# son funciones pequeñas y sin nombre que se definen utilizando la palabra clave lambda.


def cuadrado(x): return x ** 2


print(cuadrado(5))  # Imprime 25

# Documentación de funciones (docstrings)
# son cadenas de texto que describen el propósito, los parámetros y el valor de retorno de una función.
# Se colocan inmediatamente después de la definición de la función y se encierran entre triples comillas dobles.


def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

# Funciones con numero variable de argumentos (*args   y **kwargs)


def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22
