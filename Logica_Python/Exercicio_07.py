# 7. Faça um algoritmo que recebe uma quantidade de números definida pelo usuário e faz as seguintes verificações:
# - Verifique quantos desses números são primos e maiores que 1000.
# - Verifica qual o maior e menor número primo digitado pelo usuário.
# - Faz a média aritmética dos números primos encontrados.

def listar_primos():
    while True:
        print("\n--- Sistema de Números Primos ---")
        quantidade = int(input("Quantos números serão inseridos? (Digite 0 para sair): "))
        
        if quantidade == 0:
            print("Encerrando sistema.")
            break
        
        primos = []
        
        for _ in range(quantidade):
            numero = int(input("Digite um número inteiro maior que 1: "))
            
            while numero <= 1:
                print("Número inválido. Ele precisa ser maior que 1.")
                numero = int(input("Digite um número inteiro maior que 1: "))
            
            is_primo = True
            for i in range(2, int(numero ** 0.5) + 1):
                if numero % i == 0:
                    is_primo = False
                    break
            
            if is_primo:
                primos.append(numero)
        
        mostrar_resultados(primos)

def mostrar_resultados(primos):
    if primos == []:
        print("\nNenhum número primo foi informado.")
        return
    
    maiores_que_1000 = 0
    soma = 0
    quantidade_primos = 0
    
    maior = primos[0]
    menor = primos[0]
    
    for p in primos:
        quantidade_primos += 1 
        soma += p
        
        if p > 1000:
            maiores_que_1000 += 1
            
        if p > maior:
            maior = p
        if p < menor:
            menor = p
    
    media = soma / quantidade_primos
    
    print("\n--- Resultados ---")
    print(f"Primos encontrados: {primos}")
    print(f"Quantidade de primos maiores que 1000: {maiores_que_1000}")
    print(f"Maior número primo: {maior}")
    print(f"Menor número primo: {menor}")
    print(f"Média aritmética dos primos: {media:.2f}")

listar_primos()