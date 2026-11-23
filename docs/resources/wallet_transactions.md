# wallet_transactions

[All resources](../methods.md)

## reverse

Reverse a wallet transaction

[API reference](https://sell.app/docs/api/wallet/reverse-wallet-transaction) · Effect: **consequential**

```python
def reverse(
        self,
        customer: int,
        transaction: int,
        *,
        note: str,
        expected_balance_cents: int | None = None,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReverseWalletTransactionResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| transaction | `int` | Yes |
| note | `str` | Yes |
| expected_balance_cents | `int \| None` | No |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReverseWalletTransactionResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_transactions.reverse(
    customer=42,
    transaction=501,
    note="Credit went to the wrong customer",
    expected_balance_cents=2500
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

## list

List wallet transactions

[API reference](https://sell.app/docs/api/wallet/retrieve-customer-wallet) · Effect: **read**

```python
def list(
        self,
        customer: int,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        ListWalletTransactionsResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        ListWalletTransactionsResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_transactions.list(customer=42)
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

