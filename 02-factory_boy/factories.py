from __future__ import annotations

"""Factories for generating mock objects using factory_boy.

Run example:
    python -m 02-factory_boy.factories --count 3

This module defines a simple `User` dataclass and a `UserFactory` that can
produce realistic fake users. The factory can be imported elsewhere (e.g. in
Robot Framework libraries) to drive automated tests or seed databases.
"""

import argparse
import json
from dataclasses import dataclass, asdict

import factory
from faker import Faker

faker = Faker()


@dataclass
class User:
    """Lightweight user model suitable for serialization."""

    name: str
    username: str
    email: str
    address: str
    phone: str


class UserFactory(factory.Factory):
    """Factory Boy factory for `User`."""

    class Meta:
        model = User

    name = factory.LazyFunction(faker.name)
    username = factory.LazyFunction(faker.user_name)
    email = factory.LazyFunction(faker.email)
    address = factory.LazyFunction(lambda: faker.address().replace("\n", ", "))
    phone = factory.LazyFunction(faker.phone_number)

    @classmethod
    def as_dict(cls, **kwargs):  # type: ignore[override]
        """Return a single user as a Python dict."""
        return asdict(cls(**kwargs))




if __name__ == "__main__":  # pragma: no cover
    # Mock data for a single record
    single_user = UserFactory()
    print("Single User Mock Data:")
    print(single_user)

    # # Mock data for a batch of multiple records
    users = UserFactory.create_batch(10)
    print("\nBatch User Mock Data:")
    for user in users:
        print(user)

    # # Parse overrides into factory
    override_user = UserFactory(name='Liza', username='lisadon')
    print("\nOverride User Mock Data:")
    print(override_user)
