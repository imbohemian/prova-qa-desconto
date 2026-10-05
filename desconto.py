def calcular_desconto(valor_compra, tipo_cliente):
    if not isinstance(valor_compra, (int, float)) or valor_compra < 0:
        raise ValueError("Valor da compra inválido")

    if not isinstance(tipo_cliente, str) or tipo_cliente.upper() not in ("VIP", "COMUM"):
        raise ValueError("Tipo de cliente inválido")

    desconto = 0

    if valor_compra >= 100 and valor_compra < 500:
        desconto = 0.10
    elif valor_compra >= 500:
        desconto = 0.20

    if tipo_cliente.upper() == "VIP":
        desconto += 0.05

    valor_desconto = valor_compra * desconto

    if valor_desconto > 200:
        valor_desconto = 200

    return round(valor_desconto, 2)