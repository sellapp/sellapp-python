# reward_coupon_templates

[All resources](../methods.md)

## list

List reward coupon templates

[API reference](https://sell.app/docs/api/reward-coupon-templates/list-reward-coupon-templates) · Effect: **read**

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
    ) -> SyncPage[SdkListRewardCouponTemplatesResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkListRewardCouponTemplatesResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_coupon_templates.list()
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

Create a reward coupon template

[API reference](https://sell.app/docs/api/reward-coupon-templates/create-a-reward-coupon-template) · Effect: **consequential**

```python
def create(
        self,
        *,
        name: str,
        type: SdkCreateRewardCouponTemplateRequestApplicationJsonType | str,
        discount: str | float,
        store_wide: bool,
        redemption_mode: SdkCreateRewardCouponTemplateRequestApplicationJsonRedemptionMode
        | str,
        is_active: bool,
        listing_ids: builtins.list[int],
        minimum_amount: str | float | None | NotGiven = NOT_GIVEN,
        maximum_discount_amount: str | float | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        expires_after_days: int | None | NotGiven = NOT_GIVEN,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateRewardCouponTemplateResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| type | `SdkCreateRewardCouponTemplateRequestApplicationJsonType \| str` | Yes |
| discount | `str \| float` | Yes |
| store_wide | `bool` | Yes |
| redemption_mode | `SdkCreateRewardCouponTemplateRequestApplicationJsonRedemptionMode
        \| str` | Yes |
| is_active | `bool` | Yes |
| listing_ids | `builtins.list[int]` | Yes |
| minimum_amount | `str \| float \| None \| NotGiven` | No |
| maximum_discount_amount | `str \| float \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| expires_after_days | `int \| None \| NotGiven` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateRewardCouponTemplateResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_coupon_templates.create(
    name="Launch Lab thank you",
    type="PERCENTAGE",
    discount="10.00",
    store_wide=True,
    redemption_mode="customer_locked",
    is_active=False,
    listing_ids=[]
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

Search reward coupon templates

[API reference](https://sell.app/docs/api/reward-coupon-templates/search-reward-coupon-templates) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[
            SearchRewardRulesRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchRewardRulesRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchRewardRulesRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchRewardRulesRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchRewardCouponTemplatesResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[
            SearchRewardRulesRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchRewardRulesRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchRewardRulesRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchRewardRulesRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkSearchRewardCouponTemplatesResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_coupon_templates.search(
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

## get

Retrieve a reward coupon template

[API reference](https://sell.app/docs/api/reward-coupon-templates/retrieve-a-reward-coupon-template) · Effect: **read**

```python
def get(
        self,
        reward_coupon_template: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetRewardCouponTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetRewardCouponTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_coupon_templates.get(reward_coupon_template=1)
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

Update a reward coupon template

[API reference](https://sell.app/docs/api/reward-coupon-templates/update-a-reward-coupon-template) · Effect: **consequential**

```python
def replace(
        self,
        reward_coupon_template: int,
        *,
        name: str | None = None,
        type: SdkReplaceRewardCouponTemplateRequestApplicationJsonType
        | str
        | None = None,
        discount: str | float | None = None,
        store_wide: bool | None = None,
        minimum_amount: str | float | None | NotGiven = NOT_GIVEN,
        maximum_discount_amount: str | float | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        expires_after_days: int | None | NotGiven = NOT_GIVEN,
        redemption_mode: SdkReplaceRewardCouponTemplateRequestApplicationJsonRedemptionMode
        | str
        | None = None,
        is_active: bool | None = None,
        listing_ids: builtins.list[int] | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceRewardCouponTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `int` | Yes |
| name | `str \| None` | No |
| type | `SdkReplaceRewardCouponTemplateRequestApplicationJsonType
        \| str
        \| None` | No |
| discount | `str \| float \| None` | No |
| store_wide | `bool \| None` | No |
| minimum_amount | `str \| float \| None \| NotGiven` | No |
| maximum_discount_amount | `str \| float \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| expires_after_days | `int \| None \| NotGiven` | No |
| redemption_mode | `SdkReplaceRewardCouponTemplateRequestApplicationJsonRedemptionMode
        \| str
        \| None` | No |
| is_active | `bool \| None` | No |
| listing_ids | `builtins.list[int] \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceRewardCouponTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_coupon_templates.replace(
    reward_coupon_template=1,
    is_active=False
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

Update a reward coupon template

[API reference](https://sell.app/docs/api/reward-coupon-templates/update-a-reward-coupon-template) · Effect: **consequential**

```python
def update(
        self,
        reward_coupon_template: int,
        *,
        name: str | None = None,
        type: SdkUpdateRewardCouponTemplateRequestApplicationJsonType
        | str
        | None = None,
        discount: str | float | None = None,
        store_wide: bool | None = None,
        minimum_amount: str | float | None | NotGiven = NOT_GIVEN,
        maximum_discount_amount: str | float | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        expires_after_days: int | None | NotGiven = NOT_GIVEN,
        redemption_mode: SdkUpdateRewardCouponTemplateRequestApplicationJsonRedemptionMode
        | str
        | None = None,
        is_active: bool | None = None,
        listing_ids: builtins.list[int] | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateRewardCouponTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `int` | Yes |
| name | `str \| None` | No |
| type | `SdkUpdateRewardCouponTemplateRequestApplicationJsonType
        \| str
        \| None` | No |
| discount | `str \| float \| None` | No |
| store_wide | `bool \| None` | No |
| minimum_amount | `str \| float \| None \| NotGiven` | No |
| maximum_discount_amount | `str \| float \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| expires_after_days | `int \| None \| NotGiven` | No |
| redemption_mode | `SdkUpdateRewardCouponTemplateRequestApplicationJsonRedemptionMode
        \| str
        \| None` | No |
| is_active | `bool \| None` | No |
| listing_ids | `builtins.list[int] \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateRewardCouponTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_coupon_templates.update(
    reward_coupon_template=1,
    is_active=False
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

