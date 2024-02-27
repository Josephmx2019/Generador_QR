import sys
import qrcode
import os
import qrcode_terminal

def generar_qr(url, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    imagen = qr.make_image(fill_color="black", back_color="white")

    extension = input("Digita la extensión (Con punto ejemplo .png)")

    nombre_archivo += extension
    imagen.save(nombre_archivo)

    # Muestra la ubicación del archivo
    print("El código QR ha sido generado en:", os.path.abspath(nombre_archivo))

def imprimir_qr(url):
    qrcode_terminal.draw(url)

def obtener_datos_manualmente():
    enlace = input("Introduce el enlace que deseas convertir en código QR: ")
    nombre_archivo = input("Introduce el nombre del archivo para guardar el código QR (sin extensión): ")
    return enlace, nombre_archivo

def main():
  opc = 'S'
  while(opc != 'N'):
    if len(sys.argv) == 3:
        enlace = sys.argv[1]
        nombre_archivo = sys.argv[2]
    else:
        enlace, nombre_archivo = obtener_datos_manualmente()

    generar_qr(enlace, nombre_archivo)
    imprimir_qr(enlace)
    opc = input("¿Quieres continuar? S/N: ")

if __name__ == "__main__":
    main()
