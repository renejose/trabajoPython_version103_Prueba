import tkinter as tk
import string
import random

# Lista de colores visibles
COLORES = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'orange', 'white', 'purple']

class LetreroAlfabeto:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Letrero Dinámico")
        self.ventana.attributes('-fullscreen', True)
        self.ventana.configure(bg='black')

        self.texto = tk.Label(
            self.ventana,
            text="ROSTILO",
            font=("Arial", 160, "bold"),
            fg="white",
            bg="black"
        )
        self.texto.pack(expand=True)

        self.letras = list(string.ascii_uppercase)
        self.index = 0

        self.ventana.bind("<Escape>", lambda e: self.ventana.destroy())
        self.cambiar_letra()

        self.ventana.mainloop()

    def cambiar_letra(self):
        letra_actual = self.letras[self.index % len(self.letras)]
        color = random.choice(COLORES)
        self.texto.config(text=letra_actual, fg=color)
        self.index += 1
        self.ventana.after(2000, self.cambiar_letra)  # cambia cada 2 segundos ss

LetreroAlfabeto()
