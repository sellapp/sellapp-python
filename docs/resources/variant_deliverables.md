# variant_deliverables

[All resources](../methods.md)

## preview

Preview variant buyer notification

[API reference](https://sell.app/docs/api/product-variants/notify-variant-buyers) · Effect: **read**

```python
def preview(
        self,
        product: int,
        variant: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkPreviewVariantBuyerNotificationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkPreviewVariantBuyerNotificationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverables.preview(
    product=1,
    variant=2
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

## notify

Notify variant buyers

[API reference](https://sell.app/docs/api/product-variants/notify-variant-buyers) · Effect: **write**

```python
def notify(
        self,
        product: int,
        variant: int,
        *,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkNotifyVariantBuyersResponseValue202ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkNotifyVariantBuyersResponseValue202ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverables.notify(
    product=1,
    variant=2,
    idempotency_key="example-mutation-001"
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

Documented HTTP responses: 202, 400, 401, 403, 404, 409, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve variant deliverable configuration

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```python
def get(
        self,
        product: str,
        variant: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetVariantDeliverableConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetVariantDeliverableConfigurationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverables.get(
    product="string_example",
    variant=1
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

## replace

Replace variant deliverable configuration

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def replace(
        self,
        product: str,
        variant: int,
        *,
        types: list[
            SdkReplaceVariantDeliverableConfigurationRequestApplicationJsonTypes | str
        ],
        data: ReplaceVariantDeliverableConfigurationRequestApplicationJsonPropertyData,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceVariantDeliverableConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| types | `list[
            SdkReplaceVariantDeliverableConfigurationRequestApplicationJsonTypes \| str
        ]` | Yes |
| data | `ReplaceVariantDeliverableConfigurationRequestApplicationJsonPropertyData` | Yes |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceVariantDeliverableConfigurationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverables.replace(
    product="string_example",
    variant=1,
    types=["MANUAL"],
    data={"comment": "Delivery is arranged by Launch Lab."}
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

