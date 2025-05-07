def collatz(n):
    while n != 1:
        print(n, end=' → ')
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(1)

# Solicitar al usuario un número entero positivo
try:
    num = int(input("Ingresa un número entero positivo: "))
    if num > 0:
        collatz(num)
    else:
        print("Por favor, ingresa un número mayor que 0.")
except ValueError:
    print("Entrada no válida. Asegúrate de ingresar un número entero.")



import yt_dlp

def descargar_video(url):
    opciones = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [progreso_descarga],
    }
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

def progreso_descarga(d):
    if d['status'] == 'downloading':
        print(f"Descargando: {d['_percent_str']} - {d['_eta_str']} restantes")
    elif d['status'] == 'finished':
        print(f"\n¡Descarga completada! Guardado como: {d['filename']}")

if __name__ == "__main__":
    url_video = input("Ingresa la URL del video de YouTube: ")
    descargar_video(url_video)
