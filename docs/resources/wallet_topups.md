# wallet_topups

[All resources](../methods.md)

## create

Create a wallet top-up payment link

[API reference](https://sell.app/docs/api/wallet/create-wallet-top-up) · Effect: **consequential**

```python
def create(
        self,
        customer: int,
        *,
        amount_cents: int,
        payment_method: Union[
            SdkCreateWalletTopUpRequestApplicationJsonPaymentMethod, str
        ],
        custom_payment_method_id: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateWalletTopUpResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| amount_cents | `int` | Yes |
| payment_method | `Union[
            SdkCreateWalletTopUpRequestApplicationJsonPaymentMethod, str
        ]` | Yes |
| custom_payment_method_id | `Union[str, None, NotGiven]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateWalletTopUpResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_topups.create(
    customer=42,
    amount_cents=2500,
    payment_method="STRIPE",
    idempotency_key="example-mutation-001"
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

