# customers

[All resources](../methods.md)

## list

List customers

[API reference](https://sell.app/docs/api/customers/list-customers) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkListCustomersResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkListCustomersResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customers.list()
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

## create_customer

Create a customer

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **consequential**

```python
def create_customer(
        self,
        *,
        email: str,
        external_id: str | None = None,
        name: str | None | NotGiven = NOT_GIVEN,
        locale: str | None | NotGiven = NOT_GIVEN,
        metadata: CreateCustomerRequestApplicationJsonPropertyMetadata | None = None,
        idempotency_key: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateCustomerResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str` | Yes |
| external_id | `str \| None` | No |
| name | `str \| None \| NotGiven` | No |
| locale | `str \| None \| NotGiven` | No |
| metadata | `CreateCustomerRequestApplicationJsonPropertyMetadata \| None` | No |
| idempotency_key | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateCustomerResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customers.create_customer(
    external_id="crm_maya_314",
    email="maya.chen@example.com",
    name="Maya Chen",
    locale="en-GB",
    metadata={"plan": "standard", "seats": 3}
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

## search

Search customers

[API reference](https://sell.app/docs/api/customers/search-customers) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[SearchCustomersRequestApplicationJsonPropertyFiltersItem]
        | None = None,
        sort: builtins.list[SearchCustomersRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchCustomersRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchCustomersRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchCustomersResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[SearchCustomersRequestApplicationJsonPropertyFiltersItem]
        \| None` | No |
| sort | `builtins.list[SearchCustomersRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchCustomersRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchCustomersRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkSearchCustomersResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customers.search(
    filters=[{"field": "id", "operator": "=", "value": 125}],
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

## get

Retrieve a customer

[API reference](https://sell.app/docs/api/customers/retrieve-customer) · Effect: **read**

```python
def get(
        self,
        customer: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCustomerResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customers.get(customer=125)
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

## update_customer

Update a customer

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **consequential**

```python
def update_customer(
        self,
        customer: int,
        *,
        email: str | None = None,
        name: str | None | NotGiven = NOT_GIVEN,
        locale: str | None | NotGiven = NOT_GIVEN,
        metadata: UpdateCustomerRequestApplicationJsonPropertyMetadata | None = None,
        external_id: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| email | `str \| None` | No |
| name | `str \| None \| NotGiven` | No |
| locale | `str \| None \| NotGiven` | No |
| metadata | `UpdateCustomerRequestApplicationJsonPropertyMetadata \| None` | No |
| external_id | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCustomerResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customers.update_customer(
    customer=314,
    locale="en-US"
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

## get_customer_by_external_id

Retrieve a customer by external ID

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **read**

```python
def get_customer_by_external_id(
        self,
        external_id: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCustomerResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customers.get_customer_by_external_id(external_id="314")
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

## upsert_by_external_id

Create or update a customer by external ID

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **consequential**

```python
def upsert_by_external_id(
        self,
        external_id: str,
        *,
        email: str,
        name: str | None | NotGiven = NOT_GIVEN,
        locale: str | None | NotGiven = NOT_GIVEN,
        metadata: UpsertCustomerRequestApplicationJsonPropertyMetadata | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpsertCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `str` | Yes |
| email | `str` | Yes |
| name | `str \| None \| NotGiven` | No |
| locale | `str \| None \| NotGiven` | No |
| metadata | `UpsertCustomerRequestApplicationJsonPropertyMetadata \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpsertCustomerResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customers.upsert_by_external_id(
    external_id="crm_maya_314",
    email="maya.chen@example.com",
    name="Maya Chen"
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

## update_customer_by_external_id

Update a customer by external ID

[API reference](https://sell.app/docs/api/customers/identity-and-entitlements) · Effect: **consequential**

```python
def update_customer_by_external_id(
        self,
        external_id: str,
        *,
        email: str | None = None,
        name: str | None | NotGiven = NOT_GIVEN,
        locale: str | None | NotGiven = NOT_GIVEN,
        metadata: UpdateCustomerRequestApplicationJsonPropertyMetadata | None = None,
        body_external_id: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `str` | Yes |
| email | `str \| None` | No |
| name | `str \| None \| NotGiven` | No |
| locale | `str \| None \| NotGiven` | No |
| metadata | `UpdateCustomerRequestApplicationJsonPropertyMetadata \| None` | No |
| body_external_id | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCustomerResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.customers.update_customer_by_external_id(
    external_id="314",
    locale="en-US"
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

