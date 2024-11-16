from nicegui import ui
from Front.components import theme
from Front.pages import home
from Front.components import all_pages
ui.add_head_html('Front/estilos/global.css')

all_pages.create()

ui.run()
