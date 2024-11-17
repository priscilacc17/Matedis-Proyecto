# user.py (Middleware)
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import RedirectResponse
from nicegui import app

# Definimos las rutas permitidas sin autenticación
unrestricted_page_routes = {'/login', '/'}

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # Verificar si app.storage está disponible y correctamente inicializado
        if not hasattr(app.storage, 'user'):
            return await call_next(request)

        # Permitir el acceso a las rutas internas de NiceGUI
        if request.url.path.startswith('/_nicegui'):
            return await call_next(request)

        # Comprobar si el usuario está autenticado
        if not app.storage.user.get('authenticated', False):
            # Si el usuario no está autenticado y no está en una página permitida
            if request.url.path not in unrestricted_page_routes:
                # Asegurar que no intente redirigir a /login si ya está en /login
                if request.url.path != '/login':
                    app.storage.user['referrer_path'] = request.url.path
                    return RedirectResponse('/login')

        # Continuar con la solicitud si el usuario está autenticado o la página está permitida
        return await call_next(request)
