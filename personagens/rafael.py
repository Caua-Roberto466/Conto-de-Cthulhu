import random
from personagens.personagem import Herois, Habilidade
from interface.cores import cores


# =============================================================================
# ALIENISTA — Rafael
# Passiva: Mente Blindada — recupera 5 de sanidade do alvo quando alguém perde
# =============================================================================
class Alienista(Herois):
    def __init__(self):
        super().__init__(f"{cores['amarelo']}Rafael{cores['limpar']}", 10, 6, 85, 120, 50, 90, 10, "Equipamentos Médicos")
        self.classe = "Alienista"
        self.cor = 'amarelo'
        self.desc = "Médico do hospício, mente forte contra o horror. Ataca com equipamentos médicos."
        self.passiva_desc = "Mente Blindada: Quando alguém perde sanidade, recupera 5 dela."
        self.habilidades = [Sedativo(), TerapiaDeChoque(), TrabalhoMental()]

    def passiva(self, evento, dados):
        """Mente Blindada: recupera 5 de sanidade do alvo quando evento sanidade_perdida dispara."""
        if evento == "sanidade_perdida" and self.vida > 0:
            alvo = dados['alvo']
            alvo.sanidade = min(alvo.sanidade + 5, alvo.sanidade_max)
            print(f"Mente Blindada: {alvo.nome} recuperou 5 de sanidade pela passiva do {self.nome}!")


# =============================================================================
# HABILIDADES DO ALIENISTA
# =============================================================================

class Sedativo(Habilidade):
    """Aplica debuff de ataque e defesa por 3 turnos."""
    def __init__(self):
        super().__init__("Sedativo", "Tranquilizante que reduz ataque e defesa do inimigo por 3 turnos.", 15)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            #alvo.ataque -= 3
            #alvo.defesa -= 3
            alvo.efeitos.append({'nome': 'sedativo', 'turno': 3, 'ataque': -3, 'defesa': -3, 'precisao': 0})
            print(f"\n{usuario.nome} aplicou sedativo em {alvo.nome}! Ataque e defesa reduzidos por 3 turnos.")
        else:
            print(f"\n{usuario.nome} errou o sedativo.")


class TerapiaDeChoque(Habilidade):
    """Dano elétrico com chance de crítico."""
    def __init__(self):
        super().__init__("Terapia de Choque", "Descarga elétrica no inimigo com chance de crítico.", 30)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            dano_base = (usuario.ataque + usuario.nivel / 2) * 1.2
            reducao = min(alvo.defesa, 75)

            roll_crit = random.randint(1, 100)
            if roll_crit <= chance_critico:
                dano_final = max(1, usuario.critico(dano_base) * (1 - reducao / 100))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano elétrico CRÍTICO em {alvo.nome}!")
            else:
                dano_final = max(1, dano_base * (1 - reducao / 100))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano elétrico em {alvo.nome}.")

            alvo.vida = max(0, alvo.vida - dano_final)
            if alvo.vida <= 0:
                print(f"\n{alvo.nome} foi derrotado pelo choque de {usuario.nome}!")
        else:
            print(f"\n{usuario.nome} errou ao usar o aparelho.")


class TrabalhoMental(Habilidade):
    """Restaura 15 de sanidade de todos os aliados."""
    def __init__(self):
        super().__init__("Trabalho Mental", "Terapia que restaura 15 de sanidade do time inteiro.", 60)
        self.ajuda_time = True  # afeta aliados, não inimigos

    def usar(self, precisao, chance_critico, usuario, alvo):
        # alvo aqui é a lista do time (passada pelo sistema ajuda_time)
        if isinstance(alvo, list):
            for aliado in alvo:
                aliado.sanidade = min(aliado.sanidade + 15, aliado.sanidade_max)
            print(f"\n{usuario.nome} realizou uma sessão e restaurou 15 de sanidade do time!")
        else:
            usuario.sanidade = min(usuario.sanidade + 15, usuario.sanidade_max)
            print(f"\n{usuario.nome} restaurou 15 de sanidade.")
