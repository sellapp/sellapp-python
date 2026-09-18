# customer_sessions

[All resources](../methods.md)

## create_customer_session

Create a customer session

[API reference](https://sell.app/docs/api/customer-sessions) · Effect: **consequential**

```python
def create_customer_session(
        self,
        *,
        body: CreateCustomerSessionRequestApplicationJsonOneOfValue1
        | CreateCustomerSessionRequestApplicationJsonOneOfValue2
        | dict[str, Any],
        request_options: RequestOptions | None = None,
    ) -> SdkCreateCustomerSessionResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| body | `CreateCustomerSessionRequestApplicationJsonOneOfValue1
        \| CreateCustomerSessionRequestApplicationJsonOneOfValue2
        \| dict[str, Any]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateCustomerSessionResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customer_sessions.create_customer_session(body={"external_customer_id": "crm_maya_314"})
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## revoke_customer_session

Revoke a customer session

[API reference](https://sell.app/docs/api/customer-sessions) · Effect: **consequential**

```python
def revoke_customer_session(
        self,
        session: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| session | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customer_sessions.revoke_customer_session(session="session_01K4CUSTOMER")
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

