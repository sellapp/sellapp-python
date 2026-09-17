# credits_products

[All resources](../methods.md)

## list

List credits products

[API reference](https://sell.app/docs/api/credits/list-credit-products) · Effect: **read**

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
    ) -> SyncPage[SdkListCreditsProductsResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkListCreditsProductsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.credits_products.list()
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

Create a credits product

[API reference](https://sell.app/docs/api/credits/create-a-credit-product) · Effect: **consequential**

```python
def create(
        self,
        *,
        title: str,
        visibility: Union[CatalogVisibility, str],
        slug: Optional[str] = None,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        section_id: Union[int, None, NotGiven] = NOT_GIVEN,
        is_draft: Optional[bool] = None,
        price_cents: Optional[int] = None,
        currency: Optional[str] = None,
        minimum_purchase_quantity: Optional[int] = None,
        maximum_purchase_quantity: Union[int, None, NotGiven] = NOT_GIVEN,
        quantity_increment: Optional[int] = None,
        stock: Union[int, None, NotGiven] = NOT_GIVEN,
        payment_methods: Optional[
            List[
                Union[SdkCreateCreditsProductRequestApplicationJsonPaymentMethods, str]
            ]
        ] = None,
        rate_tiers: Optional[
            List[CreateCreditsProductRequestApplicationJsonPropertyRateTiersItem]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateCreditsProductResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| visibility | `Union[CatalogVisibility, str]` | Yes |
| slug | `Optional[str]` | No |
| description | `Union[str, None, NotGiven]` | No |
| section_id | `Union[int, None, NotGiven]` | No |
| is_draft | `Optional[bool]` | No |
| price_cents | `Optional[int]` | No |
| currency | `Optional[str]` | No |
| minimum_purchase_quantity | `Optional[int]` | No |
| maximum_purchase_quantity | `Union[int, None, NotGiven]` | No |
| quantity_increment | `Optional[int]` | No |
| stock | `Union[int, None, NotGiven]` | No |
| payment_methods | `Optional[
            List[
                Union[SdkCreateCreditsProductRequestApplicationJsonPaymentMethods, str]
            ]
        ]` | No |
| rate_tiers | `Optional[
            List[CreateCreditsProductRequestApplicationJsonPropertyRateTiersItem]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateCreditsProductResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.credits_products.create(
    title="Design credits",
    visibility="HIDDEN",
    price_cents=1999,
    currency="USD"
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

Search credits products

[API reference](https://sell.app/docs/api/credits/search-credit-products) · Effect: **read**

```python
def search(
        self,
        *,
        filters: Optional[
            List[SearchCreditsProductsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchCreditsProductsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[
            SearchCreditsProductsRequestApplicationJsonPropertySearch
        ] = None,
        includes: Optional[
            List[SearchCreditsProductsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchCreditsProductsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchCreditsProductsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchCreditsProductsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[
            SearchCreditsProductsRequestApplicationJsonPropertySearch
        ]` | No |
| includes | `Optional[
            List[SearchCreditsProductsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SdkSearchCreditsProductsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.credits_products.search()
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

Retrieve a credits product

[API reference](https://sell.app/docs/api/credits/retrieve-a-credit-product) · Effect: **read**

```python
def get(
        self,
        credit_product: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCreditsProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| credit_product | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetCreditsProductResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.credits_products.get(credit_product=1)
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

Replace a credits product

[API reference](https://sell.app/docs/api/credits/replace-a-credit-product) · Effect: **consequential**

```python
def replace(
        self,
        credit_product: int,
        *,
        title: Optional[str] = None,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Union[CatalogVisibility, str]] = None,
        section_id: Union[int, None, NotGiven] = NOT_GIVEN,
        is_draft: Optional[bool] = None,
        price_cents: Optional[int] = None,
        currency: Optional[str] = None,
        minimum_purchase_quantity: Optional[int] = None,
        maximum_purchase_quantity: Union[int, None, NotGiven] = NOT_GIVEN,
        quantity_increment: Optional[int] = None,
        stock: Union[int, None, NotGiven] = NOT_GIVEN,
        payment_methods: Optional[
            List[
                Union[SdkReplaceCreditsProductRequestApplicationJsonPaymentMethods, str]
            ]
        ] = None,
        rate_tiers: Optional[
            List[ReplaceCreditsProductRequestApplicationJsonPropertyRateTiersItem]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceCreditsProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| credit_product | `int` | Yes |
| title | `Optional[str]` | No |
| slug | `Optional[str]` | No |
| description | `Optional[str]` | No |
| visibility | `Optional[Union[CatalogVisibility, str]]` | No |
| section_id | `Union[int, None, NotGiven]` | No |
| is_draft | `Optional[bool]` | No |
| price_cents | `Optional[int]` | No |
| currency | `Optional[str]` | No |
| minimum_purchase_quantity | `Optional[int]` | No |
| maximum_purchase_quantity | `Union[int, None, NotGiven]` | No |
| quantity_increment | `Optional[int]` | No |
| stock | `Union[int, None, NotGiven]` | No |
| payment_methods | `Optional[
            List[
                Union[SdkReplaceCreditsProductRequestApplicationJsonPaymentMethods, str]
            ]
        ]` | No |
| rate_tiers | `Optional[
            List[ReplaceCreditsProductRequestApplicationJsonPropertyRateTiersItem]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceCreditsProductResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.credits_products.replace(
    credit_product=1,
    title="Design credits"
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

Update a credits product

[API reference](https://sell.app/docs/api/credits/update-a-credit-product) · Effect: **consequential**

```python
def update(
        self,
        credit_product: int,
        *,
        title: Optional[str] = None,
        slug: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Union[CatalogVisibility, str]] = None,
        section_id: Union[int, None, NotGiven] = NOT_GIVEN,
        is_draft: Optional[bool] = None,
        price_cents: Optional[int] = None,
        currency: Optional[str] = None,
        minimum_purchase_quantity: Optional[int] = None,
        maximum_purchase_quantity: Union[int, None, NotGiven] = NOT_GIVEN,
        quantity_increment: Optional[int] = None,
        stock: Union[int, None, NotGiven] = NOT_GIVEN,
        payment_methods: Optional[
            List[
                Union[SdkUpdateCreditsProductRequestApplicationJsonPaymentMethods, str]
            ]
        ] = None,
        rate_tiers: Optional[
            List[UpdateCreditsProductRequestApplicationJsonPropertyRateTiersItem]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCreditsProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| credit_product | `int` | Yes |
| title | `Optional[str]` | No |
| slug | `Optional[str]` | No |
| description | `Optional[str]` | No |
| visibility | `Optional[Union[CatalogVisibility, str]]` | No |
| section_id | `Union[int, None, NotGiven]` | No |
| is_draft | `Optional[bool]` | No |
| price_cents | `Optional[int]` | No |
| currency | `Optional[str]` | No |
| minimum_purchase_quantity | `Optional[int]` | No |
| maximum_purchase_quantity | `Union[int, None, NotGiven]` | No |
| quantity_increment | `Optional[int]` | No |
| stock | `Union[int, None, NotGiven]` | No |
| payment_methods | `Optional[
            List[
                Union[SdkUpdateCreditsProductRequestApplicationJsonPaymentMethods, str]
            ]
        ]` | No |
| rate_tiers | `Optional[
            List[UpdateCreditsProductRequestApplicationJsonPropertyRateTiersItem]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateCreditsProductResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.credits_products.update(
    credit_product=1,
    title="Design credits"
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

Delete a credits product

[API reference](https://sell.app/docs/api/credits/delete-a-credit-product) · Effect: **consequential**

```python
def delete(
        self,
        credit_product: int,
        *,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| credit_product | `int` | Yes |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.credits_products.delete(
    credit_product=1,
    expected_updated_at="2026-08-24T10:00:00.000000Z"
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

