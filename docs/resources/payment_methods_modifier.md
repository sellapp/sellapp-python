# payment_methods_modifier

[All resources](../methods.md)

## get

Retrieve a payment method modifier

[API reference](https://sell.app/docs/api/payment-methods/payment-method-modifier) · Effect: **read**

```python
def get(
        self,
        payment_method: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetPaymentMethodModifierResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetPaymentMethodModifierResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods_modifier.get(payment_method="STRIPE")
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

Update a payment method modifier

[API reference](https://sell.app/docs/api/payment-methods/payment-method-modifier) · Effect: **consequential**

```python
def replace(
        self,
        payment_method: str,
        *,
        kind: SdkReplacePaymentMethodModifierRequestApplicationJsonKind | str,
        percentage: str | None,
        fixed_amount: str | None,
        condition: Condition | str | None | NotGiven = NOT_GIVEN,
        threshold: float | str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplacePaymentMethodModifierResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `str` | Yes |
| kind | `SdkReplacePaymentMethodModifierRequestApplicationJsonKind \| str` | Yes |
| percentage | `str \| None` | Yes |
| fixed_amount | `str \| None` | Yes |
| condition | `Condition \| str \| None \| NotGiven` | No |
| threshold | `float \| str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplacePaymentMethodModifierResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods_modifier.replace(
    payment_method="STRIPE",
    kind="fee",
    percentage="3.00",
    fixed_amount="0.30",
    condition="below",
    threshold="20.00"
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

