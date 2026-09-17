# courses_sections

[All resources](../methods.md)

## create

Create a course section

[API reference](https://sell.app/docs/api/courses/manage-course-sections) · Effect: **write**

```python
def create(
        self,
        course: str,
        *,
        title: str,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateCourseSectionResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| title | `str` | Yes |
| description | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateCourseSectionResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_sections.create(
    course="string_example",
    title="Getting started"
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

Documented HTTP responses: 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## replace

Update a course section

[API reference](https://sell.app/docs/api/courses/manage-course-sections) · Effect: **write**

```python
def replace(
        self,
        course: str,
        section: int,
        *,
        title: Optional[str] = None,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceCourseSectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| section | `int` | Yes |
| title | `Optional[str]` | No |
| description | `Union[str, None, NotGiven]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceCourseSectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_sections.replace(
    course="string_example",
    section=1,
    title="Getting started"
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

Update a course section

[API reference](https://sell.app/docs/api/courses/manage-course-sections) · Effect: **write**

```python
def update(
        self,
        course: str,
        section: int,
        *,
        title: Optional[str] = None,
        description: Union[str, None, NotGiven] = NOT_GIVEN,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCourseSectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| section | `int` | Yes |
| title | `Optional[str]` | No |
| description | `Union[str, None, NotGiven]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateCourseSectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_sections.update(
    course="string_example",
    section=1,
    title="Getting started"
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

Delete a course section

[API reference](https://sell.app/docs/api/courses/manage-course-sections) · Effect: **consequential**

```python
def delete(
        self,
        course: str,
        section: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| section | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_sections.delete(
    course="string_example",
    section=1
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

## reorder

Reorder course sections

[API reference](https://sell.app/docs/api/courses/reorder-course-sections) · Effect: **consequential**

```python
def reorder(
        self,
        course: str,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReorderCourseSectionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReorderCourseSectionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_sections.reorder(
    course="string_example",
    resources=[501, 502]
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

