# store_settings

[All resources](../methods.md)

## get

Retrieve store settings

[API reference](https://sell.app/docs/api/store-settings/retrieve-store-settings) · Effect: **read**

```python
def get(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetStoreSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetStoreSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.get()
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

## replace_general

Update general store settings

[API reference](https://sell.app/docs/api/store-settings/update-general-settings) · Effect: **consequential**

```python
def replace_general(
        self,
        *,
        name: str,
        visibility: CourseVisibility | str,
        timezone: str,
        currency: str,
        dark_mode: DarkMode | str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceGeneralStoreSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| visibility | `CourseVisibility \| str` | Yes |
| timezone | `str` | Yes |
| currency | `str` | Yes |
| dark_mode | `DarkMode \| str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceGeneralStoreSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_general(
    name="Launch Lab",
    visibility="HIDDEN",
    timezone="Europe/London",
    currency="USD"
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

## update_general

Update general store settings

[API reference](https://sell.app/docs/api/store-settings/update-general-settings) · Effect: **consequential**

```python
def update_general(
        self,
        *,
        name: str | None = None,
        visibility: CourseVisibility | str | None = None,
        timezone: str | None = None,
        currency: str | None = None,
        dark_mode: DarkMode | str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateGeneralStoreSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str \| None` | No |
| visibility | `CourseVisibility \| str \| None` | No |
| timezone | `str \| None` | No |
| currency | `str \| None` | No |
| dark_mode | `DarkMode \| str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateGeneralStoreSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_general(name="Launch Lab")
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

## replace_analytics

Update analytics settings

[API reference](https://sell.app/docs/api/store-settings/update-analytics-settings) · Effect: **consequential**

```python
def replace_analytics(
        self,
        *,
        ga_4_measurement_id: str | None | NotGiven = NOT_GIVEN,
        meta_pixel_id: str | None | NotGiven = NOT_GIVEN,
        tiktok_pixel_id: str | None | NotGiven = NOT_GIVEN,
        ga_4_api_secret: str | None | NotGiven = NOT_GIVEN,
        meta_access_token: str | None | NotGiven = NOT_GIVEN,
        tiktok_access_token: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceAnalyticsSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ga_4_measurement_id | `str \| None \| NotGiven` | No |
| meta_pixel_id | `str \| None \| NotGiven` | No |
| tiktok_pixel_id | `str \| None \| NotGiven` | No |
| ga_4_api_secret | `str \| None \| NotGiven` | No |
| meta_access_token | `str \| None \| NotGiven` | No |
| tiktok_access_token | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceAnalyticsSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_analytics(ga_4_measurement_id=None)
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

## update_analytics

Update analytics settings

[API reference](https://sell.app/docs/api/store-settings/update-analytics-settings) · Effect: **consequential**

```python
def update_analytics(
        self,
        *,
        ga_4_measurement_id: str | None | NotGiven = NOT_GIVEN,
        meta_pixel_id: str | None | NotGiven = NOT_GIVEN,
        tiktok_pixel_id: str | None | NotGiven = NOT_GIVEN,
        ga_4_api_secret: str | None | NotGiven = NOT_GIVEN,
        meta_access_token: str | None | NotGiven = NOT_GIVEN,
        tiktok_access_token: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateAnalyticsSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ga_4_measurement_id | `str \| None \| NotGiven` | No |
| meta_pixel_id | `str \| None \| NotGiven` | No |
| tiktok_pixel_id | `str \| None \| NotGiven` | No |
| ga_4_api_secret | `str \| None \| NotGiven` | No |
| meta_access_token | `str \| None \| NotGiven` | No |
| tiktok_access_token | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateAnalyticsSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_analytics(ga_4_measurement_id=None)
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

## replace_marketing

Update marketing settings

[API reference](https://sell.app/docs/api/store-settings/update-marketing-settings) · Effect: **consequential**

```python
def replace_marketing(
        self,
        *,
        abandoned_cart: ReplaceMarketingSettingsRequestApplicationJsonPropertyAbandonedCart,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceMarketingSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| abandoned_cart | `ReplaceMarketingSettingsRequestApplicationJsonPropertyAbandonedCart` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceMarketingSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_marketing(abandoned_cart={"enabled": False})
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

## update_marketing

Update marketing settings

[API reference](https://sell.app/docs/api/store-settings/update-marketing-settings) · Effect: **consequential**

```python
def update_marketing(
        self,
        *,
        abandoned_cart: UpdateMarketingSettingsRequestApplicationJsonPropertyAbandonedCart,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateMarketingSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| abandoned_cart | `UpdateMarketingSettingsRequestApplicationJsonPropertyAbandonedCart` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateMarketingSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_marketing(abandoned_cart={"enabled": False})
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

## get_checkout

Retrieve checkout settings

[API reference](https://sell.app/docs/api/store-settings/checkout-settings) · Effect: **read**

```python
def get_checkout(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCheckoutSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCheckoutSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.get_checkout()
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

## replace_checkout

Update checkout settings

[API reference](https://sell.app/docs/api/store-settings/checkout-settings) · Effect: **consequential**

```python
def replace_checkout(
        self,
        *,
        shopping_cart_enabled: bool,
        customer_email_required: bool,
        allow_vpn_purchases: bool,
        blacklist_on_dispute: bool,
        minimum_spend: str | None,
        billing_descriptor: str | None,
        attempts_per_customer: int,
        attempts_per_ip: int | None,
        attempts_per_email: int | None,
        attempts_per_fingerprint: int | None,
        rate_limit_window_seconds: int,
        crypto: ReplaceCheckoutSettingsRequestApplicationJsonPropertyCrypto
        | None
        | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCheckoutSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| shopping_cart_enabled | `bool` | Yes |
| customer_email_required | `bool` | Yes |
| allow_vpn_purchases | `bool` | Yes |
| blacklist_on_dispute | `bool` | Yes |
| minimum_spend | `str \| None` | Yes |
| billing_descriptor | `str \| None` | Yes |
| attempts_per_customer | `int` | Yes |
| attempts_per_ip | `int \| None` | Yes |
| attempts_per_email | `int \| None` | Yes |
| attempts_per_fingerprint | `int \| None` | Yes |
| rate_limit_window_seconds | `int` | Yes |
| crypto | `ReplaceCheckoutSettingsRequestApplicationJsonPropertyCrypto
        \| None
        \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceCheckoutSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_checkout(
    shopping_cart_enabled=True,
    customer_email_required=True,
    allow_vpn_purchases=True,
    blacklist_on_dispute=True,
    minimum_spend="5.00",
    billing_descriptor="LAUNCH LAB",
    attempts_per_customer=5,
    attempts_per_ip=20,
    attempts_per_email=None,
    attempts_per_fingerprint=None,
    rate_limit_window_seconds=3600,
    crypto={"underpaid_percentage": 2, "minimum_confirmations": 2}
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

## update_checkout

Update checkout settings

[API reference](https://sell.app/docs/api/store-settings/checkout-settings) · Effect: **consequential**

```python
def update_checkout(
        self,
        *,
        shopping_cart_enabled: bool | None = None,
        customer_email_required: bool | None = None,
        allow_vpn_purchases: bool | None = None,
        blacklist_on_dispute: bool | None = None,
        minimum_spend: str | None | NotGiven = NOT_GIVEN,
        billing_descriptor: str | None | NotGiven = NOT_GIVEN,
        attempts_per_customer: int | None = None,
        attempts_per_ip: int | None | NotGiven = NOT_GIVEN,
        attempts_per_email: int | None | NotGiven = NOT_GIVEN,
        attempts_per_fingerprint: int | None | NotGiven = NOT_GIVEN,
        rate_limit_window_seconds: int | None = None,
        crypto: UpdateCheckoutSettingsRequestApplicationJsonPropertyCrypto
        | None
        | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCheckoutSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| shopping_cart_enabled | `bool \| None` | No |
| customer_email_required | `bool \| None` | No |
| allow_vpn_purchases | `bool \| None` | No |
| blacklist_on_dispute | `bool \| None` | No |
| minimum_spend | `str \| None \| NotGiven` | No |
| billing_descriptor | `str \| None \| NotGiven` | No |
| attempts_per_customer | `int \| None` | No |
| attempts_per_ip | `int \| None \| NotGiven` | No |
| attempts_per_email | `int \| None \| NotGiven` | No |
| attempts_per_fingerprint | `int \| None \| NotGiven` | No |
| rate_limit_window_seconds | `int \| None` | No |
| crypto | `UpdateCheckoutSettingsRequestApplicationJsonPropertyCrypto
        \| None
        \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCheckoutSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_checkout(
    minimum_spend="10.00",
    attempts_per_email=10
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

## get_taxes

Retrieve tax settings

[API reference](https://sell.app/docs/api/store-settings/tax-settings) · Effect: **read**

```python
def get_taxes(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetTaxSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetTaxSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.get_taxes()
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

## replace_taxes

Update tax settings

[API reference](https://sell.app/docs/api/store-settings/tax-settings) · Effect: **consequential**

```python
def replace_taxes(
        self,
        *,
        vat_enabled: bool,
        vat_inclusive_pricing: bool,
        collect_billing_details: bool,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceTaxSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| vat_enabled | `bool` | Yes |
| vat_inclusive_pricing | `bool` | Yes |
| collect_billing_details | `bool` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceTaxSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_taxes(
    vat_enabled=True,
    vat_inclusive_pricing=True,
    collect_billing_details=False
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

## update_taxes

Update tax settings

[API reference](https://sell.app/docs/api/store-settings/tax-settings) · Effect: **consequential**

```python
def update_taxes(
        self,
        *,
        vat_enabled: bool | None = None,
        vat_inclusive_pricing: bool | None = None,
        collect_billing_details: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateTaxSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| vat_enabled | `bool \| None` | No |
| vat_inclusive_pricing | `bool \| None` | No |
| collect_billing_details | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateTaxSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_taxes(vat_inclusive_pricing=True)
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

## get_customer_emails

Retrieve customer email settings

[API reference](https://sell.app/docs/api/store-settings/customer-email-settings) · Effect: **read**

```python
def get_customer_emails(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetCustomerEmailSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetCustomerEmailSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.get_customer_emails()
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

## replace_customer_emails

Update customer email settings

[API reference](https://sell.app/docs/api/store-settings/customer-email-settings) · Effect: **consequential**

```python
def replace_customer_emails(
        self,
        *,
        send_delivery_email: bool,
        send_payment_failure_email: bool,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCustomerEmailSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| send_delivery_email | `bool` | Yes |
| send_payment_failure_email | `bool` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceCustomerEmailSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_customer_emails(
    send_delivery_email=True,
    send_payment_failure_email=False
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

## update_customer_emails

Update customer email settings

[API reference](https://sell.app/docs/api/store-settings/customer-email-settings) · Effect: **consequential**

```python
def update_customer_emails(
        self,
        *,
        send_delivery_email: bool | None = None,
        send_payment_failure_email: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCustomerEmailSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| send_delivery_email | `bool \| None` | No |
| send_payment_failure_email | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCustomerEmailSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_customer_emails(send_payment_failure_email=False)
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

## get_store_alerts

Retrieve store alert settings

[API reference](https://sell.app/docs/api/store-settings/store-alert-settings) · Effect: **read**

```python
def get_store_alerts(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetStoreAlertSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetStoreAlertSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.get_store_alerts()
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

## replace_store_alerts

Update store alert settings

[API reference](https://sell.app/docs/api/store-settings/store-alert-settings) · Effect: **consequential**

```python
def replace_store_alerts(
        self,
        *,
        sale_emails_enabled: bool,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceStoreAlertSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| sale_emails_enabled | `bool` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceStoreAlertSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_store_alerts(sale_emails_enabled=False)
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

## update_store_alerts

Update store alert settings

[API reference](https://sell.app/docs/api/store-settings/store-alert-settings) · Effect: **consequential**

```python
def update_store_alerts(
        self,
        *,
        sale_emails_enabled: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateStoreAlertSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| sale_emails_enabled | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateStoreAlertSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_store_alerts(sale_emails_enabled=False)
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

## get_personalization

Retrieve personalization settings

[API reference](https://sell.app/docs/api/store-settings/personalization-settings) · Effect: **read**

```python
def get_personalization(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetPersonalizationSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetPersonalizationSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.get_personalization()
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

## replace_personalization

Update personalization settings

[API reference](https://sell.app/docs/api/store-settings/personalization-settings) · Effect: **consequential**

```python
def replace_personalization(
        self,
        *,
        support_email: str | None,
        trustpilot_email: str | None,
        sender_name: str | None,
        store_address: str | None,
        store_city: str | None,
        store_state: str | None,
        store_zip: str | None,
        store_country: str | None,
        store_tax: str | None,
        back_link_label: str | None,
        back_link_url: str | None,
        sender_email: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplacePersonalizationSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_email | `str \| None` | Yes |
| trustpilot_email | `str \| None` | Yes |
| sender_name | `str \| None` | Yes |
| store_address | `str \| None` | Yes |
| store_city | `str \| None` | Yes |
| store_state | `str \| None` | Yes |
| store_zip | `str \| None` | Yes |
| store_country | `str \| None` | Yes |
| store_tax | `str \| None` | Yes |
| back_link_label | `str \| None` | Yes |
| back_link_url | `str \| None` | Yes |
| sender_email | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplacePersonalizationSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_personalization(
    support_email="support@launch-lab.example.com",
    trustpilot_email=None,
    sender_name="Launch Lab",
    sender_email="orders@launch-lab.example.com",
    store_address="651 N Broad St, Suite 206",
    store_city="Middletown",
    store_state="Delaware",
    store_zip="19709",
    store_country="United States",
    store_tax="EIN 98-7654321",
    back_link_label="Back to Launch Lab",
    back_link_url="https://launch-lab.example.com"
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

## update_personalization

Update personalization settings

[API reference](https://sell.app/docs/api/store-settings/personalization-settings) · Effect: **consequential**

```python
def update_personalization(
        self,
        *,
        support_email: str | None | NotGiven = NOT_GIVEN,
        trustpilot_email: str | None | NotGiven = NOT_GIVEN,
        sender_name: str | None | NotGiven = NOT_GIVEN,
        sender_email: str | None | NotGiven = NOT_GIVEN,
        store_address: str | None | NotGiven = NOT_GIVEN,
        store_city: str | None | NotGiven = NOT_GIVEN,
        store_state: str | None | NotGiven = NOT_GIVEN,
        store_zip: str | None | NotGiven = NOT_GIVEN,
        store_country: str | None | NotGiven = NOT_GIVEN,
        store_tax: str | None | NotGiven = NOT_GIVEN,
        back_link_label: str | None | NotGiven = NOT_GIVEN,
        back_link_url: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdatePersonalizationSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_email | `str \| None \| NotGiven` | No |
| trustpilot_email | `str \| None \| NotGiven` | No |
| sender_name | `str \| None \| NotGiven` | No |
| sender_email | `str \| None \| NotGiven` | No |
| store_address | `str \| None \| NotGiven` | No |
| store_city | `str \| None \| NotGiven` | No |
| store_state | `str \| None \| NotGiven` | No |
| store_zip | `str \| None \| NotGiven` | No |
| store_country | `str \| None \| NotGiven` | No |
| store_tax | `str \| None \| NotGiven` | No |
| back_link_label | `str \| None \| NotGiven` | No |
| back_link_url | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdatePersonalizationSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_personalization(
    back_link_label="Return to the shop",
    back_link_url="https://launch-lab.example.com/shop"
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

## replace_crypto_checkout

Update crypto checkout settings

[API reference](https://sell.app/docs/api/store-settings/crypto-checkout-settings) · Effect: **consequential**

```python
def replace_crypto_checkout(
        self,
        *,
        underpaid_percentage: int,
        minimum_confirmations: int,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceCryptoCheckoutSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| underpaid_percentage | `int` | Yes |
| minimum_confirmations | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceCryptoCheckoutSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.replace_crypto_checkout(
    underpaid_percentage=1,
    minimum_confirmations=3
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

## update_crypto_checkout

Update crypto checkout settings

[API reference](https://sell.app/docs/api/store-settings/crypto-checkout-settings) · Effect: **consequential**

```python
def update_crypto_checkout(
        self,
        *,
        underpaid_percentage: int | None = None,
        minimum_confirmations: int | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateCryptoCheckoutSettingsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| underpaid_percentage | `int \| None` | No |
| minimum_confirmations | `int \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateCryptoCheckoutSettingsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.store_settings.update_crypto_checkout(minimum_confirmations=3)
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

