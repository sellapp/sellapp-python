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
