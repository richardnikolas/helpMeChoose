# Help Me Choose! 🎥

Com a ajuda to <b>Google Gemini</b>, a ideia desse projeto é ajudar você a escolher qual o próximo filme que você irá assistir! </br>
Procure algo sobre sua atriz favorita ou algo mais genérico, como por exemplo: </br>

> "Quais foram os últimos filmes da Anne Hathaway?" </br>
> "Me indique bons filmes de ação"

O **Gemini** irá buscar por diversas informações relacionadas aos filmes e, com a ajuda do [The Movie DB (TMDB)](https://www.themoviedb.org/), conseguimos ver até o poster dos filmes! 

![example](https://github.com/richardnikolas/helpMeChoose/assets/20261986/a1b9919a-c1c1-4477-ad4e-ebcbd7aee9e8)

> [!IMPORTANT]
> Esse projeto é focado em **filmes**. Com qualquer outro tipo de mídia os resultados não serão como esperado.

---

## Instalação / Getting Started

Esse projeto consiste em duas partes: **backend** (_Python_) e **frontend** (_Svelte_). Então você precisa clonar o projeto localmente se quiser usá-lo de fato.

Você precisará ter instalado previamente em seu computador:
- Python
- Npm
- Node


### • Backend / server side

Após clonar o projeto, via command line acesse a pasta `backend` e rode o seguinte comando para instalar todas as dependências:

```
py -m pip install -r requirements.txt
```

Após tudo instalado corretamente, rode o comando:

```
python helpMeChoose.py
```

Pronto, o servidor já deve estar funcionando corretamente. 

### • Frontend / client side

Em outra aba ou janela do seu command line, acesse a pasta `frontend` e rode:

```
npm install
```

Depois de tudo instalado, rode: 

```
npm run dev
```

E pronto, você deve ver uma mensagem de sucesso e tá tudo pronto pra testar agora!

### • Testando

Agora basta acessar `http://localhost:3000/` para usar e escolher o próximo filme da sua lista 😎

> [!NOTE]
> No terminal pode ser que esteja escrita localhost:5000, mas o projeto estará rodando mesmo no `http://localhost:3000/`
