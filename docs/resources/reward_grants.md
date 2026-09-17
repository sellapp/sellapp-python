# reward_grants

[All resources](../methods.md)

## list

List reward grants

[API reference](https://sell.app/docs/api/reward-grants/list-reward-grants) · Effect: **read**

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
    ) -> SyncPage[SdkListRewardGrantsResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkListRewardGrantsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_grants.list()
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

## issue

Issue an eligible reward grant

[API reference](https://sell.app/docs/api/reward-grants/issue-an-eligible-reward-grant) · Effect: **consequential**

```python
def issue(
        self,
        *,
        reward_rule_id: int,
        customer_id: int,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkIssueEligibleRewardGrantResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_rule_id | `int` | Yes |
| customer_id | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkIssueEligibleRewardGrantResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_grants.issue(
    reward_rule_id=10,
    customer_id=77
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

Documented HTTP responses: 200, 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search reward grants

[API reference](https://sell.app/docs/api/reward-grants/search-reward-grants) · Effect: **read**

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
    ) -> SyncPage[SdkSearchRewardGrantsResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkSearchRewardGrantsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_grants.search(
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

Retrieve a reward grant

[API reference](https://sell.app/docs/api/reward-grants/retrieve-a-reward-grant) · Effect: **read**

```python
def get(
        self,
        reward_grant: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetRewardGrantResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| reward_grant | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetRewardGrantResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.reward_grants.get(reward_grant=1)
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

