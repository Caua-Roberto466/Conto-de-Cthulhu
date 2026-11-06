from monstros.monstro import Monstro
from interface.cores import cores

class Paciente_Alucinado(Monstro):
    def __init__(self, nivel):
        super().__init__(nivel, f"{cores['amarelo']}Paciente Alucinado{cores['limpar']}", 8, 5, 35, 80, 5, 60, 0, "Corpo a Corpo")
        self.drop = []