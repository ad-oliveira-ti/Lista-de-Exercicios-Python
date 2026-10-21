# Faça um algoritmo que recebe 2 valores inteiros (base e expoente), positivos e maiores que zero e que 
# calcula a potência desses valores sem utilizar funções, utilize * para fazer o cálculo.
# - Verifique se os valores digitados são válidos.

e = 0
b = 0
try:
    b = int(input("Digite um número (base): "))
    e = int(input("Digite outro número (expoente): "))
except ValueError:
       print("Numero invalido. Digite um numero inteiro")
       quit()
r = b
if isinstance(e, int) and e > 0: 
    if isinstance(b, int) and b > 0: 
        for i in range(1, e):
            r *= b
        print(f"{b} ^ {e} = {r}")
    else:
        print("Segundo numero invalido, Digite um numero positivo.")
else:
    print("Primeiro numero invalido, Digite um numero positivo.")
