# wallet

[All resources](../methods.md)

## list

List customer wallets

[API reference](https://sell.app/docs/api/wallet/list-customer-wallets) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListCustomerWalletsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListCustomerWalletsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet.list()
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

Retrieve a customer wallet

[API reference](https://sell.app/docs/api/wallet/retrieve-customer-wallet) · Effect: **read**

```python
def get(
        self,
        customer: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomerWalletResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetCustomerWalletResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet.get(customer=1)
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

## adjust

Adjust a customer wallet

[API reference](https://sell.app/docs/api/wallet/adjust-customer-wallet) · Effect: **consequential**

```python
def adjust(
        self,
        customer: int,
        *,
        amount_cents: int,
        idempotency_key: str,
        note: str,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkAdjustCustomerWalletResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| amount_cents | `int` | Yes |
| idempotency_key | `str` | Yes |
| note | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkAdjustCustomerWalletResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet.adjust(
    customer=1,
    amount_cents=2500,
    idempotency_key="wallet-adjustment-01992a65",
    note="Launch-day account credit"
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update_status

Update a customer wallet status

[API reference](https://sell.app/docs/api/wallet/update-wallet-status) · Effect: **consequential**

```python
def update_status(
        self,
        customer: int,
        *,
        status: Union[SdkUpdateCustomerWalletStatusRequestApplicationJsonStatus, str],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCustomerWalletStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| status | `Union[SdkUpdateCustomerWalletStatusRequestApplicationJsonStatus, str]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateCustomerWalletStatusResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet.update_status(
    customer=1,
    status="frozen"
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

