#10. Faça um algoritmo que recebe 2 valores inteiros (base e expoente), 
# positivos e maiores que zero e que calcula a potência desses valores sem utilizar funções e sem utilizar sinal de multiplicação (*). 
# - Verifique se os valores digitados são válidos.

base = int(input("Digite um número (base): "))
expoente = int(input("Digite outro número (expoente): "))

while base <= 0 or expoente <= 0:
    print("Os valores devem ser positivos e maiores que zero.")
    base = int(input("Digite um número (base): "))
    expoente = int(input("Digite outro número (expoente): "))

resultado = base

for _ in range(expoente - 1):
    soma = 0
    for _ in range(base):
        soma += resultado
    resultado = soma

print(f"{base} ^ {expoente} = {resultado}")