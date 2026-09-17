# reward_rules

[All resources](../methods.md)

## list

List reward rules

[API reference](https://sell.app/docs/api/reward-rules/list-reward-rules) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkListRewardRulesResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SdkListRewardRulesResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_rules.list()
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

Create a reward rule

[API reference](https://sell.app/docs/api/reward-rules/create-a-reward-rule) · Effect: **consequential**

```python
def create(
        self,
        *,
        name: str,
        is_active: bool,
        trigger_type: Union[SdkCreateRewardRuleRequestApplicationJsonTriggerType, str],
        trigger_threshold: int,
        outputs: List[CreateRewardRuleRequestApplicationJsonPropertyOutputsItem],
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateRewardRuleResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| is_active | `bool` | Yes |
| trigger_type | `Union[SdkCreateRewardRuleRequestApplicationJsonTriggerType, str]` | Yes |
| trigger_threshold | `int` | Yes |
| outputs | `List[CreateRewardRuleRequestApplicationJsonPropertyOutputsItem]` | Yes |
| description | `Union[str, None, NotGiven]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateRewardRuleResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_rules.create(
    name="Launch Lab regular",
    is_active=False,
    trigger_type="PURCHASE_COUNT",
    trigger_threshold=3,
    outputs=[{"type": "BADGE", "label": "Launch Lab regular", "color": "violet"}]
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

## search

Search reward rules

[API reference](https://sell.app/docs/api/reward-rules/search-reward-rules) · Effect: **read**

```python
def search(
        self,
        *,
        filters: Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchRewardRulesRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchRewardRulesResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchRewardRulesRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchRewardRulesRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SdkSearchRewardRulesResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_rules.search(
    filters=[{"field": "id", "operator": "=", "value": 1}],
    sort=[{"field": "created_at", "direction": "desc"}]
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

## get

Retrieve a reward rule

[API reference](https://sell.app/docs/api/reward-rules/retrieve-a-reward-rule) · Effect: **read**

```python
def get(
        self,
        reward_rule: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetRewardRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetRewardRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_rules.get(reward_rule=1)
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

## replace

Update a reward rule

[API reference](https://sell.app/docs/api/reward-rules/update-a-reward-rule) · Effect: **consequential**

```python
def replace(
        self,
        reward_rule: int,
        *,
        name: Optional[str] = None,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        is_active: Optional[bool] = None,
        trigger_type: Optional[
            Union[SdkReplaceRewardRuleRequestApplicationJsonTriggerType, str]
        ] = None,
        trigger_threshold: Optional[int] = None,
        outputs: Optional[
            List[ReplaceRewardRuleRequestApplicationJsonPropertyOutputsItem]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceRewardRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `int` | Yes |
| name | `Optional[str]` | No |
| description | `Union[str, None, NotGiven]` | No |
| is_active | `Optional[bool]` | No |
| trigger_type | `Optional[
            Union[SdkReplaceRewardRuleRequestApplicationJsonTriggerType, str]
        ]` | No |
| trigger_threshold | `Optional[int]` | No |
| outputs | `Optional[
            List[ReplaceRewardRuleRequestApplicationJsonPropertyOutputsItem]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceRewardRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_rules.replace(
    reward_rule=1,
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

## update

Update a reward rule

[API reference](https://sell.app/docs/api/reward-rules/update-a-reward-rule) · Effect: **consequential**

```python
def update(
        self,
        reward_rule: int,
        *,
        name: Optional[str] = None,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        is_active: Optional[bool] = None,
        trigger_type: Optional[
            Union[SdkUpdateRewardRuleRequestApplicationJsonTriggerType, str]
        ] = None,
        trigger_threshold: Optional[int] = None,
        outputs: Optional[
            List[UpdateRewardRuleRequestApplicationJsonPropertyOutputsItem]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateRewardRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `int` | Yes |
| name | `Optional[str]` | No |
| description | `Union[str, None, NotGiven]` | No |
| is_active | `Optional[bool]` | No |
| trigger_type | `Optional[
            Union[SdkUpdateRewardRuleRequestApplicationJsonTriggerType, str]
        ]` | No |
| trigger_threshold | `Optional[int]` | No |
| outputs | `Optional[
            List[UpdateRewardRuleRequestApplicationJsonPropertyOutputsItem]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateRewardRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_rules.update(
    reward_rule=1,
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

