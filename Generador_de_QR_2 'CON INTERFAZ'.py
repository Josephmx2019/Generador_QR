import qrcode
import os
import qrcode_terminal
import tkinter as tk
from tkinter import simpledialog, messagebox

def generar_qr(url, nombre_archivo, extension):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    imagen = qr.make_image(fill_color="black", back_color="white")

    nombre_archivo += extension
    imagen.save(nombre_archivo)

    # Muestra la ubicación del archivo
    print("El código QR ha sido generado en:", os.path.abspath(nombre_archivo))

def imprimir_qr(url):
    qrcode_terminal.draw(url)

def obtener_datos_gui():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    enlace = simpledialog.askstring("Generador de QR", "Introduce el enlace que deseas convertir en código QR:")
    extension = simpledialog.askstring("Generador de QR", "Introduce la extensión del archivo (por ejemplo, '.png'):")
    nombre_archivo = simpledialog.askstring("Generador de QR", "Introduce el nombre del archivo para guardar el código QR (sin extensión):")
    root.destroy()  # Cerrar la ventana principal
    return enlace, nombre_archivo, extension

def main():
    try:
        while True:
            enlace, nombre_archivo, extension = obtener_datos_gui()
            generar_qr(enlace, nombre_archivo, extension)
            imprimir_qr(enlace)
            respuesta = messagebox.askyesno("Generador de QR", "¿Deseas generar otro código QR?")
            if not respuesta:
                break
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
