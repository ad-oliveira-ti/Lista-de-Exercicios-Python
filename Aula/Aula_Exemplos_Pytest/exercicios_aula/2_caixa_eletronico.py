# Faça um algoritmo com as funções de um caixa eletrônico. Utilize estrutura de repetição. 
# - Deve apresentar um menu:
# 1 - Saldo
# 2 - Saque
# 3 - Depósito
# 4 - Sair
# - O algoritmo deve executar as operações de um cliente até que ele digite a opção 4- Sair.
# - Caso o cliente digite uma opção que não exista informe "Opção inválida".
# - Algoritmo deve operar as quatro funções do caixa eletrônico.
# - O Saldo inicial é igual a 0,00.
# - Caso o usuário tente sacar um valor maior que o saldo disponível o programa deve apresentar a mensagem 
# "Saldo insuficiente".
# - No final de cada operação o saldo deve ser apresentado.

saldo = 0
opcao = 0

while opcao != 4:
    opcao = int(input("1 - Depositar\n2 - Sacar\n3 - Saldo\n4 - Sair\n\nEscolher: "))
    if opcao == 1:
        deposito = int(input("\nQuanto voce quer depositar: "))
        saldo = saldo + deposito
        print(f"\nSeu deposito foi um sucesso!\nSaldo Atual: {saldo} \n")
    elif opcao == 2:
        saque = int(input("\nQuanto voce quer sacar: "))
        if saldo > saque:
            saldo = saldo - saque
            print(f"\nSeu saque foi um sucesso!\nSaldo Atual: {saldo} \n")
        else:
            print(f"\nSaldo insuficiente.\nSaldo atual: {saldo} \n")
    elif opcao == 3:
        print(f"\nSaldo atual: {saldo} \n")
    elif opcao == 4: 
        print("\nSaindo! Volte sempre! \n")
    else: 
        print("\nOpção inválida. \n") 





