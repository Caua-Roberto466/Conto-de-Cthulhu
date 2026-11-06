import random
from personagens.personagem import Herois, Habilidade


# =============================================================================
# OCULTISTA — Claudia
# Passiva: Sexto Sentido — +15% de chance de crítico nas habilidades
# =============================================================================
class Ocultista(Herois):
    def __init__(self):
        super().__init__("Claudia", 20, 3, 70, 100, 80, 90, 25, "Rituais Antigos")
        self.classe = "Ocultista"
        self.cor = 'roxo'
        self.desc = "Forte conexão com o além-vida e rituais antigos. Ataca conjurando rituais."
        self.passiva_desc = "Sexto Sentido: +15% de chance de crítico em todas as habilidades."
        self.habilidades = [OlharDoVazio(), ChamasDoVacuo(), RitualDeSangue()]
        self.bonus_critico_passiva = 15  # bônus fixo da passiva

    def passiva(self, evento, dados):
        pass  # passiva é aplicada diretamente nas habilidades via bonus_critico_passiva


# =============================================================================
# HABILIDADES DA OCULTISTA
# =============================================================================

class OlharDoVazio(Habilidade):
    """Debuff de defesa no alvo por 3 turnos."""
    def __init__(self):
        super().__init__("Olhar do Vazio", "Encaram o inimigo reduzindo sua defesa por 3 turnos.", 20)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            alvo.defesa -= 6
            alvo.efeitos.append({'nome': 'intimidação', 'turno': 3, 'ataque': 0, 'defesa': -6, 'precisao': 0})
            print(f"\n{usuario.nome} encarou {alvo.nome} com o Olhar do Vazio! Defesa reduzida por 3 turnos.")
        else:
            print(f"\n{usuario.nome} não conseguiu afetar {alvo.nome} com seu olhar.")


class ChamasDoVacuo(Habilidade):
    """Dano + queimadura por 5 turnos."""
    def __init__(self):
        super().__init__("Chamas do Vácuo", "Portal negro que expele chamas e causa queimadura por 5 turnos.", 40)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            dano_base = (usuario.ataque + usuario.nivel) * 1.4
            reducao = min(alvo.defesa, 75)
            # aplica bônus da passiva Sexto Sentido
            crit_total = chance_critico + getattr(usuario, 'bonus_critico_passiva', 0)

            roll_crit = random.randint(1, 100)
            if roll_crit <= crit_total:
                dano_final = max(1, usuario.critico(dano_base) * (1 - reducao / 100))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano de chamas CRÍTICO em {alvo.nome}!")
            else:
                dano_final = max(1, dano_base * (1 - reducao / 100))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano de chamas em {alvo.nome}.")

            # aplica queimadura independente de crítico
            alvo.efeitos.append({'nome': 'queimadura', 'turno': 5, 'ataque': 0, 'defesa': 0, 'precisao': 0, 'dano': 15})
            alvo.vida = max(0, alvo.vida - dano_final)

            if alvo.vida <= 0:
                print(f"\n{alvo.nome} foi carbonizado pelas Chamas do Vácuo!")
        else:
            print(f"\n{usuario.nome} errou as chamas e queimou o chão.")


class RitualDeSangue(Habilidade):
    """Dano massivo em área — custa metade da própria vida."""
    def __init__(self):
        super().__init__(
            "Ritual de Sangue",
            "Invoca um horror com seu sangue causando dano massivo em área. Custa metade da vida.",
            80
        )
        self.necessita_alvo = False
        self.area = True

    def usar(self, precisao, chance_critico, usuario, alvos):
        roll = random.randint(1, 100)
        if roll <= precisao:
            dano_base = (usuario.ataque + usuario.nivel) * 1.8
            crit_total = chance_critico + getattr(usuario, 'bonus_critico_passiva', 0)

            roll_crit = random.randint(1, 100)
            dano_final = 1  # fallback

            for alvo in alvos:
                reducao = min(alvo.defesa, 75)
                if roll_crit <= crit_total:
                    d = max(1, usuario.critico(dano_base) * (1 - reducao / 100))
                else:
                    d = max(1, dano_base * (1 - reducao / 100))
                dano_final = d
                alvo.vida = max(0, alvo.vida - d)
                if alvo.vida <= 0:
                    print(f"\n{alvo.nome} foi dizimado pelo ritual de {usuario.nome}!")

            # custo: perde metade da vida atual
            usuario.vida = max(1, usuario.vida / 2)
            sufixo = "CRÍTICO " if roll_crit <= crit_total else ""
            print(f"\n{usuario.nome} causou {dano_final:.0f} de dano {sufixo}em área, mas perdeu metade da vida!")
        else:
            print(f"\n{usuario.nome} não conseguiu realizar o ritual.")
