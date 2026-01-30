###
# El manejo de excepciones nos permite capturar y manejar errores de manera controlada utilizando las declaraciones try, except y opcionalmente finally.
###

# Try y Except


# El bloque try contiene el código que puede generar una excepción. Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except correspondiente.
# El bloque except especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

# Finally
# El bloque finally se ejecuta siempre, independientemente de si se produjo una excepción o no. Se utiliza para realizar tareas de limpieza o liberar recursos.

try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción

# Excepciones personalizadas
# Puedes definir tus propias excepciones personalizadas creando una nueva clase que herede de la clase base Exception.


def funcion():
    # Código que puede generar una excepción personalizada
    condicion_error = 0/0  # Ejemplo de condición que genera un error
    if condicion_error:
        raise Exception("Descripción del error")


try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")
