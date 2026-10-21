#1. Faça um algoritmo que calcule a multiplicação entre dois números sem utilizar o sinal de multiplicação ( * ) ou função. Utilize estrutura de repetição e soma.
def multiplicar(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

multiplicando = int(input("Digite o primeiro número: "))
multiplicador = int(input("Digite o segundo número: "))

resultado_final = multiplicar(multiplicando, multiplicador)
print(f"O resultado é: {resultado_final}")
