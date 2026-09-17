# entitlements

[All resources](../methods.md)

## list_customer_entitlements

List customer entitlements

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **read**

```python
def list_customer_entitlements(
        self,
        customer: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListCustomerEntitlementsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListCustomerEntitlementsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.entitlements.list_customer_entitlements(customer=42)
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

## list_customer_entitlements_by_external_id

List customer entitlements

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **read**

```python
def list_customer_entitlements_by_external_id(
        self,
        external_id: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListCustomerEntitlementsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListCustomerEntitlementsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.entitlements.list_customer_entitlements_by_external_id(external_id="externalId_01K4CUSTOMER")
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

