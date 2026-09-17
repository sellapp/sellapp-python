# payment_methods

[All resources](../methods.md)

## list

List payment methods

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **read**

```python
def list(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListPaymentMethodsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListPaymentMethodsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods.list()
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

Retrieve payment method status

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **read**

```python
def get(
        self,
        payment_method: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetPaymentMethodStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetPaymentMethodStatusResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods.get(payment_method="STRIPE")
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

## enable

Enable or disable a payment method

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **consequential**

```python
def enable(
        self,
        payment_method: str,
        *,
        enabled: bool,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkEnableOrDisablePaymentMethodResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `str` | Yes |
| enabled | `bool` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkEnableOrDisablePaymentMethodResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods.enable(
    payment_method="STRIPE",
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

## connect

Create a payment connection handoff

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **consequential**

```python
def connect(
        self,
        payment_method: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreatePaymentConnectionHandoffResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreatePaymentConnectionHandoffResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods.connect(payment_method="STRIPE")
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

## validate

Validate and save payment method configuration

[API reference](https://sell.app/docs/api/payment-methods/manage-payment-methods) · Effect: **consequential**

```python
def validate(
        self,
        payment_method: str,
        *,
        body: Union[
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue1,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue2,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue3,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue4,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue5,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue6,
            Dict[str, Any],
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkValidateAndSavePaymentMethodConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| payment_method | `str` | Yes |
| body | `Union[
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue1,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue2,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue3,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue4,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue5,
            ValidateAndSavePaymentMethodConfigurationRequestApplicationJsonOneOfValue6,
            Dict[str, Any],
        ]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkValidateAndSavePaymentMethodConfigurationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.payment_methods.validate(
    payment_method="NMI",
    body={
        "merchant_secure_key": "replace-with-nmi-secure-key",
        "merchant_tokenization_key": "replace-with-nmi-tokenization-key",
        "signing_key": "replace-with-nmi-signing-key",
        "currencies": ["USD"]
    }
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

