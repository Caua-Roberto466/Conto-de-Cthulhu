# =============================================================================
# EFEITOS — processa efeitos de status no início de cada turno
# =============================================================================

from interface.cores import cores

def processar_efeitos(personagem):
    """
    Processa cada efeito ativo do personagem:
    - Diminui o contador de turnos
    - Aplica dano contínuo (queimadura, sangramento)
    - Remove e reverte o efeito quando expira
    """
    for efeito in personagem.efeitos[:]:
        efeito['turno'] -= 1

        if efeito['turno'] <= 0:
            # efeito expirou — reverte modificadores de atributo
            personagem.ataque  -= efeito.get('ataque', 0)
            personagem.defesa  -= efeito.get('defesa', 0)
            personagem.precisao -= efeito.get('precisao', 0)
            personagem.efeitos.remove(efeito)
            print(f"\nO efeito {efeito['nome']} acabou em {personagem.nome}!")
        else:
            # efeito ainda ativo — aplica efeitos contínuos
            match efeito['nome']:
                case 'queimadura':
                    dano = efeito.get('dano', 0)
                    personagem.vida = max(0, personagem.vida - dano)
                    print(f"\n{personagem.nome} sofreu {dano} de dano pela {cores['laranja']}queimadura{cores['limpar']}!")
                    if personagem.vida <= 0:
                        print(f"\n{personagem.nome} sucumbiu às {cores['laranja']}chamas...{cores['limpar']}")

                case 'sangramento':
                    dano = efeito.get('dano', 0)
                    personagem.vida = max(0, personagem.vida - dano)
                    print(f"\n{personagem.nome} {cores['vermelho']}sangrou{cores['limpar']} e sofreu {dano} de dano!")
                    if personagem.vida <= 0:
                        print(f"\n{personagem.nome} morreu de {cores['vermelho']}sangramento...{cores['limpar']}")
                
                case 'sedativo':
                    dano = efeito.get('dano', 0)
                    personagem.ataque -= 3
                    personagem.defesa -= 3
                    print(f"\n{personagem.nome} recebeu uma redução de 3 de defesa e ataque por {cores['amarelo']}sedativo{cores['limpar']}")

                
