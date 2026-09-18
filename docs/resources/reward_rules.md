# reward_rules

[All resources](../methods.md)

## list

List reward rules

[API reference](https://sell.app/docs/api/reward-rules/list-reward-rules) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkListRewardRulesResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        trigger_type: SdkCreateRewardRuleRequestApplicationJsonTriggerType | str,
        trigger_threshold: int,
        outputs: builtins.list[
            CreateRewardRuleRequestApplicationJsonPropertyOutputsItem
        ],
        description: str | None | NotGiven = NOT_GIVEN,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateRewardRuleResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| is_active | `bool` | Yes |
| trigger_type | `SdkCreateRewardRuleRequestApplicationJsonTriggerType \| str` | Yes |
| trigger_threshold | `int` | Yes |
| outputs | `builtins.list[
            CreateRewardRuleRequestApplicationJsonPropertyOutputsItem
        ]` | Yes |
| description | `str \| None \| NotGiven` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        filters: builtins.list[
            SearchRewardRulesRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchRewardRulesRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchRewardRulesRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchRewardRulesRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchRewardRulesResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[
            SearchRewardRulesRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchRewardRulesRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchRewardRulesRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchRewardRulesRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> SdkGetRewardRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        name: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        trigger_type: SdkReplaceRewardRuleRequestApplicationJsonTriggerType
        | str
        | None = None,
        trigger_threshold: int | None = None,
        outputs: builtins.list[
            ReplaceRewardRuleRequestApplicationJsonPropertyOutputsItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceRewardRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `int` | Yes |
| name | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| trigger_type | `SdkReplaceRewardRuleRequestApplicationJsonTriggerType
        \| str
        \| None` | No |
| trigger_threshold | `int \| None` | No |
| outputs | `builtins.list[
            ReplaceRewardRuleRequestApplicationJsonPropertyOutputsItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        name: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        trigger_type: SdkUpdateRewardRuleRequestApplicationJsonTriggerType
        | str
        | None = None,
        trigger_threshold: int | None = None,
        outputs: builtins.list[
            UpdateRewardRuleRequestApplicationJsonPropertyOutputsItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateRewardRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule | `int` | Yes |
| name | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| trigger_type | `SdkUpdateRewardRuleRequestApplicationJsonTriggerType
        \| str
        \| None` | No |
| trigger_threshold | `int \| None` | No |
| outputs | `builtins.list[
            UpdateRewardRuleRequestApplicationJsonPropertyOutputsItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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

