# variant_deliverable_files

[All resources](../methods.md)

## list

List variant deliverable files

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```python
def list(
        self,
        product: str,
        variant: int,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        ListVariantDeliverableFilesResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        ListVariantDeliverableFilesResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_files.list(
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

## upload

Upload a variant deliverable file

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def upload(
        self,
        product: str,
        variant: int,
        *,
        file: bytes,
        folder_id: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUploadVariantDeliverableFileResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| file | `bytes` | Yes |
| folder_id | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUploadVariantDeliverableFileResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_files.upload(
    product="string_example",
    variant=1,
    file="design-kit.zip"
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

Retrieve a variant deliverable file

[API reference](https://sell.app/docs/api/product-variants) · Effect: **read**

```python
def get(
        self,
        product: str,
        variant: int,
        file: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetVariantDeliverableFileResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| file | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetVariantDeliverableFileResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_files.get(
    product="string_example",
    variant=1,
    file=1
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

Replace variant deliverable file settings

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def replace(
        self,
        product: str,
        variant: int,
        file: int,
        *,
        custom_name: str | None | NotGiven = NOT_GIVEN,
        folder_id: int | None | NotGiven = NOT_GIVEN,
        watermark: bool | None = None,
        max_downloads: int | None | NotGiven = NOT_GIVEN,
        limit_to_purchase_ip: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceVariantDeliverableFileSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| file | `int` | Yes |
| custom_name | `str \| None \| NotGiven` | No |
| folder_id | `int \| None \| NotGiven` | No |
| watermark | `bool \| None` | No |
| max_downloads | `int \| None \| NotGiven` | No |
| limit_to_purchase_ip | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceVariantDeliverableFileSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_files.replace(
    product="string_example",
    variant=1,
    file=1,
    custom_name="Design kit.zip"
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

Update a variant deliverable file

[API reference](https://sell.app/docs/api/product-variants) · Effect: **write**

```python
def update(
        self,
        product: str,
        variant: int,
        file: int,
        *,
        custom_name: str | None | NotGiven = NOT_GIVEN,
        folder_id: int | None | NotGiven = NOT_GIVEN,
        watermark: bool | None = None,
        max_downloads: int | None | NotGiven = NOT_GIVEN,
        limit_to_purchase_ip: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateVariantDeliverableFileResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| file | `int` | Yes |
| custom_name | `str \| None \| NotGiven` | No |
| folder_id | `int \| None \| NotGiven` | No |
| watermark | `bool \| None` | No |
| max_downloads | `int \| None \| NotGiven` | No |
| limit_to_purchase_ip | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateVariantDeliverableFileResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_files.update(
    product="string_example",
    variant=1,
    file=1,
    custom_name="Design kit.zip"
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

Delete a variant deliverable file

[API reference](https://sell.app/docs/api/product-variants) · Effect: **consequential**

```python
def delete(
        self,
        product: str,
        variant: int,
        file: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| file | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.variant_deliverable_files.delete(
    product="string_example",
    variant=1,
    file=1
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

