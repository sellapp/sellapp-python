# tickets

[All resources](../methods.md)

## list

List all tickets

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
    ) -> SyncPage[ListTicketsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListTicketsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.list()
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

Retrieve specific ticket

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def get(
        self,
        ticket: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetTicketResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetTicketResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.get(ticket=1)
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

Search tickets

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[SearchTicketsRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[SearchTicketsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchTicketsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[SearchTicketsRequestApplicationJsonPropertyIncludesItem]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchTicketsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[SearchTicketsRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[SearchTicketsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchTicketsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[SearchTicketsRequestApplicationJsonPropertyIncludesItem]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SearchTicketsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.search(
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

## v2_list_tickets

List all tickets

[API reference](https://sell.app/docs/api/tickets/list-all-tickets) · Effect: **read**

```python
def v2_list_tickets(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        waiting_on: TicketsWaitingOn | str | None = None,
        reason: str | None = None,
        customer_email: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[V2ListTicketsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| waiting_on | `TicketsWaitingOn \| str \| None` | No |
| reason | `str \| None` | No |
| customer_email | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[V2ListTicketsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.v2_list_tickets()
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

## v2_search_tickets

Search tickets

[API reference](https://sell.app/docs/api/tickets/search-tickets) · Effect: **read**

```python
def v2_search_tickets(
        self,
        *,
        filters: builtins.list[V2SearchTicketsRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[V2SearchTicketsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: V2SearchTicketsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            V2SearchTicketsRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        waiting_on: WaitingOn | str | None | NotGiven = NOT_GIVEN,
        reason: str | None | NotGiven = NOT_GIVEN,
        customer_email: str | None | NotGiven = NOT_GIVEN,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[V2SearchTicketsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[V2SearchTicketsRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[V2SearchTicketsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `V2SearchTicketsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            V2SearchTicketsRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| waiting_on | `WaitingOn \| str \| None \| NotGiven` | No |
| reason | `str \| None \| NotGiven` | No |
| customer_email | `str \| None \| NotGiven` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[V2SearchTicketsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.v2_search_tickets(
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

## v2_get_ticket

Retrieve specific ticket

[API reference](https://sell.app/docs/api/tickets/retrieve-specific-ticket) · Effect: **read**

```python
def v2_get_ticket(
        self,
        ticket: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkV2GetTicketResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2GetTicketResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.v2_get_ticket(ticket=1)
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

Close, reopen, or archive a ticket

[API reference](https://sell.app/docs/api/tickets/retrieve-specific-ticket) · Effect: **consequential**

```python
def update(
        self,
        ticket: int,
        *,
        status: SdkUpdateTicketRequestApplicationJsonStatus | str | None = None,
        archived: bool | None = None,
        outcome: SdkUpdateTicketRequestApplicationJsonOutcome | str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateTicketResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| status | `SdkUpdateTicketRequestApplicationJsonStatus \| str \| None` | No |
| archived | `bool \| None` | No |
| outcome | `SdkUpdateTicketRequestApplicationJsonOutcome \| str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateTicketResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.update(
    ticket=42,
    status="CLOSED",
    archived=True,
    outcome="delivered"
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

## batch_update

Update several tickets

[API reference](https://sell.app/docs/api/tickets/update-several-tickets) · Effect: **consequential**

```python
def batch_update(
        self,
        *,
        action: SdkBatchUpdateTicketsRequestApplicationJsonAction | str,
        resources: builtins.list[int],
        outcome: SdkBatchUpdateTicketsRequestApplicationJsonOutcome | str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkBatchUpdateTicketsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| action | `SdkBatchUpdateTicketsRequestApplicationJsonAction \| str` | Yes |
| resources | `builtins.list[int]` | Yes |
| outcome | `SdkBatchUpdateTicketsRequestApplicationJsonOutcome \| str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkBatchUpdateTicketsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.batch_update(
    action="close",
    outcome="delivered",
    resources=[311, 313]
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_context

Retrieve a ticket's customer and refund context

[API reference](https://sell.app/docs/api/tickets/retrieve-ticket-context) · Effect: **read**

```python
def get_context(
        self,
        ticket: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkV2GetTicketContextResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkV2GetTicketContextResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.tickets.get_context(ticket=312)
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

