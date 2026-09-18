# groups_products

[All resources](../methods.md)

## add

Add products to group

[API reference](https://sell.app/docs/api/groups/add-products-to-group) · Effect: **consequential**

```python
def add(
        self,
        group: int,
        *,
        resources: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> SdkAddProductsToGroupResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| resources | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkAddProductsToGroupResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups_products.add(
    group=1,
    resources=[1]
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

## remove

Remove products from group

[API reference](https://sell.app/docs/api/groups/remove-products-from-group) · Effect: **consequential**

```python
def remove(
        self,
        group: int,
        *,
        resources: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| resources | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups_products.remove(
    group=1,
    resources=[1]
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

## list

List all products within group

[API reference](https://sell.app/docs/api/groups/list-all-products-within-group) · Effect: **read**

```python
def list(
        self,
        group: int,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        ListProductsWithinGroupResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        ListProductsWithinGroupResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups_products.list(group=1)
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

Replace ordered group products

[API reference](https://sell.app/docs/api/groups/list-all-products-within-group) · Effect: **consequential**

```python
def replace(
        self,
        group: int,
        *,
        product_ids: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> SdkSyncGroupProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| product_ids | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkSyncGroupProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups_products.replace(
    group=42,
    product_ids=[120, 121]
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

## get

List specific product within group

[API reference](https://sell.app/docs/api/groups/list-specific-product-within-group) · Effect: **read**

```python
def get(
        self,
        group: int,
        product: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetProductWithinGroupResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| product | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetProductWithinGroupResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups_products.get(
    group=1,
    product=1
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

## search

Search products within group

[API reference](https://sell.app/docs/api/groups/search-products-within-group) · Effect: **read**

```python
def search(
        self,
        group: int,
        *,
        filters: builtins.list[
            SearchProductsWithinGroupRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[
            SearchProductsWithinGroupRequestApplicationJsonPropertySortItem
        ]
        | None = None,
        search: SearchProductsWithinGroupRequestApplicationJsonPropertySearch
        | None = None,
        includes: builtins.list[
            SearchProductsWithinGroupRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        SearchProductsWithinGroupResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| filters | `builtins.list[
            SearchProductsWithinGroupRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[
            SearchProductsWithinGroupRequestApplicationJsonPropertySortItem
        ]
        \| None` | No |
| search | `SearchProductsWithinGroupRequestApplicationJsonPropertySearch
        \| None` | No |
| includes | `builtins.list[
            SearchProductsWithinGroupRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        SearchProductsWithinGroupResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups_products.search(
    group=1,
    filters=[{"field": "id", "operator": "=", "value": 1}],
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

