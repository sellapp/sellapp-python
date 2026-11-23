# community_connections_slack

[All resources](../methods.md)

## list_channels

List Slack available channels

[API reference](https://sell.app/docs/api/community-connections/slack-channels) · Effect: **read**

```python
def list_channels(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkListSlackAvailableChannelsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListSlackAvailableChannelsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections_slack.list_channels()
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

## add_channel

Add a Slack channel

[API reference](https://sell.app/docs/api/community-connections/slack-channels) · Effect: **consequential**

```python
def add_channel(
        self,
        *,
        channel_id: str,
        request_options: RequestOptions | None = None,
    ) -> SdkAddSlackChannelResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| channel_id | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkAddSlackChannelResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections_slack.add_channel(channel_id="C07LAUNCHVIP")
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

## replace_invite_link

Update Slack workspace invite link

[API reference](https://sell.app/docs/api/community-connections/slack-invite-link) · Effect: **consequential**

```python
def replace_invite_link(
        self,
        *,
        invite_link: str | None | NotGiven = NOT_GIVEN,
        workspace_invite_link: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceSlackWorkspaceInviteLinkResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invite_link | `str \| None \| NotGiven` | No |
| workspace_invite_link | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceSlackWorkspaceInviteLinkResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.community_connections_slack.replace_invite_link(invite_link="https://join.slack.com/t/launch-lab/shared_invite/zt-2abc123")
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

