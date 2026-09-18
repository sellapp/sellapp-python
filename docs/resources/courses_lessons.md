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
        type: SdkCreateCourseLessonRequestApplicationJsonType | str,
        content: str | None | NotGiven = NOT_GIVEN,
        is_preview: bool | None = None,
        is_published: bool | None = None,
        assignment: CreateCourseLessonRequestApplicationJsonPropertyAssignment
        | None = None,
        questions: list[CreateCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateCourseLessonResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| section | `int` | Yes |
| title | `str` | Yes |
| type | `SdkCreateCourseLessonRequestApplicationJsonType \| str` | Yes |
| content | `str \| None \| NotGiven` | No |
| is_preview | `bool \| None` | No |
| is_published | `bool \| None` | No |
| assignment | `CreateCourseLessonRequestApplicationJsonPropertyAssignment
        \| None` | No |
| questions | `list[CreateCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        title: str | None = None,
        type: SdkReplaceCourseLessonRequestApplicationJsonType | str | None = None,
        content: str | None | NotGiven = NOT_GIVEN,
        is_preview: bool | None = None,
        is_published: bool | None = None,
        assignment: ReplaceCourseLessonRequestApplicationJsonPropertyAssignment
        | None = None,
        questions: list[ReplaceCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCourseLessonResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| lesson | `int` | Yes |
| title | `str \| None` | No |
| type | `SdkReplaceCourseLessonRequestApplicationJsonType \| str \| None` | No |
| content | `str \| None \| NotGiven` | No |
| is_preview | `bool \| None` | No |
| is_published | `bool \| None` | No |
| assignment | `ReplaceCourseLessonRequestApplicationJsonPropertyAssignment
        \| None` | No |
| questions | `list[ReplaceCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        title: str | None = None,
        type: SdkUpdateCourseLessonRequestApplicationJsonType | str | None = None,
        content: str | None | NotGiven = NOT_GIVEN,
        is_preview: bool | None = None,
        is_published: bool | None = None,
        assignment: UpdateCourseLessonRequestApplicationJsonPropertyAssignment
        | None = None,
        questions: list[UpdateCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCourseLessonResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| lesson | `int` | Yes |
| title | `str \| None` | No |
| type | `SdkUpdateCourseLessonRequestApplicationJsonType \| str \| None` | No |
| content | `str \| None \| NotGiven` | No |
| is_preview | `bool \| None` | No |
| is_published | `bool \| None` | No |
| assignment | `UpdateCourseLessonRequestApplicationJsonPropertyAssignment
        \| None` | No |
| questions | `list[UpdateCourseLessonRequestApplicationJsonPropertyQuestionsItem]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| lesson | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        resources: list[
            ReorderCourseLessonsRequestApplicationJsonPropertyResourcesItem
        ],
        request_options: RequestOptions | None = None,
    ) -> SdkReorderCourseLessonsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| course | `str` | Yes |
| resources | `list[
            ReorderCourseLessonsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| request_options | `RequestOptions \| None` | No |

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

