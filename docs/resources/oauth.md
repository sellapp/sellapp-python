# oauth

[All resources](../methods.md)

## get_oauth_authorization_server_metadata

Read OAuth server metadata

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```python
def get_oauth_authorization_server_metadata(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> SdkGetOAuthAuthorizationServerMetadataResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkGetOAuthAuthorizationServerMetadataResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key="", store="")

result = client.oauth.get_oauth_authorization_server_metadata()
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[]
```

Documented HTTP responses: 200, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## get_oauth_authorization_request

Review CLI authorization

[API reference](https://sell.app/docs/api/oauth) · Effect: **read**

```python
def get_oauth_authorization_request(
        self,
        *,
        response_type: Literal["code"],
        client_id: str,
        redirect_uri: str,
        scope: str | None = None,
        state: str,
        code_challenge: str,
        code_challenge_method: Literal["S256"],
        request_options: RequestOptions | None = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| response_type | `Literal["code"]` | Yes |
| client_id | `str` | Yes |
| redirect_uri | `str` | Yes |
| scope | `str \| None` | No |
| state | `str` | Yes |
| code_challenge | `str` | Yes |
| code_challenge_method | `Literal["S256"]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `Any`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key="", store="")

result = client.oauth.get_oauth_authorization_request(
    response_type="code",
    client_id="01992a65-e064-71ba-b38f-902b7966a6be",
    redirect_uri="http://127.0.0.1:49152/callback",
    state="RANDOM_STATE",
    code_challenge="E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM",
    code_challenge_method="S256"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[]
```

Documented HTTP responses: 200, 302, 400, 401, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## approve_oauth_authorization

Approve CLI access

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```python
def approve_oauth_authorization(
        self,
        *,
        auth_token: str,
        client_id: str,
        state: str,
        token: str,
        request_options: RequestOptions | None = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| auth_token | `str` | Yes |
| client_id | `str` | Yes |
| state | `str` | Yes |
| token | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `Any`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], browser_session=os.environ["SELLAPP_BROWSER_SESSION"], store="")

result = client.oauth.approve_oauth_authorization(
    auth_token="CONSENT_AUTH_TOKEN",
    client_id="01992a65-e064-71ba-b38f-902b7966a6be",
    state="RANDOM_STATE",
    token="CSRF_TOKEN"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "oauthBrowserSession": []
  }
]
```

Documented HTTP responses: 302, 400, 401, 403, 419, 422, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## deny_oauth_authorization

Deny CLI access

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```python
def deny_oauth_authorization(
        self,
        *,
        auth_token: str,
        token: str,
        request_options: RequestOptions | None = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| auth_token | `str` | Yes |
| token | `str` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `Any`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], browser_session=os.environ["SELLAPP_BROWSER_SESSION"], store="")

result = client.oauth.deny_oauth_authorization(
    auth_token="CONSENT_AUTH_TOKEN",
    token="CSRF_TOKEN"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {
    "oauthBrowserSession": []
  }
]
```

Documented HTTP responses: 302, 400, 401, 419, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## exchange_oauth_token

Exchange or refresh OAuth tokens

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```python
def exchange_oauth_token(
        self,
        *,
        body: ExchangeOAuthTokenRequestApplicationXWwwFormUrlencodedOneOfValue1
        | ExchangeOAuthTokenRequestApplicationXWwwFormUrlencodedOneOfValue2
        | dict[str, Any],
        request_options: RequestOptions | None = None,
    ) -> SdkExchangeOAuthTokenResponseValue200ApplicationJson:
```

| Argument | Native type | Required |
| --- | --- | --- |
| body | `ExchangeOAuthTokenRequestApplicationXWwwFormUrlencodedOneOfValue1
        \| ExchangeOAuthTokenRequestApplicationXWwwFormUrlencodedOneOfValue2
        \| dict[str, Any]` | Yes |
| request_options | `RequestOptions \| None` | No |

Returns: `SdkExchangeOAuthTokenResponseValue200ApplicationJson`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key="", store="")

result = client.oauth.exchange_oauth_token(
    body={
        "client_id": "01992a65-e064-71ba-b38f-902b7966a6be",
        "grant_type": "authorization_code",
        "code": "AUTHORIZATION_CODE",
        "redirect_uri": "http://127.0.0.1:49152/callback",
        "code_verifier": "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
    }
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {},
  {
    "oauthClientBasic": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

## revoke_oauth_token

Revoke an OAuth token

[API reference](https://sell.app/docs/api/oauth) · Effect: **consequential**

```python
def revoke_oauth_token(
        self,
        *,
        token: str,
        client_id: str | None = None,
        client_secret: str | None = None,
        token_type_hint: SdkRevokeOAuthTokenRequestApplicationXWwwFormUrlencodedTokenTypeHint
        | str
        | None = None,
        request_options: RequestOptions | None = None,
    ) -> Any:
```

| Argument | Native type | Required |
| --- | --- | --- |
| token | `str` | Yes |
| client_id | `str \| None` | No |
| client_secret | `str \| None` | No |
| token_type_hint | `SdkRevokeOAuthTokenRequestApplicationXWwwFormUrlencodedTokenTypeHint
        \| str
        \| None` | No |
| request_options | `RequestOptions \| None` | No |

Returns: `Any`.

```py
import os
from sellapp_sdk import SellAppClient

client = SellAppClient(base_url=os.environ["SELLAPP_API_BASE_URL"], api_key="", store="")

result = client.oauth.revoke_oauth_token(
    client_id="01992a65-e064-71ba-b38f-902b7966a6be",
    token="REFRESH_TOKEN",
    token_type_hint="refresh_token"
)
print(result)
```

### Authentication and errors

Supported credential alternatives (each object is one alternative):

```json
[
  {},
  {
    "oauthClientBasic": []
  }
]
```

Documented HTTP responses: 200, 400, 401, 429, 500. See the API reference for field-level validation and consequences.

[Response access, transport controls, pagination, and typed errors](../usage.md)

