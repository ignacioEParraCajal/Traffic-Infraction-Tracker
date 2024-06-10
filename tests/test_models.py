import pytest
from src.models import Person, Vehicle, Official, Infraction
from datetime import date
from src.models import Infraction


@pytest.fixture
def pedro():
    return Person(name="pedro picapiedra", email="pedritoP@gmail.com")


@pytest.fixture
def toyota_corolla(pedro):
    return Vehicle(patent=1234, color="negro", owner=pedro)


@pytest.fixture
def oficial_perez():
    return Official(name="perez", identity_id=1)


def test_create_person(pedro, toyota_corolla):
    assert toyota_corolla.owner == pedro
    assert pedro.vehicles == [toyota_corolla]
    assert pedro.email == "pedritoP@gmail.com"


def test_add_infraction_to_vehicle(pedro, toyota_corolla, oficial_perez):
    oficial_perez.assign_infraction(toyota_corolla, "mal estacionado")

    assert toyota_corolla.number_of_infractions == 1
    assert toyota_corolla.infractions[0].comments == "mal estacionado"
