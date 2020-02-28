def F1(palabra):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if type(palabra) != str:
        return ("ERROR: Tipo de dato incorrecto")
    else:
        for letra in palabra:
            if letra == letra.upper() and letra not in numeros:
                return ("ERROR: Mayúsculas no admitidas")
    return palabra.upper()


def F2(palabra):
    if type(palabra) != str:
        return ("ERROR: Tipo de dato incorrecto")
    else:
        return ('w' in palabra)


def F3(a, b):
    if type(a) != int or type(b) != int:
        return("ERROR: Tipo de dato incorrecto")
    elif a - b < 0:
        return("ERROR: El resultado no pertenece a los números naturales")
    else:
        return (a - b)
