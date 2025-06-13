"""Sentinel Dragon package."""

__all__ = ["hello"]


def hello(name: str) -> str:
    """Return greeting"""
    return f"Hello, {name}!"
=======
=======
def hello(name: str = "World") -> str:
    """Return a greeting to the given name."""
    return f"Hello, {name}!"


__all__ = ["hello"]
