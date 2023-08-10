
from exercicio2 import calcular_total_pedido
def test_calcular_total_pedido():
    total = calcular_total_pedido([100, 101, 102])
    assert total == 32.00

    total = calcular_total_pedido([999, 201])
    assert total == 4.00

    total = calcular_total_pedido([])
    assert total == 0.00
