# 5- Escreva um algoritmo que leia um número n (número de termos de uma progressão aritmética), 
# a1 ( o primeiro termo da progressão) e r (a razão da progressão) e escreva os n termos dessa progressão, 
# bem como a soma dos elementos.

def progressao_aritmetica():
    n = int(input("\nEscreva o número de termos para a progressão aritmética: "))
    a1 = int(input("\nEscreva o primeiro termo da progressão aritmética: "))
    r = int(input("\nEscreva a razão da progressão: "))
    
    pa = [a1]
    n1 = a1
    n2 = a1

    for i in range(1, n):
        n1 += r
        n2 += n1
        pa.append(n1)

    print("\n-----------------------------\n")
    print(f"\nProgressão Aritmética = {pa}")
    print(f"\nSoma dos Números da Sequência = {n2}\n")

progressao_aritmetica()
