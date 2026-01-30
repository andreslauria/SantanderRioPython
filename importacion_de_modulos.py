# un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas.
# Podemos importar módulos integrados de Python o crear nuestros propios módulos personalizados.


from mi_paquete import modulo_desde_paquete

import datetime
import random
# tmb podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.
from math import exp
import math
import mi_modulo


# Uso de funciones del módulo mi_modulo
mi_modulo.saludar("Carlos")  # Imprime "¡Hola, Carlos!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

# Uso de funciones del módulo math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0


resultado = exp(2)
print(resultado)  # Imprime 7.3890560989306495


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual


# Imprime "Hola desde el módulo dentro del paquete!"
modulo_desde_paquete.hola_mundo()
