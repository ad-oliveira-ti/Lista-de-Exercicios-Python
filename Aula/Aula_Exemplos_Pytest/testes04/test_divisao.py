from divisao import divisao

def test_divisao_resultado_inteiro():
    assert divisao(6 , 2) ==  3

def test_divisao_resultado_decimal():
    assert divisao(5, 2) == 2.5

def test_divisao_dividendo_maior():
    assert divisao(2 , 6) ==  0.3333333333333333

# def test_divisao_dividendo_maior_error():
#     assert divisao(2 , 6) ==  0.4

def test_divisao_zero():
    assert divisao(5, 0) is None

def test_divisao_zero_2():
    assert divisao(0, 5) == 0