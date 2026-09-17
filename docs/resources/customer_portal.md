# customer_portal

[All resources](../methods.md)

## get_customer_portal_profile

Retrieve the signed-in customer

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```python
def get_customer_portal_profile(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomerPortalProfileResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetCustomerPortalProfileResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.get_customer_portal_profile()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update_customer_portal_profile

Update the signed-in customer

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def update_customer_portal_profile(
        self,
        *,
        email: Optional[str] = None,
        name: Union[str, None, NotGiven] = NOT_GIVEN,
        locale: Union[str, None, NotGiven] = NOT_GIVEN,
        metadata: Optional[
            UpdateCustomerPortalProfileRequestApplicationJsonPropertyMetadata
        ] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCustomerPortalProfileResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| email | `Optional[str]` | No |
| name | `Union[str, None, NotGiven]` | No |
| locale | `Union[str, None, NotGiven]` | No |
| metadata | `Optional[
            UpdateCustomerPortalProfileRequestApplicationJsonPropertyMetadata
        ]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateCustomerPortalProfileResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.update_customer_portal_profile(locale="en-US")
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_customer_portal_orders

List customer orders

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```python
def list_customer_portal_orders(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[CustomerPortalOrder]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[CustomerPortalOrder]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.list_customer_portal_orders()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_customer_portal_order

Retrieve a customer order

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```python
def get_customer_portal_order(
        self,
        order: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomerPortalOrderResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetCustomerPortalOrderResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.get_customer_portal_order(order=9001)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_customer_portal_subscriptions

List customer subscriptions

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```python
def list_customer_portal_subscriptions(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListCustomerPortalSubscriptionsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListCustomerPortalSubscriptionsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.list_customer_portal_subscriptions()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_customer_portal_subscription

Retrieve a customer subscription

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```python
def get_customer_portal_subscription(
        self,
        subscription: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomerPortalSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| subscription | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetCustomerPortalSubscriptionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.get_customer_portal_subscription(subscription=991)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_customer_portal_subscription_capabilities

Retrieve subscription capabilities

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```python
def get_customer_portal_subscription_capabilities(
        self,
        subscription: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetCustomerPortalSubscriptionCapabilitiesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| subscription | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetCustomerPortalSubscriptionCapabilitiesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.get_customer_portal_subscription_capabilities(subscription=42)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## list_customer_portal_entitlements

List customer entitlements

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **read**

```python
def list_customer_portal_entitlements(
        self,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListCustomerPortalEntitlementsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListCustomerPortalEntitlementsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.list_customer_portal_entitlements()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## cancel_customer_subscription_at_period_end

Cancel at period end

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def cancel_customer_subscription_at_period_end(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCancelCustomerSubscriptionAtPeriodEndResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCancelCustomerSubscriptionAtPeriodEndResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.cancel_customer_subscription_at_period_end(
    product_subscription=42,
    reason="Customer requested this change",
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## cancel_customer_subscription_immediately

Cancel immediately

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def cancel_customer_subscription_immediately(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCancelCustomerSubscriptionImmediatelyResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCancelCustomerSubscriptionImmediatelyResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.cancel_customer_subscription_immediately(
    product_subscription=42,
    reason="Customer requested this change",
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## pause_customer_subscription

Pause a subscription

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def pause_customer_subscription(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkPauseCustomerSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkPauseCustomerSubscriptionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.pause_customer_subscription(
    product_subscription=42,
    reason="Customer requested this change",
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## resume_customer_subscription

Resume a subscription

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def resume_customer_subscription(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkResumeCustomerSubscriptionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkResumeCustomerSubscriptionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.resume_customer_subscription(
    product_subscription=42,
    reason="Customer requested this change",
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## update_customer_subscription_payment_method

Update payment method

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def update_customer_subscription_payment_method(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateCustomerSubscriptionPaymentMethodResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateCustomerSubscriptionPaymentMethodResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.update_customer_subscription_payment_method(
    product_subscription=42,
    reason="Customer requested this change",
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## preview_customer_subscription_plan_change

Preview a plan change

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def preview_customer_subscription_plan_change(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkPreviewCustomerSubscriptionPlanChangeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkPreviewCustomerSubscriptionPlanChangeResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.preview_customer_subscription_plan_change(
    product_subscription=42,
    product_variant_id=84,
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## confirm_customer_subscription_plan_change

Confirm a plan change

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def confirm_customer_subscription_plan_change(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkConfirmCustomerSubscriptionPlanChangeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkConfirmCustomerSubscriptionPlanChangeResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.confirm_customer_subscription_plan_change(
    product_subscription=42,
    preview_id="preview_01K4",
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## preview_customer_subscription_renewal_date_change

Preview a renewal-date change

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def preview_customer_subscription_renewal_date_change(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkPreviewCustomerSubscriptionRenewalDateChangeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkPreviewCustomerSubscriptionRenewalDateChangeResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.preview_customer_subscription_renewal_date_change(
    product_subscription=42,
    renewal_date="2026-10-15",
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## confirm_customer_subscription_renewal_date_change

Confirm a renewal-date change

[API reference](https://sell.app/docs/api/customer-portal) · Effect: **consequential**

```python
def confirm_customer_subscription_renewal_date_change(
        self,
        product_subscription: int,
        *,
        preview_id: Optional[str] = None,
        product_variant_id: Optional[int] = None,
        renewal_date: Optional[str] = None,
        return_url: Optional[str] = None,
        reason: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkConfirmCustomerSubscriptionRenewalDateChangeResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| product_subscription | `int` | Yes |
| preview_id | `Optional[str]` | No |
| product_variant_id | `Optional[int]` | No |
| renewal_date | `Optional[str]` | No |
| return_url | `Optional[str]` | No |
| reason | `Optional[str]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkConfirmCustomerSubscriptionRenewalDateChangeResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], customer_session=os.environ["SELLAPP_CUSTOMER_SESSION"], store="")

result = client.customer_portal.confirm_customer_subscription_renewal_date_change(
    product_subscription=42,
    preview_id="preview_01K4",
    idempotency_key="example-mutation-001"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "customerSession": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

