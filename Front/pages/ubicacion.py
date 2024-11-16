from nicegui import ui
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme

ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

def content() -> None:
    ui.label("ubicacion")