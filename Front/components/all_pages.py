from nicegui import ui
from Front.components import theme
from Front.pages import home, registro_animales, registro_usuarios, ubicacion

def create():
    @ui.page('/')
    def index() -> None:
        """Home Page - Página principal"""
        with theme.frame('Home'):
            home.content()

    @ui.page('/ubicacion/')
    def ubication() -> None:
        """Ubicación Page"""
        with theme.frame('Ubicación'):
            ubicacion.content()

    @ui.page('/registro-de-animales/')
    def animales() -> None:
        """Registro de Animales Page"""
        with theme.frame('Registro de animales'):
            registro_animales.content()

    @ui.page('/registro-de-usuarios/')
    def usuarios() -> None:
        """Registro de Usuarios Page"""
        with theme.frame('Registro de usuarios'):
            registro_usuarios.content()