# tickets_messages

[All resources](../methods.md)

## list

List all ticket messages

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def list(
        self,
        ticket: int,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListTicketMessagesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListTicketMessagesResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_messages.list(ticket=1)
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

Reply to ticket

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def reply(
        self,
        ticket: int,
        *,
        content: str,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplyToTicketResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| content | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplyToTicketResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_messages.reply(
    ticket=1,
    content="You can choose from the payment methods shown at checkout."
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

Documented HTTP responses: 201, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve specific ticket message

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def get(
        self,
        ticket: int,
        message: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetTicketMessageResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| message | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetTicketMessageResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_messages.get(
    ticket=1,
    message=2
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

Search ticket messages

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def search(
        self,
        ticket: int,
        *,
        filters: Optional[
            List[SearchTicketMessagesRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchTicketMessagesRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[
            SearchTicketMessagesRequestApplicationJsonPropertySearch
        ] = None,
        includes: Optional[
            List[SearchTicketMessagesRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchTicketMessagesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| filters | `Optional[
            List[SearchTicketMessagesRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchTicketMessagesRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[
            SearchTicketMessagesRequestApplicationJsonPropertySearch
        ]` | No |
| includes | `Optional[
            List[SearchTicketMessagesRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SearchTicketMessagesResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_messages.search(
    ticket=1,
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

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v2_list_ticket_messages

List all ticket messages

[API reference](https://sell.app/docs/api/tickets/list-all-ticket-messages) · Effect: **read**

```python
def v2_list_ticket_messages(
        self,
        ticket: int,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[V2ListTicketMessagesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[V2ListTicketMessagesResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_messages.v2_list_ticket_messages(ticket=1)
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

## v2_reply_to_ticket

Reply to ticket

[API reference](https://sell.app/docs/api/tickets/reply-to-ticket) · Effect: **consequential**

```python
def v2_reply_to_ticket(
        self,
        ticket: int,
        *,
        content: str,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2ReplyToTicketResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| content | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2ReplyToTicketResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_messages.v2_reply_to_ticket(
    ticket=1,
    content="You can choose from the payment methods shown at checkout."
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

## v2_search_ticket_messages

Search ticket messages

[API reference](https://sell.app/docs/api/tickets/search-ticket-messages) · Effect: **read**

```python
def v2_search_ticket_messages(
        self,
        ticket: int,
        *,
        filters: Optional[
            List[V2SearchTicketMessagesRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[V2SearchTicketMessagesRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[
            V2SearchTicketMessagesRequestApplicationJsonPropertySearch
        ] = None,
        includes: Optional[
            List[V2SearchTicketMessagesRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[
        V2SearchTicketMessagesResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| filters | `Optional[
            List[V2SearchTicketMessagesRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[V2SearchTicketMessagesRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[
            V2SearchTicketMessagesRequestApplicationJsonPropertySearch
        ]` | No |
| includes | `Optional[
            List[V2SearchTicketMessagesRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[
        V2SearchTicketMessagesResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_messages.v2_search_ticket_messages(
    ticket=1,
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v2_get_ticket_message

Retrieve specific ticket message

[API reference](https://sell.app/docs/api/tickets/retrieve-specific-ticket-message) · Effect: **read**

```python
def v2_get_ticket_message(
        self,
        ticket: int,
        message: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkV2GetTicketMessageResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| message | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkV2GetTicketMessageResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets_messages.v2_get_ticket_message(
    ticket=1,
    message=2
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

