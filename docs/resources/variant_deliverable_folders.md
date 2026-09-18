# variant_deliverable_folders

[All resources](../methods.md)

## list

List variant deliverable folders

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```python
def list(
        self,
        product: str,
        variant: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkListVariantDeliverableFoldersResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListVariantDeliverableFoldersResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_folders.list(
    product="string_example",
    variant=1
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

## create

Create a variant deliverable folder

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def create(
        self,
        product: str,
        variant: int,
        *,
        name: str,
        description: str | None | NotGiven = NOT_GIVEN,
        parent_id: int | None | NotGiven = NOT_GIVEN,
        sort_order: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateVariantDeliverableFolderResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| name | `str` | Yes |
| description | `str \| None \| NotGiven` | No |
| parent_id | `int \| None \| NotGiven` | No |
| sort_order | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateVariantDeliverableFolderResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_folders.create(
    product="string_example",
    variant=1,
    name="Design kit",
    description="Files included with your purchase."
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

Retrieve a variant deliverable folder

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```python
def get(
        self,
        product: str,
        variant: int,
        folder: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetVariantDeliverableFolderResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| folder | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetVariantDeliverableFolderResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_folders.get(
    product="string_example",
    variant=1,
    folder=1
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

Replace variant deliverable folder settings

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def replace(
        self,
        product: str,
        variant: int,
        folder: int,
        *,
        name: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        parent_id: int | None | NotGiven = NOT_GIVEN,
        sort_order: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceVariantDeliverableFolderSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| folder | `int` | Yes |
| name | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| parent_id | `int \| None \| NotGiven` | No |
| sort_order | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceVariantDeliverableFolderSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_folders.replace(
    product="string_example",
    variant=1,
    folder=1,
    name="Design kit"
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

Update a variant deliverable folder

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def update(
        self,
        product: str,
        variant: int,
        folder: int,
        *,
        name: str | None = None,
        description: str | None | NotGiven = NOT_GIVEN,
        parent_id: int | None | NotGiven = NOT_GIVEN,
        sort_order: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateVariantDeliverableFolderResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| folder | `int` | Yes |
| name | `str \| None` | No |
| description | `str \| None \| NotGiven` | No |
| parent_id | `int \| None \| NotGiven` | No |
| sort_order | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateVariantDeliverableFolderResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_folders.update(
    product="string_example",
    variant=1,
    folder=1,
    name="Design kit"
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

Delete a variant deliverable folder

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```python
def delete(
        self,
        product: str,
        variant: int,
        folder: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| folder | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_folders.delete(
    product="string_example",
    variant=1,
    folder=1
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

