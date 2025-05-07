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
