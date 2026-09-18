# coupons

[All resources](../methods.md)

## list

List all coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListCouponsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListCouponsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.list()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create

Create a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def create(
        self,
        *,
        code: str,
        type: SdkCreateCouponRequestApplicationJsonType | str,
        discount: float | str,
        store_wide: bool,
        products: builtins.list[int] | None = None,
        product_variants: builtins.list[int] | None = None,
        limit: int | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        minimum_amount: float | str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateCouponResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| code | `str` | Yes |
| type | `SdkCreateCouponRequestApplicationJsonType \| str` | Yes |
| discount | `float \| str` | Yes |
| store_wide | `bool` | Yes |
| products | `builtins.list[int] \| None` | No |
| product_variants | `builtins.list[int] \| None` | No |
| limit | `int \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| minimum_amount | `float \| str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateCouponResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.create(
    code="PLAN10",
    type="PERCENTAGE",
    discount=10,
    store_wide=False,
    products=[123, 456],
    product_variants=[1001, 1002]
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 201, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def get(
        self,
        coupon: int,
        *,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCouponResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.get(coupon=1)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace

Update a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def replace(
        self,
        coupon: int,
        *,
        code: str | None = None,
        type: SdkReplaceCouponRequestApplicationJsonType | str | None = None,
        discount: float | str | None = None,
        store_wide: bool | None = None,
        products: builtins.list[int] | None = None,
        product_variants: builtins.list[int] | None = None,
        limit: int | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        minimum_amount: float | str | None | NotGiven = NOT_GIVEN,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| code | `str \| None` | No |
| type | `SdkReplaceCouponRequestApplicationJsonType \| str \| None` | No |
| discount | `float \| str \| None` | No |
| store_wide | `bool \| None` | No |
| products | `builtins.list[int] \| None` | No |
| product_variants | `builtins.list[int] \| None` | No |
| limit | `int \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| minimum_amount | `float \| str \| None \| NotGiven` | No |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceCouponResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.replace(
    coupon=1,
    store_wide=False,
    products=[123],
    product_variants=[1001, 1002]
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update

Update a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def update(
        self,
        coupon: int,
        *,
        code: str | None = None,
        type: SdkUpdateCouponRequestApplicationJsonType | str | None = None,
        discount: float | str | None = None,
        store_wide: bool | None = None,
        products: builtins.list[int] | None = None,
        product_variants: builtins.list[int] | None = None,
        limit: int | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        minimum_amount: float | str | None | NotGiven = NOT_GIVEN,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| code | `str \| None` | No |
| type | `SdkUpdateCouponRequestApplicationJsonType \| str \| None` | No |
| discount | `float \| str \| None` | No |
| store_wide | `bool \| None` | No |
| products | `builtins.list[int] \| None` | No |
| product_variants | `builtins.list[int] \| None` | No |
| limit | `int \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| minimum_amount | `float \| str \| None \| NotGiven` | No |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCouponResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.update(
    coupon=1,
    store_wide=False,
    products=[123],
    product_variants=[1001, 1002]
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## delete

Delete a coupon

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def delete(
        self,
        coupon: int,
        *,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.delete(coupon=1)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[SearchCouponsRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[SearchCouponsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchCouponsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[SearchCouponsRequestApplicationJsonPropertyIncludesItem]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchCouponsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[SearchCouponsRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[SearchCouponsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchCouponsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[SearchCouponsRequestApplicationJsonPropertyIncludesItem]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SearchCouponsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.search(
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
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_create

Batch create coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def batch_create(
        self,
        *,
        resources: builtins.list[
            BatchCreateCouponsRequestApplicationJsonPropertyResourcesItem
        ],
        request_options: RequestOptions | None = None,
    ) -> SdkBatchCreateCouponsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `builtins.list[
            BatchCreateCouponsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkBatchCreateCouponsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.batch_create(
    resources=[
        {
            "code": "STARTER10",
            "type": "PERCENTAGE",
            "discount": 10,
            "store_wide": False,
            "products": [123],
            "product_variants": [1001]
        }
    ]
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 201, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_update

Batch update coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def batch_update(
        self,
        *,
        resources: BatchUpdateCouponsRequestApplicationJsonPropertyResources,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkBatchUpdateCouponsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `BatchUpdateCouponsRequestApplicationJsonPropertyResources` | Yes |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkBatchUpdateCouponsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.batch_update(
    resources={
        "1": {"store_wide": False, "products": [123], "product_variants": [1001, 1002]}
    }
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_delete

Batch delete coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def batch_delete(
        self,
        *,
        resources: builtins.list[int],
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `builtins.list[int]` | Yes |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.batch_delete(resources=[1, 2])
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v2_list_coupons

List all coupons

[API reference](https://sell.app/docs/api/coupons/list-all-coupons) · Effect: **read**

```python
def v2_list_coupons(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[V2ListCouponsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[V2ListCouponsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_list_coupons()
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

## v2_create_coupon

Create a coupon

[API reference](https://sell.app/docs/api/coupons/create-a-coupon) · Effect: **consequential**

```python
def v2_create_coupon(
        self,
        *,
        code: str,
        type: SdkV2CreateCouponRequestApplicationJsonType | str,
        discount: float | str,
        store_wide: bool,
        products: builtins.list[int] | None = None,
        product_variants: builtins.list[int] | None = None,
        limit: int | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        minimum_amount: float | str | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkV2CreateCouponResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| code | `str` | Yes |
| type | `SdkV2CreateCouponRequestApplicationJsonType \| str` | Yes |
| discount | `float \| str` | Yes |
| store_wide | `bool` | Yes |
| products | `builtins.list[int] \| None` | No |
| product_variants | `builtins.list[int] \| None` | No |
| limit | `int \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| minimum_amount | `float \| str \| None \| NotGiven` | No |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2CreateCouponResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_create_coupon(
    code="PLAN10",
    type="PERCENTAGE",
    discount=10,
    store_wide=False,
    products=[123, 456],
    product_variants=[1001, 1002]
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

## v2_search_coupons

Search coupons

[API reference](https://sell.app/docs/api/coupons/search-coupons) · Effect: **read**

```python
def v2_search_coupons(
        self,
        *,
        filters: builtins.list[V2SearchCouponsRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[V2SearchCouponsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: V2SearchCouponsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            V2SearchCouponsRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[V2SearchCouponsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[V2SearchCouponsRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[V2SearchCouponsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `V2SearchCouponsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            V2SearchCouponsRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[V2SearchCouponsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_search_coupons(
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v2_get_coupon

Retrieve a coupon

[API reference](https://sell.app/docs/api/coupons/retrieve-a-coupon) · Effect: **read**

```python
def v2_get_coupon(
        self,
        coupon: int,
        *,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkV2GetCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2GetCouponResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_get_coupon(coupon=1)
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

## v2_replace_coupon

Update a coupon

[API reference](https://sell.app/docs/api/coupons/update-a-coupon) · Effect: **consequential**

```python
def v2_replace_coupon(
        self,
        coupon: int,
        *,
        code: str | None = None,
        type: SdkV2ReplaceCouponRequestApplicationJsonType | str | None = None,
        discount: float | str | None = None,
        store_wide: bool | None = None,
        products: builtins.list[int] | None = None,
        product_variants: builtins.list[int] | None = None,
        limit: int | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        minimum_amount: float | str | None | NotGiven = NOT_GIVEN,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkV2ReplaceCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| code | `str \| None` | No |
| type | `SdkV2ReplaceCouponRequestApplicationJsonType \| str \| None` | No |
| discount | `float \| str \| None` | No |
| store_wide | `bool \| None` | No |
| products | `builtins.list[int] \| None` | No |
| product_variants | `builtins.list[int] \| None` | No |
| limit | `int \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| minimum_amount | `float \| str \| None \| NotGiven` | No |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2ReplaceCouponResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_replace_coupon(
    coupon=1,
    store_wide=False,
    products=[123],
    product_variants=[1001, 1002]
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

## v2_update_coupon

Update a coupon

[API reference](https://sell.app/docs/api/coupons/update-a-coupon) · Effect: **consequential**

```python
def v2_update_coupon(
        self,
        coupon: int,
        *,
        code: str | None = None,
        type: SdkV2UpdateCouponRequestApplicationJsonType | str | None = None,
        discount: float | str | None = None,
        store_wide: bool | None = None,
        products: builtins.list[int] | None = None,
        product_variants: builtins.list[int] | None = None,
        limit: int | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        minimum_amount: float | str | None | NotGiven = NOT_GIVEN,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkV2UpdateCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| code | `str \| None` | No |
| type | `SdkV2UpdateCouponRequestApplicationJsonType \| str \| None` | No |
| discount | `float \| str \| None` | No |
| store_wide | `bool \| None` | No |
| products | `builtins.list[int] \| None` | No |
| product_variants | `builtins.list[int] \| None` | No |
| limit | `int \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| minimum_amount | `float \| str \| None \| NotGiven` | No |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2UpdateCouponResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_update_coupon(
    coupon=1,
    store_wide=False,
    products=[123],
    product_variants=[1001, 1002]
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

## v2_delete_coupon

Delete a coupon

[API reference](https://sell.app/docs/api/coupons/delete-a-coupon) · Effect: **consequential**

```python
def v2_delete_coupon(
        self,
        coupon: int,
        *,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_delete_coupon(coupon=1)
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

## v2_batch_create_coupons

Batch create coupons

[API reference](https://sell.app/docs/api/coupons/batch-create-coupons) · Effect: **consequential**

```python
def v2_batch_create_coupons(
        self,
        *,
        resources: builtins.list[
            V2BatchCreateCouponsRequestApplicationJsonPropertyResourcesItem
        ],
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkV2BatchCreateCouponsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `builtins.list[
            V2BatchCreateCouponsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2BatchCreateCouponsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_batch_create_coupons(
    resources=[
        {
            "code": "STARTER10",
            "type": "PERCENTAGE",
            "discount": 10,
            "store_wide": False,
            "products": [123],
            "product_variants": [1001]
        }
    ]
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

Documented HTTP responses: 200, 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v2_batch_update_coupons

Batch update coupons

[API reference](https://sell.app/docs/api/coupons/batch-update-coupons) · Effect: **consequential**

```python
def v2_batch_update_coupons(
        self,
        *,
        resources: V2BatchUpdateCouponsRequestApplicationJsonPropertyResources,
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkV2BatchUpdateCouponsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `V2BatchUpdateCouponsRequestApplicationJsonPropertyResources` | Yes |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2BatchUpdateCouponsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_batch_update_coupons(
    resources={
        "1": {"store_wide": False, "products": [123], "product_variants": [1001, 1002]}
    }
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

## v2_batch_delete_coupons

Batch delete coupons

[API reference](https://sell.app/docs/api/coupons/batch-delete-coupons) · Effect: **consequential**

```python
def v2_batch_delete_coupons(
        self,
        *,
        resources: builtins.list[int],
        with_trashed: bool | None = None,
        only_trashed: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `builtins.list[int]` | Yes |
| with_trashed | `bool \| None` | No |
| only_trashed | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.coupons.v2_batch_delete_coupons(resources=[1, 2])
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

