import smtplib
from email.message import EmailMessage
import os

def enviar_excel_por_correo(remitente, contraseña, destinatario, asunto, cuerpo, ruta_archivo_excel):
    # Crear el mensaje
    mensaje = EmailMessage()
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje.set_content(cuerpo)

    # Leer el archivo Excel
    with open(ruta_archivo_excel, 'rb') as f:
        contenido = f.read()
        nombre_archivo = os.path.basename(ruta_archivo_excel)
        mensaje.add_attachment(contenido, maintype='application',
                               subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                               filename=nombre_archivo)

    # Conectar al servidor SMTP (por ejemplo, Gmail)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(remitente, contraseña)
        smtp.send_message(mensaje)

# Ejemplo de uso
enviar_excel_por_correo(
    remitente='tucorreo@gmail.com',
    contraseña='tu_contraseña',
    destinatario='destinatario@example.com',
    asunto='Archivo Excel',
    cuerpo='Hola, adjunto el archivo Excel solicitado.',
    ruta_archivo_excel='datos.xlsx'
)
