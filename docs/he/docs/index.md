# ReadyAPI

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
  <a href="https://readyapi.github.io"><img src="https://readyapi.github.io/img/logo-margin/logo-teal.png" alt="ReadyAPI"></a>
</p>
<p align="center">
     <em>תשתית ReadyAPI, ביצועים גבוהים, קלה ללמידה, מהירה לתכנות, מוכנה לסביבת ייצור</em>
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

**תיעוד**: <a href="https://readyapi.github.io" target="_blank">https://readyapi.github.io</a>

**קוד**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---

ReadyAPI היא תשתית רשת מודרנית ומהירה (ביצועים גבוהים) לבניית ממשקי תכנות יישומים (API) עם פייתון 3.6+ בהתבסס על רמזי טיפוסים סטנדרטיים.

תכונות המפתח הן:

-   **מהירה**: ביצועים גבוהים מאוד, בקנה אחד עם NodeJS ו - Go (תודות ל - Starlette ו - Pydantic). [אחת מתשתיות הפייתון המהירות ביותר](#_14).

-   **מהירה לתכנות**: הגבירו את מהירות פיתוח התכונות החדשות בכ - %200 עד %300. \*
-   **פחות שגיאות**: מנעו כ - %40 משגיאות אנוש (מפתחים). \*
-   **אינטואיטיבית**: תמיכת עורך מעולה. <abbr title="ידועה גם כהשלמה אוטומטית או IntelliSense">השלמה</abbr> בכל מקום. פחות זמן ניפוי שגיאות.
-   **קלה**: מתוכננת להיות קלה לשימוש וללמידה. פחות זמן קריאת תיעוד.
-   **קצרה**: מזערו שכפול קוד. מספר תכונות מכל הכרזת פרמטר. פחות שגיאות.
-   **חסונה**: קבלו קוד מוכן לסביבת ייצור. עם תיעוד אינטרקטיבי אוטומטי.
-   **מבוססת סטנדרטים**: מבוססת על (ותואמת לחלוטין ל -) הסטדנרטים הפתוחים לממשקי תכנות יישומים: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (ידועים לשעבר כ - Swagger) ו - <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>\* הערכה מבוססת על בדיקות של צוות פיתוח פנימי שבונה אפליקציות בסביבת ייצור.</small>

## נותני חסות

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

<a href="https://readyapi.github.io/readyapi-people/#sponsors" class="external-link" target="_blank">נותני חסות אחרים</a>

## דעות

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

## **Cligenius**, ה - ReadyAPI של ממשקי שורת פקודה (CLI).

<a href="https://cligenius.khulnasoft.com" target="_blank"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

אם אתם בונים אפליקציית <abbr title="ממשק שורת פקודה">CLI</abbr> לשימוש במסוף במקום ממשק רשת, העיפו מבט על <a href="https://cligenius.khulnasoft.com/" class="external-link" target="_blank">**Cligenius**</a>.

**Cligenius** היא אחותה הקטנה של ReadyAPI. ומטרתה היא להיות ה - **ReadyAPI של ממשקי שורת פקודה**. ⌨️ 🚀

## תלויות

פייתון 3.6+

ReadyAPI עומדת על כתפי ענקיות:

-   <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> לחלקי הרשת.
-   <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> לחלקי המידע.

## התקנה

<div dir="ltr" class="termy">

```console
$ pip install readyapi

---> 100%
```

</div>

תצטרכו גם שרת ASGI כגון <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> או <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div dir="ltr" class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

## דוגמא

### צרו אותה

-   צרו קובץ בשם `main.py` עם:

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
<summary>או השתמשו ב - <code>async def</code>...</summary>

אם הקוד שלכם משתמש ב - `async` / `await`, השתמשו ב - `async def`:

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

**שימו לב**:

אם אינכם יודעים, בדקו את פרק "ממהרים?" על <a href="https://readyapi.github.io/async/#in-a-hurry" target="_blank">`async` ו - `await` בתיעוד</a>.

</details>

### הריצו אותה

התחילו את השרת עם:

<div dir="ltr" class="termy">

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
<summary>על הפקודה <code>uvicorn main:app --reload</code>...</summary>

הפקודה `uvicorn main:app` מתייחסת ל:

-   `main`: הקובץ `main.py` (מודול פייתון).
-   `app`: האובייקט שנוצר בתוך `main.py` עם השורה <code dir="ltr">app = ReadyAPI()</code>.
-   <code dir="ltr">--reload</code>: גרמו לשרת להתאתחל לאחר שינויים בקוד. עשו זאת רק בסביבת פיתוח.

</details>

### בדקו אותה

פתחו את הדפדפן שלכם בכתובת <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

אתם תראו תגובת JSON:

```JSON
{"item_id": 5, "q": "somequery"}
```

כבר יצרתם API ש:

-   מקבל בקשות HTTP בנתיבים `/` ו - <code dir="ltr">/items/{item_id}</code>.
-   שני ה _נתיבים_ מקבלים _בקשות_ `GET` (ידועות גם כ*מתודות* HTTP).
-   ה _נתיב_ <code dir="ltr">/items/{item_id}</code> כולל \*פרמטר נתיב\_ `item_id` שאמור להיות `int`.
-   ה _נתיב_ <code dir="ltr">/items/{item_id}</code> \*פרמטר שאילתא\_ אופציונלי `q`.

### תיעוד API אינטרקטיבי

כעת פנו לכתובת <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

אתם תראו את התיעוד האוטומטי (מסופק על ידי <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### תיעוד אלטרנטיבי

כעת פנו לכתובת <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

אתם תראו תיעוד אלטרנטיבי (מסופק על ידי <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

## שדרוג לדוגמא

כעת ערכו את הקובץ `main.py` כך שיוכל לקבל גוף מבקשת `PUT`.

הגדירו את הגוף בעזרת רמזי טיפוסים סטנדרטיים, הודות ל - `Pydantic`.

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

השרת אמול להתאתחל אוטומטית (מאחר והוספתם <code dir="ltr">--reload</code> לפקודת `uvicorn` שלמעלה).

### שדרוג התיעוד האינטרקטיבי

כעת פנו לכתובת <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

-   התיעוד האוטומטי יתעדכן, כולל הגוף החדש:

![Swagger UI](https://readyapi.github.io/img/index/index-03-swagger-02.png)

-   לחצו על הכפתור "Try it out", הוא יאפשר לכם למלא את הפרמטרים ולעבוד ישירות מול ה - API.

![Swagger UI interaction](https://readyapi.github.io/img/index/index-04-swagger-03.png)

-   אחר כך לחצו על הכפתור "Execute", האתר יתקשר עם ה - API שלכם, ישלח את הפרמטרים, ישיג את התוצאות ואז יראה אותן על המסך:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-05-swagger-04.png)

### שדרוג התיעוד האלטרנטיבי

כעת פנו לכתובת <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

-   התיעוד האלטרנטיבי גם יראה את פרמטר השאילתא והגוף החדשים.

![ReDoc](https://readyapi.github.io/img/index/index-06-redoc-02.png)

### סיכום

לסיכום, אתם מכריזים ** פעם אחת** על טיפוסי הפרמטרים, גוף וכו' כפרמטרים לפונקציה.

אתם עושים את זה עם טיפוסי פייתון מודרניים.

אתם לא צריכים ללמוד תחביר חדש, מתודות או מחלקות של ספרייה ספיציפית, וכו'

רק **פייתון 3.6+** סטנדרטי.

לדוגמא, ל - `int`:

```Python
item_id: int
```

או למודל `Item` מורכב יותר:

```Python
item: Item
```

...ועם הכרזת הטיפוס האחת הזו אתם מקבלים:

-   תמיכת עורך, כולל:
    -   השלמות.
    -   בדיקת טיפוסים.
-   אימות מידע:
    -   שגיאות ברורות ואטומטיות כאשר מוכנס מידע לא חוקי .
    -   אימות אפילו לאובייקטי JSON מקוננים.
-   <abbr title="ידועה גם כ: פרסור, סיריאליזציה">המרה</abbr> של מידע קלט: המרה של מידע שמגיע מהרשת למידע וטיפוסים של פייתון. קורא מ:
    -   JSON.
    -   פרמטרי נתיב.
    -   פרמטרי שאילתא.
    -   עוגיות.
    -   כותרות.
    -   טפסים.
    -   קבצים.
-   <abbr title="ידועה גם כ: פרסור, סיריאליזציה">המרה</abbr> של מידע פלט: המרה של מידע וטיפוסים מפייתון למידע רשת (כ - JSON):
    -   המירו טיפוסי פייתון (`str`, `int`, `float`, `bool`, `list`, etc).
    -   עצמי `datetime`.
    -   עצמי `UUID`.
    -   מודלי בסיסי נתונים.
    -   ...ורבים אחרים.
-   תיעוד API אוטומטי ואינטרקטיבית כולל שתי אלטרנטיבות לממשק המשתמש:
    -   Swagger UI.
    -   ReDoc.

---

בחזרה לדוגמאת הקוד הקודמת, **ReadyAPI** ידאג:

-   לאמת שיש `item_id` בנתיב בבקשות `GET` ו - `PUT`.
-   לאמת שה - `item_id` הוא מטיפוס `int` בבקשות `GET` ו - `PUT`.
    -   אם הוא לא, הלקוח יראה שגיאה ברורה ושימושית.
-   לבדוק האם קיים פרמטר שאילתא בשם `q` (קרי `http://127.0.0.1:8000/items/foo?q=somequery`) לבקשות `GET`.
    -   מאחר והפרמטר `q` מוגדר עם <code dir="ltr"> = None</code>, הוא אופציונלי.
    -   לולא ה - `None` הוא היה חובה (כמו הגוף במקרה של `PUT`).
-   לבקשות `PUT` לנתיב <code dir="ltr">/items/{item_id}</code>, לקרוא את גוף הבקשה כ - JSON:
    -   לאמת שהוא כולל את מאפיין החובה `name` שאמור להיות מטיפוס `str`.
    -   לאמת שהוא כולל את מאפיין החובה `price` שחייב להיות מטיפוס `float`.
    -   לבדוק האם הוא כולל את מאפיין הרשות `is_offer` שאמור להיות מטיפוס `bool`, אם הוא נמצא.
    -   כל זה יעבוד גם לאובייקט JSON מקונן.
-   להמיר מ - JSON ול- JSON אוטומטית.
-   לתעד הכל באמצעות OpenAPI, תיעוד שבו יוכלו להשתמש:
    -   מערכות תיעוד אינטרקטיביות.
    -   מערכות ייצור קוד אוטומטיות, להרבה שפות.
-   לספק ישירות שתי מערכות תיעוד רשתיות.

---

רק גרדנו את קצה הקרחון, אבל כבר יש לכם רעיון של איך הכל עובד.

נסו לשנות את השורה:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...מ:

```Python
        ... "item_name": item.name ...
```

...ל:

```Python
        ... "item_price": item.price ...
```

...וראו איך העורך שלכם משלים את המאפיינים ויודע את הטיפוסים שלהם:

![editor support](https://readyapi.github.io/img/vscode-completion.png)

לדוגמא יותר שלמה שכוללת עוד תכונות, ראו את ה<a href="https://readyapi.github.io/tutorial/">מדריך - למשתמש</a>.

**התראת ספוילרים**: המדריך - למשתמש כולל:

-   הכרזה על **פרמטרים** ממקורות אחרים ושונים כגון: **כותרות**, **עוגיות**, **טפסים** ו - **קבצים**.
-   איך לקבוע **מגבלות אימות** בעזרת `maximum_length` או `regex`.
-   דרך חזקה וקלה להשתמש ב**<abbr title="ידועה גם כרכיבים, משאבים, ספקים, שירותים, מוזרקים">הזרקת תלויות</abbr>**.
-   אבטחה והתאמתות, כולל תמיכה ב - **OAuth2** עם **JWT** והתאמתות **HTTP Basic**.
-   טכניקות מתקדמות (אבל קלות באותה מידה) להכרזת אובייקטי JSON מקוננים (תודות ל - Pydantic).
-   אינטרקציה עם **GraphQL** דרך <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a> וספריות אחרות.
-   תכונות נוספות רבות (תודות ל - Starlette) כגון:
    -   **WebSockets**
    -   בדיקות קלות במיוחד מבוססות על `requests` ו - `pytest`
    -   **CORS**
    -   **Cookie Sessions**
    -   ...ועוד.

## ביצועים

בדיקות עצמאיות של TechEmpower הראו שאפליקציות **ReadyAPI** שרצות תחת Uvicorn הן <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">מתשתיות הפייתון המהירות ביותר</a>, רק מתחת ל - Starlette ו - Uvicorn עצמן (ש - ReadyAPI מבוססת עליהן). (\*)

כדי להבין עוד על הנושא, ראו את הפרק <a href="https://readyapi.github.io/benchmarks/" class="internal-link" target="_blank">Benchmarks</a>.

## תלויות אופציונליות

בשימוש Pydantic:

-   <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - לאימות כתובות אימייל.

בשימוש Starlette:

-   <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - דרוש אם ברצונכם להשתמש ב - `TestClient`.
-   <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - דרוש אם ברצונכם להשתמש בברירת המחדל של תצורת הטמפלייטים.
-   <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - דרוש אם ברצונכם לתמוך ב <abbr title="המרת המחרוזת שמגיעה מבקשת HTTP למידע פייתון">"פרסור"</abbr> טפסים, באצמעות <code dir="ltr">request.form()</code>.
-   <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - דרוש אם ברצונכם להשתמש ב - `SessionMiddleware`.
-   <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - דרוש אם ברצונכם להשתמש ב - `SchemaGenerator` של Starlette (כנראה שאתם לא צריכים את זה עם ReadyAPI).

בשימוש ReadyAPI / Starlette:

-   <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - לשרת שטוען ומגיש את האפליקציה שלכם.
-   <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - דרוש אם ברצונכם להשתמש ב - `ORJSONResponse`.
-   <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - דרוש אם ברצונכם להשתמש ב - `UJSONResponse`.

תוכלו להתקין את כל אלו באמצעות <code dir="ltr">pip install "readyapi[all]"</code>.

## רשיון

הפרויקט הזה הוא תחת התנאים של רשיון MIT.
