from personagens.rafael import Alienista
from personagens.caio import Coveiro
from personagens.claudia import Ocultista
from personagens.douglas import Investigador
from monstros.monstros_rafael.doutrinador import Doutrinador
from monstros.monstros_rafael.insania import Insania
from combate.batalha import combate
from interface.menu import app
from fases.fase_rafael import batalha1, batalha2, batalha3


# Teste de combate — substituir pelas fases quando prontas
time = [Alienista(), Coveiro(), Ocultista(), Investigador()]
monstros = [Doutrinador(1), Doutrinador(1)]

#combate(time, monstros)

batalha1()
batalha2()
batalha3()