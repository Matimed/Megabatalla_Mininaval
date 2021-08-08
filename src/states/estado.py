class Estado:
    """ Una etapa definida que transitan los jugadores
        a lo largo de la partida.
    """
    controlador_estados = None

    def actualizar(self):
        """ Muestra los cambios en la interfaz gráfica
            y realiza las tareas que conciernen a ese estado particular.
        """

        raise NotImplementedError


    def finalizar(self):
        """ Le avisa al controlador de estados
            cuando se terminan todas las tareas pertinentes al estado.
        """

        raise NotImplementedError