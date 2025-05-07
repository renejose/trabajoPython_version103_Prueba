import yt_dlp
import os

def descargar_audio(url, carpeta_destino="mis_audios"):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',
        'postprocessors': [
            {   
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }
        ],
        'quiet': False,  # Cambiar a True si quieres menos texto en consola
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Pega el enlace de YouTube: ").strip()
    descargar_audio(url)
    print("¡Descarga completa!")