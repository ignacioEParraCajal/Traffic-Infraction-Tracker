# test_person.py
import pytest
from src.models import Person
from src.models import Vehicle


def test_create_person():
    """ tests una persona con un vehiculo"""
    name = "pedro picapiedra"
    email = "pedritoP@gmail.com"
    pedro = Person(name, email)

    toyota_corolla = Vehicle(1234, "negro", pedro)

    assert toyota_corolla.owner == pedro
    assert pedro.vehicles == [toyota_corolla]
    assert pedro.email == email


if __name__ == "__main__":
    pytest.main()
