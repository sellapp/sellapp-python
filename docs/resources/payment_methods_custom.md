# payment_methods_custom

[All resources](../methods.md)

## list

List custom payment methods

[API reference](https://sell.app/docs/api/payment-methods/manage-custom-payment-methods) · Effect: **read**

```python
def list(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListCustomPaymentMethodsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

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
        type: Union[SdkCreateCustomPaymentMethodRequestApplicationJsonType, str],
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        instructions: Union[str, None, NotGiven] = NOT_GIVEN,
        steps: Union[List[Optional[str]], None, NotGiven] = NOT_GIVEN,
        redirect_url: Union[str, None, NotGiven] = NOT_GIVEN,
        skip_interstitial_page: Optional[bool] = None,
        show_processing_status_page: Optional[bool] = None,
        require_proof_of_payment: Optional[bool] = None,
        enabled: Optional[bool] = None,
        sort_order: Optional[int] = None,
        modifier: Union[
            CreateCustomPaymentMethodRequestApplicationJsonPropertyModifier,
            None,
            NotGiven,
        ] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateCustomPaymentMethodResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| type | `Union[SdkCreateCustomPaymentMethodRequestApplicationJsonType, str]` | Yes |
| name | `str` | Yes |
| description | `Union[str, None, NotGiven]` | No |
| instructions | `Union[str, None, NotGiven]` | No |
| steps | `Union[List[Optional[str]], None, NotGiven]` | No |
| redirect_url | `Union[str, None, NotGiven]` | No |
| skip_interstitial_page | `Optional[bool]` | No |
| show_processing_status_page | `Optional[bool]` | No |
| require_proof_of_payment | `Optional[bool]` | No |
| enabled | `Optional[bool]` | No |
| sort_order | `Optional[int]` | No |
| modifier | `Union[
            CreateCustomPaymentMethodRequestApplicationJsonPropertyModifier,
            None,
            NotGiven,
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomPaymentMethodResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        type: Union[SdkReplaceCustomPaymentMethodRequestApplicationJsonType, str],
        name: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        instructions: Union[str, None, NotGiven] = NOT_GIVEN,
        steps: Union[List[Optional[str]], None, NotGiven] = NOT_GIVEN,
        redirect_url: Union[str, None, NotGiven] = NOT_GIVEN,
        skip_interstitial_page: Optional[bool] = None,
        show_processing_status_page: Optional[bool] = None,
        require_proof_of_payment: Optional[bool] = None,
        enabled: Optional[bool] = None,
        sort_order: Optional[int] = None,
        modifier: Union[
            ReplaceCustomPaymentMethodRequestApplicationJsonPropertyModifier,
            None,
            NotGiven,
        ] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceCustomPaymentMethodResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `str` | Yes |
| type | `Union[SdkReplaceCustomPaymentMethodRequestApplicationJsonType, str]` | Yes |
| name | `str` | Yes |
| description | `Union[str, None, NotGiven]` | No |
| instructions | `Union[str, None, NotGiven]` | No |
| steps | `Union[List[Optional[str]], None, NotGiven]` | No |
| redirect_url | `Union[str, None, NotGiven]` | No |
| skip_interstitial_page | `Optional[bool]` | No |
| show_processing_status_page | `Optional[bool]` | No |
| require_proof_of_payment | `Optional[bool]` | No |
| enabled | `Optional[bool]` | No |
| sort_order | `Optional[int]` | No |
| modifier | `Union[
            ReplaceCustomPaymentMethodRequestApplicationJsonPropertyModifier,
            None,
            NotGiven,
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        type: Optional[
            Union[SdkUpdateCustomPaymentMethodRequestApplicationJsonType, str]
        ] = None,
        name: Optional[str] = None,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        instructions: Union[str, None, NotGiven] = NOT_GIVEN,
        steps: Union[List[Optional[str]], None, NotGiven] = NOT_GIVEN,
        redirect_url: Union[str, None, NotGiven] = NOT_GIVEN,
        skip_interstitial_page: Optional[bool] = None,
        show_processing_status_page: Optional[bool] = None,
        require_proof_of_payment: Optional[bool] = None,
        enabled: Optional[bool] = None,
        sort_order: Optional[int] = None,
        modifier: Union[
            UpdateCustomPaymentMethodRequestApplicationJsonPropertyModifier,
            None,
            NotGiven,
        ] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCustomPaymentMethodResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `str` | Yes |
| type | `Optional[
            Union[SdkUpdateCustomPaymentMethodRequestApplicationJsonType, str]
        ]` | No |
| name | `Optional[str]` | No |
| description | `Union[str, None, NotGiven]` | No |
| instructions | `Union[str, None, NotGiven]` | No |
| steps | `Union[List[Optional[str]], None, NotGiven]` | No |
| redirect_url | `Union[str, None, NotGiven]` | No |
| skip_interstitial_page | `Optional[bool]` | No |
| show_processing_status_page | `Optional[bool]` | No |
| require_proof_of_payment | `Optional[bool]` | No |
| enabled | `Optional[bool]` | No |
| sort_order | `Optional[int]` | No |
| modifier | `Union[
            UpdateCustomPaymentMethodRequestApplicationJsonPropertyModifier,
            None,
            NotGiven,
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_payment_method | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

