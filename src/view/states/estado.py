from src.view.ventana import Ventana


class Estado:
    ventana = Ventana()
    ventana_sur = ventana.get_surface()

    def __init__(self):
        self.nombre = ''
        
        
    def actualizar(self, eventos):
        """ Recibe una lista de eventos y decide como interpretar
            cada uno."""

        raise NotImplementedError()


    def representar(self):
        """ Dibuja todos los sprites que contiene."""

        raise NotImplementedError()