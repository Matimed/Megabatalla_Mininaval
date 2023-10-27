class CellFullError(Exception):
    def __init__(self, msg = "Ya existe un bote en la celda consultada"):
        super().__init__(msg)