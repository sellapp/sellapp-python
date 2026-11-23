# wallet_overview

[All resources](../methods.md)

## get

Retrieve the wallet overview

[API reference](https://sell.app/docs/api/wallet/wallet-overview) · Effect: **read**

```python
def get(
        self,
        *,
        period: WalletPeriod | str | None = None,
        wallet_limit: int | None = None,
        activity_limit: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkGetWalletOverviewResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| period | `WalletPeriod \| str \| None` | No |
| wallet_limit | `int \| None` | No |
| activity_limit | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetWalletOverviewResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_overview.get()
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

