# area_rectangulo.py
# Este programa calcula el área de un rectángulo y un círculo, convierte unidades de medida, y gestiona información básica de un registro.

def calcular_area_rectangulo(ancho, alto):
    """
    Calcula el área de un rectángulo.

    :param ancho: Ancho del rectángulo (float)
    :param alto: Alto del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    return ancho * alto


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.

    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    import math
    return math.pi * radio ** 2


def convertir_metros_a_centimetros(metros):
    """
    Convierte una medida en metros a centímetros.

    :param metros: Medida en metros (float)
    :return: Medida en centímetros (float)
    """
    return metros * 100


def gestionar_registro(nombre, edad, altura_m):
    """
    Gestiona la información básica de un registro.

    :param nombre: Nombre de la persona (string)
    :param edad: Edad de la persona (int)
    :param altura_m: Altura de la persona en metros (float)
    :return: Diccionario con la información del registro
    """
    altura_cm = convertir_metros_a_centimetros(altura_m)
    return {
        "nombre": nombre,
        "edad": edad,
        "altura_cm": altura_cm
    }


# Cálculo del área del rectángulo
ancho = float(input("Introduce el ancho del rectángulo: "))
alto = float(input("Introduce el alto del rectángulo: "))
area_rectangulo = calcular_area_rectangulo(ancho, alto)
print(f"El área del rectángulo es: {area_rectangulo}")

# Verifica si el área es mayor que un valor umbral (por ejemplo, 50)
umbral = 50  # integer
es_area_grande = area_rectangulo > umbral  # boolean

# Muestra un mensaje adicional basado en la comparación
if es_area_grande:
    print("El área del rectángulo es grande.")
else:
    print("El área del rectángulo es pequeña.")

# Cálculo del área del círculo
radio = float(input("Introduce el radio del círculo: "))
area_circulo = calcular_area_circulo(radio)
print(f"El área del círculo es: {area_circulo}")

# Gestión de información básica de un registro
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
altura_m = float(input("Introduce tu altura en metros: "))
registro = gestionar_registro(nombre, edad, altura_m)
print(f"Información del registro: {registro}")