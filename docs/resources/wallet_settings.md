# wallet_settings

[All resources](../methods.md)

## get

Retrieve wallet settings

[API reference](https://sell.app/docs/api/wallet/wallet-settings) · Effect: **read**

```python
def get(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetWalletSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetWalletSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_settings.get()
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

## replace

Update wallet settings

[API reference](https://sell.app/docs/api/wallet/wallet-settings) · Effect: **consequential**

```python
def replace(
        self,
        *,
        enabled: bool,
        minimum_top_up_cents: int | None,
        maximum_top_up_cents: int | None,
        expiration_days: int | None,
        payment_methods: list[str],
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceWalletSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| enabled | `bool` | Yes |
| minimum_top_up_cents | `int \| None` | Yes |
| maximum_top_up_cents | `int \| None` | Yes |
| expiration_days | `int \| None` | Yes |
| payment_methods | `list[str]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceWalletSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_settings.replace(
    enabled=False,
    minimum_top_up_cents=None,
    maximum_top_up_cents=None,
    expiration_days=None,
    payment_methods=[]
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

