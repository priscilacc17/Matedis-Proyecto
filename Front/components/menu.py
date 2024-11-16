"""Libreria para interfaz"""
from nicegui import ui
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme

ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

def menu() -> None:
    """Menu de navegacion (Tab)
    """
    ui.link('Home', '/').style(f'color: {color_scheme.text}; {font_scheme.body1}')
    ui.link('Ubicacion', '/ubicacion/').style(f'color: {color_scheme.text}; {font_scheme.body1}')
    ui.link('Registro de animales', '/registro-de-animales/').style(f'color: {color_scheme.text}; {font_scheme.body1}')
    ui.link('Registro de usuarios', '/registro-de-usuarios/').style(f'color: {color_scheme.text}; {font_scheme.body1}')
    