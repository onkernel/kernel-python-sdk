# Shared Types

```python
from kernel.types import AppAction, ErrorDetail, ErrorEvent, ErrorModel, HeartbeatEvent, LogEvent
```

# Deployments

Types:

```python
from kernel.types import (
    DeploymentStateEvent,
    DeploymentCreateResponse,
    DeploymentRetrieveResponse,
    DeploymentListResponse,
    DeploymentFollowResponse,
)
```

Methods:

- <code title="post /deployments">client.deployments.<a href="./src/kernel/resources/deployments.py">create</a>(\*\*<a href="src/kernel/types/deployment_create_params.py">params</a>) -> <a href="./src/kernel/types/deployment_create_response.py">DeploymentCreateResponse</a></code>
- <code title="get /deployments/{id}">client.deployments.<a href="./src/kernel/resources/deployments.py">retrieve</a>(id) -> <a href="./src/kernel/types/deployment_retrieve_response.py">DeploymentRetrieveResponse</a></code>
- <code title="get /deployments">client.deployments.<a href="./src/kernel/resources/deployments.py">list</a>(\*\*<a href="src/kernel/types/deployment_list_params.py">params</a>) -> <a href="./src/kernel/types/deployment_list_response.py">DeploymentListResponse</a></code>
- <code title="get /deployments/{id}/events">client.deployments.<a href="./src/kernel/resources/deployments.py">follow</a>(id, \*\*<a href="src/kernel/types/deployment_follow_params.py">params</a>) -> <a href="./src/kernel/types/deployment_follow_response.py">DeploymentFollowResponse</a></code>

# Apps

Types:

```python
from kernel.types import AppListResponse
```

Methods:

- <code title="get /apps">client.apps.<a href="./src/kernel/resources/apps/apps.py">list</a>(\*\*<a href="src/kernel/types/app_list_params.py">params</a>) -> <a href="./src/kernel/types/app_list_response.py">AppListResponse</a></code>

## Deployments

Types:

```python
from kernel.types.apps import DeploymentCreateResponse, DeploymentFollowResponse
```

Methods:

- <code title="post /deploy">client.apps.deployments.<a href="./src/kernel/resources/apps/deployments.py">create</a>(\*\*<a href="src/kernel/types/apps/deployment_create_params.py">params</a>) -> <a href="./src/kernel/types/apps/deployment_create_response.py">DeploymentCreateResponse</a></code>
- <code title="get /apps/{id}/events">client.apps.deployments.<a href="./src/kernel/resources/apps/deployments.py">follow</a>(id) -> <a href="./src/kernel/types/apps/deployment_follow_response.py">DeploymentFollowResponse</a></code>

# Invocations

Types:

```python
from kernel.types import (
    InvocationStateEvent,
    InvocationCreateResponse,
    InvocationRetrieveResponse,
    InvocationUpdateResponse,
    InvocationFollowResponse,
)
```

Methods:

- <code title="post /invocations">client.invocations.<a href="./src/kernel/resources/invocations.py">create</a>(\*\*<a href="src/kernel/types/invocation_create_params.py">params</a>) -> <a href="./src/kernel/types/invocation_create_response.py">InvocationCreateResponse</a></code>
- <code title="get /invocations/{id}">client.invocations.<a href="./src/kernel/resources/invocations.py">retrieve</a>(id) -> <a href="./src/kernel/types/invocation_retrieve_response.py">InvocationRetrieveResponse</a></code>
- <code title="patch /invocations/{id}">client.invocations.<a href="./src/kernel/resources/invocations.py">update</a>(id, \*\*<a href="src/kernel/types/invocation_update_params.py">params</a>) -> <a href="./src/kernel/types/invocation_update_response.py">InvocationUpdateResponse</a></code>
- <code title="delete /invocations/{id}/browsers">client.invocations.<a href="./src/kernel/resources/invocations.py">delete_browsers</a>(id) -> None</code>
- <code title="get /invocations/{id}/events">client.invocations.<a href="./src/kernel/resources/invocations.py">follow</a>(id) -> <a href="./src/kernel/types/invocation_follow_response.py">InvocationFollowResponse</a></code>

# Browsers

Types:

```python
from kernel.types import (
    BrowserPersistence,
    BrowserCreateResponse,
    BrowserRetrieveResponse,
    BrowserListResponse,
)
```

Methods:

- <code title="post /browsers">client.browsers.<a href="./src/kernel/resources/browsers.py">create</a>(\*\*<a href="src/kernel/types/browser_create_params.py">params</a>) -> <a href="./src/kernel/types/browser_create_response.py">BrowserCreateResponse</a></code>
- <code title="get /browsers/{id}">client.browsers.<a href="./src/kernel/resources/browsers.py">retrieve</a>(id) -> <a href="./src/kernel/types/browser_retrieve_response.py">BrowserRetrieveResponse</a></code>
- <code title="get /browsers">client.browsers.<a href="./src/kernel/resources/browsers.py">list</a>() -> <a href="./src/kernel/types/browser_list_response.py">BrowserListResponse</a></code>
- <code title="delete /browsers">client.browsers.<a href="./src/kernel/resources/browsers.py">delete</a>(\*\*<a href="src/kernel/types/browser_delete_params.py">params</a>) -> None</code>
- <code title="delete /browsers/{id}">client.browsers.<a href="./src/kernel/resources/browsers.py">delete_by_id</a>(id) -> None</code>
- <code title="get /browsers/{id}/replay">client.browsers.<a href="./src/kernel/resources/browsers.py">retrieve_replay</a>(id) -> BinaryAPIResponse</code>
