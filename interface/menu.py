from prompt_toolkit import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, VSplit, Window, ConditionalContainer
from prompt_toolkit.widgets import Frame
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit.filters import Condition

#---------------------------------------------------------------------------------------
# Menu principal
#---------------------------------------------------------------------------------------
opcoes = [
    "Jogar",
    "Carregar",
    "Personagens",
    "Sair"
]

selecionado = 0
selecionado_p = 0

def menu():
    linhas = []
    linhas.append(('class:opcao', '\n'))
    for i, opcao in enumerate(opcoes):
        if i == selecionado:
            linhas.append(('class:selecionado', f'▶ {opcao}  \n\n'))
        else:
            linhas.append(('class:opcao', f'  {opcao}  \n\n'))
    return linhas

#---------------------------------------------------------------------------------------
# Menu personagens
#---------------------------------------------------------------------------------------
from personagens.caio import Coveiro
from personagens.claudia import Ocultista
from personagens.douglas import Investigador
from personagens.rafael import Alienista

personagens = [
    Coveiro(),
    Ocultista(),
    Investigador(),
    Alienista()
]

selecionado_p = 0

def menu_personagens():
    linhas = []
    for i, personagem in enumerate(personagens):
        linhas.append(('class:opcao', '\n'))
        if i == selecionado_p:
            linhas.append(('class:selecionado', f'▶ {personagem.nome}  \n'))
        else:
            linhas.append(('class:opcao', f'  {personagem.nome}  \n'))
    return linhas


tela_atual = 'menu'

kb = KeyBindings()

@kb.add('up')
def subir(event):
    global selecionado
    global selecionado_p
    if tela_atual == 'menu':
        selecionado = (selecionado - 1) % len(opcoes)
    elif tela_atual == 'personagens':
        selecionado_p = (selecionado_p - 1) % len(personagens)

@kb.add('down')
def descer(event):
    global selecionado
    global selecionado_p
    if tela_atual == 'menu':
            selecionado = (selecionado + 1) % len(opcoes)
    elif tela_atual == 'personagens':
        selecionado_p = (selecionado_p + 1) % len(personagens)

@kb.add('enter')
def confirmar(event):
    global tela_atual
    if selecionado == 0:
        pass
    elif selecionado == 2:
        tela_atual = 'personagens'
    elif selecionado == 3:
        event.app.exit()

@kb.add('escape')
def voltar(event):
    global tela_atual
    tela_atual = 'menu'

def conteudo():
    if tela_atual == 'menu':
        return menu()
    elif tela_atual == 'personagens':
        return menu_personagens()

layout = Layout(
    HSplit([
        Window(),  # espaço em cima
        VSplit([
            Window(),  # espaço à esquerda
            Frame(
                Window(
                    content=FormattedTextControl(conteudo),
                    width=24,
                    height=9,
                ),
                title='🐙 Conto de Cthulhu',
                style='class:borda',
            ),
            Window(),  # espaço à direita
        ]),
        Window(),  # espaço em baixo
    ])
)

estilo = Style.from_dict({
    'selecionado': 'bold fg:white',
    'opcao': 'fg:red',
    'borda': 'fg:ansibrightblue',
    'frame.label': 'bold fg:ansibrightblue'
})

app = Application(
    layout=layout,
    style=estilo,
    key_bindings=kb,
    full_screen=True
)
