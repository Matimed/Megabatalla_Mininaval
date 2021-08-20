from aenum import Enum
from functools import singledispatchmethod


class Evento(Enum):
    """ Enumeracion de tipos de eventos 
        que permite documentar los argumentos que recibe"""
    
    
    def __init__(self, valor, *args):
        """ Cumple la funcion de separar el valor del evento 
            y la documentacion del mismo."""

        self.valor = valor
        if args:
            self.__doc__ = "Argumentos:"
            for arg in args:
                self.__doc__ += f" {arg},"
            self.__doc__ = self.__doc__[:-1]
        else:
            self.__doc__ = "No recibe argumentos"


    @singledispatchmethod
    def __eq__(self, other):
        """Compara dos eventos"""

        try:    return self.valor == other.valor
        except AttributeError:  raise NotImplementedError()


    @__eq__.register(int)
    def _(self, other):
        """Compara el evento con un int"""
        
        return self.valor == other

   
    


