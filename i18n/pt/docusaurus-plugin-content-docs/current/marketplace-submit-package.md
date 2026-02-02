# Publicar pacotes na Marketplace da ITsMagic (GitHub)

Este guia explica, passo a passo, como publicar seu pacote na Marketplace da ITsMagic. A marketplace fica hospedada no GitHub, entao voce vai enviar um Pull Request (PR) com as informacoes do seu pacote.

Repositorio:
```
https://github.com/ITsMagic-Software/Packages-Manifest
```

## Visao geral (o que voce vai fazer)

1. Criar um repositorio publico no GitHub com o conteudo do pacote.
2. Adicionar o pacote no `database.json` do repositorio da Marketplace.
3. Enviar as imagens (thumbnail + imagens) na pasta correta.
4. Abrir um Pull Request com as mudancas.

## Passo 1: Crie um repositorio publico para o seu pacote

Seus arquivos precisam estar em um repositorio publico no GitHub (na sua conta).

- Crie um novo repositorio publico no GitHub.
- Envie os arquivos do pacote (cenas, scripts, assets, etc.).
- Copie o URL do repositorio. Voce vai usar em `repositoryURL`.

## Passo 2: Faca um fork do repositorio da Marketplace

1. Abra o repositorio da Marketplace:
```
https://github.com/ITsMagic-Software/Packages-Manifest
```
2. Clique em **Fork** para criar uma copia na sua conta.
3. Abra o seu fork e clone para o seu computador.

## Passo 3: Adicione o pacote no database.json

Abra o `database.json` e adicione uma entrada nova com esta estrutura:

```json
{
  "id": "6cb01fa1-a3dc-4cf8-a7c6-e115a36d8806",
  "userName": "ITsMagic",
  "titleB64": "Q2F2ZSBjaHVyY2ggKEhJR0ggR1JBUEhJQ1Mp",
  "descriptionB64": "VW5kZXJncm91bmQgY2h1cmNoIHByb2plY3Qgd2l0aCBhbWF6aW5nIGdyYXBoY2lzLg==",
  "tags": "graphics,afpp",
  "version": 1,
  "repositoryURL": "https://github.com/ITsMagic-Software/Package-CaveChurch",
  "isTemplate": false,
  "mediaFolder": "itsmagic/cavechurch",
  "thumbnail": "thumb.jpg",
  "images": [
    "img1.jpg",
    "img2.jpg",
    "img3.jpg",
    "img4.jpg"
  ]
}
```

### Explicacao dos campos (simples)

- `id`: Um ID unico para o pacote (use um UUID).
- `userName`: Seu nome de usuario no GitHub.
- `titleB64`: O titulo do pacote em Base64.
- `descriptionB64`: A descricao do pacote em Base64.
- `tags`: Tags separadas por virgula, para ajudar na busca.
- `version`: Comece com `1` e aumente quando atualizar.
- `repositoryURL`: O repositorio publico com os arquivos do pacote.
- `isTemplate`: `true` se for template, senao `false`.
- `mediaFolder`: A pasta onde as imagens vao ficar (veja o proximo passo).
- `thumbnail`: A imagem principal do pacote.
- `images`: Imagens extras (screenshots) do pacote.

### Como criar Base64 para titulo/descricao

Voce pode usar qualquer conversor de Base64. Exemplo:

- Titulo: `Cave church (HIGH GRAPHICS)`
- Descricao: `Underground church project with amazing graphics.`

Depois converta cada texto para Base64 e coloque em `titleB64` e `descriptionB64`.

## Passo 4: Adicione as imagens na pasta media

**Requisitos das imagens**
- Tamanho maximo: 1 MB por imagem
- Formatos aceitos: JPG ou PNG
- Maximo: 8 imagens por produto

Dentro do repositorio da Marketplace existe a pasta `media`. Crie o caminho:

```
media/seuusuario/seupacote/
```

Exemplo:

```
media/itsmagic/cavechurch/
```

Coloque a imagem `thumbnail` e todas as `images` dentro desta pasta.

## Passo 5: Abra um Pull Request

1. Commit as mudancas (database.json + arquivos de media).
2. Envie (push) para o seu fork.
3. Abra um Pull Request para:
   - Base repository: `ITsMagic-Software/Packages-Manifest`
   - Compare repository: seu fork
4. Descreva o pacote e envie.

Depois da revisao, o pacote sera publicado na Marketplace.

## Moderacao e aprovacao

O seu Pull Request pode ser aprovado ou recusado pelos moderadores da Marketplace. Se for recusado, os moderadores vao deixar informacoes sobre o que voce precisa alterar para conseguir aprovacao.
