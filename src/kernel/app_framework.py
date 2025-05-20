import json
import inspect
import functools
from typing import Any, Dict, List, TypeVar, Callable, Optional
from dataclasses import dataclass

T = TypeVar("T")

# Context definition
@dataclass
class KernelContext:
    """Context object passed to action handlers"""
    invocation_id: str

# Action definition
@dataclass
class KernelAction:
    """Action that can be invoked on a Kernel app"""
    name: str
    handler: Callable[..., Any]

# JSON interfaces
@dataclass
class KernelActionJson:
    """JSON representation of a Kernel action"""
    name: str

@dataclass
class KernelAppJson:
    """JSON representation of a Kernel app"""
    name: str
    actions: List[KernelActionJson]

@dataclass
class KernelJson:
    """JSON representation of Kernel manifest"""
    apps: List[KernelAppJson]

# App class
class KernelApp:
    def __init__(self, name: str):
        self.name = name
        self.actions: Dict[str, KernelAction] = {}
        # Register this app in the global registry
        _app_registry.register_app(self)

    def action(self, name: str) -> Callable[..., Any]:
        """
        Decorator to register an action with the app
        
        Usage:
            @app.action("action-name")
            def my_handler(ctx: KernelContext):
                # ...
                
            @app.action("action-with-payload")
            def my_handler(ctx: KernelContext, payload: dict):
                # ...
        """
        def decorator(handler: Callable[..., Any]) -> Callable[..., Any]:
            return self._register_action(name, handler)
        return decorator

    def _register_action(self, name: str, handler: Callable[..., Any]) -> Callable[..., Any]:
        """Internal method to register an action"""
        # Validate handler signature
        sig = inspect.signature(handler)
        param_count = len(sig.parameters)
        
        if param_count == 0:
            raise TypeError("Action handler must accept at least the context parameter")
        elif param_count > 2:
            raise TypeError("Action handler can only accept context and payload parameters")
            
        param_names = list(sig.parameters.keys())

        @functools.wraps(handler)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Ensure the first argument is the context
            if not args or not isinstance(args[0], KernelContext):
                raise TypeError("First argument to action handler must be a KernelContext")
                
            ctx = args[0]
            
            if param_count == 1:
                # Handler takes only context
                return handler(ctx)
            else:  # param_count == 2
                # Handler takes context and payload
                if len(args) >= 2:
                    return handler(ctx, args[1])
                else:
                    # Try to find payload in kwargs
                    payload_name = param_names[1]
                    if payload_name in kwargs:
                        return handler(ctx, kwargs[payload_name])
                    else:
                        raise TypeError(f"Missing required payload parameter '{payload_name}'")

        action = KernelAction(name=name, handler=wrapper)
        self.actions[name] = action
        return wrapper

    def get_actions(self) -> List[KernelAction]:
        """Get all actions for this app"""
        return list(self.actions.values())

    def get_action(self, name: str) -> Optional[KernelAction]:
        """Get an action by name"""
        return self.actions.get(name)

    def to_dict(self) -> KernelAppJson:
        """Export app information without handlers"""
        return KernelAppJson(
            name=self.name,
            actions=[KernelActionJson(name=action.name) for action in self.get_actions()]
        )


# Registry for storing Kernel apps
class KernelAppRegistry:
    def __init__(self) -> None:
        self.apps: Dict[str, KernelApp] = {}

    def register_app(self, app: KernelApp) -> None:
        self.apps[app.name] = app

    def get_apps(self) -> List[KernelApp]:
        return list(self.apps.values())

    def get_app_by_name(self, name: str) -> Optional[KernelApp]:
        return self.apps.get(name)
        
    def export(self) -> KernelJson:
        """Export the registry as a KernelJson object"""
        apps = [app.to_dict() for app in self.get_apps()]
        return KernelJson(apps=apps)

    def export_json(self) -> str:
        """Export the registry as JSON"""
        kernel_json = self.export()
        return json.dumps(kernel_json.__dict__, indent=2)


# Create singleton registry for apps
_app_registry = KernelAppRegistry()

# Create a simple function for creating apps
def App(name: str) -> KernelApp:
    """Create a new Kernel app"""
    return KernelApp(name)

# Export the app registry for boot loader
app_registry = _app_registry

# Function to export registry as JSON
def export_registry() -> str:
    """Export the registry as JSON"""
    return _app_registry.export_json()
