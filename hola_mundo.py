print("Hola, Mundo!")

a = 10
b = 3
edad = 18


suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1
exponenciacion = a ** b   # 1000

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", división_entera)
print("Módulo:", modulo)
print("Exponenciación:", exponenciacion)

igual = a == b   # False
diferente = a != b   # True
mayor_que = a > b   # True
menor_que = a < b   # False
mayor_o_igual = a >= b   # True
menor_o_igual = a <= b   # False

print("Igual:", igual)
print("Diferente:", diferente)
print("Mayor que:", mayor_que)
print("Menor que:", menor_que)
print("Mayor o igual:", mayor_o_igual)
print("Menor o igual:", menor_o_igual)

resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

print("Resultado AND:", resultado_and)
print("Resultado OR:", resultado_or)
print("Resultado NOT:", resultado_not)

# If-Elif-Else

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("eres menor de edad.")

calificacion = 85


if calificacion >= 90:
    print("Excelente")

elif calificacion >= 80:
    print("Muy bueno")

elif calificacion >= 70:
    print("Bueno")

else:
    print("Necesita mejorar")


# Bucle For

frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

# Bucle While

contador = 0

while contador < 5:
    print(contador)
    contador += 1

#### Control de Bucles ####

# break (salir prematuramente de un bucle, independientemente de la condición del bucle)

contador = 0
while True:

    print(contador)
    contador += 1

    if contador == 5:
        break

# continue (saltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass (operacion nula que no hace nada)

for i in range(5):
    pass

