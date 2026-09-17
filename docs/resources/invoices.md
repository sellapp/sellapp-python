# invoices

[All resources](../methods.md)

## list

List all invoices

[API reference](https://sell.app/docs/api/invoices/list-all-invoices) · Effect: **read**

```python
def list(
        self,
        *,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        page: Optional[int] = None,
        search: Optional[str] = None,
        search_by: Optional[Union[InvoicesSearchBy, str]] = None,
        id: Optional[str] = None,
        email: Optional[str] = None,
        transaction_id: Optional[str] = None,
        serial_code: Optional[str] = None,
        additional_info: Optional[str] = None,
        product_name: Optional[str] = None,
        discord_data: Optional[str] = None,
        crypto_txid: Optional[str] = None,
        crypto_address: Optional[str] = None,
        coupon_code: Optional[str] = None,
        status: Optional[List[Union[InvoicesStatus, str]]] = None,
        payment_methods: Optional[List[Union[InvoicesPaymentMethods, str]]] = None,
        sort: Optional[Union[InvoicesSort, str]] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[ListInvoicesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| page | `Optional[int]` | No |
| search | `Optional[str]` | No |
| search_by | `Optional[Union[InvoicesSearchBy, str]]` | No |
| id | `Optional[str]` | No |
| email | `Optional[str]` | No |
| transaction_id | `Optional[str]` | No |
| serial_code | `Optional[str]` | No |
| additional_info | `Optional[str]` | No |
| product_name | `Optional[str]` | No |
| discord_data | `Optional[str]` | No |
| crypto_txid | `Optional[str]` | No |
| crypto_address | `Optional[str]` | No |
| coupon_code | `Optional[str]` | No |
| status | `Optional[List[Union[InvoicesStatus, str]]]` | No |
| payment_methods | `Optional[List[Union[InvoicesPaymentMethods, str]]]` | No |
| sort | `Optional[Union[InvoicesSort, str]]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        payment_method: Union[SdkCreateInvoiceRequestApplicationJsonPaymentMethod, str],
        product_variants: CreateInvoiceRequestApplicationJsonPropertyProductVariants,
        customer_ip: Union[str, None, NotGiven] = NOT_GIVEN,
        coupon: Optional[str] = None,
        vat_id: Optional[str] = None,
        country: Optional[str] = None,
        affiliate: Union[str, None, NotGiven] = NOT_GIVEN,
        extra: Optional[CreateInvoiceRequestApplicationJsonPropertyExtra] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateInvoiceResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| customer_email | `str` | Yes |
| payment_method | `Union[SdkCreateInvoiceRequestApplicationJsonPaymentMethod, str]` | Yes |
| product_variants | `CreateInvoiceRequestApplicationJsonPropertyProductVariants` | Yes |
| customer_ip | `Union[str, None, NotGiven]` | No |
| coupon | `Optional[str]` | No |
| vat_id | `Optional[str]` | No |
| country | `Optional[str]` | No |
| affiliate | `Union[str, None, NotGiven]` | No |
| extra | `Optional[CreateInvoiceRequestApplicationJsonPropertyExtra]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        search: Optional[str] = None,
        search_by: Optional[
            Union[SdkSearchInvoicesRequestApplicationJsonSearchBy, str]
        ] = None,
        id: Optional[str] = None,
        email: Optional[str] = None,
        transaction_id: Optional[str] = None,
        serial_code: Optional[str] = None,
        additional_info: Optional[str] = None,
        product_name: Optional[str] = None,
        discord_data: Optional[str] = None,
        crypto_txid: Optional[str] = None,
        crypto_address: Optional[str] = None,
        coupon_code: Optional[str] = None,
        status: Optional[
            List[Union[SdkSearchInvoicesRequestApplicationJsonStatus, str]]
        ] = None,
        payment_methods: Optional[
            List[Union[SdkSearchInvoicesRequestApplicationJsonPaymentMethods, str]]
        ] = None,
        sort: Optional[Union[SdkSearchInvoicesRequestApplicationJsonSort, str]] = None,
        limit: Optional[int] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        order: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> SyncPage[SearchInvoicesResponseValue200ApplicationJsonPropertyDataItem]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| search | `Optional[str]` | No |
| search_by | `Optional[
            Union[SdkSearchInvoicesRequestApplicationJsonSearchBy, str]
        ]` | No |
| id | `Optional[str]` | No |
| email | `Optional[str]` | No |
| transaction_id | `Optional[str]` | No |
| serial_code | `Optional[str]` | No |
| additional_info | `Optional[str]` | No |
| product_name | `Optional[str]` | No |
| discord_data | `Optional[str]` | No |
| crypto_txid | `Optional[str]` | No |
| crypto_address | `Optional[str]` | No |
| coupon_code | `Optional[str]` | No |
| status | `Optional[
            List[Union[SdkSearchInvoicesRequestApplicationJsonStatus, str]]
        ]` | No |
| payment_methods | `Optional[
            List[Union[SdkSearchInvoicesRequestApplicationJsonPaymentMethods, str]]
        ]` | No |
| sort | `Optional[Union[SdkSearchInvoicesRequestApplicationJsonSort, str]]` | No |
| limit | `Optional[int]` | No |
| before | `Optional[str]` | No |
| after | `Optional[str]` | No |
| order | `Optional[str]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetInvoiceResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateCheckoutSessionResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkGetInvoiceDeliverablesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        expected_status: Union[Union[ExpectedStatus, str], None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkMarkPendingInvoiceCompletedResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| expected_status | `Union[Union[ExpectedStatus, str], None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        expected_status: Union[Union[ExpectedStatus, str], None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkMarkPendingInvoiceVoidedResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| expected_status | `Union[Union[ExpectedStatus, str], None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkIssueReplacementForCompletedInvoiceResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| product_variants | `IssueReplacementForCompletedInvoiceRequestApplicationJsonPropertyProductVariants` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        status: Union[SdkUpdateInvoiceStatusRequestApplicationJsonStatus, str],
        expected_status: Union[Union[ExpectedStatus, str], None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkUpdateInvoiceStatusResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| status | `Union[SdkUpdateInvoiceStatusRequestApplicationJsonStatus, str]` | Yes |
| expected_status | `Union[Union[ExpectedStatus, str], None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        amount: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateInvoiceRefundResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| amount | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        email: Union[str, None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateFulfillmentRetryResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| email | `Union[str, None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateDynamicDeliveryRetryResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| delivered_product_id | `int` | Yes |
| request_options | `Optional[RequestOptions]` | No |

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
        email: Union[str, None, NotGiven] = NOT_GIVEN,
        product_variant_ids: Union[List[int], None, NotGiven] = NOT_GIVEN,
        request_options: Optional[RequestOptions] = None,
    ) -> SdkCreateFulfillmentNotificationsResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| invoice | `int` | Yes |
| email | `Union[str, None, NotGiven]` | No |
| product_variant_ids | `Union[List[int], None, NotGiven]` | No |
| request_options | `Optional[RequestOptions]` | No |

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

