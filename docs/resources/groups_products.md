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
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkAddProductsToGroupResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[
        ListProductsWithinGroupResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        product_ids: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkSyncGroupProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| product_ids | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetProductWithinGroupResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| product | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchProductsWithinGroupRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchProductsWithinGroupRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[
            SearchProductsWithinGroupRequestApplicationJsonPropertySearch
        ] = None,
        includes: Optional[
            List[SearchProductsWithinGroupRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[
        SearchProductsWithinGroupResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| filters | `Optional[
            List[SearchProductsWithinGroupRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchProductsWithinGroupRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[
            SearchProductsWithinGroupRequestApplicationJsonPropertySearch
        ]` | No |
| includes | `Optional[
            List[SearchProductsWithinGroupRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

