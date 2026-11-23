# community_connections_servers

[All resources](../methods.md)

## get

Retrieve a community server

[API reference](https://sell.app/docs/api/community-connections/community-server) · Effect: **read**

```python
def get(
        self,
        platform: CommunityConnectionsPlatform | str,
        server: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCommunityServerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `CommunityConnectionsPlatform \| str` | Yes |
| server | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCommunityServerResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections_servers.get(
    platform="discord",
    server="server_ship_room"
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

## remove

Remove a community server

[API reference](https://sell.app/docs/api/community-connections/community-server) · Effect: **consequential**

```python
def remove(
        self,
        platform: CommunityConnectionsPlatform | str,
        server: str,
        *,
        affected_variant_ids: list[int] | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| platform | `CommunityConnectionsPlatform \| str` | Yes |
| server | `str` | Yes |
| affected_variant_ids | `list[int] \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections_servers.remove(
    platform="discord",
    server="server_ship_room",
    affected_variant_ids=[902]
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

