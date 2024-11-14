from nicegui import ui
from Front.components import menu, sidebar
ui.add_head_html('<link rel="stylesheet" href="styles/global.css">')


@ui.page('/')
def index():
    

ui.run()
