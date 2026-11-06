from interface.cores import cores


def distribuir_xp(time, monstros_derrotados):
    """
    Distribui o XP de cada monstro derrotado para todos os heróis do time.
    Exibe o XP ganho e o progresso de nível de cada herói.
    """
    if not monstros_derrotados:
        return

    xp_total = sum(m.xp_dropado for m in monstros_derrotados)

    print(f"\n{'='*50}")
    print(f"XP conquistado nessa batalha: {cores['amarelo']}{xp_total}{cores['limpar']}")
    print(f"{'='*50}")

    for heroi in time:
        heroi.ganhar_xp(xp_total)
        print(
            f"{cores[heroi.cor]}{heroi.nome}{cores['limpar']} | "
            f"LVL {heroi.nivel} | "
            f"XP: {cores['azul']}{heroi.xp}{cores['limpar']}/{cores['verde']}{heroi.xp_prox}{cores['limpar']}"
        )

def descansar(time):
    for heroi in time:
        heroi.vida = heroi.vida_max
        heroi.sanidade = heroi.sanidade_max
        heroi.energia = heroi.energia_max
        heroi.efeitos = []

def treinar(time):
    for heroi in time:
        xp = heroi.xp_prox / 4
        heroi.ganhar_xp(xp)

