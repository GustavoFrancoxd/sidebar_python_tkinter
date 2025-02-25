from PIL import Image, ImageDraw, ImageFont, ImageTk

def generar_icono_fontawesome(icon_code, font_size=22, image_size=(40, 40), color="white"):
    """
    Genera un ícono de FontAwesome como una imagen compatible con Tkinter.
    :param icon_code: Código Unicode del ícono de FontAwesome (ej: "\uf109").
    :param font_size: Tamaño de la fuente del ícono.
    :param image_size: Tamaño de la imagen resultante.
    :param color: Color del ícono.
    :return: Objeto ImageTk.PhotoImage con el ícono.
    """

    # Ruta al archivo .ttf de FontAwesome (descargado desde https://fontawesome.com/)
    font_path = "./imagenes/fontawesome/otfs/Font Awesome 6 Free-Solid-900.otf"

    image = Image.new("RGBA", image_size, (255, 255, 255, 0))  # Imagen con fondo transparente
    draw = ImageDraw.Draw(image)
    try:
        font_awesome = ImageFont.truetype(font_path, font_size)  # Cargar la fuente FontAwesome
    except IOError:
        print("Error: No se pudo cargar la fuente FontAwesome. Asegúrate de que la ruta al archivo .ttf sea correcta.")
        exit()
    draw.text((10, 10), icon_code, font=font_awesome, fill=color)  # Dibujar el ícono
    return ImageTk.PhotoImage(image)