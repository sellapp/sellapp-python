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
        refund_last_payment: bool | None = None,
        pro_rated_refund: bool | None = None,
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCancelSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| subscription | `int` | Yes |
| cancel_at_period_end | `bool` | Yes |
| refund_last_payment | `bool \| None` | No |
| pro_rated_refund | `bool \| None` | No |
| idempotency_key | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> SdkGetSubscriptionCapabilitiesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        reason: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCancelSubscriptionAtPeriodEndResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| reason | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        reason: str | None | NotGiven = NOT_GIVEN,
        refund_last_payment: bool | None = None,
        pro_rated_refund: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCancelSubscriptionImmediatelyResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| reason | `str \| None \| NotGiven` | No |
| refund_last_payment | `bool \| None` | No |
| pro_rated_refund | `bool \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        resume_at: str | None | NotGiven = NOT_GIVEN,
        reason: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkPauseSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| resume_at | `str \| None \| NotGiven` | No |
| reason | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkResumeSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        effective_timing: SdkPreviewSubscriptionPlanChangeRequestApplicationJsonEffectiveTiming
        | str
        | None = None,
        proration_behavior: SdkPreviewSubscriptionPlanChangeRequestApplicationJsonProrationBehavior
        | str
        | None = None,
        metadata: PreviewSubscriptionPlanChangeRequestApplicationJsonPropertyMetadata
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| target_variant_id | `int` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| effective_timing | `SdkPreviewSubscriptionPlanChangeRequestApplicationJsonEffectiveTiming
        \| str
        \| None` | No |
| proration_behavior | `SdkPreviewSubscriptionPlanChangeRequestApplicationJsonProrationBehavior
        \| str
        \| None` | No |
| metadata | `PreviewSubscriptionPlanChangeRequestApplicationJsonPropertyMetadata
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        effective_timing: SdkConfirmSubscriptionPlanChangeRequestApplicationJsonEffectiveTiming
        | str
        | None = None,
        proration_behavior: SdkConfirmSubscriptionPlanChangeRequestApplicationJsonProrationBehavior
        | str
        | None = None,
        metadata: ConfirmSubscriptionPlanChangeRequestApplicationJsonPropertyMetadata
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| target_variant_id | `int` | Yes |
| preview_token | `str` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| effective_timing | `SdkConfirmSubscriptionPlanChangeRequestApplicationJsonEffectiveTiming
        \| str
        \| None` | No |
| proration_behavior | `SdkConfirmSubscriptionPlanChangeRequestApplicationJsonProrationBehavior
        \| str
        \| None` | No |
| metadata | `ConfirmSubscriptionPlanChangeRequestApplicationJsonPropertyMetadata
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        reason: str | None | NotGiven = NOT_GIVEN,
        metadata: PreviewSubscriptionRenewalDateChangeRequestApplicationJsonPropertyMetadata
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkPreviewSubscriptionRenewalDateChangeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| renewal_date | `str` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| reason | `str \| None \| NotGiven` | No |
| metadata | `PreviewSubscriptionRenewalDateChangeRequestApplicationJsonPropertyMetadata
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        idempotency_key: str | None | NotGiven = NOT_GIVEN,
        preview_token: str | None | NotGiven = NOT_GIVEN,
        reason: str | None | NotGiven = NOT_GIVEN,
        metadata: ConfirmSubscriptionRenewalDateChangeRequestApplicationJsonPropertyMetadata
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkConfirmSubscriptionRenewalDateChangeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| renewal_date | `str` | Yes |
| idempotency_key | `str \| None \| NotGiven` | No |
| preview_token | `str \| None \| NotGiven` | No |
| reason | `str \| None \| NotGiven` | No |
| metadata | `ConfirmSubscriptionRenewalDateChangeRequestApplicationJsonPropertyMetadata
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListSubscriptionsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        search: str | None = None,
        status: str | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchSubscriptionsResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| search | `str \| None` | No |
| status | `str \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

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
        request_options: RequestOptions | None = None,
    ) -> SdkGetSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

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

