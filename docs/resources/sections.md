# sections

[All resources](../methods.md)

## list

List all sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

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
    ) -> SyncPage[ListSectionsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListSectionsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.list()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create

Create a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def create(
        self,
        *,
        title: str,
        hidden: bool,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateSectionResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| hidden | `bool` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateSectionResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.create(
    title="Founder resources",
    hidden=False
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 201, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def get(
        self,
        section: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetSectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetSectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.get(section=1)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace

Update a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def replace(
        self,
        section: int,
        *,
        title: Optional[str] = None,
        hidden: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceSectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| title | `Optional[str]` | No |
| hidden | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceSectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.replace(
    section=1,
    title="Founder resources",
    hidden=False
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update

Update a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def update(
        self,
        section: int,
        *,
        title: Optional[str] = None,
        hidden: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateSectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| title | `Optional[str]` | No |
| hidden | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateSectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.update(
    section=1,
    title="Founder resources",
    hidden=False
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## delete

Delete a section

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def delete(
        self,
        section: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.delete(section=1)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace_order

Replace section order

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def replace_order(
        self,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceSectionOrderResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceSectionOrderResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.replace_order(resources=[3, 1, 2])
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace_products

Replace section products

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def replace_products(
        self,
        section: int,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceSectionProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceSectionProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.replace_products(
    section=1,
    resources=[3, 1, 2]
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace_groups

Replace section groups

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def replace_groups(
        self,
        section: int,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceSectionGroupsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceSectionGroupsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.replace_groups(
    section=1,
    resources=[3, 1, 2]
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def search(
        self,
        *,
        filters: Optional[
            List[SearchSectionsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchSectionsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchSectionsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchSectionsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchSectionsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchSectionsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchSectionsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchSectionsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchSectionsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SearchSectionsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.search(
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
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_create

Batch create sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def batch_create(
        self,
        *,
        resources: List[BatchCreateSectionsRequestApplicationJsonPropertyResourcesItem],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkBatchCreateSectionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[BatchCreateSectionsRequestApplicationJsonPropertyResourcesItem]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkBatchCreateSectionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.batch_create(resources=[{"title": "Featured", "hidden": False}])
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 201, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_update

Batch update sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def batch_update(
        self,
        *,
        resources: BatchUpdateSectionsRequestApplicationJsonPropertyResources,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkBatchUpdateSectionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `BatchUpdateSectionsRequestApplicationJsonPropertyResources` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkBatchUpdateSectionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.batch_update(resources={"1": {"title": "Featured", "hidden": False}})
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_delete

Batch delete sections

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def batch_delete(
        self,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.batch_delete(resources=[1, 2])
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v2_list_sections

List all sections

[API reference](https://sell.app/docs/api/sections/list-all-sections) · Effect: **read**

```python
def v2_list_sections(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[V2ListSectionsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[V2ListSectionsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_list_sections()
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

## v2_create_section

Create a section

[API reference](https://sell.app/docs/api/sections/create-a-section) · Effect: **write**

```python
def v2_create_section(
        self,
        *,
        title: str,
        hidden: bool,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2CreateSectionResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| hidden | `bool` | Yes |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2CreateSectionResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_create_section(
    title="Founder resources",
    hidden=False
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

## v2_search_sections

Search sections

[API reference](https://sell.app/docs/api/sections/search-sections) · Effect: **read**

```python
def v2_search_sections(
        self,
        *,
        filters: Optional[
            List[V2SearchSectionsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[V2SearchSectionsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[V2SearchSectionsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[V2SearchSectionsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[V2SearchSectionsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[V2SearchSectionsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[V2SearchSectionsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[V2SearchSectionsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[V2SearchSectionsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[V2SearchSectionsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_search_sections(
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

## v2_get_section

Retrieve a section

[API reference](https://sell.app/docs/api/sections/retrieve-a-section) · Effect: **read**

```python
def v2_get_section(
        self,
        section: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2GetSectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2GetSectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_get_section(section=1)
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

## v2_replace_section

Update a section

[API reference](https://sell.app/docs/api/sections/update-a-section) · Effect: **write**

```python
def v2_replace_section(
        self,
        section: int,
        *,
        title: Optional[str] = None,
        hidden: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2ReplaceSectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| title | `Optional[str]` | No |
| hidden | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2ReplaceSectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_replace_section(
    section=1,
    title="Founder resources",
    hidden=False
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

## v2_update_section

Update a section

[API reference](https://sell.app/docs/api/sections/update-a-section) · Effect: **write**

```python
def v2_update_section(
        self,
        section: int,
        *,
        title: Optional[str] = None,
        hidden: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2UpdateSectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| title | `Optional[str]` | No |
| hidden | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2UpdateSectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_update_section(
    section=1,
    title="Founder resources",
    hidden=False
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

## v2_delete_section

Delete a section

[API reference](https://sell.app/docs/api/sections/delete-a-section) · Effect: **consequential**

```python
def v2_delete_section(
        self,
        section: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_delete_section(section=1)
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

## v2_batch_create_sections

Batch create sections

[API reference](https://sell.app/docs/api/sections/batch-create-sections) · Effect: **consequential**

```python
def v2_batch_create_sections(
        self,
        *,
        resources: List[
            V2BatchCreateSectionsRequestApplicationJsonPropertyResourcesItem
        ],
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2BatchCreateSectionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[
            V2BatchCreateSectionsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2BatchCreateSectionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_batch_create_sections(resources=[{"title": "Featured", "hidden": False}])
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

## v2_batch_update_sections

Batch update sections

[API reference](https://sell.app/docs/api/sections/batch-update-sections) · Effect: **consequential**

```python
def v2_batch_update_sections(
        self,
        *,
        resources: V2BatchUpdateSectionsRequestApplicationJsonPropertyResources,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2BatchUpdateSectionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `V2BatchUpdateSectionsRequestApplicationJsonPropertyResources` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2BatchUpdateSectionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_batch_update_sections(resources={"1": {"title": "Featured", "hidden": False}})
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

## v2_batch_delete_sections

Batch delete sections

[API reference](https://sell.app/docs/api/sections/batch-delete-sections) · Effect: **consequential**

```python
def v2_batch_delete_sections(
        self,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_batch_delete_sections(resources=[1, 2])
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

## v2_replace_section_order

Replace section order

[API reference](https://sell.app/docs/api/sections/order-sections) · Effect: **consequential**

```python
def v2_replace_section_order(
        self,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2ReplaceSectionOrderResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2ReplaceSectionOrderResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_replace_section_order(resources=[3, 1, 2])
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

## v2_replace_section_products

Replace section products

[API reference](https://sell.app/docs/api/sections/replace-section-products) · Effect: **consequential**

```python
def v2_replace_section_products(
        self,
        section: int,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2ReplaceSectionProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2ReplaceSectionProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_replace_section_products(
    section=1,
    resources=[3, 1, 2]
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

## v2_replace_section_groups

Replace section groups

[API reference](https://sell.app/docs/api/sections/replace-section-groups) · Effect: **consequential**

```python
def v2_replace_section_groups(
        self,
        section: int,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2ReplaceSectionGroupsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| section | `int` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2ReplaceSectionGroupsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.sections.v2_replace_section_groups(
    section=1,
    resources=[3, 1, 2]
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

