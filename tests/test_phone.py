import pytest
from src.phone import Phone


@pytest.fixture()
def data():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


def test_phone(data):
    assert str(data) == 'iPhone 14'
    assert repr(data) == "Phone('iPhone 14', 120000, 5, 2)"
    assert data.number_of_sim == 2
    data.number_of_sim = 3
    assert data.number_of_sim == 3
