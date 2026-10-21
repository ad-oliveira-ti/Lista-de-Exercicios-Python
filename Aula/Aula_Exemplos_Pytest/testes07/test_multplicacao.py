from multplicacao import multiplicar

def test_dois_positivos():
    assert multiplicar(3, 4) == 12

def test_primeiro_negativo():
    assert multiplicar(-3, 4) == -12

def test_segundo_negativo():
    assert multiplicar(3, -4) == -12

def test_dois_negativos():
    assert multiplicar(-3, -4) == 12

def test_primeiro_numero_zero():
    assert multiplicar(0, 4) == 0

def test_segundo_numero_zero():
    assert multiplicar(4, 0) == 0

def test_dois_zeros():
    assert multiplicar(0, 0) == 0

def test_dois_decimal():
    assert multiplicar(2.5, 3.5) == 8.75