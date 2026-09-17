"""Compile examples and bind calls to the installed client's actual signatures; no HTTP requests."""
import ast
import inspect
import json
import os
import sys
from pathlib import Path

os.environ['SELLAPP_API_KEY'] = 'documentation-fixture-key'
for credential in ['ACCESS_TOKEN', 'CUSTOMER_SESSION', 'BROWSER_SESSION']:
    os.environ[f'SELLAPP_{credential}'] = 'documentation-fixture-credential'
os.environ['SELLAPP_STORE'] = 'launch-lab'
os.environ['SELLAPP_API_BASE_URL'] = 'http://127.0.0.1:1/api'
snippets = [snippet for name in ['operation-examples.json', 'operation-variants.json'] for snippet in json.loads((Path(sys.argv[1]) / 'docs' / name).read_text())]
errors = []
for snippet in snippets:
    namespace = {}
    try:
        tree = ast.parse(snippet['content'])
        compile(tree, snippet['operationId'], 'exec')
        calls = 0
        for statement in tree.body:
            if isinstance(statement, (ast.Expr, ast.Assign)) and isinstance(statement.value, ast.Call) and ast.unparse(statement.value.func).startswith('client.'):
                call = statement.value
                function = eval(compile(ast.Expression(call.func), '<target>', 'eval'), namespace)
                positional = [eval(compile(ast.Expression(value), '<arg>', 'eval'), namespace) for value in call.args]
                keywords = {value.arg: eval(compile(ast.Expression(value.value), '<arg>', 'eval'), namespace) for value in call.keywords}
                inspect.signature(function).bind(*positional, **keywords)
                calls += 1
            elif isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call) and ast.unparse(statement.value.func) == 'print':
                continue
            else:
                exec(compile(ast.Module(body=[statement], type_ignores=[]), '<setup>', 'exec'), namespace)
        if calls != 1:
            raise ValueError(f'Expected one SDK call, found {calls}')
    except Exception as error:
        errors.append(f"{snippet['operationId']}: {error}")
    finally:
        client = namespace.get('client')
        if client is not None and hasattr(client, 'close'):
            client.close()
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Compiled and signature-bound {len(snippets)} Python operation examples; no HTTP requests executed.")
