# feedback

[All resources](../methods.md)

## list

List all feedback

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
    ) -> SyncPage[ListFeedbackResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplyToFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| reply | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchFeedbackRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchFeedbackRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchFeedbackRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchFeedbackRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchFeedbackResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchFeedbackRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchFeedbackRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchFeedbackRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchFeedbackRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[V2ListFeedbackResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[V2SearchFeedbackRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[V2SearchFeedbackRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[V2SearchFeedbackRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[V2SearchFeedbackRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[V2SearchFeedbackResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[V2SearchFeedbackRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[V2SearchFeedbackRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[V2SearchFeedbackRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[V2SearchFeedbackRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2GetFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2ReplaceFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| reply | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2ReplyToFeedbackResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| feedback | `int` | Yes |
| reply | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

