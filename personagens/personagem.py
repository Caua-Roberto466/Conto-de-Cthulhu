import random
from interface.cores import cores


# =============================================================================
# CLASSE BASE — todos os personagens (heróis e monstros) herdam daqui
# =============================================================================
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
        """Retorna o dano com multiplicador de crítico (×1.2)."""
        return ataque * 1.2

    def _calcular_dano(self, dano_base, defesa_alvo):
        """Aplica a redução de defesa com teto de 75%. Nunca retorna menos que 1."""
        reducao = min(defesa_alvo, 75)
        return max(1, dano_base * (1 - reducao / 100))

    def atacar(self, ataque, defesa, nome_alvo):
        """
        Ataque básico com chance de acerto e crítico.
        Retorna o dano final calculado (0 se errar).
        """
        roll_acerto = random.randint(1, 100)

        if roll_acerto <= self.precisao:
            roll_crit = random.randint(1, 100)

            if roll_crit <= self.chance_critico:
                dano_final = self._calcular_dano(self.critico(ataque), defesa)
                print(f"\n{self.nome} acertou um {cores['vermelho']}CRÍTICO{cores['limpar']} "
                      f"em {nome_alvo}! Dano: {cores['vermelho']}{dano_final:.0f}{cores['limpar']}")
                return dano_final
            else:
                dano_final = self._calcular_dano(ataque, defesa)
                print(f"\n{self.nome} acertou {nome_alvo}! Dano: {dano_final:.0f}")
                return dano_final
        else:
            print(f"\n{self.nome} errou o ataque!")
            return 0

    def defender(self):
        """Aumenta a defesa em +10 por um turno."""
        self.defesa += 10


# =============================================================================
# CLASSE DOS HERÓIS — herda de Personagem, adiciona sanidade, energia, XP etc.
# =============================================================================
class Herois(Personagem):
    def __init__(self, nome, ataque, defesa, vida, sanidade, energia, precisao, chance_critico, arma):
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
        print(f"{self.nome} | Vida: {self.vida:.0f}/{self.vida_max:.0f} "
              f"| San: {self.sanidade:.0f}/{self.sanidade_max:.0f} "
              f"| Energia: {self.energia:.0f}/{self.energia_max:.0f}")

    def nivel_up(self):
        """Sobe de nível e aumenta os atributos automaticamente."""
        self.nivel += 1
        self.xp_prox = int(self.xp_prox * 1.1)
        self.ataque *= 1.2
        self.defesa *= 1.1
        self.vida_max += 10
        self.vida = self.vida_max          # restaura vida ao upar
        self.sanidade_max *= 1.01
        self.sanidade = self.sanidade_max  # restaura sanidade ao upar
        self.energia_max *= 1.10
        self.energia = self.energia_max    # restaura energia ao upar
        print(f"\n{cores['amarelo']}*** {self.nome} subiu para o nível {self.nivel}! ***{cores['limpar']}")

    def ganhar_xp(self, quantidade):
        """Adiciona XP e verifica se sobe de nível."""
        self.xp += quantidade
        if self.xp >= self.xp_prox:
            self.xp -= self.xp_prox
            self.nivel_up()

    def defender(self):
        """Ativa modo de defesa: +10 defesa até o próximo turno."""
        self.defendendo = True
        self.defesa += 10

    def passiva(self, evento, dados):
        """Cada herói sobrescreve com sua passiva específica."""
        pass

    def ativa(self):
        """Reservado para habilidades ativas futuras."""
        pass


# =============================================================================
# CLASSE BASE DAS HABILIDADES — cada habilidade herda daqui
# =============================================================================
class Habilidade:
    def __init__(self, nome, descricao, custo):
        self.nome = nome
        self.descricao = descricao
        self.custo = custo
        self.necessita_alvo = False  # True se precisa escolher um monstro
        self.area = False            # True se atinge todos os monstros
        self.ajuda_time = False      # True se beneficia aliados

    def usar(self, precisao, chance_critico, usuario, alvo=None):
        """Cada habilidade sobrescreve com seu efeito."""
        pass
