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
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        with_drafts: bool | None = None,
        only_drafts: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListProductVariantsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| with_drafts | `bool \| None` | No |
| only_drafts | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        payment_methods: builtins.list[
            SdkCreateProductVariantRequestApplicationJsonPaymentMethods | str
        ],
        minimum_purchase_quantity: int | None = None,
        maximum_purchase_quantity: int | None | NotGiven = NOT_GIVEN,
        bulk_discount: builtins.list[
            CreateProductVariantRequestApplicationJsonPropertyBulkDiscountItem
        ]
        | None = None,
        other_settings: CreateProductVariantRequestApplicationJsonPropertyOtherSettings
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateProductVariantResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| title | `str` | Yes |
| description | `str` | Yes |
| deliverable | `CreateProductVariantRequestApplicationJsonPropertyDeliverable` | Yes |
| pricing | `CreateProductVariantRequestApplicationJsonPropertyPricing` | Yes |
| payment_methods | `builtins.list[
            SdkCreateProductVariantRequestApplicationJsonPaymentMethods \| str
        ]` | Yes |
| minimum_purchase_quantity | `int \| None` | No |
| maximum_purchase_quantity | `int \| None \| NotGiven` | No |
| bulk_discount | `builtins.list[
            CreateProductVariantRequestApplicationJsonPropertyBulkDiscountItem
        ]
        \| None` | No |
| other_settings | `CreateProductVariantRequestApplicationJsonPropertyOtherSettings
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        with_drafts: bool | None = None,
        only_drafts: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkGetProductVariantResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| with_drafts | `bool \| None` | No |
| only_drafts | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        title: str | None = None,
        description: str | None = None,
        deliverable: ReplaceProductVariantWithPutRequestApplicationJsonPropertyDeliverable
        | None = None,
        pricing: ReplaceProductVariantWithPutRequestApplicationJsonPropertyPricing
        | None = None,
        minimum_purchase_quantity: int | None = None,
        maximum_purchase_quantity: int | None | NotGiven = NOT_GIVEN,
        bulk_discount: builtins.list[
            ReplaceProductVariantWithPutRequestApplicationJsonPropertyBulkDiscountItem
        ]
        | None = None,
        payment_methods: builtins.list[
            SdkReplaceProductVariantWithPutRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        other_settings: ReplaceProductVariantWithPutRequestApplicationJsonPropertyOtherSettings
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceProductVariantWithPutResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| title | `str \| None` | No |
| description | `str \| None` | No |
| deliverable | `ReplaceProductVariantWithPutRequestApplicationJsonPropertyDeliverable
        \| None` | No |
| pricing | `ReplaceProductVariantWithPutRequestApplicationJsonPropertyPricing
        \| None` | No |
| minimum_purchase_quantity | `int \| None` | No |
| maximum_purchase_quantity | `int \| None \| NotGiven` | No |
| bulk_discount | `builtins.list[
            ReplaceProductVariantWithPutRequestApplicationJsonPropertyBulkDiscountItem
        ]
        \| None` | No |
| payment_methods | `builtins.list[
            SdkReplaceProductVariantWithPutRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| other_settings | `ReplaceProductVariantWithPutRequestApplicationJsonPropertyOtherSettings
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        title: str | None = None,
        description: str | None = None,
        deliverable: UpdateProductVariantRequestApplicationJsonPropertyDeliverable
        | None = None,
        pricing: UpdateProductVariantRequestApplicationJsonPropertyPricing
        | None = None,
        minimum_purchase_quantity: int | None = None,
        maximum_purchase_quantity: int | None | NotGiven = NOT_GIVEN,
        bulk_discount: builtins.list[
            UpdateProductVariantRequestApplicationJsonPropertyBulkDiscountItem
        ]
        | None = None,
        payment_methods: builtins.list[
            SdkUpdateProductVariantRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        other_settings: UpdateProductVariantRequestApplicationJsonPropertyOtherSettings
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateProductVariantResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| title | `str \| None` | No |
| description | `str \| None` | No |
| deliverable | `UpdateProductVariantRequestApplicationJsonPropertyDeliverable
        \| None` | No |
| pricing | `UpdateProductVariantRequestApplicationJsonPropertyPricing
        \| None` | No |
| minimum_purchase_quantity | `int \| None` | No |
| maximum_purchase_quantity | `int \| None \| NotGiven` | No |
| bulk_discount | `builtins.list[
            UpdateProductVariantRequestApplicationJsonPropertyBulkDiscountItem
        ]
        \| None` | No |
| payment_methods | `builtins.list[
            SdkUpdateProductVariantRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| other_settings | `UpdateProductVariantRequestApplicationJsonPropertyOtherSettings
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        filters: builtins.list[
            SearchProductVariantsRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchProductVariantsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchProductVariantsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchProductVariantsRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchProductVariantsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| filters | `builtins.list[
            SearchProductVariantsRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchProductVariantsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchProductVariantsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchProductVariantsRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        resources: builtins.list[
            BatchCreateProductVariantsRequestApplicationJsonPropertyResourcesItem
        ],
        request_options: RequestOptions | None = None,
    ) -> SdkBatchCreateProductVariantsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| resources | `builtins.list[
            BatchCreateProductVariantsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> SdkBatchUpdateProductVariantsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| resources | `BatchUpdateProductVariantsRequestApplicationJsonPropertyResources` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        resources: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| resources | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

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

