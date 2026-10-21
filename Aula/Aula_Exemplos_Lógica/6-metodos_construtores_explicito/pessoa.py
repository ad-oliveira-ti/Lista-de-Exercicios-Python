class Pessoa():
    
    def __init__(self, nome, endereco):
        self._nome = nome 
        self._endereco = endereco 

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome




