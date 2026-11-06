from prompt_toolkit import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, VSplit, Window, ConditionalContainer
from prompt_toolkit.widgets import Frame
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit.filters import Condition

from combate.vitoria import descansar, treinar
#===============================================================
# Iniciação de menu
#===============================================================

opcoes = [
    "Treinar",
    "Descansar"
]

selecionado = 0

def menu_descanso():
    linha = []
    linha.append(('class:opcao', '\n'))
    for i, opcao in enumerate(opcoes):
        if i == selecionado:
            linha.append(('class:selecionado', f'▶ {opcao}  \n\n'))
        else:
            linha.append(('class:opcao', f'  {opcao}  \n\n'))
    return linha

def hub_descanso(time):
    kb = KeyBindings()

    @kb.add('up')
    def subir(event):
        global selecionado
        selecionado = (selecionado - 1) % len(opcoes)

    @kb.add('down')
    def descer(event):
        global selecionado
        selecionado = (selecionado + 1) % len(opcoes)

    @kb.add('enter')
    def confirmar(event):
        if selecionado == 0:
            event.app.exit()
            treinar(time)
            
        elif selecionado == 1:
            event.app.exit()
            descansar(time)

    layout = Layout(
        HSplit([
            Window(),  # espaço em cima
            VSplit([
                Window(),  # espaço à esquerda
                Frame(
                    Window(
                        content=FormattedTextControl(menu_descanso),
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
    app.run()
