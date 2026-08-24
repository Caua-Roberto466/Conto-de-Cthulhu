from personagens.rafael import Alienista
from personagens.caio import Coveiro
from personagens.claudia import Ocultista
from personagens.douglas import Investigador
from monstros.doutrinador import Doutrinador
from combate.batalha import combate

monstros = [Doutrinador(1), Doutrinador(1)]
time = [Investigador(), Coveiro(), Ocultista()]

combate(time, monstros)