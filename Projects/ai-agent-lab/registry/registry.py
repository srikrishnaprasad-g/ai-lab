"""Generic Registry framework."""

from typing import Generic, TypeVar, Protocol, Iterable
from registry.exceptions import DuplicateRegistrationError, ComponentNotFoundError


class NamedComponent(Protocol):
    """Protocol for components that have a name."""

    def name(self) -> str:
        """Returns the name of the component."""
        ...


T = TypeVar("T", bound=NamedComponent)


class Registry(Generic[T]):
    """Generic registry to manage named components."""

    def __init__(self) -> None:
        """Initializes an empty registry."""
        self._components: dict[str, T] = {}

    def register(self, component: T) -> None:
        """Registers a component.

        Args:
            component: The component to register.

        Raises:
            DuplicateRegistrationError: If a component with the same name exists.
        """
        name = component.name()
        if name in self._components:
            raise DuplicateRegistrationError(f"Component '{name}' already registered.")
        self._components[name] = component

    def get(self, name: str) -> T:
        """Retrieves a component by name.

        Args:
            name: The name of the component.

        Returns:
            The component.

        Raises:
            ComponentNotFoundError: If the component does not exist.
        """
        if name not in self._components:
            raise ComponentNotFoundError(f"Component '{name}' not found.")
        return self._components[name]

    def exists(self, name: str) -> bool:
        """Checks if a component exists.

        Args:
            name: The name of the component.

        Returns:
            True if exists, False otherwise.
        """
        return name in self._components

    def list_all(self) -> list[T]:
        """Lists all registered components.

        Note: Renamed from list() to avoid shadowing built-in type.

        Returns:
            A list of all registered components.
        """
        return list(self._components.values())

    def remove(self, name: str) -> None:
        """Removes a component by name.

        Args:
            name: The name of the component.

        Raises:
            ComponentNotFoundError: If the component does not exist.
        """
        if name not in self._components:
            raise ComponentNotFoundError(f"Component '{name}' not found.")
        del self._components[name]
