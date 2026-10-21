
minutos = int(input("Quantos minutos você utilizou este mês:"))

if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15


print(f"Você vai pagar este mês: R${minutos * preço:6.2f}")
