# licenses

[All resources](../methods.md)

## activate

Activate a license key

[API reference](https://sell.app/docs/api/licenses/activate-a-license-key) · Effect: **consequential**

```python
def activate(
        self,
        *,
        license_key: str,
        instance_name: str,
        request_options: RequestOptions | None = None,
    ) -> SdkActivateLicenseKeyResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `str` | Yes |
| instance_name | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkActivateLicenseKeyResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.licenses.activate(
    license_key="01965f1d-f038-7116-b57f-9e7ecb4e7b8f",
    instance_name="Grace Wilson"
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

## validate

Validate a license key

[API reference](https://sell.app/docs/api/licenses/validate-a-license-key) · Effect: **consequential**

```python
def validate(
        self,
        *,
        license_key: str,
        instance_id: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkValidateLicenseKeyResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `str` | Yes |
| instance_id | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkValidateLicenseKeyResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.licenses.validate(license_key="01965f1d-f038-7116-b57f-9e7ecb4e7b8f")
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

## list

List all license keys

[API reference](https://sell.app/docs/api/licenses/list-all-license-keys) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkListLicenseKeysResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkListLicenseKeysResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.licenses.list()
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

## get

Retrieve a license key

[API reference](https://sell.app/docs/api/licenses/retrieve-a-license-key) · Effect: **read**

```python
def get(
        self,
        license_key: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetLicenseKeyResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetLicenseKeyResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.licenses.get(license_key=1)
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

Update a license key

[API reference](https://sell.app/docs/api/licenses/update-a-license-key) · Effect: **consequential**

```python
def update(
        self,
        license_key: int,
        *,
        limit: int | None | NotGiven = NOT_GIVEN,
        expires_at: str | None | NotGiven = NOT_GIVEN,
        active: bool | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateLicenseKeyResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `int` | Yes |
| limit | `int \| None \| NotGiven` | No |
| expires_at | `str \| None \| NotGiven` | No |
| active | `bool \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateLicenseKeyResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.licenses.update(
    license_key=1,
    limit=10,
    active=False
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

## deactivate_license

Deactivate a license instance

[API reference](https://sell.app/docs/api/licenses/deactivate-a-license) · Effect: **consequential**

```python
def deactivate_license(
        self,
        *,
        license_key: str,
        instance_id: str,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkDeactivateLicenseResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| license_key | `str` | Yes |
| instance_id | `str` | Yes |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkDeactivateLicenseResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.licenses.deactivate_license(
    license_key="SELL-LICENSE-REDACTED",
    instance_id="laptop-maya",
    idempotency_key="example-mutation-001"
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

