from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica
from categoria import Categoria
from conta_corrente import ContaCorrente
from agencia import Agencia


def main():
    pf1 = PessoaFisica('Antonio Leaes','rua tal 1', 1111111, '11/11/2011') 
    pf2 = PessoaFisica('Luiz Leaes','rua tal 2', 222222, '22/02/2022') 
    c1 = Categoria('Minha categoria1 ', 1000.08 ,'Classe ouro')
    c2 = Categoria('Minha categoria 2', 2000.04 ,'Classe prata')
    c3 = Categoria('Minha categoria 3', 3000.43 ,'Classe bronze')
    a1 = Agencia(11, 99999, 'Endereco TAl 1')
    a2 = Agencia(12, 88888, 'Endereco TAl 2')
    cc1 = ContaCorrente(1111, 2500.23, pf1, a1, c2)
    cc2 = ContaCorrente(2222, 3000.00, pf2, a1, c1)
    cod1 = ContaCorrente.codigos_bancos() # Metodo estatico sendo instaciado
    print(cc1._codigo_banco) # Atributo estatico
    print(cod1)
    print(cod1['Banco do Brasil'])
    print(cod1['Banrisul'])
    
if __name__ == "__main__": 
    main()

