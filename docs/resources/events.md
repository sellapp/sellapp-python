# events

[All resources](../methods.md)

## list_integration_events

List integration events

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```python
def list_integration_events(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        cursor: str | None = None,
        type: str | None = None,
        subject_type: Literal["order"] | None = None,
        subject_id: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListIntegrationEventsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| cursor | `str \| None` | No |
| type | `str \| None` | No |
| subject_type | `Literal["order"] \| None` | No |
| subject_id | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListIntegrationEventsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.events.list_integration_events()
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_order_events

List order events

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```python
def list_order_events(
        self,
        order: int,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order_: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListOrderEventsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order_ | `str \| None` | No |
| cursor | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListOrderEventsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.events.list_order_events(order=42)
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

