"""Registry-specific exception definitions."""


class RegistryException(Exception):
    """Base exception for all registry-related errors."""
    pass


class DuplicateRegistrationError(RegistryException):
    """Raised when trying to register a component with an existing name."""
    pass


class ComponentNotFoundError(RegistryException):
    """Raised when a component is not found in the registry."""
    pass
