from sys import set_asyncgen_hooks
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
    cc1 = ContaCorrente('1111', 140, p1, ag2, cat2)

    print(p1.nome)
    p1.nome = 'antonio'
    print(p1.nome)


if __name__ == "__main__": 
    main()
    
