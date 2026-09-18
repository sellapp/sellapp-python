# affiliates

[All resources](../methods.md)

## list

List affiliates

[API reference](https://sell.app/docs/api/affiliates/list-affiliates) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        status: AffiliatesStatus | str | None = None,
        search: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListAffiliatesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| status | `AffiliatesStatus \| str \| None` | No |
| search | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListAffiliatesResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliates.list()
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

Retrieve an affiliate

[API reference](https://sell.app/docs/api/affiliates/retrieve-affiliate) · Effect: **read**

```python
def get(
        self,
        affiliate: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetAffiliateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetAffiliateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliates.get(affiliate=1)
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

Update affiliate status

[API reference](https://sell.app/docs/api/affiliates/update-affiliate-status) · Effect: **consequential**

```python
def update(
        self,
        affiliate: int,
        *,
        status: SdkUpdateAffiliateStatusRequestApplicationJsonStatus | str,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateAffiliateStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `int` | Yes |
| status | `SdkUpdateAffiliateStatusRequestApplicationJsonStatus \| str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateAffiliateStatusResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliates.update(
    affiliate=42,
    status="active"
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

