# product_variants_pricing

[All resources](../methods.md)

## replace

Replace product variant pricing

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def replace(
        self,
        product: int,
        variant: int,
        *,
        pricing: ReplaceProductVariantPricingRequestApplicationJsonPropertyPricing,
        payment_methods: list[
            SdkReplaceProductVariantPricingRequestApplicationJsonPaymentMethods | str
        ],
        custom_payment_method_ids: list[str] | None = None,
        bulk_discount: list[
            ReplaceProductVariantPricingRequestApplicationJsonPropertyBulkDiscountItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceProductVariantPricingResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| pricing | `ReplaceProductVariantPricingRequestApplicationJsonPropertyPricing` | Yes |
| payment_methods | `list[
            SdkReplaceProductVariantPricingRequestApplicationJsonPaymentMethods \| str
        ]` | Yes |
| custom_payment_method_ids | `list[str] \| None` | No |
| bulk_discount | `list[
            ReplaceProductVariantPricingRequestApplicationJsonPropertyBulkDiscountItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceProductVariantPricingResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_pricing.replace(
    product=120,
    variant=4321,
    pricing={
        "type": "SUBSCRIPTION",
        "humble": False,
        "price": {"price": 1999, "currency": "USD"},
        "frequency": {"value": 1, "interval": "MONTH"}
    },
    payment_methods=["STRIPE"]
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

Partially update product variant pricing

[API reference](https://sell.app/docs/api/product-variants/update-product-variant-pricing) · Effect: **write**

```python
def update(
        self,
        product: int,
        variant: int,
        *,
        pricing: UpdateProductVariantPricingRequestApplicationJsonPropertyPricing
        | None = None,
        payment_methods: list[
            SdkUpdateProductVariantPricingRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        custom_payment_method_ids: list[str] | None = None,
        bulk_discount: list[
            UpdateProductVariantPricingRequestApplicationJsonPropertyBulkDiscountItem
        ]
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateProductVariantPricingResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| pricing | `UpdateProductVariantPricingRequestApplicationJsonPropertyPricing
        \| None` | No |
| payment_methods | `list[
            SdkUpdateProductVariantPricingRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| custom_payment_method_ids | `list[str] \| None` | No |
| bulk_discount | `list[
            UpdateProductVariantPricingRequestApplicationJsonPropertyBulkDiscountItem
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateProductVariantPricingResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_pricing.update(
    product=120,
    variant=4321,
    pricing={"price": {"price": 2499, "currency": "USD"}}
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

