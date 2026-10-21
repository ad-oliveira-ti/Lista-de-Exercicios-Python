import pytest

from ex1_total import calcular_total


def test_varios_precos_sem_desconto():
    assert calcular_total([10, 20, 30], 0) == 60


def test_compra_com_desconto():
    assert calcular_total([50, 50], 10) == 90


def test_lista_vazia():
    assert calcular_total([], 0) == 0


def test_desconto_abaixo_de_zero():
    with pytest.raises(ValueError):
        calcular_total([10], -1)


def test_desconto_acima_de_cem():
    with pytest.raises(ValueError):
        calcular_total([10], 101)
