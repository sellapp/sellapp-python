# products

[All resources](../methods.md)

## list

List all products

[API reference](https://sell.app/docs/api/products/list-all-products) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        with_drafts: bool | None = None,
        only_drafts: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListProductsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| with_drafts | `bool \| None` | No |
| only_drafts | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListProductsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.list(limit=1)
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create

Create a product

[API reference](https://sell.app/docs/api/products/create-a-product) · Effect: **write**

```python
def create(
        self,
        *,
        title: str,
        description: str,
        visibility: CatalogVisibility | str,
        slug: str | None = None,
        type: SdkCreateProductRequestApplicationJsonType | str | None = None,
        section: int | None | NotGiven = NOT_GIVEN,
        additional_information: builtins.list[
            CreateProductRequestApplicationJsonPropertyAdditionalInformationItem
        ]
        | None = None,
        other_settings: CreateProductRequestApplicationJsonPropertyOtherSettings
        | None = None,
        variants: builtins.list[CreateProductRequestApplicationJsonPropertyVariantsItem]
        | None = None,
        bundle_items: builtins.list[
            CreateProductRequestApplicationJsonPropertyBundleItemsItem
        ]
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateProductResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| description | `str` | Yes |
| visibility | `CatalogVisibility \| str` | Yes |
| slug | `str \| None` | No |
| type | `SdkCreateProductRequestApplicationJsonType \| str \| None` | No |
| section | `int \| None \| NotGiven` | No |
| additional_information | `builtins.list[
            CreateProductRequestApplicationJsonPropertyAdditionalInformationItem
        ]
        \| None` | No |
| other_settings | `CreateProductRequestApplicationJsonPropertyOtherSettings
        \| None` | No |
| variants | `builtins.list[CreateProductRequestApplicationJsonPropertyVariantsItem]
        \| None` | No |
| bundle_items | `builtins.list[
            CreateProductRequestApplicationJsonPropertyBundleItemsItem
        ]
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateProductResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.create(
    title="Design kit",
    description="Templates for your next project.",
    visibility="HIDDEN"
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a product

[API reference](https://sell.app/docs/api/products/retrieve-a-product) · Effect: **read**

```python
def get(
        self,
        product: int,
        *,
        with_drafts: bool | None = None,
        only_drafts: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkGetProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| with_drafts | `bool \| None` | No |
| only_drafts | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetProductResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.get(product=1)
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

Update a product

[API reference](https://sell.app/docs/api/products) · Effect: **write**

```python
def replace(
        self,
        product: int,
        *,
        title: str | None = None,
        description: str | None = None,
        visibility: CatalogVisibility | str | None = None,
        slug: str | None = None,
        section: int | None | NotGiven = NOT_GIVEN,
        additional_information: builtins.list[
            ReplaceProductRequestApplicationJsonPropertyAdditionalInformationItem
        ]
        | None = None,
        other_settings: ReplaceProductRequestApplicationJsonPropertyOtherSettings
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| title | `str \| None` | No |
| description | `str \| None` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| slug | `str \| None` | No |
| section | `int \| None \| NotGiven` | No |
| additional_information | `builtins.list[
            ReplaceProductRequestApplicationJsonPropertyAdditionalInformationItem
        ]
        \| None` | No |
| other_settings | `ReplaceProductRequestApplicationJsonPropertyOtherSettings
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceProductResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.replace(
    product=120,
    title="Design kit",
    description="Templates for your next project.",
    visibility="HIDDEN",
    expected_updated_at="2026-08-30T12:00:00.000000Z"
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

Update a product

[API reference](https://sell.app/docs/api/products/update-a-product) · Effect: **write**

```python
def update(
        self,
        product: int,
        *,
        title: str | None = None,
        description: str | None = None,
        visibility: CatalogVisibility | str | None = None,
        slug: str | None = None,
        section: int | None | NotGiven = NOT_GIVEN,
        additional_information: builtins.list[
            UpdateProductRequestApplicationJsonPropertyAdditionalInformationItem
        ]
        | None = None,
        other_settings: UpdateProductRequestApplicationJsonPropertyOtherSettings
        | None = None,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| title | `str \| None` | No |
| description | `str \| None` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| slug | `str \| None` | No |
| section | `int \| None \| NotGiven` | No |
| additional_information | `builtins.list[
            UpdateProductRequestApplicationJsonPropertyAdditionalInformationItem
        ]
        \| None` | No |
| other_settings | `UpdateProductRequestApplicationJsonPropertyOtherSettings
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateProductResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.update(
    product=120,
    title="Design kit",
    description="Templates for your next project.",
    visibility="HIDDEN",
    expected_updated_at="2026-08-30T12:00:00.000000Z"
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

Delete a product

[API reference](https://sell.app/docs/api/products/delete-a-product) · Effect: **consequential**

```python
def delete(
        self,
        product: int,
        *,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.delete(
    product=1,
    expected_updated_at="2026-08-01T12:00:00Z"
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

Search products

[API reference](https://sell.app/docs/api/products/search-products) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[SearchProductsRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[SearchProductsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchProductsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchProductsRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchProductsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[SearchProductsRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[SearchProductsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchProductsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchProductsRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SearchProductsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.search(
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_create

Batch create products

[API reference](https://sell.app/docs/api/products/batch-create-products) · Effect: **consequential**

```python
def batch_create(
        self,
        *,
        resources: builtins.list[
            BatchCreateProductsRequestApplicationJsonPropertyResourcesItem
        ],
        request_options: RequestOptions | None = None,
    ) -> SdkBatchCreateProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `builtins.list[
            BatchCreateProductsRequestApplicationJsonPropertyResourcesItem
        ]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkBatchCreateProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.batch_create(
    resources=[
        {
            "title": "Example product",
            "description": "An example product created through the API.",
            "visibility": "PUBLIC",
            "type": "product"
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

Documented HTTP responses: 200, 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_update

Batch update products

[API reference](https://sell.app/docs/api/products/batch-update-products) · Effect: **consequential**

```python
def batch_update(
        self,
        *,
        resources: BatchUpdateProductsRequestApplicationJsonPropertyResources,
        request_options: RequestOptions | None = None,
    ) -> SdkBatchUpdateProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `BatchUpdateProductsRequestApplicationJsonPropertyResources` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkBatchUpdateProductsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.batch_update(resources={"1": {"title": "Updated product", "visibility": "PUBLIC"}})
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## batch_delete

Batch delete products

[API reference](https://sell.app/docs/api/products/batch-delete-products) · Effect: **consequential**

```python
def batch_delete(
        self,
        *,
        resources: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.products.batch_delete(resources=[1, 2])
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

Documented HTTP responses: 200, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

