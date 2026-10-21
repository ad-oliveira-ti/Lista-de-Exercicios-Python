class Pessoa:
    
    def __init__(self, nome, endereco):
        self._nome = nome 
        self._endereco = endereco 

    def __str__(self):
         return self.__class__.__name__