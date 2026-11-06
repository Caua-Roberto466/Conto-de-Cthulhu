from monstros.monstro import Monstro
from interface.cores import cores

class Enfermeiro_Possuido(Monstro):
    def __init__(self, nivel):
        super().__init__(nivel, f"{cores['vermelho']}Paciente Alucinado{cores['limpar']}", 15, 10, 70, 80, 10, 90, 0, "Corpo a Corpo")
        self.drop = []