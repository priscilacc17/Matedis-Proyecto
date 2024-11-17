from nicegui import ui, app
import os
from Front.components import theme, all_pages, login
from Front.pages import home
from Front.components.user import AuthMiddleware

ui.add_css(os.path.join(os.path.dirname(__file__), 'static/global.css'))

login.setup_login()
all_pages.create()
@ui.page('/')
def index() -> None:
        home.content()
app.add_middleware(AuthMiddleware)
ui.run(storage_secret='UNA_CLAVE_SECRETA_SEGURA')