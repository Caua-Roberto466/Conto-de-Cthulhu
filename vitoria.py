from interface.cores import cores

def distribuir_xp(time, monstros):
    xp_final = 0
    for monstro in monstros:
        xp = monstro.xp_dropado
        xp_final += xp
        for heroi in time:
            heroi.ganhar_xp(xp)

    for heroi in time:
        print(f"{heroi.nome} ganhou {xp_final} XP | LVL {heroi.nivel} {cores['azul']}{heroi.xp}{cores['limpar']}/{cores['verde']}{heroi.xp_prox}{cores['limpar']}")