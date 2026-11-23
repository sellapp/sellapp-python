# store_sender_email

[All resources](../methods.md)

## get

Retrieve the sender email

[API reference](https://sell.app/docs/api/store-settings/sender-email) · Effect: **read**

```python
def get(
        self,
        *,
        email: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSenderEmailResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSenderEmailResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_sender_email.get()
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

## set

Set the sender email

[API reference](https://sell.app/docs/api/store-settings/sender-email) · Effect: **consequential**

```python
def set(
        self,
        *,
        email: str,
        request_options: RequestOptions | None = None,
    ) -> SdkSetSenderEmailResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkSetSenderEmailResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_sender_email.set(email="orders@launch-lab.example.com")
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

## delete

Delete the sender email

[API reference](https://sell.app/docs/api/store-settings/sender-email) · Effect: **consequential**

```python
def delete(
        self,
        *,
        email: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_sender_email.delete()
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500, 503. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## send_verification

Send a sender email verification

[API reference](https://sell.app/docs/api/store-settings/sender-email) · Effect: **consequential**

```python
def send_verification(
        self,
        *,
        email: str,
        request_options: RequestOptions | None = None,
    ) -> SdkSendSenderEmailVerificationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkSendSenderEmailVerificationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_sender_email.send_verification(email="orders@launch-lab.example.com")
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500, 503. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

