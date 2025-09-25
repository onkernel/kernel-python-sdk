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
- <code title="get /deployments">client.deployments.<a href="./src/kernel/resources/deployments.py">list</a>(\*\*<a href="src/kernel/types/deployment_list_params.py">params</a>) -> <a href="./src/kernel/types/deployment_list_response.py">SyncOffsetPagination[DeploymentListResponse]</a></code>
- <code title="get /deployments/{id}/events">client.deployments.<a href="./src/kernel/resources/deployments.py">follow</a>(id, \*\*<a href="src/kernel/types/deployment_follow_params.py">params</a>) -> <a href="./src/kernel/types/deployment_follow_response.py">DeploymentFollowResponse</a></code>

# Apps

Types:

```python
from kernel.types import AppListResponse
```

Methods:

- <code title="get /apps">client.apps.<a href="./src/kernel/resources/apps.py">list</a>(\*\*<a href="src/kernel/types/app_list_params.py">params</a>) -> <a href="./src/kernel/types/app_list_response.py">AppListResponse</a></code>

# Invocations

Types:

```python
from kernel.types import (
    InvocationStateEvent,
    InvocationCreateResponse,
    InvocationRetrieveResponse,
    InvocationUpdateResponse,
    InvocationListResponse,
    InvocationFollowResponse,
)
```

Methods:

- <code title="post /invocations">client.invocations.<a href="./src/kernel/resources/invocations.py">create</a>(\*\*<a href="src/kernel/types/invocation_create_params.py">params</a>) -> <a href="./src/kernel/types/invocation_create_response.py">InvocationCreateResponse</a></code>
- <code title="get /invocations/{id}">client.invocations.<a href="./src/kernel/resources/invocations.py">retrieve</a>(id) -> <a href="./src/kernel/types/invocation_retrieve_response.py">InvocationRetrieveResponse</a></code>
- <code title="patch /invocations/{id}">client.invocations.<a href="./src/kernel/resources/invocations.py">update</a>(id, \*\*<a href="src/kernel/types/invocation_update_params.py">params</a>) -> <a href="./src/kernel/types/invocation_update_response.py">InvocationUpdateResponse</a></code>
- <code title="get /invocations">client.invocations.<a href="./src/kernel/resources/invocations.py">list</a>(\*\*<a href="src/kernel/types/invocation_list_params.py">params</a>) -> <a href="./src/kernel/types/invocation_list_response.py">SyncOffsetPagination[InvocationListResponse]</a></code>
- <code title="delete /invocations/{id}/browsers">client.invocations.<a href="./src/kernel/resources/invocations.py">delete_browsers</a>(id) -> None</code>
- <code title="get /invocations/{id}/events">client.invocations.<a href="./src/kernel/resources/invocations.py">follow</a>(id, \*\*<a href="src/kernel/types/invocation_follow_params.py">params</a>) -> <a href="./src/kernel/types/invocation_follow_response.py">InvocationFollowResponse</a></code>

# Browsers

Types:

```python
from kernel.types import (
    BrowserPersistence,
    Profile,
    BrowserCreateResponse,
    BrowserRetrieveResponse,
    BrowserListResponse,
)
```

Methods:

- <code title="post /browsers">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">create</a>(\*\*<a href="src/kernel/types/browser_create_params.py">params</a>) -> <a href="./src/kernel/types/browser_create_response.py">BrowserCreateResponse</a></code>
- <code title="get /browsers/{id}">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">retrieve</a>(id) -> <a href="./src/kernel/types/browser_retrieve_response.py">BrowserRetrieveResponse</a></code>
- <code title="get /browsers">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">list</a>() -> <a href="./src/kernel/types/browser_list_response.py">BrowserListResponse</a></code>
- <code title="delete /browsers">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">delete</a>(\*\*<a href="src/kernel/types/browser_delete_params.py">params</a>) -> None</code>
- <code title="delete /browsers/{id}">client.browsers.<a href="./src/kernel/resources/browsers/browsers.py">delete_by_id</a>(id) -> None</code>

## Replays

Types:

```python
from kernel.types.browsers import ReplayListResponse, ReplayStartResponse
```

Methods:

- <code title="get /browsers/{id}/replays">client.browsers.replays.<a href="./src/kernel/resources/browsers/replays.py">list</a>(id) -> <a href="./src/kernel/types/browsers/replay_list_response.py">ReplayListResponse</a></code>
- <code title="get /browsers/{id}/replays/{replay_id}">client.browsers.replays.<a href="./src/kernel/resources/browsers/replays.py">download</a>(replay_id, \*, id) -> BinaryAPIResponse</code>
- <code title="post /browsers/{id}/replays">client.browsers.replays.<a href="./src/kernel/resources/browsers/replays.py">start</a>(id, \*\*<a href="src/kernel/types/browsers/replay_start_params.py">params</a>) -> <a href="./src/kernel/types/browsers/replay_start_response.py">ReplayStartResponse</a></code>
- <code title="post /browsers/{id}/replays/{replay_id}/stop">client.browsers.replays.<a href="./src/kernel/resources/browsers/replays.py">stop</a>(replay_id, \*, id) -> None</code>

## Fs

Types:

```python
from kernel.types.browsers import FFileInfoResponse, FListFilesResponse
```

Methods:

- <code title="put /browsers/{id}/fs/create_directory">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">create_directory</a>(id, \*\*<a href="src/kernel/types/browsers/f_create_directory_params.py">params</a>) -> None</code>
- <code title="put /browsers/{id}/fs/delete_directory">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">delete_directory</a>(id, \*\*<a href="src/kernel/types/browsers/f_delete_directory_params.py">params</a>) -> None</code>
- <code title="put /browsers/{id}/fs/delete_file">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">delete_file</a>(id, \*\*<a href="src/kernel/types/browsers/f_delete_file_params.py">params</a>) -> None</code>
- <code title="get /browsers/{id}/fs/download_dir_zip">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">download_dir_zip</a>(id, \*\*<a href="src/kernel/types/browsers/f_download_dir_zip_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /browsers/{id}/fs/file_info">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">file_info</a>(id, \*\*<a href="src/kernel/types/browsers/f_file_info_params.py">params</a>) -> <a href="./src/kernel/types/browsers/f_file_info_response.py">FFileInfoResponse</a></code>
- <code title="get /browsers/{id}/fs/list_files">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">list_files</a>(id, \*\*<a href="src/kernel/types/browsers/f_list_files_params.py">params</a>) -> <a href="./src/kernel/types/browsers/f_list_files_response.py">FListFilesResponse</a></code>
- <code title="put /browsers/{id}/fs/move">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">move</a>(id, \*\*<a href="src/kernel/types/browsers/f_move_params.py">params</a>) -> None</code>
- <code title="get /browsers/{id}/fs/read_file">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">read_file</a>(id, \*\*<a href="src/kernel/types/browsers/f_read_file_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /browsers/{id}/fs/set_file_permissions">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">set_file_permissions</a>(id, \*\*<a href="src/kernel/types/browsers/f_set_file_permissions_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/fs/upload">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">upload</a>(id, \*\*<a href="src/kernel/types/browsers/f_upload_params.py">params</a>) -> None</code>
- <code title="post /browsers/{id}/fs/upload_zip">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">upload_zip</a>(id, \*\*<a href="src/kernel/types/browsers/f_upload_zip_params.py">params</a>) -> None</code>
- <code title="put /browsers/{id}/fs/write_file">client.browsers.fs.<a href="./src/kernel/resources/browsers/fs/fs.py">write_file</a>(id, contents, \*\*<a href="src/kernel/types/browsers/f_write_file_params.py">params</a>) -> None</code>

### Watch

Types:

```python
from kernel.types.browsers.fs import WatchEventsResponse, WatchStartResponse
```

Methods:

- <code title="get /browsers/{id}/fs/watch/{watch_id}/events">client.browsers.fs.watch.<a href="./src/kernel/resources/browsers/fs/watch.py">events</a>(watch_id, \*, id) -> <a href="./src/kernel/types/browsers/fs/watch_events_response.py">WatchEventsResponse</a></code>
- <code title="post /browsers/{id}/fs/watch">client.browsers.fs.watch.<a href="./src/kernel/resources/browsers/fs/watch.py">start</a>(id, \*\*<a href="src/kernel/types/browsers/fs/watch_start_params.py">params</a>) -> <a href="./src/kernel/types/browsers/fs/watch_start_response.py">WatchStartResponse</a></code>
- <code title="delete /browsers/{id}/fs/watch/{watch_id}">client.browsers.fs.watch.<a href="./src/kernel/resources/browsers/fs/watch.py">stop</a>(watch_id, \*, id) -> None</code>

## Process

Types:

```python
from kernel.types.browsers import (
    ProcessExecResponse,
    ProcessKillResponse,
    ProcessSpawnResponse,
    ProcessStatusResponse,
    ProcessStdinResponse,
    ProcessStdoutStreamResponse,
)
```

Methods:

- <code title="post /browsers/{id}/process/exec">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">exec</a>(id, \*\*<a href="src/kernel/types/browsers/process_exec_params.py">params</a>) -> <a href="./src/kernel/types/browsers/process_exec_response.py">ProcessExecResponse</a></code>
- <code title="post /browsers/{id}/process/{process_id}/kill">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">kill</a>(process_id, \*, id, \*\*<a href="src/kernel/types/browsers/process_kill_params.py">params</a>) -> <a href="./src/kernel/types/browsers/process_kill_response.py">ProcessKillResponse</a></code>
- <code title="post /browsers/{id}/process/spawn">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">spawn</a>(id, \*\*<a href="src/kernel/types/browsers/process_spawn_params.py">params</a>) -> <a href="./src/kernel/types/browsers/process_spawn_response.py">ProcessSpawnResponse</a></code>
- <code title="get /browsers/{id}/process/{process_id}/status">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">status</a>(process_id, \*, id) -> <a href="./src/kernel/types/browsers/process_status_response.py">ProcessStatusResponse</a></code>
- <code title="post /browsers/{id}/process/{process_id}/stdin">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">stdin</a>(process_id, \*, id, \*\*<a href="src/kernel/types/browsers/process_stdin_params.py">params</a>) -> <a href="./src/kernel/types/browsers/process_stdin_response.py">ProcessStdinResponse</a></code>
- <code title="get /browsers/{id}/process/{process_id}/stdout/stream">client.browsers.process.<a href="./src/kernel/resources/browsers/process.py">stdout_stream</a>(process_id, \*, id) -> <a href="./src/kernel/types/browsers/process_stdout_stream_response.py">ProcessStdoutStreamResponse</a></code>

## Logs

Methods:

- <code title="get /browsers/{id}/logs/stream">client.browsers.logs.<a href="./src/kernel/resources/browsers/logs.py">stream</a>(id, \*\*<a href="src/kernel/types/browsers/log_stream_params.py">params</a>) -> <a href="./src/kernel/types/shared/log_event.py">LogEvent</a></code>

# Profiles

Types:

```python
from kernel.types import ProfileListResponse
```

Methods:

- <code title="post /profiles">client.profiles.<a href="./src/kernel/resources/profiles.py">create</a>(\*\*<a href="src/kernel/types/profile_create_params.py">params</a>) -> <a href="./src/kernel/types/profile.py">Profile</a></code>
- <code title="get /profiles/{id_or_name}">client.profiles.<a href="./src/kernel/resources/profiles.py">retrieve</a>(id_or_name) -> <a href="./src/kernel/types/profile.py">Profile</a></code>
- <code title="get /profiles">client.profiles.<a href="./src/kernel/resources/profiles.py">list</a>() -> <a href="./src/kernel/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /profiles/{id_or_name}">client.profiles.<a href="./src/kernel/resources/profiles.py">delete</a>(id_or_name) -> None</code>
- <code title="get /profiles/{id_or_name}/download">client.profiles.<a href="./src/kernel/resources/profiles.py">download</a>(id_or_name) -> BinaryAPIResponse</code>

# Proxies

Types:

```python
from kernel.types import ProxyCreateResponse, ProxyRetrieveResponse, ProxyListResponse
```

Methods:

- <code title="post /proxies">client.proxies.<a href="./src/kernel/resources/proxies.py">create</a>(\*\*<a href="src/kernel/types/proxy_create_params.py">params</a>) -> <a href="./src/kernel/types/proxy_create_response.py">ProxyCreateResponse</a></code>
- <code title="get /proxies/{id}">client.proxies.<a href="./src/kernel/resources/proxies.py">retrieve</a>(id) -> <a href="./src/kernel/types/proxy_retrieve_response.py">ProxyRetrieveResponse</a></code>
- <code title="get /proxies">client.proxies.<a href="./src/kernel/resources/proxies.py">list</a>() -> <a href="./src/kernel/types/proxy_list_response.py">ProxyListResponse</a></code>
- <code title="delete /proxies/{id}">client.proxies.<a href="./src/kernel/resources/proxies.py">delete</a>(id) -> None</code>
