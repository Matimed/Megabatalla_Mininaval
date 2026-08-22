import pygame


class Temporizador:
    """ Mide un plazo sin bloquear el hilo principal.

        pygame.time.wait() detiene todo hasta que el plazo se cumple. En
        el navegador eso congela la pestaña entera, porque el bucle nunca
        le devuelve el control. Aca en cambio se anota el instante de
        vencimiento y se lo consulta una vez por frame, asi el juego
        sigue dibujandose mientras espera.
    """

    def __init__(self):
        self._vencimiento = None
        self._accion = None


    def programar(self, milisegundos, accion = None):
        """ Arranca la cuenta.

            Recibe:
                milisegundos:<int> cuanto dura el plazo.
                accion:<callable> opcional, se ejecuta al vencer.
        """

        self._vencimiento = pygame.time.get_ticks() + milisegundos
        self._accion = accion


    def corriendo(self):
        """ Devuelve True mientras el plazo no se haya cumplido."""

        if self._vencimiento is None:
            return False

        if pygame.time.get_ticks() < self._vencimiento:
            return True

        self._vencimiento = None
        return False


    def actualizar(self):
        """ Ejecuta la accion pendiente si ya se cumplio el plazo.

            Hay que llamarlo una vez por frame.
        """

        if self._accion is None or self.corriendo():
            return

        accion, self._accion = self._accion, None
        accion()
