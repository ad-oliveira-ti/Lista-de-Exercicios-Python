from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, nome, endereco, cargo, matricula, senha, salario, quantidade_funcionarios,atribuicao_funcao):
        super().__init__(nome,  endereco, cargo, matricula, senha, salario)
        self._quantidade_funcionarios = quantidade_funcionarios
        self._atribuicao_funcao = atribuicao_funcao

    def calcular_gratificacao(self):
        return super().calcular_gratificacao() * 1.2

