from personagens.personagem import Personagem

class Monstro(Personagem):
    def __init__(self, nivel, nome, ataque, defesa, vida, precisao, chance_critico, xp, dano_sanidade, fraqueza):
        super().__init__(nome, ataque, defesa, vida, precisao, chance_critico)
        self.xp = xp
        self.nivel = nivel
        self.xp_dropado = xp * nivel
        self.efeitos = []
        self.dano_sanidade = dano_sanidade
        self.fraqueza = fraqueza