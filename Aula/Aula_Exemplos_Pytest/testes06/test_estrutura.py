from estrutura import verificar_estrutura_listas

def test_sao_iguais():
    assert verificar_estrutura_listas([44,23,2,1,10] , [44,23,2,1,10]) == True
    
def test_sao_diferentes():
    assert verificar_estrutura_listas([44,23,2,1,10] , [44,23]) == False

def test_sao_diferentes_error():
    assert verificar_estrutura_listas([44,23,2,1,10] , [44,23]) == True