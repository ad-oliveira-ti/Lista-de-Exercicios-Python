# 8. Faça um algoritmo que recebe 2 valores inteiros (x e x), positivos e maiores que zero e que calcula a multiplicação desses valores 
# sem utilizar funções, utilize + para fazer o cálculo.

multiplicando = int(input("Digite o primeiro número: "))
multiplicador = int(input("Digite o segundo número: "))

while multiplicando <= 0 or multiplicador <= 0:
    print("Os valores devem ser positivos e maiores que zero.")
    multiplicando = int(input("Digite o primeiro número: "))
    multiplicador = int(input("Digite o segundo número: "))
    
resultado = 0
for _ in range(multiplicador):
    resultado += multiplicando
    
print(f"\nO resultado da multiplicação é: {resultado}")