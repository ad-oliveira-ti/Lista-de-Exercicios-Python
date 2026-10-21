# Faça um algoritmo que receba 90000 números inteiros e verifique qual deles foi o menor e maior digitado.
import random

num = random.randint(0, 1000000)
maior = num
menor = num
print(num)
for i in range (1, 90000):
    if num > maior: maior = num 
    if num < menor: menor = num
    num = random.randint(0, 1000000)
    print(num)

print("\n-----------------------------\n")
print(f"Maior numero sorteado: {maior}")
print(f"Menor numero sorteado: {menor}")