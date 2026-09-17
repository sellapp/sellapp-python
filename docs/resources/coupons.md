# coupons

[All resources](../methods.md)

## list

List all coupons

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListCouponsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        type: Union[SdkCreateCouponRequestApplicationJsonType, str],
        discount: Union[float, str],
        store_wide: bool,
        products: Optional[List[int]] = None,
        product_variants: Optional[List[int]] = None,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        minimum_amount: Union[Union[float, str], None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateCouponResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| code | `str` | Yes |
| type | `Union[SdkCreateCouponRequestApplicationJsonType, str]` | Yes |
| discount | `Union[float, str]` | Yes |
| store_wide | `bool` | Yes |
| products | `Optional[List[int]]` | No |
| product_variants | `Optional[List[int]]` | No |
| limit | `Union[int, None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| minimum_amount | `Union[Union[float, str], None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        code: Optional[str] = None,
        type: Optional[Union[SdkReplaceCouponRequestApplicationJsonType, str]] = None,
        discount: Optional[Union[float, str]] = None,
        store_wide: Optional[bool] = None,
        products: Optional[List[int]] = None,
        product_variants: Optional[List[int]] = None,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        minimum_amount: Union[Union[float, str], None, NotGiven] = NOT_GIVEN,
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| code | `Optional[str]` | No |
| type | `Optional[Union[SdkReplaceCouponRequestApplicationJsonType, str]]` | No |
| discount | `Optional[Union[float, str]]` | No |
| store_wide | `Optional[bool]` | No |
| products | `Optional[List[int]]` | No |
| product_variants | `Optional[List[int]]` | No |
| limit | `Union[int, None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| minimum_amount | `Union[Union[float, str], None, NotGiven]` | No |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        code: Optional[str] = None,
        type: Optional[Union[SdkUpdateCouponRequestApplicationJsonType, str]] = None,
        discount: Optional[Union[float, str]] = None,
        store_wide: Optional[bool] = None,
        products: Optional[List[int]] = None,
        product_variants: Optional[List[int]] = None,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        minimum_amount: Union[Union[float, str], None, NotGiven] = NOT_GIVEN,
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| code | `Optional[str]` | No |
| type | `Optional[Union[SdkUpdateCouponRequestApplicationJsonType, str]]` | No |
| discount | `Optional[Union[float, str]]` | No |
| store_wide | `Optional[bool]` | No |
| products | `Optional[List[int]]` | No |
| product_variants | `Optional[List[int]]` | No |
| limit | `Union[int, None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| minimum_amount | `Union[Union[float, str], None, NotGiven]` | No |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchCouponsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchCouponsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchCouponsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchCouponsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchCouponsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchCouponsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchCouponsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchCouponsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchCouponsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        resources: List[BatchCreateCouponsRequestApplicationJsonPropertyResourcesItem],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkBatchCreateCouponsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[BatchCreateCouponsRequestApplicationJsonPropertyResourcesItem]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkBatchUpdateCouponsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `BatchUpdateCouponsRequestApplicationJsonPropertyResources` | Yes |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        resources: List[int],
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[int]` | Yes |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[V2ListCouponsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        type: Union[SdkV2CreateCouponRequestApplicationJsonType, str],
        discount: Union[float, str],
        store_wide: bool,
        products: Optional[List[int]] = None,
        product_variants: Optional[List[int]] = None,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        minimum_amount: Union[Union[float, str], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2CreateCouponResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| code | `str` | Yes |
| type | `Union[SdkV2CreateCouponRequestApplicationJsonType, str]` | Yes |
| discount | `Union[float, str]` | Yes |
| store_wide | `bool` | Yes |
| products | `Optional[List[int]]` | No |
| product_variants | `Optional[List[int]]` | No |
| limit | `Union[int, None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| minimum_amount | `Union[Union[float, str], None, NotGiven]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[V2SearchCouponsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[V2SearchCouponsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[V2SearchCouponsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[V2SearchCouponsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[V2SearchCouponsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[V2SearchCouponsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[V2SearchCouponsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[V2SearchCouponsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[V2SearchCouponsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2GetCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        code: Optional[str] = None,
        type: Optional[Union[SdkV2ReplaceCouponRequestApplicationJsonType, str]] = None,
        discount: Optional[Union[float, str]] = None,
        store_wide: Optional[bool] = None,
        products: Optional[List[int]] = None,
        product_variants: Optional[List[int]] = None,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        minimum_amount: Union[Union[float, str], None, NotGiven] = NOT_GIVEN,
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2ReplaceCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| code | `Optional[str]` | No |
| type | `Optional[Union[SdkV2ReplaceCouponRequestApplicationJsonType, str]]` | No |
| discount | `Optional[Union[float, str]]` | No |
| store_wide | `Optional[bool]` | No |
| products | `Optional[List[int]]` | No |
| product_variants | `Optional[List[int]]` | No |
| limit | `Union[int, None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| minimum_amount | `Union[Union[float, str], None, NotGiven]` | No |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        code: Optional[str] = None,
        type: Optional[Union[SdkV2UpdateCouponRequestApplicationJsonType, str]] = None,
        discount: Optional[Union[float, str]] = None,
        store_wide: Optional[bool] = None,
        products: Optional[List[int]] = None,
        product_variants: Optional[List[int]] = None,
        limit: Union[int, None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        minimum_amount: Union[Union[float, str], None, NotGiven] = NOT_GIVEN,
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2UpdateCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| code | `Optional[str]` | No |
| type | `Optional[Union[SdkV2UpdateCouponRequestApplicationJsonType, str]]` | No |
| discount | `Optional[Union[float, str]]` | No |
| store_wide | `Optional[bool]` | No |
| products | `Optional[List[int]]` | No |
| product_variants | `Optional[List[int]]` | No |
| limit | `Union[int, None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| minimum_amount | `Union[Union[float, str], None, NotGiven]` | No |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| coupon | `int` | Yes |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        resources: List[
            V2BatchCreateCouponsRequestApplicationJsonPropertyResourcesItem
        ],
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2BatchCreateCouponsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[
            V2BatchCreateCouponsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2BatchUpdateCouponsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `V2BatchUpdateCouponsRequestApplicationJsonPropertyResources` | Yes |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        resources: List[int],
        with_trashed: Optional[bool] = None,
        only_trashed: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[int]` | Yes |
| with_trashed | `Optional[bool]` | No |
| only_trashed | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

