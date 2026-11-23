# support_automation_settings

[All resources](../methods.md)

## get

Retrieve support automation settings

[API reference](https://sell.app/docs/api/support-automation-settings/retrieve-support-automation-settings) · Effect: **read**

```python
def get(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSupportAutomationSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSupportAutomationSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_settings.get()
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

## replace

Update support automation settings

[API reference](https://sell.app/docs/api/support-automation-settings/update-support-automation-settings) · Effect: **consequential**

```python
def replace(
        self,
        *,
        automation_enabled: bool | None = None,
        daily_refund_cap_cents: int | None | NotGiven = NOT_GIVEN,
        expected_automation_enabled: bool | None = None,
        expected_daily_refund_cap_cents: int | None | NotGiven = NOT_GIVEN,
        currency: Literal["USD"] | None = None,
        active_rules_count: int | None = None,
        active_refund_rules_count: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceSupportAutomationSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| automation_enabled | `bool \| None` | No |
| daily_refund_cap_cents | `int \| None \| NotGiven` | No |
| expected_automation_enabled | `bool \| None` | No |
| expected_daily_refund_cap_cents | `int \| None \| NotGiven` | No |
| currency | `Literal["USD"] \| None` | No |
| active_rules_count | `int \| None` | No |
| active_refund_rules_count | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceSupportAutomationSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_settings.replace(
    automation_enabled=True,
    daily_refund_cap_cents=5000,
    expected_automation_enabled=False,
    expected_daily_refund_cap_cents=None
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

## update

Update support automation settings

[API reference](https://sell.app/docs/api/support-automation-settings/update-support-automation-settings) · Effect: **consequential**

```python
def update(
        self,
        *,
        automation_enabled: bool | None = None,
        daily_refund_cap_cents: int | None | NotGiven = NOT_GIVEN,
        expected_automation_enabled: bool | None = None,
        expected_daily_refund_cap_cents: int | None | NotGiven = NOT_GIVEN,
        currency: Literal["USD"] | None = None,
        active_rules_count: int | None = None,
        active_refund_rules_count: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateSupportAutomationSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| automation_enabled | `bool \| None` | No |
| daily_refund_cap_cents | `int \| None \| NotGiven` | No |
| expected_automation_enabled | `bool \| None` | No |
| expected_daily_refund_cap_cents | `int \| None \| NotGiven` | No |
| currency | `Literal["USD"] \| None` | No |
| active_rules_count | `int \| None` | No |
| active_refund_rules_count | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateSupportAutomationSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_settings.update(
    automation_enabled=True,
    daily_refund_cap_cents=5000,
    expected_automation_enabled=False,
    expected_daily_refund_cap_cents=None
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

