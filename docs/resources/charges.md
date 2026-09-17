# charges

[All resources](../methods.md)

## list

List all charges

[API reference](https://sell.app/docs/api/charges/list-all-charges) · Effect: **read**

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
    ) -> SyncPage[ListChargesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        cancel_url: Union[str, None, NotGiven] = NOT_GIVEN,
        webhook: Union[str, None, NotGiven] = NOT_GIVEN,
        reference: Union[str, None, NotGiven] = NOT_GIVEN,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        currency: Optional[str] = None,
        total: Optional[int] = None,
        payment_method: Optional[
            Union[SdkCreateChargeRequestApplicationJsonPaymentMethod, str]
        ] = None,
        payment_methods: Optional[
            List[Union[SdkCreateChargeRequestApplicationJsonPaymentMethods, str]]
        ] = None,
        custom_payment_method_id: Union[str, None, NotGiven] = NOT_GIVEN,
        custom_payment_method_ids: Optional[List[str]] = None,
        use_all_payment_methods: Optional[bool] = None,
        deliverable: Optional[
            CreateChargeRequestApplicationJsonPropertyDeliverable
        ] = None,
        metadata: Optional[CreateChargeRequestApplicationJsonPropertyMetadata] = None,
        coupon_code: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateChargeResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str` | Yes |
| return_url | `str` | Yes |
| cancel_url | `Union[str, None, NotGiven]` | No |
| webhook | `Union[str, None, NotGiven]` | No |
| reference | `Union[str, None, NotGiven]` | No |
| description | `Union[str, None, NotGiven]` | No |
| currency | `Optional[str]` | No |
| total | `Optional[int]` | No |
| payment_method | `Optional[
            Union[SdkCreateChargeRequestApplicationJsonPaymentMethod, str]
        ]` | No |
| payment_methods | `Optional[
            List[Union[SdkCreateChargeRequestApplicationJsonPaymentMethods, str]]
        ]` | No |
| custom_payment_method_id | `Union[str, None, NotGiven]` | No |
| custom_payment_method_ids | `Optional[List[str]]` | No |
| use_all_payment_methods | `Optional[bool]` | No |
| deliverable | `Optional[
            CreateChargeRequestApplicationJsonPropertyDeliverable
        ]` | No |
| metadata | `Optional[CreateChargeRequestApplicationJsonPropertyMetadata]` | No |
| coupon_code | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetChargeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkMarkPendingChargeCompletedResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge_id | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkMarkPendingChargeVoidedResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| charge_id | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

