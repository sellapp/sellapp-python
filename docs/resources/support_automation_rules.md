# support_automation_rules

[All resources](../methods.md)

## list

List support automation rules

[API reference](https://sell.app/docs/api/support-automation-rules/list-support-automation-rules) · Effect: **read**

```python
def list(
        self,
        *,
        limit: int | None = None,
        before: str | None = None,
        after: str | None = None,
        order: str | None = None,
        page: int | None = None,
        active_state: SupportAutomationRulesActiveState | str | None = None,
        archive_state: SupportAutomationRulesArchiveState | str | None = None,
        search: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SyncPage[
        ListSupportAutomationRulesResponseValue200ApplicationJsonPropertyDataItem
    ]:
```

| Argument | Native type | Required |
| --- | --- | --- |
| limit | `int \| None` | No |
| before | `str \| None` | No |
| after | `str \| None` | No |
| order | `str \| None` | No |
| page | `int \| None` | No |
| active_state | `SupportAutomationRulesActiveState \| str \| None` | No |
| archive_state | `SupportAutomationRulesArchiveState \| str \| None` | No |
| search | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SyncPage[
        ListSupportAutomationRulesResponseValue200ApplicationJsonPropertyDataItem
    ]`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_rules.list()
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

Create a support automation rule

[API reference](https://sell.app/docs/api/support-automation-rules/create-a-support-automation-rule) · Effect: **consequential**

```python
def create(
        self,
        *,
        name: str,
        response_template_id: int | None,
        match_reason_source: MatchReasonSource | str | None | NotGiven = NOT_GIVEN,
        match_reason_code: str | None | NotGiven = NOT_GIVEN,
        match_product_ids: builtins.list[int] | None = None,
        match_customer_filter: MatchCustomerFilter | str | None | NotGiven = NOT_GIVEN,
        history_window: HistoryWindow | str | None | NotGiven = NOT_GIVEN,
        match_min_order_total_cents: int | None | NotGiven = NOT_GIVEN,
        match_max_order_total_cents: int | None | NotGiven = NOT_GIVEN,
        min_completed_orders: int | None | NotGiven = NOT_GIVEN,
        max_completed_orders: int | None | NotGiven = NOT_GIVEN,
        min_lifetime_spend_cents: int | None | NotGiven = NOT_GIVEN,
        max_lifetime_spend_cents: int | None | NotGiven = NOT_GIVEN,
        min_prior_ticket_count: int | None | NotGiven = NOT_GIVEN,
        max_prior_ticket_count: int | None | NotGiven = NOT_GIVEN,
        min_prior_support_refund_count: int | None | NotGiven = NOT_GIVEN,
        max_prior_support_refund_count: int | None | NotGiven = NOT_GIVEN,
        min_prior_support_refund_cents: int | None | NotGiven = NOT_GIVEN,
        max_prior_support_refund_cents: int | None | NotGiven = NOT_GIVEN,
        customer_age_days_min: int | None | NotGiven = NOT_GIVEN,
        customer_age_days_max: int | None | NotGiven = NOT_GIVEN,
        action_refund_kind: ActionRefundKind | str | None | NotGiven = NOT_GIVEN,
        action_refund_percent_basis: int | None | NotGiven = NOT_GIVEN,
        action_refund_fixed_cents: int | None | NotGiven = NOT_GIVEN,
        action_refund_cap_cents: int | None | NotGiven = NOT_GIVEN,
        action_close_outcome: ActionCloseOutcome | str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        id: int | None = None,
        archived: bool | None = None,
        currency: Literal["USD"] | None = None,
        created_at: str | None | NotGiven = NOT_GIVEN,
        updated_at: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkCreateSupportAutomationRuleResponseValue201ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| name | `str` | Yes |
| response_template_id | `int \| None` | Yes |
| match_reason_source | `MatchReasonSource \| str \| None \| NotGiven` | No |
| match_reason_code | `str \| None \| NotGiven` | No |
| match_product_ids | `builtins.list[int] \| None` | No |
| match_customer_filter | `MatchCustomerFilter \| str \| None \| NotGiven` | No |
| history_window | `HistoryWindow \| str \| None \| NotGiven` | No |
| match_min_order_total_cents | `int \| None \| NotGiven` | No |
| match_max_order_total_cents | `int \| None \| NotGiven` | No |
| min_completed_orders | `int \| None \| NotGiven` | No |
| max_completed_orders | `int \| None \| NotGiven` | No |
| min_lifetime_spend_cents | `int \| None \| NotGiven` | No |
| max_lifetime_spend_cents | `int \| None \| NotGiven` | No |
| min_prior_ticket_count | `int \| None \| NotGiven` | No |
| max_prior_ticket_count | `int \| None \| NotGiven` | No |
| min_prior_support_refund_count | `int \| None \| NotGiven` | No |
| max_prior_support_refund_count | `int \| None \| NotGiven` | No |
| min_prior_support_refund_cents | `int \| None \| NotGiven` | No |
| max_prior_support_refund_cents | `int \| None \| NotGiven` | No |
| customer_age_days_min | `int \| None \| NotGiven` | No |
| customer_age_days_max | `int \| None \| NotGiven` | No |
| action_refund_kind | `ActionRefundKind \| str \| None \| NotGiven` | No |
| action_refund_percent_basis | `int \| None \| NotGiven` | No |
| action_refund_fixed_cents | `int \| None \| NotGiven` | No |
| action_refund_cap_cents | `int \| None \| NotGiven` | No |
| action_close_outcome | `ActionCloseOutcome \| str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| id | `int \| None` | No |
| archived | `bool \| None` | No |
| currency | `Literal["USD"] \| None` | No |
| created_at | `str \| None \| NotGiven` | No |
| updated_at | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkCreateSupportAutomationRuleResponseValue201ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_rules.create(
    name="Expired download links",
    match_reason_source="store",
    match_reason_code="download-link-expired",
    match_product_ids=[120],
    match_max_order_total_cents=5000,
    max_prior_support_refund_count=0,
    response_template_id=32,
    action_refund_kind="partial",
    action_refund_percent_basis=5000,
    action_refund_cap_cents=1000,
    action_close_outcome="refunded_partial"
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

## get

Retrieve a support automation rule

[API reference](https://sell.app/docs/api/support-automation-rules/retrieve-a-support-automation-rule) · Effect: **read**

```python
def get(
        self,
        support_automation_rule: int,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetSupportAutomationRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_automation_rule | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetSupportAutomationRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_rules.get(support_automation_rule=7)
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

Update a support automation rule

[API reference](https://sell.app/docs/api/support-automation-rules/update-a-support-automation-rule) · Effect: **consequential**

```python
def replace(
        self,
        support_automation_rule: int,
        *,
        name: str | None = None,
        match_reason_source: MatchReasonSource | str | None | NotGiven = NOT_GIVEN,
        match_reason_code: str | None | NotGiven = NOT_GIVEN,
        match_product_ids: builtins.list[int] | None = None,
        match_customer_filter: MatchCustomerFilter | str | None | NotGiven = NOT_GIVEN,
        history_window: HistoryWindow | str | None | NotGiven = NOT_GIVEN,
        match_min_order_total_cents: int | None | NotGiven = NOT_GIVEN,
        match_max_order_total_cents: int | None | NotGiven = NOT_GIVEN,
        min_completed_orders: int | None | NotGiven = NOT_GIVEN,
        max_completed_orders: int | None | NotGiven = NOT_GIVEN,
        min_lifetime_spend_cents: int | None | NotGiven = NOT_GIVEN,
        max_lifetime_spend_cents: int | None | NotGiven = NOT_GIVEN,
        min_prior_ticket_count: int | None | NotGiven = NOT_GIVEN,
        max_prior_ticket_count: int | None | NotGiven = NOT_GIVEN,
        min_prior_support_refund_count: int | None | NotGiven = NOT_GIVEN,
        max_prior_support_refund_count: int | None | NotGiven = NOT_GIVEN,
        min_prior_support_refund_cents: int | None | NotGiven = NOT_GIVEN,
        max_prior_support_refund_cents: int | None | NotGiven = NOT_GIVEN,
        customer_age_days_min: int | None | NotGiven = NOT_GIVEN,
        customer_age_days_max: int | None | NotGiven = NOT_GIVEN,
        response_template_id: int | None | NotGiven = NOT_GIVEN,
        action_refund_kind: ActionRefundKind | str | None | NotGiven = NOT_GIVEN,
        action_refund_percent_basis: int | None | NotGiven = NOT_GIVEN,
        action_refund_fixed_cents: int | None | NotGiven = NOT_GIVEN,
        action_refund_cap_cents: int | None | NotGiven = NOT_GIVEN,
        action_close_outcome: ActionCloseOutcome | str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        clear: builtins.list[
            SdkReplaceSupportAutomationRuleRequestApplicationJsonClear | str
        ]
        | None = None,
        expected_updated_at: str | None = None,
        id: int | None = None,
        archived: bool | None = None,
        priority: int | None = None,
        currency: Literal["USD"] | None = None,
        created_at: str | None | NotGiven = NOT_GIVEN,
        updated_at: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkReplaceSupportAutomationRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_automation_rule | `int` | Yes |
| name | `str \| None` | No |
| match_reason_source | `MatchReasonSource \| str \| None \| NotGiven` | No |
| match_reason_code | `str \| None \| NotGiven` | No |
| match_product_ids | `builtins.list[int] \| None` | No |
| match_customer_filter | `MatchCustomerFilter \| str \| None \| NotGiven` | No |
| history_window | `HistoryWindow \| str \| None \| NotGiven` | No |
| match_min_order_total_cents | `int \| None \| NotGiven` | No |
| match_max_order_total_cents | `int \| None \| NotGiven` | No |
| min_completed_orders | `int \| None \| NotGiven` | No |
| max_completed_orders | `int \| None \| NotGiven` | No |
| min_lifetime_spend_cents | `int \| None \| NotGiven` | No |
| max_lifetime_spend_cents | `int \| None \| NotGiven` | No |
| min_prior_ticket_count | `int \| None \| NotGiven` | No |
| max_prior_ticket_count | `int \| None \| NotGiven` | No |
| min_prior_support_refund_count | `int \| None \| NotGiven` | No |
| max_prior_support_refund_count | `int \| None \| NotGiven` | No |
| min_prior_support_refund_cents | `int \| None \| NotGiven` | No |
| max_prior_support_refund_cents | `int \| None \| NotGiven` | No |
| customer_age_days_min | `int \| None \| NotGiven` | No |
| customer_age_days_max | `int \| None \| NotGiven` | No |
| response_template_id | `int \| None \| NotGiven` | No |
| action_refund_kind | `ActionRefundKind \| str \| None \| NotGiven` | No |
| action_refund_percent_basis | `int \| None \| NotGiven` | No |
| action_refund_fixed_cents | `int \| None \| NotGiven` | No |
| action_refund_cap_cents | `int \| None \| NotGiven` | No |
| action_close_outcome | `ActionCloseOutcome \| str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| clear | `builtins.list[
            SdkReplaceSupportAutomationRuleRequestApplicationJsonClear \| str
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| id | `int \| None` | No |
| archived | `bool \| None` | No |
| priority | `int \| None` | No |
| currency | `Literal["USD"] \| None` | No |
| created_at | `str \| None \| NotGiven` | No |
| updated_at | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReplaceSupportAutomationRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_rules.replace(
    support_automation_rule=7,
    name="Expired download links, first refund only",
    clear=["match_max_order_total_cents"],
    expected_updated_at="2026-07-03T09:20:00.000000Z"
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

Update a support automation rule

[API reference](https://sell.app/docs/api/support-automation-rules/update-a-support-automation-rule) · Effect: **consequential**

```python
def update(
        self,
        support_automation_rule: int,
        *,
        name: str | None = None,
        match_reason_source: MatchReasonSource | str | None | NotGiven = NOT_GIVEN,
        match_reason_code: str | None | NotGiven = NOT_GIVEN,
        match_product_ids: builtins.list[int] | None = None,
        match_customer_filter: MatchCustomerFilter | str | None | NotGiven = NOT_GIVEN,
        history_window: HistoryWindow | str | None | NotGiven = NOT_GIVEN,
        match_min_order_total_cents: int | None | NotGiven = NOT_GIVEN,
        match_max_order_total_cents: int | None | NotGiven = NOT_GIVEN,
        min_completed_orders: int | None | NotGiven = NOT_GIVEN,
        max_completed_orders: int | None | NotGiven = NOT_GIVEN,
        min_lifetime_spend_cents: int | None | NotGiven = NOT_GIVEN,
        max_lifetime_spend_cents: int | None | NotGiven = NOT_GIVEN,
        min_prior_ticket_count: int | None | NotGiven = NOT_GIVEN,
        max_prior_ticket_count: int | None | NotGiven = NOT_GIVEN,
        min_prior_support_refund_count: int | None | NotGiven = NOT_GIVEN,
        max_prior_support_refund_count: int | None | NotGiven = NOT_GIVEN,
        min_prior_support_refund_cents: int | None | NotGiven = NOT_GIVEN,
        max_prior_support_refund_cents: int | None | NotGiven = NOT_GIVEN,
        customer_age_days_min: int | None | NotGiven = NOT_GIVEN,
        customer_age_days_max: int | None | NotGiven = NOT_GIVEN,
        response_template_id: int | None | NotGiven = NOT_GIVEN,
        action_refund_kind: ActionRefundKind | str | None | NotGiven = NOT_GIVEN,
        action_refund_percent_basis: int | None | NotGiven = NOT_GIVEN,
        action_refund_fixed_cents: int | None | NotGiven = NOT_GIVEN,
        action_refund_cap_cents: int | None | NotGiven = NOT_GIVEN,
        action_close_outcome: ActionCloseOutcome | str | None | NotGiven = NOT_GIVEN,
        is_active: bool | None = None,
        clear: builtins.list[
            SdkUpdateSupportAutomationRuleRequestApplicationJsonClear | str
        ]
        | None = None,
        expected_updated_at: str | None = None,
        id: int | None = None,
        archived: bool | None = None,
        priority: int | None = None,
        currency: Literal["USD"] | None = None,
        created_at: str | None | NotGiven = NOT_GIVEN,
        updated_at: str | None | NotGiven = NOT_GIVEN,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateSupportAutomationRuleResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_automation_rule | `int` | Yes |
| name | `str \| None` | No |
| match_reason_source | `MatchReasonSource \| str \| None \| NotGiven` | No |
| match_reason_code | `str \| None \| NotGiven` | No |
| match_product_ids | `builtins.list[int] \| None` | No |
| match_customer_filter | `MatchCustomerFilter \| str \| None \| NotGiven` | No |
| history_window | `HistoryWindow \| str \| None \| NotGiven` | No |
| match_min_order_total_cents | `int \| None \| NotGiven` | No |
| match_max_order_total_cents | `int \| None \| NotGiven` | No |
| min_completed_orders | `int \| None \| NotGiven` | No |
| max_completed_orders | `int \| None \| NotGiven` | No |
| min_lifetime_spend_cents | `int \| None \| NotGiven` | No |
| max_lifetime_spend_cents | `int \| None \| NotGiven` | No |
| min_prior_ticket_count | `int \| None \| NotGiven` | No |
| max_prior_ticket_count | `int \| None \| NotGiven` | No |
| min_prior_support_refund_count | `int \| None \| NotGiven` | No |
| max_prior_support_refund_count | `int \| None \| NotGiven` | No |
| min_prior_support_refund_cents | `int \| None \| NotGiven` | No |
| max_prior_support_refund_cents | `int \| None \| NotGiven` | No |
| customer_age_days_min | `int \| None \| NotGiven` | No |
| customer_age_days_max | `int \| None \| NotGiven` | No |
| response_template_id | `int \| None \| NotGiven` | No |
| action_refund_kind | `ActionRefundKind \| str \| None \| NotGiven` | No |
| action_refund_percent_basis | `int \| None \| NotGiven` | No |
| action_refund_fixed_cents | `int \| None \| NotGiven` | No |
| action_refund_cap_cents | `int \| None \| NotGiven` | No |
| action_close_outcome | `ActionCloseOutcome \| str \| None \| NotGiven` | No |
| is_active | `bool \| None` | No |
| clear | `builtins.list[
            SdkUpdateSupportAutomationRuleRequestApplicationJsonClear \| str
        ]
        \| None` | No |
| expected_updated_at | `str \| None` | No |
| id | `int \| None` | No |
| archived | `bool \| None` | No |
| priority | `int \| None` | No |
| currency | `Literal["USD"] \| None` | No |
| created_at | `str \| None \| NotGiven` | No |
| updated_at | `str \| None \| NotGiven` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateSupportAutomationRuleResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_rules.update(
    support_automation_rule=7,
    name="Expired download links, first refund only",
    clear=["match_max_order_total_cents"],
    expected_updated_at="2026-07-03T09:20:00.000000Z"
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

## update_state

Update a support automation rule state

[API reference](https://sell.app/docs/api/support-automation-rules/change-a-support-automation-rule-state) · Effect: **consequential**

```python
def update_state(
        self,
        support_automation_rule: int,
        *,
        state: SdkUpdateSupportAutomationRuleStateRequestApplicationJsonState | str,
        expected_updated_at: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> SdkUpdateSupportAutomationRuleStateResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| support_automation_rule | `int` | Yes |
| state | `SdkUpdateSupportAutomationRuleStateRequestApplicationJsonState \| str` | Yes |
| expected_updated_at | `str \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkUpdateSupportAutomationRuleStateResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_rules.update_state(
    support_automation_rule=1,
    state="active",
    expected_updated_at="2026-07-03T09:20:00.000000Z"
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

## reorder

Reorder support automation rules

[API reference](https://sell.app/docs/api/support-automation-rules/reorder-support-automation-rules) · Effect: **consequential**

```python
def reorder(
        self,
        *,
        ordered_rule_ids: builtins.list[int],
        request_options: RequestOptions | None = None,
    ) -> SdkReorderSupportAutomationRulesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ordered_rule_ids | `builtins.list[int]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkReorderSupportAutomationRulesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_rules.reorder(ordered_rule_ids=[7])
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

## dry_run

Dry run support automation rules

[API reference](https://sell.app/docs/api/support-automation-rules/dry-run-support-automation-rules) · Effect: **read**

```python
def dry_run(
        self,
        *,
        ticket_id: int,
        request_options: RequestOptions | None = None,
    ) -> SdkDryRunSupportAutomationRulesResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| ticket_id | `int` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkDryRunSupportAutomationRulesResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key=os.environ["SELLAPP_API_KEY"], store=os.environ["SELLAPP_STORE"])

result = client.support_automation_rules.dry_run(ticket_id=4821)
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

