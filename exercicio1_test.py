import pytest
from exercicio1 import exercisio_para_teste

def test_exercicio1_entre_10_e_99():
    valor = exercisio_para_teste(1, 10)
    assert valor == (10, 9.5)

def test_exercicio1_entre_100_e_999():
    Valor = exercisio_para_teste(1, 100)
    assert Valor == (100, 90)

def test_exercicio1_maior_que_999():
    Valor = exercisio_para_teste(1, 1000)
    assert Valor == (1000, 850)

    