#2. Faça um algoritmo com as funções de um caixa eletrônico. Utilize estrutura de repetição. 
# - Deve apresentar um menu:
# 1 - Saldo
# 2 - Saque
# 3 - Depósito
# 4 - Sair
# - O algoritmo deve executar as operações de um cliente até que ele digite a opção 4- Sair.
# - Caso o cliente digite uma opção que não exista informe "Opção invalida".
# - Algoritmo deve operar as quatro funções do caixa eletrônico.
# - O Saldo inicial é igual a 0,00.
# - Caso o usuário tente sacar um valor maior que o saldo disponível o programa deve apresentar a mensagem "Saldo insuficiente".
# - No final de cada operação o saldo deve ser apresentado.

def exibir_menu():
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Depósito")
    print("4 - Sair")

def caixa_eletronico():
    saldo = 0.00

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
           print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "2":
            valor_saque = float(input("\nDigite o valor de saque: "))
            if valor_saque > saldo:
                print("Saldo insuficiente.")
            elif valor_saque <= 0:
                print("Valor inválido para saque.")
            else:
                saldo -= valor_saque
                print(f"Saque realizado com sucesso.")
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "3":
            valor_deposito = float(input("\nDigite o valor de depósito: "))
            if valor_deposito < 0:
                print("Valor inválido para o depósito.")
            else:
                saldo += valor_deposito
                print(f"Depósito realizado com sucesso.")
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == "4":
            print(f"Até a próxima.")
            break

        else:
            print(f"Opção inválida.")

caixa_eletronico()