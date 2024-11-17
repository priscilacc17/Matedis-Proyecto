from nicegui import ui
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme

ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

def content() -> None:
    with ui.header().classes('flex justify-between p-4').style(f'background-color: {color_scheme.background};'):
        with ui.row().classes('flex items-center w-1/4'):
            ui.label('MONDA').style(f'color: {color_scheme.text}; {font_scheme.title}; margin: 0;')
        with ui.row().classes('1 flex justify-end'):
            ui.link('Home', '#home').style(f'color: {color_scheme.text}; {font_scheme.tab}').classes('p-4 no-underline')
            ui.link('¿Quienes somos?', '#quienes-somos').style(f'color: {color_scheme.text}; {font_scheme.tab}').classes('p-4 no-underline')
            ui.link('Modulos', '#modulos').style(f'color: {color_scheme.text}; {font_scheme.tab}').classes('p-4 no-underline')
            ui.link('Contacto', '#contacto').style(f'color: {color_scheme.text}; {font_scheme.tab}').classes('p-4 no-underline')
    with ui.element('section').props('id=home').style(f'background-color: {color_scheme.background};'):
        ui.button("Acceso", on_click=lambda: ui.navigate.to('/login')).style(f'background-color:{color_scheme.primary}; color{color_scheme.text} {font_scheme.tab}').classes('p-4 rounded-md')
    
    with ui.element('section').props('id=quienes-somos').style(f'background-color: {color_scheme.background};'):
        ui.label('¿Quienes somos?').style(f'color: {color_scheme.text}; {font_scheme.title}; margin: 0;')
        ui.label('Somos una empresa que se dedica a la venta de productos agricolas').style(f'color: {color_scheme.text}; {font_scheme.body1}; margin: 0;')
    
    with ui.element('section').props('id=modulos').style(f'background-color: {color_scheme.background};'):
        ui.label('Modulos').style(f'color: {color_scheme.text}; {font_scheme.title}; margin: 0;')
        ui.label('Modulo 1').style(f'color: {color_scheme.text}; {font_scheme.body1}; margin: 0;')
        ui.label('Modulo 2').style(f'color: {color_scheme.text}; {font_scheme.body1}; margin: 0;')
        ui.label('Modulo 3').style(f'color: {color_scheme.text}; {font_scheme.body1}; margin: 0;')
    
    with ui.element('section').props('id=contacto').style(f'background-color: {color_scheme.background};'):
        ui.label('Contacto').style(f'color: {color_scheme.text}; {font_scheme.title}; margin: 0;')
        ui.label('Correo: example@gmail.com').style(f'color: {color_scheme.text}; {font_scheme.body1}; margin: 0;')
        ui.label('Telefono: 1234567890').style(f'color: {color_scheme.text}; {font_scheme.body1}; margin: 0;')