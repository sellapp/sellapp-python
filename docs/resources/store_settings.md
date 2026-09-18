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

