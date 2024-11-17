from nicegui import ui, app
from fastapi.responses import RedirectResponse
from Front.components import theme

def setup_login():
    @ui.page('/login')
    def login():
        if app.storage.user.get('authenticated', False):
            return RedirectResponse('/dashboard')

        def try_login():
            if email.value == "user@example.com" and password.value == "password":
                app.storage.user.update({'username': email.value, 'authenticated': True})
                ui.navigate.to(app.storage.user.get('referrer_path', '/dashboard'))  # CORRECCIÓN: cambiar ui.navigate() a ui.navigate.to()
            else:
                ui.notify('Credenciales incorrectas', color='negative')

        with theme.frame('Bienvenido a Agropecuaria'):
            with ui.card().classes('w-96 p-8'):
                ui.label('Bienvenido a Agropecuaria!').classes('text-2xl font-bold text-center mb-4')
                email = ui.input('Correo Electrónico').props('type=email')
                password = ui.input('Contraseña').props('type=password password-icon')
                ui.button('Entrar', on_click=try_login).props('color=primary').classes('mt-5 w-full')
                
    @ui.page('/logout')
    def logout():
        app.storage.user.clear()
        ui.navigate.to('/login')