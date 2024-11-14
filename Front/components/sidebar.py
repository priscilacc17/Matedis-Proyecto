from nicegui import ui
from Front.estilos.styles import sidebar_style, tabs_style

def sidebar() -> None :
    with ui.left_drawer().classes(sidebar_style()) :
        ui.link('Home', '/').classes(replace = tabs_style())
        ui.link('Ubicacion', '/ubicacion/').classes(replace = tabs_style())
        ui.link('Registro de animales', '/registro-de-animales/').classes(replace = tabs_style())
        