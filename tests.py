
from funciones import F1, F2, F3


def test_1():

    assert F1('micros') == 'MICROS'
    assert F2('while')
    assert F3(5, 2) == 3


def test_2():

    assert F1(123) == "ERROR: Tipo de dato incorrecto"
    assert F2(456) == "ERROR: Tipo de dato incorrecto"


def test_3():

    assert F3(5, 6) == "ERROR: Número no natural"
