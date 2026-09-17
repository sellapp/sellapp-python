# cashback_rules

[All resources](../methods.md)

## list

List cashback rules

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **read**

```python
def list(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListCashbackRulesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListCashbackRulesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.cashback_rules.list()
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

Create a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```python
def create(
        self,
        *,
        percent_basis: int,
        maximum_cashback_cents: Optional[int],
        is_active: bool,
        product_ids: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateCashbackRuleResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| percent_basis | `int` | Yes |
| maximum_cashback_cents | `Optional[int]` | Yes |
| is_active | `bool` | Yes |
| product_ids | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateCashbackRuleResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.cashback_rules.create(
    percent_basis=500,
    maximum_cashback_cents=1000,
    is_active=False,
    product_ids=[120]
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

Update a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```python
def replace(
        self,
        cashback_rule: int,
        *,
        percent_basis: int,
        maximum_cashback_cents: Optional[int],
        is_active: bool,
        product_ids: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceCashbackRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| cashback_rule | `int` | Yes |
| percent_basis | `int` | Yes |
| maximum_cashback_cents | `Optional[int]` | Yes |
| is_active | `bool` | Yes |
| product_ids | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceCashbackRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.cashback_rules.replace(
    cashback_rule=1,
    percent_basis=500,
    maximum_cashback_cents=1000,
    is_active=False,
    product_ids=[120]
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

## update

Update a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```python
def update(
        self,
        cashback_rule: int,
        *,
        percent_basis: Optional[int] = None,
        maximum_cashback_cents: Union[int, None, NotGiven] = NOT_GIVEN,
        is_active: Optional[bool] = None,
        product_ids: Optional[List[int]] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCashbackRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| cashback_rule | `int` | Yes |
| percent_basis | `Optional[int]` | No |
| maximum_cashback_cents | `Union[int, None, NotGiven]` | No |
| is_active | `Optional[bool]` | No |
| product_ids | `Optional[List[int]]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateCashbackRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.cashback_rules.update(
    cashback_rule=1,
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## archive

Archive a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```python
def archive(
        self,
        cashback_rule: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| cashback_rule | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.cashback_rules.archive(cashback_rule=1)
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

Restore a cashback rule

[API reference](https://sell.app/docs/api/wallet/cashback-rules) · Effect: **consequential**

```python
def restore(
        self,
        cashback_rule: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkRestoreCashbackRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| cashback_rule | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkRestoreCashbackRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.cashback_rules.restore(cashback_rule=1)
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

