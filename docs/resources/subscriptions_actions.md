# subscriptions_actions

[All resources](../methods.md)

## list

List subscription actions

[API reference](https://sell.app/docs/api/subscriptions/list-subscription-actions) · Effect: **read**

```python
def list(
        self,
        product_subscription: int,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkListSubscriptionActionsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkListSubscriptionActionsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions_actions.list(product_subscription=124)
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

## get

Retrieve a subscription action

[API reference](https://sell.app/docs/api/subscriptions/retrieve-a-subscription-action) · Effect: **read**

```python
def get(
        self,
        product_subscription: int,
        action: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSubscriptionActionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| action | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSubscriptionActionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions_actions.get(
    product_subscription=124,
    action=4192
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

## dismiss

Dismiss a subscription action

[API reference](https://sell.app/docs/api/subscriptions/dismiss-a-subscription-action) · Effect: **consequential**

```python
def dismiss(
        self,
        product_subscription: int,
        action: int,
        *,
        note: str,
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkDismissSubscriptionActionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| action | `int` | Yes |
| note | `str` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkDismissSubscriptionActionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions_actions.dismiss(
    product_subscription=124,
    action=4207,
    note="Confirmed with the customer that they no longer want the upgrade."
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

