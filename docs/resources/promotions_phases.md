# promotions_phases

[All resources](../methods.md)

## list

List promotion phases

[API reference](https://sell.app/docs/api/promotions/replace-promotion-phases) · Effect: **read**

```python
def list(
        self,
        promotion: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListPromotionPhasesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListPromotionPhasesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions_phases.list(promotion=1)
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

Replace promotion phases

[API reference](https://sell.app/docs/api/promotions/replace-promotion-phases) · Effect: **consequential**

```python
def replace(
        self,
        promotion: int,
        *,
        phases: List[ReplacePromotionPhasesRequestApplicationJsonPropertyPhasesItem],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplacePromotionPhasesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| phases | `List[ReplacePromotionPhasesRequestApplicationJsonPropertyPhasesItem]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplacePromotionPhasesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions_phases.replace(
    promotion=1,
    phases=[
        {
            "discount_type": "percentage",
            "discount_value": "20",
            "ends_at": "2026-08-04T00:00:00Z",
            "max_redemptions": 200,
            "minimum_amount": "10"
        },
        {
            "discount_type": "fixed",
            "discount_value": "5",
            "ends_at": None,
            "max_redemptions": None,
            "minimum_amount": "25"
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

