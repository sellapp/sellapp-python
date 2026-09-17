# blacklists

[All resources](../methods.md)

## list

List all blacklist rules

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[Blacklist]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[Blacklist]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.list()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create

Create a blacklist rule

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def create(
        self,
        *,
        type: Union[BlacklistType, str],
        data: str,
        description: str,
        request_options: Optional[RequestOptions] = None,
    ) -> BlacklistResponse:
```

| Argument | Native type | Required |
| --- | --- | --- |
| type | `Union[BlacklistType, str]` | Yes |
| data | `str` | Yes |
| description | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `BlacklistResponse`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.create(
    type="ASN",
    data="@blocked.example",
    description="Retired after the growth experiment ended."
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 201, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get

Retrieve a blacklist rule

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **read**

```python
def get(
        self,
        blacklist: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> BlacklistResponse:
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `BlacklistResponse`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.get(blacklist=1)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update

Update a blacklist rule

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def update(
        self,
        blacklist: int,
        *,
        type: Optional[Union[BlacklistType, str]] = None,
        data: Optional[str] = None,
        description: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> BlacklistResponse:
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `int` | Yes |
| type | `Optional[Union[BlacklistType, str]]` | No |
| data | `Optional[str]` | No |
| description | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `BlacklistResponse`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.update(blacklist=1)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## delete

Delete a blacklist rule

[API reference](https://sell.app/docs/api/legacy-v1) · Effect: **consequential**

```python
def delete(
        self,
        blacklist: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.delete(blacklist=1)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "bearerAuth": [],
    "storeAuth": []
  }
]
```

Documented HTTP responses: 200, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v2_list_blacklists

List blacklist rules

[API reference](https://sell.app/docs/api/blacklists/list-blacklists) · Effect: **read**

```python
def v2_list_blacklists(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[Blacklist]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[Blacklist]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.v2_list_blacklists()
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

## v2_create_blacklist

Create a blacklist rule

[API reference](https://sell.app/docs/api/blacklists/create-blacklist) · Effect: **consequential**

```python
def v2_create_blacklist(
        self,
        *,
        type: Union[BlacklistType, str],
        data: str,
        description: str,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> BlacklistResponse:
```

| Argument | Native type | Required |
| --- | --- | --- |
| type | `Union[BlacklistType, str]` | Yes |
| data | `str` | Yes |
| description | `str` | Yes |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `BlacklistResponse`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.v2_create_blacklist(
    type="EMAIL",
    data="blocked@example.com",
    description="Blocked after a verified fraud report."
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## v2_get_blacklist

Retrieve a blacklist rule

[API reference](https://sell.app/docs/api/blacklists/retrieve-blacklist) · Effect: **read**

```python
def v2_get_blacklist(
        self,
        blacklist: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> BlacklistResponse:
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `BlacklistResponse`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.v2_get_blacklist(blacklist=42)
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

## v2_replace_blacklist

Replace a blacklist rule

[API reference](https://sell.app/docs/api/blacklists) · Effect: **consequential**

```python
def v2_replace_blacklist(
        self,
        blacklist: int,
        *,
        type: Optional[Union[BlacklistType, str]] = None,
        data: Optional[str] = None,
        description: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> BlacklistResponse:
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `int` | Yes |
| type | `Optional[Union[BlacklistType, str]]` | No |
| data | `Optional[str]` | No |
| description | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `BlacklistResponse`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.v2_replace_blacklist(
    blacklist=42,
    description="Blocked after a verified fraud report."
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

## v2_update_blacklist

Update a blacklist rule

[API reference](https://sell.app/docs/api/blacklists/update-blacklist) · Effect: **consequential**

```python
def v2_update_blacklist(
        self,
        blacklist: int,
        *,
        type: Optional[Union[BlacklistType, str]] = None,
        data: Optional[str] = None,
        description: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> BlacklistResponse:
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `int` | Yes |
| type | `Optional[Union[BlacklistType, str]]` | No |
| data | `Optional[str]` | No |
| description | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `BlacklistResponse`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.v2_update_blacklist(
    blacklist=42,
    description="Blocked after a verified fraud report."
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

## v2_delete_blacklist

Delete a blacklist rule

[API reference](https://sell.app/docs/api/blacklists/delete-blacklist) · Effect: **consequential**

```python
def v2_delete_blacklist(
        self,
        blacklist: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| blacklist | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.blacklists.v2_delete_blacklist(blacklist=42)
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

