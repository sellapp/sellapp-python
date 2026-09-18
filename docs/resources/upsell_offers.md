# upsell_offers

[All resources](../methods.md)

## list

List upsell offers

[API reference](https://sell.app/docs/api/products) · Effect: **read**

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
    ) -> SyncPage[SdkListUpsellOffersResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkListUpsellOffersResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.upsell_offers.list()
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

Create an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```python
def create(
        self,
        *,
        name: str,
        is_active: bool,
        source_listing_id: int,
        items: builtins.list[CreateUpsellOfferRequestApplicationJsonPropertyItemsItem],
        description: str | None | NotGiven = NOT_GIVEN,
        source_variant_id: int | None | NotGiven = NOT_GIVEN,
        minimum_order_total_usd_cents: int | None | NotGiven = NOT_GIVEN,
        maximum_order_total_usd_cents: int | None | NotGiven = NOT_GIVEN,
        starts_at: str | None | NotGiven = NOT_GIVEN,
        ends_at: str | None | NotGiven = NOT_GIVEN,
        available_for_days: int | None | NotGiven = NOT_GIVEN,
        max_accepts_per_customer: int | None | NotGiven = NOT_GIVEN,
        expected_version: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateUpsellOfferResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| is_active | `bool` | Yes |
| source_listing_id | `int` | Yes |
| items | `builtins.list[CreateUpsellOfferRequestApplicationJsonPropertyItemsItem]` | Yes |
| description | `str \| None \| NotGiven` | No |
| source_variant_id | `int \| None \| NotGiven` | No |
| minimum_order_total_usd_cents | `int \| None \| NotGiven` | No |
| maximum_order_total_usd_cents | `int \| None \| NotGiven` | No |
| starts_at | `str \| None \| NotGiven` | No |
| ends_at | `str \| None \| NotGiven` | No |
| available_for_days | `int \| None \| NotGiven` | No |
| max_accepts_per_customer | `int \| None \| NotGiven` | No |
| expected_version | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateUpsellOfferResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.upsell_offers.create(
    name="One More Feature",
    description="Offer the advanced package with additional resources.",
    is_active=True,
    source_listing_id=120,
    source_variant_id=880,
    minimum_order_total_usd_cents=1000,
    maximum_order_total_usd_cents=25000,
    available_for_days=14,
    max_accepts_per_customer=1,
    items=[
        {
            "target_listing_id": 121,
            "target_variant_id": 881,
            "headline": "Upgrade today",
            "description": "Unlock dark mode, webhooks, and the premium launch checklist.",
            "discount_type": "percentage",
            "discount_value": "15.00",
            "maximum_discount_amount": "25.00"
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search upsell offers

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[
            SearchUpsellOffersRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchUpsellOffersRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchUpsellOffersRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchUpsellOffersRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchUpsellOffersResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[
            SearchUpsellOffersRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchUpsellOffersRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchUpsellOffersRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchUpsellOffersRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkSearchUpsellOffersResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.upsell_offers.search(
    filters=[{"field": "id", "operator": "=", "value": 71}],
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

Retrieve an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```python
def get(
        self,
        upsell_offer: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetUpsellOfferResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetUpsellOfferResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.upsell_offers.get(upsell_offer=71)
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

Update an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```python
def replace(
        self,
        upsell_offer: int,
        *,
        expected_version: int,
        name: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        source_listing_id: int | None = None,
        source_variant_id: int | None | NotGiven = NOT_GIVEN,
        minimum_order_total_usd_cents: int | None | NotGiven = NOT_GIVEN,
        maximum_order_total_usd_cents: int | None | NotGiven = NOT_GIVEN,
        starts_at: str | None | NotGiven = NOT_GIVEN,
        ends_at: str | None | NotGiven = NOT_GIVEN,
        available_for_days: int | None | NotGiven = NOT_GIVEN,
        max_accepts_per_customer: int | None | NotGiven = NOT_GIVEN,
        items: builtins.list[ReplaceUpsellOfferRequestApplicationJsonPropertyItemsItem]
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceUpsellOfferResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `int` | Yes |
| expected_version | `int` | Yes |
| name | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| source_listing_id | `int \| None` | No |
| source_variant_id | `int \| None \| NotGiven` | No |
| minimum_order_total_usd_cents | `int \| None \| NotGiven` | No |
| maximum_order_total_usd_cents | `int \| None \| NotGiven` | No |
| starts_at | `str \| None \| NotGiven` | No |
| ends_at | `str \| None \| NotGiven` | No |
| available_for_days | `int \| None \| NotGiven` | No |
| max_accepts_per_customer | `int \| None \| NotGiven` | No |
| items | `builtins.list[ReplaceUpsellOfferRequestApplicationJsonPropertyItemsItem]
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceUpsellOfferResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.upsell_offers.replace(
    upsell_offer=71,
    name="One More Feature 2.0",
    is_active=False,
    expected_version=1
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

Update an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```python
def update(
        self,
        upsell_offer: int,
        *,
        expected_version: int,
        name: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        source_listing_id: int | None = None,
        source_variant_id: int | None | NotGiven = NOT_GIVEN,
        minimum_order_total_usd_cents: int | None | NotGiven = NOT_GIVEN,
        maximum_order_total_usd_cents: int | None | NotGiven = NOT_GIVEN,
        starts_at: str | None | NotGiven = NOT_GIVEN,
        ends_at: str | None | NotGiven = NOT_GIVEN,
        available_for_days: int | None | NotGiven = NOT_GIVEN,
        max_accepts_per_customer: int | None | NotGiven = NOT_GIVEN,
        items: builtins.list[UpdateUpsellOfferRequestApplicationJsonPropertyItemsItem]
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateUpsellOfferResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `int` | Yes |
| expected_version | `int` | Yes |
| name | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| source_listing_id | `int \| None` | No |
| source_variant_id | `int \| None \| NotGiven` | No |
| minimum_order_total_usd_cents | `int \| None \| NotGiven` | No |
| maximum_order_total_usd_cents | `int \| None \| NotGiven` | No |
| starts_at | `str \| None \| NotGiven` | No |
| ends_at | `str \| None \| NotGiven` | No |
| available_for_days | `int \| None \| NotGiven` | No |
| max_accepts_per_customer | `int \| None \| NotGiven` | No |
| items | `builtins.list[UpdateUpsellOfferRequestApplicationJsonPropertyItemsItem]
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateUpsellOfferResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.upsell_offers.update(
    upsell_offer=71,
    name="One More Feature 2.0",
    is_active=False,
    expected_version=1
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

Delete an upsell offer

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```python
def delete(
        self,
        upsell_offer: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.upsell_offers.delete(upsell_offer=71)
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

