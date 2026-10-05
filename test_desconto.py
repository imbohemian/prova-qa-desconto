import pytest

from desconto import calcular_desconto


@pytest.mark.parametrize("valor_compra, esperado", [
    (0, 0),
    (50, 0),
    (99.99, 0),
    (100, 10),
    (300, 30),
    (499.99, 50),
    (500, 100),
    (800, 160),
])
def test_desconto_cliente_comum(valor_compra, esperado):
    assert calcular_desconto(valor_compra, "COMUM") == esperado


@pytest.mark.parametrize("valor_compra, esperado", [
    (50, 2.5),
    (99, 4.95),
    (100, 15),
    (300, 45),
    (499, 74.85),
    (500, 125),
])
def test_desconto_cliente_vip(valor_compra, esperado):
    assert calcular_desconto(valor_compra, "VIP") == esperado


@pytest.mark.parametrize("tipo_cliente", ["vip", "Vip", "vIp"])
def test_vip_em_maiusculo_ou_minusculo(tipo_cliente):
    assert calcular_desconto(300, tipo_cliente) == 45


def test_comum_em_minusculo():
    assert calcular_desconto(300, "comum") == 30


@pytest.mark.parametrize("valor_compra, tipo_cliente", [
    (1000, "COMUM"),
    (1001, "COMUM"),
    (2000, "COMUM"),
    (800, "VIP"),
    (801, "VIP"),
    (5000, "VIP"),
])
def test_teto_de_200_reais(valor_compra, tipo_cliente):
    assert calcular_desconto(valor_compra, tipo_cliente) == 200


@pytest.mark.parametrize("valor_compra", [-1, -100, "abc", None])
def test_valor_da_compra_invalido(valor_compra):
    with pytest.raises(ValueError, match="Valor da compra inválido"):
        calcular_desconto(valor_compra, "VIP")


@pytest.mark.parametrize("tipo_cliente", ["GOLD", "", None, 123])
def test_tipo_de_cliente_invalido(tipo_cliente):
    with pytest.raises(ValueError, match="Tipo de cliente inválido"):
        calcular_desconto(300, tipo_cliente)
