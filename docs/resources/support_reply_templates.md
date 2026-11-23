# support_reply_templates

[All resources](../methods.md)

## list

List support reply templates

[API reference](https://sell.app/docs/api/support-reply-templates/list-support-reply-templates) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        active_state: SupportReplyTemplatesActiveState | str | None = None,
        availability: SupportReplyTemplatesAvailability | str | None = None,
        search: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        ListSupportReplyTemplatesResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| active_state | `SupportReplyTemplatesActiveState \| str \| None` | No |
| availability | `SupportReplyTemplatesAvailability \| str \| None` | No |
| search | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        ListSupportReplyTemplatesResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.list()
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

Create a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/create-a-support-reply-template) · Effect: **consequential**

```python
def create(
        self,
        *,
        label: str,
        body: str,
        is_active: bool | None = None,
        supports_manual: bool | None = None,
        supports_auto_respond: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateSupportReplyTemplateResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| label | `str` | Yes |
| body | `str` | Yes |
| is_active | `bool \| None` | No |
| supports_manual | `bool \| None` | No |
| supports_auto_respond | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateSupportReplyTemplateResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.create(
    label="Refund credited",
    body="Hi {customer_email}, we credited {refund_amount} to your {store_name} wallet for {product_title}. Your wallet balance is now {wallet_balance}.",
    supports_auto_respond=True
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

Retrieve a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/retrieve-a-support-reply-template) · Effect: **read**

```python
def get(
        self,
        support_reply_template: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSupportReplyTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSupportReplyTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.get(support_reply_template=32)
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

Update a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/update-a-support-reply-template) · Effect: **consequential**

```python
def replace(
        self,
        support_reply_template: int,
        *,
        label: str | None = None,
        body: str | None = None,
        is_active: bool | None = None,
        supports_manual: bool | None = None,
        supports_auto_respond: bool | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceSupportReplyTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `int` | Yes |
| label | `str \| None` | No |
| body | `str \| None` | No |
| is_active | `bool \| None` | No |
| supports_manual | `bool \| None` | No |
| supports_auto_respond | `bool \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceSupportReplyTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.replace(
    support_reply_template=31,
    is_active=False,
    expected_updated_at="2026-07-03T09:12:00.000000Z"
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

Update a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/update-a-support-reply-template) · Effect: **consequential**

```python
def update(
        self,
        support_reply_template: int,
        *,
        label: str | None = None,
        body: str | None = None,
        is_active: bool | None = None,
        supports_manual: bool | None = None,
        supports_auto_respond: bool | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateSupportReplyTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `int` | Yes |
| label | `str \| None` | No |
| body | `str \| None` | No |
| is_active | `bool \| None` | No |
| supports_manual | `bool \| None` | No |
| supports_auto_respond | `bool \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateSupportReplyTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.update(
    support_reply_template=31,
    is_active=False,
    expected_updated_at="2026-07-03T09:12:00.000000Z"
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

Delete a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/delete-a-support-reply-template) · Effect: **consequential**

```python
def delete(
        self,
        support_reply_template: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.delete(support_reply_template=33)
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

## render

Render a support reply template

[API reference](https://sell.app/docs/api/support-reply-templates/render-a-support-reply-template) · Effect: **consequential**

```python
def render(
        self,
        support_reply_template: int,
        *,
        ticket_id: int,
        values: RenderSupportReplyTemplateRequestApplicationJsonPropertyValues
        | None = None,
        invoice_id: int | None | NotGiven = NOT_GIVEN,
        refund_amount_cents: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkRenderSupportReplyTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_reply_template | `int` | Yes |
| ticket_id | `int` | Yes |
| values | `RenderSupportReplyTemplateRequestApplicationJsonPropertyValues
        \| None` | No |
| invoice_id | `int \| None \| NotGiven` | No |
| refund_amount_cents | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkRenderSupportReplyTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.render(
    support_reply_template=1,
    ticket_id=4821,
    invoice_id=7001,
    refund_amount_cents=999
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

## reorder

Reorder support reply templates

[API reference](https://sell.app/docs/api/support-reply-templates/reorder-support-reply-templates) · Effect: **consequential**

```python
def reorder(
        self,
        *,
        ordered_template_ids: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> SdkReorderSupportReplyTemplatesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ordered_template_ids | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReorderSupportReplyTemplatesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.reorder(ordered_template_ids=[32, 31])
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

## get_options

Retrieve support reply template options

[API reference](https://sell.app/docs/api/support-reply-templates/support-reply-template-options) · Effect: **read**

```python
def get_options(
        self,
        *,
        body: str | None = None,
        requested_placeholders: builtins.list[str] | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSupportReplyTemplateOptionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| body | `str \| None` | No |
| requested_placeholders | `builtins.list[str] \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSupportReplyTemplateOptionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_reply_templates.get_options()
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

