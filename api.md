# Apps

## Deployments

Types:

```python
from kernel.types.apps import DeploymentCreateResponse
```

Methods:

- <code title="post /deploy">client.apps.deployments.<a href="./src/kernel/resources/apps/deployments.py">create</a>(\*\*<a href="src/kernel/types/apps/deployment_create_params.py">params</a>) -> <a href="./src/kernel/types/apps/deployment_create_response.py">DeploymentCreateResponse</a></code>

## Invocations

Types:

```python
from kernel.types.apps import InvocationCreateResponse, InvocationRetrieveResponse
```

Methods:

- <code title="post /invocations">client.apps.invocations.<a href="./src/kernel/resources/apps/invocations.py">create</a>(\*\*<a href="src/kernel/types/apps/invocation_create_params.py">params</a>) -> <a href="./src/kernel/types/apps/invocation_create_response.py">InvocationCreateResponse</a></code>
- <code title="get /invocations/{id}">client.apps.invocations.<a href="./src/kernel/resources/apps/invocations.py">retrieve</a>(id) -> <a href="./src/kernel/types/apps/invocation_retrieve_response.py">InvocationRetrieveResponse</a></code>

# Browsers

Types:

```python
from kernel.types import BrowserCreateResponse, BrowserRetrieveResponse
```

Methods:

- <code title="post /browsers">client.browsers.<a href="./src/kernel/resources/browsers.py">create</a>(\*\*<a href="src/kernel/types/browser_create_params.py">params</a>) -> <a href="./src/kernel/types/browser_create_response.py">BrowserCreateResponse</a></code>
- <code title="get /browsers/{id}">client.browsers.<a href="./src/kernel/resources/browsers.py">retrieve</a>(id) -> <a href="./src/kernel/types/browser_retrieve_response.py">BrowserRetrieveResponse</a></code>
