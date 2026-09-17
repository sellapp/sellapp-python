# affiliate_referrals

[All resources](../methods.md)

## list

List affiliate referrals

[API reference](https://sell.app/docs/api/affiliates/list-referrals) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        affiliate_id: Optional[int] = None,
        order_id: Optional[int] = None,
        status: Optional[Union[AffiliateReferralsStatus, str]] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[
        ListAffiliateReferralsResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| affiliate_id | `Optional[int]` | No |
| order_id | `Optional[int]` | No |
| status | `Optional[Union[AffiliateReferralsStatus, str]]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetAffiliateReferralResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| referral | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        status: Union[SdkUpdateReferralStatusRequestApplicationJsonStatus, str],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateReferralStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| referral | `int` | Yes |
| status | `Union[SdkUpdateReferralStatusRequestApplicationJsonStatus, str]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

