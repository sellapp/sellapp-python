# charges

[All resources](../methods.md)

## list

List all charges

[API reference](https://sell.app/docs/api/charges/list-all-charges) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListChargesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListChargesResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.charges.list()
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

Create a charge

[API reference](https://sell.app/docs/api/charges/create-a-charge) · Effect: **consequential**

```python
def create(
        self,
        *,
        email: str,
        return_url: str,
        cancel_url: str | None | NotGiven = NOT_GIVEN,
        webhook: str | None | NotGiven = NOT_GIVEN,
        reference: str | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        currency: str | None = None,
        total: int | None = None,
        payment_method: SdkCreateChargeRequestApplicationJsonPaymentMethod
        | str
        | None = None,
        payment_methods: builtins.list[
            SdkCreateChargeRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        custom_payment_method_id: str | None | NotGiven = NOT_GIVEN,
        custom_payment_method_ids: builtins.list[str] | None = None,
        use_all_payment_methods: bool | None = None,
        deliverable: CreateChargeRequestApplicationJsonPropertyDeliverable
        | None = None,
        metadata: CreateChargeRequestApplicationJsonPropertyMetadata | None = None,
        coupon_code: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateChargeResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str` | Yes |
| return_url | `str` | Yes |
| cancel_url | `str \| None \| NotGiven` | No |
| webhook | `str \| None \| NotGiven` | No |
| reference | `str \| None \| NotGiven` | No |
| description | `str \| None \| NotGiven` | No |
| currency | `str \| None` | No |
| total | `int \| None` | No |
| payment_method | `SdkCreateChargeRequestApplicationJsonPaymentMethod
        \| str
        \| None` | No |
| payment_methods | `builtins.list[
            SdkCreateChargeRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| custom_payment_method_id | `str \| None \| NotGiven` | No |
| custom_payment_method_ids | `builtins.list[str] \| None` | No |
| use_all_payment_methods | `bool \| None` | No |
| deliverable | `CreateChargeRequestApplicationJsonPropertyDeliverable
        \| None` | No |
| metadata | `CreateChargeRequestApplicationJsonPropertyMetadata \| None` | No |
| coupon_code | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateChargeResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.charges.create(
    email="sofia.rivera@example.com",
    return_url="https://example.com/launch-complete",
    reference="One more thing launch",
    currency="USD",
    total=10000,
    payment_method="PAYPAL"
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

## get

Retrieve a charge

[API reference](https://sell.app/docs/api/charges/retrieve-a-charge) · Effect: **read**

```python
def get(
        self,
        charge: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetChargeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetChargeResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.charges.get(charge=1)
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

## mark_completed

Mark pending charge completed

[API reference](https://sell.app/docs/api/charges/mark-pending-charge-completed) · Effect: **consequential**

```python
def mark_completed(
        self,
        charge_id: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkMarkPendingChargeCompletedResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge_id | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkMarkPendingChargeCompletedResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.charges.mark_completed(charge_id=1)
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

## mark_voided

Mark pending charge voided

[API reference](https://sell.app/docs/api/charges/mark-pending-charge-voided) · Effect: **consequential**

```python
def mark_voided(
        self,
        charge_id: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkMarkPendingChargeVoidedResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge_id | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkMarkPendingChargeVoidedResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.charges.mark_voided(charge_id=1)
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

