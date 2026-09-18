# highlights_media

[All resources](../methods.md)

## list

List highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **read**

```python
def list(
        self,
        highlight: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkListHighlightMediaResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListHighlightMediaResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights_media.list(highlight=1)
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

## add

Add highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **write**

```python
def add(
        self,
        highlight: int,
        *,
        file: bytes,
        cta_title: str | None = None,
        product_id: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkAddHighlightMediaResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| file | `bytes` | Yes |
| cta_title | `str \| None` | No |
| product_id | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkAddHighlightMediaResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights_media.add(
    highlight=1,
    file="/path/to/example.png",
    cta_title="View product",
    product_id=123
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

## reorder

Reorder highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **consequential**

```python
def reorder(
        self,
        highlight: int,
        *,
        resources: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> SdkReorderHighlightMediaResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| resources | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReorderHighlightMediaResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights_media.reorder(
    highlight=1,
    resources=[42, 41]
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

## replace

Replace highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **write**

```python
def replace(
        self,
        highlight: int,
        media: int,
        *,
        file: bytes,
        cta_title: str | None = None,
        product_id: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceHighlightMediaResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| media | `int` | Yes |
| file | `bytes` | Yes |
| cta_title | `str \| None` | No |
| product_id | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceHighlightMediaResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights_media.replace(
    highlight=1,
    media=84,
    file="/path/to/example.png",
    cta_title="View product",
    product_id=123
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

## replace_metadata

Update highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **write**

```python
def replace_metadata(
        self,
        highlight: int,
        media: int,
        *,
        cta_title: str | None = None,
        product_id: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceHighlightMediaMetadataResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| media | `int` | Yes |
| cta_title | `str \| None` | No |
| product_id | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceHighlightMediaMetadataResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights_media.replace_metadata(
    highlight=1,
    media=84,
    cta_title="View product",
    product_id=123
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

## update

Update highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **write**

```python
def update(
        self,
        highlight: int,
        media: int,
        *,
        cta_title: str | None = None,
        product_id: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateHighlightMediaResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| media | `int` | Yes |
| cta_title | `str \| None` | No |
| product_id | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateHighlightMediaResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights_media.update(
    highlight=1,
    media=84,
    cta_title="View product",
    product_id=123
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

## delete

Delete highlight media

[API reference](https://sell.app/docs/api/highlights/manage-highlight-media) · Effect: **consequential**

```python
def delete(
        self,
        highlight: int,
        media: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| media | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights_media.delete(
    highlight=1,
    media=84
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

