# Pillow para manipulação de imagem
from PIL import Image
## import Matplotlib
import matplotlib.pyplot as pp


class Extract:

    def __init__(self):
        pass

    @staticmethod
    def extract_feature(img, show):

        # características de extração

        character_one_feature_one = 0 # Abu - Cor da Pele
        character_one_feature_two = 0 # Abu - Cor do Casaco
        character_one_feature_three = 0 # Abu - Cor da Calca
        character_two_feature_one = 0 # Nelson - Cor da Pele
        character_two_feature_two = 0 # Nelson - Cor do Colete
        character_two_feature_three = 0 # Nelson -  Cor da Camisa
        character = 'Apu'

        # Lista de caracteriscas que serão extraidas
        features = []

        # Segrega de quem é  a imagem
        if img[16] == 'n':
            character = 'Nelson'
        # Exibe o Caminho da Imagem no Console
        print('Caminho ', img)

        # Importa a imagem do diretório
        original = Image.open(img)
        processed = Image.open(img)

        # Pega as coordenanadas da imagem
        width, height = processed.size

        # Loop que percorre cada Pixel da imagem
        for x in range(0, height):
            for y in range(0, width):

                #extrai a cor Red Green e Blue da Imagem
                r, g, b = processed.getpixel((y, x))
                # print("Red: {0}, Green: {1}, Blue: {2}".format(r, g, b))

                # verifica se existe a característica na imagem
                if (x > height / 4) and Extract.has_feature_one_character_one(r, g, b):
                    character_one_feature_one += 1
                    processed.putpixel((y, x), (213, 76, 233))
                if Extract.has_feature_two_character_one(r, g, b):
                    character_one_feature_two += 1
                    processed.putpixel((y, x), (213, 76, 233))
                if (x > height / 2) and Extract.has_feature_three_character_one(r, g, b):
                    character_one_feature_three += 1
                    processed.putpixel((y, x), (213, 76, 233))
                if Extract.has_feature_one_character_two(r, g, b):
                    character_two_feature_one += 1
                    processed.putpixel((y, x), (0, 255, 255))
                if (x > height / 2) and Extract.has_feature_two_character_two(r, g, b):
                    character_two_feature_two += 1
                    processed.putpixel((y, x), (0, 255, 255))
                if (x > height / 2) and Extract.has_feature_three_character_two(r, g, b):
                    character_two_feature_three += 1
                    processed.putpixel((y, x), (0, 255, 255))

        # salva o resultado da extração
        features = [
            (character_one_feature_one / (width * height)) * 100,
            (character_one_feature_two / (width * height)) * 100,
            (character_one_feature_three / (width * height)) * 100,
            (character_two_feature_one / (width * height)) * 100,
            (character_two_feature_two / (width * height)) * 100,
            (character_two_feature_three / (width * height)) * 100,
            character
        ]
        # Imprime no console as características extraidas da imagem
        print("Caracteristicas extraidas", features)

        if show:
            # percorre a lista e monta as duas imagens
            fig, ax = pp.subplots(2, 1, figsize=(5, 7))  # Lines and cols
            ax[0].imshow(original)
            ax[0].set_title('Imagem Original')
            ax[0].axis('off')
            ax[1].imshow(processed)
            ax[1].set_title('Imagem Processada')
            ax[1].axis('off')
            pp.show()
        return features

    @classmethod
    def has_feature_one_character_one(cls, r, g, b):
        if 90 <= r <= 255 and 35 <= g <= 160 and 0 <= b <= 50:
            return True
        else:
            return False

    @classmethod
    def has_feature_two_character_one(cls, r, g, b):
        if 10 <= r <= 57 and 91 <= g <= 255 and 15 <= b <= 81:
            return True
        else:
            return False

    @classmethod
    def has_feature_three_character_one(cls, r, g, b):
        if 192 <= r <= 255 and 180 <= g <= 252 and 74 <= b <= 150:
            return True
        else:
            return False

    @classmethod
    def has_feature_one_character_two(cls, r, g, b):
        if 185 <= r <= 255 and 155 <= g <= 215 and 15 <= b <= 70:
            return True
        else:
            return False

    @classmethod
    def has_feature_two_character_two(cls, r, g, b):
        if 80 <= r <= 160 and 111 <= g <= 175 and 168 <= b <= 250:
            return True
        else:
            return False

    @classmethod
    def has_feature_three_character_two(cls, r, g, b):
        if 180 <= r <= 255 and 98 <= g <= 180 and 74 <= b <= 122:
            return True
        else:
            return False
