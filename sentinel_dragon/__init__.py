def hello(name: str = "World") -> str:
    """Return a greeting to the given name."""
    return f"Hello, {name}!"


__all__ = ["hello"]
