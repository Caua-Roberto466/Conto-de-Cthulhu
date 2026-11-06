import random
from personagens.personagem import Herois, Habilidade
from interface.cores import cores


# =============================================================================
# INVESTIGADOR — Douglas
# Passiva: Instinto de Londres — nunca erra ataques básicos
# =============================================================================
class Investigador(Herois):
    def __init__(self):
        super().__init__("Douglas", 17, 7, 90, 95, 60, 100, 15, "Revólver Webley")
        self.classe = "Investigador"
        self.cor = 'verde'
        self.desc = "Detetive de Londres que já capturou muitos criminosos. Ataca com seu revólver Webley."
        self.passiva_desc = "Instinto de Londres: Nunca erra ataques básicos (precisão sempre 100)."
        self.habilidades = [Investigar(), Coronhada(), TiroDuplo()]

    def passiva(self, evento, dados):
        pass  # passiva aplicada diretamente no atacar — precisao já é 100


# =============================================================================
# HABILIDADES DO INVESTIGADOR
# =============================================================================

class Investigar(Habilidade):
    """Revela a fraqueza do inimigo."""
    def __init__(self):
        super().__init__("Investigar", "Investiga o inimigo e revela sua fraqueza.", 10)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            fraqueza = getattr(alvo, 'fraqueza', 'desconhecida')
            print(f"\nA fraqueza de {alvo.nome} é {cores['vermelho']}{fraqueza}{cores['limpar']}!")
        else:
            print(f"\n{usuario.nome} não conseguiu investigar {alvo.nome}.")


class Coronhada(Habilidade):
    """Ataque físico com alta chance de crítico."""
    def __init__(self):
        super().__init__("Coronhada", "Golpe com a coronha da arma — alta chance de crítico.", 25)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            dano_base = (usuario.ataque + usuario.nivel) * 1.2
            reducao = min(alvo.defesa, 75)
            # chance de crítico elevada: base + 35%
            roll_crit = random.randint(1, 100)
            if roll_crit <= min(chance_critico + 35, 100):
                dano_final = max(1, usuario.critico(dano_base) * (1 - reducao / 100))
                print(f"\n{usuario.nome} deu uma coronhada CRÍTICA em {alvo.nome}! Dano: {dano_final:.0f}")
            else:
                dano_final = max(1, dano_base * (1 - reducao / 100))
                print(f"\n{usuario.nome} deu uma coronhada em {alvo.nome}. Dano: {dano_final:.0f}")

            alvo.vida = max(0, alvo.vida - dano_final)
            if alvo.vida <= 0:
                print(f"\n{usuario.nome} derrubou {alvo.nome} com a coronhada!")
        else:
            print(f"\n{usuario.nome} errou a coronhada e acertou a parede.")


class TiroDuplo(Habilidade):
    """Dois tiros em sequência — ambos com crítico garantido."""
    def __init__(self):
        super().__init__("Tiro Duplo", "Dois tiros rápidos — ambos causam crítico.", 50)
        self.necessita_alvo = True

    def usar(self, precisao, chance_critico, usuario, alvo):
        roll = random.randint(1, 100)
        if roll <= precisao:
            dano_base = (usuario.ataque + usuario.nivel) * 1.5
            reducao = min(alvo.defesa, 75)
            # dois tiros críticos em sequência
            tiro1 = max(1, usuario.critico(dano_base) * (1 - reducao / 100))
            tiro2 = max(1, usuario.critico(dano_base) * (1 - reducao / 100))
            dano_total = tiro1 + tiro2

            print(f"\n{usuario.nome} disparou duas vezes em {alvo.nome}!")
            print(f"  Tiro 1: {cores['vermelho']}{tiro1:.0f}{cores['limpar']} | "
                  f"Tiro 2: {cores['vermelho']}{tiro2:.0f}{cores['limpar']} | "
                  f"Total: {cores['vermelho']}{dano_total:.0f}{cores['limpar']}")

            alvo.vida = max(0, alvo.vida - dano_total)
            if alvo.vida <= 0:
                print(f"\n{alvo.nome} foi alvejado e derrotado!")
        else:
            print(f"\n{usuario.nome} errou os dois tiros.")
