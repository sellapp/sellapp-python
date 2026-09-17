# bookings

[All resources](../methods.md)

## list

List appointments

[API reference](https://sell.app/docs/api/bookings/list-appointments) · Effect: **read**

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
    ) -> SyncPage[SdkListAppointmentsResponseValue200ApplicationJson]:
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
        filters: Optional[
            List[SearchAppointmentsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchAppointmentsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchAppointmentsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchAppointmentsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchAppointmentsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchAppointmentsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchAppointmentsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchAppointmentsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchAppointmentsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetAppointmentResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `str` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        timezone: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateAppointmentResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `str` | Yes |
| slot_start_at | `str` | Yes |
| timezone | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCancelAppointmentResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| booking | `str` | Yes |
| status | `Literal["cancelled"]` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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

