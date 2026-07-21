"""Unit tests for the Tool Registry."""
from registry.tool_registry import ToolRegistry
from tools.tool import Tool
from tools.tool_result import ToolResult
from registry.exceptions import DuplicateRegistrationError, ComponentNotFoundError

class MockTool(Tool):
    def __init__(self, name: str):
        self._name = name
    def name(self) -> str:
        return self._name
    def description(self) -> str:
        return "mock tool"
    def execute(self, context) -> ToolResult:
        return ToolResult(success=True)

def test_registry_registration():
    registry = ToolRegistry()
    tool = MockTool("test_tool")
    registry.register(tool)
    assert registry.exists("test_tool")
    assert registry.get("test_tool") == tool

def test_registry_duplicate_prevention():
    registry = ToolRegistry()
    tool = MockTool("test_tool")
    registry.register(tool)
    try:
        registry.register(tool)
        assert False, "Should have raised DuplicateRegistrationError"
    except DuplicateRegistrationError:
        pass

def test_registry_not_found():
    registry = ToolRegistry()
    try:
        registry.get("non_existent")
        assert False, "Should have raised ComponentNotFoundError"
    except ComponentNotFoundError:
        pass

if __name__ == "__main__":
    test_registry_registration()
    test_registry_duplicate_prevention()
    test_registry_not_found()
    print("All tool registry tests PASSED.")
