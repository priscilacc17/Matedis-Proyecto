from nicegui import ui
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme

ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

def header() -> None:
    with ui.header.style(f'display: flex; align-items: center; justify-content: space-between; width: 100%; height: 80px; background-color: {color_scheme.primary}; color: {color_scheme.text}; padding: 0 20px;'):
        ui.label("Titulo").style(f'{font_scheme.h1} padding: 5px; text-align: center; width: 100%;')