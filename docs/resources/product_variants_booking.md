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
        from_: Optional[str] = None,
        to: Optional[str] = None,
        quantity: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListBookingAvailabilityResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| from_ | `Optional[str]` | No |
| to | `Optional[str]` | No |
| quantity | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        quantity: Optional[int] = None,
        customer_key: Union[str, None, NotGiven] = NOT_GIVEN,
        meta: Optional[CreateBookingHoldRequestApplicationJsonPropertyMeta] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateBookingHoldResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| variant | `int` | Yes |
| slot_start_at | `str` | Yes |
| quantity | `Optional[int]` | No |
| customer_key | `Union[str, None, NotGiven]` | No |
| meta | `Optional[CreateBookingHoldRequestApplicationJsonPropertyMeta]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        customer_key: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `int` | Yes |
| hold | `str` | Yes |
| customer_key | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetBookingConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        mode: Optional[Literal["native"]] = None,
        conflict_scope: Optional[
            Union[
                SdkReplaceBookingConfigurationRequestApplicationJsonConflictScope, str
            ]
        ] = None,
        timezone: Optional[str] = None,
        duration_minutes: Optional[int] = None,
        capacity_per_slot: Optional[int] = None,
        min_notice_minutes: Optional[int] = None,
        max_advance_days: Optional[int] = None,
        buffer_before_minutes: Optional[int] = None,
        buffer_after_minutes: Optional[int] = None,
        availability: Optional[
            List[
                ReplaceBookingConfigurationRequestApplicationJsonPropertyAvailabilityItem
            ]
        ] = None,
        provider_connection_ids: Optional[List[int]] = None,
        video_provider: Optional[
            Union[
                SdkReplaceBookingConfigurationRequestApplicationJsonVideoProvider, str
            ]
        ] = None,
        video_provider_connection_id: Union[int, None, NotGiven] = NOT_GIVEN,
        reminders_enabled: Optional[bool] = None,
        reminder_offset_value: Optional[int] = None,
        reminder_offset_unit: Optional[
            Union[
                SdkReplaceBookingConfigurationRequestApplicationJsonReminderOffsetUnit,
                str,
            ]
        ] = None,
        meta: Optional[
            ReplaceBookingConfigurationRequestApplicationJsonPropertyMeta
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplaceBookingConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| mode | `Optional[Literal["native"]]` | No |
| conflict_scope | `Optional[
            Union[
                SdkReplaceBookingConfigurationRequestApplicationJsonConflictScope, str
            ]
        ]` | No |
| timezone | `Optional[str]` | No |
| duration_minutes | `Optional[int]` | No |
| capacity_per_slot | `Optional[int]` | No |
| min_notice_minutes | `Optional[int]` | No |
| max_advance_days | `Optional[int]` | No |
| buffer_before_minutes | `Optional[int]` | No |
| buffer_after_minutes | `Optional[int]` | No |
| availability | `Optional[
            List[
                ReplaceBookingConfigurationRequestApplicationJsonPropertyAvailabilityItem
            ]
        ]` | No |
| provider_connection_ids | `Optional[List[int]]` | No |
| video_provider | `Optional[
            Union[
                SdkReplaceBookingConfigurationRequestApplicationJsonVideoProvider, str
            ]
        ]` | No |
| video_provider_connection_id | `Union[int, None, NotGiven]` | No |
| reminders_enabled | `Optional[bool]` | No |
| reminder_offset_value | `Optional[int]` | No |
| reminder_offset_unit | `Optional[
            Union[
                SdkReplaceBookingConfigurationRequestApplicationJsonReminderOffsetUnit,
                str,
            ]
        ]` | No |
| meta | `Optional[
            ReplaceBookingConfigurationRequestApplicationJsonPropertyMeta
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        mode: Optional[Literal["native"]] = None,
        conflict_scope: Optional[
            Union[SdkUpdateBookingConfigurationRequestApplicationJsonConflictScope, str]
        ] = None,
        timezone: Optional[str] = None,
        duration_minutes: Optional[int] = None,
        capacity_per_slot: Optional[int] = None,
        min_notice_minutes: Optional[int] = None,
        max_advance_days: Optional[int] = None,
        buffer_before_minutes: Optional[int] = None,
        buffer_after_minutes: Optional[int] = None,
        availability: Optional[
            List[
                UpdateBookingConfigurationRequestApplicationJsonPropertyAvailabilityItem
            ]
        ] = None,
        provider_connection_ids: Optional[List[int]] = None,
        video_provider: Optional[
            Union[SdkUpdateBookingConfigurationRequestApplicationJsonVideoProvider, str]
        ] = None,
        video_provider_connection_id: Union[int, None, NotGiven] = NOT_GIVEN,
        reminders_enabled: Optional[bool] = None,
        reminder_offset_value: Optional[int] = None,
        reminder_offset_unit: Optional[
            Union[
                SdkUpdateBookingConfigurationRequestApplicationJsonReminderOffsetUnit,
                str,
            ]
        ] = None,
        meta: Optional[
            UpdateBookingConfigurationRequestApplicationJsonPropertyMeta
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateBookingConfigurationResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product | `str` | Yes |
| variant | `int` | Yes |
| mode | `Optional[Literal["native"]]` | No |
| conflict_scope | `Optional[
            Union[SdkUpdateBookingConfigurationRequestApplicationJsonConflictScope, str]
        ]` | No |
| timezone | `Optional[str]` | No |
| duration_minutes | `Optional[int]` | No |
| capacity_per_slot | `Optional[int]` | No |
| min_notice_minutes | `Optional[int]` | No |
| max_advance_days | `Optional[int]` | No |
| buffer_before_minutes | `Optional[int]` | No |
| buffer_after_minutes | `Optional[int]` | No |
| availability | `Optional[
            List[
                UpdateBookingConfigurationRequestApplicationJsonPropertyAvailabilityItem
            ]
        ]` | No |
| provider_connection_ids | `Optional[List[int]]` | No |
| video_provider | `Optional[
            Union[SdkUpdateBookingConfigurationRequestApplicationJsonVideoProvider, str]
        ]` | No |
| video_provider_connection_id | `Union[int, None, NotGiven]` | No |
| reminders_enabled | `Optional[bool]` | No |
| reminder_offset_value | `Optional[int]` | No |
| reminder_offset_unit | `Optional[
            Union[
                SdkUpdateBookingConfigurationRequestApplicationJsonReminderOffsetUnit,
                str,
            ]
        ]` | No |
| meta | `Optional[
            UpdateBookingConfigurationRequestApplicationJsonPropertyMeta
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

