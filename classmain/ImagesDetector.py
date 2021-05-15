import cv2


class ImagesDetector:

    def __init__(self, image: bytes):
        self.image = image

    def __str__(self):
        return f'Object of type <class \'ImagesDetector\'> with variables [self.image]'

    def detection_bodys(self) -> int:
        """RECEBE UMA URL DE IMAGEM, E RETORNA A QUANTIDADE
        DE PARTES SUPERIORES DAS PESSOAS NA FOTO"""

        carregaAlgoritmo = cv2.CascadeClassifier("classmain/haarcascade/haarcascade_fullbody.xml")
        #print(carregaAlgoritmo)
        imagem = self.image

        # Limpando iamge
        scale_percent = 120  # percent of original size
        width = int(imagem.shape[1] * scale_percent / 100)
        height = int(imagem.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        imagem = cv2.resize(imagem, dim, interpolation=cv2.INTER_AREA)

        # =============================================
        # imagem = cv2.resize(imagem, (0,0), fx=1, fy=1)
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # DETECÇÃO DAS bodys
        bodys = carregaAlgoritmo.detectMultiScale(
            imagemCinza,
            scaleFactor=1.1,
            minNeighbors=3,  # abordagem de vizihança, (^) = + perder os verdadeiros positivos, (v) = + falsos positivos
            minSize=(1, 1),
            maxSize=(20, 60)
        )

        ##crie um retangulo nas bodys que detectMultiScale localizou
        """ for(x, y, l, a) in bodys:
            cv2.rectangle( imagem, ( x , y ), ( x + l, y + a ),( 0, 255, 0 ), 2 ) """

        ##exibe a imagem
        """ cv2.imshow("bodys", imagem)
        cv2.waitKey() """

        # Pequena regra de negócio
        count = 0
        try:
            for bodys_x in bodys:
                #print(bodys_x)
                count += 1

            print("Quat. de pessoas: ", count)
            return (count)

        except Exception as erro:
            print("Erro: ", EOFError)
            return (count)

    def detection_faces(self) -> int:
        """RECEBE UMA URL DE IMAGEM E RETORNA UMA QUANTIDADE DE FACES DETECTADAS"""

        carregaAlgoritmo = cv2.CascadeClassifier("classmain/haarcascade/haarcascade_frontalface_default.xml")

        imagem = self.image
        # imagem = cv2.imread('caminho')
        imagem = cv2.resize(imagem, (0, 0), fx=0.7, fy=0.7)
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # DETECÇÃO DAS FACES
        faces = carregaAlgoritmo.detectMultiScale(
            imagemCinza,
            scaleFactor=1.1,
            minNeighbors=3,  # abordagem de vizihança, (^) = + perder os verdadeiros positivos, (v) = + falsos positivos
            minSize=(20, 20)  # tamanho da detecção de uma face
        )

        # Pequena regra de negócio
        count = 0
        try:
            for faces_x in faces:
                #print(faces_x)
                count += 1
            print("Quat. de faces: ", count)
            return (count)

        except Exception as erro:
            print("Erro: ", EOFError)
            return (count)

    def detection_guns(self) -> int:
        """RECEBE UMA URL DE IMAGEM, E RETORNA A QUANTIDADE
                DE PARTES SUPERIORES DAS PESSOAS NA FOTO"""
        carregaAlgoritmo = cv2.CascadeClassifier("classmain/haarcascade/haarcascade_gun.xml")
        """RECEBE UMA URL DE IMAGEM E RETORNA UMA QUANTIDADE DE FACES DETECTADAS"""

        imagem = self.image
        # imagem = cv2.imread('caminho')
        imagem = cv2.resize(imagem, (0, 0), fx=0.1, fy=0.1)
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        # DETECÇÃO DAS FACES
        faces = carregaAlgoritmo.detectMultiScale(
            imagemCinza
        )

        # Pequena regra de negócio
        count = 0
        try:
            for faces_x in faces:
                print(faces_x)
                count += 1
            print("Quat. de faces: ", count)
            return (count)

        except Exception as erro:
            print("Erro: ", EOFError)
            return (count)


""" url = "https://www.tvsaj.com.br/wp-content/uploads/2020/06/Pessoa-em-situa%C3%A7%C3%A3o-de-rua-resgatada-pela-prefeitura-de-santo-antonio-de-jesus.jpeg"
url2 = "https://amenteemaravilhosa.com.br/wp-content/uploads/2018/09/homem-andnaod-e-mexendo-no-celular.jpg"
print(detection_bodys(url)) """
