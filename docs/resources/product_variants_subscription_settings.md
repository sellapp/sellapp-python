# product_variants_subscription_settings

[All resources](../methods.md)

## get

Retrieve variant subscription settings

[API reference](https://sell.app/docs/api/product-variants/variant-subscription-settings) · Effect: **read**

```python
def get(
        self,
        product: int,
        variant: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetVariantSubscriptionSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetVariantSubscriptionSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_subscription_settings.get(
    product=1,
    variant=4
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

Update variant subscription settings

[API reference](https://sell.app/docs/api/product-variants/variant-subscription-settings) · Effect: **write**

```python
def update(
        self,
        product: int,
        variant: int,
        *,
        pause_policy: UpdateVariantSubscriptionSettingsRequestApplicationJsonPropertyPausePolicy
        | None = None,
        billing_date_policy: UpdateVariantSubscriptionSettingsRequestApplicationJsonPropertyBillingDatePolicy
        | None = None,
        renewal_policy: UpdateVariantSubscriptionSettingsRequestApplicationJsonPropertyRenewalPolicy
        | None = None,
        expected_state: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateVariantSubscriptionSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| pause_policy | `UpdateVariantSubscriptionSettingsRequestApplicationJsonPropertyPausePolicy
        \| None` | No |
| billing_date_policy | `UpdateVariantSubscriptionSettingsRequestApplicationJsonPropertyBillingDatePolicy
        \| None` | No |
| renewal_policy | `UpdateVariantSubscriptionSettingsRequestApplicationJsonPropertyRenewalPolicy
        \| None` | No |
| expected_state | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateVariantSubscriptionSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_subscription_settings.update(
    product=1,
    variant=4,
    pause_policy={"max_pause_days": 30},
    renewal_policy={"redeliver_on_renewal": False},
    expected_state="3f9a1c0e7b2d4a6f8e1c5b9d0a7f3e2c4b6d8a0f1e3c5a7b9d2f4e6a8c0b1d3e"
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

