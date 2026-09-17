# store_custom_domains

[All resources](../methods.md)

## list

List custom domains

[API reference](https://sell.app/docs/api/store-settings/list-custom-domains) · Effect: **read**

```python
def list(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListCustomDomainsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListCustomDomainsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_custom_domains.list()
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

## connect

Connect a custom domain

[API reference](https://sell.app/docs/api/store-settings/connect-custom-domain) · Effect: **consequential**

```python
def connect(
        self,
        *,
        domain: str,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkConnectCustomDomainResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| domain | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkConnectCustomDomainResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_custom_domains.connect(domain="example.com")
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

Retrieve a custom domain

[API reference](https://sell.app/docs/api/store-settings/manage-custom-domain) · Effect: **read**

```python
def get(
        self,
        custom_domain: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomDomainResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_domain | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetCustomDomainResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_custom_domains.get(custom_domain=1)
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

## disconnect

Disconnect a custom domain

[API reference](https://sell.app/docs/api/store-settings/manage-custom-domain) · Effect: **consequential**

```python
def disconnect(
        self,
        custom_domain: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_domain | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_custom_domains.disconnect(custom_domain=1)
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

## refresh

Refresh custom domain status

[API reference](https://sell.app/docs/api/store-settings/refresh-custom-domain) · Effect: **consequential**

```python
def refresh(
        self,
        custom_domain: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkRefreshCustomDomainStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| custom_domain | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkRefreshCustomDomainStatusResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_custom_domains.refresh(custom_domain=1)
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

