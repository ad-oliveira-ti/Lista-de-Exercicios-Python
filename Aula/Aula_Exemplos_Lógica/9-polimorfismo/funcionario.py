
#######################################################
#                  POLIMORFISMO                       #
#                                                     #
# Polimorfismo é o princípio pelo qual duas ou        #
# mais classes derivadas da mesma superclasse         #
# podem invocar métodos que têm a mesma assinatura,   #
# mas comportamentos distintos.                       #                                  #
#######################################################

from pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, nome, endereco,  cargo, matricula, senha, salario):
        super().__init__(nome,  endereco)
        self._cargo = cargo
        self._matricula = matricula
        self._senha = senha
        self._salario = salario

    def calcular_gratificacao(self):
        return self._salario * 1.15
