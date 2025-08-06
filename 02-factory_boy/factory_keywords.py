from factories import UserFactory
from robot.api.deco import keyword

@keyword
def create_user(**overrides):  # noqa: D401
    """Keyword: *Create User*

    Return a single fake user dictionary. Accepts optional named arguments as
    overrides: `Create User    email=foo@bar.com`"""

    return UserFactory(**overrides)

@keyword
def create_users(count: int = 10, **overrides):  # noqa: D401
    """Keyword: *Create Users*

    Return a list of *count* fake user dictionaries."""

    return UserFactory.create_batch(count, **overrides)

