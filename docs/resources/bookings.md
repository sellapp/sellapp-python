# bookings

[All resources](../methods.md)

## list

List appointments

[API reference](https://sell.app/docs/api/bookings/list-appointments) · Effect: **read**

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
    ) -> SyncPage[SdkListAppointmentsResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkListAppointmentsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bookings.list()
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

## search

Search appointments

[API reference](https://sell.app/docs/api/bookings/search-appointments) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[
            SearchAppointmentsRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchAppointmentsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchAppointmentsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchAppointmentsRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchAppointmentsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[
            SearchAppointmentsRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchAppointmentsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchAppointmentsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchAppointmentsRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkSearchAppointmentsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bookings.search(
    filters=[
        {
            "field": "id",
            "operator": "=",
            "value": "018f61d6-1c46-7b42-8a94-522bc6b5c53f"
        }
    ],
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

Retrieve an appointment

[API reference](https://sell.app/docs/api/bookings/retrieve-an-appointment) · Effect: **read**

```python
def get(
        self,
        booking: str,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetAppointmentResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetAppointmentResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bookings.get(booking="018f61d6-1c46-7b42-8a94-522bc6b5c53f")
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

Update an appointment

[API reference](https://sell.app/docs/api/bookings/update-an-appointment) · Effect: **consequential**

```python
def update(
        self,
        booking: str,
        *,
        slot_start_at: str,
        timezone: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateAppointmentResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `str` | Yes |
| slot_start_at | `str` | Yes |
| timezone | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateAppointmentResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bookings.update(
    booking="018f61d6-1c46-7b42-8a94-522bc6b5c53f",
    slot_start_at="2028-03-27T10:00:00+01:00",
    timezone="Europe/London"
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

## cancel

Cancel an appointment

[API reference](https://sell.app/docs/api/bookings/update-an-appointment) · Effect: **consequential**

```python
def cancel(
        self,
        booking: str,
        *,
        status: Literal["cancelled"],
        request_options: RequestOptions | None = None,
    ) -> SdkCancelAppointmentResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `str` | Yes |
| status | `Literal["cancelled"]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCancelAppointmentResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bookings.cancel(
    booking="018f61d6-1c46-7b42-8a94-522bc6b5c53f",
    status="cancelled"
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

