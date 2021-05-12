from main import app
from otherclass import Utilities
from servicesin import Services
# rota de teste
@app.route("/olamundo/<string:user>", methods=["GET"])
def olaMundo(user: str) -> str:
    return {"Olá": "{0}".format(user)}


@app.route("/detectartudo/<string:url>", methods=["GET"])
def detect_no_treat(url):
    url = url.replace("||", "/")

    if not Utilities.Utilities.valid_url(url):
        return response_generator(400, "o parametro (url) é obrigatório")

    result = Services.ServicesDetectsAll(url)
    return response_generator(200, "Imagem processada com sucesso", str(result[0]), str(result[1]), str(result[2]),
                              str(result[3]))



def response_generator(status: int, mensage: str, quatPeople: str = "", quatFaces: str = "", probilidGun: str = "",
                       noProbilidGun: str = ""):
    response = {}
    response["status"] = status
    response["mensagem"] = mensage
    response["pessoas"] = quatPeople
    response["faces"] = quatFaces
    response["probabilidadeArma"] = probilidGun
    response["probabilidadeNaoSerArma"] = noProbilidGun
    return (response)
