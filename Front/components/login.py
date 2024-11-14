"""Libreria para crear una interfaz de usuario (GUI) en Python."""
from nicegui import ui

"""Libreria para estilos de botones."""
from Front.estilos.styles import button_style

def verificar_usuario(user, password):
    """Verificacion del usuario
    Args:
        user (str): correo electronico
        password (str): contraseña
    """
    if user == 'admin' and password == 'admin':
        ui.notify("Inicio de sesión exitoso.")
    else:
        ui.notify('Inicio de sesión fallido.')

def login():
    user = ui.input(label = 'Usuario', placeholder='Usuario').classes('w-1/2')
    user_password = ui.input(label = 'Contraseña', placeholder='Contraseña', password=True)
    ui.button('Iniciar sesión', on_click = lambda: verificar_usuario(user.value, user_password.value)).classes(button_style())
