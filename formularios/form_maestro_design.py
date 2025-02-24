import  tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk

from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (560, 136))  # Propiedad imagen logo
        self.perfil = util_img.leer_imagen("./imagenes/Perfil.png", (100,100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()

    def config_window(self):
        #Configuracion inicial de la ventana
        self.title("Python GUI")
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 1024, 600
        self.geometry("%dx%d+0+0" % (w,h))
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        #Crear paneles: barra superior, menu lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50) #barra superior
        self.barra_superior.pack(side=tk.TOP, fill="both")

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150) #barra lateral
        self.menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL, width=150) #contenedor principal
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        #configuracion de la barra superior

        # Ruta al archivo .ttf de FontAwesome (descárgalo desde https://fontawesome.com/)
        font_path = "sidebar_python_tkinter/imagenes/fontawesome/fontawesome-free-6.7.2-desktop/otfs/Font Awesome 6 Free-Solid-900.otf"

        # Tamaño de la fuente y del ícono
        font_size = 40
        image_size = (50, 50)  # Tamaño de la imagen

        # Crear una imagen en blanco con fondo transparente
        image = Image.new("RGBA", image_size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)

        # Cargar la fuente FontAwesome
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print(
                "Error: No se pudo cargar la fuente FontAwesome. Asegúrate de que la ruta al archivo .ttf sea correcta.")
            exit()

        # Dibujar el ícono de FontAwesome en la imagen
        icon_code = "\uf0c9"  # Código Unicode del ícono de usuario ()
        draw.text((10, 10), icon_code, font=font, fill="black")

        # Convertir la imagen a un formato compatible con Tkinter
        self.tk_image = ImageTk.PhotoImage(image)


        #Etiqueta de titulo
        self.labelTitulo = tk.Label(self.barra_superior, text="Autodidacta")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        #Boton del menu lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, image=self.tk_image,
            bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
