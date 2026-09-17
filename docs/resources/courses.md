# courses

[All resources](../methods.md)

## list

List courses

[API reference](https://sell.app/docs/api/courses/list-courses) · Effect: **read**

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
    ) -> SyncPage[SdkListCoursesResponseValue200ApplicationJson]:
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
    ) -> SyncPage[SdkSearchCoursesResponseValue200ApplicationJson]:
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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCourseResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        category: Union[Union[Category, str], None, NotGiven] = NOT_GIVEN,
        level: Optional[Union[SdkReplaceCourseRequestApplicationJsonLevel, str]] = None,
        language: Optional[str] = None,
        subtitle: Union[str, None, NotGiven] = NOT_GIVEN,
        author: Union[str, None, NotGiven] = NOT_GIVEN,
        subcategory: Union[str, None, NotGiven] = NOT_GIVEN,
        what_you_learn: Optional[List[str]] = None,
        requirements: Optional[List[str]] = None,
        certificate_enabled: Optional[bool] = None,
        access_type: Optional[
            Union[SdkReplaceCourseRequestApplicationJsonAccessType, str]
        ] = None,
        access_duration_days: Union[int, None, NotGiven] = NOT_GIVEN,
        enrollment_limit: Union[int, None, NotGiven] = NOT_GIVEN,
        delivery_text: Union[str, None, NotGiven] = NOT_GIVEN,
        visibility: Optional[Union[CatalogVisibility, str]] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceCourseResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| category | `Union[Union[Category, str], None, NotGiven]` | No |
| level | `Optional[Union[SdkReplaceCourseRequestApplicationJsonLevel, str]]` | No |
| language | `Optional[str]` | No |
| subtitle | `Union[str, None, NotGiven]` | No |
| author | `Union[str, None, NotGiven]` | No |
| subcategory | `Union[str, None, NotGiven]` | No |
| what_you_learn | `Optional[List[str]]` | No |
| requirements | `Optional[List[str]]` | No |
| certificate_enabled | `Optional[bool]` | No |
| access_type | `Optional[
            Union[SdkReplaceCourseRequestApplicationJsonAccessType, str]
        ]` | No |
| access_duration_days | `Union[int, None, NotGiven]` | No |
| enrollment_limit | `Union[int, None, NotGiven]` | No |
| delivery_text | `Union[str, None, NotGiven]` | No |
| visibility | `Optional[Union[CatalogVisibility, str]]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        category: Union[Union[Category, str], None, NotGiven] = NOT_GIVEN,
        level: Optional[Union[SdkUpdateCourseRequestApplicationJsonLevel, str]] = None,
        language: Optional[str] = None,
        subtitle: Union[str, None, NotGiven] = NOT_GIVEN,
        author: Union[str, None, NotGiven] = NOT_GIVEN,
        subcategory: Union[str, None, NotGiven] = NOT_GIVEN,
        what_you_learn: Optional[List[str]] = None,
        requirements: Optional[List[str]] = None,
        certificate_enabled: Optional[bool] = None,
        access_type: Optional[
            Union[SdkUpdateCourseRequestApplicationJsonAccessType, str]
        ] = None,
        access_duration_days: Union[int, None, NotGiven] = NOT_GIVEN,
        enrollment_limit: Union[int, None, NotGiven] = NOT_GIVEN,
        delivery_text: Union[str, None, NotGiven] = NOT_GIVEN,
        visibility: Optional[Union[CatalogVisibility, str]] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCourseResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| category | `Union[Union[Category, str], None, NotGiven]` | No |
| level | `Optional[Union[SdkUpdateCourseRequestApplicationJsonLevel, str]]` | No |
| language | `Optional[str]` | No |
| subtitle | `Union[str, None, NotGiven]` | No |
| author | `Union[str, None, NotGiven]` | No |
| subcategory | `Union[str, None, NotGiven]` | No |
| what_you_learn | `Optional[List[str]]` | No |
| requirements | `Optional[List[str]]` | No |
| certificate_enabled | `Optional[bool]` | No |
| access_type | `Optional[
            Union[SdkUpdateCourseRequestApplicationJsonAccessType, str]
        ]` | No |
| access_duration_days | `Union[int, None, NotGiven]` | No |
| enrollment_limit | `Union[int, None, NotGiven]` | No |
| delivery_text | `Union[str, None, NotGiven]` | No |
| visibility | `Optional[Union[CatalogVisibility, str]]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

