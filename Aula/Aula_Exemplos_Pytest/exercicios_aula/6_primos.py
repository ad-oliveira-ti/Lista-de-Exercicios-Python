# Faça um algoritmo que receba somente números inteiros, positivos e maiores que zero. O algoritmo deve
# verificar se o número informado é primo ou não.

num = 0.00
continuar = True
while continuar:
    try:
        num = int(input("\nDigite um numero(inteiro > 0): "))
    except ValueError:
       print("Numero invalido. Digite um numero inteiro > 0")
    
    if type(num) == int and num>0:
        div = 0
        for i in range (1, num+1):
            if num % i == 0:
                div += 1
        if div > 2:
            print("\nEsse numero nao eh primo\n")
        else:
            print("\nEsse numero eh primo\n")
    elif num<0: 
        print("\nNumero invalido. Digite um numero inteiro > 0\n")
        num = input("\nDigite um numero(inteiro > 0): ")
    
    cont = True
    while cont:
        c = (input("deseja continuar? [s/n]: "))
        if c == "s":
            continuar = True
            cont = False
        elif c == "n":
            continuar = False
            cont = False
        else:
            print("opcao invalida.")




        
            
