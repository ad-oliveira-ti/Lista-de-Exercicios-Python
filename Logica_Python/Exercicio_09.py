#9. Faça um algoritmo que recebe 2 valores inteiros (base e expoente), positivos e maiores que zero e que calcula a potência desses valores sem utilizar funções, 
# utilize * para fazer o cálculo.- Verifique se os valores digitados são válidos.

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

while base <= 0 or expoente <= 0:
    print("Os valores devem ser positivos e maiores que zero.")
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))

resultado = 1
for _ in range(expoente):
    resultado *= base

print(f"\nO resultado da potência é: {resultado}")