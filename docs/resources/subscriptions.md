# subscriptions

[All resources](../methods.md)

## cancel

Cancel a subscription

[API reference](https://sell.app/docs/api/subscriptions/cancel-a-subscription-immediately-with-a-refund) · Effect: **consequential**

```python
def cancel(
        self,
        subscription: int,
        *,
        cancel_at_period_end: bool,
        refund_last_payment: Optional[bool] = None,
        pro_rated_refund: Optional[bool] = None,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCancelSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| subscription | `int` | Yes |
| cancel_at_period_end | `bool` | Yes |
| refund_last_payment | `Optional[bool]` | No |
| pro_rated_refund | `Optional[bool]` | No |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCancelSubscriptionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.cancel(
    subscription=55,
    cancel_at_period_end=True,
    idempotency_key="design-kit-subscription-55-cancel-v1"
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

## get_capabilities

View subscription capabilities

[API reference](https://sell.app/docs/api/subscriptions/view-subscription-capabilities) · Effect: **read**

```python
def get_capabilities(
        self,
        product_subscription: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetSubscriptionCapabilitiesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetSubscriptionCapabilitiesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.get_capabilities(product_subscription=1)
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

## cancel_at_period_end

Cancel a subscription at period end

[API reference](https://sell.app/docs/api/subscriptions/cancel-at-period-end) · Effect: **consequential**

```python
def cancel_at_period_end(
        self,
        product_subscription: int,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        reason: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCancelSubscriptionAtPeriodEndResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| reason | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCancelSubscriptionAtPeriodEndResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.cancel_at_period_end(
    product_subscription=55,
    reason="Customer request"
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

## cancel_immediately

Cancel a subscription immediately

[API reference](https://sell.app/docs/api/subscriptions/cancel-immediately) · Effect: **consequential**

```python
def cancel_immediately(
        self,
        product_subscription: int,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        reason: Union[str, None, NotGiven] = NOT_GIVEN,
        refund_last_payment: Optional[bool] = None,
        pro_rated_refund: Optional[bool] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCancelSubscriptionImmediatelyResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| reason | `Union[str, None, NotGiven]` | No |
| refund_last_payment | `Optional[bool]` | No |
| pro_rated_refund | `Optional[bool]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCancelSubscriptionImmediatelyResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.cancel_immediately(
    product_subscription=55,
    reason="Customer request"
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

## pause

Pause a subscription

[API reference](https://sell.app/docs/api/subscriptions/pause-a-subscription) · Effect: **consequential**

```python
def pause(
        self,
        product_subscription: int,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        resume_at: Union[str, None, NotGiven] = NOT_GIVEN,
        reason: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkPauseSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| resume_at | `Union[str, None, NotGiven]` | No |
| reason | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkPauseSubscriptionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.pause(
    product_subscription=55,
    resume_at="2026-10-10T12:00:00Z",
    reason="Customer request"
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

## resume

Resume a subscription

[API reference](https://sell.app/docs/api/subscriptions/resume-a-subscription) · Effect: **consequential**

```python
def resume(
        self,
        product_subscription: int,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkResumeSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkResumeSubscriptionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.resume(product_subscription=55)
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

## update_payment_method

Update a subscription payment method

[API reference](https://sell.app/docs/api/subscriptions/update-payment-method) · Effect: **consequential**

```python
def update_payment_method(
        self,
        product_subscription: int,
        *,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `Any`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.update_payment_method(product_subscription=1)
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

Documented HTTP responses: 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## preview_plan_change

Preview a subscription plan change

[API reference](https://sell.app/docs/api/subscriptions/preview-plan-change) · Effect: **consequential**

```python
def preview_plan_change(
        self,
        product_subscription: int,
        *,
        target_variant_id: int,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        effective_timing: Optional[
            Union[
                SdkPreviewSubscriptionPlanChangeRequestApplicationJsonEffectiveTiming,
                str,
            ]
        ] = None,
        proration_behavior: Optional[
            Union[
                SdkPreviewSubscriptionPlanChangeRequestApplicationJsonProrationBehavior,
                str,
            ]
        ] = None,
        metadata: Optional[
            PreviewSubscriptionPlanChangeRequestApplicationJsonPropertyMetadata
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| target_variant_id | `int` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| effective_timing | `Optional[
            Union[
                SdkPreviewSubscriptionPlanChangeRequestApplicationJsonEffectiveTiming,
                str,
            ]
        ]` | No |
| proration_behavior | `Optional[
            Union[
                SdkPreviewSubscriptionPlanChangeRequestApplicationJsonProrationBehavior,
                str,
            ]
        ]` | No |
| metadata | `Optional[
            PreviewSubscriptionPlanChangeRequestApplicationJsonPropertyMetadata
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `Any`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.preview_plan_change(
    product_subscription=1,
    target_variant_id=4321,
    effective_timing="immediate",
    proration_behavior="provider_default"
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

Documented HTTP responses: 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## confirm_plan_change

Confirm a subscription plan change

[API reference](https://sell.app/docs/api/subscriptions/confirm-plan-change) · Effect: **consequential**

```python
def confirm_plan_change(
        self,
        product_subscription: int,
        *,
        target_variant_id: int,
        preview_token: str,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        effective_timing: Optional[
            Union[
                SdkConfirmSubscriptionPlanChangeRequestApplicationJsonEffectiveTiming,
                str,
            ]
        ] = None,
        proration_behavior: Optional[
            Union[
                SdkConfirmSubscriptionPlanChangeRequestApplicationJsonProrationBehavior,
                str,
            ]
        ] = None,
        metadata: Optional[
            ConfirmSubscriptionPlanChangeRequestApplicationJsonPropertyMetadata
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| target_variant_id | `int` | Yes |
| preview_token | `str` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| effective_timing | `Optional[
            Union[
                SdkConfirmSubscriptionPlanChangeRequestApplicationJsonEffectiveTiming,
                str,
            ]
        ]` | No |
| proration_behavior | `Optional[
            Union[
                SdkConfirmSubscriptionPlanChangeRequestApplicationJsonProrationBehavior,
                str,
            ]
        ]` | No |
| metadata | `Optional[
            ConfirmSubscriptionPlanChangeRequestApplicationJsonPropertyMetadata
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `Any`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.confirm_plan_change(
    product_subscription=1,
    target_variant_id=4321,
    preview_token="subprev_9c4b2f"
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

Documented HTTP responses: 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## preview_renewal_date

Preview a subscription renewal date change

[API reference](https://sell.app/docs/api/subscriptions/preview-renewal-date-change) · Effect: **consequential**

```python
def preview_renewal_date(
        self,
        product_subscription: int,
        *,
        renewal_date: str,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        reason: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Optional[
            PreviewSubscriptionRenewalDateChangeRequestApplicationJsonPropertyMetadata
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkPreviewSubscriptionRenewalDateChangeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| renewal_date | `str` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| reason | `Union[str, None, NotGiven]` | No |
| metadata | `Optional[
            PreviewSubscriptionRenewalDateChangeRequestApplicationJsonPropertyMetadata
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkPreviewSubscriptionRenewalDateChangeResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.preview_renewal_date(
    product_subscription=1,
    renewal_date="2026-10-01T12:00:00Z",
    reason="Align Maya's membership with the monthly reading circle."
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

## confirm_renewal_date

Confirm a subscription renewal date change

[API reference](https://sell.app/docs/api/subscriptions/confirm-renewal-date-change) · Effect: **consequential**

```python
def confirm_renewal_date(
        self,
        product_subscription: int,
        *,
        renewal_date: str,
        idempotency_key: Union[str, None, NotGiven] = NOT_GIVEN,
        preview_token: Union[str, None, NotGiven] = NOT_GIVEN,
        reason: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Optional[
            ConfirmSubscriptionRenewalDateChangeRequestApplicationJsonPropertyMetadata
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkConfirmSubscriptionRenewalDateChangeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| renewal_date | `str` | Yes |
| idempotency_key | `Union[str, None, NotGiven]` | No |
| preview_token | `Union[str, None, NotGiven]` | No |
| reason | `Union[str, None, NotGiven]` | No |
| metadata | `Optional[
            ConfirmSubscriptionRenewalDateChangeRequestApplicationJsonPropertyMetadata
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkConfirmSubscriptionRenewalDateChangeResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.confirm_renewal_date(
    product_subscription=1,
    renewal_date="2026-10-01T12:00:00Z",
    preview_token="subprev_project_library_55",
    reason="Align Maya's membership with the monthly reading circle."
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

## list_subscriptions

List subscriptions

[API reference](https://sell.app/docs/api/subscriptions/read-subscriptions) · Effect: **read**

```python
def list_subscriptions(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListSubscriptionsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListSubscriptionsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.list_subscriptions()
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search_subscriptions

Search subscriptions

[API reference](https://sell.app/docs/api/subscriptions/read-subscriptions) · Effect: **read**

```python
def search_subscriptions(
        self,
        *,
        search: Optional[str] = None,
        status: Optional[str] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchSubscriptionsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| search | `Optional[str]` | No |
| status | `Optional[str]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SearchSubscriptionsResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.search_subscriptions(
    search="maya.chen@example.com",
    status="active"
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_subscription

Retrieve a subscription

[API reference](https://sell.app/docs/api/subscriptions/read-subscriptions) · Effect: **read**

```python
def get_subscription(
        self,
        product_subscription: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetSubscriptionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.subscriptions.get_subscription(product_subscription=991)
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

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

