# ReadyAPI

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
  <a href="https://readyapi.github.io"><img src="https://readyapi.github.io/img/logo-margin/logo-teal.png" alt="ReadyAPI"></a>
</p>
<p align="center">
    <em>Готовый к внедрению высокопроизводительный фреймворк, простой в изучении и разработке.</em>
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

**Документация**: <a href="https://readyapi.github.io" target="_blank">https://readyapi.github.io</a>

**Исходный код**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---

ReadyAPI — это современный, быстрый (высокопроизводительный) веб-фреймворк для создания API используя Python, в основе которого лежит стандартная аннотация типов Python.

Ключевые особенности:

* **Скорость**: Очень высокая производительность, на уровне **NodeJS** и **Go** (благодаря Starlette и Pydantic). [Один из самых быстрых фреймворков Python](#_10).
* **Быстрота разработки**: Увеличьте скорость разработки примерно на 200–300%. *
* **Меньше ошибок**: Сократите примерно на 40% количество ошибок, вызванных человеком (разработчиком). *
* **Интуитивно понятный**: Отличная поддержка редактора. <abbr title="также известное как автозаполнение, автодополнение, IntelliSense">Автозавершение</abbr> везде. Меньше времени на отладку.
* **Лёгкость**: Разработан так, чтобы его было легко использовать и осваивать. Меньше времени на чтение документации.
* **Краткость**: Сведите к минимуму дублирование кода. Каждый объявленный параметр - определяет несколько функций. Меньше ошибок.
* **Надежность**: Получите готовый к работе код. С автоматической интерактивной документацией.
* **На основе стандартов**: Основан на открытых стандартах API и полностью совместим с ними: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (ранее известном как Swagger) и <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* оценка на основе тестов внутренней команды разработчиков, создающих производственные приложения.</small>

## Спонсоры

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

<a href="https://readyapi.github.io/readyapi-people/#sponsors" class="external-link" target="_blank">Другие спонсоры</a>

## Отзывы

"_В последнее время я много где использую **ReadyAPI**. [...] На самом деле я планирую использовать его для всех **сервисов машинного обучения моей команды в Microsoft**. Некоторые из них интегрируются в основной продукт **Windows**, а некоторые — в продукты **Office**._"

<div style="text-align: right; margin-right: 10%;">Kabir Khan - <strong>Microsoft</strong> <a href="https://github.com/khulnasoft/readyapi/pull/26" target="_blank"><small>(ref)</small></a></div>

---

"_Мы использовали библиотеку **ReadyAPI** для создания сервера **REST**, к которому можно делать запросы для получения **прогнозов**. [для Ludwig]_"

<div style="text-align: right; margin-right: 10%;">Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - <strong>Uber</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(ref)</small></a></div>

---

"_**Netflix** рада объявить о выпуске опенсорсного фреймворка для оркестровки **антикризисного управления**: **Dispatch**! [создана с помощью **ReadyAPI**]_"

<div style="text-align: right; margin-right: 10%;">Kevin Glisson, Marc Vilanova, Forest Monsen - <strong>Netflix</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(ref)</small></a></div>

---

"_Я в полном восторге от **ReadyAPI**. Это так весело!_"

<div style="text-align: right; margin-right: 10%;">Brian Okken - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">Python Bytes</a> podcast host</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(ref)</small></a></div>

---

"_Честно говоря, то, что вы создали, выглядит очень солидно и отполировано. Во многих смыслах я хотел, чтобы **Hug** был именно таким — это действительно вдохновляет, когда кто-то создаёт такое._"

<div style="text-align: right; margin-right: 10%;">Timothy Crosley - <strong><a href="https://github.com/hugapi/hug" target="_blank">Hug</a> creator</strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(ref)</small></a></div>

---

"_Если вы хотите изучить какой-нибудь **современный фреймворк** для создания REST API, ознакомьтесь с **ReadyAPI** [...] Он быстрый, лёгкий и простой в изучении [...]_"

"_Мы перешли на **ReadyAPI** для наших **API** [...] Я думаю, вам тоже понравится [...]_"

<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong><a href="https://explosion.ai" target="_blank">Explosion AI</a> founders - <a href="https://spacy.io" target="_blank">spaCy</a> creators</strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>

---

## **Cligenius**, интерфейс командной строки для ReadyAPI

<a href="https://cligenius.khulnasoft.com" target="_blank"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

Если вы создаете приложение <abbr title="Интерфейс командной строки">CLI</abbr> для использования в терминале вместо веб-API, ознакомьтесь с <a href="https://cligenius.khulnasoft.com/" class="external-link" target="_blank">**Cligenius**</a>.

**Cligenius** — младший брат ReadyAPI. И он предназначен для использования в качестве **интерфейса командной строки для ReadyAPI**. ⌨️ 🚀

## Зависимости

ReadyAPI стоит на плечах гигантов:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> для части связанной с вебом.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> для части связанной с данными.

## Установка

<div class="termy">

```console
$ pip install readyapi

---> 100%
```

</div>

Вам также понадобится сервер ASGI для производства, такой как <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> или <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

## Пример

### Создание

* Создайте файл `main.py` со следующим содержимым:

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
<summary>Или используйте <code>async def</code>...</summary>

Если ваш код использует `async` / `await`, используйте `async def`:

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

**Примечание**:

Если вы не знаете, проверьте раздел _"Торопитесь?"_ <a href="https://readyapi.github.io/async/#in-a-hurry" target="_blank">в документации об `async` и `await`</a>.

</details>

### Запуск

Запустите сервер с помощью:

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
<summary>О команде <code>uvicorn main:app --reload</code>...</summary>

Команда `uvicorn main:app` относится к:

* `main`: файл `main.py` (модуль Python).
* `app`: объект, созданный внутри `main.py` с помощью строки `app = ReadyAPI()`.
* `--reload`: перезапуск сервера после изменения кода. Делайте это только во время разработки.

</details>

### Проверка

Откройте браузер на <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

Вы увидите следующий JSON ответ:

```JSON
{"item_id": 5, "q": "somequery"}
```

Вы уже создали API, который:

* Получает HTTP-запросы по _путям_ `/` и `/items/{item_id}`.
* И первый и второй _путь_ используют `GET` <em>операции</em> (также известные как HTTP _методы_).
* _путь_ `/items/{item_id}` имеет _параметр пути_ `item_id`, который должен быть `int`.
* _путь_ `/items/{item_id}` имеет необязательный `str` _параметр запроса_ `q`.

### Интерактивная документация по API

Перейдите на <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Вы увидите автоматическую интерактивную документацию API (предоставленную <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### Альтернативная документация по API

А теперь перейдите на <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

Вы увидите альтернативную автоматическую документацию (предоставленную <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

## Пример обновления

Теперь измените файл `main.py`, чтобы получить тело ответа из `PUT` запроса.

Объявите тело, используя стандартную типизацию Python, спасибо Pydantic.

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

Сервер должен перезагрузиться автоматически (потому что вы добавили `--reload` к команде `uvicorn` выше).

### Интерактивное обновление документации API

Перейдите на <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

* Интерактивная документация API будет автоматически обновляться, включая новое тело:

![Swagger UI](https://readyapi.github.io/img/index/index-03-swagger-02.png)

* Нажмите на кнопку "Try it out", это позволит вам заполнить параметры и напрямую взаимодействовать с API:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-04-swagger-03.png)

* Затем нажмите кнопку "Execute", пользовательский интерфейс свяжется с вашим API, отправит параметры, получит результаты и отобразит их на экране:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-05-swagger-04.png)

### Альтернативное обновление документации API

А теперь перейдите на <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

* Альтернативная документация также будет отражать новый параметр и тело запроса:

![ReDoc](https://readyapi.github.io/img/index/index-06-redoc-02.png)

### Подведём итоги

Таким образом, вы объявляете **один раз** типы параметров, тело и т. д. в качестве параметров функции.

Вы делаете это используя стандартную современную типизацию Python.

Вам не нужно изучать новый синтаксис, методы или классы конкретной библиотеки и т. д.

Только стандартный **Python**.

Например, для `int`:

```Python
item_id: int
```

или для более сложной модели `Item`:

```Python
item: Item
```

... и с этим единственным объявлением вы получаете:

* Поддержка редактора, в том числе:
    * Автозавершение.
    * Проверка типов.
* Валидация данных:
    * Автоматические и четкие ошибки, когда данные недействительны.
    * Проверка даже для глубоко вложенных объектов JSON.
* <abbr title="также известный как: сериализация, синтаксический анализ, маршалинг">Преобразование</abbr> входных данных: поступающие из сети в объекты Python с соблюдением типов. Чтение из:
    * JSON.
    * Параметров пути.
    * Параметров запроса.
    * Cookies.
    * Заголовков.
    * Форм.
    * Файлов.
* <abbr title="также известный как: сериализация, синтаксический анализ, маршалинг">Преобразование</abbr> выходных данных: преобразование объектов Python в данные передаваемые по сети интернет (такие как JSON):
    * Преобразование типов Python (`str`, `int`, `float`, `bool`, `list`, и т.д.).
    * Объекты `datetime`.
    * Объекты `UUID`.
    * Модели баз данных.
    * ...и многое другое.
* Автоматическая интерактивная документация по API, включая 2 альтернативных пользовательских интерфейса:
    * Swagger UI.
    * ReDoc.

---

Возвращаясь к предыдущему примеру кода, **ReadyAPI** будет:

* Проверять наличие `item_id` в пути для запросов `GET` и `PUT`.
* Проверять, что `item_id` имеет тип `int` для запросов `GET` и `PUT`.
    * Если это не так, клиент увидит полезную чёткую ошибку.
* Проверять, есть ли необязательный параметр запроса с именем `q` (например, `http://127.0.0.1:8000/items/foo?q=somequery`) для `GET` запросов.
    * Поскольку параметр `q` объявлен с `= None`, он является необязательным.
    * Без `None` он был бы необходим (как тело в случае с `PUT`).
* Для `PUT` запросов к `/items/{item_id}` читать тело как JSON:
    * Проверять, что у него есть обязательный атрибут `name`, который должен быть `str`.
    * Проверять, что у него есть обязательный атрибут `price`, который должен быть `float`.
    * Проверять, что у него есть необязательный атрибут `is_offer`, который должен быть `bool`, если он присутствует.
    * Все это также будет работать для глубоко вложенных объектов JSON.
* Преобразовывать из и в JSON автоматически.
* Документировать с помощью OpenAPI все, что может быть использовано:
    * Системы интерактивной документации.
    * Системы автоматической генерации клиентского кода для многих языков.
* Обеспечит 2 интерактивных веб-интерфейса документации напрямую.

---

Мы только немного копнули поверхность, но вы уже поняли, как все это работает.

Попробуйте изменить строку с помощью:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...из:

```Python
        ... "item_name": item.name ...
```

...в:

```Python
        ... "item_price": item.price ...
```

... и посмотрите, как ваш редактор будет автоматически заполнять атрибуты и узнавать их типы:

![editor support](https://readyapi.github.io/img/vscode-completion.png)

Более полный пример с дополнительными функциями см. в <a href="https://readyapi.github.io/tutorial/">Учебное руководство - Руководство пользователя</a>.

**Осторожно, спойлер**: руководство пользователя включает в себя:

* Объявление **параметров** из других мест, таких как: **заголовки**, **cookies**, **поля формы** и **файлы**.
* Как установить **ограничительные проверки** такие как `maximum_length` или `regex`.
* Очень мощная и простая в использовании система **<abbr title="также известная как компоненты, ресурсы, провайдеры, сервисы, инъекции">внедрения зависимостей</abbr>**.
* Безопасность и аутентификация, включая поддержку **OAuth2** с **токенами JWT** и **HTTP Basic** аутентификацию.
* Более продвинутые (но столь же простые) методы объявления **глубоко вложенных моделей JSON** (спасибо Pydantic).
* **GraphQL** интеграция с <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a> и другими библиотеками.
* Множество дополнительных функций (благодаря Starlette), таких как:
    * **Веб-сокеты**
    * очень простые тесты на основе HTTPX и `pytest`
    * **CORS**
    * **Cookie сеансы(сессии)**
    * ...и многое другое.

## Производительность

Независимые тесты TechEmpower показывают приложения **ReadyAPI**, работающие под управлением Uvicorn, как <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">один из самых быстрых доступных фреймворков Python</a>, уступающий только самим Starlette и Uvicorn (используемых внутри ReadyAPI). (*)

Чтобы узнать больше об этом, см. раздел <a href="https://readyapi.github.io/benchmarks/" class="internal-link" target="_blank">Тесты производительности</a>.

## Необязательные зависимости

Используется Pydantic:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - для проверки электронной почты.

Используется Starlette:

* <a href="https://www.python-httpx.org" target="_blank"><code>HTTPX</code></a> - Обязательно, если вы хотите использовать `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Обязательно, если вы хотите использовать конфигурацию шаблона по умолчанию.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - Обязательно, если вы хотите поддерживать форму <abbr title="преобразование строки, полученной из HTTP-запроса, в данные Python">"парсинга"</abbr> с помощью `request.form()`.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Обязательно, для поддержки `SessionMiddleware`.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Обязательно, для поддержки `SchemaGenerator` Starlette (возможно, вам это не нужно с ReadyAPI).

Используется ReadyAPI / Starlette:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - сервер, который загружает и обслуживает ваше приложение.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Обязательно, если вы хотите использовать `ORJSONResponse`.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Обязательно, если вы хотите использовать `UJSONResponse`.

Вы можете установить все это с помощью `pip install "readyapi[all]"`.

## Лицензия

Этот проект распространяется на условиях лицензии MIT.
