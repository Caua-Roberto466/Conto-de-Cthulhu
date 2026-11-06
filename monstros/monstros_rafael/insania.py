from monstros.monstro import Monstro
from interface.cores import cores

class Insania(Monstro):
    def __init__(self, nivel):
        super().__init__(nivel, f"{cores['roxo']}Insânia{cores['limpar']}", 12, 8, 60, 85, 5, 70, 1, "Corpo a Corpo")
        self.drop = []