# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""


def F1(palabra):
    if type(palabra) != str:
        return ("ERROR: Tipo de dato incorrecto")
    else:
        for letra in palabra:
            if letra == letra.upper():
                return ("ERROR: Mayúsculas no admitidas")
        return palabra.upper()


def F2(palabra):
    if type(palabra) != str:
        return ("ERROR: Tipo de dato incorrecto")
    else:
        return('w' in palabra)


def F3(a, b):
    if type(a) != int or type(b) != int:
        return("ERROR: Tipo de dato incorrecto")
    elif a - b < 0:
        return("ERROR: El resultado no pertenece a los números naturales")
    else:
        return (a - b)
