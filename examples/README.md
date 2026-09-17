# Python examples

[Back to onboarding](../README.md)

Start with a product title, then try more pages or error handling. Each script is
complete: copy it, run it, and change it to fit what you're building.

Install the local SDK from its repository root with `python -m pip install .`.
Set `SELLAPP_API_KEY`, `SELLAPP_STORE`, and
`SELLAPP_API_BASE_URL` as shown in the README. These scripts only read products:

```sh
python examples/first_request.py
python examples/async_first_request.py
python examples/pagination.py
python examples/errors.py
```

The pagination example reads all pages. The error example prints a count on
success and shows diagnostic information if the request fails; it does not
deliberately provoke a production error.

To exercise the exact scripts with dummy credentials and a localhost mock,
run `python examples/check.py` from the source checkout after installing
the SDK. This also tests an empty store, two pages, a forbidden response with a
request ID, both authentication headers, and failure before transport when the
example base URL is absent. It makes no SellApp API calls.
