# ReadyAPI

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
  <a href="https://readyapi.github.io"><img src="https://readyapi.github.io/img/logo-margin/logo-teal.png" alt="ReadyAPI"></a>
</p>
<p align="center">
    <em>فریم‌ورک ReadyAPI، کارایی بالا، یادگیری آسان، کدنویسی سریع، آماده برای استفاده در محیط پروداکشن</em>
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

**مستندات**: <a href="https://readyapi.github.io" target="_blank">https://readyapi.github.io</a>

**کد منبع**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---
ReadyAPI یک وب فریم‌ورک مدرن و سریع (با کارایی بالا) برای ایجاد APIهای متنوع (وب، وب‌سوکت و غبره) با زبان پایتون نسخه +۳.۶ است. این فریم‌ورک با رعایت کامل راهنمای نوع داده (Type Hint) ایجاد شده است.

ویژگی‌های کلیدی این فریم‌ورک عبارتند از:

* **<abbr title="Fast">سرعت</abbr>**: کارایی بسیار بالا و قابل مقایسه با  **NodeJS** و **Go** (با تشکر از Starlette و Pydantic). [یکی از سریع‌ترین فریم‌ورک‌های پایتونی موجود](#_10).

* **<abbr title="Fast to code">کدنویسی سریع</abbr>**: افزایش ۲۰۰ تا ۳۰۰ درصدی سرعت توسعه قابلیت‌های جدید. *
* **<abbr title="Fewer bugs">باگ کمتر</abbr>**: کاهش ۴۰ درصدی خطاهای انسانی (برنامه‌نویسی). *
* **<abbr title="Intuitive">هوشمندانه</abbr>**: پشتیبانی فوق‌العاده در محیط‌های توسعه یکپارچه (IDE). <abbr title="یا اتوکامپلیت، اتوکامپلشن، اینتلیسنس">تکمیل</abbr> در همه بخش‌های کد. کاهش زمان رفع باگ.
* **<abbr title="Easy">آسان</abbr>**: طراحی شده برای یادگیری و استفاده آسان. کاهش زمان مورد نیاز برای مراجعه به مستندات.
* **<abbr title="Short">کوچک</abbr>**: کاهش تکرار در کد. چندین قابلیت برای هر پارامتر (منظور پارامترهای ورودی تابع هندلر می‌باشد، به بخش <a href="https://readyapi.github.io/#recap">خلاصه</a> در همین صفحه مراجعه شود). باگ کمتر.
* **<abbr title="Robust">استوار</abbr>**: ایجاد کدی آماده برای استفاده در محیط پروداکشن و تولید خودکار <abbr title="Interactive documentation">مستندات تعاملی</abbr>
* **<abbr title="Standards-based">مبتنی بر استانداردها</abbr>**: مبتنی بر (و منطبق با) استانداردهای متن باز مربوط به API: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (سوگر سابق) و <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* تخمین‌ها بر اساس تست‌های انجام شده در یک تیم توسعه داخلی که مشغول ایجاد برنامه‌های کاربردی واقعی بودند صورت گرفته است.</small>

## اسپانسرهای طلایی

<!-- sponsors -->

{% if sponsors %}
{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}"></a>
{% endfor %}
{% endif %}

<!-- /sponsors -->

<a href="https://readyapi.github.io/readyapi-people/#sponsors" class="external-link" target="_blank">دیگر اسپانسرها</a>

## نظر دیگران در مورد ReadyAPI

<div style="text-align: left; direction: ltr;"><em> [...] I'm using <strong>ReadyAPI</strong> a ton these days. [...] I'm actually planning to use it for all of my team's <strong>ML services at Microsoft</strong>. Some of them are getting integrated into the core <strong>Windows</strong> product and some <strong>Office</strong> products."</em></div>

<div style="text-align: right; margin-right: 10%;">Kabir Khan - <strong>Microsoft</strong> <a href="https://github.com/khulnasoft/readyapi/pull/26" target="_blank"><small>(ref)</small></a></div>

---

<div style="text-align: left; direction: ltr;"><em>"We adopted the <strong>ReadyAPI</strong> library to spawn a <strong>REST</strong>server that can be queried to obtain <strong>predictions</strong>. [for Ludwig]"</em></div>

<div style="text-align: right; margin-right: 10%;">Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - <strong>Uber</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(ref)</small></a></div>

---

<div style="text-align: left; direction: ltr;">"<strong>Netflix</strong> is pleased to announce the open-source release of our <strong>crisis management</strong> orchestration framework: <strong>Dispatch</strong>! [built with <strong>ReadyAPI</strong>]"</div>

<div style="text-align: right; margin-right: 10%;">Kevin Glisson, Marc Vilanova, Forest Monsen - <strong>Netflix</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(ref)</small></a></div>

---

<div style="text-align: left; direction: ltr;">"<em>I’m over the moon excited about <strong>ReadyAPI</strong>. It’s so fun!"</em></div>

<div style="text-align: right; margin-right: 10%;">Brian Okken - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">Python Bytes</a> podcast host</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(ref)</small></a></div>

---

<div style="text-align: left; direction: ltr;">"<em>Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted <strong>Hug</strong> to be - it's really inspiring to see someone build that."</em></div>

<div style="text-align: right; margin-right: 10%;">Timothy Crosley - <strong><a href="https://github.com/hugapi/hug" target="_blank">Hug</a> creator</strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(ref)</small></a></div>

---

<div style="text-align: left; direction: ltr;">"<em>If you're looking to learn one <strong>modern framework</strong> for building REST APIs, check out <strong>ReadyAPI</strong> [...] It's fast, easy to use and easy to learn [...]"</em></div>

<div style="text-align: left; direction: ltr;">"<em>We've switched over to <strong>ReadyAPI</strong> for our <strong>APIs</strong> [...] I think you'll like it [...]</em>"</div>

<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong><a href="https://explosion.ai" target="_blank">Explosion AI</a> founders - <a href="https://spacy.io" target="_blank">spaCy</a> creators</strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>

---

## **Cligenius**, فریم‌ورکی معادل ReadyAPI برای کار با <abbr title="CLI (Command Line Interface)">واسط خط فرمان</abbr>

<a href="https://cligenius.khulnasoft.com" target="_blank"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

اگر در حال ساختن برنامه‌ای برای استفاده در <abbr title="Command Line Interface">CLI</abbr> (به جای استفاده در وب) هستید، می‌توانید از <a href="https://cligenius.khulnasoft.com/" class="external-link" target="_blank">**Cligenius**</a>. استفاده کنید.

**Cligenius** دوقلوی کوچکتر ReadyAPI است و قرار است معادلی برای ReadyAPI در برنامه‌های CLI باشد.️ 🚀

## نیازمندی‌ها

پایتون +۳.۶

ReadyAPI مبتنی بر ابزارهای قدرتمند زیر است:

* فریم‌ورک <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> برای بخش وب.
* کتابخانه <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> برای بخش داده‌.

## نصب

<div class="termy">

```console
$ pip install readyapi

---> 100%
```

</div>

نصب یک سرور پروداکشن نظیر <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> یا <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a> نیز جزء نیازمندی‌هاست.

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

## مثال

### ایجاد کنید
* فایلی به نام `main.py` با محتوای زیر ایجاد کنید:

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
<summary>همچنین می‌توانید از <code>async def</code>... نیز استفاده کنید</summary>

اگر در کدتان از `async` / `await` استفاده می‌کنید، از `async def` برای تعریف تابع خود استفاده کنید:

```Python hl_lines="9  14"
from typing import Optional

from readyapi import ReadyAPI

app = ReadyAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

**توجه**:

اگر با `async / await` آشنا نیستید، به بخش _"عجله‌ دارید?"_ در صفحه درباره <a href="https://readyapi.github.io/async/#in-a-hurry" target="_blank">`async` و `await` در مستندات</a> مراجعه کنید.


</details>

### اجرا کنید

با استفاده از دستور زیر سرور را اجرا کنید:

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
<summary>درباره دستور <code>uvicorn main:app --reload</code>...</summary>

دستور `uvicorn main:app` شامل موارد زیر است:

* `main`: فایل `main.py` (ماژول پایتون ایجاد شده).
* `app`: شیء ایجاد شده در فایل `main.py` در خط `app = ReadyAPI()`.
* `--reload`: ریستارت کردن سرور با تغییر کد. تنها در هنگام توسعه از این گزینه استفاده شود..

</details>

### بررسی کنید

آدرس <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a> را در مرورگر خود باز کنید.

پاسخ JSON زیر را مشاهده خواهید کرد:

```JSON
{"item_id": 5, "q": "somequery"}
```

تا اینجا شما APIای ساختید که:

* درخواست‌های HTTP به _مسیرهای_ `/` و `/items/{item_id}` را دریافت می‌کند.
* هردو  _مسیر_ <abbr title="operations در OpenAPI">عملیات</abbr> (یا HTTP _متد_) `GET` را پشتیبانی می‌کند.
* _مسیر_ `/items/{item_id}` شامل  <abbr title="Path Parameter">_پارامتر مسیر_</abbr> `item_id` از نوع `int` است.
* _مسیر_ `/items/{item_id}` شامل  <abbr title="Query Parameter">_پارامتر پرسمان_</abbr> اختیاری `q` از نوع `str` است.

### مستندات API تعاملی

حال به آدرس  <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> بروید.

مستندات API تعاملی (ایجاد شده به کمک <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>) را مشاهده خواهید کرد:

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### مستندات API جایگزین

حال به آدرس  <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> بروید.

مستندات خودکار دیگری را مشاهده خواهید کرد که به کمک <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a> ایجاد می‌شود:

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

## تغییر مثال

حال فایل `main.py` را مطابق زیر ویرایش کنید تا بتوانید <abbr title="Body">بدنه</abbr> یک درخواست `PUT` را دریافت کنید.

به کمک Pydantic بدنه درخواست را با <abbr title="Type">انواع</abbr> استاندارد پایتون تعریف کنید.

```Python hl_lines="4  9-12  25-27"
from typing import Optional

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

سرور به صورت خودکار ری‌استارت می‌شود (زیرا پیشتر از گزینه `--reload` در دستور  `uvicorn`  استفاده کردیم).

### تغییر مستندات API تعاملی

مجددا به آدرس  <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> بروید.

* مستندات API تعاملی به صورت خودکار به‌روز شده است و شامل بدنه تعریف شده در مرحله قبل است:

![Swagger UI](https://readyapi.github.io/img/index/index-03-swagger-02.png)

* روی دکمه "Try it out" کلیک کنید، اکنون می‌توانید پارامترهای مورد نیاز هر API را مشخص کرده و به صورت مستقیم با آنها تعامل کنید:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-04-swagger-03.png)

* سپس روی دکمه "Execute" کلیک کنید، خواهید دید که واسط کاربری با APIهای تعریف شده ارتباط برقرار کرده، پارامترهای مورد نیاز را به آن‌ها ارسال می‌کند، سپس نتایج را دریافت کرده و در صفحه نشان می‌دهد:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-05-swagger-04.png)

### تغییر مستندات API جایگزین

حال به آدرس <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> بروید.

* خواهید دید که مستندات جایگزین نیز به‌روزرسانی شده و شامل پارامتر پرسمان و بدنه تعریف شده می‌باشد:

![ReDoc](https://readyapi.github.io/img/index/index-06-redoc-02.png)

### خلاصه

به طور خلاصه شما **یک بار** انواع پارامترها، بدنه و غیره را به عنوان پارامترهای ورودی تابع خود تعریف می‌کنید.

 این کار را با استفاده از انواع استاندارد و مدرن موجود در پایتون انجام می‌دهید.

نیازی به یادگیری <abbr title="Syntax">نحو</abbr> جدید یا متدها و کلاس‌های یک کتابخانه بخصوص و غیره نیست.

تنها  **پایتون +۳.۶**.

به عنوان مثال برای یک پارامتر از نوع `int`:

```Python
item_id: int
```

یا برای یک مدل پیچیده‌تر مثل `Item`:

```Python
item: Item
```

...و با همین اعلان تمامی قابلیت‌های زیر در دسترس قرار می‌گیرد:

* پشتیبانی ویرایشگر متنی شامل:
    * تکمیل کد.
    * بررسی انواع داده.
* اعتبارسنجی داده:
    * خطاهای خودکار و مشخص در هنگام نامعتبر بودن داده.
    * اعتبارسنجی، حتی برای اشیاء JSON تو در تو.
* <abbr title="serialization, parsing, marshalling">تبدیل</abbr> داده ورودی: که از شبکه رسیده به انواع و داد‌ه‌ پایتونی. این داده‌ شامل:
    * JSON.
    * <abbr title="Path parameters">پارامترهای مسیر</abbr>.
    * <abbr title="Query parameters">پارامترهای پرسمان</abbr>.
    * <abbr title="Cookies">کوکی‌ها</abbr>.
    * <abbr title="Headers">سرآیند‌ها (هدرها)</abbr>.
    * <abbr title="Forms">فرم‌ها</abbr>.
    * <abbr title="Files">فایل‌ها</abbr>.
* <abbr title="serialization, parsing, marshalling">تبدیل</abbr> داده خروجی: تبدیل از انواع و داده‌ پایتون به داده شبکه  (مانند JSON):
    * تبدیل انواع داده پایتونی (`str`, `int`, `float`, `bool`, `list` و غیره).
    * اشیاء `datetime`.
    * اشیاء `UUID`.
    * qمدل‌های پایگاه‌داده.
    * و موارد بیشمار دیگر.
* دو مدل مستند API تعاملی خودکار :
    * Swagger UI.
    * ReDoc.

---

به مثال قبلی باز می‌گردیم، در این مثال **ReadyAPI** موارد زیر را انجام می‌دهد:

* اعتبارسنجی اینکه پارامتر `item_id` در مسیر درخواست‌های `GET` و `PUT` موجود است.
* اعتبارسنجی اینکه پارامتر `item_id` در درخواست‌های `GET` و `PUT` از نوع `int` است.
    * اگر غیر از این موارد باشد، سرویس‌گیرنده خطای مفید و مشخصی دریافت خواهد کرد.
* بررسی وجود پارامتر پرسمان اختیاری `q` (مانند `http://127.0.0.1:8000/items/foo?q=somequery`) در درخواست‌های `GET`.
    * از آنجا که پارامتر `q` با  `= None` مقداردهی شده است، این پارامتر اختیاری است.
    * اگر از مقدار اولیه `None` استفاده نکنیم، این پارامتر الزامی خواهد بود (همانند بدنه درخواست در درخواست `PUT`).
* برای درخواست‌های `PUT` به آدرس `/items/{item_id}`، بدنه درخواست باید از نوع JSON تعریف شده باشد:
    * بررسی اینکه بدنه شامل فیلدی با نام `name` و از نوع `str` است.
    * بررسی اینکه بدنه شامل فیلدی با نام `price` و از نوع `float` است.
    * بررسی اینکه بدنه شامل فیلدی اختیاری با نام `is_offer` است، که در صورت وجود باید از نوع `bool` باشد.
    * تمامی این موارد برای اشیاء JSON در هر عمقی قابل بررسی می‌باشد.
* تبدیل از/به JSON به صورت خودکار.
* مستندسازی همه چیز با استفاده از OpenAPI، که می‌توان از آن برای موارد زیر استفاده کرد:
    * سیستم مستندات تعاملی.
    * تولید خودکار کد سرویس‌گیرنده‌ در زبان‌های برنامه‌نویسی بیشمار.
* فراهم سازی ۲ مستند تعاملی مبتنی بر وب به صورت پیش‌فرض.

---

موارد ذکر شده تنها پاره‌ای از ویژگی‌های بیشمار ReadyAPI است اما ایده‌ای کلی از طرز کار آن در اختیار قرار می‌دهد.

خط زیر را به این صورت تغییر دهید:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

از:

```Python
        ... "item_name": item.name ...
```

به:

```Python
        ... "item_price": item.price ...
```

در حین تایپ کردن توجه کنید که چگونه ویرایش‌گر، ویژگی‌های کلاس  `Item` را تشخیص داده و به تکمیل خودکار آنها کمک می‌کند:

![editor support](https://readyapi.github.io/img/vscode-completion.png)

برای مشاهده مثال‌های کامل‌تر که شامل قابلیت‌های بیشتری از ReadyAPI باشد به بخش <a href="https://readyapi.github.io/tutorial/">آموزش - راهنمای کاربر</a> مراجعه کنید.

**هشدار اسپویل**: بخش آموزش - راهنمای کاربر شامل موارد زیر است:

* اعلان **پارامترهای** موجود در بخش‌های دیگر درخواست، شامل: **سرآیند‌ (هدر)ها**، **کوکی‌ها**، **فیلد‌های فرم** و **فایل‌ها**.
* چگونگی تنظیم **<abbr title="Validation Constraints">محدودیت‌های اعتبارسنجی</abbr>** به عنوان مثال `maximum_length` یا `regex`.
* سیستم **<abbr title="also known as components, resources, providers, services, injectables">Dependency Injection</abbr>** قوی و کاربردی.
* امنیت و تایید هویت, شامل پشتیبانی از **OAuth2** مبتنی بر **JWT tokens** و **HTTP Basic**.
* تکنیک پیشرفته برای تعریف **مدل‌های چند سطحی JSON** (بر اساس Pydantic).
* قابلیت‌های اضافی دیگر (بر اساس Starlette) شامل:
    * **<abbr title="WebSocket">وب‌سوکت</abbr>**
    * **GraphQL**
    * تست‌های خودکار آسان مبتنی بر HTTPX و `pytest`
    * **CORS**
    * **Cookie Sessions**
    * و موارد بیشمار دیگر.

## کارایی

معیار (بنچمارک‌)های مستقل TechEmpower حاکی از آن است که برنامه‌های **ReadyAPI** که تحت Uvicorn اجرا می‌شود، <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">یکی از سریع‌ترین فریم‌ورک‌های مبتنی بر پایتون</a>، است که کمی ضعیف‌تر از Starlette و Uvicorn عمل می‌کند (فریم‌ورک و سروری که ReadyAPI بر اساس آنها ایجاد شده است) (*)

برای درک بهتری از این موضوع به بخش <a href="https://readyapi.github.io/benchmarks/" class="internal-link" target="_blank">بنچ‌مارک‌ها</a> مراجعه کنید.

## نیازمندی‌های اختیاری

استفاده شده توسط Pydantic:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - برای اعتبارسنجی آدرس‌های ایمیل.

استفاده شده توسط Starlette:

* <a href="https://www.python-httpx.org" target="_blank"><code>HTTPX</code></a> - در صورتی که می‌خواهید از `TestClient` استفاده کنید.
* <a href="https://github.com/Tinche/aiofiles" target="_blank"><code>aiofiles</code></a> - در صورتی که می‌خواهید از `FileResponse` و `StaticFiles` استفاده کنید.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - در صورتی که بخواهید از پیکربندی پیش‌فرض برای قالب‌ها استفاده کنید.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - در صورتی که بخواهید با استفاده از `request.form()` از قابلیت <abbr title="تبدیل رشته متنی موجود در درخواست HTTP به انواع داده پایتون">"تجزیه (parse)"</abbr> فرم استفاده کنید.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - در صورتی که بخواید از `SessionMiddleware` پشتیبانی کنید.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - برای پشتیبانی `SchemaGenerator` در Starlet (به احتمال زیاد برای کار کردن با ReadyAPI به آن نیازی پیدا نمی‌کنید).
* <a href="https://graphene-python.org/" target="_blank"><code>graphene</code></a> - در صورتی که از  `GraphQLApp` پشتیبانی می‌کنید.

استفاده شده توسط ReadyAPI / Starlette:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - برای سرور اجرا کننده برنامه وب.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - در صورتی که بخواهید از `ORJSONResponse` استفاده کنید.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - در صورتی که بخواهید از `UJSONResponse` استفاده کنید.

می‌توان همه این موارد را با استفاده از دستور `pip install readyapi[all]`. به صورت یکجا نصب کرد.

##   لایسنس

این پروژه مشمول قوانین و مقررات لایسنس MIT است.
