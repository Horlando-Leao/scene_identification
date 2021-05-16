from flask import json

from app.main import app
from otherclass import Utilities
from servicesin import Services


# rota de teste
@app.route("/", methods=["GET"])
def index() -> json:
    return "<H1>Page Index<H1>"


@app.route("/detectsall/<string:url>", methods=["GET"])
def detectsall(url: str) -> json:
    url = url.replace("||", "/")

    if not Utilities.Utilities.valid_url(url):
        return response_generator(400, "o parametro (url) é obrigatório")

    result = Services.ServicesDetectsAll(url).main()
    return response_generator(status=200,
                              message="Imagem processada com sucesso",
                              number_people=int(result[0]),
                              number_faces=int(result[1]),
                              number_guns=int(result[2]),
                              url=url)


def response_generator(status: int,
                       message: str,
                       number_people: int = "",
                       number_faces: int = "",
                       number_guns: int = "",
                       url: str = ""):
    response = {}
    response["status"] = status
    response["mensagem"] = message
    response["data"] = {
        "number_people": number_people,
        "number_faces": number_faces,
        "number_guns": number_guns
    }
    response["url"] = url
    return response
