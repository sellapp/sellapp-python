# groups

[All resources](../methods.md)

## list

List all groups

[API reference](https://sell.app/docs/api/groups/list-all-groups) · Effect: **read**

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
    ) -> SyncPage[ListGroupsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListGroupsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups.list()
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

Create a group

[API reference](https://sell.app/docs/api/groups/create-a-group) · Effect: **write**

```python
def create(
        self,
        *,
        title: str,
        unlisted: bool,
        order: Union[int, None, NotGiven] = NOT_GIVEN,
        product_ids: Optional[List[int]] = None,
        section_id: Union[int, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateGroupResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| unlisted | `bool` | Yes |
| order | `Union[int, None, NotGiven]` | No |
| product_ids | `Optional[List[int]]` | No |
| section_id | `Union[int, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateGroupResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups.create(
    title="Design kit",
    unlisted=True
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

## get

Retrieve a group

[API reference](https://sell.app/docs/api/groups/retrieve-a-group) · Effect: **read**

```python
def get(
        self,
        group: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetGroupResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetGroupResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups.get(group=1)
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

Update a group

[API reference](https://sell.app/docs/api/groups/update-a-group) · Effect: **consequential**

```python
def update(
        self,
        group: int,
        *,
        title: Optional[str] = None,
        unlisted: Optional[bool] = None,
        order: Union[int, None, NotGiven] = NOT_GIVEN,
        product_ids: Optional[List[int]] = None,
        section_id: Union[int, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateGroupResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| title | `Optional[str]` | No |
| unlisted | `Optional[bool]` | No |
| order | `Union[int, None, NotGiven]` | No |
| product_ids | `Optional[List[int]]` | No |
| section_id | `Union[int, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateGroupResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups.update(
    group=1,
    title="Founder reading room",
    unlisted=True
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

## delete

Delete a group

[API reference](https://sell.app/docs/api/groups/delete-a-group) · Effect: **consequential**

```python
def delete(
        self,
        group: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups.delete(group=1)
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

## search

Search groups

[API reference](https://sell.app/docs/api/groups/search-groups) · Effect: **read**

```python
def search(
        self,
        *,
        filters: Optional[
            List[SearchGroupsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[List[SearchGroupsRequestApplicationJsonPropertySortItem]] = None,
        search: Optional[SearchGroupsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchGroupsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchGroupsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchGroupsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[List[SearchGroupsRequestApplicationJsonPropertySortItem]]` | No |
| search | `Optional[SearchGroupsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchGroupsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SearchGroupsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.groups.search(
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

