import random
from interface.cores import cores
from time import sleep
from combate.vitoria import distribuir_xp
from efeitos.efeito import processar_efeitos
from interface.hub_descanso import hub_descanso


# =============================================================================
# DISPLAY — funções de exibição do estado do combate
# =============================================================================

def menu_heroi(nome_heroi):
    print("")
    print("-=" * 25)
    print(f"Turno de {cores['azul']}{nome_heroi}{cores['limpar']}")
    print("1 - Atacar")
    print("2 - Usar habilidade")
    print("3 - Defender")
    print("4 - Usar item")
    print("5 - Fugir")
    print("-=" * 25)


def apresentar_time(time):
    print("\nEstado da equipe:")
    for heroi in time:
        print(
            f"  {cores[heroi.cor]}{heroi.nome}{cores['limpar']} | "
            f"Vida: {cores['verde']}{heroi.vida:.0f}{cores['limpar']}/{cores['verde_claro']}{heroi.vida_max:.0f}{cores['limpar']} | "
            f"Energia: {cores['azul']}{heroi.energia:.0f}{cores['limpar']}/{cores['azul_claro']}{heroi.energia_max:.0f}{cores['limpar']} | "
            f"Sanidade: {cores['roxo_claro']}{heroi.sanidade:.0f}{cores['limpar']}/{cores['roxo']}{heroi.sanidade_max:.0f}{cores['limpar']}"
        )


def apresentar_monstros(monstros):
    print("\nInimigos:")
    for i, monstro in enumerate(monstros, start=1):
        print(
            f"  {i} - {cores['vermelho']}{monstro.nome}{cores['limpar']} | "
            f"Vida: {cores['verde']}{monstro.vida:.0f}{cores['limpar']}/{cores['verde_claro']}{monstro.vida_max:.0f}{cores['limpar']}"
        )


# =============================================================================
# PASSIVA — notifica todos os heróis sobre eventos do combate
# =============================================================================

def notificar_time(time, evento, dados):
    """Dispara o evento para a passiva de cada herói."""
    for heroi in time:
        heroi.passiva(evento, dados)


# =============================================================================
# HABILIDADES EM ÁREA
# =============================================================================

def usar_habilidade_area(usuario, monstros, habilidade):
    """Executa habilidade em área e reporta monstros derrotados."""
    habilidade.usar(usuario.precisao, usuario.chance_critico, usuario, monstros)
    for monstro in monstros:
        if monstro.vida <= 0:
            print(f"\n{monstro.nome} foi derrotado...")


# =============================================================================
# FASE DOS HERÓIS
# =============================================================================

def fase_heroi(time, monstros, monstros_derrotados):
    for heroi in time:
        processar_efeitos(heroi)

        # pula herói morto
        if heroi.vida <= 0:
            continue

        # todos os monstros já foram derrotados neste turno
        if not monstros:
            break

        while True:
            # reseta defesa se estava defendendo no turno anterior
            if heroi.defendendo:
                heroi.defesa -= 10
                heroi.defendendo = False
            sleep(1.2)
            apresentar_time(time)
            sleep(1.2)
            apresentar_monstros(monstros)
            sleep(1.2)
            menu_heroi(heroi.nome)

            try:
                escolha = int(input("Escolha (1-5): "))
            except ValueError:
                print("\nOpção inválida! Digite um número.")
                continue

            # ----------------------------------------------------------------
            if escolha == 1:  # ATACAR
            # ----------------------------------------------------------------
                while True:
                    print("\nQual alvo deseja atacar?")
                    apresentar_monstros(monstros)
                    try:
                        escolha_ataque = int(input("Qual atacar? "))
                    except ValueError:
                        print("Digite um número válido.")
                        continue

                    if 1 <= escolha_ataque <= len(monstros):
                        alvo = monstros[escolha_ataque - 1]
                        dano = heroi.atacar(heroi.ataque, alvo.defesa, alvo.nome)
                        alvo.vida -= dano

                        if alvo.vida <= 0:
                            monstros_derrotados.append(alvo)
                            print(f"\n{alvo.nome} foi derrotado!")
                        break
                    else:
                        print("\nMonstro não existe.")

                monstros[:] = [m for m in monstros if m.vida > 0]
                break

            # ----------------------------------------------------------------
            elif escolha == 2:  # USAR HABILIDADE
            # ----------------------------------------------------------------
                if not heroi.habilidades:
                    print(f"\n{heroi.nome} não tem habilidades disponíveis.")
                    continue

                print("\nHabilidades disponíveis:")
                for i, hab in enumerate(heroi.habilidades, start=1):
                    print(f"  {i} - {hab.nome} | Custo: {hab.custo} energia | {hab.descricao}")

                try:
                    escolha_hab = int(input("\nEscolha a habilidade: "))
                    hab = heroi.habilidades[escolha_hab - 1]
                except (ValueError, IndexError):
                    print("Habilidade inválida.")
                    continue

                if heroi.energia < hab.custo:
                    print(f"\n{heroi.nome} não tem energia suficiente! ({heroi.energia:.0f}/{hab.custo})")
                    continue

                # habilidade que ajuda o time
                if hab.ajuda_time:
                    hab.usar(heroi.precisao, heroi.chance_critico, heroi, time)
                    heroi.energia -= hab.custo
                    break

                # habilidade em área contra monstros
                if hab.area:
                    usar_habilidade_area(heroi, monstros, hab)
                    for m in monstros:
                        if m.vida <= 0:
                            monstros_derrotados.append(m)
                    heroi.energia -= hab.custo
                    monstros[:] = [m for m in monstros if m.vida > 0]
                    break

                # habilidade que precisa de alvo específico
                if hab.necessita_alvo:
                    print("\nEscolha o alvo:")
                    apresentar_monstros(monstros)
                    try:
                        escolha_alvo = int(input("Qual alvo? "))
                        alvo = monstros[escolha_alvo - 1]
                    except (ValueError, IndexError):
                        print("Alvo inválido.")
                        continue
                else:
                    alvo = None

                hab.usar(heroi.precisao, heroi.chance_critico, heroi, alvo)
                heroi.energia -= hab.custo

                if alvo and alvo.vida <= 0:
                    monstros_derrotados.append(alvo)
                    print(f"\n{alvo.nome} foi derrotado!")

                monstros[:] = [m for m in monstros if m.vida > 0]
                break

            # ----------------------------------------------------------------
            elif escolha == 3:  # DEFENDER
            # ----------------------------------------------------------------
                heroi.defender()
                print(f"\n{heroi.nome} está se defendendo até o próximo turno!")
                break

            # ----------------------------------------------------------------
            elif escolha == 4:  # USAR ITEM
            # ----------------------------------------------------------------
                print("\nSistema de itens em desenvolvimento.")
                # não gasta o turno — volta ao menu

            # ----------------------------------------------------------------
            elif escolha == 5:  # FUGIR
            # ----------------------------------------------------------------
                print("\nSistema de fuga em desenvolvimento.")
                # não gasta o turno — volta ao menu

            else:
                print("\nOpção inválida. Escolha entre 1 e 5.")


# =============================================================================
# FASE DOS MONSTROS
# =============================================================================

def fase_monstro(time, monstros, notificar):
    for monstro in monstros:
        processar_efeitos(monstro)

        if monstro.vida <= 0:
            continue

        # ataca um herói vivo aleatório
        vivos = [h for h in time if h.vida > 0]
        if not vivos:
            break

        alvo = random.choice(vivos)
        dano = monstro.atacar(monstro.ataque, alvo.defesa, alvo.nome)
        alvo.vida -= dano

        # dano de sanidade — dispara passiva do time
        if monstro.dano_sanidade > 0:
            alvo.sanidade = max(0, alvo.sanidade - monstro.dano_sanidade)
            notificar(time, "sanidade_perdida", {'alvo': alvo})

        if alvo.vida <= 0:
            print(f"\n{alvo.nome} foi derrotado...")


# =============================================================================
# CONTROLE DO COMBATE
# =============================================================================

def tem_vivo(grupo):
    """Retorna True se pelo menos um membro do grupo tem vida > 0."""
    return any(m.vida >= 1 for m in grupo)


def combate(time, monstros):
    """
    Loop principal de combate.
    Fase dos heróis → filtra mortos → fase dos monstros → repete.
    """
    monstros_derrotados = []

    while tem_vivo(time) and tem_vivo(monstros):
        # turno dos heróis
        fase_heroi(time, monstros, monstros_derrotados)
        sleep(0.5)

        # captura monstros que morreram neste turno
        novos_mortos = [m for m in monstros if m.vida <= 0]
        monstros_derrotados.extend(novos_mortos)
        monstros[:] = [m for m in monstros if m.vida > 0]

        if not monstros:
            break

        # turno dos monstros
        fase_monstro(time, monstros, notificar_time)

        # remove heróis derrotados da lista ativa
        time[:] = [h for h in time if h.vida > 0]

    # resultado final
    if tem_vivo(time):
        sleep(1)
        distribuir_xp(time, monstros_derrotados)
        print(f"\n{cores['verde']}Vitória! O grupo sobreviveu!{cores['limpar']}")
        sleep(1)
        hub_descanso(time)
    else:
        sleep(1)
        print(f"\n{cores['vermelho']}Derrota... O grupo foi dizimado.{cores['limpar']}")
        sleep(1)
