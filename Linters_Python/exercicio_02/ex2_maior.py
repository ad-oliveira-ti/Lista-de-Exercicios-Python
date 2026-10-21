def encontrar_maior(numeros):
    """Retorna o maior número da lista, sem usar max()."""
    if len(numeros) == 0:
        raise ValueError("A lista não pode estar vazia.")

    maior = numeros[0]  # começa pelo primeiro (funciona com lista toda negativa)
    for numero in numeros:
        if numero > maior:  # noqa: PLR1730 (o exercício proíbe usar max())
            maior = numero

    return maior
