class ContaCorrente:
    
    def __init__(self, numero_cc, saldo, pessoa, agencia, categoria):
        self._numero_cc = numero_cc
        self._saldo = saldo 
        self._pessoa = pessoa
        self._agencia = agencia
        self._categoria = categoria

    # Definindo getters e setters da forma incorreta, 
    # comparando com outras lingaugens de programacao:
    
    #def get_saldo(self):
    #        return self._saldo
    
    #def set_saldo(self, saldo):
    #    self._saldo = saldo
    
    def __str__(self):
        return 'Concatenando %s texto %s' % (self._numero_cc , self._saldo)  
