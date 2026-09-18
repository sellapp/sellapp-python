# product_variants_booking

[All resources](../methods.md)

## list_availability

List booking availability

[API reference](https://sell.app/docs/api/product-variants/list-booking-availability) · Effect: **read**

```python
def list_availability(
        self,
        product: int,
        variant: int,
        *,
        from_: str | None = None,
        to: str | None = None,
        quantity: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkListBookingAvailabilityResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| from_ | `str \| None` | No |
| to | `str \| None` | No |
| quantity | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkListBookingAvailabilityResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_booking.list_availability(
    product=1,
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

## create_hold

Create a booking hold

[API reference](https://sell.app/docs/api/product-variants/create-booking-hold) · Effect: **consequential**

```python
def create_hold(
        self,
        product: int,
        variant: int,
        *,
        slot_start_at: str,
        quantity: int | None = None,
        customer_key: str | None | NotGiven = NOT_GIVEN,
        meta: CreateBookingHoldRequestApplicationJsonPropertyMeta | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateBookingHoldResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| slot_start_at | `str` | Yes |
| quantity | `int \| None` | No |
| customer_key | `str \| None \| NotGiven` | No |
| meta | `CreateBookingHoldRequestApplicationJsonPropertyMeta \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateBookingHoldResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_booking.create_hold(
    product=1,
    variant=1,
    slot_start_at="2026-06-22T14:00:00+00:00",
    quantity=1,
    customer_key="visitor-session-123",
    meta={"customer_timezone": "America/New_York"}
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

## release_hold

Release a booking hold

[API reference](https://sell.app/docs/api/product-variants/release-booking-hold) · Effect: **consequential**

```python
def release_hold(
        self,
        product: int,
        hold: str,
        *,
        customer_key: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| hold | `str` | Yes |
| customer_key | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_booking.release_hold(
    product=1,
    hold="string_example",
    customer_key="visitor-session-123"
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

## get

Retrieve booking configuration

[API reference](https://sell.app/docs/api/bookings/retrieve-booking-configuration) · Effect: **read**

```python
def get(
        self,
        product: str,
        variant: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetBookingConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetBookingConfigurationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_booking.get(
    product="41",
    variant=73
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

Update booking configuration

[API reference](https://sell.app/docs/api/bookings/update-booking-configuration) · Effect: **consequential**

```python
def replace(
        self,
        product: str,
        variant: int,
        *,
        mode: Literal["native"] | None = None,
        conflict_scope: SdkReplaceBookingConfigurationRequestApplicationJsonConflictScope
        | str
        | None = None,
        timezone: str | None = None,
        duration_minutes: int | None = None,
        capacity_per_slot: int | None = None,
        min_notice_minutes: int | None = None,
        max_advance_days: int | None = None,
        buffer_before_minutes: int | None = None,
        buffer_after_minutes: int | None = None,
        availability: list[
            ReplaceBookingConfigurationRequestApplicationJsonPropertyAvailabilityItem
        ]
        | None = None,
        provider_connection_ids: list[int] | None = None,
        video_provider: SdkReplaceBookingConfigurationRequestApplicationJsonVideoProvider
        | str
        | None = None,
        video_provider_connection_id: int | None | NotGiven = NOT_GIVEN,
        reminders_enabled: bool | None = None,
        reminder_offset_value: int | None = None,
        reminder_offset_unit: SdkReplaceBookingConfigurationRequestApplicationJsonReminderOffsetUnit
        | str
        | None = None,
        meta: ReplaceBookingConfigurationRequestApplicationJsonPropertyMeta
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceBookingConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| mode | `Literal["native"] \| None` | No |
| conflict_scope | `SdkReplaceBookingConfigurationRequestApplicationJsonConflictScope
        \| str
        \| None` | No |
| timezone | `str \| None` | No |
| duration_minutes | `int \| None` | No |
| capacity_per_slot | `int \| None` | No |
| min_notice_minutes | `int \| None` | No |
| max_advance_days | `int \| None` | No |
| buffer_before_minutes | `int \| None` | No |
| buffer_after_minutes | `int \| None` | No |
| availability | `list[
            ReplaceBookingConfigurationRequestApplicationJsonPropertyAvailabilityItem
        ]
        \| None` | No |
| provider_connection_ids | `list[int] \| None` | No |
| video_provider | `SdkReplaceBookingConfigurationRequestApplicationJsonVideoProvider
        \| str
        \| None` | No |
| video_provider_connection_id | `int \| None \| NotGiven` | No |
| reminders_enabled | `bool \| None` | No |
| reminder_offset_value | `int \| None` | No |
| reminder_offset_unit | `SdkReplaceBookingConfigurationRequestApplicationJsonReminderOffsetUnit
        \| str
        \| None` | No |
| meta | `ReplaceBookingConfigurationRequestApplicationJsonPropertyMeta
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceBookingConfigurationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_booking.replace(
    product="41",
    variant=73,
    timezone="Europe/London",
    duration_minutes=60,
    capacity_per_slot=1,
    min_notice_minutes=1440,
    max_advance_days=60
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

Update booking configuration

[API reference](https://sell.app/docs/api/bookings/update-booking-configuration) · Effect: **consequential**

```python
def update(
        self,
        product: str,
        variant: int,
        *,
        mode: Literal["native"] | None = None,
        conflict_scope: SdkUpdateBookingConfigurationRequestApplicationJsonConflictScope
        | str
        | None = None,
        timezone: str | None = None,
        duration_minutes: int | None = None,
        capacity_per_slot: int | None = None,
        min_notice_minutes: int | None = None,
        max_advance_days: int | None = None,
        buffer_before_minutes: int | None = None,
        buffer_after_minutes: int | None = None,
        availability: list[
            UpdateBookingConfigurationRequestApplicationJsonPropertyAvailabilityItem
        ]
        | None = None,
        provider_connection_ids: list[int] | None = None,
        video_provider: SdkUpdateBookingConfigurationRequestApplicationJsonVideoProvider
        | str
        | None = None,
        video_provider_connection_id: int | None | NotGiven = NOT_GIVEN,
        reminders_enabled: bool | None = None,
        reminder_offset_value: int | None = None,
        reminder_offset_unit: SdkUpdateBookingConfigurationRequestApplicationJsonReminderOffsetUnit
        | str
        | None = None,
        meta: UpdateBookingConfigurationRequestApplicationJsonPropertyMeta
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateBookingConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| mode | `Literal["native"] \| None` | No |
| conflict_scope | `SdkUpdateBookingConfigurationRequestApplicationJsonConflictScope
        \| str
        \| None` | No |
| timezone | `str \| None` | No |
| duration_minutes | `int \| None` | No |
| capacity_per_slot | `int \| None` | No |
| min_notice_minutes | `int \| None` | No |
| max_advance_days | `int \| None` | No |
| buffer_before_minutes | `int \| None` | No |
| buffer_after_minutes | `int \| None` | No |
| availability | `list[
            UpdateBookingConfigurationRequestApplicationJsonPropertyAvailabilityItem
        ]
        \| None` | No |
| provider_connection_ids | `list[int] \| None` | No |
| video_provider | `SdkUpdateBookingConfigurationRequestApplicationJsonVideoProvider
        \| str
        \| None` | No |
| video_provider_connection_id | `int \| None \| NotGiven` | No |
| reminders_enabled | `bool \| None` | No |
| reminder_offset_value | `int \| None` | No |
| reminder_offset_unit | `SdkUpdateBookingConfigurationRequestApplicationJsonReminderOffsetUnit
        \| str
        \| None` | No |
| meta | `UpdateBookingConfigurationRequestApplicationJsonPropertyMeta
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateBookingConfigurationResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.product_variants_booking.update(
    product="41",
    variant=73,
    timezone="Europe/London",
    duration_minutes=60,
    capacity_per_slot=1,
    min_notice_minutes=1440,
    max_advance_days=60
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

