# upsell_offers

[All resources](../methods.md)

## list

List upsell offers

[API reference](https://sell.app/docs/api/products) · Effect: **read**

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
    ) -> SyncPage[SdkListUpsellOffersResponseValue200ApplicationJson]:
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
        items: List[CreateUpsellOfferRequestApplicationJsonPropertyItemsItem],
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        source_variant_id: Union[int, None, NotGiven] = NOT_GIVEN,
        minimum_order_total_usd_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        maximum_order_total_usd_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        starts_at: Union[str, None, NotGiven] = NOT_GIVEN,
        ends_at: Union[str, None, NotGiven] = NOT_GIVEN,
        available_for_days: Union[int, None, NotGiven] = NOT_GIVEN,
        max_accepts_per_customer: Union[int, None, NotGiven] = NOT_GIVEN,
        expected_version: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateUpsellOfferResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| is_active | `bool` | Yes |
| source_listing_id | `int` | Yes |
| items | `List[CreateUpsellOfferRequestApplicationJsonPropertyItemsItem]` | Yes |
| description | `Union[str, None, NotGiven]` | No |
| source_variant_id | `Union[int, None, NotGiven]` | No |
| minimum_order_total_usd_cents | `Union[int, None, NotGiven]` | No |
| maximum_order_total_usd_cents | `Union[int, None, NotGiven]` | No |
| starts_at | `Union[str, None, NotGiven]` | No |
| ends_at | `Union[str, None, NotGiven]` | No |
| available_for_days | `Union[int, None, NotGiven]` | No |
| max_accepts_per_customer | `Union[int, None, NotGiven]` | No |
| expected_version | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchUpsellOffersRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchUpsellOffersRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchUpsellOffersRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchUpsellOffersRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchUpsellOffersResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchUpsellOffersRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchUpsellOffersRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchUpsellOffersRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchUpsellOffersRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetUpsellOfferResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Optional[str] = None,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        is_active: Optional[bool] = None,
        source_listing_id: Optional[int] = None,
        source_variant_id: Union[int, None, NotGiven] = NOT_GIVEN,
        minimum_order_total_usd_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        maximum_order_total_usd_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        starts_at: Union[str, None, NotGiven] = NOT_GIVEN,
        ends_at: Union[str, None, NotGiven] = NOT_GIVEN,
        available_for_days: Union[int, None, NotGiven] = NOT_GIVEN,
        max_accepts_per_customer: Union[int, None, NotGiven] = NOT_GIVEN,
        items: Optional[
            List[ReplaceUpsellOfferRequestApplicationJsonPropertyItemsItem]
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceUpsellOfferResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `int` | Yes |
| expected_version | `int` | Yes |
| name | `Optional[str]` | No |
| description | `Union[str, None, NotGiven]` | No |
| is_active | `Optional[bool]` | No |
| source_listing_id | `Optional[int]` | No |
| source_variant_id | `Union[int, None, NotGiven]` | No |
| minimum_order_total_usd_cents | `Union[int, None, NotGiven]` | No |
| maximum_order_total_usd_cents | `Union[int, None, NotGiven]` | No |
| starts_at | `Union[str, None, NotGiven]` | No |
| ends_at | `Union[str, None, NotGiven]` | No |
| available_for_days | `Union[int, None, NotGiven]` | No |
| max_accepts_per_customer | `Union[int, None, NotGiven]` | No |
| items | `Optional[
            List[ReplaceUpsellOfferRequestApplicationJsonPropertyItemsItem]
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Optional[str] = None,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        is_active: Optional[bool] = None,
        source_listing_id: Optional[int] = None,
        source_variant_id: Union[int, None, NotGiven] = NOT_GIVEN,
        minimum_order_total_usd_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        maximum_order_total_usd_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        starts_at: Union[str, None, NotGiven] = NOT_GIVEN,
        ends_at: Union[str, None, NotGiven] = NOT_GIVEN,
        available_for_days: Union[int, None, NotGiven] = NOT_GIVEN,
        max_accepts_per_customer: Union[int, None, NotGiven] = NOT_GIVEN,
        items: Optional[
            List[UpdateUpsellOfferRequestApplicationJsonPropertyItemsItem]
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateUpsellOfferResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `int` | Yes |
| expected_version | `int` | Yes |
| name | `Optional[str]` | No |
| description | `Union[str, None, NotGiven]` | No |
| is_active | `Optional[bool]` | No |
| source_listing_id | `Optional[int]` | No |
| source_variant_id | `Union[int, None, NotGiven]` | No |
| minimum_order_total_usd_cents | `Union[int, None, NotGiven]` | No |
| maximum_order_total_usd_cents | `Union[int, None, NotGiven]` | No |
| starts_at | `Union[str, None, NotGiven]` | No |
| ends_at | `Union[str, None, NotGiven]` | No |
| available_for_days | `Union[int, None, NotGiven]` | No |
| max_accepts_per_customer | `Union[int, None, NotGiven]` | No |
| items | `Optional[
            List[UpdateUpsellOfferRequestApplicationJsonPropertyItemsItem]
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| upsell_offer | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

