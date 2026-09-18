# credits_products

[All resources](../methods.md)

## list

List credits products

[API reference](https://sell.app/docs/api/credits/list-credit-products) · Effect: **read**

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
    ) -> SyncPage[SdkListCreditsProductsResponseValue200ApplicationJson]:
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
        visibility: CatalogVisibility | str,
        slug: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        section_id: int | None | NotGiven = NOT_GIVEN,
        is_draft: bool | None = None,
        price_cents: int | None = None,
        currency: str | None = None,
        minimum_purchase_quantity: int | None = None,
        maximum_purchase_quantity: int | None | NotGiven = NOT_GIVEN,
        quantity_increment: int | None = None,
        stock: int | None | NotGiven = NOT_GIVEN,
        payment_methods: builtins.list[
            SdkCreateCreditsProductRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        rate_tiers: builtins.list[
            CreateCreditsProductRequestApplicationJsonPropertyRateTiersItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateCreditsProductResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| visibility | `CatalogVisibility \| str` | Yes |
| slug | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| section_id | `int \| None \| NotGiven` | No |
| is_draft | `bool \| None` | No |
| price_cents | `int \| None` | No |
| currency | `str \| None` | No |
| minimum_purchase_quantity | `int \| None` | No |
| maximum_purchase_quantity | `int \| None \| NotGiven` | No |
| quantity_increment | `int \| None` | No |
| stock | `int \| None \| NotGiven` | No |
| payment_methods | `builtins.list[
            SdkCreateCreditsProductRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| rate_tiers | `builtins.list[
            CreateCreditsProductRequestApplicationJsonPropertyRateTiersItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        filters: builtins.list[
            SearchCreditsProductsRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchCreditsProductsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchCreditsProductsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchCreditsProductsRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchCreditsProductsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[
            SearchCreditsProductsRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchCreditsProductsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchCreditsProductsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchCreditsProductsRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> SdkGetCreditsProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| credit_product | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        title: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        visibility: CatalogVisibility | str | None = None,
        section_id: int | None | NotGiven = NOT_GIVEN,
        is_draft: bool | None = None,
        price_cents: int | None = None,
        currency: str | None = None,
        minimum_purchase_quantity: int | None = None,
        maximum_purchase_quantity: int | None | NotGiven = NOT_GIVEN,
        quantity_increment: int | None = None,
        stock: int | None | NotGiven = NOT_GIVEN,
        payment_methods: builtins.list[
            SdkReplaceCreditsProductRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        rate_tiers: builtins.list[
            ReplaceCreditsProductRequestApplicationJsonPropertyRateTiersItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCreditsProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| credit_product | `int` | Yes |
| title | `str \| None` | No |
| slug | `str \| None` | No |
| description | `str \| None` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| section_id | `int \| None \| NotGiven` | No |
| is_draft | `bool \| None` | No |
| price_cents | `int \| None` | No |
| currency | `str \| None` | No |
| minimum_purchase_quantity | `int \| None` | No |
| maximum_purchase_quantity | `int \| None \| NotGiven` | No |
| quantity_increment | `int \| None` | No |
| stock | `int \| None \| NotGiven` | No |
| payment_methods | `builtins.list[
            SdkReplaceCreditsProductRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| rate_tiers | `builtins.list[
            ReplaceCreditsProductRequestApplicationJsonPropertyRateTiersItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        title: str | None = None,
        slug: str | None = None,
        description: str | None = None,
        visibility: CatalogVisibility | str | None = None,
        section_id: int | None | NotGiven = NOT_GIVEN,
        is_draft: bool | None = None,
        price_cents: int | None = None,
        currency: str | None = None,
        minimum_purchase_quantity: int | None = None,
        maximum_purchase_quantity: int | None | NotGiven = NOT_GIVEN,
        quantity_increment: int | None = None,
        stock: int | None | NotGiven = NOT_GIVEN,
        payment_methods: builtins.list[
            SdkUpdateCreditsProductRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        rate_tiers: builtins.list[
            UpdateCreditsProductRequestApplicationJsonPropertyRateTiersItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCreditsProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| credit_product | `int` | Yes |
| title | `str \| None` | No |
| slug | `str \| None` | No |
| description | `str \| None` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| section_id | `int \| None \| NotGiven` | No |
| is_draft | `bool \| None` | No |
| price_cents | `int \| None` | No |
| currency | `str \| None` | No |
| minimum_purchase_quantity | `int \| None` | No |
| maximum_purchase_quantity | `int \| None \| NotGiven` | No |
| quantity_increment | `int \| None` | No |
| stock | `int \| None \| NotGiven` | No |
| payment_methods | `builtins.list[
            SdkUpdateCreditsProductRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| rate_tiers | `builtins.list[
            UpdateCreditsProductRequestApplicationJsonPropertyRateTiersItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| credit_product | `int` | Yes |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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

