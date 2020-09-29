from tkinter import *
from modules.extracao_de_caracteristicas import Extract
from tkinter.filedialog import askopenfilename

import os
# extensao arff
import arff

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "12")

        # Container de Botões
        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1.pack()



        # Botão Extrair Características
        self.btnExtract = Button(self.container1, text="Extrair Características",
                                 font=self.fonte, width=20 )
        self.btnExtract["command"] = self.extract
        self.btnExtract.pack(side=LEFT)

        # Botão Selecionar Imagem
        self.btnSelect = Button(self.container1, text="Selecionar Imagem",
                                 font=self.fonte, width=20)
        self.btnSelect["command"] = self.select_image
        self.btnSelect.pack(side=LEFT)

        # Botão Selecionar Imagem
        self.btnClassify = Button(self.container1, text="Classificar",
                                font=self.fonte, width=20)
        self.btnClassify["command"] = self.select_image
        self.btnClassify.pack(side=RIGHT)

        # Container de Imagens
        self.container2 = Frame(master)
        self.container2["pady"] = 10
        self.container2["padx"] = 5
        self.container2.pack(side=LEFT)

        # Container de Classificação
        self.container3 = Frame(master)
        self.container3["pady"] = 10
        self.container3["padx"] = 5
        self.container3.pack(side=RIGHT)
        # self.container3.grid(row=1, column=1)

        self.container4 = Frame(master)
        self.container4.pack(side=RIGHT)
        self.container5 = Frame(master)
        self.container5.pack(side=RIGHT)
        self.container6 = Frame(master)
        self.container6.pack(side=RIGHT)
        self.container7 = Frame(master)
        self.container7.pack(side=RIGHT)
        self.container8 = Frame(master)
        self.container8.pack(side=RIGHT)

        self.lblfeatures = Label(self.container3, text="Características",
                              font=22, justify=CENTER)
        self.lblfeatures.pack(side=TOP)

        self.lblapu = Label(self.container4, text="APU",
                                 font=22, justify=CENTER)
        self.lblapu.pack(side=LEFT)

        self.lblapufeatureone = Label(self.container5, text="Cor da Pele",
                            font=22, justify=CENTER)
        self.lblapufeatureone.pack(side=LEFT)

        self.lblapufeaturetwo = Label(self.container6, text="Cor da Jaqueta",
                            font=22, justify=CENTER)
        self.lblapufeaturetwo.pack(side=LEFT)

        self.lblapufeaturethree = Label(self.container7, text="Cor da Calça",
                            font=22, justify=CENTER)
        self.lblapufeaturethree.pack(side=LEFT)

        self.lblnelson = Label(self.container4, text="NELSON",
                                 font=22, justify=CENTER)
        self.lblnelson.pack(side=RIGHT)

        self.lblnelsonfeatureone = Label(self.container5, text="Cor da Pele",
                                      font=22, justify=CENTER)
        self.lblnelsonfeatureone.pack(side=LEFT)

        self.lblnelsonfeaturetwo = Label(self.container6, text="Cor do Colete",
                                      font=22, justify=CENTER)
        self.lblnelsonfeaturetwo.pack(side=LEFT)

        self.lblnelsonfeaturethree = Label(self.container7, text="Cor da Camisa",
                                        font=22, justify=CENTER)
        self.lblnelsonfeaturethree.pack(side=LEFT)


        #
        #
        #
        # self.lbloriginal = Label(self.container2, text="Imagem Original",
        #                       font=22, justify=CENTER )
        # self.lbloriginal.pack(side=TOP)
        # self.lblprocessed = Label(self.container3, text="Imagem Processada",
        #                          font=22 )
        # self.lblprocessed.pack(side=TOP)
        #
        # self.imgoriginal = PhotoImage(file="images/img.png")
        # self.lblimage1 = Label(self.container2, image=self.imgoriginal).pack()

    def extract(self):
        # carregando a imagem
        data = []
        # Carregando a lista de Imagens
        images = os.listdir('images/coaching')
        for img in images:
            data += [Extract.extract_feature('images/coaching/' + img, False)]

        # gerando arquivo .arrf
        attributes = [
            'cor_da_pele_Apu',
            'cor_da_jaqueta_Apu',
            'cor_da_calca_Apu',
            'cor_da_pele_nelson',
            'cor_do_colete_nelson',
            'cor_da_camisa_nelson',
            'classe {Apu, Nelson}'
        ]
        try:
            arff.dump('caracteristicas.arff', data, relation="caracteristicas", names=attributes)
        except NameError:
            print('error', NameError)

    def select_image(self):
        Tk().withdraw()
        filename = askopenfilename()
        Extract.extract_feature(filename, True)


root = Tk()
Application(root)
root.mainloop()


    # Plot normal and equalized image



