# courses

[All resources](../methods.md)

## list

List courses

[API reference](https://sell.app/docs/api/courses/list-courses) · Effect: **read**

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
    ) -> SyncPage[SdkListCoursesResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkListCoursesResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses.list()
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

## search

Search courses

[API reference](https://sell.app/docs/api/courses/search-courses) · Effect: **read**

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
    ) -> SyncPage[SdkSearchCoursesResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkSearchCoursesResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses.search(
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

Retrieve a course

[API reference](https://sell.app/docs/api/courses/retrieve-course) · Effect: **read**

```python
def get(
        self,
        course: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCourseResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCourseResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses.get(course="string_example")
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

Update a course

[API reference](https://sell.app/docs/api/courses/update-course) · Effect: **write**

```python
def replace(
        self,
        course: str,
        *,
        category: Category | str | None | NotGiven = NOT_GIVEN,
        level: SdkReplaceCourseRequestApplicationJsonLevel | str | None = None,
        language: str | None = None,
        subtitle: str | None | NotGiven = NOT_GIVEN,
        author: str | None | NotGiven = NOT_GIVEN,
        subcategory: str | None | NotGiven = NOT_GIVEN,
        what_you_learn: builtins.list[str] | None = None,
        requirements: builtins.list[str] | None = None,
        certificate_enabled: bool | None = None,
        access_type: SdkReplaceCourseRequestApplicationJsonAccessType
        | str
        | None = None,
        access_duration_days: int | None | NotGiven = NOT_GIVEN,
        enrollment_limit: int | None | NotGiven = NOT_GIVEN,
        delivery_text: str | None | NotGiven = NOT_GIVEN,
        visibility: CatalogVisibility | str | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCourseResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| category | `Category \| str \| None \| NotGiven` | No |
| level | `SdkReplaceCourseRequestApplicationJsonLevel \| str \| None` | No |
| language | `str \| None` | No |
| subtitle | `str \| None \| NotGiven` | No |
| author | `str \| None \| NotGiven` | No |
| subcategory | `str \| None \| NotGiven` | No |
| what_you_learn | `builtins.list[str] \| None` | No |
| requirements | `builtins.list[str] \| None` | No |
| certificate_enabled | `bool \| None` | No |
| access_type | `SdkReplaceCourseRequestApplicationJsonAccessType
        \| str
        \| None` | No |
| access_duration_days | `int \| None \| NotGiven` | No |
| enrollment_limit | `int \| None \| NotGiven` | No |
| delivery_text | `str \| None \| NotGiven` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceCourseResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses.replace(
    course="string_example",
    level="beginner",
    visibility="HIDDEN"
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

Update a course

[API reference](https://sell.app/docs/api/courses/update-course) · Effect: **write**

```python
def update(
        self,
        course: str,
        *,
        category: Category | str | None | NotGiven = NOT_GIVEN,
        level: SdkUpdateCourseRequestApplicationJsonLevel | str | None = None,
        language: str | None = None,
        subtitle: str | None | NotGiven = NOT_GIVEN,
        author: str | None | NotGiven = NOT_GIVEN,
        subcategory: str | None | NotGiven = NOT_GIVEN,
        what_you_learn: builtins.list[str] | None = None,
        requirements: builtins.list[str] | None = None,
        certificate_enabled: bool | None = None,
        access_type: SdkUpdateCourseRequestApplicationJsonAccessType
        | str
        | None = None,
        access_duration_days: int | None | NotGiven = NOT_GIVEN,
        enrollment_limit: int | None | NotGiven = NOT_GIVEN,
        delivery_text: str | None | NotGiven = NOT_GIVEN,
        visibility: CatalogVisibility | str | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCourseResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| category | `Category \| str \| None \| NotGiven` | No |
| level | `SdkUpdateCourseRequestApplicationJsonLevel \| str \| None` | No |
| language | `str \| None` | No |
| subtitle | `str \| None \| NotGiven` | No |
| author | `str \| None \| NotGiven` | No |
| subcategory | `str \| None \| NotGiven` | No |
| what_you_learn | `builtins.list[str] \| None` | No |
| requirements | `builtins.list[str] \| None` | No |
| certificate_enabled | `bool \| None` | No |
| access_type | `SdkUpdateCourseRequestApplicationJsonAccessType
        \| str
        \| None` | No |
| access_duration_days | `int \| None \| NotGiven` | No |
| enrollment_limit | `int \| None \| NotGiven` | No |
| delivery_text | `str \| None \| NotGiven` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCourseResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses.update(
    course="string_example",
    level="beginner",
    visibility="HIDDEN"
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

