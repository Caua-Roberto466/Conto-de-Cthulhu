from personagens.personagem import Herois
from personagens.personagem import Habilidade
import random

class Coveiro(Herois):
    def __init__(self):
        super().__init__("Caio", 14, 10, 100, 80, 90, 90, 15, "Pá de ferro")
        self.classe = "Coveiro"

        self.desc = "Anos trabalhando no cemitério fez ele se familiarizar com a morte. Ataca com sua pá de ferro."

        self.passiva_desc = "Olhar de cadáver: Assusta humanos com seu olhar, e é imune a efeitos de medo e insanidade"

        self.habilidades = [CorteDeDefunto(), GiroDoCoveiro(), EnterroMarcado()]
        self.cor = 'claro'

class CorteDeDefunto(Habilidade):
    def __init__(self):
        super().__init__("Corte de Defunto", "Movimento rápido com a pá que corta o inimigo e causa sangramento", 15)
        self.necessita_alvo = True
        self.area = False

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            roll_critico = random.randint(1, 100)
            dano = (usuario.ataque + (usuario.nivel)) * 1.15
            if roll_critico <= chance_critico:
                dano_critico = usuario.critico(dano)
                dano_final = max(1, dano_critico - (dano_critico * (alvo.defesa/100)))

                alvo.vida = max(0, alvo.vida - dano_final)

                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com um corte crítico!")
            else:
                dano_final = max(1, dano - (dano * (alvo.defesa/100)))
                
                alvo.vida = max(0, alvo.vida - dano_final)

                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com sua pá!")
            
            if alvo.vida <= 0:
                print(f"\n{usuario.nome} derrotou {alvo.nome} com o corte de sua pá") 
        else:
            print(f"\n{usuario.nome} errou a pá ao tentar cortar o inimigo")



class GiroDoCoveiro(Habilidade):
    def __init__(self):
        super().__init__("Giro do Coveiro", "Gira igual um louco para cima do inimigo", 20)
        self.necessita_alvo = True
        self.area = False
    
    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)

        if roll <= precisao:
            dano = (usuario.ataque + (usuario.nivel)) * 1.25
            roll_critico = random.randint(1, 100)

            if roll_critico <= chance_critico:
                dano_critico = usuario.critico(dano)
                dano_final = max(1, dano_critico - (dano_critico * (alvo.defesa / 100)))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com um giro crítico em {alvo.nome}")
                
                alvo.vida = max(0, alvo.vida - dano_final)
                

            else:
                dano_final = max(1, dano - (dano * (alvo.defesa / 100)))
                print(f"\n{usuario.nome} causou {dano_final:.0f} com sua pá em {alvo.nome}")
                
                alvo.vida = max(0, alvo.vida - dano_final)
                
                

            if alvo.vida <= 0:
                print(f"\n{alvo.nome} foi derrotado pelo giro do {usuario.nome}")
            
        else:
            print(f"{usuario.nome} errou seu giro e passou reto por {alvo.nome}")



class EnterroMarcado(Habilidade):
    def __init__(self):
        super().__init__("Enterro Marcado", "Bate a pá em alta velocidade na cabeça do inimigo, causando um acerto crítico", 50)
        self.necessita_alvo = True
        self.area = False
    
    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)

        if roll <= precisao:
            dano = (usuario.ataque + (usuario.nivel)) * 1.5
            critico = usuario.critico(dano)
            dano_final = max(1, critico - (critico * (usuario.defesa / 100)))
            print(f"\n{usuario.nome} golpeu a cabeça de {alvo.nome} e causou um acerto crítico de {dano_final:.0f} de dano")

            alvo.vida = max(0, alvo.vida - dano_final)
        
            if alvo.vida <= 0:
                print(f"\n{alvo.nome} teve a cabeça esmagada e foi derrotado")

        else:
            print(f"\n{usuario.nome} Errou seu movimento e acertou o chão com sua pá")