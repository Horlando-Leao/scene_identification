from classmain import ImagesDetector
from otherclass import Utilities
from classmain import GetImageUrl
import time
import os


class ServicesDetectsAll:
    def __init__(self, url: str):
        self.url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise TypeError("URL precisa ser do tipo str")

        if not Utilities.Utilities.valid_url(value):
            raise FileNotFoundError("URL não é valida")
        self._url = value

    def main(self):
        image = GetImageUrl.GetImageUrl(self.url).url_to_image_array()
        detection = ImagesDetector.ImagesDetector(image)
        body = detection.detection_bodys()
        face = detection.detection_faces()
        gun = detection.detection_guns()

        return [body, face, gun]

# newservice = ServicesDetectsAll(url="https://i.ytmg.com/vi/LKlH9Cdi_oA/maxresdefault.jpg");
