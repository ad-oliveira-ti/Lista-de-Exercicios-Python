from pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def __init__(self, nome, endereco,  cnpj , ano_fundacao):
        super().__init__(nome,  endereco)
        self._cnpj = cnpj
        self._ano_fundacao = ano_fundacao