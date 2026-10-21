def calcular_total(precos, desconto):
    """Soma os preços com um laço e aplica o desconto percentual (0 a 100)."""
    if desconto < 0 or desconto > 100:
        raise ValueError("O desconto deve estar entre 0 e 100.")

    total = 0
    for preco in precos:
        total += preco

    return total * (100 - desconto) / 100
