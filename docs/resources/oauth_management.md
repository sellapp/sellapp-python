# oauth_management

[All resources](../methods.md)

## get_oauth_installation

Read your CLI connection

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```python
def get_oauth_installation(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetOAuthInstallationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetOAuthInstallationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], access_token=os.environ["SELLAPP_ACCESS_TOKEN"], store="")

result = client.oauth_management.get_oauth_installation()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "oauthAccessToken": [
      "admin"
    ]
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## delete_oauth_installation

Disconnect your CLI connection

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```python
def delete_oauth_installation(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], access_token=os.environ["SELLAPP_ACCESS_TOKEN"], store="")

result = client.oauth_management.delete_oauth_installation()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "oauthAccessToken": [
      "admin"
    ]
  }
]
```

Documented HTTP responses: 204, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

