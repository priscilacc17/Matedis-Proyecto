from nicegui import ui
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme

ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

def header(navigation_title, left_drawer) -> None:
    with ui.row().style('display: flex; width: 100%; background-color: #6DA34D; align-items: center;'):
        # Bloque Izquierdo - 25% del ancho
        with ui.row().style('flex: 0 0 285px; display: flex; align-items: center;'):
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            ui.image('Front/static/logo.png').style('width: 31.5px; height: auto; ')
            ui.label('MONDA').style(f'color: {color_scheme.text}; {font_scheme.h2}; margin: 0;')

        # Bloque Derecho - 75% del ancho
        with ui.row().style('flex: 1; display: flex; align-items: center; justify-content: center;'):
            ui.label(navigation_title).style(f'color: {color_scheme.text}; {font_scheme.h2}; text-align: center; margin: 0;')
            ui.button('Cerrar Sesión', on_click=lambda: ui.navigate.to('/logout')).props('color=negative').classes('mr-4').style('text-align: right;')