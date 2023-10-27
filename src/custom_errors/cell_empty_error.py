class CellEmptyError(Exception):
    def __init__(self, msg = "No existe un bote en la celda consultada"):
        super().__init__(msg)