def contar_vogais(texto):
    """Conta as vogais (a, e, i, o, u), maiúsculas ou minúsculas, sem str.count()."""
    vogais = "aeiouAEIOU"
    quantidade = 0

    for letra in texto:
        if letra in vogais:
            quantidade += 1

    return quantidade
