# product_variants_community_access

[All resources](../methods.md)

## replace

Replace variant community access

[API reference](https://sell.app/docs/api/product-variants/replace-variant-community-access) · Effect: **write**

```python
def replace(
        self,
        product: int,
        variant: int,
        *,
        community: ReplaceVariantCommunityAccessRequestApplicationJsonPropertyCommunity,
        expected_updated_at: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceVariantCommunityAccessResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| community | `ReplaceVariantCommunityAccessRequestApplicationJsonPropertyCommunity` | Yes |
| expected_updated_at | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceVariantCommunityAccessResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_community_access.replace(
    product=1,
    variant=2,
    community={
        "platform": "discord",
        "server_id": "1187040134912155648",
        "role_ids": ["1187040299781210112"],
        "required": True,
        "remove_on_expire": True
    },
    expected_updated_at="2024-01-10T18:47:22.000000Z"
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

