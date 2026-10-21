# Faça um algoritmo que recebe uma quantidade de números definida pelo usuário e faz as seguintes verificações:
# - Verifique quantos desses números são primos e maiores que 1000.
# - Verifica qual o maior e menor número primo digitado pelo usuário.
# - Faz a média aritmética dos números primos encontrados.
quant = int(input("\nQuantos números deseja inserir? "))
num = int(input("\nDigite um numero(inteiro, >0): "))
maior = menor = num
soma = 0
primil = []
for i in range (0, quant-1):
    num = int(input("\nDigite um numero(inteiro, >0): "))
    div = 0
    for i in range (1, num+1):
        if num % i == 0:
            div += 1
    if div <= 2:
        if num > maior: maior = num 
        if num < menor: menor = num
        if num > 1000: primil.append(num)
        soma += num
med = soma / quant

print(f"Maior primo: {maior}\nMenor primo: {menor}\nPrimos maiores de mil: {primil}\nMédia dos primos: {med:.2f}")