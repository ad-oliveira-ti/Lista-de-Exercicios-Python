from tamanho_lista import calcula_tamanho_lista

def test_calcula_tamanho_lista_1():
    assert calcula_tamanho_lista([1,2,3,4,5]) == 5

def test_calcula_tamanho_lista_2():
    assert calcula_tamanho_lista([2,2,3]) == 3

def test_calcula_tamanho_lista_3():
    assert calcula_tamanho_lista([2,2,3,-3]) == 3

