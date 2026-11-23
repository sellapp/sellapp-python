# tickets_analytics

[All resources](../methods.md)

## get

Retrieve support analytics

[API reference](https://sell.app/docs/api/tickets/retrieve-support-analytics) · Effect: **read**

```python
def get(
        self,
        *,
        range: TicketsRange | str | None = None,
        rule_limit: int | None = None,
        activity_limit: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSupportAnalyticsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| range | `TicketsRange \| str \| None` | No |
| rule_limit | `int \| None` | No |
| activity_limit | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSupportAnalyticsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_analytics.get()
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

