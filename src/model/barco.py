class Barco:
    def __init__(self):
        self.hundido = False

    def hundir(self):
        self.hundido = True

    def get_hundido(self):
        return self.hundido
    
    