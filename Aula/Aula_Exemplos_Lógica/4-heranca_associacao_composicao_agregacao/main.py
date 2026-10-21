from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica
from pessoa import Pessoa
from categoria import Categoria
from conta_corrente import ContaCorrente
from agencia import Agencia

def main():
    ag1 = Agencia('0001', '(51)8888', 'Rua tal 1',)
    ag2 = Agencia('0002', '(51)9999', 'Rua tal 2',)
    cat1 = Categoria('Top', 10000.00, 'Super Conta')
    cat2 = Categoria('Media', 5000.00, 'Conta Poupanca')
    cat3 = Categoria('Comun', 100.00, 'Conta Universitaria')
    p1 = Pessoa('Guilherme Silva', 'Rua tal 3')
    p2 = Pessoa('Antonio Silva', 'Rua tal 4')
    cc1 = ContaCorrente('1111', 0, p1, ag2, cat2)
    print(cc1)
    print(cc1._numero_cc)
    print(cc1._saldo)
    print(cc1._pessoa)
    print(cc1._pessoa._nome)
    print(cc1._categoria._descricao)

if __name__ == "__main__": 
    main()






    
    # pf1 = PessoaFisica('Antonio Leaes','rua tal 1', 1111111, '11/11/2011') 
    # pf2 = PessoaFisica('Luiz Leaes','rua tal 2', 222222, '22/02/2022') 
    # c1 = Categoria('Minha categoria1 ', 1000.08 ,'Classe ouro')
    # c2 = Categoria('Minha categoria 2', 2000.04 ,'Classe prata')
    # c3 = Categoria('Minha categoria 3', 3000.43 ,'Classe bronze')
    # a1 = Agencia(11, 99999, 'Endereco TAl 1')
    # a2 = Agencia(12, 88888, 'Endereco TAl 2')
    # cc1 = ContaCorrente(1111, 2500.23, pf1, a1, c2)
    # cc2 = ContaCorrente(2222, 3000.00, pf2, a1, c1)
    # print(cc1)