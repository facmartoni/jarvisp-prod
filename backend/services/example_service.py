"""
Example service module.
Services encapsulate business logic and should be used by GraphQL resolvers.
"""


class ExampleService:
    """Example service to demonstrate service-oriented architecture."""
    
    @staticmethod
    def get_greeting(name: str = "World") -> str:
        """Return a greeting message."""
        return f"Hello, {name}!"
