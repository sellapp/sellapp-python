# store_notification_channels

[All resources](../methods.md)

## list

List notification channels

[API reference](https://sell.app/docs/api/store-settings/list-notification-channels) · Effect: **read**

```python
def list(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkListNotificationChannelsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListNotificationChannelsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_notification_channels.list()
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

Create a notification channel

[API reference](https://sell.app/docs/api/store-settings/create-notification-channel) · Effect: **consequential**

```python
def create(
        self,
        *,
        channel: CreateNotificationChannelRequestApplicationJsonPropertyChannel,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateNotificationChannelResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| channel | `CreateNotificationChannelRequestApplicationJsonPropertyChannel` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateNotificationChannelResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_notification_channels.create(channel={"type": "email", "email": "maya@example.com", "allowed_notifications": []})
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

## get

Retrieve a notification channel

[API reference](https://sell.app/docs/api/store-settings/manage-notification-channel) · Effect: **read**

```python
def get(
        self,
        notification_channel: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetNotificationChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| notification_channel | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetNotificationChannelResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_notification_channels.get(notification_channel="string_example")
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

Update a notification channel

[API reference](https://sell.app/docs/api/store-settings/manage-notification-channel) · Effect: **consequential**

```python
def replace(
        self,
        notification_channel: str,
        *,
        channel: ReplaceNotificationChannelRequestApplicationJsonPropertyChannel,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceNotificationChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| notification_channel | `str` | Yes |
| channel | `ReplaceNotificationChannelRequestApplicationJsonPropertyChannel` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceNotificationChannelResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_notification_channels.replace(
    notification_channel="string_example",
    channel={"type": "email", "email": "maya@example.com", "allowed_notifications": []}
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

Update a notification channel

[API reference](https://sell.app/docs/api/store-settings/manage-notification-channel) · Effect: **consequential**

```python
def update(
        self,
        notification_channel: str,
        *,
        channel: UpdateNotificationChannelRequestApplicationJsonPropertyChannel,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateNotificationChannelResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| notification_channel | `str` | Yes |
| channel | `UpdateNotificationChannelRequestApplicationJsonPropertyChannel` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateNotificationChannelResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_notification_channels.update(
    notification_channel="string_example",
    channel={"allowed_notifications": []}
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

Delete a notification channel

[API reference](https://sell.app/docs/api/store-settings/manage-notification-channel) · Effect: **consequential**

```python
def delete(
        self,
        notification_channel: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| notification_channel | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_notification_channels.delete(notification_channel="string_example")
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

