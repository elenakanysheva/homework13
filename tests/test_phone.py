import pytest
from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone('iPhone 14', 120000, 5, 2)


def test_phone_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone1):
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
    with pytest.raises(ValueError):
        phone1.number_of_sim = -1
        phone1.number_of_sim = 0
        phone1.number_of_sim = 1.2
