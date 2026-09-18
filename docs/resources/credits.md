# credits

[All resources](../methods.md)

## record

Record a credit transaction

[API reference](https://sell.app/docs/api/credits/record-a-credit-transaction) · Effect: **consequential**

```python
def record(
        self,
        *,
        customer_id: int,
        product_id: int,
        kind: SdkRecordCreditTransactionRequestApplicationJsonKind | str,
        amount_units: int,
        idempotency_key: str,
        reason: str | None | NotGiven = NOT_GIVEN,
        source_type: str | None | NotGiven = NOT_GIVEN,
        source_id: str | None | NotGiven = NOT_GIVEN,
        metadata: RecordCreditTransactionRequestApplicationJsonPropertyMetadata
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkRecordCreditTransactionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer_id | `int` | Yes |
| product_id | `int` | Yes |
| kind | `SdkRecordCreditTransactionRequestApplicationJsonKind \| str` | Yes |
| amount_units | `int` | Yes |
| idempotency_key | `str` | Yes |
| reason | `str \| None \| NotGiven` | No |
| source_type | `str \| None \| NotGiven` | No |
| source_id | `str \| None \| NotGiven` | No |
| metadata | `RecordCreditTransactionRequestApplicationJsonPropertyMetadata
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkRecordCreditTransactionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.credits.record(
    customer_id=125,
    product_id=120,
    kind="grant",
    amount_units=1000,
    idempotency_key="credits-grant-01992a65",
    reason="Launch cohort allocation"
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

Documented HTTP responses: 200, 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

