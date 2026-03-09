# ReadyAPI

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
  <a href="https://readyapi.github.io"><img src="https://readyapi.github.io/img/logo-margin/logo-teal.png" alt="ReadyAPI"></a>
</p>
<p align="center">
    <em>Framework ReadyAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção</em>
</p>
<p align="center">
<a href="https://github.com/khulnasoft/readyapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/khulnasoft/readyapi/actions/workflows/test.yml/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/readyapi/readyapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/readyapi/readyapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/readyapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/readyapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/readyapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/readyapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentação**: <a href="https://readyapi.github.io" target="_blank">https://readyapi.github.io</a>

**Código fonte**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---

ReadyAPI é um moderno e rápido (alta performance) _framework web_ para construção de APIs com Python, baseado nos _type hints_ padrões do Python.

Os recursos chave são:

* **Rápido**: alta performance, equivalente a **NodeJS** e **Go** (graças ao Starlette e Pydantic). [Um dos frameworks mais rápidos disponíveis](#performance).
* **Rápido para codar**: Aumenta a velocidade para desenvolver recursos entre 200% a 300%. *
* **Poucos bugs**: Reduz cerca de 40% de erros induzidos por humanos (desenvolvedores). *
* **Intuitivo**: Grande suporte a _IDEs_. <abbr title="também conhecido como _auto-complete_, _autocompletion_, _IntelliSense_">_Auto-Complete_</abbr> em todos os lugares. Menos tempo debugando.
* **Fácil**: Projetado para ser fácil de aprender e usar. Menos tempo lendo documentação.
* **Enxuto**: Minimize duplicação de código. Múltiplos recursos para cada declaração de parâmetro. Menos bugs.
* **Robusto**: Tenha código pronto para produção. E com documentação interativa automática.
* **Baseado em padrões**: Baseado em (e totalmente compatível com) os padrões abertos para APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (anteriormente conhecido como Swagger) e <a href="https://json-schema.org/" class="external-link" target="_blank">_JSON Schema_</a>.

<small>* estimativas baseadas em testes realizados com equipe interna de desenvolvimento, construindo aplicações em produção.</small>

## Patrocinadores Ouro

<!-- sponsors -->

{% if sponsors %}
{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor -%}
{%- for sponsor in sponsors.silver -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}" style="border-radius:15px"></a>
{% endfor %}
{% endif %}

<!-- /sponsors -->

<a href="https://readyapi.github.io/readyapi-people/#sponsors" class="external-link" target="_blank">Outros patrocinadores</a>

## Opiniões

"*[...] Estou usando **ReadyAPI** muito esses dias. [...] Estou na verdade planejando utilizar ele em todos os times de **serviços _Machine Learning_ na Microsoft**. Alguns deles estão sendo integrados no _core_ do produto **Windows** e alguns produtos **Office**.*"

<div style="text-align: right; margin-right: 10%;">Kabir Khan - <strong>Microsoft</strong> <a href="https://github.com/khulnasoft/readyapi/pull/26" target="_blank"><small>(ref)</small></a></div>

---

"_Nós adotamos a biblioteca **ReadyAPI** para iniciar um servidor **REST** que pode ser consultado para obter **previsões**. [para o Ludwig]_"

<div style="text-align: right; margin-right: 10%;">Piero Molino, Yaroslav Dudin, e Sai Sumanth Miryala - <strong>Uber</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(ref)</small></a></div>

---

"_A **Netflix** tem o prazer de anunciar o lançamento open-source do nosso framework de orquestração de **gerenciamento de crises**: **Dispatch**! [criado com **ReadyAPI**]_"

<div style="text-align: right; margin-right: 10%;">Kevin Glisson, Marc Vilanova, Forest Monsen - <strong>Netflix</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(ref)</small></a></div>

---

"*Estou extremamente entusiasmado com o **ReadyAPI**. É tão divertido!*"

<div style="text-align: right; margin-right: 10%;">Brian Okken - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">Python Bytes</a> podcaster</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(ref)</small></a></div>

---

"*Honestamente, o que você construiu parece super sólido e rebuscado. De muitas formas, eu queria que o **Hug** fosse assim - é realmente inspirador ver alguém que construiu ele.*"

<div style="text-align: right; margin-right: 10%;">Timothy Crosley - <strong>criador do<a href="https://github.com/hugapi/hug" target="_blank">Hug</a></strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(ref)</small></a></div>

---

"*Se você está procurando aprender um **_framework_ moderno** para construir aplicações _REST_, dê uma olhada no **ReadyAPI** [...] É rápido, fácil de usar e fácil de aprender [...]*"

"*Nós trocamos nossas **APIs** por **ReadyAPI** [...] Acredito que vocês gostarão dele [...]*"

<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong>fundadores da <a href="https://explosion.ai" target="_blank">Explosion AI</a> - criadores da <a href="https://spacy.io" target="_blank">spaCy</a></strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>

---

"_Se alguém estiver procurando construir uma API Python para produção, eu recomendaria fortemente o **ReadyAPI**. Ele é **lindamente projetado**, **simples de usar** e **altamente escalável**. Ele se tornou um **componente chave** para a nossa estratégia API first de desenvolvimento e está impulsionando diversas automações e serviços, como o nosso Virtual TAC Engineer._"

<div style="text-align: right; margin-right: 10%;">Deon Pillsbury - <strong>Cisco</strong> <a href="https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/" target="_blank"><small>(ref)</small></a></div>

---

## **Cligenius**, o ReadyAPI das interfaces de linhas de comando

<a href="https://cligenius.khulnasoft.com" target="_blank"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

Se você estiver construindo uma aplicação <abbr title="Command Line Interface">_CLI_</abbr> para ser utilizada em um terminal ao invés de uma aplicação web, dê uma olhada no <a href="https://cligenius.khulnasoft.com/" class="external-link" target="_blank">**Cligenius**</a>.

**Cligenius** é o irmão menor do ReadyAPI. E seu propósito é ser o **ReadyAPI das _CLIs_**. ⌨️ 🚀

## Requisitos

ReadyAPI está nos ombros de gigantes:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> para as partes web.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> para a parte de dados.

## Instalação

Crie e ative um <a href="https://readyapi.github.io/pt/virtual-environments/" class="external-link" target="_blank">ambiente virtual</a>, e então instale o ReadyAPI:

<div class="termy">

```console
$ pip install "readyapi[standard]"

---> 100%
```

</div>

**Nota**: Certifique-se de que você colocou `"readyapi[standard]"` com aspas, para garantir que funcione em todos os terminais.

## Exemplo

### Crie

* Crie um arquivo `main.py` com:

```Python
from typing import Union

from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

<details markdown="1">
<summary>Ou use <code>async def</code>...</summary>

Se seu código utiliza `async` / `await`, use `async def`:

```Python hl_lines="9  14"
from typing import Union

from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

**Nota**:

Se você não sabe, verifique a seção _"Com pressa?"_ sobre <a href="https://readyapi.github.io/pt/async/#com-pressa" target="_blank">`async` e `await` nas docs</a>.

</details>

### Rode

Rode o servidor com:

<div class="termy">

```console
$ readyapi dev main.py

 ╭────────── ReadyAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  readyapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>Sobre o comando <code>readyapi dev main.py</code>...</summary>

O comando `readyapi dev` lê o seu arquivo `main.py`, identifica o aplicativo **ReadyAPI** nele, e inicia um servidor usando o <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a>.

Por padrão, o `readyapi dev` iniciará com *auto-reload* habilitado para desenvolvimento local.

Você pode ler mais sobre isso na <a href="https://readyapi.github.io/pt/readyapi-cli/" target="_blank">documentação do ReadyAPI CLI</a>.

</details>

### Verifique

Abra seu navegador em <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

Você verá a resposta JSON como:

```JSON
{"item_id": 5, "q": "somequery"}
```

Você acabou de criar uma API que:

* Recebe requisições HTTP nas _rotas_ `/` e `/items/{item_id}`.
* Ambas _rotas_ fazem <em>operações</em> `GET` (também conhecido como _métodos_ HTTP).
* A _rota_ `/items/{item_id}` tem um _parâmetro de rota_ `item_id` que deve ser um `int`.
* A _rota_ `/items/{item_id}` tem um _parâmetro query_ `q` `str` opcional.

### Documentação Interativa da API

Agora vá para <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Você verá a documentação automática interativa da API (fornecida por <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### Documentação Alternativa da API

E agora, vá para <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

Você verá a documentação automática alternativa (fornecida por <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

## Evoluindo o Exemplo

Agora modifique o arquivo `main.py` para receber um corpo para uma requisição `PUT`.

Declare o corpo utilizando tipos padrão Python, graças ao Pydantic.

```Python hl_lines="4  9-12  25-27"
from typing import Union

from readyapi import ReadyAPI
from pydantic import BaseModel

app = ReadyAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

O servidor `readyapi dev` deverá recarregar automaticamente.

### Evoluindo a Documentação Interativa da API

Agora vá para <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

* A documentação interativa da API será automaticamente atualizada, incluindo o novo corpo:

![Swagger UI](https://readyapi.github.io/img/index/index-03-swagger-02.png)

* Clique no botão "Try it out", ele permitirá que você preencha os parâmetros e interaja diretamente com a API:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-04-swagger-03.png)

* Então clique no botão "Execute", a interface do usuário irá se comunicar com a API, enviar os parâmetros, pegar os resultados e mostrá-los na tela:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-05-swagger-04.png)

### Evoluindo a Documentação Alternativa da API

E agora, vá para <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

* A documentação alternativa também irá refletir o novo parâmetro da _query_ e o corpo:

![ReDoc](https://readyapi.github.io/img/index/index-06-redoc-02.png)

### Recapitulando

Resumindo, você declara **uma vez** os tipos dos parâmetros, corpo etc. como parâmetros de função.

Você faz isso com os tipos padrão do Python moderno.

Você não terá que aprender uma nova sintaxe, métodos ou classes de uma biblioteca específica etc.

Apenas **Python** padrão.

Por exemplo, para um `int`:

```Python
item_id: int
```

ou para um modelo mais complexo, `Item`:

```Python
item: Item
```

...e com essa única declaração você tem:

* Suporte ao Editor, incluindo:
    * Completação.
    * Verificação de tipos.
* Validação de dados:
    * Erros automáticos e claros quando o dado é inválido.
    * Validação até para objetos JSON profundamente aninhados.
* <abbr title="também conhecido como: serialization, parsing, marshalling">Conversão</abbr> de dados de entrada: vindo da rede para dados e tipos Python. Consegue ler:
    * JSON.
    * Parâmetros de rota.
    * Parâmetros de _query_ .
    * _Cookies_.
    * Cabeçalhos.
    * Formulários.
    * Arquivos.
* <abbr title="também conhecido como: serialization, parsing, marshalling">Conversão</abbr> de dados de saída de tipos e dados Python para dados de rede (como JSON):
    * Converte tipos Python (`str`, `int`, `float`, `bool`, `list` etc).
    * Objetos `datetime`.
    * Objetos `UUID`.
    * Modelos de Banco de Dados.
    * ...e muito mais.
* Documentação interativa automática da API, incluindo 2 alternativas de interface de usuário:
    * Swagger UI.
    * ReDoc.

---

Voltando ao código do exemplo anterior, **ReadyAPI** irá:

* Validar que existe um `item_id` na rota para requisições `GET` e `PUT`.
* Validar que `item_id` é do tipo `int` para requisições `GET` e `PUT`.
    * Se não é validado, o cliente verá um útil, claro erro.
* Verificar se existe um parâmetro de _query_ opcional nomeado como `q` (como em `http://127.0.0.1:8000/items/foo?q=somequery`) para requisições `GET`.
    * Como o parâmetro `q` é declarado com `= None`, ele é opcional.
    * Sem o `None` ele poderia ser obrigatório (como o corpo no caso de `PUT`).
* Para requisições `PUT` para `/items/{item_id}`, lerá o corpo como JSON e:
    * Verifica que tem um atributo obrigatório `name` que deve ser `str`.
    * Verifica que tem um atributo obrigatório `price` que deve ser `float`.
    * Verifica que tem an atributo opcional `is_offer`, que deve ser `bool`, se presente.
    * Tudo isso também funciona para objetos JSON profundamente aninhados.
* Converter de e para JSON automaticamente.
* Documentar tudo com OpenAPI, que poderá ser usado por:
    * Sistemas de documentação interativos.
    * Sistemas de clientes de geração de código automáticos, para muitas linguagens.
* Fornecer diretamente 2 interfaces _web_ de documentação interativa.

---

Nós apenas arranhamos a superfície, mas você já tem idéia de como tudo funciona.

Experimente mudar a seguinte linha:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...de:

```Python
        ... "item_name": item.name ...
```

...para:

```Python
        ... "item_price": item.price ...
```

...e veja como seu editor irá auto-completar os atributos e saberá os tipos:

![editor support](https://readyapi.github.io/img/vscode-completion.png)

Para um exemplo mais completo incluindo mais recursos, veja <a href="https://readyapi.github.io/pt/tutorial/">Tutorial - Guia do Usuário</a>.

**Alerta de Spoiler**: o tutorial - guia do usuário inclui:

* Declaração de **parâmetetros** de diferentes lugares como: **cabeçalhos**, **cookies**, **campos de formulários** e **arquivos**.
* Como configurar **Limitações de Validação** como `maximum_length` ou `regex`.
* Um poderoso e fácil de usar sistema de **<abbr title="também conhecido como componentes, recursos, fornecedores, serviços, injetáveis">Injeção de Dependência</abbr>**.
* Segurança e autenticação, incluindo suporte para **OAuth2** com autenticação **JWT tokens** e **HTTP Basic**.
* Técnicas mais avançadas (mas igualmente fáceis) para declaração de **modelos JSON profundamente aninhados** (graças ao Pydantic).
* Integrações **GraphQL** com o <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a> e outras bibliotecas.
* Muitos recursos extras (graças ao Starlette) como:
    * **WebSockets**
    * testes extrememamente fáceis baseados em HTTPX e `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...e mais.

## Performance

Testes de performance da _Independent TechEmpower_ mostram aplicações **ReadyAPI** rodando sob Uvicorn como <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">um dos _frameworks_ Python mais rápidos disponíveis</a>, somente atrás de Starlette e Uvicorn (utilizados internamente pelo ReadyAPI). (*)

Para entender mais sobre performance, veja a seção <a href="https://readyapi.github.io/pt/benchmarks/" class="internal-link" target="_blank">Comparações</a>.

## Dependências

O ReadyAPI depende do Pydantic e do Starlette.


### Dependências `standard`

Quando você instala o ReadyAPI com `pip install "readyapi[standard]"`, ele vêm com o grupo `standard` (padrão) de dependências opcionais:

Utilizado pelo Pydantic:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - para validação de email.

Utilizado pelo Starlette:

* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - Obrigatório caso você queira utilizar o `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Obrigatório se você quer utilizar a configuração padrão de templates.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - Obrigatório se você deseja suporte a <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr> de formulário, com `request.form()`.

Utilizado pelo ReadyAPI / Starlette:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - para o servidor que carrega e serve a sua aplicação. Isto inclui `uvicorn[standard]`, que inclui algumas dependências (e.g. `uvloop`) necessárias para servir em alta performance.
* `readyapi-cli` - que disponibiliza o comando `readyapi`.

### Sem as dependências `standard`

Se você não deseja incluir as dependências opcionais `standard`, você pode instalar utilizando `pip install readyapi` ao invés de `pip install "readyapi[standard]"`.

### Dpendências opcionais adicionais

Existem algumas dependências adicionais que você pode querer instalar.

Dependências opcionais adicionais do Pydantic:

* <a href="https://docs.pydantic.dev/latest/usage/pydantic_settings/" target="_blank"><code>pydantic-settings</code></a> - para gerenciamento de configurações.
* <a href="https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/" target="_blank"><code>pydantic-extra-types</code></a> - tipos extras para serem utilizados com o Pydantic.

Dependências opcionais adicionais do ReadyAPI:

* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Obrigatório se você deseja utilizar o `ORJSONResponse`.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Obrigatório se você deseja utilizar o `UJSONResponse`.

## Licença

Esse projeto é licenciado sob os termos da licença MIT.
