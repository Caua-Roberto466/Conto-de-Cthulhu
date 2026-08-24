from personagens.personagem import Herois
from personagens.personagem import Habilidade
import random


class Ocultista(Herois):
    def __init__(self):
        super().__init__("Claudia", 20, 3, 70, 100, 80, 90, 25, "Rituais Antigos")
        self.classe = "Ocultista"
        self.desc = "Forte conexão com o além-vida e conhecimento de rituais antigos. Ataca conjurando rituais."
        self.passiva_desc = "Sexto sentido: Aumenta a chance de crítico em todas as habilidades"
        self.habilidades = [OlharDoVazio(), ChamasDoVacuo(), RitualDeSangue()]
        self.cor = 'roxo'


class OlharDoVazio(Habilidade):
    def __init__(self):
        super().__init__("Olhar do Vazio", "Encara o inimigo com os olhos dos mortos, diminuindo a defesa do alvo", 20)
        self.necessita_alvo = True
        self.area = False

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            alvo.defesa -= 6
            alvo.efeitos.append({'nome': 'intimidação', 'turno': 3, 'ataque': 0, 'defesa': -6, 'precisao': 0, 'dano': 0})

            print(f"{usuario.nome} encarou {alvo.nome} com seu olhar do vazio e diminuiu sua defesa")
        
        else:
            print(f"{usuario.nome} não consegiu afetar o inimigo com seu olhar")


class ChamasDoVacuo(Habilidade):
    def __init__(self):
        super().__init__("Chamas do Vácuo", "Convoca um portal negro que expele chamas no inimigo, queimando ele por 5 turnos", 40)
        self.necessita_alvo = True
        self.area = False

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        
        if roll <= precisao:
            dano = (usuario.ataque + usuario.nivel) * 1.4
            roll_crt = random.randint(1, 100)

            if roll_crt <= chance_critico:
                dano_crt = usuario.critico(dano)
                dano_final = max(1, dano_crt - (dano_crt * (alvo.defesa / 100)))
                alvo.efeitos.append({'nome': 'queimadura', 'turno': 5, 'ataque': 0, 'defesa': 0, 'precisao': 0, 'dano': 15})

                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano crítico com suas chamas em {alvo.nome}")

                alvo.vida = max(0, alvo.vida - dano_final)

            else:
                dano_final = max(1, dano - (dano * alvo.defesa/100))
                alvo.efeitos.append({'efeito': 'queimadura', 'turno': 5, 'ataque': 0, 'defesa': 0, 'precisao': 0, 'dano': 15})

                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com suas chamas em {alvo.nome}")

                alvo.vida = max(0, alvo.vida - dano_final)

            if alvo.vida <= 0:
                print(f"\n{alvo.nome} foi carbonizado pelas Chamas do vácuo")
        
        else:
            print(f"\n{usuario.nome} errou as chamas e queimou o chão a sua volta")


class RitualDeSangue(Habilidade):
    def __init__(self):
        super().__init__("Ritual de Sangue", "Corta sua própria mão e usa seu sangue em um ritual que invoca parte de um monstro, causando um dano massivo(área) em troca de metade da sua vida", 80)
        self.necessita_alvo = False
        self.area = True

    def usar(self, precisao, chance_critico, usuario, alvos):
        roll = random.randint(1, 100)
        
        if roll <= precisao:
            dano = (usuario.ataque + usuario.nivel) * 1.6
            roll_crt = random.randint(1, 100)

            if roll_crt <= chance_critico:
                for alvo in alvos:
                    dano_crt = usuario.critico(dano)
                    dano_final = max(1, dano_crt - (dano_crt * (alvo.defesa / 100)))
                    

                    alvo.vida = max(0, alvo.vida - dano_final)

                    if alvo.vida <= 0:
                        print(f"\n{alvo.nome} foi dizimado pelo ritual da {usuario.nome}")
                
                usuario.vida -= (usuario.vida / 2)
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com seu ritual crítico em todos os monstros, mas perdeu metade da vida")

            else:
                for alvo in alvos:
                    dano_final = max(1, dano - (dano * alvo.defesa/100))
                    

                    alvo.vida = max(0, alvo.vida - dano_final)

                    if alvo.vida <= 0:
                        print(f"\n{alvo.nome} foi dizimado pelo ritual da {usuario.nome}")

                usuario.vida -= (usuario.vida / 2)
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com seu ritual em todos os monstros, mas perdeu metade da vida")

        else:
            print(f"\n{usuario.nome} não conseguiu realizar seu ritual")
