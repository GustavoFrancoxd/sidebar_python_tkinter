from PIL import ImageTk, Image #TKINTER NO MANEJA ARCHIVOS PNG, PARA ESO ESTE PAQUETE

def leer_imagen(path, size):
    """ESTA FUNCION BUSCA LA RUTA DE LA IMAGEN Y TAMBIEN LA REDIMENCIONA"""
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))



