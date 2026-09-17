# add_ons

[All resources](../methods.md)

## list

List add-ons

[API reference](https://sell.app/docs/api/add-ons/list-add-ons) · Effect: **read**

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
        with_drafts: Optional[bool] = None,
        only_drafts: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkListAddOnsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| with_drafts | `Optional[bool]` | No |
| only_drafts | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        visibility: Union[CatalogVisibility, str],
        slug: Optional[str] = None,
        is_draft: Optional[bool] = None,
        parent_product_ids: Optional[List[int]] = None,
        variant: Optional[CreateAddOnDraftRequestApplicationJsonPropertyVariant] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateAddOnDraftResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| description | `str` | Yes |
| visibility | `Union[CatalogVisibility, str]` | Yes |
| slug | `Optional[str]` | No |
| is_draft | `Optional[bool]` | No |
| parent_product_ids | `Optional[List[int]]` | No |
| variant | `Optional[CreateAddOnDraftRequestApplicationJsonPropertyVariant]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchAddOnsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[List[SearchAddOnsRequestApplicationJsonPropertySortItem]] = None,
        search: Optional[SearchAddOnsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchAddOnsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        with_drafts: Optional[bool] = None,
        only_drafts: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchAddOnsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchAddOnsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[List[SearchAddOnsRequestApplicationJsonPropertySortItem]]` | No |
| search | `Optional[SearchAddOnsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchAddOnsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| with_drafts | `Optional[bool]` | No |
| only_drafts | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        pagination: Optional[bool] = None,
        with_drafts: Optional[bool] = None,
        only_drafts: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetAddOnResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `int` | Yes |
| pagination | `Optional[bool]` | No |
| with_drafts | `Optional[bool]` | No |
| only_drafts | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        title: Optional[str] = None,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Union[CatalogVisibility, str]] = None,
        is_draft: Optional[bool] = None,
        parent_product_ids: Optional[List[int]] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceAddOnResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `int` | Yes |
| title | `Optional[str]` | No |
| slug | `Optional[str]` | No |
| description | `Optional[str]` | No |
| visibility | `Optional[Union[CatalogVisibility, str]]` | No |
| is_draft | `Optional[bool]` | No |
| parent_product_ids | `Optional[List[int]]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        title: Optional[str] = None,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Union[CatalogVisibility, str]] = None,
        is_draft: Optional[bool] = None,
        parent_product_ids: Optional[List[int]] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateAddOnResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `int` | Yes |
| title | `Optional[str]` | No |
| slug | `Optional[str]` | No |
| description | `Optional[str]` | No |
| visibility | `Optional[Union[CatalogVisibility, str]]` | No |
| is_draft | `Optional[bool]` | No |
| parent_product_ids | `Optional[List[int]]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| addon | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

