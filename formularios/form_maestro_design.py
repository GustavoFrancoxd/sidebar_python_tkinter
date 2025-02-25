import tkinter as tk
from tkinter import font

from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
import util.util_iconos as util_icon


class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (560, 136))  # Propiedad imagen logo
        self.perfil = util_img.leer_imagen("./imagenes/Perfil.png", (100, 100))

        # Configuración inicial de la ventana
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title("Python GUI")
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 1024, 600
        self.geometry("%dx%d+0+0" % (w, h))
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)  # Barra superior
        self.barra_superior.pack(side=tk.TOP, fill="both")

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)  # Menú lateral
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)  # Cuerpo principal
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        # Configuración de la barra superior

        # Generar el ícono de FontAwesome para el botón del menú lateral
        icon_code = "\uf0c9"  # Código Unicode del ícono de menú
        self.tk_image = util_icon.generar_icono_fontawesome(icon_code)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Autodidacta")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=21)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, image=self.tk_image, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", command=self.toggle_panel)
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de información
        self.labelTitulo = tk.Label(self.barra_superior, text="servicio@autodidacta.mx")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 200  # Ancho inicial de los botones
        alto_menu = 40  # Altura de los botones
        font_awesome = font.Font(family='FontAwesome', size=15)

        # Etiqueta de perfil
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        self.buttonDashBoard = tk.Button(self.menu_lateral)
        self.buttonProfile = tk.Button(self.menu_lateral)
        self.buttonPicture = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Dashboard", "\uf109", self.buttonDashBoard),
            ("Profile", "\uf007", self.buttonProfile),
            ("Picture", "\uf03e", self.buttonPicture),
            ("Info", "\uf129", self.buttonInfo),
            ("Settings", "\uf013", self.buttonSettings)
        ]

        for text, icon, button in buttons_info:
            # Generar el ícono de FontAwesome
            icon_image = util_icon.generar_icono_fontawesome(icon)

            # Configurar el botón con el ícono y el texto
            button.config(
                image=icon_image,
                compound=tk.LEFT,  # Coloca la imagen a la izquierda del texto
                text=f"  {text}",  # Espacio antes del texto para separarlo de la imagen
                anchor="w",  # Alinea el contenido a la izquierda
                font=font_awesome,
                bd=0,
                bg=COLOR_MENU_LATERAL,
                fg="white",
                width=ancho_menu,
                height=alto_menu,
                padx=10,  # Padding horizontal para separar el contenido de los bordes
                pady=5  # Padding vertical para separar el contenido de los bordes
            )
            button.image = icon_image  # Guardar una referencia para evitar que la imagen sea eliminada por el recolector de basura
            button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)  # Ajustar el padding y el relleno
            self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos enter y leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg="white")
        # Expandir el botón para ocupar el ancho del menú lateral
        button.pack_configure(fill=tk.X, padx=0)  # Eliminar el padding horizontal para que ocupe completamente el ancho

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')
        # Restaurar el tamaño original del botón
        button.pack_configure(fill=tk.X, padx=10)  # Restaurar el padding horizontal

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
            self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True) #se cambio aca el cuerpo principal
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)
            self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)