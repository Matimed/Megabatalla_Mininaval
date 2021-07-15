class CellFullError(Exception):
    def __init__(self, msg = "Ya existe un barco en la celda consultada"):
        super().__init__(msg)