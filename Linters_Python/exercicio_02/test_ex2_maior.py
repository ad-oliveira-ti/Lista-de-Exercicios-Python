import pytest

from ex2_maior import encontrar_maior


def test_numeros_positivos():
    assert encontrar_maior([3, 7, 2, 9, 5]) == 9


def test_numeros_negativos():
    assert encontrar_maior([-8, -3, -10]) == -3


def test_numeros_repetidos():
    assert encontrar_maior([4, 9, 9, 1, 4]) == 9


def test_lista_vazia():
    with pytest.raises(ValueError):
        encontrar_maior([])


# Casos da inspeção de código
def test_primeiro_ja_e_o_maior():
    assert encontrar_maior([10, 2, 5]) == 10


def test_todos_negativos_nao_retorna_zero():
    assert encontrar_maior([-5, -2, -9]) == -2
