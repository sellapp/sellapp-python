# affiliate_payouts

[All resources](../methods.md)

## list

List affiliate payouts

[API reference](https://sell.app/docs/api/affiliates/list-payouts) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        affiliate_id: int | None = None,
        status: AffiliatePayoutsStatus | str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListAffiliatePayoutsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| affiliate_id | `int \| None` | No |
| status | `AffiliatePayoutsStatus \| str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListAffiliatePayoutsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_payouts.list()
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

Retrieve an affiliate payout

[API reference](https://sell.app/docs/api/affiliates/list-payouts) · Effect: **read**

```python
def get(
        self,
        payout: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetAffiliatePayoutResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| payout | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetAffiliatePayoutResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_payouts.get(payout=1)
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

## create

Create an affiliate payout

[API reference](https://sell.app/docs/api/affiliates/create-payout) · Effect: **consequential**

```python
def create(
        self,
        affiliate: int,
        *,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateAffiliatePayoutResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `int` | Yes |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateAffiliatePayoutResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_payouts.create(
    affiliate=1,
    idempotency_key="example-mutation-001"
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update

Update affiliate payout status

[API reference](https://sell.app/docs/api/affiliates/update-payout-status) · Effect: **consequential**

```python
def update(
        self,
        payout: int,
        *,
        status: SdkUpdateAffiliatePayoutStatusRequestApplicationJsonStatus | str,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateAffiliatePayoutStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| payout | `int` | Yes |
| status | `SdkUpdateAffiliatePayoutStatusRequestApplicationJsonStatus \| str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateAffiliatePayoutStatusResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_payouts.update(
    payout=1,
    status="paid"
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

