from nicegui import ui, app
from Front.components import theme
from Front.pages import registro_animales, registro_usuarios, ubicacion, home

def create():
    @ui.page('/dashboard')
    def dashboard() -> None:
        if not app.storage.user.get('authenticated', False):
            ui.navigate.to('/login')
            return

        with theme.frame('Dashboard'):
            ui.label('Bienvenido al Dashboard de Agropecuaria').classes('text-lg')
    @ui.page('/')
    def index() -> None:
            home.content()
    @ui.page('/ubicacion/')
    def ubication() -> None:
        if not app.storage.user.get('authenticated', False):
            ui.navigate.to('/login')
            ui.notify('Debes iniciar sesión para acceder a esta modulo', color='negative').classes('mt-4')
            return
        """Ubicación Page"""
        with theme.frame('Ubicación'):
            ubicacion.content()

    @ui.page('/registro-de-animales/')
    def animales() -> None:
        if not app.storage.user.get('authenticated', False):
            ui.notify('Debes iniciar sesión para acceder a esta modulo', color='negative').classes('mt-4')
            ui.navigate.to('/login')
            return
        """Registro de Animales Page"""
        with theme.frame('Registro de animales'):
            registro_animales.content()

    @ui.page('/registro-de-usuarios/')
    def usuarios() -> None:
        if not app.storage.user.get('authenticated', False):
            ui.notify('Debes iniciar sesión para acceder a esta modulo', color='negative').classes('mt-4')
            ui.navigate.to('/login')
            return
        """Registro de Usuarios Page"""
        with theme.frame('Registro de usuarios'):
            registro_usuarios.content()
    