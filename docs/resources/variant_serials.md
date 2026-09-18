# variant_serials

[All resources](../methods.md)

## list

List variant serial inventory

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```python
def list(
        self,
        product: int,
        variant: int,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        search: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        ListVariantSerialInventoryResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| search | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        ListVariantSerialInventoryResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_serials.list(
    product=1,
    variant=1
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## append

Append variant serial inventory

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```python
def append(
        self,
        product: int,
        variant: int,
        *,
        serials: builtins.list[str],
        remove_duplicates: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkAppendVariantSerialInventoryResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| serials | `builtins.list[str]` | Yes |
| remove_duplicates | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkAppendVariantSerialInventoryResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_serials.append(
    product=1,
    variant=1,
    serials=["LICENSE-KEY-001", "LICENSE-KEY-002"],
    remove_duplicates=True
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

Documented HTTP responses: 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace

Replace variant serial inventory

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```python
def replace(
        self,
        product: int,
        variant: int,
        *,
        serials: builtins.list[str],
        remove_duplicates: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceVariantSerialInventoryResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| serials | `builtins.list[str]` | Yes |
| remove_duplicates | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceVariantSerialInventoryResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_serials.replace(
    product=1,
    variant=1,
    serials=["LICENSE-KEY-001", "LICENSE-KEY-002"],
    remove_duplicates=True
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## queue

Queue a variant serial import

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```python
def queue(
        self,
        product: int,
        variant: int,
        *,
        file: bytes,
        parsing_mode: SdkQueueVariantSerialImportRequestMultipartFormDataParsingMode
        | str,
        custom_delimiter: str | None | NotGiven = NOT_GIVEN,
        remove_duplicates: bool | None = None,
        mode: SdkQueueVariantSerialImportRequestMultipartFormDataMode
        | str
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkQueueVariantSerialImportResponseValue202ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| file | `bytes` | Yes |
| parsing_mode | `SdkQueueVariantSerialImportRequestMultipartFormDataParsingMode
        \| str` | Yes |
| custom_delimiter | `str \| None \| NotGiven` | No |
| remove_duplicates | `bool \| None` | No |
| mode | `SdkQueueVariantSerialImportRequestMultipartFormDataMode
        \| str
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkQueueVariantSerialImportResponseValue202ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_serials.queue(
    product=1,
    variant=1,
    file="serials.txt",
    parsing_mode="NEW_LINE",
    remove_duplicates=True,
    mode="append"
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

Documented HTTP responses: 202, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## delete

Delete a variant serial

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```python
def delete(
        self,
        product: int,
        variant: int,
        serial: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| serial | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_serials.delete(
    product=1,
    variant=1,
    serial="string_example"
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

