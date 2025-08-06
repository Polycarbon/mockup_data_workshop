from __future__ import annotations

"""factory_boy factories backed by SQLAlchemy sessions."""

import factory
from faker import Faker

from db import SessionLocal, engine
from models import Base, Customer

# Ensure the table exists
Base.metadata.create_all(bind=engine)

faker = Faker()


class CustomerFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Factory that persists generated customers to the database."""

    class Meta:
        model = Customer
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    name = factory.LazyFunction(faker.name)
    email = factory.LazyFunction(faker.email)
    phone = factory.LazyFunction(faker.phone_number)
