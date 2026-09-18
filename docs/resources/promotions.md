# promotions

[All resources](../methods.md)

## list

List promotions

[API reference](https://sell.app/docs/api/promotions/list-promotions) · Effect: **read**

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
    ) -> SyncPage[SdkListPromotionsResponseValue200ApplicationJson]:
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

Returns: `SyncPage[SdkListPromotionsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions.list()
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

## create

Create a promotion

[API reference](https://sell.app/docs/api/promotions/create-promotion) · Effect: **consequential**

```python
def create(
        self,
        *,
        name: str,
        status: SdkCreatePromotionRequestApplicationJsonStatus | str,
        priority: int,
        is_stackable: bool,
        phases: builtins.list[CreatePromotionRequestApplicationJsonPropertyPhasesItem],
        starts_at: str | None | NotGiven = NOT_GIVEN,
        ends_at: str | None | NotGiven = NOT_GIVEN,
        max_redemptions: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreatePromotionResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| status | `SdkCreatePromotionRequestApplicationJsonStatus \| str` | Yes |
| priority | `int` | Yes |
| is_stackable | `bool` | Yes |
| phases | `builtins.list[CreatePromotionRequestApplicationJsonPropertyPhasesItem]` | Yes |
| starts_at | `str \| None \| NotGiven` | No |
| ends_at | `str \| None \| NotGiven` | No |
| max_redemptions | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreatePromotionResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions.create(
    name="Ship Week",
    status="active",
    starts_at="2026-08-01T00:00:00Z",
    ends_at="2026-08-08T00:00:00Z",
    priority=1,
    is_stackable=False,
    max_redemptions=500,
    phases=[
        {
            "discount_type": "percentage",
            "discount_value": "20",
            "ends_at": "2026-08-04T00:00:00Z",
            "max_redemptions": 200,
            "minimum_amount": "10"
        },
        {
            "discount_type": "fixed",
            "discount_value": "5",
            "ends_at": None,
            "max_redemptions": None,
            "minimum_amount": "25"
        }
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

## search

Search promotions

[API reference](https://sell.app/docs/api/promotions/search-promotions) · Effect: **read**

```python
def search(
        self,
        *,
        filters: builtins.list[
            SearchPromotionsRequestApplicationJsonPropertyFiltersItem
        ]
        | None = None,
        sort: builtins.list[SearchPromotionsRequestApplicationJsonPropertySortItem]
        | None = None,
        search: SearchPromotionsRequestApplicationJsonPropertySearch | None = None,
        includes: builtins.list[
            SearchPromotionsRequestApplicationJsonPropertyIncludesItem
        ]
        | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        pagination: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SdkSearchPromotionsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `builtins.list[
            SearchPromotionsRequestApplicationJsonPropertyFiltersItem
        ]
        \| None` | No |
| sort | `builtins.list[SearchPromotionsRequestApplicationJsonPropertySortItem]
        \| None` | No |
| search | `SearchPromotionsRequestApplicationJsonPropertySearch \| None` | No |
| includes | `builtins.list[
            SearchPromotionsRequestApplicationJsonPropertyIncludesItem
        ]
        \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| pagination | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SdkSearchPromotionsResponseValue200ApplicationJson]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions.search(
    filters=[{"field": "id", "operator": "=", "value": 1}],
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

Retrieve a promotion

[API reference](https://sell.app/docs/api/promotions/retrieve-promotion) · Effect: **read**

```python
def get(
        self,
        promotion: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetPromotionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetPromotionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions.get(promotion=1)
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

Update a promotion

[API reference](https://sell.app/docs/api/promotions/update-promotion) · Effect: **consequential**

```python
def replace(
        self,
        promotion: int,
        *,
        name: str | None = None,
        status: SdkReplacePromotionRequestApplicationJsonStatus | str | None = None,
        starts_at: str | None | NotGiven = NOT_GIVEN,
        ends_at: str | None | NotGiven = NOT_GIVEN,
        priority: int | None = None,
        is_stackable: bool | None = None,
        max_redemptions: int | None | NotGiven = NOT_GIVEN,
        phases: builtins.list[ReplacePromotionRequestApplicationJsonPropertyPhasesItem]
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkReplacePromotionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| name | `str \| None` | No |
| status | `SdkReplacePromotionRequestApplicationJsonStatus \| str \| None` | No |
| starts_at | `str \| None \| NotGiven` | No |
| ends_at | `str \| None \| NotGiven` | No |
| priority | `int \| None` | No |
| is_stackable | `bool \| None` | No |
| max_redemptions | `int \| None \| NotGiven` | No |
| phases | `builtins.list[ReplacePromotionRequestApplicationJsonPropertyPhasesItem]
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplacePromotionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions.replace(
    promotion=1,
    name="One More Sprint",
    is_stackable=True
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

Update a promotion

[API reference](https://sell.app/docs/api/promotions/update-promotion) · Effect: **consequential**

```python
def update(
        self,
        promotion: int,
        *,
        name: str | None = None,
        status: SdkUpdatePromotionRequestApplicationJsonStatus | str | None = None,
        starts_at: str | None | NotGiven = NOT_GIVEN,
        ends_at: str | None | NotGiven = NOT_GIVEN,
        priority: int | None = None,
        is_stackable: bool | None = None,
        max_redemptions: int | None | NotGiven = NOT_GIVEN,
        phases: builtins.list[UpdatePromotionRequestApplicationJsonPropertyPhasesItem]
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdatePromotionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| name | `str \| None` | No |
| status | `SdkUpdatePromotionRequestApplicationJsonStatus \| str \| None` | No |
| starts_at | `str \| None \| NotGiven` | No |
| ends_at | `str \| None \| NotGiven` | No |
| priority | `int \| None` | No |
| is_stackable | `bool \| None` | No |
| max_redemptions | `int \| None \| NotGiven` | No |
| phases | `builtins.list[UpdatePromotionRequestApplicationJsonPropertyPhasesItem]
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdatePromotionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions.update(
    promotion=1,
    name="One More Sprint",
    is_stackable=True
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

## delete

Delete a promotion

[API reference](https://sell.app/docs/api/promotions/delete-promotion) · Effect: **consequential**

```python
def delete(
        self,
        promotion: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `None`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions.delete(promotion=1)
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

## restore

Restore a promotion

[API reference](https://sell.app/docs/api/promotions/restore-promotion) · Effect: **consequential**

```python
def restore(
        self,
        promotion: int,
        *,
        name: str,
        status: SdkRestorePromotionRequestApplicationJsonStatus | str,
        priority: int,
        is_stackable: bool,
        phases: builtins.list[RestorePromotionRequestApplicationJsonPropertyPhasesItem],
        starts_at: str | None | NotGiven = NOT_GIVEN,
        ends_at: str | None | NotGiven = NOT_GIVEN,
        max_redemptions: int | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkRestorePromotionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| name | `str` | Yes |
| status | `SdkRestorePromotionRequestApplicationJsonStatus \| str` | Yes |
| priority | `int` | Yes |
| is_stackable | `bool` | Yes |
| phases | `builtins.list[RestorePromotionRequestApplicationJsonPropertyPhasesItem]` | Yes |
| starts_at | `str \| None \| NotGiven` | No |
| ends_at | `str \| None \| NotGiven` | No |
| max_redemptions | `int \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkRestorePromotionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.promotions.restore(
    promotion=1,
    name="Ship Week",
    status="active",
    starts_at="2026-08-01T00:00:00Z",
    ends_at="2026-08-08T00:00:00Z",
    priority=1,
    is_stackable=False,
    max_redemptions=500,
    phases=[
        {
            "discount_type": "percentage",
            "discount_value": "20",
            "ends_at": "2026-08-04T00:00:00Z",
            "max_redemptions": 200,
            "minimum_amount": "10"
        },
        {
            "discount_type": "fixed",
            "discount_value": "5",
            "ends_at": None,
            "max_redemptions": None,
            "minimum_amount": "25"
        }
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

Documented HTTP responses: 200, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

