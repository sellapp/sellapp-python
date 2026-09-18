# orders_line_items

[All resources](../methods.md)

## list

List an order's line items

[API reference](https://sell.app/docs/api/order-line-items/list-an-orders-line-items) · Effect: **read**

```python
def list(
        self,
        order: int,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order_: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListOrderSLineItemsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order_ | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListOrderSLineItemsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders_line_items.list(order=4001)
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

Search an order's line items

[API reference](https://sell.app/docs/api/order-line-items/search-an-orders-line-items) · Effect: **read**

```python
def search(
        self,
        order: int,
        *,
        filters: builtins.list[
            SearchOrderSLineItemsRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchOrderSLineItemsRequestApplicationJsonPropertySortItem]
        | None = None,
        pagination: SearchOrderSLineItemsRequestApplicationJsonPropertyPagination
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order_: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchOrderSLineItemsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| filters | `builtins.list[
            SearchOrderSLineItemsRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchOrderSLineItemsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| pagination | `SearchOrderSLineItemsRequestApplicationJsonPropertyPagination
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order_ | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SearchOrderSLineItemsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders_line_items.search(order=4001)
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

Retrieve an order's line item

[API reference](https://sell.app/docs/api/order-line-items/retrieve-an-orders-line-item) · Effect: **read**

```python
def get(
        self,
        order: int,
        line_item: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetOrderSLineItemResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| line_item | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetOrderSLineItemResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders_line_items.get(
    order=4001,
    line_item=9001
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

