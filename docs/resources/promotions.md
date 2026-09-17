# promotions

[All resources](../methods.md)

## list

List promotions

[API reference](https://sell.app/docs/api/promotions/list-promotions) · Effect: **read**

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
    ) -> SyncPage[SdkListPromotionsResponseValue200ApplicationJson]:
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
        status: Union[SdkCreatePromotionRequestApplicationJsonStatus, str],
        priority: int,
        is_stackable: bool,
        phases: List[CreatePromotionRequestApplicationJsonPropertyPhasesItem],
        starts_at: Union[str, None, NotGiven] = NOT_GIVEN,
        ends_at: Union[str, None, NotGiven] = NOT_GIVEN,
        max_redemptions: Union[int, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreatePromotionResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| status | `Union[SdkCreatePromotionRequestApplicationJsonStatus, str]` | Yes |
| priority | `int` | Yes |
| is_stackable | `bool` | Yes |
| phases | `List[CreatePromotionRequestApplicationJsonPropertyPhasesItem]` | Yes |
| starts_at | `Union[str, None, NotGiven]` | No |
| ends_at | `Union[str, None, NotGiven]` | No |
| max_redemptions | `Union[int, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        filters: Optional[
            List[SearchPromotionsRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[
            List[SearchPromotionsRequestApplicationJsonPropertySortItem]
        ] = None,
        search: Optional[SearchPromotionsRequestApplicationJsonPropertySearch] = None,
        includes: Optional[
            List[SearchPromotionsRequestApplicationJsonPropertyIncludesItem]
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        pagination: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SdkSearchPromotionsResponseValue200ApplicationJson]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchPromotionsRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[
            List[SearchPromotionsRequestApplicationJsonPropertySortItem]
        ]` | No |
| search | `Optional[SearchPromotionsRequestApplicationJsonPropertySearch]` | No |
| includes | `Optional[
            List[SearchPromotionsRequestApplicationJsonPropertyIncludesItem]
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| pagination | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetPromotionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Optional[str] = None,
        status: Optional[
            Union[SdkReplacePromotionRequestApplicationJsonStatus, str]
        ] = None,
        starts_at: Union[str, None, NotGiven] = NOT_GIVEN,
        ends_at: Union[str, None, NotGiven] = NOT_GIVEN,
        priority: Optional[int] = None,
        is_stackable: Optional[bool] = None,
        max_redemptions: Union[int, None, NotGiven] = NOT_GIVEN,
        phases: Optional[
            List[ReplacePromotionRequestApplicationJsonPropertyPhasesItem]
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkReplacePromotionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| name | `Optional[str]` | No |
| status | `Optional[
            Union[SdkReplacePromotionRequestApplicationJsonStatus, str]
        ]` | No |
| starts_at | `Union[str, None, NotGiven]` | No |
| ends_at | `Union[str, None, NotGiven]` | No |
| priority | `Optional[int]` | No |
| is_stackable | `Optional[bool]` | No |
| max_redemptions | `Union[int, None, NotGiven]` | No |
| phases | `Optional[
            List[ReplacePromotionRequestApplicationJsonPropertyPhasesItem]
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        name: Optional[str] = None,
        status: Optional[
            Union[SdkUpdatePromotionRequestApplicationJsonStatus, str]
        ] = None,
        starts_at: Union[str, None, NotGiven] = NOT_GIVEN,
        ends_at: Union[str, None, NotGiven] = NOT_GIVEN,
        priority: Optional[int] = None,
        is_stackable: Optional[bool] = None,
        max_redemptions: Union[int, None, NotGiven] = NOT_GIVEN,
        phases: Optional[
            List[UpdatePromotionRequestApplicationJsonPropertyPhasesItem]
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdatePromotionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| name | `Optional[str]` | No |
| status | `Optional[
            Union[SdkUpdatePromotionRequestApplicationJsonStatus, str]
        ]` | No |
| starts_at | `Union[str, None, NotGiven]` | No |
| ends_at | `Union[str, None, NotGiven]` | No |
| priority | `Optional[int]` | No |
| is_stackable | `Optional[bool]` | No |
| max_redemptions | `Union[int, None, NotGiven]` | No |
| phases | `Optional[
            List[UpdatePromotionRequestApplicationJsonPropertyPhasesItem]
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> None:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        status: Union[SdkRestorePromotionRequestApplicationJsonStatus, str],
        priority: int,
        is_stackable: bool,
        phases: List[RestorePromotionRequestApplicationJsonPropertyPhasesItem],
        starts_at: Union[str, None, NotGiven] = NOT_GIVEN,
        ends_at: Union[str, None, NotGiven] = NOT_GIVEN,
        max_redemptions: Union[int, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkRestorePromotionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| promotion | `int` | Yes |
| name | `str` | Yes |
| status | `Union[SdkRestorePromotionRequestApplicationJsonStatus, str]` | Yes |
| priority | `int` | Yes |
| is_stackable | `bool` | Yes |
| phases | `List[RestorePromotionRequestApplicationJsonPropertyPhasesItem]` | Yes |
| starts_at | `Union[str, None, NotGiven]` | No |
| ends_at | `Union[str, None, NotGiven]` | No |
| max_redemptions | `Union[int, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

