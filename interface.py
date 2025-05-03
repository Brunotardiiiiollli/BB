import tkinter as tk
from PIL import Image, ImageTk
import threading
import time
import os

class InterfaceVisual:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sexta-feira")
        self.root.geometry("600x400")
        self.root.configure(bg='black')
        self.root.resizable(False, False)

        self.label_status = tk.Label(self.root, text="Aguardando comando...", fg="cyan", bg="black", font=("Consolas", 16))
        self.label_status.pack(pady=10)

        imagem = Image.open("audio/ia_face.png").resize((300, 300))
        self.imagem_ia = ImageTk.PhotoImage(imagem)
        self.label_imagem = tk.Label(self.root, image=self.imagem_ia, bg="black")
        self.label_imagem.pack()

        self.thread = threading.Thread(target=self.loop_visual)
        self.thread.daemon = True
        self.thread.start()

    def loop_visual(self):
        while True:
            time.sleep(1)

    def atualizar_status(self, texto):
        self.label_status.config(text=texto)

    def iniciar(self):
        self.root.mainloop()
