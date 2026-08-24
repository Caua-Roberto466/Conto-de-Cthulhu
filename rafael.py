from personagens.personagem import Herois
from personagens.personagem import Habilidade
import random


class Alienista(Herois):
    def __init__(self):
        super().__init__("Rafael", 10, 6, 85, 120, 50, 90, 10, "Equipamentos Médicos")
        self.classe = "Alienista"
        
        self.desc = "Médico do hospício, tem uma mente forte contra todo o horror da vida e tem experiência com loucos. Ataca com seus equipamentos médicos."
        
        self.passiva_desc = "Mente Blindada: Toda vez que ele ou algum membro da equipe perder sanidade vai recuperar 5 dela"

        self.habilidades = [Sedativo(), TerapiaDeChoque(), TrabalhoMental()]
        self.cor = 'amarelo'
        
    
    def passiva(self, evento, dados):
        if evento == "sanidade_perdida":
            alvo = dados['alvo']
            alvo.sanidade = min(alvo.sanidade + 5, alvo.sanidade_max)
            print("5 de sanidade recuperada pela passiva do Rafael")

class Sedativo(Habilidade):
    def __init__(self):
        super().__init__("Sedativo", "Aplica um tranquilizante que diminui os atributos do inimigo", 15)
        self.necessita_alvo = True
        self.area = False
    
    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            alvo.ataque -= 3
            alvo.defesa -= 3
            alvo.efeitos.append({'nome': 'sedativo', 'turno': 3, 'ataque': -3, 'defesa': -3, 'precisao': 0})
            print(f"\n{usuario.nome} aplicou sedativo em {alvo.nome}")
        else:
            print(f"\n{usuario.nome} errou o sedativo")


class TerapiaDeChoque(Habilidade):
    def __init__(self):
        super().__init__("Terapia de Choque", "Descarrega seu aparelho experimental que causa dano elétrico no inimigo", 30)
        self.necessita_alvo = True
        self.area = False
 
    
    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            roll_critico = random.randint(1, 100)
            dano = (usuario.ataque + (usuario.nivel/2)) * 1.2
            
            if roll_critico <= chance_critico:
                dano_critico = usuario.critico(dano)
                dano_final = max(1, dano_critico - (dano_critico * (alvo.defesa / 100)))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com um choque crítico")
            
                alvo.vida = max(0, alvo.vida - dano_final)

            else:
                dano_final = max(1, dano - (dano * (alvo.defesa / 100)))
                alvo.vida = max(0, alvo.vida - dano_final)
                print(f"\n{usuario.nome} causou {dano_final:.0f} em {alvo.nome} com seu aparelho")
            
            if alvo.vida <= 0:
                print(f"\n{usuario.nome} derrotou {alvo.nome} com o choque de seu aparelho")
        else:
            print(f"\n{usuario.nome} errou ao usar seu aparelho")


class TrabalhoMental(Habilidade):
    def __init__(self):
        super().__init__("Trabalho Mental", "Realiza uma terapia para tratar o horror da mente, restaurando totalmente a sua sanidade", 60)
        self.necessita_alvo = False
        self.area = False
    
    def usar(self, precisao, chance_critico, usuario, alvo=None):
        usuario.sanidade = usuario.sanidade_max
