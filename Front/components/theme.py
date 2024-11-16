from nicegui import ui
from contextlib import contextmanager
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme
from Front.components.menu import menu
ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

@contextmanager
def frame(navigation_title: str):
    with ui.header().style(f'background-color: {color_scheme.primary};'):
        ui.image('Front/static/logo.png').style('width: 32px; display: flex; align-items: center;')
        ui.label('MONDA').style(f'color: {color_scheme.text}; {font_scheme.h2} width: 25%; display: flex; align-items: center;')
        ui.space()
        ui.label(navigation_title).style(f'color: {color_scheme.text}; {font_scheme.body1}')
        ui.space()
    with ui.left_drawer().style(f'height: 100%; background-color: {color_scheme.secondary};'):
        menu()
    with ui.column().classes('absolute-center items-center'):
        yield
