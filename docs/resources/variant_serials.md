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
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        search: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[
        ListVariantSerialInventoryResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| search | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        serials: List[str],
        remove_duplicates: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkAppendVariantSerialInventoryResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| serials | `List[str]` | Yes |
| remove_duplicates | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        serials: List[str],
        remove_duplicates: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceVariantSerialInventoryResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| serials | `List[str]` | Yes |
| remove_duplicates | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        parsing_mode: Union[
            SdkQueueVariantSerialImportRequestMultipartFormDataParsingMode, str
        ],
        custom_delimiter: Union[str, None, NotGiven] = NOT_GIVEN,
        remove_duplicates: Optional[bool] = None,
        mode: Optional[
            Union[SdkQueueVariantSerialImportRequestMultipartFormDataMode, str]
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkQueueVariantSerialImportResponseValue202ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| file | `bytes` | Yes |
| parsing_mode | `Union[
            SdkQueueVariantSerialImportRequestMultipartFormDataParsingMode, str
        ]` | Yes |
| custom_delimiter | `Union[str, None, NotGiven]` | No |
| remove_duplicates | `Optional[bool]` | No |
| mode | `Optional[
            Union[SdkQueueVariantSerialImportRequestMultipartFormDataMode, str]
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| serial | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

