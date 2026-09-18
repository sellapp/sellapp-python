# payment_methods_custom

[All resources](../methods.md)

## list

List custom payment methods

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **read**

```python
def list(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkListCustomPaymentMethodsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListCustomPaymentMethodsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods_custom.list()
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

Create a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **consequential**

```python
def create(
        self,
        *,
        type: SdkCreateCustomPaymentMethodRequestApplicationJsonType | str,
        name: str,
        description: str | None | NotGiven = NOT_GIVEN,
        instructions: str | None | NotGiven = NOT_GIVEN,
        steps: builtins.list[str | None] | None | NotGiven = NOT_GIVEN,
        redirect_url: str | None | NotGiven = NOT_GIVEN,
        skip_interstitial_page: bool | None = None,
        show_processing_status_page: bool | None = None,
        require_proof_of_payment: bool | None = None,
        enabled: bool | None = None,
        sort_order: int | None = None,
        modifier: CreateCustomPaymentMethodRequestApplicationJsonPropertyModifier
        | None
        | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateCustomPaymentMethodResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| type | `SdkCreateCustomPaymentMethodRequestApplicationJsonType \| str` | Yes |
| name | `str` | Yes |
| description | `str \| None \| NotGiven` | No |
| instructions | `str \| None \| NotGiven` | No |
| steps | `builtins.list[str \| None] \| None \| NotGiven` | No |
| redirect_url | `str \| None \| NotGiven` | No |
| skip_interstitial_page | `bool \| None` | No |
| show_processing_status_page | `bool \| None` | No |
| require_proof_of_payment | `bool \| None` | No |
| enabled | `bool \| None` | No |
| sort_order | `int \| None` | No |
| modifier | `CreateCustomPaymentMethodRequestApplicationJsonPropertyModifier
        \| None
        \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateCustomPaymentMethodResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods_custom.create(
    type="instructions",
    name="Manual payment",
    instructions="Contact Launch Lab before sending a payment.",
    enabled=False,
    modifier={"percentage": "-2.50", "fixed": "-1.00"}
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

Retrieve a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **read**

```python
def get(
        self,
        custom_payment_method: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCustomPaymentMethodResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCustomPaymentMethodResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods_custom.get(custom_payment_method="string_example")
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

Replace a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **consequential**

```python
def replace(
        self,
        custom_payment_method: str,
        *,
        type: SdkReplaceCustomPaymentMethodRequestApplicationJsonType | str,
        name: str,
        description: str | None | NotGiven = NOT_GIVEN,
        instructions: str | None | NotGiven = NOT_GIVEN,
        steps: builtins.list[str | None] | None | NotGiven = NOT_GIVEN,
        redirect_url: str | None | NotGiven = NOT_GIVEN,
        skip_interstitial_page: bool | None = None,
        show_processing_status_page: bool | None = None,
        require_proof_of_payment: bool | None = None,
        enabled: bool | None = None,
        sort_order: int | None = None,
        modifier: ReplaceCustomPaymentMethodRequestApplicationJsonPropertyModifier
        | None
        | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCustomPaymentMethodResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `str` | Yes |
| type | `SdkReplaceCustomPaymentMethodRequestApplicationJsonType \| str` | Yes |
| name | `str` | Yes |
| description | `str \| None \| NotGiven` | No |
| instructions | `str \| None \| NotGiven` | No |
| steps | `builtins.list[str \| None] \| None \| NotGiven` | No |
| redirect_url | `str \| None \| NotGiven` | No |
| skip_interstitial_page | `bool \| None` | No |
| show_processing_status_page | `bool \| None` | No |
| require_proof_of_payment | `bool \| None` | No |
| enabled | `bool \| None` | No |
| sort_order | `int \| None` | No |
| modifier | `ReplaceCustomPaymentMethodRequestApplicationJsonPropertyModifier
        \| None
        \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceCustomPaymentMethodResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods_custom.replace(
    custom_payment_method="string_example",
    type="instructions",
    name="Manual payment",
    instructions="Contact Launch Lab before sending a payment.",
    enabled=False
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

Update a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **consequential**

```python
def update(
        self,
        custom_payment_method: str,
        *,
        type: SdkUpdateCustomPaymentMethodRequestApplicationJsonType
        | str
        | None = None,
        name: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        instructions: str | None | NotGiven = NOT_GIVEN,
        steps: builtins.list[str | None] | None | NotGiven = NOT_GIVEN,
        redirect_url: str | None | NotGiven = NOT_GIVEN,
        skip_interstitial_page: bool | None = None,
        show_processing_status_page: bool | None = None,
        require_proof_of_payment: bool | None = None,
        enabled: bool | None = None,
        sort_order: int | None = None,
        modifier: UpdateCustomPaymentMethodRequestApplicationJsonPropertyModifier
        | None
        | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCustomPaymentMethodResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `str` | Yes |
| type | `SdkUpdateCustomPaymentMethodRequestApplicationJsonType
        \| str
        \| None` | No |
| name | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| instructions | `str \| None \| NotGiven` | No |
| steps | `builtins.list[str \| None] \| None \| NotGiven` | No |
| redirect_url | `str \| None \| NotGiven` | No |
| skip_interstitial_page | `bool \| None` | No |
| show_processing_status_page | `bool \| None` | No |
| require_proof_of_payment | `bool \| None` | No |
| enabled | `bool \| None` | No |
| sort_order | `int \| None` | No |
| modifier | `UpdateCustomPaymentMethodRequestApplicationJsonPropertyModifier
        \| None
        \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCustomPaymentMethodResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods_custom.update(
    custom_payment_method="string_example",
    enabled=False,
    modifier=None
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

## delete

Delete a custom payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **consequential**

```python
def delete(
        self,
        custom_payment_method: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods_custom.delete(custom_payment_method="string_example")
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

