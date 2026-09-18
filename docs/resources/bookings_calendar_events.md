# bookings_calendar_events

[All resources](../methods.md)

## list

List booking date overrides

[API reference](https://sell.app/docs/api/bookings/list-booking-date-overrides) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        product_variant_id: int | None = None,
        from_: str | None = None,
        to: str | None = None,
        status: BookingsStatus | str | None = None,
        pagination: bool | None = None,
        page: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkListBookingDateOverridesResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| product_variant_id | `int \| None` | No |
| from_ | `str \| None` | No |
| to | `str \| None` | No |
| status | `BookingsStatus \| str \| None` | No |
| pagination | `bool \| None` | No |
| page | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkListBookingDateOverridesResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bookings_calendar_events.list()
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

## set

Set booking date availability

[API reference](https://sell.app/docs/api/bookings/set-booking-date-availability) · Effect: **consequential**

```python
def set(
        self,
        *,
        dates: builtins.list[str],
        available: bool,
        product_variant_id: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkSetBookingDateAvailabilityResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| dates | `builtins.list[str]` | Yes |
| available | `bool` | Yes |
| product_variant_id | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkSetBookingDateAvailabilityResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.bookings_calendar_events.set(
    product_variant_id=73,
    dates=["2028-03-26", "2028-03-27"],
    available=False
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

