class NotEnoughtBoatsError(Exception):
    def __init__(self, msg = "No se hayan mas barcos disponibles"):
        super().__init__(msg)