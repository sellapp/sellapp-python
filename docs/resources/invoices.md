# invoices

[All resources](../methods.md)

## list

List all invoices

[API reference](https://sell.app/docs/api/invoices/list-all-invoices) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        search: str | None = None,
        search_by: InvoicesSearchBy | str | None = None,
        id: str | None = None,
        email: str | None = None,
        transaction_id: str | None = None,
        serial_code: str | None = None,
        additional_info: str | None = None,
        product_name: str | None = None,
        discord_data: str | None = None,
        crypto_txid: str | None = None,
        crypto_address: str | None = None,
        coupon_code: str | None = None,
        status: builtins.list[InvoicesStatus | str] | None = None,
        payment_methods: builtins.list[InvoicesPaymentMethods | str] | None = None,
        sort: InvoicesSort | str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[ListInvoicesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| search | `str \| None` | No |
| search_by | `InvoicesSearchBy \| str \| None` | No |
| id | `str \| None` | No |
| email | `str \| None` | No |
| transaction_id | `str \| None` | No |
| serial_code | `str \| None` | No |
| additional_info | `str \| None` | No |
| product_name | `str \| None` | No |
| discord_data | `str \| None` | No |
| crypto_txid | `str \| None` | No |
| crypto_address | `str \| None` | No |
| coupon_code | `str \| None` | No |
| status | `builtins.list[InvoicesStatus \| str] \| None` | No |
| payment_methods | `builtins.list[InvoicesPaymentMethods \| str] \| None` | No |
| sort | `InvoicesSort \| str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[ListInvoicesResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.list()
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

Create an invoice

[API reference](https://sell.app/docs/api/invoices/create-an-invoice) · Effect: **consequential**

```python
def create(
        self,
        *,
        customer_email: str,
        payment_method: SdkCreateInvoiceRequestApplicationJsonPaymentMethod | str,
        product_variants: CreateInvoiceRequestApplicationJsonPropertyProductVariants,
        customer_ip: str | None | NotGiven = NOT_GIVEN,
        coupon: str | None = None,
        vat_id: str | None = None,
        country: str | None = None,
        affiliate: str | None | NotGiven = NOT_GIVEN,
        extra: CreateInvoiceRequestApplicationJsonPropertyExtra | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateInvoiceResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer_email | `str` | Yes |
| payment_method | `SdkCreateInvoiceRequestApplicationJsonPaymentMethod \| str` | Yes |
| product_variants | `CreateInvoiceRequestApplicationJsonPropertyProductVariants` | Yes |
| customer_ip | `str \| None \| NotGiven` | No |
| coupon | `str \| None` | No |
| vat_id | `str \| None` | No |
| country | `str \| None` | No |
| affiliate | `str \| None \| NotGiven` | No |
| extra | `CreateInvoiceRequestApplicationJsonPropertyExtra \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateInvoiceResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.create(
    customer_email="maya.chen@example.com",
    payment_method="STRIPE",
    product_variants={"4321": {"quantity": 1}}
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

Search invoices

[API reference](https://sell.app/docs/api/invoices/search-invoices) · Effect: **read**

```python
def search(
        self,
        *,
        search: str | None = None,
        search_by: SdkSearchInvoicesRequestApplicationJsonSearchBy | str | None = None,
        id: str | None = None,
        email: str | None = None,
        transaction_id: str | None = None,
        serial_code: str | None = None,
        additional_info: str | None = None,
        product_name: str | None = None,
        discord_data: str | None = None,
        crypto_txid: str | None = None,
        crypto_address: str | None = None,
        coupon_code: str | None = None,
        status: builtins.list[SdkSearchInvoicesRequestApplicationJsonStatus | str]
        | None = None,
        payment_methods: builtins.list[
            SdkSearchInvoicesRequestApplicationJsonPaymentMethods | str
        ]
        | None = None,
        sort: SdkSearchInvoicesRequestApplicationJsonSort | str | None = None,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[SearchInvoicesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| search | `str \| None` | No |
| search_by | `SdkSearchInvoicesRequestApplicationJsonSearchBy \| str \| None` | No |
| id | `str \| None` | No |
| email | `str \| None` | No |
| transaction_id | `str \| None` | No |
| serial_code | `str \| None` | No |
| additional_info | `str \| None` | No |
| product_name | `str \| None` | No |
| discord_data | `str \| None` | No |
| crypto_txid | `str \| None` | No |
| crypto_address | `str \| None` | No |
| coupon_code | `str \| None` | No |
| status | `builtins.list[SdkSearchInvoicesRequestApplicationJsonStatus \| str]
        \| None` | No |
| payment_methods | `builtins.list[
            SdkSearchInvoicesRequestApplicationJsonPaymentMethods \| str
        ]
        \| None` | No |
| sort | `SdkSearchInvoicesRequestApplicationJsonSort \| str \| None` | No |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[SearchInvoicesResponseValue200ApplicationJsonPropertyDataItem]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.search(
    id="1",
    sort="-created_at"
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

Retrieve an invoice

[API reference](https://sell.app/docs/api/invoices/retrieve-an-invoice) · Effect: **read**

```python
def get(
        self,
        invoice: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetInvoiceResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetInvoiceResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.get(invoice=1)
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

## go_to_checkout

Create a checkout session

[API reference](https://sell.app/docs/api/invoices/create-a-checkout-session) · Effect: **consequential**

```python
def go_to_checkout(
        self,
        invoice: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateCheckoutSessionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateCheckoutSessionResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.go_to_checkout(invoice=9001)
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

Documented HTTP responses: 200, 201, 400, 401, 403, 404, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_deliverables

View invoice deliverables

[API reference](https://sell.app/docs/api/invoices/view-invoice-deliverables) · Effect: **read**

```python
def get_deliverables(
        self,
        invoice: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetInvoiceDeliverablesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetInvoiceDeliverablesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.get_deliverables(invoice=1234)
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

## mark_completed

Mark pending invoice completed

[API reference](https://sell.app/docs/api/invoices/mark-pending-invoice-completed) · Effect: **consequential**

```python
def mark_completed(
        self,
        invoice: int,
        *,
        expected_status: ExpectedStatus | str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkMarkPendingInvoiceCompletedResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| expected_status | `ExpectedStatus \| str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkMarkPendingInvoiceCompletedResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.mark_completed(
    invoice=1,
    expected_status="PENDING"
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

## mark_voided

Mark pending invoice voided

[API reference](https://sell.app/docs/api/invoices/mark-pending-invoice-voided) · Effect: **consequential**

```python
def mark_voided(
        self,
        invoice: int,
        *,
        expected_status: ExpectedStatus | str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkMarkPendingInvoiceVoidedResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| expected_status | `ExpectedStatus \| str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkMarkPendingInvoiceVoidedResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.mark_voided(
    invoice=1,
    expected_status="PENDING"
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

## issue_replacement

Issue replacement for completed invoice

[API reference](https://sell.app/docs/api/invoices/issue-replacement-for-completed-invoice) · Effect: **consequential**

```python
def issue_replacement(
        self,
        invoice: int,
        *,
        product_variants: IssueReplacementForCompletedInvoiceRequestApplicationJsonPropertyProductVariants,
        request_options: RequestOptions | None = None,
    ) -> SdkIssueReplacementForCompletedInvoiceResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| product_variants | `IssueReplacementForCompletedInvoiceRequestApplicationJsonPropertyProductVariants` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkIssueReplacementForCompletedInvoiceResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.issue_replacement(
    invoice=1,
    product_variants=[117214]
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

## update_status

Update invoice status

[API reference](https://sell.app/docs/api/invoices/update-invoice-status) · Effect: **consequential**

```python
def update_status(
        self,
        invoice: int,
        *,
        status: SdkUpdateInvoiceStatusRequestApplicationJsonStatus | str,
        expected_status: ExpectedStatus | str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateInvoiceStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| status | `SdkUpdateInvoiceStatusRequestApplicationJsonStatus \| str` | Yes |
| expected_status | `ExpectedStatus \| str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateInvoiceStatusResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.update_status(
    invoice=1,
    status="REVIEW",
    expected_status="PENDING"
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

## create_refund

Create invoice refund

[API reference](https://sell.app/docs/api/invoices/refund-an-invoice) · Effect: **consequential**

```python
def create_refund(
        self,
        invoice: int,
        *,
        amount: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateInvoiceRefundResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| amount | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateInvoiceRefundResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.create_refund(
    invoice=1,
    amount="12.50"
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

## retry_fulfillment

Create fulfillment retry

[API reference](https://sell.app/docs/api/invoices/retry-invoice-fulfillment) · Effect: **consequential**

```python
def retry_fulfillment(
        self,
        invoice: int,
        *,
        email: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateFulfillmentRetryResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| email | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateFulfillmentRetryResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.retry_fulfillment(invoice=1)
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

## retry_dynamic_delivery

Create dynamic delivery retry

[API reference](https://sell.app/docs/api/invoices/retry-dynamic-delivery) · Effect: **consequential**

```python
def retry_dynamic_delivery(
        self,
        invoice: int,
        *,
        delivered_product_id: int,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateDynamicDeliveryRetryResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| delivered_product_id | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateDynamicDeliveryRetryResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.retry_dynamic_delivery(
    invoice=1,
    delivered_product_id=42
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

## notify_fulfillment

Create fulfillment notifications

[API reference](https://sell.app/docs/api/invoices/resend-invoice-deliverables) · Effect: **consequential**

```python
def notify_fulfillment(
        self,
        invoice: int,
        *,
        email: str | None | NotGiven = NOT_GIVEN,
        product_variant_ids: builtins.list[int] | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateFulfillmentNotificationsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| email | `str \| None \| NotGiven` | No |
| product_variant_ids | `builtins.list[int] \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateFulfillmentNotificationsResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.invoices.notify_fulfillment(invoice=1)
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

