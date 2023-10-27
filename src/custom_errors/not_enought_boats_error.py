class NotEnoughtBoatsError(Exception):
    def __init__(self, msg = "No se hayan mas botes disponibles"):
        super().__init__(msg)