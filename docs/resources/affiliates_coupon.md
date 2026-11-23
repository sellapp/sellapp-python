# affiliates_coupon

[All resources](../methods.md)

## get

Retrieve an affiliate coupon

[API reference](https://sell.app/docs/api/affiliates/affiliate-coupon) · Effect: **read**

```python
def get(
        self,
        affiliate: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetAffiliateCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetAffiliateCouponResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliates_coupon.get(affiliate=88)
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

## save

Save an affiliate coupon

[API reference](https://sell.app/docs/api/affiliates/affiliate-coupon) · Effect: **consequential**

```python
def save(
        self,
        affiliate: int,
        *,
        code: str | None = None,
        type: SdkSaveAffiliateCouponRequestApplicationJsonType | str | None = None,
        discount: float | str | None = None,
        store_wide: bool | None = None,
        products: list[int] | None = None,
        product_variants: list[int] | None = None,
        limit: int | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        minimum_amount: float | str | None | NotGiven = NOT_GIVEN,
        applies_to: SdkSaveAffiliateCouponRequestApplicationJsonAppliesTo
        | str
        | None = None,
        subscription_payments: int | None | NotGiven = NOT_GIVEN,
        maximum_discount_amount: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkSaveAffiliateCouponResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `int` | Yes |
| code | `str \| None` | No |
| type | `SdkSaveAffiliateCouponRequestApplicationJsonType \| str \| None` | No |
| discount | `float \| str \| None` | No |
| store_wide | `bool \| None` | No |
| products | `list[int] \| None` | No |
| product_variants | `list[int] \| None` | No |
| limit | `int \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| minimum_amount | `float \| str \| None \| NotGiven` | No |
| applies_to | `SdkSaveAffiliateCouponRequestApplicationJsonAppliesTo
        \| str
        \| None` | No |
| subscription_payments | `int \| None \| NotGiven` | No |
| maximum_discount_amount | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkSaveAffiliateCouponResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliates_coupon.save(
    affiliate=88,
    code="ALEX15",
    type="PERCENTAGE",
    discount="15",
    store_wide=True,
    maximum_discount_amount="20"
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

## disable

Disable an affiliate coupon

[API reference](https://sell.app/docs/api/affiliates/affiliate-coupon) · Effect: **consequential**

```python
def disable(
        self,
        affiliate: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliates_coupon.disable(affiliate=88)
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

