# affiliate_referral_sessions

[All resources](../methods.md)

## list

List affiliate referral sessions

[API reference](https://sell.app/docs/api/affiliates/list-referral-sessions) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        affiliate_id: int | None = None,
        active: bool | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        ListAffiliateReferralSessionsResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| affiliate_id | `int \| None` | No |
| active | `bool \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        ListAffiliateReferralSessionsResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_referral_sessions.list()
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

Retrieve an affiliate referral session

[API reference](https://sell.app/docs/api/affiliates/list-referral-sessions) · Effect: **read**

```python
def get(
        self,
        referral_session: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetAffiliateReferralSessionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| referral_session | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetAffiliateReferralSessionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_referral_sessions.get(referral_session=1)
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

