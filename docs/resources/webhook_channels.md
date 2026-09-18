# webhook_channels

[All resources](../methods.md)

## list

List webhook channels

[API reference](https://sell.app/docs/api/webhook-channels/list-webhook-channels) · Effect: **read**

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
    ) -> SyncPage[ListWebhookChannelsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListWebhookChannelsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.list()
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

## create

Create a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/create-a-webhook-channel) · Effect: **consequential**

```python
def create(
        self,
        *,
        url: str,
        allowed_notifications: builtins.list[
            SdkCreateWebhookChannelRequestApplicationJsonAllowedNotifications | str
        ],
        name: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateWebhookChannelResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| url | `str` | Yes |
| allowed_notifications | `builtins.list[
            SdkCreateWebhookChannelRequestApplicationJsonAllowedNotifications \| str
        ]` | Yes |
| name | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateWebhookChannelResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.create(
    name="Ship It webhook",
    url="https://example.com/webhooks/ship-it",
    allowed_notifications=["order.created", "order.paid"]
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search webhook channels

[API reference](https://sell.app/docs/api/webhook-channels/search-webhook-channels) · Effect: **read**

```python
def search(
        self,
        *,
        search: SearchWebhookChannelsRequestApplicationJsonPropertySearch | None = None,
        event: Event | str | None | NotGiven = NOT_GIVEN,
        page: int | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchWebhookChannelsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| search | `SearchWebhookChannelsRequestApplicationJsonPropertySearch \| None` | No |
| event | `Event \| str \| None \| NotGiven` | No |
| page | `int \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SearchWebhookChannelsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.search(
    search={"value": "orders"},
    event="order.paid"
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

## rotate

Rotate the webhook signing secret

[API reference](https://sell.app/docs/api/webhook-channels/rotate-the-signing-secret) · Effect: **consequential**

```python
def rotate(
        self,
        *,
        signing_secret: str,
        request_options: RequestOptions | None = None,
    ) -> SdkRotateWebhookSigningSecretResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| signing_secret | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkRotateWebhookSigningSecretResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.rotate(signing_secret="replace-with-a-random-secret-at-least-32-characters-long")
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

Retrieve a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/retrieve-a-webhook-channel) · Effect: **read**

```python
def get(
        self,
        webhook_channel: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetWebhookChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetWebhookChannelResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.get(webhook_channel="0f33d01f-f9f8-45e8-80c8-7734d057196d")
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

Replace a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/replace-a-webhook-channel) · Effect: **consequential**

```python
def replace(
        self,
        webhook_channel: str,
        *,
        name: str | None,
        url: str,
        allowed_notifications: builtins.list[
            SdkReplaceWebhookChannelRequestApplicationJsonAllowedNotifications | str
        ],
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceWebhookChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| name | `str \| None` | Yes |
| url | `str` | Yes |
| allowed_notifications | `builtins.list[
            SdkReplaceWebhookChannelRequestApplicationJsonAllowedNotifications \| str
        ]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceWebhookChannelResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.replace(
    webhook_channel="0f33d01f-f9f8-45e8-80c8-7734d057196d",
    name="Primary Ship It webhook",
    url="https://example.com/webhooks/ship-it",
    allowed_notifications=["order.paid"]
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

Update a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/update-a-webhook-channel) · Effect: **consequential**

```python
def update(
        self,
        webhook_channel: str,
        *,
        name: str | None | NotGiven = NOT_GIVEN,
        url: str | None = None,
        allowed_notifications: builtins.list[
            SdkUpdateWebhookChannelRequestApplicationJsonAllowedNotifications | str
        ]
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateWebhookChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| name | `str \| None \| NotGiven` | No |
| url | `str \| None` | No |
| allowed_notifications | `builtins.list[
            SdkUpdateWebhookChannelRequestApplicationJsonAllowedNotifications \| str
        ]
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateWebhookChannelResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.update(
    webhook_channel="0f33d01f-f9f8-45e8-80c8-7734d057196d",
    name="Primary Ship It webhook",
    allowed_notifications=["order.paid"]
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

Delete a webhook channel

[API reference](https://sell.app/docs/api/webhook-channels/delete-a-webhook-channel) · Effect: **consequential**

```python
def delete(
        self,
        webhook_channel: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.delete(webhook_channel="0f33d01f-f9f8-45e8-80c8-7734d057196d")
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

## send

Send a test webhook

[API reference](https://sell.app/docs/api/webhook-channels/send-a-test-webhook) · Effect: **consequential**

```python
def send(
        self,
        webhook_channel: str,
        *,
        event: SdkSendTestWebhookRequestApplicationJsonEvent | str,
        request_options: RequestOptions | None = None,
    ) -> SdkSendTestWebhookResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| event | `SdkSendTestWebhookRequestApplicationJsonEvent \| str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkSendTestWebhookResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.webhook_channels.send(
    webhook_channel="0f33d01f-f9f8-45e8-80c8-7734d057196d",
    event="order.created"
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

