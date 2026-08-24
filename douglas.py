from personagens.personagem import Herois
from personagens.personagem import Habilidade
import random
from interface.cores import cores

class Investigador(Herois):
    def __init__(self):
        super().__init__("Douglas", 17, 7, 90, 95, 60, 100, 15, "Revolver Werbly")
        self.desc = "Investiga pistas por Londres, que já capturou diversos criminosos. Ataca com seu revolver Webley."
        self.passiva_desc = "Instinto de Londres: Elimina a chance de errar seus ataques."
        self.habilidades = [Investigar()]
        self.cor = 'verde'

class Investigar(Habilidade):
    def __init__(self):
        super().__init__("Investigar", "Investiga o inimigo e descobre sua fraqueza", 10)
        self.necessita_alvo = True
        self.area = False
    
    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)

        if roll <= precisao:
            print(f"\nA fraqueza de {alvo.nome} é {cores['vermelho']}{alvo.fraqueza}{cores['limpar']}")

        else:
            print(f"\n{usuario.nome} não conseguiu investigar {alvo.nome}")

class Coronhada(Habilidade):
    def __init__(self):
        super().__init__("Coronhada", "Bata com a parte de trás da arma na cabeça do inimigo, alta chance de crítico", 25)
        self.necessita_alvo = True
        self.area = False
        
    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            roll_crt = random.randint(1,100)
            dano = (usuario.ataque + usuario.nivel) * 1.2

        else:
            print(f"{usuario.nome} errou a coronhada e acertou a parede")

class TiroDuplo(Habilidade):
    pass