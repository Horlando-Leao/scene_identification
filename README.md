# DETECÇÃO DE CENAS POTENCIALMENTE PERIGOSAS
## Esse repositório é um refatoramente que tem origem em outro repositório remoto

### Descrição:
O repositório é uma api, que recebe apenas uma url de imagem, e retorna se aquela imagem apresenta perigo

### o que essa api faz:
Avalia se a pessoa está encapuzado, quantidade de pessoas e se possui armas na imagem

### Blz, mas o que está rodando?:
Muitas libs, as principais são openCV e Keras.

### o que pretendo:
Disponibilizar para a comunidade api muito simples, aonde um usuário poderá usar em seu sistema de segurança local

### blz, mas como usar:
#### 0: chame a url (http://servidor.inexistente.ainda/)
#### 1: escolha um link url de imagem e troque as barras "/" por "||" (use algum replace)
####    1.1: antes = "http://fotos.google/minha-imagem.jpg"
####    1.2 depois = "http:||||fotos.google||minha-imagem.jpg"
#### 2: passe o link já modificado como parâmetro após a última barra da url

### Ficaria algo assim:
url = "http://servidor.inexistente.ainda/http:||||fotos.google||minha-imagem.jpg"