# reward_coupon_templates

[All resources](../methods.md)

## list

List reward coupon templates

[API reference](https://sell.app/docs/api/reward-coupon-templates/list-reward-coupon-templates) · Effect: **read**

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
    ) -> SyncPage[SdkListRewardCouponTemplatesResponseValue200ApplicationJson]:
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
        type: Union[SdkCreateRewardCouponTemplateRequestApplicationJsonType, str],
        discount: Union[str, float],
        store_wide: bool,
        redemption_mode: Union[
            SdkCreateRewardCouponTemplateRequestApplicationJsonRedemptionMode, str
        ],
        is_active: bool,
        listing_ids: List[int],
        minimum_amount: Union[Union[str, float], None, NotGiven] = NOT_GIVEN,
        maximum_discount_amount: Union[Union[str, float], None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        expires_after_days: Union[int, None, NotGiven] = NOT_GIVEN,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateRewardCouponTemplateResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| type | `Union[SdkCreateRewardCouponTemplateRequestApplicationJsonType, str]` | Yes |
| discount | `Union[str, float]` | Yes |
| store_wide | `bool` | Yes |
| redemption_mode | `Union[
            SdkCreateRewardCouponTemplateRequestApplicationJsonRedemptionMode, str
        ]` | Yes |
| is_active | `bool` | Yes |
| listing_ids | `List[int]` | Yes |
| minimum_amount | `Union[Union[str, float], None, NotGiven]` | No |
| maximum_discount_amount | `Union[Union[str, float], None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| expires_after_days | `Union[int, None, NotGiven]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchRewardRulesRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchRewardCouponTemplatesResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchRewardRulesRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetRewardCouponTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Optional[str] = None,
        type: Optional[
            Union[SdkReplaceRewardCouponTemplateRequestApplicationJsonType, str]
        ] = None,
        discount: Optional[Union[str, float]] = None,
        store_wide: Optional[bool] = None,
        minimum_amount: Union[Union[str, float], None, NotGiven] = NOT_GIVEN,
        maximum_discount_amount: Union[Union[str, float], None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        expires_after_days: Union[int, None, NotGiven] = NOT_GIVEN,
        redemption_mode: Optional[
            Union[
                SdkReplaceRewardCouponTemplateRequestApplicationJsonRedemptionMode, str
            ]
        ] = None,
        is_active: Optional[bool] = None,
        listing_ids: Optional[List[int]] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceRewardCouponTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `int` | Yes |
| name | `Optional[str]` | No |
| type | `Optional[
            Union[SdkReplaceRewardCouponTemplateRequestApplicationJsonType, str]
        ]` | No |
| discount | `Optional[Union[str, float]]` | No |
| store_wide | `Optional[bool]` | No |
| minimum_amount | `Union[Union[str, float], None, NotGiven]` | No |
| maximum_discount_amount | `Union[Union[str, float], None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| expires_after_days | `Union[int, None, NotGiven]` | No |
| redemption_mode | `Optional[
            Union[
                SdkReplaceRewardCouponTemplateRequestApplicationJsonRedemptionMode, str
            ]
        ]` | No |
| is_active | `Optional[bool]` | No |
| listing_ids | `Optional[List[int]]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Optional[str] = None,
        type: Optional[
            Union[SdkUpdateRewardCouponTemplateRequestApplicationJsonType, str]
        ] = None,
        discount: Optional[Union[str, float]] = None,
        store_wide: Optional[bool] = None,
        minimum_amount: Union[Union[str, float], None, NotGiven] = NOT_GIVEN,
        maximum_discount_amount: Union[Union[str, float], None, NotGiven] = NOT_GIVEN,
        expires_at: Union[str, None, NotGiven] = NOT_GIVEN,
        expires_after_days: Union[int, None, NotGiven] = NOT_GIVEN,
        redemption_mode: Optional[
            Union[
                SdkUpdateRewardCouponTemplateRequestApplicationJsonRedemptionMode, str
            ]
        ] = None,
        is_active: Optional[bool] = None,
        listing_ids: Optional[List[int]] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateRewardCouponTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_coupon_template | `int` | Yes |
| name | `Optional[str]` | No |
| type | `Optional[
            Union[SdkUpdateRewardCouponTemplateRequestApplicationJsonType, str]
        ]` | No |
| discount | `Optional[Union[str, float]]` | No |
| store_wide | `Optional[bool]` | No |
| minimum_amount | `Union[Union[str, float], None, NotGiven]` | No |
| maximum_discount_amount | `Union[Union[str, float], None, NotGiven]` | No |
| expires_at | `Union[str, None, NotGiven]` | No |
| expires_after_days | `Union[int, None, NotGiven]` | No |
| redemption_mode | `Optional[
            Union[
                SdkUpdateRewardCouponTemplateRequestApplicationJsonRedemptionMode, str
            ]
        ]` | No |
| is_active | `Optional[bool]` | No |
| listing_ids | `Optional[List[int]]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

