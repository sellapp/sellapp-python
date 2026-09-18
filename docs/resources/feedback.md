# feedback

[All resources](../methods.md)

## list

List all feedback

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

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
    ) -> SyncPage[ListFeedbackResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListFeedbackResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.list()
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

## get

Retrieve specific feedback

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def get(
        self,
        feedback: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetFeedbackResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.get(feedback=1)
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

## reply

Reply to feedback

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def reply(
        self,
        feedback: int,
        *,
        reply: str,
        request_options: RequestOptions | None = None,
    ) -> SdkReplyToFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| reply | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplyToFeedbackResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.reply(
    feedback=1,
    reply="Please contact support if you need help with your download."
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

Search feedback

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[SearchFeedbackRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[SearchFeedbackRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchFeedbackRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchFeedbackRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchFeedbackResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[SearchFeedbackRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[SearchFeedbackRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchFeedbackRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchFeedbackRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SearchFeedbackResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.search(
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

## v2_list_feedback

List all feedback

[API reference](https://sell.app/docs/api/feedback/list-all-feedback) · Effect: **read**

```python
def v2_list_feedback(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[V2ListFeedbackResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[V2ListFeedbackResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.v2_list_feedback()
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

## v2_search_feedback

Search feedback

[API reference](https://sell.app/docs/api/feedback/search-feedback) · Effect: **read**

```python
def v2_search_feedback(
        self,
        *,
        filters: builtins.list[
            V2SearchFeedbackRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[V2SearchFeedbackRequestApplicationJsonPropertySortItem]
        | None = None,
        search: V2SearchFeedbackRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            V2SearchFeedbackRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[V2SearchFeedbackResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[
            V2SearchFeedbackRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[V2SearchFeedbackRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `V2SearchFeedbackRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            V2SearchFeedbackRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[V2SearchFeedbackResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.v2_search_feedback(
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

## v2_get_feedback

Retrieve specific feedback

[API reference](https://sell.app/docs/api/feedback/retrieve-specific-feedback) · Effect: **read**

```python
def v2_get_feedback(
        self,
        feedback: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkV2GetFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2GetFeedbackResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.v2_get_feedback(feedback=1)
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

## v2_replace_feedback

Reply to feedback

[API reference](https://sell.app/docs/api/feedback) · Effect: **consequential**

```python
def v2_replace_feedback(
        self,
        feedback: int,
        *,
        reply: str,
        request_options: RequestOptions | None = None,
    ) -> SdkV2ReplaceFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| reply | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2ReplaceFeedbackResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.v2_replace_feedback(
    feedback=1,
    reply="Please contact support if you need help with your download."
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

## v2_reply_to_feedback

Reply to feedback

[API reference](https://sell.app/docs/api/feedback/reply-to-feedback) · Effect: **consequential**

```python
def v2_reply_to_feedback(
        self,
        feedback: int,
        *,
        reply: str,
        request_options: RequestOptions | None = None,
    ) -> SdkV2ReplyToFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| reply | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2ReplyToFeedbackResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.feedback.v2_reply_to_feedback(
    feedback=1,
    reply="Please contact support if you need help with your download."
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

