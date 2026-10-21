# Faça um algoritmo que recebe 2 valores inteiros (x e x), positivos e maiores que zero e que calcula a 
# multiplicação desses valores sem utilizar funções, utilize + para fazer o cálculo.
# - Verifique se os valores digitados são válidos.
n = m = r = 0
try:
    n = int(input("Digite um número: "))
    m = int(input("Digite outro número: "))
except ValueError:
       print("Numero invalido. Digite um numero inteiro")
       quit()

if isinstance(n, int) and n > 0: 
    if isinstance(m, int) and m > 0: 
        for i in range(1, m):
            r += n
        print(f"{n} * {m} = {r}")
    else:
        print("Segundo numero invalido, Digite um numero positivo.")
else:
    print("Primeiro numero invalido, Digite um numero positivo.")

