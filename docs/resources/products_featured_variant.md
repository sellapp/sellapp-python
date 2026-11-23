# products_featured_variant

[All resources](../methods.md)

## get

Retrieve product featured variant

[API reference](https://sell.app/docs/api/products/product-featured-variant) · Effect: **read**

```python
def get(
        self,
        product: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetProductFeaturedVariantResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetProductFeaturedVariantResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products_featured_variant.get(product=1)
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

Replace product featured variant

[API reference](https://sell.app/docs/api/products/product-featured-variant) · Effect: **write**

```python
def replace(
        self,
        product: int,
        *,
        variant_id: int | None,
        highlight_label: HighlightLabel | str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceProductFeaturedVariantResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant_id | `int \| None` | Yes |
| highlight_label | `HighlightLabel \| str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceProductFeaturedVariantResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products_featured_variant.replace(
    product=1,
    variant_id=2,
    highlight_label="best_value"
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

