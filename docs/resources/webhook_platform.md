# webhook_platform

[All resources](../methods.md)

## list_webhook_event_types

List webhook event types

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```python
def list_webhook_event_types(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListWebhookEventTypesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListWebhookEventTypesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_platform.list_webhook_event_types()
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

## list_webhook_deliveries

List webhook deliveries

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```python
def list_webhook_deliveries(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListWebhookDeliveriesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListWebhookDeliveriesResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_platform.list_webhook_deliveries()
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

## get_webhook_delivery

Retrieve a webhook delivery

[API reference](https://sell.app/docs/api/events) · Effect: **read**

```python
def get_webhook_delivery(
        self,
        delivery: str,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetWebhookDeliveryResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| delivery | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetWebhookDeliveryResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_platform.get_webhook_delivery(delivery="01992b31-c8bd-75b5-b02d-6ae0aa418940")
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

## replay_webhook_delivery

Replay a webhook delivery

[API reference](https://sell.app/docs/api/events) · Effect: **consequential**

```python
def replay_webhook_delivery(
        self,
        delivery: str,
        *,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplayWebhookDeliveryResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| delivery | `str` | Yes |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplayWebhookDeliveryResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_platform.replay_webhook_delivery(
    delivery="delivery_01K4CUSTOMER",
    idempotency_key="example-mutation-001"
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

