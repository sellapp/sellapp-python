# exports

[All resources](../methods.md)

## list_exports

List exports

[API reference](https://sell.app/docs/api/exports) · Effect: **read**

```python
def list_exports(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListExportsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListExportsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.exports.list_exports()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create_export

Create an export

[API reference](https://sell.app/docs/api/exports) · Effect: **consequential**

```python
def create_export(
        self,
        *,
        type: SdkCreateExportRequestApplicationJsonType | str,
        format: SdkCreateExportRequestApplicationJsonFormat | str,
        parameters: CreateExportRequestApplicationJsonPropertyParameters | None = None,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateExportResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| type | `SdkCreateExportRequestApplicationJsonType \| str` | Yes |
| format | `SdkCreateExportRequestApplicationJsonFormat \| str` | Yes |
| parameters | `CreateExportRequestApplicationJsonPropertyParameters \| None` | No |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateExportResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.exports.create_export(
    type="sales",
    format="csv",
    parameters={"from": "2026-08-01", "to": "2026-08-31"}
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_export

Retrieve an export

[API reference](https://sell.app/docs/api/exports) · Effect: **read**

```python
def get_export(
        self,
        export: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetExportResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| export | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetExportResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.exports.get_export(export="01992a65-e064-71ba-b38f-902b7966a6be")
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## download_export

Download an export

[API reference](https://sell.app/docs/api/exports) · Effect: **read**

```python
def download_export(
        self,
        export: str,
        *,
        expires: int,
        signature: str,
        request_options: RequestOptions | None = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| export | `str` | Yes |
| expires | `int` | Yes |
| signature | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `Any`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.exports.download_export(
    export="01992a65-e064-71ba-b38f-902b7966a6be",
    expires=1788513423,
    signature="2c91df645a086ec399153a932b741f809d2b85c69740eaf3612384ebfb913a65"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": []
  },
  {
    "oauthAccessToken": [
      "admin"
    ],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 302, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

