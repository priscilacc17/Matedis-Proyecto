"""Libreria para interfaz"""
from nicegui import ui

def menu():
    """Menu de navegacion (Tab)
    """
    ui.link('Home', '/').classes(replace = 'text-black')
    ui.link('Ubicacion', '/ubicacion/').classes(replace = 'text-black')
    ui.link('Registro de animales', '/registro-de-animales/').classes(replace = 'text-black')
    ui.link('Registro de usuarios', '/registro-de-usuarios/').classes(replace = 'text-black')
    