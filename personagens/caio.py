import random
from personagens.personagem import Herois, Habilidade


# =============================================================================
# COVEIRO — Caio
# Passiva: Olhar de Cadáver — imune a efeitos de medo e insanidade
# =============================================================================
class Coveiro(Herois):
    def __init__(self):
        super().__init__("Caio", 14, 10, 100, 80, 90, 90, 15, "Pá de ferro")
        self.classe = "Coveiro"
        self.cor = 'claro'
        self.desc = "Anos no cemitério o familiarizaram com a morte. Ataca com sua pá de ferro."
        self.passiva_desc = "Olhar de Cadáver: Imune a efeitos de medo e insanidade."
        self.habilidades = [CorteDeDefunto(), GiroDoCoveiro(), EnterroMarcado()]

    def passiva(self, evento, dados):
        """Olhar de Cadáver: bloqueia efeitos de medo e insanidade."""
        pass  # implementar quando sistema de medo estiver pronto


# =============================================================================
# HABILIDADES DO COVEIRO
# =============================================================================

class CorteDeDefunto(Habilidade):
    """Corte rápido com a pá."""
    def __init__(self):
        super().__init__("Corte de Defunto", "Corte rápido com a pá que causa dano físico.", 15)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            dano_base = (usuario.ataque + usuario.nivel) * 1.15
            reducao = min(alvo.defesa, 75)

            roll_crit = random.randint(1, 100)
            if roll_crit <= chance_critico:
                dano_final = max(1, usuario.critico(dano_base) * (1 - reducao / 100))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com um corte CRÍTICO!")
            else:
                dano_final = max(1, dano_base * (1 - reducao / 100))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com sua pá!")

            alvo.vida = max(0, alvo.vida - dano_final)
            if alvo.vida <= 0:
                print(f"\n{alvo.nome} foi derrotado pelo corte de {usuario.nome}!")
        else:
            print(f"\n{usuario.nome} errou a pá!")


class GiroDoCoveiro(Habilidade):
    """Giro com a pá causando dano maior."""
    def __init__(self):
        super().__init__("Giro do Coveiro", "Giro poderoso com a pá causando dano alto.", 20)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            dano_base = (usuario.ataque + usuario.nivel) * 1.25
            reducao = min(alvo.defesa, 75)

            roll_crit = random.randint(1, 100)
            if roll_crit <= chance_critico:
                dano_final = max(1, usuario.critico(dano_base) * (1 - reducao / 100))
                print(f"\n{usuario.nome} causou {dano_final:.0f} de dano com um giro CRÍTICO em {alvo.nome}!")
            else:
                dano_final = max(1, dano_base * (1 - reducao / 100))
                print(f"\n{usuario.nome} causou {dano_final:.0f} com o giro da pá em {alvo.nome}.")

            alvo.vida = max(0, alvo.vida - dano_final)
            if alvo.vida <= 0:
                print(f"\n{alvo.nome} foi derrubado pelo giro do {usuario.nome}!")
        else:
            print(f"\n{usuario.nome} errou o giro e passou reto por {alvo.nome}.")


class EnterroMarcado(Habilidade):
    """Pancada letal que sempre aplica crítico."""
    def __init__(self):
        super().__init__("Enterro Marcado", "Pancada letal na cabeça — sempre causa crítico.", 50)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            dano_base = (usuario.ataque + usuario.nivel) * 1.5
            # sempre crítico — usa alvo.defesa corretamente
            dano_critico = usuario.critico(dano_base)
            reducao = min(alvo.defesa, 75)
            dano_final = max(1, dano_critico * (1 - reducao / 100))
            print(f"\n{usuario.nome} esmagou a cabeça de {alvo.nome} causando {dano_final:.0f} de dano CRÍTICO!")

            alvo.vida = max(0, alvo.vida - dano_final)
            if alvo.vida <= 0:
                print(f"\n{alvo.nome} teve a cabeça esmagada e foi derrotado!")
        else:
            print(f"\n{usuario.nome} errou e acertou o chão com a pá.")
