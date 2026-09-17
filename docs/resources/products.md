# products

[All resources](../methods.md)

## list

List all products

[API reference](https://sell.app/docs/api/products/list-all-products) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        with_drafts: Optional[bool] = None,
        only_drafts: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListProductsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| with_drafts | `Optional[bool]` | No |
| only_drafts | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        visibility: Union[CatalogVisibility, str],
        slug: Optional[str] = None,
        type: Optional[Union[SdkCreateProductRequestApplicationJsonType, str]] = None,
        section: Union[int, None, NotGiven] = NOT_GIVEN,
        additional_information: Optional[
            List[CreateProductRequestApplicationJsonPropertyAdditionalInformationItem]
        ] = None,
        other_settings: Optional[
            CreateProductRequestApplicationJsonPropertyOtherSettings
        ] = None,
        variants: Optional[
            List[CreateProductRequestApplicationJsonPropertyVariantsItem]
        ] = None,
        bundle_items: Optional[
            List[CreateProductRequestApplicationJsonPropertyBundleItemsItem]
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateProductResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| description | `str` | Yes |
| visibility | `Union[CatalogVisibility, str]` | Yes |
| slug | `Optional[str]` | No |
| type | `Optional[Union[SdkCreateProductRequestApplicationJsonType, str]]` | No |
| section | `Union[int, None, NotGiven]` | No |
| additional_information | `Optional[
            List[CreateProductRequestApplicationJsonPropertyAdditionalInformationItem]
        ]` | No |
| other_settings | `Optional[
            CreateProductRequestApplicationJsonPropertyOtherSettings
        ]` | No |
| variants | `Optional[
            List[CreateProductRequestApplicationJsonPropertyVariantsItem]
        ]` | No |
| bundle_items | `Optional[
            List[CreateProductRequestApplicationJsonPropertyBundleItemsItem]
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        with_drafts: Optional[bool] = None,
        only_drafts: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| with_drafts | `Optional[bool]` | No |
| only_drafts | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        title: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Union[CatalogVisibility, str]] = None,
        slug: Optional[str] = None,
        section: Union[int, None, NotGiven] = NOT_GIVEN,
        additional_information: Optional[
            List[ReplaceProductRequestApplicationJsonPropertyAdditionalInformationItem]
        ] = None,
        other_settings: Optional[
            ReplaceProductRequestApplicationJsonPropertyOtherSettings
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| title | `Optional[str]` | No |
| description | `Optional[str]` | No |
| visibility | `Optional[Union[CatalogVisibility, str]]` | No |
| slug | `Optional[str]` | No |
| section | `Union[int, None, NotGiven]` | No |
| additional_information | `Optional[
            List[ReplaceProductRequestApplicationJsonPropertyAdditionalInformationItem]
        ]` | No |
| other_settings | `Optional[
            ReplaceProductRequestApplicationJsonPropertyOtherSettings
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        title: Optional[str] = None,
        description: Optional[str] = None,
        visibility: Optional[Union[CatalogVisibility, str]] = None,
        slug: Optional[str] = None,
        section: Union[int, None, NotGiven] = NOT_GIVEN,
        additional_information: Optional[
            List[UpdateProductRequestApplicationJsonPropertyAdditionalInformationItem]
        ] = None,
        other_settings: Optional[
            UpdateProductRequestApplicationJsonPropertyOtherSettings
        ] = None,
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateProductResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| title | `Optional[str]` | No |
| description | `Optional[str]` | No |
| visibility | `Optional[Union[CatalogVisibility, str]]` | No |
| slug | `Optional[str]` | No |
| section | `Union[int, None, NotGiven]` | No |
| additional_information | `Optional[
            List[UpdateProductRequestApplicationJsonPropertyAdditionalInformationItem]
        ]` | No |
| other_settings | `Optional[
            UpdateProductRequestApplicationJsonPropertyOtherSettings
        ]` | No |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        expected_updated_at: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| expected_updated_at | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchProductsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchProductsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchProductsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchProductsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchProductsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchProductsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchProductsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchProductsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchProductsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        resources: List[BatchCreateProductsRequestApplicationJsonPropertyResourcesItem],
        request_options: Optional[RequestOptions] = None,
    ) -> SdkBatchCreateProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[BatchCreateProductsRequestApplicationJsonPropertyResourcesItem]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkBatchUpdateProductsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `BatchUpdateProductsRequestApplicationJsonPropertyResources` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

