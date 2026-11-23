# products_similar_products

[All resources](../methods.md)

## list

List product similar products

[API reference](https://sell.app/docs/api/products/product-similar-products) · Effect: **read**

```python
def list(
        self,
        product: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkListProductSimilarProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListProductSimilarProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products_similar_products.list(product=30)
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

Replace product similar products

[API reference](https://sell.app/docs/api/products/product-similar-products) · Effect: **write**

```python
def replace(
        self,
        product: int,
        *,
        variant_ids: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceProductSimilarProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant_ids | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceProductSimilarProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products_similar_products.replace(
    product=30,
    variant_ids=[31, 41]
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

