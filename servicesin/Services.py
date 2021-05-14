from classmain import GetImageUrl
from classmain import ImagesDetector
from otherclass import Utilities


class ServicesDetectsAll(GetImageUrl.GetImageUrl, ImagesDetector.ImagesDetector):
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
        body = self.detection_bodys(self.url_to_image_normal(self.url))
        return body

# newservice = ServicesDetectsAll(url="https://i.ytmg.com/vi/LKlH9Cdi_oA/maxresdefault.jpg");
