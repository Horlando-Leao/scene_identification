from urllib.request import urlopen
from io import BytesIO

import cv2
import numpy as np
import requests as req
from PIL import Image, ImageFilter


class GetImageUrl:
    def __init__(self, url_image: str):
        self.url_image = url_image

    @property
    def url_image(self):
        return self._url_image

    @url_image.setter
    def url_image(self, value):
        if not isinstance(value, str):
            raise TypeError("atributo url_image precisa ser do tipo <str>")
        self._url_image = value

    def url_to_image_array(self):
        """RECEBE UMA URL STRING E RETORNA UMA IMAGEM FORMATADA EM ARRAY
        ,SALVA APENAS NA MÉMORIA RAM."""

        try:
            resp = urlopen(self.url_image)
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            return image
        except Exception as erro:
            print("ERRO:", erro)
            return False

    def url_to_image_download(self, path_for_save: str):
        """RECEBE UMA URL STRING E SALVA UMA IMAGEM,
        RETORNANDO O CAMINHO DA IMAGEM SALVA."""

        path = path_for_save

        with open(path, 'wb') as handle:
            response = req.get(self.url_image, stream=True)

            if not response.ok:
                print(response)
                return 'no-save'

            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
                return path

    def url_to_image_normal(self):
        """RECEBE UMA URL STRING E RETORNA UMA IMAGEM SEM FORMATAÇÃO
        ,SALVA APENAS NA MÉMORIA RAM."""

        response = req.get(self.url_image)
        im = Image.open(BytesIO(response.content))
        #im.show()  # mostrar imagem
        return (im)




#minhaimagem = GetImageUrl(url_image = "https://i.ytimg.com/vi/LKlH9Cdi_oA/maxresdefault.jpg")
#print(minhaimagem.url_to_image_normal())

