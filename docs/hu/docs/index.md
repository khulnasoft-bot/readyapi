<p align="center">
  <a href="https://readyapi.github.io"><img src="https://readyapi.github.io/img/logo-margin/logo-teal.png" alt="ReadyAPI"></a>
</p>
<p align="center">
    <em>ReadyAPI keretrendszer, nagy teljesítmény, könnyen tanulható, gyorsan kódolható, productionre kész</em>
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

**Dokumentáció**: <a href="https://readyapi.github.io" target="_blank">https://readyapi.github.io</a>

**Forrás kód**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---
A ReadyAPI egy modern, gyors (nagy teljesítményű), webes keretrendszer API-ok építéséhez Python -al, a Python szabványos típusjelöléseire építve.


Kulcs funkciók:

* **Gyors**: Nagyon nagy teljesítmény, a **NodeJS**-el és a **Go**-val egyenrangú (a Starlettenek és a Pydantic-nek köszönhetően). [Az egyik leggyorsabb Python keretrendszer](#performance).
* **Gyorsan kódolható**: A funkciók fejlesztési sebességét 200-300 százalékkal megnöveli. *
* **Kevesebb hiba**: Körülbelül 40%-al csökkenti az emberi (fejlesztői) hibák számát. *
* **Intuitív**: Kiváló szerkesztő támogatás. <abbr title="más néven auto-complete, autocompletion, IntelliSense">Kiegészítés</abbr> mindenhol. Kevesebb hibakereséssel töltött idő.
* **Egyszerű**: Egyszerű tanulásra és használatra tervezve. Kevesebb dokumentáció olvasással töltött idő.
* **Rövid**: Kód duplikáció minimalizálása. Több funkció minden paraméter deklarálásával. Kevesebb hiba.
* **Robosztus**: Production ready kód. Automatikus interaktív dokumentáció val.
* **Szabvány alapú**: Az API-ok nyílt szabványaira alapuló (és azokkal teljesen kompatibilis): <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (korábban Swagger néven ismert) és a <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* Egy production alkalmazásokat építő belső fejlesztői csapat tesztjein alapuló becslés. </small>

## Szponzorok

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

<a href="https://readyapi.github.io/readyapi-people/#sponsors" class="external-link" target="_blank">További szponzorok</a>

## Vélemények

"_[...] I'm using **ReadyAPI** a ton these days. [...] I'm actually planning to use it for all of my team's **ML services at Microsoft**. Some of them are getting integrated into the core **Windows** product and some **Office** products._"

<div style="text-align: right; margin-right: 10%;">Kabir Khan - <strong>Microsoft</strong> <a href="https://github.com/khulnasoft/readyapi/pull/26" target="_blank"><small>(ref)</small></a></div>

---

"_We adopted the **ReadyAPI** library to spawn a **REST** server that can be queried to obtain **predictions**. [for Ludwig]_"

<div style="text-align: right; margin-right: 10%;">Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - <strong>Uber</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(ref)</small></a></div>

---

"_**Netflix** is pleased to announce the open-source release of our **crisis management** orchestration framework: **Dispatch**! [built with **ReadyAPI**]_"

<div style="text-align: right; margin-right: 10%;">Kevin Glisson, Marc Vilanova, Forest Monsen - <strong>Netflix</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(ref)</small></a></div>

---

"_I’m over the moon excited about **ReadyAPI**. It’s so fun!_"

<div style="text-align: right; margin-right: 10%;">Brian Okken - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">Python Bytes</a> podcast host</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(ref)</small></a></div>

---

"_Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted **Hug** to be - it's really inspiring to see someone build that._"

<div style="text-align: right; margin-right: 10%;">Timothy Crosley - <strong><a href="https://github.com/hugapi/hug" target="_blank">Hug</a> creator</strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(ref)</small></a></div>

---

"_If you're looking to learn one **modern framework** for building REST APIs, check out **ReadyAPI** [...] It's fast, easy to use and easy to learn [...]_"

"_We've switched over to **ReadyAPI** for our **APIs** [...] I think you'll like it [...]_"

<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong><a href="https://explosion.ai" target="_blank">Explosion AI</a> founders - <a href="https://spacy.io" target="_blank">spaCy</a> creators</strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>

---

"_If anyone is looking to build a production Python API, I would highly recommend **ReadyAPI**. It is **beautifully designed**, **simple to use** and **highly scalable**, it has become a **key component** in our API first development strategy and is driving many automations and services such as our Virtual TAC Engineer._"

<div style="text-align: right; margin-right: 10%;">Deon Pillsbury - <strong>Cisco</strong> <a href="https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/" target="_blank"><small>(ref)</small></a></div>

---

## **Cligenius**, a CLI-ok ReadyAPI-ja

<a href="https://cligenius.khulnasoft.com" target="_blank"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

Ha egy olyan CLI alkalmazást fejlesztesz amit a parancssorban kell használni webes API helyett, tekintsd meg: <a href="https://cligenius.khulnasoft.com/" class="external-link" target="_blank">**Cligenius**</a>.

**Cligenius** a ReadyAPI kistestvére. A **CLI-k ReadyAPI-ja**. ⌨️ 🚀

## Követelmények

A ReadyAPI óriások vállán áll:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> a webes részekhez.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> az adat részekhez.

## Telepítés

<div class="termy">

```console
$ pip install readyapi

---> 100%
```

</div>

A production-höz egy ASGI szerverre is szükség lesz, mint például az <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> vagy a <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

## Példa

### Hozd létre

* Hozz létre a `main.py` fájlt a következő tartalommal:

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
<summary>Vagy használd az <code>async def</code>-et...</summary>

Ha a kódod `async` / `await`-et, használ `async def`:

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

**Megjegyzés**:

Ha nem tudod, tekintsd meg a _"Sietsz?"_ szekciót <a href="https://readyapi.github.io/async/#in-a-hurry" target="_blank">`async` és `await`-ről dokumentációba</a>.

</details>

### Futtasd le

Indítsd el a szervert a következő paranccsal:

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>A parancsról <code>uvicorn main:app --reload</code>...</summary>

A `uvicorn main:app` parancs a következőre utal:

* `main`: fájl `main.py` (a Python "modul").
* `app`: a `main.py`-ban a `app = ReadyAPI()` sorral létrehozott objektum.
* `--reload`: kód változtatás esetén újra indítja a szervert. Csak fejlesztés közben használandó.

</details>

### Ellenőrizd

Nyisd meg a böngésződ a következő címen: <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

A következő JSON választ fogod látni:

```JSON
{"item_id": 5, "q": "somequery"}
```

Máris létrehoztál egy API-t ami:

* HTTP kéréseket fogad a  `/` és `/items/{item_id}` _útvonalakon_.
* Mindkét _útvonal_ a `GET` <em>műveletet</em> használja (másik elnevezés: HTTP _metódus_).
* A `/items/{item_id}` _útvonalnak_ van egy _path paramétere_, az `item_id`, aminek `int` típusúnak kell lennie.
* A `/items/{item_id}` _útvonalnak_ még van egy opcionális, `str` típusú _query paramétere_ is, a `q`.

### Interaktív API dokumentáció

Most nyisd meg a <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> címet.

Az automatikus interaktív API dokumentációt fogod látni (amit a <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>-al hozunk létre):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### Alternatív API dokumentáció

És most menj el a <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> címre.

Az alternatív automatikus dokumentációt fogod látni. (lásd <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

## Példa frissítése

Módosítsuk a `main.py` fájlt, hogy `PUT` kérések esetén tudjon body-t fogadni.

Deklaráld a body-t standard Python típusokkal, a Pydantic-nak köszönhetően.

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

A szerver automatikusan újraindul (mert hozzáadtuk a --reload paramétert a fenti `uvicorn` parancshoz).

### Interaktív API dokumentáció frissítése

Most menj el a <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> címre.

* Az interaktív API dokumentáció automatikusan frissült így már benne van az új body.

![Swagger UI](https://readyapi.github.io/img/index/index-03-swagger-02.png)

* Kattints rá a "Try it out" gombra, ennek segítségével kitöltheted a paramétereket és közvetlen használhatod az API-t:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-04-swagger-03.png)

* Ezután kattints az "Execute" gompra, a felhasználói felület kommunikálni fog az API-oddal. Elküldi a paramétereket és a visszakapott választ megmutatja a képernyődön.

![Swagger UI interaction](https://readyapi.github.io/img/index/index-05-swagger-04.png)

### Alternatív API dokumentáció frissítés

Most menj el a <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> címre.

* Az alternatív dokumentáció szintúgy tükrözni fogja az új kérési paraméter és body-t.

![ReDoc](https://readyapi.github.io/img/index/index-06-redoc-02.png)

### Összefoglalás

Összegzésül, deklarálod **egyszer** a paraméterek, body, stb típusát funkciós paraméterekként.

Ezt standard modern Python típusokkal csinálod.

Nem kell új szintaxist, vagy specifikus könyvtár mert metódósait, stb. megtanulnod.

Csak standard **Python**.

Például egy `int`-nek:

```Python
item_id: int
```

Egy komplexebb `Item` modellnek:

```Python
item: Item
```

... És csupán egy deklarációval megkapod a:

* Szerkesztő támogatást, beleértve:
    * Szövegkiegészítés.
    * Típus ellenőrzés.
* Adatok validációja:
    * Automatikus és érthető hibák amikor az adatok hibásak.
    * Validáció mélyen ágyazott objektumok esetén is.
* Bemeneti adatok<abbr title="also known as: serialization, parsing, marshalling"> átváltása</abbr> : a hálózatról érkező Python adatokká és típusokká. Adatok olvasása következő forrásokból:
    * JSON.
    * Cím paraméterek.
    * Query paraméterek.
    * Cookie-k.
    * Header-ök.
    * Formok.
    * Fájlok.
* Kimeneti adatok <abbr title=" más néven: serialization, parsing, marshalling">átváltása</abbr>: Python adatok is típusokról hálózati adatokká:
    * válts át Python típusokat (`str`, `int`, `float`, `bool`, `list`, etc).
    * `datetime` csak objektumokat.
    * `UUID` objektumokat.
    * Adatbázis modelleket.
    * ...És sok mást.
* Automatikus interaktív dokumentáció, beleértve két alternatív dokumentációt is:
    * Swagger UI.
    * ReDoc.

---

Visszatérve az előző kód példához. A **ReadyAPI**:

* Validálja hogy van egy `item_id` mező a `GET` és `PUT` kérésekben.
* Validálja hogy az `item_id` `int` típusú a `GET` és `PUT` kérésekben.
    * Ha nem akkor látni fogunk egy tiszta hibát ezzel kapcsolatban.
* ellenőrzi hogyha van egy opcionális query paraméter `q` névvel (azaz `http://127.0.0.1:8000/items/foo?q=somequery`) `GET` kérések esetén.
    * Mivel a `q` paraméter `= None`-al van deklarálva, ezért opcionális.
    * `None` nélkül ez a mező kötelező lenne (mint például a body `PUT` kérések esetén).
* a `/items/{item_id}` címre érkező `PUT` kérések esetén, a JSON-t a következőképpen olvassa be:
    * Ellenőrzi hogy létezik a kötelező `name` nevű attribútum és `string`.
    * Ellenőrzi hogy létezik a kötelező `price` nevű attribútum és `float`.
    * Ellenőrzi hogy létezik a `is_offer` nevű opcionális paraméter, ami ha létezik akkor `bool`
    * Ez ágyazott JSON objektumokkal is működik
* JSONről való automatikus konvertálás.
* dokumentáljuk mindent OpenAPI-al amit használható:
    * Interaktív dokumentációs rendszerekkel.
    * Automatikus kliens kód generáló a rendszerekkel, több nyelven.
* Hozzá tartozik kettő interaktív dokumentációs web felület.

---

Eddig csak a felszínt kapargattuk, de a lényeg hogy most már könnyebben érthető hogyan működik.

Próbáld kicserélni a következő sorban:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...ezt:

```Python
        ... "item_name": item.name ...
```

...erre:

```Python
        ... "item_price": item.price ...
```

... És figyeld meg hogy a szerkesztő automatikusan tudni fogja a típusokat és kiegészíti azokat:

![editor support](https://readyapi.github.io/img/vscode-completion.png)

Teljesebb példákért és funkciókért tekintsd meg a <a href="https://readyapi.github.io/tutorial/">Tutorial - User Guide</a> -t.

**Spoiler veszély**: a Tutorial - User Guidehoz tartozik:

* **Paraméterek** deklarációja különböző helyekről: **header-ök**, **cookie-k**, **form mezők** és **fájlok**.
* Hogyan állíts be **validációs feltételeket** mint a `maximum_length` vagy a `regex`.
* Nagyon hatékony és erős **<abbr title="also known as components, resources, providers, services, injectables">Függőség Injekció</abbr>** rendszerek.
* Biztonság és autentikáció beleértve, **OAuth2**, **JWT tokens** és **HTTP Basic** támogatást.
* Több haladó (de ugyanannyira könnyű) technika **mélyen ágyazott JSON modellek deklarációjára** (Pydantic-nek köszönhetően).
* **GraphQL** integráció <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a>-vel és más könyvtárakkal.
* több extra funkció (Starlette-nek köszönhetően) pl.:
    * **WebSockets**
    * rendkívül könnyű tesztek HTTPX és `pytest` alapokra építve
    * **CORS**
    * **Cookie Sessions**
    * ...és több.

## Teljesítmény

A független TechEmpower benchmarkok szerint az Uvicorn alatt futó **ReadyAPI** alkalmazások az <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">egyik leggyorsabb Python keretrendszerek közé tartoznak</a>, éppen lemaradva a Starlette és az Uvicorn (melyeket a ReadyAPI belsőleg használ) mögött.(*)

Ezeknek a további megértéséhez: <a href="https://readyapi.github.io/benchmarks/" class="internal-link" target="_blank">Benchmarks</a>.

## Opcionális követelmények

Pydantic által használt:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - e-mail validációkra.
* <a href="https://docs.pydantic.dev/latest/usage/pydantic_settings/" target="_blank"><code>pydantic-settings</code></a> - Beállítások követésére.
* <a href="https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/" target="_blank"><code>pydantic-extra-types</code></a> - Extra típusok Pydantic-hoz.

Starlette által használt:

* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - Követelmény ha a `TestClient`-et akarod használni.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Követelmény ha az alap template konfigurációt akarod használni.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - Követelmény ha <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>-ot akarsz támogatni, `request.form()`-al.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Követelmény `SessionMiddleware` támogatáshoz.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Követelmény a Starlette `SchemaGenerator`-ának támogatásához (valószínűleg erre nincs szükség ReadyAPI használása esetén).

ReadyAPI / Starlette által használt

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - Szerverekhez amíg betöltik és szolgáltatják az applikációdat.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Követelmény ha `ORJSONResponse`-t akarsz használni.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Követelmény ha `UJSONResponse`-t akarsz használni.

Ezeket mind telepítheted a `pip install "readyapi[all]"` paranccsal.

## Licensz
Ez a projekt az MIT license, licensz alatt fut
