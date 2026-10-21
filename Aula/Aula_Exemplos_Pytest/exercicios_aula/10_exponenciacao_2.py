# Faça um algoritmo que recebe 2 valores inteiros (base e expoente), positivos e maiores que zero e que 
# calcula a potência desses valores sem utilizar funções e sem utilizar sinal de multiplicação (*).
# - Verifique se os valores digitados são válidos.

try:
    b = int(input("Digite um número (base): "))
    e = int(input("Digite outro número (expoente): "))
except ValueError:
       print("Numero invalido. Digite um numero inteiro")
       quit()


if isinstance(e, int) and e > 0: 
    if isinstance(b, int) and b > 0: 
        
        r = b
        for i in range(1, e):
            s = 0
            for i in range(1, b+1):
                s += r
            r = s
        print(f"{b} ^ {e} = {r}")

    else:
        print("Segundo numero invalido, Digite um numero positivo.")
else:
    print("Primeiro numero invalido, Digite um numero positivo.")
