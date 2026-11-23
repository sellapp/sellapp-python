# community_connections

[All resources](../methods.md)

## list

List community connections

[API reference](https://sell.app/docs/api/community-connections) · Effect: **read**

```python
def list(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkListCommunityConnectionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListCommunityConnectionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections.list()
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

## start

Start a community connection

[API reference](https://sell.app/docs/api/community-connections) · Effect: **consequential**

```python
def start(
        self,
        platform: CommunityConnectionsPlatform | str,
        *,
        mode: SdkStartCommunityConnectionRequestApplicationJsonMode | str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkStartCommunityConnectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `CommunityConnectionsPlatform \| str` | Yes |
| mode | `SdkStartCommunityConnectionRequestApplicationJsonMode \| str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkStartCommunityConnectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections.start(
    platform="discord",
    mode="official_bot"
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

## poll

Poll a community connection

[API reference](https://sell.app/docs/api/community-connections) · Effect: **read**

```python
def poll(
        self,
        platform: CommunityConnectionsPlatform | str,
        *,
        status_token: str,
        request_options: RequestOptions | None = None,
    ) -> SdkPollCommunityConnectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `CommunityConnectionsPlatform \| str` | Yes |
| status_token | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkPollCommunityConnectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections.poll(
    platform="discord",
    status_token="string_example"
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

## complete

Complete a community connection

[API reference](https://sell.app/docs/api/community-connections) · Effect: **consequential**

```python
def complete(
        self,
        platform: CommunityConnectionsPlatform | str,
        *,
        status_token: str,
        server_id: str,
        request_options: RequestOptions | None = None,
    ) -> SdkCompleteCommunityConnectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `CommunityConnectionsPlatform \| str` | Yes |
| status_token | `str` | Yes |
| server_id | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCompleteCommunityConnectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections.complete(
    platform="whatsapp",
    status_token="replace-with-token-from-connection-start",
    server_id="replace-with-returned-server-id"
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

## verify

Verify a community connection

[API reference](https://sell.app/docs/api/community-connections) · Effect: **consequential**

```python
def verify(
        self,
        platform: CommunityConnectionsPlatform | str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkVerifyCommunityConnectionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `CommunityConnectionsPlatform \| str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkVerifyCommunityConnectionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections.verify(platform="discord")
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

## disconnect

Disconnect a community platform

[API reference](https://sell.app/docs/api/community-connections) · Effect: **consequential**

```python
def disconnect(
        self,
        platform: CommunityConnectionsPlatform | str,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `CommunityConnectionsPlatform \| str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections.disconnect(platform="discord")
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

## list_failed_grant_reasons

List community failed grant reasons

[API reference](https://sell.app/docs/api/community-connections/list-failed-grant-reasons) · Effect: **read**

```python
def list_failed_grant_reasons(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkListCommunityFailedGrantReasonsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListCommunityFailedGrantReasonsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections.list_failed_grant_reasons()
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

## sync_discord_roles

Sync Discord roles

[API reference](https://sell.app/docs/api/community-connections/sync-discord-roles) · Effect: **consequential**

```python
def sync_discord_roles(
        self,
        *,
        server_id: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkSyncDiscordRolesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| server_id | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkSyncDiscordRolesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections.sync_discord_roles()
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

