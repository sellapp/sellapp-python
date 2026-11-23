# tickets_wallet_refunds

[All resources](../methods.md)

## list_options

List a ticket's wallet refund options

[API reference](https://sell.app/docs/api/tickets/list-ticket-wallet-refund-options) · Effect: **read**

```python
def list_options(
        self,
        ticket: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkV2ListTicketWalletRefundOptionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2ListTicketWalletRefundOptionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_wallet_refunds.list_options(ticket=312)
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

## list

List a ticket's wallet refunds

[API reference](https://sell.app/docs/api/tickets/list-ticket-wallet-refunds) · Effect: **read**

```python
def list(
        self,
        ticket: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkV2ListTicketWalletRefundsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2ListTicketWalletRefundsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_wallet_refunds.list(ticket=312)
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

## create

Refund a ticket to the customer's wallet

[API reference](https://sell.app/docs/api/tickets/refund-ticket-to-wallet) · Effect: **consequential**

```python
def create(
        self,
        ticket: int,
        *,
        invoice_id: int,
        amount_cents: int,
        expected_refundable_cents: int,
        customer_note: str,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkV2RefundTicketToWalletResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| invoice_id | `int` | Yes |
| amount_cents | `int` | Yes |
| expected_refundable_cents | `int` | Yes |
| customer_note | `str` | Yes |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2RefundTicketToWalletResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_wallet_refunds.create(
    ticket=312,
    invoice_id=5120,
    amount_cents=500,
    expected_refundable_cents=1999,
    customer_note="We added $5.00 to your store wallet for the trouble with your download link.",
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

## reverse

Reverse a ticket's wallet refund

[API reference](https://sell.app/docs/api/tickets/reverse-ticket-wallet-refund) · Effect: **consequential**

```python
def reverse(
        self,
        ticket: int,
        wallet_refund: int,
        *,
        reason: str,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkV2ReverseTicketWalletRefundResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| wallet_refund | `int` | Yes |
| reason | `str` | Yes |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2ReverseTicketWalletRefundResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_wallet_refunds.reverse(
    ticket=312,
    wallet_refund=7001,
    reason="Issued on the wrong ticket."
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

