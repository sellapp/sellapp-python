# product_variants

[All resources](../methods.md)

## list

List all product variants

[API reference](https://sell.app/docs/api/product-variants/list-all-product-variants) · Effect: **read**

```python
def list(
        self,
        product: int,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        with_drafts: Optional[bool] = None,
        only_drafts: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListProductVariantsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| with_drafts | `Optional[bool]` | No |
| only_drafts | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListProductVariantsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.list(product=1)
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

## create

Create a product variant

[API reference](https://sell.app/docs/api/product-variants/create-a-product-variant) · Effect: **write**

```python
def create(
        self,
        product: int,
        *,
        title: str,
        description: str,
        deliverable: CreateProductVariantRequestApplicationJsonPropertyDeliverable,
        pricing: CreateProductVariantRequestApplicationJsonPropertyPricing,
        payment_methods: List[
            Union[SdkCreateProductVariantRequestApplicationJsonPaymentMethods, str]
        ],
        minimum_purchase_quantity: Optional[int] = None,
        maximum_purchase_quantity: Union[int, None, NotGiven] = NOT_GIVEN,
        bulk_discount: Optional[
            List[CreateProductVariantRequestApplicationJsonPropertyBulkDiscountItem]
        ] = None,
        other_settings: Optional[
            CreateProductVariantRequestApplicationJsonPropertyOtherSettings
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateProductVariantResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| title | `str` | Yes |
| description | `str` | Yes |
| deliverable | `CreateProductVariantRequestApplicationJsonPropertyDeliverable` | Yes |
| pricing | `CreateProductVariantRequestApplicationJsonPropertyPricing` | Yes |
| payment_methods | `List[
            Union[SdkCreateProductVariantRequestApplicationJsonPaymentMethods, str]
        ]` | Yes |
| minimum_purchase_quantity | `Optional[int]` | No |
| maximum_purchase_quantity | `Union[int, None, NotGiven]` | No |
| bulk_discount | `Optional[
            List[CreateProductVariantRequestApplicationJsonPropertyBulkDiscountItem]
        ]` | No |
| other_settings | `Optional[
            CreateProductVariantRequestApplicationJsonPropertyOtherSettings
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateProductVariantResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.create(
    product=120,
    title="Monthly membership",
    description="One operating memo each month; access is provisioned by our team.",
    deliverable={
        "types": ["MANUAL"],
        "data": {"stock": None, "comment": "We will send your reading-room invitation."}
    },
    pricing={"humble": False, "price": {"price": 1999, "currency": "USD"}},
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

Documented HTTP responses: 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a product variant

[API reference](https://sell.app/docs/api/product-variants/retrieve-a-product-variant) · Effect: **read**

```python
def get(
        self,
        product: int,
        variant: int,
        *,
        with_drafts: Optional[bool] = None,
        only_drafts: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetProductVariantResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| with_drafts | `Optional[bool]` | No |
| only_drafts | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetProductVariantResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.get(
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

## replace

Update a product variant with PUT

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def replace(
        self,
        product: int,
        variant: int,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        deliverable: Optional[
            ReplaceProductVariantWithPutRequestApplicationJsonPropertyDeliverable
        ] = None,
        pricing: Optional[
            ReplaceProductVariantWithPutRequestApplicationJsonPropertyPricing
        ] = None,
        minimum_purchase_quantity: Optional[int] = None,
        maximum_purchase_quantity: Union[int, None, NotGiven] = NOT_GIVEN,
        bulk_discount: Optional[
            List[
                ReplaceProductVariantWithPutRequestApplicationJsonPropertyBulkDiscountItem
            ]
        ] = None,
        payment_methods: Optional[
            List[
                Union[
                    SdkReplaceProductVariantWithPutRequestApplicationJsonPaymentMethods,
                    str,
                ]
            ]
        ] = None,
        other_settings: Optional[
            ReplaceProductVariantWithPutRequestApplicationJsonPropertyOtherSettings
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceProductVariantWithPutResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| title | `Optional[str]` | No |
| description | `Optional[str]` | No |
| deliverable | `Optional[
            ReplaceProductVariantWithPutRequestApplicationJsonPropertyDeliverable
        ]` | No |
| pricing | `Optional[
            ReplaceProductVariantWithPutRequestApplicationJsonPropertyPricing
        ]` | No |
| minimum_purchase_quantity | `Optional[int]` | No |
| maximum_purchase_quantity | `Union[int, None, NotGiven]` | No |
| bulk_discount | `Optional[
            List[
                ReplaceProductVariantWithPutRequestApplicationJsonPropertyBulkDiscountItem
            ]
        ]` | No |
| payment_methods | `Optional[
            List[
                Union[
                    SdkReplaceProductVariantWithPutRequestApplicationJsonPaymentMethods,
                    str,
                ]
            ]
        ]` | No |
| other_settings | `Optional[
            ReplaceProductVariantWithPutRequestApplicationJsonPropertyOtherSettings
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkReplaceProductVariantWithPutResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.replace(
    product=120,
    variant=4321,
    title="Monthly membership plus",
    description="One annotated operating memo and a monthly founder discussion."
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

Update a product variant

[API reference](https://sell.app/docs/api/product-variants/update-a-product-variant) · Effect: **write**

```python
def update(
        self,
        product: int,
        variant: int,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        deliverable: Optional[
            UpdateProductVariantRequestApplicationJsonPropertyDeliverable
        ] = None,
        pricing: Optional[
            UpdateProductVariantRequestApplicationJsonPropertyPricing
        ] = None,
        minimum_purchase_quantity: Optional[int] = None,
        maximum_purchase_quantity: Union[int, None, NotGiven] = NOT_GIVEN,
        bulk_discount: Optional[
            List[UpdateProductVariantRequestApplicationJsonPropertyBulkDiscountItem]
        ] = None,
        payment_methods: Optional[
            List[
                Union[SdkUpdateProductVariantRequestApplicationJsonPaymentMethods, str]
            ]
        ] = None,
        other_settings: Optional[
            UpdateProductVariantRequestApplicationJsonPropertyOtherSettings
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateProductVariantResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| title | `Optional[str]` | No |
| description | `Optional[str]` | No |
| deliverable | `Optional[
            UpdateProductVariantRequestApplicationJsonPropertyDeliverable
        ]` | No |
| pricing | `Optional[
            UpdateProductVariantRequestApplicationJsonPropertyPricing
        ]` | No |
| minimum_purchase_quantity | `Optional[int]` | No |
| maximum_purchase_quantity | `Union[int, None, NotGiven]` | No |
| bulk_discount | `Optional[
            List[UpdateProductVariantRequestApplicationJsonPropertyBulkDiscountItem]
        ]` | No |
| payment_methods | `Optional[
            List[
                Union[SdkUpdateProductVariantRequestApplicationJsonPaymentMethods, str]
            ]
        ]` | No |
| other_settings | `Optional[
            UpdateProductVariantRequestApplicationJsonPropertyOtherSettings
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateProductVariantResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.update(
    product=120,
    variant=4321,
    title="Monthly membership plus",
    description="One annotated operating memo and a monthly founder discussion."
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

Delete a product variant

[API reference](https://sell.app/docs/api/product-variants/delete-a-product-variant) · Effect: **consequential**

```python
def delete(
        self,
        product: int,
        variant: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.delete(
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

## search

Search product variants

[API reference](https://sell.app/docs/api/product-variants/search-product-variants) · Effect: **read**

```python
def search(
        self,
        product: int,
        *,
        filters: Optional[
            List[SearchProductVariantsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchProductVariantsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[
            SearchProductVariantsRequestApplicationJsonPropertySearch
        ] = None,
        includes: Optional[
            List[SearchProductVariantsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchProductVariantsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| filters | `Optional[
            List[SearchProductVariantsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchProductVariantsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[
            SearchProductVariantsRequestApplicationJsonPropertySearch
        ]` | No |
| includes | `Optional[
            List[SearchProductVariantsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SearchProductVariantsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.search(
    product=1,
    filters=[{"field": "id", "operator": "=", "value": 1}],
    sort=[{"field": "created_at", "direction": "desc"}]
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

## batch_create

Batch create product variants

[API reference](https://sell.app/docs/api/product-variants/batch-create-product-variants) · Effect: **consequential**

```python
def batch_create(
        self,
        product: int,
        *,
        resources: List[
            BatchCreateProductVariantsRequestApplicationJsonPropertyResourcesItem
        ],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkBatchCreateProductVariantsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| resources | `List[
            BatchCreateProductVariantsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkBatchCreateProductVariantsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.batch_create(
    product=1,
    resources=[
        {
            "title": "Default",
            "description": "Default product variant.",
            "deliverable": {
                "types": ["TEXT"],
                "data": {"serials": ["SERIAL-001"], "parsingMode": "NEW_LINE", "removeDuplicate": True}
            },
            "pricing": {"humble": False, "price": {"price": 1000, "currency": "USD"}},
            "payment_methods": ["PAYPAL"]
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_update

Batch update product variants

[API reference](https://sell.app/docs/api/product-variants/batch-update-product-variants) · Effect: **consequential**

```python
def batch_update(
        self,
        product: int,
        *,
        resources: BatchUpdateProductVariantsRequestApplicationJsonPropertyResources,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkBatchUpdateProductVariantsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| resources | `BatchUpdateProductVariantsRequestApplicationJsonPropertyResources` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkBatchUpdateProductVariantsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.batch_update(
    product=1,
    resources={"1": {"title": "Updated variant"}}
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

## batch_delete

Batch delete product variants

[API reference](https://sell.app/docs/api/product-variants/batch-delete-product-variants) · Effect: **consequential**

```python
def batch_delete(
        self,
        product: int,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants.batch_delete(
    product=1,
    resources=[1, 2]
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

