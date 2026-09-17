# webhook_channels

[All resources](../methods.md)

## list

List webhook channels

[API reference](https://sell.app/docs/api/webhook-channels/list-webhook-channels) · Effect: **read**

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
    ) -> SyncPage[ListWebhookChannelsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        allowed_notifications: List[
            Union[
                SdkCreateWebhookChannelRequestApplicationJsonAllowedNotifications, str
            ]
        ],
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateWebhookChannelResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| url | `str` | Yes |
| allowed_notifications | `List[
            Union[
                SdkCreateWebhookChannelRequestApplicationJsonAllowedNotifications, str
            ]
        ]` | Yes |
| name | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        search: Optional[
            SearchWebhookChannelsRequestApplicationJsonPropertySearch
        ] = None,
        event: Union[Union[Event, str], None, NotGiven] = NOT_GIVEN,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchWebhookChannelsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| search | `Optional[
            SearchWebhookChannelsRequestApplicationJsonPropertySearch
        ]` | No |
| event | `Union[Union[Event, str], None, NotGiven]` | No |
| page | `Optional[int]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkRotateWebhookSigningSecretResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| signing_secret | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetWebhookChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Optional[str],
        url: str,
        allowed_notifications: List[
            Union[
                SdkReplaceWebhookChannelRequestApplicationJsonAllowedNotifications, str
            ]
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceWebhookChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| name | `Optional[str]` | Yes |
| url | `str` | Yes |
| allowed_notifications | `List[
            Union[
                SdkReplaceWebhookChannelRequestApplicationJsonAllowedNotifications, str
            ]
        ]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        url: Optional[str] = None,
        allowed_notifications: Optional[
            List[
                Union[
                    SdkUpdateWebhookChannelRequestApplicationJsonAllowedNotifications,
                    str,
                ]
            ]
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateWebhookChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| name | `Union[str, None, NotGiven]` | No |
| url | `Optional[str]` | No |
| allowed_notifications | `Optional[
            List[
                Union[
                    SdkUpdateWebhookChannelRequestApplicationJsonAllowedNotifications,
                    str,
                ]
            ]
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        event: Union[SdkSendTestWebhookRequestApplicationJsonEvent, str],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkSendTestWebhookResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| webhook_channel | `str` | Yes |
| event | `Union[SdkSendTestWebhookRequestApplicationJsonEvent, str]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

