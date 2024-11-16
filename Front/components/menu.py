from nicegui import ui
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme

ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

def menu() -> None:
    """Menu de navegación (barra lateral)
    
    Tabs:
    - Home
    - Ubicación
    - Registro de animales
    - Registro de usuarios
    """ 
    # Tab - Home
    ui.link('Home', '/').style(f' color: {font_scheme.body2} background-color: {color_scheme.background};').classes(add='nav-link w-full p-4 no-underline rounded-md')
    # Tab - Ubicación
    ui.link('Ubicación', '/ubicacion/').style(f' color: {font_scheme.body2} background-color: {color_scheme.background};').classes(add='nav-link w-full p-4 no-underline rounded-md')
    # Tab - Registro de animales
    ui.link('Registro de animales', '/registro-de-animales/').style(f' color: {font_scheme.body2} background-color: {color_scheme.background};').classes(add='nav-link w-full p-4 no-underline rounded-md')
    # Tab - Registro de usuarios
    ui.link('Registro de usuarios', '/registro-de-usuarios/').style(f' color: {font_scheme.body2} background-color: {color_scheme.background};').classes(add='nav-link w-full p-4 no-underline rounded-md')
