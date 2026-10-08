# 6- Faça um algoritmo que receba somente números inteiros, positivos e maiores que zero. O algoritmo deve verificar se o número informado é primo ou não.
def detectar_primo():
    while True:
        print("\nDigite 0 para parar o sistema.")
        numero = int(input("Escreva um número para verificar se ele é primo. \n"))
        
        if numero < 0:
            print("Número inválido. Ele precisa ser maior que zero.")
        
        elif numero == 0:
            print("Encerrando sistema.")
            break
        
        if numero == 1:
            print(f"O número {numero} NÃO é primo (primos devem ser maiores que 1).")
        
        else:
            is_primo = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    is_primo = False
                    break
            
            if is_primo:
                print(f"O número {numero} É primo!")
            else:
                print(f"O número {numero} NÃO é primo.")

        
detectar_primo()
