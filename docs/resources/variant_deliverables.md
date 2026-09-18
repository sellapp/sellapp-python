# variant_deliverables

[All resources](../methods.md)

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

