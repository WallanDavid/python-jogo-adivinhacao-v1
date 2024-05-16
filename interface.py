import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivinhação de Números")

        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

        self.label = tk.Label(root, text="Adivinhe o número secreto entre 1 e 100:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Enviar", command=self.verificar_palpite)
        self.button.pack()

    def verificar_palpite(self):
        palpite = self.entry.get()

        if not palpite.isdigit():
            messagebox.showerror("Erro", "Por favor, digite um número válido.")
            return

        palpite = int(palpite)
        self.tentativas += 1

        if palpite < self.numero_secreto:
            messagebox.showinfo("Resultado", "Muito baixo! Tente novamente.")
        elif palpite > self.numero_secreto:
            messagebox.showinfo("Resultado", "Muito alto! Tente novamente.")
        else:
            messagebox.showinfo("Parabéns", f"Você adivinhou o número em {self.tentativas} tentativas.")
            self.root.quit()

# Configuração da janela principal
root = tk.Tk()
jogo = JogoAdivinhacao(root)

# Executar o loop principal da interface
root.mainloop()