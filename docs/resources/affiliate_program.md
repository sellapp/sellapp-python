# affiliate_program

[All resources](../methods.md)

## get

Retrieve affiliate program configuration

[API reference](https://sell.app/docs/api/affiliate-program/retrieve-affiliate-program) · Effect: **read**

```python
def get(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetAffiliateProgramConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetAffiliateProgramConfigurationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_program.get()
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

Replace affiliate program configuration

[API reference](https://sell.app/docs/api/affiliate-program/replace-affiliate-program) · Effect: **consequential**

```python
def replace(
        self,
        *,
        enabled: bool,
        settings: ReplaceAffiliateProgramConfigurationRequestApplicationJsonPropertySettings,
        products: List[
            ReplaceAffiliateProgramConfigurationRequestApplicationJsonPropertyProductsItem
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceAffiliateProgramConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| enabled | `bool` | Yes |
| settings | `ReplaceAffiliateProgramConfigurationRequestApplicationJsonPropertySettings` | Yes |
| products | `List[
            ReplaceAffiliateProgramConfigurationRequestApplicationJsonPropertyProductsItem
        ]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceAffiliateProgramConfigurationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_program.replace(
    enabled=True,
    settings={
        "auto_approve_affiliates": False,
        "minimum_payout": "25",
        "commission": {"type": "percentage", "amount": "20"},
        "referrer_type": "first_referrer",
        "tracking_length": 30,
        "subscription_commission": True,
        "enabled_specific_products": True,
        "payout_methods": ["PAYPAL"],
        "enable_hub": False
    },
    products=[
        {
            "id": 42,
            "enabled": True,
            "commission": {"type": "percentage", "percentage": "25"}
        }
    ]
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

## list

List pending affiliate invitations

[API reference](https://sell.app/docs/api/affiliate-program/list-affiliate-invitations) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[
        ListPendingAffiliateInvitationsResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[
        ListPendingAffiliateInvitationsResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_program.list()
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

## invite

Invite an affiliate

[API reference](https://sell.app/docs/api/affiliate-program/invite-an-affiliate) · Effect: **consequential**

```python
def invite(
        self,
        *,
        email: str,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkInviteAffiliateResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkInviteAffiliateResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliate_program.invite(email="alex.morgan@example.com")
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

