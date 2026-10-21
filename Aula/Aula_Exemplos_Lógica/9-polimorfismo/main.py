from gerente import Gerente
from funcionario import Funcionario

def main():
    f1 = Funcionario('Antonio','Rua Tal 1','Professor',1233,'Senha123456',1000)
    g1 = Gerente('Luiz','Rua Tal 2','Coordenador',4321,'Senha123456',1000, 30, 'Mandar nos outros')
    print(f1._salario)
    print(f1.calcular_gratificacao())
    print(g1.calcular_gratificacao())
    
if __name__ == "__main__": 
    main()

