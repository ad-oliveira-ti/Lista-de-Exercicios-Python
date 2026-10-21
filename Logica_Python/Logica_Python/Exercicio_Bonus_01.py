# Bônus- Faça um algoritmo que liste todos os números primos possíveis até um número definido pelo usuário. 
# O número deve ser inteiro, positivo e maior que 0.


def detectar_primo():
    while True:
        print("\nDigite 0 para parar o sistema.")
        numero = int(input("Escreva um número, será listado todos os números primos no caminho até chegar nesse número. \n"))
        limite = numero
        primos = []
        
        if numero < 0:
            print("Número inválido. Ele precisa ser maior que zero.")
        
        elif numero == 0:
            print("Encerrando sistema.")
            break
        
        if numero == 1:
            print(f"O número {numero} NÃO é primo (primos devem ser maiores que 1).")
        
        else:
            for numero in range(1, limite + 1):

                is_primo = True
                for i in range(2, int(numero ** 0.5) + 1):
                    if numero % i == 0:
                        is_primo = False
                        break
            
                if is_primo:
                    primos.append(numero)
        
            print(f"Números primos até {limite}: {primos}")
            
detectar_primo()

