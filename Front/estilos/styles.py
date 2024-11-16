from nicegui import ui
from colors import colorScheme
from fonts import fontScheme

ui_obj = ui
color_scheme = colorScheme(ui_obj)
font_scheme = fontScheme(color_scheme)

head_style = """
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
body {
    font-family: 'Poppins';
    background-color: #0A0B0C;
    margin: 0;
}
"""
ui_obj.add_head_html(f'<style>{head_style}</style>')
