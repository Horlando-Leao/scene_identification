# DETECÇÃO DE CENAS POTENCIALMENTE PERIGOSAS
## Esse repositório é um refatoramente que tem origem de outro repositório remoto meu: https://github.com/Horlando-Leao/dangerousSceneIdentification

### Descrição:
O repositório é uma api, que recebe apenas uma url de imagem, e retorna se aquela imagem apresenta perigo

### o que essa api faz:
Analisa em uma imagem a quantidade de faces humanas e também corpos e além disso a quantidade de armas.

### Tecnologias
- Python
  - Libs
    - OpenCV
    - Pandas
    - Pillow
    - Requests
  - Framework
    - Flask
  - Deploy
    - Heroku

### o que pretendo:
Disponibilizar para a comunidade api muito simples, no qual um usuário poderá usar em seu sistema de segurança local

### Como usar:


Teste se o servidor está funcionando com a url abaixo, deverá aparacer a Mensagem "Page Index":
https://secview.herokuapp.com/

---------------------------
Passa no URL da requisição do tipo GET um parâmetro.
exemplo https://secview.herokuapp.com/detectsall/{seu parametro}

O parâmetro deve ser uma URL de uma imagem em um servidor acessível, caso contrário receberá está mensagem do servidor:

```JSON
{
  "data": {
    "number_faces": "",
    "number_guns": "",
    "number_people": ""
  },
  "mensagem": "o parametro (url) é obrigatório",
  "status": 400,
  "url": ""
}
```

---------------------------
Este parâmetro do tipo URL deve trocar todas as / (barras invetidas) por ||
Exemplo: de https://images.uol/pessoa_andando.jpeg para https:||||images.uol||pessoa_andando.jpeg 

Exemplos de requisições para testar agora:

https://secview.herokuapp.com/detectsall/https:||||s.france24.com||media||display||3fe8f454-88c3-11eb-ad87-005056a98db9||w:1280||p:16x9||000_DV915340.webp

https://secview.herokuapp.com/detectsall/https:||||media.gazetadopovo.com.br||2010||11||38fb3a8e0d31e8a4b9f98dcc38508a47-gpMedium.jpg

https://secview.herokuapp.com/detectsall/https:||||ep00.epimg.net||brasil||imagenes||2014||03||30||album||1396205399_006677_1396205894_album_normal.jpg

Estou tendo um pouco de problema com precisão.











