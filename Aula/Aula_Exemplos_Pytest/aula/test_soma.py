from soma import somar

def test_soma_inteiros_positivos_iguais():
    assert somar(5,5) == 10

def test_soma_inteiros_positivos_diferentes():
    assert somar(1,9) == 10

def test_soma_inteiros_negativos_diferentes():
    assert somar(-2,-15) == -17

def test_soma_zero_negativos():
    assert somar(0,-20) == -20