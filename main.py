from nicegui import ui
from Front.components import theme
from Front.components import header
from Front.pages import home


@ui.page('/')
def index() -> None:
        with theme.frame('Home'):
                home.content()
                

ui.run()
