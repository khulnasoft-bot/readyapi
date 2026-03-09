<p align="center">
  <a href="https://readyapi.github.io"><img src="https://readyapi.github.io/img/logo-margin/logo-teal.png" alt="ReadyAPI"></a>
</p>
<p align="center">
    <em>Готовий до продакшину, високопродуктивний, простий у вивченні та швидкий для написання коду фреймворк</em>
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

**Документація**: <a href="https://readyapi.github.io" target="_blank">https://readyapi.github.io</a>

**Програмний код**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---

ReadyAPI - це сучасний, швидкий (високопродуктивний), вебфреймворк для створення API за допомогою Python,в основі якого лежить стандартна анотація типів Python.

Ключові особливості:

* **Швидкий**: Дуже висока продуктивність, на рівні з **NodeJS** та **Go** (завдяки Starlette та Pydantic). [Один із найшвидших фреймворків](#performance).

* **Швидке написання коду**: Пришвидшує розробку функціоналу приблизно на 200%-300%. *
* **Менше помилок**: Зменшить кількість помилок спричинених людиною (розробником) на 40%. *
* **Інтуїтивний**: Чудова підтримка редакторами коду. <abbr title="Також відоме як auto-complete, autocompletion, IntelliSense.">Доповнення</abbr> всюди. Зменште час на налагодження.
* **Простий**: Спроектований, для легкого використання та навчання. Знадобиться менше часу на читання документації.
* **Короткий**: Зведе до мінімуму дублювання коду. Кожен оголошений параметр може виконувати кілька функцій.
* **Надійний**: Ви матимете стабільний код готовий до продакшину з автоматичною інтерактивною документацією.
* **Стандартизований**: Оснований та повністю сумісний з відкритими стандартами для API: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (попередньо відомий як Swagger) та <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* оцінка на основі тестів внутрішньої команди розробників, створення продуктових застосунків.</small>

## Спонсори

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

<a href="https://readyapi.github.io/readyapi-people/#sponsors" class="external-link" target="_blank">Other sponsors</a>

## Враження

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

## **Cligenius**, ReadyAPI CLI

<a href="https://cligenius.khulnasoft.com" target="_blank"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

Створюючи <abbr title="Command Line Interface">CLI</abbr> застосунок для використання в терміналі, замість веб-API зверніть увагу на <a href="https://cligenius.khulnasoft.com/" class="external-link" target="_blank">**Cligenius**</a>.

**Cligenius** є молодшим братом ReadyAPI. І це **ReadyAPI для CLI**. ⌨️ 🚀

## Вимоги

ReadyAPI стоїть на плечах гігантів:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> для web частини.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> для частини даних.

## Вставновлення

<div class="termy">

```console
$ pip install readyapi

---> 100%
```

</div>

Вам також знадобиться сервер ASGI для продакшину, наприклад <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> або <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div class="termy">

```console
$ pip install uvicorn[standard]

---> 100%
```

</div>

## Приклад

### Створіть

* Створіть файл `main.py` з:

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
<summary>Або використайте <code>async def</code>...</summary>

Якщо ваш код використовує `async` / `await`, скористайтеся `async def`:

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

**Примітка**:

Стикнувшись з проблемами, не зайвим буде ознайомитися з розділом _"In a hurry?"_ про <a href="https://readyapi.github.io/async/#in-a-hurry" target="_blank">`async` та `await` у документації</a>.

</details>

### Запустіть

Запустіть server з:

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
<summary>Про команди <code>uvicorn main:app --reload</code>...</summary>

Команда `uvicorn main:app` посилається на:

* `main`: файл `main.py` ("Модуль" Python).
* `app`: об’єкт створений усередині `main.py` рядком `app = ReadyAPI()`.
* `--reload`: перезапускає сервер після зміни коду. Використовуйте виключно для розробки.

</details>

### Перевірте

Відкрийте браузер та введіть адресу <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

Ви побачите у відповідь подібний JSON:

```JSON
{"item_id": 5, "q": "somequery"}
```

Ви вже створили API, який:

* Отримує HTTP запити за _шляхами_ `/` та `/items/{item_id}`.
* Обидва _шляхи_ приймають `GET` <em>операції</em> (також відомі як HTTP _методи_).
* _Шлях_ `/items/{item_id}` містить _параметр шляху_ `item_id` який має бути типу `int`.
* _Шлях_ `/items/{item_id}` містить необовʼязковий `str` _параметр запиту_ `q`.

### Інтерактивні документації API

Перейдемо сюди <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Ви побачите автоматичну інтерактивну API документацію (створену завдяки <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### Альтернативні документації API

Тепер перейдемо сюди <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

Ви побачите альтернативну автоматичну документацію (створену завдяки  <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

## Приклад оновлення

Тепер модифікуйте файл `main.py`, щоб отримати вміст запиту `PUT`.

Оголошуйте вміст запиту за допомогою стандартних типів Python завдяки Pydantic.

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

Сервер повинен автоматично перезавантажуватися (тому що Ви додали `--reload` до `uvicorn` команди вище).

### Оновлення інтерактивної API документації

Тепер перейдемо сюди <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

* Інтерактивна документація API буде автоматично оновлена, включаючи новий вміст:

![Swagger UI](https://readyapi.github.io/img/index/index-03-swagger-02.png)

* Натисніть кнопку "Try it out", це дозволить вам заповнити параметри та безпосередньо взаємодіяти з API:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-04-swagger-03.png)

* Потім натисніть кнопку "Execute", інтерфейс користувача зв'яжеться з вашим API, надішле параметри, у відповідь отримає результати та покаже їх на екрані:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-05-swagger-04.png)

### Оновлення альтернативної API документації

Зараз перейдемо <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

* Альтернативна документація також показуватиме новий параметр і вміст запиту:

![ReDoc](https://readyapi.github.io/img/index/index-06-redoc-02.png)

### Підсумки

Таким чином, Ви  **один раз** оголошуєте типи параметрів, тіла тощо, як параметри функції.

Ви робите це за допомогою стандартних сучасних типів Python.

Вам не потрібно вивчати новий синтаксис, методи чи класи конкретної бібліотеки тощо.

Використовуючи стандартний **Python**.

Наприклад, для `int`:

```Python
item_id: int
```

або для більш складної моделі `Item`:

```Python
item: Item
```

...і з цим єдиним оголошенням Ви отримуєте:

* Підтримку редактора, включаючи:
    * Варіанти заповнення.
    * Перевірку типів.
* Перевірку даних:
    * Автоматичні та зрозумілі помилки, у разі некоректних даних.
    * Перевірка навіть для JSON з високим рівнем вкладеності.
* <abbr title="також відомий як: serialization, parsing, marshalling">Перетворення</abbr> вхідних даних: з мережі до даних і типів Python. Читання з:
    * JSON.
    * Параметрів шляху.
    * Параметрів запиту.
    * Cookies.
    * Headers.
    * Forms.
    * Файлів.
* <abbr title="також відомий як: serialization, parsing, marshalling">Перетворення</abbr> вихідних даних: з типів і даних Python до мережевих даних (як JSON):
    * Конвертація Python типів (`str`, `int`, `float`, `bool`, `list`, тощо).
    * `datetime` об'єкти.
    * `UUID` об'єкти.
    * Моделі бази даних.
    * ...та багато іншого.
* Автоматичну інтерактивну документацію API, включаючи 2 альтернативні інтерфейси користувача:
    * Swagger UI.
    * ReDoc.

---

Повертаючись до попереднього прикладу коду, **ReadyAPI**:

* Підтвердить наявність `item_id` у шляху для запитів `GET` та `PUT`.
* Підтвердить, що `item_id` має тип `int` для запитів `GET` and `PUT`.
    * Якщо це не так, клієнт побачить корисну, зрозумілу помилку.
* Перевірить, чи є необов'язковий параметр запиту з назвою `q` (а саме `http://127.0.0.1:8000/items/foo?q=somequery`) для запитів `GET`.
    * Оскільки параметр `q` оголошено як `= None`, він необов'язковий.
    * За відсутності `None` він був би обов'язковим (як і вміст у випадку з `PUT`).
* Для запитів `PUT` із `/items/{item_id}`, читає вміст як JSON:
    * Перевірить, чи має обов'язковий атрибут `name` тип `str`.
    * Перевірить, чи має обов'язковий атрибут `price` тип `float`.
    * Перевірить, чи існує необов'язковий атрибут `is_offer` та чи має він тип `bool`.
    * Усе це також працюватиме для глибоко вкладених об'єктів JSON.
* Автоматично конвертує із та в JSON.
* Документує все за допомогою OpenAPI, який може бути використано в:
    * Інтерактивних системах документації.
    * Системах автоматичної генерації клієнтського коду для багатьох мов.
* Надає безпосередньо 2 вебінтерфейси інтерактивної документації.

---

Ми лише трішки доторкнулися до коду, але Ви вже маєте уявлення про те, як все працює.

Спробуйте змінити рядок:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...із:

```Python
        ... "item_name": item.name ...
```

...на:

```Python
        ... "item_price": item.price ...
```

...і побачите, як ваш редактор автоматично заповнюватиме атрибути та знатиме їхні типи:

![editor support](https://readyapi.github.io/img/vscode-completion.png)

Для більш повного ознайомлення з додатковими функціями, перегляньте <a href="https://readyapi.github.io/tutorial/">Туторіал - Посібник Користувача</a>.

**Spoiler alert**: туторіал - посібник користувача містить:

* Оголошення **параметрів** з інших місць як: **headers**, **cookies**, **form fields** та **files**.
* Як встановити **перевірку обмежень** як `maximum_length` або `regex`.
* Дуже потужна і проста у використанні система **<abbr title="також відома як: components, resources, providers, services, injectables">Ін'єкція Залежностей</abbr>**.
* Безпека та автентифікація, включаючи підтримку **OAuth2** з **JWT tokens** та **HTTP Basic** автентифікацію.
* Досконаліші (але однаково прості) техніки для оголошення **глибоко вкладених моделей JSON** (завдяки Pydantic).
* Багато додаткових функцій (завдяки Starlette) як-от:
    * **WebSockets**
    * надзвичайно прості тести на основі HTTPX та `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...та більше.

## Продуктивність

Незалежні тести TechEmpower показують що застосунки **ReadyAPI**, які працюють під керуванням Uvicorn <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">є одними з найшвидших серед доступних фреймворків в Python</a>, поступаючись лише Starlette та Uvicorn (які внутрішньо використовуються в ReadyAPI). (*)

Щоб дізнатися більше про це, перегляньте розділ <a href="https://readyapi.github.io/benchmarks/" class="internal-link" target="_blank">Benchmarks</a>.

## Необов'язкові залежності

Pydantic використовує:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - для валідації електронної пошти.
* <a href="https://docs.pydantic.dev/latest/usage/pydantic_settings/" target="_blank"><code>pydantic-settings</code></a> - для управління налаштуваннями.
* <a href="https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/" target="_blank"><code>pydantic-extra-types</code></a> - для додаткових типів, що можуть бути використані з Pydantic.


Starlette використовує:

* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - Необхідно, якщо Ви хочете використовувати `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Необхідно, якщо Ви хочете використовувати шаблони як конфігурацію за замовчуванням.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - Необхідно, якщо Ви хочете підтримувати <abbr title="перетворення рядка, який надходить із запиту HTTP, на дані Python">"розбір"</abbr> форми за допомогою `request.form()`.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Необхідно для підтримки `SessionMiddleware`.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Необхідно для підтримки Starlette `SchemaGenerator` (ймовірно, вам це не потрібно з ReadyAPI).

ReadyAPI / Starlette використовують:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - для сервера, який завантажує та обслуговує вашу програму.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Необхідно, якщо Ви хочете використовувати `ORJSONResponse`.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Необхідно, якщо Ви хочете використовувати `UJSONResponse`.

Ви можете встановити все це за допомогою `pip install readyapi[all]`.

## Ліцензія

Цей проєкт ліцензовано згідно з умовами ліцензії MIT.
