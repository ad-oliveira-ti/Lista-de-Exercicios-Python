
##########################################
#          CLASSES ABSTRATAS             #
#                                        #
#   É um tipo de classe especial que não #
# pode ser instanciada, apenas herdada.  #
# Sendo assim, uma classe abstrata não   #
# pode ter um objeto criado a partir de  #
# sua instanciação.                      #
##########################################

from abc import ABC, abstractmethod
 
class Veiculo(ABC):

    @abstractmethod
    def qtda_rodas(self):
        pass

