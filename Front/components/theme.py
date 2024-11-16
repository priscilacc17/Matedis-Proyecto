from nicegui import ui
from contextlib import contextmanager
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme
from Front.components.menu import menu
from Front.components.header import header
ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

@contextmanager
def frame(navigation_title: str):
    with ui.left_drawer().style(f'height: 100%; background-color: {color_scheme.secondary};') as left_drawer:
        menu()
    with ui.header().style(f'background-color: {color_scheme.primary};'):
        header(navigation_title, left_drawer)
    with ui.column().classes('absolute-center items-center'):
        yield
