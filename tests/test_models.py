import pytest
from src.models import (
    Person,
    Vehicle,
    Official,
    Infraction
)


def test_create_person():
    """ tests una persona con un vehiculo"""
    name = "pedro picapiedra"
    email = "pedritoP@gmail.com"
    pedro = Person(name, email)

    toyota_corolla = Vehicle(1234, "negro", pedro)

    assert toyota_corolla.owner == pedro
    assert pedro.vehicles == [toyota_corolla]
    assert pedro.email == email


def test_add_infraction_to_vehicle():
    """ tests una persona con un vechicul con una infraccion"""
    name = "pedro picapiedra"
    email = "pedritoP@gmail.com"
    pedro = Person(name, email)

    toyota_corolla = Vehicle(1234, "negro", pedro)
    oficial_perez = Official("perez", 1)

    oficial_perez.assign_infraction(toyota_corolla, "mal estacionado")

    assert toyota_corolla.number_of_infractions == 1
    assert toyota_corolla.infractions == [toyota_corolla.infractions[0]]


if __name__ == "__main__":
    pytest.main()
