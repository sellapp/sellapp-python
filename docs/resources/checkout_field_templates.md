# checkout_field_templates

[All resources](../methods.md)

## list

List checkout field templates

[API reference](https://sell.app/docs/api/checkout-field-templates/list-checkout-field-templates) · Effect: **read**

```python
def list(
        self,
        *,
        search: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkListCheckoutFieldTemplatesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| search | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListCheckoutFieldTemplatesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.checkout_field_templates.list()
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

Create a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/create-a-checkout-field-template) · Effect: **consequential**

```python
def create(
        self,
        *,
        name: str,
        fields: builtins.list[
            CreateCheckoutFieldTemplateRequestApplicationJsonPropertyFieldsItem
        ],
        request_options: RequestOptions | None = None,
    ) -> SdkCreateCheckoutFieldTemplateResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| fields | `builtins.list[
            CreateCheckoutFieldTemplateRequestApplicationJsonPropertyFieldsItem
        ]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateCheckoutFieldTemplateResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.checkout_field_templates.create(
    name="Discord access",
    fields=[
        {
            "type": "text",
            "label": "Discord username",
            "key": "discord_username",
            "required": True,
            "placeholder": "name#0001",
            "description": "We add this account to the community after purchase."
        },
        {
            "type": "radio",
            "label": "Experience level",
            "key": "experience_level",
            "required": False,
            "options": ["Beginner", "Intermediate", "Advanced"],
            "variant": "cards",
            "variant_options": {"vertical": True, "indicator": True}
        }
    ]
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

Retrieve a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/retrieve-a-checkout-field-template) · Effect: **read**

```python
def get(
        self,
        checkout_field_template: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCheckoutFieldTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCheckoutFieldTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.checkout_field_templates.get(checkout_field_template=14)
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

Update a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/update-a-checkout-field-template) · Effect: **consequential**

```python
def replace(
        self,
        checkout_field_template: int,
        *,
        name: str | None = None,
        fields: builtins.list[
            ReplaceCheckoutFieldTemplateRequestApplicationJsonPropertyFieldsItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCheckoutFieldTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `int` | Yes |
| name | `str \| None` | No |
| fields | `builtins.list[
            ReplaceCheckoutFieldTemplateRequestApplicationJsonPropertyFieldsItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceCheckoutFieldTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.checkout_field_templates.replace(
    checkout_field_template=14,
    name="Discord onboarding",
    expected_updated_at="2026-09-04T09:00:00.000000Z"
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

Update a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/update-a-checkout-field-template) · Effect: **consequential**

```python
def update(
        self,
        checkout_field_template: int,
        *,
        name: str | None = None,
        fields: builtins.list[
            UpdateCheckoutFieldTemplateRequestApplicationJsonPropertyFieldsItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCheckoutFieldTemplateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `int` | Yes |
| name | `str \| None` | No |
| fields | `builtins.list[
            UpdateCheckoutFieldTemplateRequestApplicationJsonPropertyFieldsItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCheckoutFieldTemplateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.checkout_field_templates.update(
    checkout_field_template=14,
    name="Discord onboarding",
    expected_updated_at="2026-09-04T09:00:00.000000Z"
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

Delete a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/delete-a-checkout-field-template) · Effect: **consequential**

```python
def delete(
        self,
        checkout_field_template: int,
        *,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `int` | Yes |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.checkout_field_templates.delete(
    checkout_field_template=14,
    expected_updated_at="2026-09-04T09:00:00.000000Z"
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

## duplicate

Duplicate a checkout field template

[API reference](https://sell.app/docs/api/checkout-field-templates/duplicate-a-checkout-field-template) · Effect: **consequential**

```python
def duplicate(
        self,
        checkout_field_template: int,
        *,
        name: str,
        request_options: RequestOptions | None = None,
    ) -> SdkDuplicateCheckoutFieldTemplateResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| checkout_field_template | `int` | Yes |
| name | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkDuplicateCheckoutFieldTemplateResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.checkout_field_templates.duplicate(
    checkout_field_template=14,
    name="Discord access for courses"
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

Documented HTTP responses: 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

