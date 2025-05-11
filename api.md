# Apps

Types:

```python
from kernel.types import AppDeployResponse, AppInvokeResponse, AppRetrieveInvocationResponse
```

Methods:

- <code title="post /apps/deploy">client.apps.<a href="./src/kernel/resources/apps.py">deploy</a>(\*\*<a href="src/kernel/types/app_deploy_params.py">params</a>) -> <a href="./src/kernel/types/app_deploy_response.py">AppDeployResponse</a></code>
- <code title="post /apps/invoke">client.apps.<a href="./src/kernel/resources/apps.py">invoke</a>(\*\*<a href="src/kernel/types/app_invoke_params.py">params</a>) -> <a href="./src/kernel/types/app_invoke_response.py">AppInvokeResponse</a></code>
- <code title="get /apps/invocations/{id}">client.apps.<a href="./src/kernel/resources/apps.py">retrieve_invocation</a>(id) -> <a href="./src/kernel/types/app_retrieve_invocation_response.py">AppRetrieveInvocationResponse</a></code>

# Browser

Types:

```python
from kernel.types import BrowserCreateSessionResponse
```

Methods:

- <code title="post /browser">client.browser.<a href="./src/kernel/resources/browser.py">create_session</a>() -> <a href="./src/kernel/types/browser_create_session_response.py">BrowserCreateSessionResponse</a></code>
