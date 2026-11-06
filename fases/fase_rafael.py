from monstros.monstros_rafael.doutrinador import Doutrinador
from monstros.monstros_rafael.paciente_alucinado import Paciente_Alucinado
from monstros.monstros_rafael.insania import Insania
from monstros.monstros_rafael.enfermeiro_possuido import Enfermeiro_Possuido
from monstros.monstros_rafael.cobaia_amaldicoada import Cobaia_Amaldicoada
from time import sleep
from personagens.rafael import Alienista
from combate.batalha import combate


monstros1 = [Paciente_Alucinado(1), Paciente_Alucinado(1)]
monstros2 = [Paciente_Alucinado(2), Insania(1)]
monstros3 = [Insania(2), Insania(2)]
monstros4 = [Doutrinador(1), Doutrinador(1), Enfermeiro_Possuido(1)]
monstros5 = [Cobaia_Amaldicoada(1)]

rafael = Alienista()

frase1 = "Rafael está chegando em seu local de trabalho..."
frase2 = "O local está destruído, a porta da frente arromba, critos ecoam do local..."
frase3 = "Ele caminha pelos corredores quando encontra figuras misteriosas vindo em sua direção!"

frase4 = "Ele corre para seu escritório!"
frase5 = "Gritos são ouvidos! Sangue escorre pelo chão..."
frase6 = "No seu escritório tem algo diferente! Um monstro aparece!"

frase7 = "Após algumas dificuldades, ele consegue vencer..."
frase8 = "Uma voz ao longe o chama..."
frase9 = "Mais insânia!"

def batalha1():
    print(frase1)
    sleep(1)
    print(frase2)
    sleep(2)
    print(frase3)
    sleep(1)

    try:
        time
    except NameError:
        time = []

    time.append(rafael)

    combate(time, monstros1)

def batalha2():
    sleep(1)
    print(frase4)
    sleep(1)
    print(frase5)
    sleep(1)
    print(frase6)

    try:
        time
    except NameError:
        time = []

    time.append(rafael)

    combate(time, monstros2)

def batalha3():
    sleep(1)
    print(frase7)
    sleep(1)
    print(frase8)
    sleep(1)
    print(frase9)

    try:
        time
    except NameError:
        time = []

    time.append(rafael)

    combate(time, monstros3)
