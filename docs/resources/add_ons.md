# add_ons

[All resources](../methods.md)

## list

List add-ons

[API reference](https://sell.app/docs/api/add-ons/list-add-ons) · Effect: **read**

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
        with_drafts: bool | None = None,
        only_drafts: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkListAddOnsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| with_drafts | `bool \| None` | No |
| only_drafts | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkListAddOnsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.add_ons.list()
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

Create an add-on draft

[API reference](https://sell.app/docs/api/add-ons/create-an-add-on-draft) · Effect: **consequential**

```python
def create(
        self,
        *,
        title: str,
        description: str,
        visibility: CatalogVisibility | str,
        slug: str | None = None,
        is_draft: bool | None = None,
        parent_product_ids: builtins.list[int] | None = None,
        variant: CreateAddOnDraftRequestApplicationJsonPropertyVariant | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateAddOnDraftResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| description | `str` | Yes |
| visibility | `CatalogVisibility \| str` | Yes |
| slug | `str \| None` | No |
| is_draft | `bool \| None` | No |
| parent_product_ids | `builtins.list[int] \| None` | No |
| variant | `CreateAddOnDraftRequestApplicationJsonPropertyVariant \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateAddOnDraftResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.add_ons.create(
    title="Customer support",
    description="Priority support for launches scheduled suspiciously close to Friday.",
    visibility="PUBLIC",
    parent_product_ids=[120, 121]
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search add-ons

[API reference](https://sell.app/docs/api/add-ons/search-add-ons) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[SearchAddOnsRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[SearchAddOnsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchAddOnsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[SearchAddOnsRequestApplicationJsonPropertyIncludesItem]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        with_drafts: bool | None = None,
        only_drafts: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchAddOnsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[SearchAddOnsRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[SearchAddOnsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchAddOnsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[SearchAddOnsRequestApplicationJsonPropertyIncludesItem]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| with_drafts | `bool \| None` | No |
| only_drafts | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkSearchAddOnsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.add_ons.search(
    filters=[{"field": "id", "operator": "=", "value": 410}],
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

## get

Retrieve an add-on

[API reference](https://sell.app/docs/api/add-ons/retrieve-an-add-on) · Effect: **read**

```python
def get(
        self,
        addon: int,
        *,
        pagination: bool | None = None,
        with_drafts: bool | None = None,
        only_drafts: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkGetAddOnResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `int` | Yes |
| pagination | `bool \| None` | No |
| with_drafts | `bool \| None` | No |
| only_drafts | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetAddOnResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.add_ons.get(addon=410)
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

Update an add-on

[API reference](https://sell.app/docs/api/add-ons/replace-an-add-on) · Effect: **consequential**

```python
def replace(
        self,
        addon: int,
        *,
        title: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        visibility: CatalogVisibility | str | None = None,
        is_draft: bool | None = None,
        parent_product_ids: builtins.list[int] | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceAddOnResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `int` | Yes |
| title | `str \| None` | No |
| slug | `str \| None` | No |
| description | `str \| None` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| is_draft | `bool \| None` | No |
| parent_product_ids | `builtins.list[int] \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceAddOnResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.add_ons.replace(
    addon=410,
    description="Priority email, chat, and launch-day reassurance.",
    is_draft=False
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

Update an add-on

[API reference](https://sell.app/docs/api/add-ons/update-an-add-on) · Effect: **consequential**

```python
def update(
        self,
        addon: int,
        *,
        title: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        visibility: CatalogVisibility | str | None = None,
        is_draft: bool | None = None,
        parent_product_ids: builtins.list[int] | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateAddOnResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `int` | Yes |
| title | `str \| None` | No |
| slug | `str \| None` | No |
| description | `str \| None` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| is_draft | `bool \| None` | No |
| parent_product_ids | `builtins.list[int] \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateAddOnResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.add_ons.update(
    addon=410,
    description="Priority email, chat, and launch-day reassurance.",
    is_draft=False
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

Delete an add-on

[API reference](https://sell.app/docs/api/add-ons/delete-an-add-on) · Effect: **consequential**

```python
def delete(
        self,
        addon: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.add_ons.delete(addon=410)
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

