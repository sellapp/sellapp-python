# bundle_items

[All resources](../methods.md)

## get

Retrieve a bundle item

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```python
def get(
        self,
        bundle: int,
        item: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetBundleItemResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| bundle | `int` | Yes |
| item | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetBundleItemResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bundle_items.get(
    bundle=1,
    item=2
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

## list

List bundle items

[API reference](https://sell.app/docs/api/products) · Effect: **read**

```python
def list(
        self,
        bundle: int,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListBundleItemsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| bundle | `int` | Yes |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListBundleItemsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bundle_items.list(bundle=1)
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

## attach

Attach bundle items

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```python
def attach(
        self,
        bundle: int,
        *,
        resources: AttachBundleItemsRequestApplicationJsonPropertyResources,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkAttachBundleItemsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| bundle | `int` | Yes |
| resources | `AttachBundleItemsRequestApplicationJsonPropertyResources` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkAttachBundleItemsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bundle_items.attach(
    bundle=1,
    resources={"1": {"quantity": 1}}
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

## detach

Detach bundle items

[API reference](https://sell.app/docs/api/products) · Effect: **consequential**

```python
def detach(
        self,
        bundle: int,
        *,
        resources: List[int],
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| bundle | `int` | Yes |
| resources | `List[int]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bundle_items.detach(
    bundle=1,
    resources=[1]
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

