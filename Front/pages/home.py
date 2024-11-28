from nicegui import ui, app
from Front.estilos.colors import colorScheme
from Front.estilos.fonts import fontScheme

ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

def content() -> None:
    # Encabezado con enlaces de navegación
    with ui.header().classes('flex justify-between items-center p-4 w-full').style(f'background-color: {color_scheme.background};'):
        with ui.row().classes('flex items-center w-1/4'):
            ui.label('MONDA').style(f'color: {color_scheme.secondary}; {font_scheme.title}; margin: 0;')

        # Enlaces de navegación
        with ui.row().classes('flex justify-end'):
            ui.link('Home', '#home').style(f'color: {color_scheme.text}; {font_scheme.tab}').classes('p-4 no-underline')
            ui.link('¿Quienes somos?', '#quienes-somos').style(f'color: {color_scheme.text}; {font_scheme.tab}').classes('p-4 no-underline')
            ui.link('Módulos', '#modulos').style(f'color: {color_scheme.text}; {font_scheme.tab}').classes('p-4 no-underline')

    # Sección Home 
    with ui.column().classes('w-full h-full p-8 bg-opacity-70 bg-white').props('id=home'):
        # Contenedor para el título y el botón de acceso
        with ui.row().classes('w-full justify-between items-center'):
            # Contenido textual (título)
            with ui.column().classes('w-3/4 p-4'):
                ui.label('Software de monitoreo y gestión para el control').style(f'color: {color_scheme.text}; {font_scheme.title};')
                ui.label('del crecimiento y la alimentación del ganado en').style(f'color: {color_scheme.text}; {font_scheme.title};')
                ui.label('una granja').style(f'color: {color_scheme.text}; {font_scheme.title};')
                ui.button('Acceso', on_click=lambda: ui.navigate.to('/login')).classes('mt-4 bg-primary text-white rounded-lg p-3 w-1/6').style(
                f'background-color: {color_scheme.color_box}; {font_scheme.body1}'
            )
            # Imagen del logo
            ui.image('Front/static/logo.png').classes('flex').style('width: 300px; height: auto; margin-right: 20px;')

    # Tarjetas explicativas en la parte inferior de la sección Home
    with ui.row().classes('w-full flex justify-center mt-12 gap-4'):
        # Cada una de las tarjetas
        with ui.column().classes('w-1/4 p-6 bg-white rounded-lg shadow-md mx-8'):
            ui.label('¿Qué hace por ti MONDA?').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.secondary};')
            ui.label('Monda es la solución completa para ganaderos que centraliza y automatiza el manejo de datos clave en tiempo real, eliminando la fragmentación y errores de los métodos tradicionales.').style(
                f'color: {color_scheme.text}; {font_scheme.body2};')

        with ui.column().classes('w-1/4 p-6 bg-white rounded-lg shadow-md mx-8'):
            ui.label('Gestión de ganadería').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.secondary};')
            ui.label('Permite el monitoreo del crecimiento, las necesidades de alimentación y el estado de salud de cada animal, optimizando el control de la producción y facilitando las proyecciones de crecimiento y consumo.').style(
                f'color: {color_scheme.text}; {font_scheme.body2};')

        with ui.column().classes('w-1/4 p-6 bg-white rounded-lg shadow-md mx-8'):
            ui.label('Información general').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.secondary};')
            ui.label('Ayuda a gestionar los recursos necesarios para el funcionamiento de la granja, integrando todos los aspectos del sistema productivo en una sola plataforma de fácil acceso.').style(
                f'color: {color_scheme.text}; {font_scheme.body2};')
    # Sección ¿Quiénes somos?
    with ui.row().classes('w-full flex gap-8 p-12 bg-gray-50').props('id=quienes-somos'):
        # Imagen a la izquierda
        with ui.column().classes('w-1/4'):
            ui.image('Front/static/farm.jpeg').style('width: 100%; height: auto; border-radius: 10px;')

        # Contenido a la derecha
        with ui.column().classes('flex flex-col justify-start items-start gap-8'):
        # Título y descripción general
            with ui.column().classes('flex items-start gap-2 mx-7'):
                ui.label('¿Quiénes somos?').classes('text-xl font-bold mb-4').style(f'color: {color_scheme.text};')
                ui.label('Somos una empresa que se dedica a la venta de productos agrícolas y monitoreo de granjas.').classes('text-base leading-relaxed').style(f'color: {color_scheme.text}; {font_scheme.body2};')
            with ui.column().classes('w-full flex gap-8 mt-6'):
                # Historia
                with ui.column().classes('flex flex-col items-start gap-2 mx-7'):
                    with ui.row():
                        ui.icon('history', size='60').classes('mb-2')
                        ui.label('Historia').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.text};')
                    ui.label('Nuestro proyecto nació al ver los desafíos de la ganadería moderna y la falta de herramientas efectivas.').classes('text-base leading-relaxed ml-8').style(f'color: {color_scheme.text}; {font_scheme.body2};')
                
                # Motivación
                with ui.column().classes('flex flex-col items-start gap-2 mx-7'):
                    with ui.row():
                        ui.icon('insights', size='60').classes('mb-2')
                        ui.label('Motivación').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.text};')
                    ui.label('Nuestra motivación es transformar los datos en información útil para mejorar la productividad de las granjas.').classes('text-base leading-relaxed ml-8').style(f'color: {color_scheme.text}; {font_scheme.body2};')

    # Sección Módulos
    with ui.row().classes('w-full flex items-center justify-center mt-5').props('id=modulos'):
        ui.label('Módulos').classes('text-xl font-bold mb-6').style(f'color: {color_scheme.text};')
    with ui.column().classes('w-full p-8 text-center bg-gray-50'):
        with ui.row().classes('w-full flex items-center justify-center gap-8'):
            
            with ui.column().classes('p-4 w-1/4 items-center shadow-lg mx-8 my-6'):
                ui.icon('location_on', size='48').classes('mb-4')
                ui.label('Ubicación').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.text};')
                ui.label('Información gráfica para el usuario sobre el crecimiento proyectado.').style(f'color: {color_scheme.text}; {font_scheme.body2};')
                
            with ui.column().classes('p-4 w-1/4 items-center shadow-lg mx-8 my-6'):
                ui.icon('pets', size='48').classes('mb-4')
                ui.label('Registro de animales').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.text};')
                ui.label('Dispone del registro de animales y sus características.').style(f'color: {color_scheme.text}; {font_scheme.body2};')

            with ui.column().classes('p-4 w-1/4 items-center shadow-lg mx-8 my-6'):
                ui.icon('agriculture', size='48').classes('mb-4')
                ui.label('Registro de granjeros').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.text};')
                ui.label('Dashboard con indicadores de crecimiento.').style(f'color: {color_scheme.text}; {font_scheme.body2};')

            with ui.column().classes('p-4 w-1/4 items-center shadow-lg mx-8 my-6'):
                ui.icon('analytics', size='48').classes('mb-4')
                ui.label('Proyeccion de crecimiento').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.text};')
                ui.label('Dashboard con indicadores de crecimiento.').style(f'color: {color_scheme.text}; {font_scheme.body2};')
            
            with ui.column().classes('p-4 w-1/4 items-center shadow-lg mx-8 my-6'):
                ui.icon('analytics', size='48').classes('mb-4')
                ui.label('Proyeccion de consumo').classes('font-bold text-lg mb-2').style(f'color: {color_scheme.text};')
                ui.label('Dashboard con indicadores de crecimiento.').style(f'color: {color_scheme.text}; {font_scheme.body2};')
    # Sección Contacto
    with ui.footer(value=False).classes('bg-gray-600') as footer:
        with ui.column().classes('w-full flex justify-center items-center p-2 rounded-lg text-center'):
        # Encabezado del footer
            ui.label('Contáctanos').classes('text-2xl font-bold mb-3').style('color: white;')

        # Contenedor para las tarjetas de contacto
        with ui.row().classes('w-full justify-center gap-4'):
            # Tarjeta de Correo Electrónico
            with ui.column().classes('p-4 bg-white rounded-lg shadow-md items-center w-1/4 mx-28'):
                with ui.row().classes('items-center'):
                    ui.icon('email', size='48').style('color: #F9A825;')
                    ui.label('Correo electrónico').classes('font-bold text-lg').style(f'color: {color_scheme.text};')
                ui.label('example@gmail.com').style(f'color: {color_scheme.text}; {font_scheme.body2};')
                ui.label('example@gmail.com').style(f'color: {color_scheme.text}; {font_scheme.body2};')

            # Tarjeta de Teléfono
            with ui.column().classes('p-4 bg-white rounded-lg shadow-md items-center w-1/4 mx-28'):
                with ui.row().classes('items-center'):
                    ui.icon('phone', size='48').style('color: #F9A825;')
                    ui.label('Teléfono').classes('font-bold text-lg').style(f'color: {color_scheme.text};')
                ui.label('+51 999999999').style(f'color: {color_scheme.text}; {font_scheme.body2};')
                ui.label('+51 999999999').style(f'color: {color_scheme.text}; {font_scheme.body2};')
    
    with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon='contact_support').props('fab')
