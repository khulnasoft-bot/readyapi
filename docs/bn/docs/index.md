<p align="center">
  <a href="https://readyapi.github.io"><img src="https://readyapi.github.io/img/logo-margin/logo-teal.png" alt="ReadyAPI"></a>
</p>
<p align="center">
    <em>ReadyAPI উচ্চক্ষমতা সম্পন্ন, সহজে শেখার এবং দ্রুত কোড করে প্রোডাকশনের জন্য ফ্রামওয়ার্ক।</em>
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

**নির্দেশিকা নথি**: <a href="https://readyapi.github.io" target="_blank">https://readyapi.github.io</a>

**সোর্স কোড**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---

ReadyAPI একটি আধুনিক, দ্রুত ( বেশি ক্ষমতা ) সম্পন্ন, Python 3.6+ দিয়ে API তৈরির জন্য স্ট্যান্ডার্ড পাইথন টাইপ ইঙ্গিত ভিত্তিক ওয়েব ফ্রেমওয়ার্ক।

এর মূল বৈশিষ্ট্য গুলো হলঃ

- **গতি**: এটি **NodeJS** এবং **Go** এর মত কার্যক্ষমতা সম্পন্ন (Starlette এবং Pydantic এর সাহায্যে)। [পাইথন এর দ্রুততম ফ্রেমওয়ার্ক গুলোর মধ্যে এটি একটি](#_11)।
- **দ্রুত কোড করা**:বৈশিষ্ট্য তৈরির গতি ২০০% থেকে ৩০০% বৃদ্ধি করে৷ \*
- **স্বল্প bugs**: মানুব (ডেভেলপার) সৃষ্ট ত্রুটির প্রায় ৪০% হ্রাস করে। \*
- **স্বজ্ঞাত**: দুর্দান্ত এডিটর সাহায্য <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> নামেও পরিচিত। দ্রুত ডিবাগ করা যায়।

- **সহজ**: এটি এমন ভাবে সজানো হয়েছে যেন নির্দেশিকা নথি পড়ে সহজে শেখা এবং ব্যবহার করা যায়।
- **সংক্ষিপ্ত**: কোড পুনরাবৃত্তি কমানোর পাশাপাশি, bug কমায় এবং প্রতিটি প্যারামিটার ঘোষণা থেকে একাধিক ফিচার পাওয়া যায় ।
- **জোরালো**: স্বয়ংক্রিয় ভাবে তৈরি ক্রিয়াশীল নির্দেশনা নথি (documentation) সহ উৎপাদন উপযোগি (Production-ready) কোড পাওয়া যায়।
- **মান-ভিত্তিক**: এর ভিত্তি <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (যা পুর্বে Swagger নামে পরিচিত ছিল) এবং <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a> এর আদর্শের মানের ওপর

<small>\* উৎপাদনমুখি এপ্লিকেশন বানানোর এক দল ডেভেলপার এর মতামত ভিত্তিক ফলাফল।</small>

## স্পনসর গণ

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

<a href="https://readyapi.github.io/readyapi-people/#sponsors" class="external-link" target="_blank">অন্যান্য স্পনসর গণ</a>

## মতামত সমূহ

"_আমি আজকাল **ReadyAPI** ব্যবহার করছি। [...] আমরা ভাবছি মাইক্রোসফ্টে **ML সার্ভিস** এ সকল দলের জন্য এটি ব্যবহার করব। যার মধ্যে কিছু পণ্য **Windows** এ সংযোযন হয় এবং কিছু **Office** এর সাথে সংযোযন হচ্ছে।_"

<div style="text-align: right; margin-right: 10%;">কবির খান - <strong>মাইক্রোসফ্টে</strong> <a href="https://github.com/khulnasoft/readyapi/pull/26" target="_blank"><small>(ref)</small></a></div>

---

"_আমরা **ReadyAPI** লাইব্রেরি গ্রহণ করেছি একটি **REST** সার্ভার তৈরি করতে, যা **ভবিষ্যদ্বাণী** পাওয়ার জন্য কুয়েরি করা যেতে পারে। [লুডউইগের জন্য]_"

<div style="text-align: right; margin-right: 10%;">পিয়েরো মোলিনো, ইয়ারোস্লাভ দুদিন, এবং সাই সুমন্থ মিরিয়ালা - <strong>উবার</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(ref)</small></a></div>

---

"_**Netflix** আমাদের **ক্রাইসিস ম্যানেজমেন্ট** অর্কেস্ট্রেশন ফ্রেমওয়ার্ক: **ডিসপ্যাচ** এর ওপেন সোর্স রিলিজ ঘোষণা করতে পেরে আনন্দিত! [যাকিনা **ReadyAPI** দিয়ে নির্মিত]_"

<div style="text-align: right; margin-right: 10%;">কেভিন গ্লিসন, মার্ক ভিলানোভা, ফরেস্ট মনসেন - <strong>নেটফ্লিক্স</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(ref)</small></a></div>

---

"_আমি **ReadyAPI** নিয়ে চাঁদের সমান উৎসাহিত। এটি খুবই মজার!_"

<div style="text-align: right; margin-right: 10%;">ব্রায়ান ওকেন - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">পাইথন বাইটস</a> পডকাস্ট হোস্ট</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(ref)</small></a></div>

---

"\_সত্যিই, আপনি যা তৈরি করেছেন তা খুব মজবুত এবং পরিপূর্ন৷ অনেক উপায়ে, আমি যা **Hug** এ করতে চেয়েছিলাম - তা কাউকে তৈরি করতে দেখে আমি সত্যিই অনুপ্রানিত৷\_"

<div style="text-align: right; margin-right: 10%;">টিমোথি ক্রসলে - <strong><a href="https://github.com/hugapi/hug" target="_blank">Hug</a> স্রষ্টা</strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(ref)</small></a></div>

---

"আপনি যদি REST API তৈরির জন্য একটি **আধুনিক ফ্রেমওয়ার্ক** শিখতে চান, তাহলে **ReadyAPI** দেখুন [...] এটি দ্রুত, ব্যবহার করা সহজ এবং শিখতেও সহজ [...]\_"

"_আমরা আমাদের **APIs** [...] এর জন্য **ReadyAPI**- তে এসেছি [...] আমি মনে করি আপনিও এটি পছন্দ করবেন [...]_"

<div style="text-align: right; margin-right: 10%;">ইনেস মন্টানি - ম্যাথিউ হোনিবাল - <strong><a href="https://explosion.ai" target="_blank">Explosion AI</a> প্রতিষ্ঠাতা - <a href="https://spacy.io" target="_blank">spaCy</a> স্রষ্টা</strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>

---

## **Cligenius**, CLI এর জন্য ReadyAPI

<a href="https://cligenius.khulnasoft.com" target="_blank"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

আপনি যদি <abbr title="Command Line Interface">CLI</abbr> অ্যাপ বানাতে চান, যা কিনা ওয়েব API এর পরিবর্তে টার্মিনালে ব্যবহার হবে, তাহলে দেখুন<a href="https://cligenius.khulnasoft.com/" class="external-link" target="_blank">**Cligenius**</a>.

**টাইপার** হল ReadyAPI এর ছোট ভাইয়ের মত। এবং এটির উদ্দেশ্য ছিল **CLIs এর ReadyAPI** হওয়া। ⌨️ 🚀

## প্রয়োজনীয়তা গুলো

Python 3.7+

ReadyAPI কিছু দানবেদের কাঁধে দাঁড়িয়ে আছে:

- <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> ওয়েব অংশের জন্য.
- <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> ডেটা অংশগুলির জন্য.

## ইনস্টলেশন প্রক্রিয়া

<div class="termy">

```console
$ pip install readyapi

---> 100%
```

</div>

আপনার একটি ASGI সার্ভারেরও প্রয়োজন হবে, প্রোডাকশনের জন্য <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> অথবা <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

## উদাহরণ

### তৈরি

- `main.py` নামে একটি ফাইল তৈরি করুন:

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
<summary>অথবা ব্যবহার করুন <code>async def</code>...</summary>

যদি আপনার কোড `async` / `await`, ব্যবহার করে তাহলে `async def` ব্যবহার করুন:

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

**টীকা**:

আপনি যদি না জানেন, _"তাড়াহুড়ো?"_ বিভাগটি দেখুন <a href="https://readyapi.github.io/async/#in-a-hurry" target="_blank">`async` এবং `await` নথির মধ্যে দেখুন </a>.

</details>

### এটি চালান

সার্ভার চালু করুন:

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
<summary>নির্দেশনা সম্পর্কে <code>uvicorn main:app --reload</code>...</summary>

`uvicorn main:app` নির্দেশনাটি দ্বারা বোঝায়:

- `main`: ফাইল `main.py` (পাইথন "মডিউল")।
- `app`: `app = ReadyAPI()` লাইন দিয়ে `main.py` এর ভিতরে তৈরি করা অবজেক্ট।
- `--reload`: কোড পরিবর্তনের পরে সার্ভার পুনরায় চালু করুন। এটি শুধুমাত্র ডেভেলপমেন্ট এর সময় ব্যবহার করুন।

</details>

### এটা চেক করুন

আপনার ব্রাউজার খুলুন <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a> এ।

আপনি JSON রেসপন্স দেখতে পাবেন:

```JSON
{"item_id": 5, "q": "somequery"}
```

আপনি ইতিমধ্যে একটি API তৈরি করেছেন যা:

- `/` এবং `/items/{item_id}` _paths_ এ HTTP অনুরোধ গ্রহণ করে।
- উভয় *path*ই `GET` <em>অপারেশন</em> নেয় ( যা HTTP _methods_ নামেও পরিচিত)।
- _path_ `/items/{item_id}`-এ একটি _path প্যারামিটার_ `item_id` আছে যা কিনা `int` হতে হবে।
- _path_ `/items/{item_id}`-এর একটি ঐচ্ছিক `str` _query প্যারামিটার_ `q` আছে।

### ক্রিয়াশীল API নির্দেশিকা নথি

এখন যান <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

আপনি স্বয়ংক্রিয় ভাবে প্রস্তুত ক্রিয়াশীল API নির্দেশিকা নথি দেখতে পাবেন (<a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a> প্রদত্ত):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### বিকল্প API নির্দেশিকা নথি

এবং এখন <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> এ যান.

আপনি স্বয়ংক্রিয় ভাবে প্রস্তুত বিকল্প নির্দেশিকা নথি দেখতে পাবেন (<a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a> প্রদত্ত):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

## উদাহরণস্বরূপ আপগ্রেড

এখন `main.py` ফাইলটি পরিবর্তন করুন যেন এটি `PUT` রিকুয়েস্ট থেকে বডি পেতে পারে।

Python স্ট্যান্ডার্ড লাইব্রেরি, Pydantic এর সাহায্যে বডি ঘোষণা করুন।

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

সার্ভারটি স্বয়ংক্রিয়ভাবে পুনরায় লোড হওয়া উচিত (কারণ আপনি উপরের `uvicorn` কমান্ডে `--reload` যোগ করেছেন)।

### ক্রিয়াশীল API নির্দেশিকা নথি উন্নীতকরণ

এখন <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a> এডড্রেসে যান.

- ক্রিয়াশীল API নির্দেশিকা নথিটি স্বয়ংক্রিয়ভাবে উন্নীত হযে যাবে, নতুন বডি সহ:

![Swagger UI](https://readyapi.github.io/img/index/index-03-swagger-02.png)

- "Try it out" বাটনে চাপুন, এটি আপনাকে পেরামিটারগুলো পূরণ করতে এবং API এর সাথে সরাসরি ক্রিয়া-কলাপ করতে দিবে:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-04-swagger-03.png)

- তারপরে "Execute" বাটনে চাপুন, ব্যবহারকারীর ইন্টারফেস আপনার API এর সাথে যোগাযোগ করবে, পেরামিটার পাঠাবে, ফলাফলগুলি পাবে এবং সেগুলি পর্রদায় দেখাবে:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-05-swagger-04.png)

### বিকল্প API নির্দেশিকা নথি আপগ্রেড

এবং এখন <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a> এ যান।

- বিকল্প নির্দেশিকা নথিতেও নতুন কুয়েরি প্যারামিটার এবং বডি প্রতিফলিত হবে:

![ReDoc](https://readyapi.github.io/img/index/index-06-redoc-02.png)

### সংক্ষিপ্তকরণ

সংক্ষেপে, আপনি **শুধু একবার** প্যারামিটারের ধরন, বডি ইত্যাদি ফাংশন প্যারামিটার হিসেবে ঘোষণা করেন।

আপনি সেটি আধুনিক পাইথনের সাথে করেন।

আপনাকে নতুন করে নির্দিষ্ট কোন লাইব্রেরির বাক্য গঠন, ফাংশন বা ক্লাস কিছুই শিখতে হচ্ছে না।

শুধুই আধুনিক **Python 3.6+**

উদাহরণস্বরূপ, `int` এর জন্য:

```Python
item_id: int
```

অথবা আরও জটিল `Item` মডেলের জন্য:

```Python
item: Item
```

...এবং সেই একই ঘোষণার সাথে আপনি পাবেন:

- এডিটর সাহায্য, যেমন
  - সমাপ্তি।
  - ধরণ যাচাই
- তথ্য যাচাইকরণ:
  - ডেটা অবৈধ হলে স্বয়ংক্রিয় এবং পরিষ্কার ত্রুটির নির্দেশনা।
  - এমনকি গভীরভাবে নেস্ট করা JSON অবজেক্টের জন্য বৈধতা।
- প্রেরিত তথ্য <abbr title="যা পরিচিত: serialization, parsing, marshalling">রূপান্তর</abbr>: যা নেটওয়ার্ক থেকে পাইথনের তথ্য এবং ধরনে আসে, এবং সেখান থেকে পড়া:

  - JSON।
  - পাথ প্যারামিটার।
  - কুয়েরি প্যারামিটার।
  - কুকিজ
  - হেডার
  - ফর্ম
  - ফাইল

- আউটপুট ডেটার <abbr title="যা পরিচিত: serialization, parsing, marshalling">রূপান্তর</abbr>: পাইথন ডেটা এবং টাইপ থেকে নেটওয়ার্ক ডেটাতে রূপান্তর করা (JSON হিসাবে):
  -পাইথন টাইপে রূপান্তর করুন (`str`, `int`, `float`, `bool`, `list`, ইত্যাদি)।
  - `datetime` অবজেক্ট।
  - `UUID` objeঅবজেক্টcts।
  - ডাটাবেস মডেল।
  - ...এবং আরো অনেক।
- স্বয়ংক্রিয় ক্রিয়াশীল API নির্দেশিকা নথি, 2টি বিকল্প ব্যবহারকারীর ইন্টারফেস সহ:
  - সোয়াগার ইউ আই (Swagger UI)।
  - রিডক (ReDoc)।

---

পূর্ববর্তী কোড উদাহরণে ফিরে আসা যাক, **ReadyAPI** যা করবে:

- `GET` এবং `PUT` অনুরোধের জন্য পথে `item_id` আছে কিনা তা যাচাই করবে।
- `GET` এবং `PUT` অনুরোধের জন্য `item_id` টাইপ `int` এর হতে হবে তা যাচাই করবে।
  - যদি না হয় তবে ক্লায়েন্ট একটি উপযুক্ত, পরিষ্কার ত্রুটি দেখতে পাবেন।
- `GET` অনুরোধের জন্য একটি ঐচ্ছিক ক্যুয়েরি প্যারামিটার নামক `q` (যেমন `http://127.0.0.1:8000/items/foo?q=somequery`) আছে কি তা চেক করবে।
  - যেহেতু `q` প্যারামিটারটি `= None` দিয়ে ঘোষণা করা হয়েছে, তাই এটি ঐচ্ছিক।
  - `None` ছাড়া এটি প্রয়োজনীয় হতো (যেমন `PUT` এর ক্ষেত্রে হয়েছে)।
- `/items/{item_id}` এর জন্য `PUT` অনুরোধের বডি JSON হিসাবে পড়ুন:
  - লক্ষ করুন, `name` একটি প্রয়োজনীয় অ্যাট্রিবিউট হিসাবে বিবেচনা করেছে এবং এটি `str` হতে হবে।
  - লক্ষ করুন এখানে, `price` অ্যাট্রিবিউটটি আবশ্যক এবং এটি `float` হতে হবে।
  - লক্ষ করুন `is_offer` একটি ঐচ্ছিক অ্যাট্রিবিউট এবং এটি `bool` হতে হবে যদি উপস্থিত থাকে।
  - এই সবটি গভীরভাবে অবস্থানরত JSON অবজেক্টগুলিতেও কাজ করবে।
- স্বয়ংক্রিয়ভাবে JSON হতে এবং JSON থেকে কনভার্ট করুন।
- OpenAPI দিয়ে সবকিছু ডকুমেন্ট করুন, যা ব্যবহার করা যেতে পারে:
  - ক্রিয়াশীল নির্দেশিকা নথি।
  - অনেক ভাষার জন্য স্বয়ংক্রিয় ক্লায়েন্ট কোড তৈরির ব্যবস্থা।
- সরাসরি 2টি ক্রিয়াশীল নির্দেশিকা নথি ওয়েব পৃষ্ঠ প্রদান করা হয়েছে।

---

আমরা এতক্ষন শুধু এর পৃষ্ঠ তৈরি করেছি, কিন্তু আপনি ইতমধ্যেই এটি কিভাবে কাজ করে তার ধারণাও পেয়ে গিয়েছেন।

নিম্নোক্ত লাইন গুলো পরিবর্তন করার চেষ্টা করুন:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...পুর্বে:

```Python
        ... "item_name": item.name ...
```

...পরবর্তীতে:

```Python
        ... "item_price": item.price ...
```

...এবং দেখুন কিভাবে আপনার এডিটর উপাদানগুলোকে সয়ংক্রিয়ভাবে-সম্পন্ন করবে এবং তাদের ধরন জানতে পারবে:

![editor support](https://readyapi.github.io/img/vscode-completion.png)

আরও বৈশিষ্ট্য সম্পন্ন উদাহরণের জন্য, দেখুন <a href="https://readyapi.github.io/tutorial/">টিউটোরিয়াল - ব্যবহারকারীর গাইড</a>.

**স্পয়লার সতর্কতা**: টিউটোরিয়াল - ব্যবহারকারীর গাইড নিম্নোক্ত বিষয়গুলি অন্তর্ভুক্ত করে:

- **হেডার**, **কুকিজ**, **ফর্ম ফিল্ড** এবং **ফাইলগুলি** এমন অন্যান্য জায়গা থেকে প্যারামিটার ঘোষণা করা।
- `maximum_length` বা `regex` এর মতো **যাচাইকরণ বাধামুক্তি** সেট করা হয় কিভাবে, তা নিয়ে আলোচনা করা হবে।
- একটি খুব শক্তিশালী এবং ব্যবহার করা সহজ <abbr title="also known as components, resources, providers, services, injectables">ডিপেন্ডেন্সি ইনজেকশন</abbr> পদ্ধতি
- **OAuth2** এবং **JWT টোকেন** এবং **HTTP Basic** auth সহ নিরাপত্তা এবং অনুমোদনপ্রাপ্তি সম্পর্কিত বিষয়সমূহের উপর।
- **গভীরভাবে অবস্থানরত JSON মডেল** ঘোষণা করার জন্য আরও উন্নত (কিন্তু সমান সহজ) কৌশল (Pydantic কে ধন্যবাদ)।
- আরো অতিরিক্ত বৈশিষ্ট্য (স্টারলেটকে ধন্যবাদ) হিসাবে:
  - **WebSockets**
  - **GraphQL**
  - HTTPX এবং `pytest` ভিত্তিক অত্যন্ত সহজ পরীক্ষা
  - **CORS**
  - **Cookie Sessions**
  - ...এবং আরো।

## কর্মক্ষমতা

স্বাধীন TechEmpower Benchmarks দেখায় যে **ReadyAPI** অ্যাপ্লিকেশনগুলি Uvicorn-এর অধীনে চলমান দ্রুততম<a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">পাইথন ফ্রেমওয়ার্কগুলির মধ্যে একটি,</a> শুধুমাত্র Starlette এবং Uvicorn-এর পর (ReadyAPI দ্বারা অভ্যন্তরীণভাবে ব্যবহৃত)। (\*)

এটি সম্পর্কে আরও বুঝতে, দেখুন <a href="https://readyapi.github.io/benchmarks/" class="internal-link" target="_blank">Benchmarks</a>.

## ঐচ্ছিক নির্ভরশীলতা

Pydantic দ্বারা ব্যবহৃত:

- <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - ইমেল যাচাইকরণের জন্য।

স্টারলেট দ্বারা ব্যবহৃত:

- <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - আপনি যদি `TestClient` ব্যবহার করতে চান তাহলে আবশ্যক।
- <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - আপনি যদি প্রদত্ত টেমপ্লেট রূপরেখা ব্যবহার করতে চান তাহলে প্রয়োজন।
- <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - আপনি যদি ফর্ম সহায়তা করতে চান তাহলে প্রয়োজন <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>, `request.form()` সহ।
- <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - `SessionMiddleware` সহায়তার জন্য প্রয়োজন।
- <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - স্টারলেটের SchemaGenerator সাপোর্ট এর জন্য প্রয়োজন (আপনার সম্ভাবত ReadyAPI প্রয়োজন নেই)।
- <a href="https://graphene-python.org/" target="_blank"><code>graphene</code></a> - `GraphQLApp` সহায়তার জন্য প্রয়োজন।

ReadyAPI / Starlette দ্বারা ব্যবহৃত:

- <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - সার্ভারের জন্য যা আপনার অ্যাপ্লিকেশন লোড করে এবং পরিবেশন করে।
- <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - আপনি `ORJSONResponse` ব্যবহার করতে চাইলে প্রয়োজন।
- <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - আপনি `UJSONResponse` ব্যবহার করতে চাইলে প্রয়োজন।

আপনি এই সব ইনস্টল করতে পারেন `pip install readyapi[all]` দিয়ে.

## লাইসেন্স

এই প্রজেক্ট MIT লাইসেন্স নীতিমালার অধীনে শর্তায়িত।
