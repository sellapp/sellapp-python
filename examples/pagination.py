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
