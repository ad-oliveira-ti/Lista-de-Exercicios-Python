from ex3_vogais import contar_vogais


def test_minusculas():
    assert contar_vogais("banana") == 3


def test_maiusculas():
    assert contar_vogais("ABELHA") == 3


def test_sem_vogais():
    assert contar_vogais("xyz bcd") == 0


def test_vazio():
    assert contar_vogais("") == 0


# Casos da inspeção de código
def test_cada_ocorrencia_conta_uma_vez():
    assert contar_vogais("aaa") == 3


def test_nao_conta_consoantes():
    assert contar_vogais("bcdfg") == 0
