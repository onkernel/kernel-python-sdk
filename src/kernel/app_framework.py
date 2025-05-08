import json
import inspect
import functools
from typing import Any, Dict, List, Union, TypeVar, Callable, Optional
from dataclasses import dataclass

T = TypeVar("T")


# Context definition
@dataclass
class KernelContext:
    """Context object passed to action handlers"""

    invocation_id: str


# Browser definition
class Browser:
    def __init__(self, cdp_ws_url: str):
        self.cdp_ws_url = cdp_ws_url


# Action definition
class KernelAction:
    def __init__(self, name: str, handler: Callable[..., Any]):
        self.name = name
        self.handler = handler


# App class
class KernelApp:
    def __init__(self, name: str):
        self.name = name
        self.actions: Dict[str, KernelAction] = {}
        # Register this app in the global registry
        _app_registry.register_app(self)

    def action(self, name_or_handler: Optional[Union[str, Callable[..., Any]]] = None):
        """Decorator to register an action with the app"""
        if name_or_handler is None:
            # This is the @app.action() case, which should return the decorator
            def decorator(f: Callable[..., Any]):
                return self._register_action(f.__name__, f)

            return decorator
        elif callable(name_or_handler):
            # This is the @app.action case (handler passed directly)
            return self._register_action(name_or_handler.__name__, name_or_handler)
        else:
            # This is the @app.action("name") case (name_or_handler is a string)
            def decorator(f: Callable[..., Any]):
                return self._register_action(name_or_handler, f)  # name_or_handler is the name string here

            return decorator

    def _register_action(self, name: str, handler: Callable[..., Any]) -> Callable[..., Any]:
        """Internal method to register an action"""

        @functools.wraps(handler)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Determine if the original handler accepts context as first argument
            sig = inspect.signature(handler)
            param_names = list(sig.parameters.keys())
            param_count = len(param_names)

            if param_count == 1:
                actual_input = None
                # The handler only takes input
                if len(args) > 0:  # Prioritize args if context was implicitly passed
                    # If context (args[0]) and input (args[1]) were provided, or just input (args[0])
                    actual_input = args[1] if len(args) > 1 else args[0]
                elif kwargs:
                    # Attempt to find the single expected kwarg
                    if param_names:  # Should always be true if param_count == 1
                        param_name = param_names[0]
                        if param_name in kwargs:
                            actual_input = kwargs[param_name]
                        elif kwargs:  # Fallback if name doesn't match but kwargs exist
                            actual_input = next(iter(kwargs.values()))
                    elif kwargs:  # param_names is empty but kwargs exist (unlikely for param_count==1)
                        actual_input = next(iter(kwargs.values()))
                # If no args/kwargs, actual_input remains None, handler might raise error or accept None
                return handler(actual_input)
            else:  # param_count == 0 or param_count > 1
                # Handler takes context and input (or more), or no args
                return handler(*args, **kwargs)

        action = KernelAction(name=name, handler=wrapper)
        self.actions[name] = action
        return wrapper

    def get_actions(self) -> List[KernelAction]:
        """Get all actions for this app"""
        return list(self.actions.values())

    def get_action(self, name: str) -> Optional[KernelAction]:
        """Get an action by name"""
        return self.actions.get(name)

    def to_dict(self) -> Dict[str, Any]:
        """Export app information without handlers"""
        return {"name": self.name, "actions": [{"name": action.name} for action in self.get_actions()]}


# Registry for storing Kernel apps
class KernelAppRegistry:
    def __init__(self):
        self.apps: Dict[str, KernelApp] = {}

    def register_app(self, app: KernelApp) -> None:
        self.apps[app.name] = app

    def get_apps(self) -> List[KernelApp]:
        return list(self.apps.values())

    def get_app_by_name(self, name: str) -> Optional[KernelApp]:
        return self.apps.get(name)

    def export_json(self, entrypoint_relpath: str) -> str:
        """Export the registry as JSON"""
        apps = [app.to_dict() for app in self.get_apps()]
        return json.dumps({"apps": apps, "entrypoint": entrypoint_relpath}, indent=2)


# Create singleton registry for apps
_app_registry = KernelAppRegistry()


# Browser management
class Browsers:
    @staticmethod
    def create(invocation_id: str) -> Browser:
        """Create a new browser instance"""
        # TODO: The cdp_ws_url is hardcoded here. This might need to be
        # dynamically configured or provided by the Kernel platform.
        return Browser(
            cdp_ws_url="wss://floral-morning-3s0r8t7x.iad-prod-apiukp-0.onkernel.app:9222/devtools/browser/4dc1cbf6-be0e-4612-bba3-8e399d9638c7"
        )


# Create browser management instance
browsers = Browsers()


# Create a simple function for creating apps
def App(name: str) -> KernelApp:
    """Create a new Kernel app"""
    return KernelApp(name)


# Export the app registry for boot loader
app_registry = _app_registry


# Function to export registry as JSON
def export_registry(entrypoint_relpath: str) -> str:
    """Export the registry as JSON"""
    return _app_registry.export_json(entrypoint_relpath)
