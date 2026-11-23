# affiliates_products

[All resources](../methods.md)

## get

Retrieve affiliate products

[API reference](https://sell.app/docs/api/affiliates/affiliate-products) · Effect: **read**

```python
def get(
        self,
        affiliate: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetAffiliateProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetAffiliateProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliates_products.get(affiliate=88)
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

Update affiliate products

[API reference](https://sell.app/docs/api/affiliates/affiliate-products) · Effect: **consequential**

```python
def update(
        self,
        affiliate: int,
        *,
        enable_specific_products: bool | None = None,
        products: list[
            UpdateAffiliateProductsRequestApplicationJsonPropertyProductsItem
        ]
        | None = None,
        replace_products: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateAffiliateProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| affiliate | `int` | Yes |
| enable_specific_products | `bool \| None` | No |
| products | `list[
            UpdateAffiliateProductsRequestApplicationJsonPropertyProductsItem
        ]
        \| None` | No |
| replace_products | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateAffiliateProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.affiliates_products.update(
    affiliate=88,
    enable_specific_products=True,
    products=[
        {
            "id": 42,
            "enabled": True,
            "commission": {"type": "percentage", "percentage": "25"}
        },
        {
            "id": 43,
            "enabled": True,
            "commission": {"type": "fixed", "amount_usd_cents": 550}
        }
    ],
    replace_products=True
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

