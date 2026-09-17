# Python usage guide

[Back to onboarding](../README.md)

## Pagination

The first request gives you one batch of products. To read a larger catalog,
process that batch and ask for the next one. This is pagination: enough data to
keep going, without downloading the entire store in one response.

`products.list()` returns a `SyncPage` (or an `AsyncPage` when awaited).
`data` contains typed product models for the current page. Products default to
15 per page on the API; use `limit` and `page` for explicit page requests.
The next-page helper uses `meta.current_page` and `meta.last_page` from the
response. It does not follow arbitrary URLs in `links` or provide an automatic
iterator over every page. Stop whenever you have enough results. Process a page
at a time to avoid keeping the whole catalog in memory.

Complete example, also saved as [pagination.py](../examples/pagination.py):

```python
import os

from sellapp_sdk import SellAppClient

base_url = os.environ["SELLAPP_API_BASE_URL"]
if not base_url.strip():
    raise ValueError("Set a nonempty SELLAPP_API_BASE_URL before running this example")

with SellAppClient(base_url=base_url) as client:
    page = client.products.list(limit=15)
    while page is not None:
        for product in page.data:
            print(product.id, product.title)
        page = page.get_next_page()
```

For async code, await both `client.products.list(...)` and
`page.get_next_page()`; iterate `page.data` with a regular `for` loop.
Other list endpoints may return arrays or different response models; consult
their generated signatures rather than assuming every result is a page.

## Errors with something useful to say

A failed request should leave you with a next step. Check credentials for an
authentication failure, inspect the status and message for an API rejection,
and check the connection for a transport failure. The request ID, when available,
helps identify the particular request you're investigating.

Complete example, also saved as [errors.py](../examples/errors.py):

```python
import os

from sellapp_sdk import (
    ApiError,
    AuthenticationError,
    SellAppClient,
    SerializationError,
    TimeoutError,
    TransportError,
)

base_url = os.environ["SELLAPP_API_BASE_URL"]
if not base_url.strip():
    raise ValueError("Set a nonempty SELLAPP_API_BASE_URL before running this example")

try:
    with SellAppClient(base_url=base_url) as client:
        page = client.products.list(limit=1, request_options={"max_retries": 0})
        print(f"Read {len(page.data)} product(s).")
except AuthenticationError as error:
    print(f"Check your API key and store: {error}")
except ApiError as error:
    print(f"API error: {error.status} {error.code}: {error.message}")
    print(f"Request ID: {error.request_id or 'not supplied'}")
except TimeoutError as error:
    print(f"Request timed out: {error}")
except TransportError as error:
    print(f"Connection failed: {error}")
except SerializationError as error:
    print(f"Unexpected response: {error}")
```

`ApiError` provides `type`, `code`, `message`, `status`, `param`,
`request_id`, `docs_url`, and the parsed `body`. Optional values may be
`None`; the request ID falls back to the response's `X-Request-ID` header.
Treat server-provided text and links as data. A 401 response or missing credentials
raises `AuthenticationError`, which retains structured fields for a 401 while
also representing credentials rejected locally before transport.

Timeouts are `TimeoutError` (a subclass of `TransportError`), so catch them
before other transport failures. Invalid JSON and malformed typed responses use
`SerializationError`. Locally invalid request models use `SchemaValidationError`.
All these SDK exceptions derive from `SellAppError`.

## Timeouts, retries, and idempotency

Sometimes a request needs another try. Retries handle certain temporary failures;
a timeout limits how long the client waits. Neither means every failed write is
safe to repeat, so check these rules before adding your own retry loop.

The default is two retries, up to three attempts. Safe HTTP methods, or a POST
whose operation declares idempotency and carries a nonblank key, may retry HTTP
408, 409, 429, 500, 502, 503, and 504 or transient transport failures. Backoff
starts at 0.5 seconds, doubles with jitter, and is bounded. A valid `Retry-After`
value takes precedence and is capped at 30 seconds. The 60-second timeout applies to HTTPX
operations within each attempt, not to the whole call including retry waits.

Pass nonnegative `max_retries` values. Per-request options use the same units
and semantics as constructor options; the error example disables retries so a
failure can be handled immediately. `SELLAPP_REQUEST_TIMEOUT` is not read by
this Python runtime.

An idempotency key names one intended change, so a supporting endpoint can
recognize another attempt at the same change.
Operations exposing `idempotency_key` forward a supplied value to
`Idempotency-Key`; the Python runtime does not generate a key automatically.
Retries reuse the supplied key. Do not assume a write is deduplicated merely
because it is retried; use the endpoint's documented idempotency support.

## Models and client lifetime

Use response fields as Python attributes, as the first example does with
`product.title`. You don't need to decode the response JSON yourself.

Response models are dataclasses with attribute access and `to_dict()` helpers.
Known timestamp fields become Python `datetime` values. Additive response fields
are retained in `additional_properties`; new request models remain subject to
schema validation. Keep one client for related work to reuse its connection pool.
Use `with` / `async with`, or call `close()` / `await close()` explicitly.
An injected HTTPX client's lifetime remains yours to manage.

The transport also accepts HTTPX-compatible `files` in request options for
multipart uploads, including bytes and file objects. For endpoint details, consult the
[API reference](https://sell.app/docs/api) and [method index](methods.md).

## Client configuration

The examples let the client read credentials from your environment. You can also
pass them directly, along with settings such as the timeout. Both client classes
accept the same keyword options:

Use access_token with store for OAuth business operations. OAuth management
operations select the installation directly. Use customer_session for the customer
portal; a seller credential cannot replace it. If both seller credentials are
configured, supported v2 calls prefer access_token and v1 calls use api_key.

OAuth protocol requests use the authorization server origin, without /api.
authorization_base_url overrides that origin for testing. client_basic accepts a
(client ID, secret) pair; omit body client_id and client_secret when using it.
browser_session accepts the complete browser Cookie header for consent forms.
Anonymous operations send no credentials. Redirect responses return their Location
without following it; the raw-response facade retains status and headers.

Token exchanges and customer-session creation never retry automatically. Serialize
refreshes per installation and save the replacement token pair together. After
losing a refresh response, do not retry the consumed credential blindly.

| Option | Behavior |
| --- | --- |
| `api_key`, `store` | Explicit non-`None` values override `SELLAPP_API_KEY` and `SELLAPP_STORE`. API keys can omit the store for v2 operations; v1 operations require it. |
| `base_url` | Defaults to `https://sell.app/api`. Include the `/api` prefix. |
| `timeout` | Defaults to 60 seconds; passed to HTTPX for each attempt. |
| `max_retries` | Defaults to 2 retries after the first attempt. Use 0 to disable. |
| `http_client` | Optional `httpx.Client` or `httpx.AsyncClient`; you retain responsibility for closing an injected client. |

Methods accept `request_options` with `timeout` (seconds), `max_retries`, and
`headers`. These override the corresponding request settings. There is no
per-request base URL option or automatic timeout environment variable.
