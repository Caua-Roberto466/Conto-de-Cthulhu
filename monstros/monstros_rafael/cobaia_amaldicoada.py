from monstros.monstro import Monstro
from interface.cores import cores

class Cobaia_Amaldicoada(Monstro):
    def __init__(self, nivel):
        super().__init__(nivel, f"{cores['vermelho_escuro']}Paciente Alucinado{cores['limpar']}", 35, 20, 150, 90, 15, 200, 0, "Corpo a Corpo")
        self.drop = []