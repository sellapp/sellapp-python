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
