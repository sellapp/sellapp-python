# highlights

[All resources](../methods.md)

## list

List highlights

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkListHighlightsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkListHighlightsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights.list()
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create

Create a highlight

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **write**

```python
def create(
        self,
        *,
        title: str,
        hidden: bool,
        files: builtins.list[bytes],
        request_options: RequestOptions | None = None,
    ) -> SdkCreateHighlightResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| hidden | `bool` | Yes |
| files | `builtins.list[bytes]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateHighlightResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights.create(
    title="Stealth-mode launch",
    hidden=False,
    files=["/path/to/example.png"]
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

## search

Search highlights

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[
            SearchHighlightsRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchHighlightsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchHighlightsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchHighlightsRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchHighlightsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[
            SearchHighlightsRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchHighlightsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchHighlightsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchHighlightsRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkSearchHighlightsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights.search(
    filters=[{"field": "id", "operator": "=", "value": 42}],
    sort=[{"field": "created_at", "direction": "desc"}]
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## reorder

Reorder highlights

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **consequential**

```python
def reorder(
        self,
        *,
        resources: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> SdkReorderHighlightsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReorderHighlightsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights.reorder(resources=[42, 41])
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

## get

Retrieve a highlight

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **read**

```python
def get(
        self,
        highlight: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetHighlightResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetHighlightResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights.get(highlight=42)
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

Update a highlight

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **write**

```python
def replace(
        self,
        highlight: int,
        *,
        title: str | None = None,
        hidden: bool | None = None,
        published: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceHighlightResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| title | `str \| None` | No |
| hidden | `bool \| None` | No |
| published | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceHighlightResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights.replace(
    highlight=42,
    title="Stealth-mode launch",
    hidden=False
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

Update a highlight

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **write**

```python
def update(
        self,
        highlight: int,
        *,
        title: str | None = None,
        hidden: bool | None = None,
        published: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateHighlightResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| title | `str \| None` | No |
| hidden | `bool \| None` | No |
| published | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateHighlightResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights.update(
    highlight=42,
    title="Stealth-mode launch",
    hidden=False
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

Delete a highlight

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **consequential**

```python
def delete(
        self,
        highlight: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.highlights.delete(highlight=42)
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

