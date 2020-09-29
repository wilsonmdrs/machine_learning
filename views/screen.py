from tkinter import *
from modules.extracao_de_caracteristicas import Extract

class Application:
    def __init__(self, master=None):

        # Container de Botões
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack

        self.btnExtract = Button(self.container1, text="Extrair Características", font=self.fonte, width=12)
        self.btnExtract["command"] = Extract.extract_features







    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"


root = Tk()
Application(root)
root.mainloop()