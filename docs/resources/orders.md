# orders

[All resources](../methods.md)

## list

List orders

[API reference](https://sell.app/docs/api/orders/list-orders) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListOrdersResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[ListOrdersResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.list()
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

Create an order

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def create(
        self,
        *,
        customer_email: str,
        payment_method: Union[SdkCreateOrderRequestApplicationJsonPaymentMethod, str],
        product_variants: CreateOrderRequestApplicationJsonPropertyProductVariants,
        customer_ip: Union[str, None, NotGiven] = NOT_GIVEN,
        coupon: Optional[str] = None,
        vat_id: Optional[str] = None,
        country: Optional[str] = None,
        affiliate: Union[str, None, NotGiven] = NOT_GIVEN,
        extra: Optional[CreateOrderRequestApplicationJsonPropertyExtra] = None,
        custom_payment_method_id: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateOrderResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer_email | `str` | Yes |
| payment_method | `Union[SdkCreateOrderRequestApplicationJsonPaymentMethod, str]` | Yes |
| product_variants | `CreateOrderRequestApplicationJsonPropertyProductVariants` | Yes |
| customer_ip | `Union[str, None, NotGiven]` | No |
| coupon | `Optional[str]` | No |
| vat_id | `Optional[str]` | No |
| country | `Optional[str]` | No |
| affiliate | `Union[str, None, NotGiven]` | No |
| extra | `Optional[CreateOrderRequestApplicationJsonPropertyExtra]` | No |
| custom_payment_method_id | `Union[str, None, NotGiven]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateOrderResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.create(
    customer_email="maya@example.com",
    payment_method="STRIPE",
    product_variants={"4321": {"quantity": 1}},
    idempotency_key="example-mutation-001"
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

Documented HTTP responses: 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## search

Search orders

[API reference](https://sell.app/docs/api/orders/search-orders) · Effect: **read**

```python
def search(
        self,
        *,
        filters: Optional[
            List[SearchOrdersRequestApplicationJsonPropertyFiltersItem]
        ] = None,
        sort: Optional[List[SearchOrdersRequestApplicationJsonPropertySortItem]] = None,
        pagination: Optional[
            SearchOrdersRequestApplicationJsonPropertyPagination
        ] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchOrdersResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| filters | `Optional[
            List[SearchOrdersRequestApplicationJsonPropertyFiltersItem]
        ]` | No |
| sort | `Optional[List[SearchOrdersRequestApplicationJsonPropertySortItem]]` | No |
| pagination | `Optional[
            SearchOrdersRequestApplicationJsonPropertyPagination
        ]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SyncPage[SearchOrdersResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.search(
    filters=[
        {"field": "transaction_id", "operator": "contains", "value": "pi_3Example"},
        {"field": "status", "operator": "in", "value": ["COMPLETED"]}
    ],
    sort=[{"field": "created_at", "direction": "desc"}],
    pagination={"page": 1, "limit": 25}
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

Retrieve an order

[API reference](https://sell.app/docs/api/orders/retrieve-an-order) · Effect: **read**

```python
def get(
        self,
        order: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetOrderResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkGetOrderResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.get(order=1042)
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

## update_status

Update order status

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def update_status(
        self,
        order: int,
        *,
        status: Union[SdkUpdateOrderStatusRequestApplicationJsonStatus, str],
        expected_status: Union[Union[ExpectedStatus, str], None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateOrderStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| status | `Union[SdkUpdateOrderStatusRequestApplicationJsonStatus, str]` | Yes |
| expected_status | `Union[Union[ExpectedStatus, str], None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkUpdateOrderStatusResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.update_status(
    order=9001,
    status="COMPLETED",
    expected_status="PAID",
    request_options={"headers": {"Idempotency-Key": "example-mutation-001"}}
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

## create_checkout

Create order checkout

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def create_checkout(
        self,
        order: int,
        *,
        expected_status: Union[Union[ExpectedStatus, str], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateOrderCheckoutResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| expected_status | `Union[Union[ExpectedStatus, str], None, NotGiven]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateOrderCheckoutResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.create_checkout(
    order=9001,
    idempotency_key="example-mutation-001"
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## create_replacement

Issue replacements

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def create_replacement(
        self,
        order: int,
        *,
        product_variants: CreateOrderReplacementRequestApplicationJsonPropertyProductVariants,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateOrderReplacementResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| product_variants | `CreateOrderReplacementRequestApplicationJsonPropertyProductVariants` | Yes |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateOrderReplacementResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.create_replacement(
    order=9001,
    product_variants=[4321],
    idempotency_key="example-mutation-001"
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

## create_refund

Refund an order

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def create_refund(
        self,
        order: int,
        *,
        amount: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateOrderRefundResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| amount | `Union[str, None, NotGiven]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateOrderRefundResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.create_refund(
    order=9001,
    amount="5.00",
    idempotency_key="example-mutation-001"
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

## retry_fulfillment

Retry fulfillment

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def retry_fulfillment(
        self,
        order: int,
        *,
        email: Union[str, None, NotGiven] = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkRetryOrderFulfillmentResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| email | `Union[str, None, NotGiven]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkRetryOrderFulfillmentResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.retry_fulfillment(
    order=9001,
    email="maya@example.com",
    idempotency_key="example-mutation-001"
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

## retry_dynamic_delivery

Retry dynamic delivery

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def retry_dynamic_delivery(
        self,
        order: int,
        *,
        delivered_product_id: int,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkRetryOrderDynamicDeliveryResponseValue202ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| delivered_product_id | `int` | Yes |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkRetryOrderDynamicDeliveryResponseValue202ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.retry_dynamic_delivery(
    order=9001,
    delivered_product_id=81,
    idempotency_key="example-mutation-001"
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

Documented HTTP responses: 202, 400, 401, 403, 404, 409, 410, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## send_fulfillment_notifications

Send fulfillment notifications

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def send_fulfillment_notifications(
        self,
        order: int,
        *,
        email: Union[str, None, NotGiven] = NOT_GIVEN,
        product_variant_ids: Union[List[int], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkSendOrderFulfillmentNotificationsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| email | `Union[str, None, NotGiven]` | No |
| product_variant_ids | `Union[List[int], None, NotGiven]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkSendOrderFulfillmentNotificationsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.send_fulfillment_notifications(
    order=9001,
    email="maya@example.com",
    product_variant_ids=[4321],
    idempotency_key="example-mutation-001"
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

## list_deliverables

List order deliverables

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **read**

```python
def list_deliverables(
        self,
        order: int,
        *,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkListOrderDeliverablesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkListOrderDeliverablesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.list_deliverables(order=9001)
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

## create_from_wallet

Create and pay an order from a wallet

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def create_from_wallet(
        self,
        *,
        customer_email: str,
        product_variants: CreateWalletOrderRequestApplicationJsonPropertyProductVariants,
        customer_ip: Union[str, None, NotGiven] = NOT_GIVEN,
        coupon: Optional[str] = None,
        vat_id: Optional[str] = None,
        country: Optional[str] = None,
        affiliate: Union[str, None, NotGiven] = NOT_GIVEN,
        extra: Optional[CreateWalletOrderRequestApplicationJsonPropertyExtra] = None,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateWalletOrderResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer_email | `str` | Yes |
| product_variants | `CreateWalletOrderRequestApplicationJsonPropertyProductVariants` | Yes |
| customer_ip | `Union[str, None, NotGiven]` | No |
| coupon | `Optional[str]` | No |
| vat_id | `Optional[str]` | No |
| country | `Optional[str]` | No |
| affiliate | `Union[str, None, NotGiven]` | No |
| extra | `Optional[CreateWalletOrderRequestApplicationJsonPropertyExtra]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkCreateWalletOrderResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.create_from_wallet(
    customer_email="maya.chen@example.com",
    country="US",
    product_variants={"4321": {"quantity": 1}},
    idempotency_key="example-mutation-001"
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

## pay_from_wallet

Pay an existing order from its customer wallet

[API reference](https://sell.app/docs/api/orders/create-and-operate) · Effect: **consequential**

```python
def pay_from_wallet(
        self,
        order: int,
        *,
        expected_status: Union[Union[ExpectedStatus, str], None, NotGiven] = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkPayOrderFromWalletResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| order | `int` | Yes |
| expected_status | `Union[Union[ExpectedStatus, str], None, NotGiven]` | No |
| idempotency_key | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

Returns: `SdkPayOrderFromWalletResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.orders.pay_from_wallet(
    order=42,
    expected_status="PENDING",
    idempotency_key="example-mutation-001"
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

