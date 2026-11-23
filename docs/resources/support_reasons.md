# support_reasons

[All resources](../methods.md)

## list

List support reasons

[API reference](https://sell.app/docs/api/support-reasons/list-support-reasons) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        active_state: SupportReasonsActiveState | str | None = None,
        product_scope: SupportReasonsProductScope | str | None = None,
        search: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListSupportReasonsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| active_state | `SupportReasonsActiveState \| str \| None` | No |
| product_scope | `SupportReasonsProductScope \| str \| None` | No |
| search | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListSupportReasonsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reasons.list()
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

Create a support reason

[API reference](https://sell.app/docs/api/support-reasons/create-a-support-reason) · Effect: **consequential**

```python
def create(
        self,
        *,
        label: str,
        description: str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        product_ids: builtins.list[int] | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateSupportReasonResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| label | `str` | Yes |
| description | `str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| product_ids | `builtins.list[int] \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateSupportReasonResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reasons.create(
    label="Download link expired",
    description="The download link in the order email no longer works."
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

## get

Retrieve a support reason

[API reference](https://sell.app/docs/api/support-reasons/retrieve-a-support-reason) · Effect: **read**

```python
def get(
        self,
        support_reason: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSupportReasonResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reason | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSupportReasonResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reasons.get(support_reason=14)
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

Update a support reason

[API reference](https://sell.app/docs/api/support-reasons/update-a-support-reason) · Effect: **consequential**

```python
def replace(
        self,
        support_reason: int,
        *,
        label: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        product_ids: builtins.list[int] | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceSupportReasonResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reason | `int` | Yes |
| label | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| product_ids | `builtins.list[int] \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceSupportReasonResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reasons.replace(
    support_reason=14,
    description="The download link in the order email no longer opens.",
    expected_updated_at="2026-07-03T09:10:00.000000Z"
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

Update a support reason

[API reference](https://sell.app/docs/api/support-reasons/update-a-support-reason) · Effect: **consequential**

```python
def update(
        self,
        support_reason: int,
        *,
        label: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        product_ids: builtins.list[int] | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateSupportReasonResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reason | `int` | Yes |
| label | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| product_ids | `builtins.list[int] \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateSupportReasonResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reasons.update(
    support_reason=14,
    description="The download link in the order email no longer opens.",
    expected_updated_at="2026-07-03T09:10:00.000000Z"
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

Delete a support reason

[API reference](https://sell.app/docs/api/support-reasons/delete-a-support-reason) · Effect: **consequential**

```python
def delete(
        self,
        support_reason: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reason | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reasons.delete(support_reason=15)
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

## get_options

Retrieve support reason options

[API reference](https://sell.app/docs/api/support-reasons/support-reason-options) · Effect: **read**

```python
def get_options(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSupportReasonOptionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSupportReasonOptionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reasons.get_options()
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

