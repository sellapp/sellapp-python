# customers

[All resources](../methods.md)

## list

List customers

[API reference](https://sell.app/docs/api/customers/list-customers) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkListCustomersResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        external_id: Optional[str] = None,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        locale: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Optional[CreateCustomerRequestApplicationJsonPropertyMetadata] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateCustomerResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `str` | Yes |
| external_id | `Optional[str]` | No |
| name | `Union[str, None, NotGiven]` | No |
| locale | `Union[str, None, NotGiven]` | No |
| metadata | `Optional[CreateCustomerRequestApplicationJsonPropertyMetadata]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchCustomersRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchCustomersRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchCustomersRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchCustomersRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchCustomersResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchCustomersRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchCustomersRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchCustomersRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchCustomersRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        email: Optional[str] = None,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        locale: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Optional[UpdateCustomerRequestApplicationJsonPropertyMetadata] = None,
        external_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer | `int` | Yes |
| email | `Optional[str]` | No |
| name | `Union[str, None, NotGiven]` | No |
| locale | `Union[str, None, NotGiven]` | No |
| metadata | `Optional[UpdateCustomerRequestApplicationJsonPropertyMetadata]` | No |
| external_id | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        locale: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Optional[UpsertCustomerRequestApplicationJsonPropertyMetadata] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpsertCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `str` | Yes |
| email | `str` | Yes |
| name | `Union[str, None, NotGiven]` | No |
| locale | `Union[str, None, NotGiven]` | No |
| metadata | `Optional[UpsertCustomerRequestApplicationJsonPropertyMetadata]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        email: Optional[str] = None,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        locale: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Optional[UpdateCustomerRequestApplicationJsonPropertyMetadata] = None,
        body_external_id: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCustomerResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| external_id | `str` | Yes |
| email | `Optional[str]` | No |
| name | `Union[str, None, NotGiven]` | No |
| locale | `Union[str, None, NotGiven]` | No |
| metadata | `Optional[UpdateCustomerRequestApplicationJsonPropertyMetadata]` | No |
| body_external_id | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

