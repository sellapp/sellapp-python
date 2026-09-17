# highlights

[All resources](../methods.md)

## list

List highlights

[API reference](https://sell.app/docs/api/highlights/manage-highlights) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkListHighlightsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        files: List[bytes],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateHighlightResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| hidden | `bool` | Yes |
| files | `List[bytes]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchHighlightsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchHighlightsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchHighlightsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchHighlightsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchHighlightsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchHighlightsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchHighlightsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchHighlightsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchHighlightsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReorderHighlightsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetHighlightResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        title: Optional[str] = None,
        hidden: Optional[bool] = None,
        published: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceHighlightResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| title | `Optional[str]` | No |
| hidden | `Optional[bool]` | No |
| published | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        title: Optional[str] = None,
        hidden: Optional[bool] = None,
        published: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateHighlightResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| title | `Optional[str]` | No |
| hidden | `Optional[bool]` | No |
| published | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| highlight | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

