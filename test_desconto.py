import pytest

from desconto import calcular_desconto


@pytest.mark.parametrize("valor_compra, desconto_esperado", [
    (0, 0),
    (50, 0),
    (99.99, 0),
    (100, 10),
    (100.01, 10),
    (300, 30),
    (499.99, 50),
    (500, 100),
    (500.01, 100),
    (800, 160),
])
def test_desconto_cliente_comum_por_faixa_de_valor(valor_compra, desconto_esperado):
    tipo_cliente = "COMUM"

    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == desconto_esperado


@pytest.mark.parametrize("valor_compra, desconto_esperado", [
    (50, 2.5),
    (99, 4.95),
    (100, 15),
    (100.01, 15),
    (300, 45),
    (499, 74.85),
    (500, 125),
    (500.01, 125),
])
def test_desconto_cliente_vip_por_faixa_de_valor(valor_compra, desconto_esperado):
    tipo_cliente = "VIP"

    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == desconto_esperado


@pytest.mark.parametrize("tipo_cliente", ["vip", "Vip", "vIp"])
def test_vip_escrito_em_maiusculo_ou_minusculo_recebe_5_por_cento_extra(tipo_cliente):
    valor_compra = 300

    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == 45


def test_comum_escrito_em_minusculo_nao_recebe_acrescimo():
    valor_compra = 300
    tipo_cliente = "comum"

    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == 30


@pytest.mark.parametrize("valor_compra, tipo_cliente, desconto_esperado", [
    (999, "COMUM", 199.8),
    (1000, "COMUM", 200),
    (1001, "COMUM", 200),
    (2000, "COMUM", 200),
    (799, "VIP", 199.75),
    (800, "VIP", 200),
    (801, "VIP", 200),
    (5000, "VIP", 200),
])
def test_desconto_nao_ultrapassa_teto_de_200_reais(valor_compra, tipo_cliente, desconto_esperado):
    resultado = calcular_desconto(valor_compra, tipo_cliente)

    assert resultado == desconto_esperado


@pytest.mark.parametrize("valor_compra", [-1, -100, "abc", None])
def test_valor_da_compra_invalido_lanca_erro(valor_compra):
    tipo_cliente = "VIP"

    with pytest.raises(ValueError, match="Valor da compra inválido"):
        calcular_desconto(valor_compra, tipo_cliente)


@pytest.mark.parametrize("tipo_cliente", ["GOLD", "", None, 123])
def test_tipo_de_cliente_invalido_lanca_erro(tipo_cliente):
    valor_compra = 300

    with pytest.raises(ValueError, match="Tipo de cliente inválido"):
        calcular_desconto(valor_compra, tipo_cliente)