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

## create

Create a booking product

[API reference](https://sell.app/docs/api/bookings/create-a-booking-product) · Effect: **consequential**

```python
def create(
        self,
        *,
        title: str,
        price_cents: int,
        description: str | None | NotGiven = NOT_GIVEN,
        visibility: CatalogVisibility | str | None = None,
        variant_title: str | None = None,
        variant_description: str | None = None,
        compare_at_price_cents: int | None | NotGiven = NOT_GIVEN,
        currency: SdkCreateBookingProductRequestApplicationJsonCurrency
        | str
        | None = None,
        payment_methods: builtins.list[
            SdkCreateBookingProductRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        timezone: str | None = None,
        duration_minutes: int | None = None,
        min_notice_minutes: int | None = None,
        max_advance_days: int | None = None,
        buffer_before_minutes: int | None = None,
        buffer_after_minutes: int | None = None,
        provider_connection_ids: builtins.list[int] | None = None,
        video_provider: SdkCreateBookingProductRequestApplicationJsonVideoProvider
        | str
        | None = None,
        video_provider_connection_id: int | None | NotGiven = NOT_GIVEN,
        reminders_enabled: bool | None = None,
        reminder_offset_value: int | None = None,
        reminder_offset_unit: SdkCreateBookingProductRequestApplicationJsonReminderOffsetUnit
        | str
        | None = None,
        availability: builtins.list[
            CreateBookingProductRequestApplicationJsonPropertyAvailabilityItem
        ]
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateBookingProductResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| title | `str` | Yes |
| price_cents | `int` | Yes |
| description | `str \| None \| NotGiven` | No |
| visibility | `CatalogVisibility \| str \| None` | No |
| variant_title | `str \| None` | No |
| variant_description | `str \| None` | No |
| compare_at_price_cents | `int \| None \| NotGiven` | No |
| currency | `SdkCreateBookingProductRequestApplicationJsonCurrency
        \| str
        \| None` | No |
| payment_methods | `builtins.list[
            SdkCreateBookingProductRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| timezone | `str \| None` | No |
| duration_minutes | `int \| None` | No |
| min_notice_minutes | `int \| None` | No |
| max_advance_days | `int \| None` | No |
| buffer_before_minutes | `int \| None` | No |
| buffer_after_minutes | `int \| None` | No |
| provider_connection_ids | `builtins.list[int] \| None` | No |
| video_provider | `SdkCreateBookingProductRequestApplicationJsonVideoProvider
        \| str
        \| None` | No |
| video_provider_connection_id | `int \| None \| NotGiven` | No |
| reminders_enabled | `bool \| None` | No |
| reminder_offset_value | `int \| None` | No |
| reminder_offset_unit | `SdkCreateBookingProductRequestApplicationJsonReminderOffsetUnit
        \| str
        \| None` | No |
| availability | `builtins.list[
            CreateBookingProductRequestApplicationJsonPropertyAvailabilityItem
        ]
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateBookingProductResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bookings.create(
    title="Strategy consultation",
    description="<p>A private strategy session for your next launch.</p>",
    variant_title="60 minute session",
    price_cents=2500,
    currency="USD",
    payment_methods=["STRIPE"],
    timezone="Europe/London",
    duration_minutes=60,
    availability=[
        {"day": 1, "enabled": True, "start": "09:00", "end": "12:00"},
        {"day": 3, "enabled": True, "start": "13:00", "end": "17:00"}
    ]
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

Documented HTTP responses: 201, 400, 401, 403, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

