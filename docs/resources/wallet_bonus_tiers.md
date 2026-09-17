# wallet_bonus_tiers

[All resources](../methods.md)

## list

List wallet bonus tiers

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **read**

```python
def list(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListWalletBonusTiersResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListWalletBonusTiersResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_bonus_tiers.list()
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

## create

Create a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```python
def create(
        self,
        *,
        minimum_top_up_cents: int,
        bonus_kind: Union[SdkCreateWalletBonusTierRequestApplicationJsonBonusKind, str],
        fixed_bonus_cents: Optional[int],
        percent_basis: Optional[int],
        maximum_bonus_cents: Optional[int],
        priority: int,
        is_active: bool,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateWalletBonusTierResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| minimum_top_up_cents | `int` | Yes |
| bonus_kind | `Union[SdkCreateWalletBonusTierRequestApplicationJsonBonusKind, str]` | Yes |
| fixed_bonus_cents | `Optional[int]` | Yes |
| percent_basis | `Optional[int]` | Yes |
| maximum_bonus_cents | `Optional[int]` | Yes |
| priority | `int` | Yes |
| is_active | `bool` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateWalletBonusTierResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_bonus_tiers.create(
    minimum_top_up_cents=10000,
    bonus_kind="fixed",
    fixed_bonus_cents=500,
    percent_basis=None,
    maximum_bonus_cents=None,
    priority=0,
    is_active=False
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace

Update a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```python
def replace(
        self,
        bonus_tier: int,
        *,
        minimum_top_up_cents: int,
        bonus_kind: Union[
            SdkReplaceWalletBonusTierRequestApplicationJsonBonusKind, str
        ],
        fixed_bonus_cents: Optional[int],
        percent_basis: Optional[int],
        maximum_bonus_cents: Optional[int],
        priority: int,
        is_active: bool,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceWalletBonusTierResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| bonus_tier | `int` | Yes |
| minimum_top_up_cents | `int` | Yes |
| bonus_kind | `Union[
            SdkReplaceWalletBonusTierRequestApplicationJsonBonusKind, str
        ]` | Yes |
| fixed_bonus_cents | `Optional[int]` | Yes |
| percent_basis | `Optional[int]` | Yes |
| maximum_bonus_cents | `Optional[int]` | Yes |
| priority | `int` | Yes |
| is_active | `bool` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceWalletBonusTierResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_bonus_tiers.replace(
    bonus_tier=1,
    minimum_top_up_cents=10000,
    bonus_kind="fixed",
    fixed_bonus_cents=500,
    percent_basis=None,
    maximum_bonus_cents=None,
    priority=0,
    is_active=False
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

Update a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```python
def update(
        self,
        bonus_tier: int,
        *,
        minimum_top_up_cents: Optional[int] = None,
        bonus_kind: Optional[
            Union[SdkUpdateWalletBonusTierRequestApplicationJsonBonusKind, str]
        ] = None,
        fixed_bonus_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        percent_basis: Union[int, None, NotGiven] = NOT_GIVEN,
        maximum_bonus_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        priority: Optional[int] = None,
        is_active: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateWalletBonusTierResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| bonus_tier | `int` | Yes |
| minimum_top_up_cents | `Optional[int]` | No |
| bonus_kind | `Optional[
            Union[SdkUpdateWalletBonusTierRequestApplicationJsonBonusKind, str]
        ]` | No |
| fixed_bonus_cents | `Union[int, None, NotGiven]` | No |
| percent_basis | `Union[int, None, NotGiven]` | No |
| maximum_bonus_cents | `Union[int, None, NotGiven]` | No |
| priority | `Optional[int]` | No |
| is_active | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateWalletBonusTierResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_bonus_tiers.update(
    bonus_tier=1,
    is_active=False
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

## archive

Archive a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```python
def archive(
        self,
        bonus_tier: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| bonus_tier | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_bonus_tiers.archive(bonus_tier=1)
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

## restore

Restore a wallet bonus tier

[API reference](https://sell.app/docs/api/wallet/bonus-tiers) · Effect: **consequential**

```python
def restore(
        self,
        bonus_tier: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkRestoreWalletBonusTierResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| bonus_tier | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkRestoreWalletBonusTierResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.wallet_bonus_tiers.restore(bonus_tier=1)
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

