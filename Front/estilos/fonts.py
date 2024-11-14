class fontScheme:
    """Clase que contiene las fuentes de la aplicación
    
    ...
    Atributos:
    -----------
    primary_font : str
        Fuente primaria del sistema de diseño.
    secondary_font : str
        Fuente secundaria del sistema de diseño.
    h1 : str
        Estilos para encabezados H1.
    h2 : str
        Estilos para encabezados H2.
    h3 : str
        Estilos para encabezados H3.
    h4 : str
        Estilos para encabezados H4.
    h5 : str
        Estilos para encabezados H5.
    h6 : str
        Estilos para encabezados H6.
    subtitle1 : str
        Estilos para subtítulos de primer nivel.
    subtitle2 : str
        Estilos para subtítulos de segundo nivel.
    body1 : str
        Estilos para texto del cuerpo principal.
    body2 : str
        Estilos para texto del cuerpo secundario.
    caption : str
        Estilos para subtítulos.
    overline : str
        Estilos para sobrelineas.
    """
    def __init__(self,color_scheme):
        self.primary_font = 'Roboto'
        self.secondary_font = 'serif'
        
        #headers
        self.h1 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '2em', 'bold', color_scheme['white'])
        self.h2 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '1.5em', 'bold', color_scheme['white'])
        self.h3 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '1.17em', 'bold', color_scheme['white'])
        self.h4 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '1em', 'bold', color_scheme['white'])
        self.h5 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '0.875em', 'bold', color_scheme['white'])
        self.h6 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '0.75em', 'bold', color_scheme['white'])
        
        #subtitulos
        self.subtitle1 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '1em', 'medium', color_scheme['white'])
        self.subtitle2 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '0.875em', 'medium', color_scheme['white'])
        
        #texto del cuerpo
        self.body1 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '1em', 'normal', color_scheme['white'])
        self.body2 = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.secondary_font, '0.875em', 'normal', color_scheme['white'])
        
        #caption y overline
        self.caption = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '0.75em', 'light', color_scheme['white'])
        self.overline = "font-family: {}; font-size: {}; font-weight: {}; color: {};".format(self.primary_font, '0.625em', 'light', color_scheme['white'])