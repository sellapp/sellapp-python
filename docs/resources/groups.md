# groups

[All resources](../methods.md)

## list

List all groups

[API reference](https://sell.app/docs/api/groups/list-all-groups) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListGroupsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        order: int | None | NotGiven = NOT_GIVEN,
        product_ids: builtins.list[int] | None = None,
        section_id: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateGroupResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| unlisted | `bool` | Yes |
| order | `int \| None \| NotGiven` | No |
| product_ids | `builtins.list[int] \| None` | No |
| section_id | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> SdkGetGroupResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        title: str | None = None,
        unlisted: bool | None = None,
        order: int | None | NotGiven = NOT_GIVEN,
        product_ids: builtins.list[int] | None = None,
        section_id: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateGroupResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| title | `str \| None` | No |
| unlisted | `bool \| None` | No |
| order | `int \| None \| NotGiven` | No |
| product_ids | `builtins.list[int] \| None` | No |
| section_id | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| group | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        filters: builtins.list[SearchGroupsRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[SearchGroupsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchGroupsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[SearchGroupsRequestApplicationJsonPropertyIncludesItem]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchGroupsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[SearchGroupsRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[SearchGroupsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchGroupsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[SearchGroupsRequestApplicationJsonPropertyIncludesItem]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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

