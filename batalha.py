import random
from personagens.rafael import Alienista
from personagens.caio import Coveiro
from monstros.monstro import Monstro
from monstros.doutrinador import Doutrinador
from interface.cores import cores
from time import sleep
from combate.vitoria import distribuir_xp

#-----------------------------------------------------------------------------------
#Menu
#-----------------------------------------------------------------------------------
def menu_heroi(heroi):
    print("")
    print("-="*25)
    print(f"Turno do {cores['azul']}{heroi}{cores['limpar']}")
    print("1 - Atacar")
    print("2 - Usar habilidade")
    print("3 - Defender")
    print("4 - Usar item")
    print("5 - Fugir")
    print("-="*25)

def apresentar_time(time):
    print("")
    print(f"Estado da sua equipe\n")
    for i, heroi in enumerate(time, start=1):
        print(f"{i} - {cores[heroi.cor]}{heroi.nome}{cores['limpar']} | Vida: {cores['verde']}{heroi.vida:.0f}{cores['limpar']}/{cores['verde_claro']}{heroi.vida_max:.0f}{cores['limpar']} | Energia: {cores['azul']}{heroi.energia}{cores['limpar']}/{cores['azul_claro']}{heroi.energia_max}{cores['limpar']} | Sanidade: {cores['roxo_claro']}{heroi.sanidade}{cores['limpar']}/{cores['roxo']}{heroi.sanidade_max}{cores['limpar']}")
        

def apresentar_monstros(monstros):
    print("")
    print("Estado dos monstros")
    for i, monstro in enumerate(monstros, start=1):
        print(f"{i} - {cores['azul']}{monstro.nome}{cores['limpar']} | Vida: {cores['verde']}{monstro.vida:.0f}{cores['limpar']}/{cores['verde_claro']}{monstro.vida_max:.0f}{cores['limpar']}")


#-----------------------------------------------------------------------------------
#Passiva
#-----------------------------------------------------------------------------------
def notificar_time(time, evento, dados):
    for heroi in time:
        heroi.passiva(evento, dados)
#-----------------------------------------------------------------------------------
#Efeitos
#-----------------------------------------------------------------------------------
def processar_efeitos(personagem):
    for efeito in personagem.efeitos[:]:
        efeito['turno'] -= 1
        if efeito['turno'] <= 0:
            personagem.ataque -= efeito.get('ataque', 0)
            personagem.defesa -= efeito.get('defesa', 0)
            personagem.precisao -= efeito.get('precisao', 0)
            personagem.efeitos.remove(efeito)
            print(f"O efeito {efeito['nome']} acabou em {personagem.nome}!")


#-----------------------------------------------------------------------------------
#Combate
#-----------------------------------------------------------------------------------
def fase_heroi(time, monstros, monstros_derrotados):
        for heroi in time:
            processar_efeitos(heroi)
            if heroi.vida <= 0:
                continue  

            if not monstros:
                break

            while True:
                if heroi.defendendo:
                    heroi.defesa -= 10
                    heroi.defendendo = False

                apresentar_time(time)
                sleep(1)
                apresentar_monstros(monstros)

                menu_heroi(heroi.nome)
                try:
                    escolha = int(input("Escolha(1|2|3|4|5): "))

                except ValueError:
                    print(f"\nOpção inválida! Digite um número")
                    continue

                else:
                    if escolha == 1:
                        while True:
                            print("\nQual alvo deseja atacar?")
                            for i, monstro in enumerate(monstros, start=1):
                                print(f"{i} - {monstro.nome} | Vida: {cores['verde']}{monstro.vida:.0f}{cores['limpar']}/{cores['verde_claro']}{monstro.vida_max:.0f}{cores['limpar']}")
                            escolha_ataque = int(input("\nQual atacar? "))

                            if 1 <= escolha_ataque <= len(monstros):
                                alvo = monstros[escolha_ataque-1]
                                dano = heroi.atacar(heroi.ataque, alvo.defesa, alvo.nome)
                                alvo.vida -= dano

                                if alvo.vida <= 0:
                                    monstros_derrotados.append(alvo) 
                                    print(f"\n{alvo.nome} foi derrotado...")
                                break

                            else:
                                print("\nMonstro não existe")

                        monstros[:] = [m for m in monstros if m.vida > 0]
                        break

                    elif escolha == 2:
                        for i, hab in enumerate(heroi.habilidades, start=1):
                            print(f"{i} - {hab.nome} | Custo {hab.custo}")
                        escolha_hab = int(input("\nEscolha a Habilidade: "))
                        hab = heroi.habilidades[escolha_hab - 1]

                        if heroi.energia < hab.custo:
                            print(f"\n{heroi.nome} não tem energia para usar {hab.nome}")
                            continue

                        if hab.necessita_alvo:
                            print("")
                            for i, monstro in enumerate(monstros, start=1):
                                    print(f"{i} - {monstro.nome} | Vida: {cores['verde']}{monstro.vida:.0f}{cores['limpar']}/{cores['verde_claro']}{monstro.vida_max:.0f}{cores['limpar']}")
                            escolha_alvo = int(input("\nEscolha o alvo: "))
                            alvo = monstros[escolha_alvo - 1]
                            
                        else:
                            alvo = None
                        
                        if hab.area:
                            print("")
                            hab.usar(heroi.precisao, heroi.chance_critico, heroi, monstros)
                        else:
                            hab.usar(heroi.precisao, heroi.chance_critico, heroi, alvo)
                        
                        heroi.energia -= hab.custo
                            
                        if alvo and alvo.vida <= 0:
                            monstros_derrotados.append(alvo) 

                        monstros[:] = [m for m in monstros if m.vida > 0]
                        break

                    elif escolha == 3:
                        heroi.defender()
                        heroi.defendendo = True
                        print(f"\n{heroi.nome} está se defendendo!")
                        break

                    elif escolha == 4:
                        #vai usar item
                        pass

                    elif escolha == 5:
                        #foge
                        pass
                    
                    else:
                        print("Opção inválida")
    
def fase_monstro(time, monstros, notificar):
    for monstro in monstros:
        processar_efeitos(monstro)
        if monstro.vida <= 0:
            continue
        alvo = random.choice(time)
        dano = monstro.atacar(monstro.ataque, alvo.defesa, alvo.nome)
        alvo.vida -= dano

        if monstro.dano_sanidade > 0:
            alvo.sanidade -= monstro.dano_sanidade
            notificar(time, "sanidade_perdida", {'alvo': alvo})

        if alvo.vida <= 0:
            print(f"\n{alvo.nome} foi derrotado...")

#-----------------------------------------------------------------------------------
#Controle
#-----------------------------------------------------------------------------------

def tem_vivo(time):
    for membro in time:
        if membro.vida > 0:
            return True
    return False




def combate(time, monstros):
    monstros_derrotados = []
    while tem_vivo(time) and tem_vivo(monstros):
        fase_heroi(time, monstros, monstros_derrotados)
        sleep(1)
        mortos = [m for m in monstros if m.vida <= 0]
        monstros_derrotados.extend(mortos)
        monstros[:] = [m for m in monstros if m.vida > 0]
        
        if not monstros:
            break

        fase_monstro(time, monstros, notificar_time)

        time[:] = [h for h in time if h.vida > 0]
    
    if tem_vivo(time):
        distribuir_xp(time, monstros_derrotados)
        sleep(1)
        print("\nVitória! O grupo sobreviveu!")
        sleep(1)
    else:
        sleep(2)
        print("\nDerrota... O grupo foi dizimado.")
        sleep(1)

#/usr/bin/python3 -m combate.batalha