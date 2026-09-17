# SellApp Python SDK

Put your SellApp store to work from Python. Read your catalog, work with orders,
or connect customers to your own tools. The SDK turns Python method calls into
API requests and returns objects whose fields you can use straight away.

We'll start with one product and print its title. A small script is enough to
find out whether your store and your code are on speaking terms.
Already building an integration? Jump to [configuration](https://github.com/sellapp/sellapp-python/blob/main/docs/usage.md#client-configuration),
[async](#prefer-async), or the [method index](https://github.com/sellapp/sellapp-python/blob/main/docs/methods.md).

## Availability and installation

**Install from source for now.** This SDK is pre-release, and publication of
`sellapp-sdk` on PyPI has not been verified.

You'll need access to [this private repository](https://github.com/sellapp/sellapp-python). Open a terminal
in your local copy, then create a virtual environment and install the SDK there.
The virtual environment keeps this project's Python packages together:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install .
```

On Windows, activate with `.venv\Scripts\Activate.ps1`. The distribution name
is `sellapp-sdk`; the import is `sellapp_sdk`.

Use Python 3.12, the tested native toolchain. The package metadata currently says
3.9+, but generated type aliases import `typing.TypeAlias` (introduced in 3.10),
so Python 3.9 is not usable. Support for the other declared versions has not been
validated in this onboarding pass.

## First request

Your API key identifies your account; the store slug selects the store. For
`launch-lab.sell.app`, the slug is `launch-lab`. This request needs the key's
`listing` ability, which grants catalog access. Follow the
[authentication guide](https://sell.app/docs/api/authentication) for key setup and
permissions, and keep the secret key on your server.

Set these environment variables in a Bash-compatible terminal, replacing both placeholders.
Your script can read these settings without keeping credentials in its source:

```sh
export SELLAPP_API_KEY="your-api-key"
export SELLAPP_STORE="your-store"
export SELLAPP_API_BASE_URL="https://sell.app/api"
```

The address above connects to your real store. This first request only reads data.
The SDK sends the key as `Authorization: Bearer` and the slug as `X-STORE`.
The API site's curl examples use `SELLAPP_STORE`; the Python SDK reads
`SELLAPP_STORE`.

The examples require an explicit base URL: you choose where they connect.
`SELLAPP_API_BASE_URL` is an example convention,
read by the scripts and passed to `base_url`; the SDK itself does not read it.

Save this as `first_request.py` and run `python first_request.py`, or use the
copy in the checkout with `python examples/first_request.py`:

```python
import os

from sellapp_sdk import SellAppClient

base_url = os.environ["SELLAPP_API_BASE_URL"]
if not base_url.strip():
    raise ValueError("Set a nonempty SELLAPP_API_BASE_URL before running this example")

with SellAppClient(base_url=base_url) as client:
    page = client.products.list(limit=1)
    for product in page.data:
        print(product.id, product.title)
    if not page.data:
        print("No products yet. Your connection is ready.")
```

The result is a page, or one batch of products. `limit=1` asks for at most one;
`page.data` holds the returned product objects. The script prints each product's
ID and title. An empty store still proves the connection works, and the script
says so. The `with` block closes the client's HTTP connections when it finishes.

### Prefer async?

If your app already uses `asyncio`, use `AsyncSellAppClient`
and `await` each request. It comes in the same package; there's nothing extra to
install. For a simple script, the synchronous example above is all you need.
Run `python examples/async_first_request.py`:

```python
import asyncio
import os

from sellapp_sdk import AsyncSellAppClient

base_url = os.environ["SELLAPP_API_BASE_URL"]
if not base_url.strip():
    raise ValueError("Set a nonempty SELLAPP_API_BASE_URL before running this example")


async def main():
    async with AsyncSellAppClient(base_url=base_url) as client:
        page = await client.products.list(limit=1)
        for product in page.data:
            print(product.id, product.title)
        if not page.data:
            print("No products yet. Your connection is ready.")


asyncio.run(main())
```

## Account access and first-store setup

Create a user-owned key in [API keys](https://sell.app/user/api-tokens), even
before you have a store. Enable `account:read` for identity, store discovery and
permission inspection, and `stores:create` separately for store creation.
Identity, discovery, store detail by ID and creation omit `X-STORE`; permission
inspection and business requests select a store explicitly.

An unrestricted key covers current and future accessible stores. A selected-store
key covers only its fixed list; an empty list covers none. Membership and role
changes still apply. Selected-store keys cannot create stores. Existing keys do
not gain abilities automatically; `*` satisfies the new abilities while retaining
membership, role and restriction checks.

The [account guide](https://sell.app/docs/api/authentication#discover-your-account-before-selecting-a-store)
shows first-store creation, required idempotency keys, and bounded reads across
several stores with partial failures. Creation returns an ID and slug; use the
slug for subsequent product requests. Find your language's methods in the
[resource reference](https://github.com/sellapp/sellapp-python/blob/main/docs/methods.md). CLI and MCP connections retain browser OAuth.

## If the request fails

| Result | Next step |
| --- | --- |
| Empty product list | The read succeeded. Create a product when you are ready. |
| 401 | Check the selected credential and whether it has expired or been revoked. |
| 403 | Check the key's listing ability, selected-store restrictions and the account's current store permissions. Official CLI OAuth also requires its active grant. |
| 400 with a missing-store message | Set SELLAPP_STORE to an authorized store slug. |
| 429 | Follow Retry-After and the SDK's documented retry behavior. |

Keep the request ID when reporting an API failure. Never include credentials.

## Three useful next actions

1. [Create and edit a product](https://github.com/sellapp/sellapp-python/blob/main/docs/resources/products.md): exact signatures and complete examples.
2. [Read orders or create a checkout](https://github.com/sellapp/sellapp-python/blob/main/docs/resources/orders.md): inspect permissions and effects before changing a purchase.
3. [Read more than one page](https://github.com/sellapp/sellapp-python/blob/main/docs/usage.md): pagination, request controls, errors, and retry behavior.

## Reference and examples

- [Resource reference](https://github.com/sellapp/sellapp-python/blob/main/docs/methods.md)
- [Runnable examples](https://github.com/sellapp/sellapp-python/blob/main/examples/README.md)
- [API documentation](https://sell.app/docs/api)

## Support and releases

This source candidate is not a verified registry release. Use the source installation above.
[Report an SDK issue](https://github.com/sellapp/sellapp-python/issues) if you have repository access.
Include the SDK version, runtime version, and a redacted reproduction.
Licensed under [MIT](https://github.com/sellapp/sellapp-python/blob/main/LICENSE.txt); see [third-party notices](https://github.com/sellapp/sellapp-python/blob/main/NOTICE.txt).
