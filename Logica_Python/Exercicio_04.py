#4. Faça um algoritmo que receba 90000 números inteiros e verifique qual deles foi o menor e maior digitado. 
import random

def calcular_maior_menor():
    numero = random.randint(0, 100000000000)
    maior = numero
    menor = numero
    print(numero)
    for i in range (1, 90000):
        if numero > maior: maior = numero
        if numero < menor: menor = numero
        numero = random.randint(0, 100000000000)
        print(numero)

    return maior, menor

def exibir_resultado(maior, menor):
    print("\n-----------------------------\n")
    print(f"Maior numero sorteado: {maior}")
    print(f"Menor numero sorteado: {menor}")
    

maior_valor, menor_valor = calcular_maior_menor()
exibir_resultado(maior_valor, menor_valor)
