import random
from interface.cores import cores

class Personagem:
    def __init__(self, nome, ataque, defesa, vida, precisao, chance_critico):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.defesa = defesa
        self.ataque = ataque
        self.precisao = precisao
        self.chance_critico = chance_critico
    
    def critico(self, ataque):
        return ataque * 1.2

    def atacar(self, ataque, defesa, alvo):
        roll_acert = random.randint(1, 100)
        
        if roll_acert <= self.precisao:
            roll_crit = random.randint(1, 100)

            if roll_crit <= self.chance_critico:
                critico = self.critico(ataque)
                dano_final = max(1, critico - (critico * (defesa/100)))
                print(f"\n{self.nome} Acertou o ataque! Casou {cores['vermelho']}{dano_final:.0f}{cores['limpar']} de dano com um acerto crítico em {alvo}")
                return dano_final
            
            else:
                dano_final = max(1, self.ataque - (self.ataque * (defesa/100)))
                print(f"\n{self.nome} Acertou o ataque! Casou {dano_final:.0f} de dano em {alvo}")
                return dano_final
        
        else:
            print(f"\n{self.nome} errou o ataque!")
            return 0
    
    def defender(self):
            self.defesa += 10

#Classe dos heróis
class Herois(Personagem):
    def __init__(self, nome, ataque, defesa, vida, sanidade, energia, precisao, chance_critico,  arma):
        super().__init__(nome, ataque, defesa, vida, precisao, chance_critico)
        self.energia_max = energia
        self.energia = energia
        self.arma = arma
        self.inventario = [arma]
        self.sanidade_max = sanidade
        self.sanidade = sanidade
        self.nivel = 1
        self.xp = 0
        self.xp_prox = 100
        self.defendendo = False
        self.efeitos = []
    
    def status(self):
        print(f"Nome: {self.nome} | Vida: {self.vida}")

    def nivel_up(self):
        self.nivel += 1
        self.xp_prox = int(self.xp_prox * 1.1)
        self.ataque = self.ataque * 1.2
        self.defesa = self.defesa * 1.1
        self.vida_max += 10
        self.vida = self.vida_max
        self.sanidade_max = self.sanidade_max * 1.01
        self.sanidade = self.sanidade_max
        self.energia = self.energia * 1.10
        print(f"{self.nome} subiu para o nível {self.nivel}")

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        if self.xp >= self.xp_prox:
            self.xp = self.xp - self.xp_prox
            self.nivel_up()

    def defender(self):
        self.defendendo = True
        self.defesa += 10

    def passiva(self, evento, dados):
        #O herói sobrescreve
        pass

    def ativa(self):
        #O herói sobrescreve
        pass

class Habilidade:
    def __init__(self, nome, descricao, custo):
        self.nome = nome
        self.descricao = descricao
        self.custo = custo
        self.necessita_alvo = False
        self.area = False

    def usar(self, precisao, chance_critico, usuario, alvo=None):
        #A habilidade 
        pass