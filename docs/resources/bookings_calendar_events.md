# bookings_calendar_events

[All resources](../methods.md)

## list

List booking date overrides

[API reference](https://sell.app/docs/api/bookings/list-booking-date-overrides) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        status: Optional[Union[BookingsStatus, str]] = None,
        pagination: Optional[bool] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkListBookingDateOverridesResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| from_ | `Optional[str]` | No |
| to | `Optional[str]` | No |
| status | `Optional[Union[BookingsStatus, str]]` | No |
| pagination | `Optional[bool]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        dates: List[str],
        available: bool,
        product_variant_id: Union[int, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkSetBookingDateAvailabilityResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| dates | `List[str]` | Yes |
| available | `bool` | Yes |
| product_variant_id | `Union[int, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

