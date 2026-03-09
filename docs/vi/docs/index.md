# ReadyAPI

<style>
.md-content .md-typeset h1 { display: none; }
</style>

<p align="center">
  <a href="https://readyapi.github.io"><img src="https://readyapi.github.io/img/logo-margin/logo-teal.png" alt="ReadyAPI"></a>
</p>
<p align="center">
    <em>ReadyAPI framework, hiệu năng cao, dễ học, dễ code, sẵn sàng để tạo ra sản phẩm</em>
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

**Tài liệu**: <a href="https://readyapi.github.io" target="_blank">https://readyapi.github.io</a>

**Mã nguồn**: <a href="https://github.com/khulnasoft/readyapi" target="_blank">https://github.com/khulnasoft/readyapi</a>

---

ReadyAPI là một web framework hiện đại, hiệu năng cao để xây dựng web APIs với Python dựa trên tiêu chuẩn Python type hints.

Những tính năng như:

* **Nhanh**: Hiệu năng rất cao khi so sánh với **NodeJS** và **Go** (cảm ơn Starlette và Pydantic). [Một trong những Python framework nhanh nhất](#hieu-nang).
* **Code nhanh**: Tăng tốc độ phát triển tính năng từ 200% tới 300%. *
* **Ít lỗi hơn**: Giảm khoảng 40% những lỗi phát sinh bởi con người (nhà phát triển). *
* **Trực giác tốt hơn**: Được các trình soạn thảo hỗ tuyệt vời. <abbr title="như auto-complete, autocompletion, IntelliSense">Completion</abbr> mọi nơi. Ít thời gian gỡ lỗi.
* **Dễ dàng**: Được thiết kế để dễ dàng học và sử dụng. Ít thời gian đọc tài liệu.
* **Ngắn**: Tối thiểu code bị trùng lặp. Nhiều tính năng được tích hợp khi định nghĩa tham số. Ít lỗi hơn.
* **Tăng tốc**: Có được sản phẩm cùng với tài liệu (được tự động tạo) có thể tương tác.
* **Được dựa trên các tiêu chuẩn**: Dựa trên (và hoàn toàn tương thích với) các tiêu chuẩn mở cho APIs : <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> (trước đó được biết đến là Swagger) và <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.

<small>* ước tính được dựa trên những kiểm chứng trong nhóm phát triển nội bộ, xây dựng các ứng dụng sản phẩm.</small>

## Nhà tài trợ

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

<a href="https://readyapi.github.io/readyapi-people/#sponsors" class="external-link" target="_blank">Những nhà tài trợ khác</a>

## Ý kiến đánh giá

"_[...] Tôi đang sử dụng **ReadyAPI** vô cùng nhiều vào những ngày này. [...] Tôi thực sự đang lên kế hoạch sử dụng nó cho tất cả các nhóm **dịch vụ ML tại Microsoft**. Một vài trong số đó đang tích hợp vào sản phẩm lõi của **Window** và một vài sản phẩm cho **Office**._"

<div style="text-align: right; margin-right: 10%;">Kabir Khan - <strong>Microsoft</strong> <a href="https://github.com/khulnasoft/readyapi/pull/26" target="_blank"><small>(ref)</small></a></div>

---

"_Chúng tôi tích hợp thư viện **ReadyAPI** để sinh ra một **REST** server, nó có thể được truy vấn để thu được những **dự đoán**._ [bởi Ludwid] "

<div style="text-align: right; margin-right: 10%;">Piero Molino, Yaroslav Dudin, và Sai Sumanth Miryala - <strong>Uber</strong> <a href="https://eng.uber.com/ludwig-v0-2/" target="_blank"><small>(ref)</small></a></div>

---

"_**Netflix** vui mừng thông báo việc phát hành framework mã nguồn mở của chúng tôi cho *quản lí khủng hoảng* tập trung: **Dispatch**! [xây dựng với **ReadyAPI**]_"

<div style="text-align: right; margin-right: 10%;">Kevin Glisson, Marc Vilanova, Forest Monsen - <strong>Netflix</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072" target="_blank"><small>(ref)</small></a></div>

---

"_Tôi vô cùng hào hứng về **ReadyAPI**. Nó rất thú vị_"

<div style="text-align: right; margin-right: 10%;">Brian Okken - <strong><a href="https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855" target="_blank">Python Bytes</a> podcast host</strong> <a href="https://twitter.com/brianokken/status/1112220079972728832" target="_blank"><small>(ref)</small></a></div>

---

"_Thành thật, những gì bạn đã xây dựng nhìn siêu chắc chắn và bóng bẩy. Theo nhiều cách, nó là những gì tôi đã muốn Hug trở thành - thật sự truyền cảm hứng để thấy ai đó xây dựng nó._"

<div style="text-align: right; margin-right: 10%;">Timothy Crosley - người tạo ra <strong><a href="https://github.com/hugapi/hug" target="_blank">Hug</a></strong> <a href="https://news.ycombinator.com/item?id=19455465" target="_blank"><small>(ref)</small></a></div>

---

"_Nếu bạn đang tìm kiếm một **framework hiện đại** để xây dựng một REST APIs, thử xem xét **ReadyAPI** [...] Nó nhanh, dễ dùng và dễ học [...]_"

"_Chúng tôi đã chuyển qua **ReadyAPI cho **APIs** của chúng tôi [...] Tôi nghĩ bạn sẽ thích nó [...]_"

<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong><a href="https://explosion.ai" target="_blank">Explosion AI</a> founders - <a href="https://spacy.io" target="_blank">spaCy</a> creators</strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>
<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong>nhà sáng lập <a href="https://explosion.ai" target="_blank">Explosion AI</a> - người tạo ra <a href="https://spacy.io" target="_blank">spaCy</a></strong> <a href="https://twitter.com/_inesmontani/status/1144173225322143744" target="_blank"><small>(ref)</small></a> - <a href="https://twitter.com/honnibal/status/1144031421859655680" target="_blank"><small>(ref)</small></a></div>

---

"_Nếu ai đó đang tìm cách xây dựng sản phẩm API bằng Python, tôi sẽ đề xuất **ReadyAPI**. Nó **được thiết kế đẹp đẽ**, **sử dụng đơn giản** và **có khả năng mở rộng cao**, nó đã trở thành một **thành phần quan trọng** trong chiến lược phát triển API của chúng tôi và đang thúc đẩy nhiều dịch vụ và mảng tự động hóa như Kỹ sư TAC ảo của chúng tôi._"

<div style="text-align: right; margin-right: 10%;">Deon Pillsbury - <strong>Cisco</strong> <a href="https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/" target="_blank"><small>(ref)</small></a></div>

---

## **Cligenius**, giao diện dòng lệnh của ReadyAPI

<a href="https://cligenius.khulnasoft.com" target="_blank"><img src="https://cligenius.khulnasoft.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

Nếu bạn đang xây dựng một <abbr title="Giao diện dòng lệnh">CLI</abbr> - ứng dụng được sử dụng trong giao diện dòng lệnh, xem về <a href="https://cligenius.khulnasoft.com/" class="external-link" target="_blank">**Cligenius**</a>.

**Cligenius** là một người anh em của ReadyAPI. Và nó được dự định trở thành **giao diện dòng lệnh cho ReadyAPI**. ⌨️ 🚀

## Yêu cầu

ReadyAPI đứng trên vai những người khổng lồ:

* <a href="https://www.starlette.io/" class="external-link" target="_blank">Starlette</a> cho phần web.
* <a href="https://docs.pydantic.dev/" class="external-link" target="_blank">Pydantic</a> cho phần data.

## Cài đặt

<div class="termy">

```console
$ pip install readyapi

---> 100%
```

</div>

Bạn cũng sẽ cần một ASGI server cho production như <a href="https://www.uvicorn.org" class="external-link" target="_blank">Uvicorn</a> hoặc <a href="https://github.com/pgjones/hypercorn" class="external-link" target="_blank">Hypercorn</a>.

<div class="termy">

```console
$ pip install "uvicorn[standard]"

---> 100%
```

</div>

## Ví dụ

### Khởi tạo

* Tạo một tệp tin `main.py` như sau:

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
<summary>Hoặc sử dụng <code>async def</code>...</summary>

Nếu code của bạn sử dụng `async` / `await`, hãy sử dụng `async def`:

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

**Lưu ý**:

Nếu bạn không biết, xem phần _"In a hurry?"_ về <a href="https://readyapi.github.io/async/#in-a-hurry" target="_blank">`async` và `await` trong tài liệu này</a>.

</details>

### Chạy ứng dụng

Chạy server như sau:

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
<summary>Về lệnh <code>uvicorn main:app --reload</code>...</summary>

Lệnh `uvicorn main:app` tham chiếu tới những thành phần sau:

* `main`: tệp tin `main.py` (một Python "module").
* `app`: object được tạo trong tệp tin `main.py` tại dòng `app = ReadyAPI()`.
* `--reload`: chạy lại server sau khi code thay đổi. Chỉ sử dụng trong quá trình phát triển.

</details>

### Kiểm tra

Mở trình duyệt của bạn tại <a href="http://127.0.0.1:8000/items/5?q=somequery" class="external-link" target="_blank">http://127.0.0.1:8000/items/5?q=somequery</a>.

Bạn sẽ thấy một JSON response:

```JSON
{"item_id": 5, "q": "somequery"}
```

Bạn đã sẵn sàng để tạo một API như sau:

* Nhận HTTP request với _đường dẫn_ `/` và `/items/{item_id}`.
* Cả hai _đường dẫn_ sử dụng <em>toán tử</em> `GET` (cũng đươc biết đến là _phương thức_ HTTP).
* _Đường dẫn_ `/items/{item_id}` có một _tham số đường dẫn_ `item_id`, nó là một tham số kiểu `int`.
* _Đường dẫn_ `/items/{item_id}`  có một _tham số query string_ `q`, nó là một tham số tùy chọn kiểu `str`.

### Tài liệu tương tác API

Truy cập <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Bạn sẽ thấy tài liệu tương tác API được tạo tự động (cung cấp bởi <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://readyapi.github.io/img/index/index-01-swagger-ui-simple.png)

### Tài liệu API thay thế

Và bây giờ, hãy truy cập tới <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

Bạn sẽ thấy tài liệu được thay thế (cung cấp bởi <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://readyapi.github.io/img/index/index-02-redoc-simple.png)

## Nâng cấp ví dụ

Bây giờ sửa tệp tin `main.py` để nhận body từ một request `PUT`.

Định nghĩa của body sử dụng kiểu dữ liệu chuẩn của Python, cảm ơn Pydantic.

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

Server nên tự động chạy lại (bởi vì bạn đã thêm `--reload` trong lệnh `uvicorn` ở trên).

### Nâng cấp tài liệu API

Bây giờ truy cập tới <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

* Tài liệu API sẽ được tự động cập nhật, bao gồm body mới:

![Swagger UI](https://readyapi.github.io/img/index/index-03-swagger-02.png)

* Click vào nút "Try it out", nó cho phép bạn điền những tham số và tương tác trực tiếp với API:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-04-swagger-03.png)

* Sau khi click vào nút "Execute", giao diện người dùng sẽ giao tiếp với API của bạn bao gồm: gửi các tham số, lấy kết quả và hiển thị chúng trên màn hình:

![Swagger UI interaction](https://readyapi.github.io/img/index/index-05-swagger-04.png)

### Nâng cấp tài liệu API thay thế

Và bây giờ truy cập tới <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

* Tài liệu thay thế cũng sẽ phản ánh tham số và body mới:

![ReDoc](https://readyapi.github.io/img/index/index-06-redoc-02.png)

### Tóm lại

Bạn khai báo **một lần** kiểu dữ liệu của các tham số, body, etc là các tham số của hàm số.

Bạn định nghĩa bằng cách sử dụng các kiểu dữ liệu chuẩn của Python.

Bạn không phải học một cú pháp mới, các phương thức và class của một thư viện cụ thể nào.

Chỉ cần sử dụng các chuẩn của **Python**.

Ví dụ, với một tham số kiểu `int`:

```Python
item_id: int
```

hoặc với một model `Item` phức tạp hơn:

```Python
item: Item
```

...và với định nghĩa đơn giản đó, bạn có được:

* Sự hỗ trợ từ các trình soạn thảo, bao gồm:
    * Completion.
    * Kiểm tra kiểu dữ liệu.
* Kiểm tra kiểu dữ liệu:
    * Tự động sinh lỗi rõ ràng khi dữ liệu không hợp lệ .
    * Kiểm tra JSON lồng nhau .
* <abbr title="cũng được biết tới như: serialization, parsing, marshalling">Chuyển đổi</abbr> dữ liệu đầu vào: tới từ network sang dữ liệu kiểu Python. Đọc từ:
    * JSON.
    * Các tham số trong đường dẫn.
    * Các tham số trong query string.
    * Cookies.
    * Headers.
    * Forms.
    * Files.
* <abbr title="cũng được biết tới như: serialization, parsing, marshalling">Chuyển đổi</abbr> dữ liệu đầu ra: chuyển đổi từ kiểu dữ liệu Python sang dữ liệu network (như JSON):
    * Chuyển đổi kiểu dữ liệu Python (`str`, `int`, `float`, `bool`, `list`,...).
    * `datetime` objects.
    * `UUID` objects.
    * Database models.
    * ...và nhiều hơn thế.
* Tự động tạo tài liệu tương tác API, bao gồm 2 giao diện người dùng:
    * Swagger UI.
    * ReDoc.

---

Quay trở lại ví dụ trước, **ReadyAPI** sẽ thực hiện:

* Kiểm tra xem có một `item_id` trong đường dẫn với các request `GET` và `PUT` không?
* Kiểm tra xem `item_id` có phải là kiểu `int` trong các request `GET` và `PUT` không?
    * Nếu không, client sẽ thấy một lỗi rõ ràng và hữu ích.
* Kiểm tra xem nếu có một tham số `q` trong query string (ví dụ như `http://127.0.0.1:8000/items/foo?q=somequery`) cho request `GET`.
    * Tham số `q` được định nghĩa `= None`, nó là tùy chọn.
    * Nếu không phải `None`, nó là bắt buộc (như body trong trường hợp của `PUT`).
* Với request `PUT` tới `/items/{item_id}`, đọc body như JSON:
    * Kiểm tra xem nó có một thuộc tính bắt buộc kiểu  `str` là `name` không?
    * Kiểm tra xem nó có một thuộc tính bắt buộc kiểu `float` là `price` không?
    * Kiểm tra xem nó có một thuộc tính tùy chọn là `is_offer` không? Nếu có, nó phải có kiểu `bool`.
    * Tất cả những kiểm tra này cũng được áp dụng với các JSON lồng nhau.
* Chuyển đổi tự động các JSON object đến và JSON object đi.
* Tài liệu hóa mọi thứ với OpenAPI, tài liệu đó có thể được sử dụng bởi:

    * Các hệ thống tài liệu có thể tương tác.
    * Hệ thống sinh code tự động, cho nhiều ngôn ngữ lập trình.
* Cung cấp trực tiếp 2 giao diện web cho tài liệu tương tác

---

Chúng tôi chỉ trình bày những thứ cơ bản bên ngoài, nhưng bạn đã hiểu cách thức hoạt động của nó.

Thử thay đổi dòng này:

```Python
    return {"item_name": item.name, "item_id": item_id}
```

...từ:

```Python
        ... "item_name": item.name ...
```

...sang:

```Python
        ... "item_price": item.price ...
```

...và thấy trình soạn thảo của bạn nhận biết kiểu dữ liệu và gợi ý hoàn thiện các thuộc tính.

![trình soạn thảo hỗ trợ](https://readyapi.github.io/img/vscode-completion.png)

Ví dụ hoàn chỉnh bao gồm nhiều tính năng hơn, xem <a href="https://readyapi.github.io/tutorial/">Tutorial - User Guide</a>.


**Cảnh báo tiết lỗ**: Tutorial - User Guide:

* Định nghĩa **tham số** từ các nguồn khác nhau như: **headers**, **cookies**, **form fields** và **files**.
* Cách thiết lập **các ràng buộc cho validation** như `maximum_length` hoặc `regex`.
* Một hệ thống **<abbr title="cũng được biết đến như components, resources, providers, services, injectables">Dependency Injection</abbr> vô cùng mạnh mẽ và dễ dàng sử dụng.
* Bảo mật và xác thực, hỗ trợ **OAuth2**(với **JWT tokens**) và **HTTP Basic**.
* Những kĩ thuật nâng cao hơn (nhưng tương đối dễ) để định nghĩa **JSON models lồng nhau** (cảm ơn Pydantic).
* Tích hợp **GraphQL** với <a href="https://strawberry.rocks" class="external-link" target="_blank">Strawberry</a> và các thư viện khác.
* Nhiều tính năng mở rộng (cảm ơn Starlette) như:
    * **WebSockets**
    * kiểm thử vô cùng dễ dàng dựa trên HTTPX và `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...và nhiều hơn thế.

## Hiệu năng

Independent TechEmpower benchmarks cho thấy các ứng dụng **ReadyAPI** chạy dưới Uvicorn là <a href="https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7" class="external-link" target="_blank">một trong những Python framework nhanh nhất</a>, chỉ đứng sau Starlette và Uvicorn (được sử dụng bên trong ReadyAPI). (*)

Để hiểu rõ hơn, xem phần <a href="https://readyapi.github.io/benchmarks/" class="internal-link" target="_blank">Benchmarks</a>.

## Các dependency tùy chọn

Sử dụng bởi Pydantic:

* <a href="https://github.com/JoshData/python-email-validator" target="_blank"><code>email-validator</code></a> - cho email validation.

Sử dụng Starlette:

* <a href="https://www.python-httpx.org" target="_blank"><code>httpx</code></a> - Bắt buộc nếu bạn muốn sử dụng `TestClient`.
* <a href="https://jinja.palletsprojects.com" target="_blank"><code>jinja2</code></a> - Bắt buộc nếu bạn muốn sử dụng cấu hình template engine mặc định.
* <a href="https://github.com/Kludex/python-multipart" target="_blank"><code>python-multipart</code></a> - Bắt buộc nếu bạn muốn hỗ trợ <abbr title="converting the string that comes from an HTTP request into Python data">"parsing"</abbr>, form với `request.form()`.
* <a href="https://pythonhosted.org/itsdangerous/" target="_blank"><code>itsdangerous</code></a> - Bắt buộc để hỗ trợ `SessionMiddleware`.
* <a href="https://pyyaml.org/wiki/PyYAMLDocumentation" target="_blank"><code>pyyaml</code></a> - Bắt buộc để hỗ trợ `SchemaGenerator` cho Starlette (bạn có thể không cần nó trong ReadyAPI).

Sử dụng bởi ReadyAPI / Starlette:

* <a href="https://www.uvicorn.org" target="_blank"><code>uvicorn</code></a> - Server để chạy ứng dụng của bạn.
* <a href="https://github.com/ijl/orjson" target="_blank"><code>orjson</code></a> - Bắt buộc nếu bạn muốn sử dụng `ORJSONResponse`.
* <a href="https://github.com/esnme/ultrajson" target="_blank"><code>ujson</code></a> - Bắt buộc nếu bạn muốn sử dụng `UJSONResponse`.

Bạn có thể cài đặt tất cả những dependency trên với `pip install "readyapi[all]"`.

## Giấy phép

Dự án này được cấp phép dưới những điều lệ của giấy phép MIT.
