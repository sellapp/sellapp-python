# courses_lessons

[All resources](../methods.md)

## create

Create a course lesson

[API reference](https://sell.app/docs/api/courses/manage-course-lessons) · Effect: **write**

```python
def create(
        self,
        course: str,
        section: int,
        *,
        title: str,
        type: Union[SdkCreateCourseLessonRequestApplicationJsonType, str],
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        is_preview: Optional[bool] = None,
        is_published: Optional[bool] = None,
        assignment: Optional[
            CreateCourseLessonRequestApplicationJsonPropertyAssignment
        ] = None,
        questions: Optional[
            List[CreateCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateCourseLessonResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| section | `int` | Yes |
| title | `str` | Yes |
| type | `Union[SdkCreateCourseLessonRequestApplicationJsonType, str]` | Yes |
| content | `Union[str, None, NotGiven]` | No |
| is_preview | `Optional[bool]` | No |
| is_published | `Optional[bool]` | No |
| assignment | `Optional[
            CreateCourseLessonRequestApplicationJsonPropertyAssignment
        ]` | No |
| questions | `Optional[
            List[CreateCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateCourseLessonResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_lessons.create(
    course="string_example",
    section=1,
    title="Welcome",
    type="text",
    content="Welcome to Launch Lab.",
    is_published=False
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

Update a course lesson

[API reference](https://sell.app/docs/api/courses/manage-course-lessons) · Effect: **write**

```python
def replace(
        self,
        course: str,
        lesson: int,
        *,
        title: Optional[str] = None,
        type: Optional[
            Union[SdkReplaceCourseLessonRequestApplicationJsonType, str]
        ] = None,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        is_preview: Optional[bool] = None,
        is_published: Optional[bool] = None,
        assignment: Optional[
            ReplaceCourseLessonRequestApplicationJsonPropertyAssignment
        ] = None,
        questions: Optional[
            List[ReplaceCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceCourseLessonResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| lesson | `int` | Yes |
| title | `Optional[str]` | No |
| type | `Optional[
            Union[SdkReplaceCourseLessonRequestApplicationJsonType, str]
        ]` | No |
| content | `Union[str, None, NotGiven]` | No |
| is_preview | `Optional[bool]` | No |
| is_published | `Optional[bool]` | No |
| assignment | `Optional[
            ReplaceCourseLessonRequestApplicationJsonPropertyAssignment
        ]` | No |
| questions | `Optional[
            List[ReplaceCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceCourseLessonResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_lessons.replace(
    course="string_example",
    lesson=1,
    title="Welcome",
    is_published=False
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

Update a course lesson

[API reference](https://sell.app/docs/api/courses/manage-course-lessons) · Effect: **write**

```python
def update(
        self,
        course: str,
        lesson: int,
        *,
        title: Optional[str] = None,
        type: Optional[
            Union[SdkUpdateCourseLessonRequestApplicationJsonType, str]
        ] = None,
        content: Union[str, None, NotGiven] = NOT_GIVEN,
        is_preview: Optional[bool] = None,
        is_published: Optional[bool] = None,
        assignment: Optional[
            UpdateCourseLessonRequestApplicationJsonPropertyAssignment
        ] = None,
        questions: Optional[
            List[UpdateCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCourseLessonResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| lesson | `int` | Yes |
| title | `Optional[str]` | No |
| type | `Optional[
            Union[SdkUpdateCourseLessonRequestApplicationJsonType, str]
        ]` | No |
| content | `Union[str, None, NotGiven]` | No |
| is_preview | `Optional[bool]` | No |
| is_published | `Optional[bool]` | No |
| assignment | `Optional[
            UpdateCourseLessonRequestApplicationJsonPropertyAssignment
        ]` | No |
| questions | `Optional[
            List[UpdateCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateCourseLessonResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_lessons.update(
    course="string_example",
    lesson=1,
    title="Welcome",
    is_published=False
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

Delete a course lesson

[API reference](https://sell.app/docs/api/courses/manage-course-lessons) · Effect: **consequential**

```python
def delete(
        self,
        course: str,
        lesson: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| lesson | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_lessons.delete(
    course="string_example",
    lesson=1
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

Reorder course lessons

[API reference](https://sell.app/docs/api/courses/reorder-course-lessons) · Effect: **consequential**

```python
def reorder(
        self,
        course: str,
        *,
        resources: List[
            ReorderCourseLessonsRequestApplicationJsonPropertyResourcesItem
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReorderCourseLessonsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| resources | `List[
            ReorderCourseLessonsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReorderCourseLessonsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.courses_lessons.reorder(
    course="string_example",
    resources=[{"id": 601, "section_id": 501}, {"id": 602, "section_id": 501}]
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

