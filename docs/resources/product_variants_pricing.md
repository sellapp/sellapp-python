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
        payment_methods: List[
            Union[
                SdkReplaceProductVariantPricingRequestApplicationJsonPaymentMethods, str
            ]
        ],
        custom_payment_method_ids: Optional[List[str]] = None,
        bulk_discount: Optional[
            List[
                ReplaceProductVariantPricingRequestApplicationJsonPropertyBulkDiscountItem
            ]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceProductVariantPricingResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| pricing | `ReplaceProductVariantPricingRequestApplicationJsonPropertyPricing` | Yes |
| payment_methods | `List[
            Union[
                SdkReplaceProductVariantPricingRequestApplicationJsonPaymentMethods, str
            ]
        ]` | Yes |
| custom_payment_method_ids | `Optional[List[str]]` | No |
| bulk_discount | `Optional[
            List[
                ReplaceProductVariantPricingRequestApplicationJsonPropertyBulkDiscountItem
            ]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        pricing: Optional[
            UpdateProductVariantPricingRequestApplicationJsonPropertyPricing
        ] = None,
        payment_methods: Optional[
            List[
                Union[
                    SdkUpdateProductVariantPricingRequestApplicationJsonPaymentMethods,
                    str,
                ]
            ]
        ] = None,
        custom_payment_method_ids: Optional[List[str]] = None,
        bulk_discount: Optional[
            List[
                UpdateProductVariantPricingRequestApplicationJsonPropertyBulkDiscountItem
            ]
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateProductVariantPricingResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| pricing | `Optional[
            UpdateProductVariantPricingRequestApplicationJsonPropertyPricing
        ]` | No |
| payment_methods | `Optional[
            List[
                Union[
                    SdkUpdateProductVariantPricingRequestApplicationJsonPaymentMethods,
                    str,
                ]
            ]
        ]` | No |
| custom_payment_method_ids | `Optional[List[str]]` | No |
| bulk_discount | `Optional[
            List[
                UpdateProductVariantPricingRequestApplicationJsonPropertyBulkDiscountItem
            ]
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

