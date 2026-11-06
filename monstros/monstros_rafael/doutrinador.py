from monstros.monstro import Monstro

class Doutrinador(Monstro):
    def __init__(self, nivel):
        super().__init__(nivel,"\033[94mDoutrinador\033[0m", 10, 6, 80, 95, 10, 40, 0, 'Intimidação')
        self.drops = ['Livro Dos Virgens']