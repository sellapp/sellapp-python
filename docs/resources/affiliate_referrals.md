# affiliate_referrals

[All resources](../methods.md)

## list

List affiliate referrals

[API reference](https://sell.app/docs/api/affiliates/list-referrals) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        affiliate_id: int | None = None,
        order_id: int | None = None,
        status: AffiliateReferralsStatus | str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        ListAffiliateReferralsResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| affiliate_id | `int \| None` | No |
| order_id | `int \| None` | No |
| status | `AffiliateReferralsStatus \| str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        ListAffiliateReferralsResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_referrals.list()
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

Retrieve an affiliate referral

[API reference](https://sell.app/docs/api/affiliates/manage-referral) · Effect: **read**

```python
def get(
        self,
        referral: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetAffiliateReferralResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| referral | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetAffiliateReferralResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_referrals.get(referral=1)
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

Update referral status

[API reference](https://sell.app/docs/api/affiliates/manage-referral) · Effect: **consequential**

```python
def update(
        self,
        referral: int,
        *,
        status: SdkUpdateReferralStatusRequestApplicationJsonStatus | str,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateReferralStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| referral | `int` | Yes |
| status | `SdkUpdateReferralStatusRequestApplicationJsonStatus \| str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateReferralStatusResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_referrals.update(
    referral=71,
    status="accepted"
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

