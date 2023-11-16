"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.paths import Csv_path
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    Item.pay_rate = 0.8
    item.apply_discount()

    assert item.price == 8000.0


def test_all_items_list(item):
    item2 = Item("Ноутбук", 20000, 5)

    assert len(Item.all) == 4
    assert item in Item.all
    assert item2 in Item.all
    Item.all.clear()


def test_instantiate_from_csv():
    Item.instantiate_from_csv(Csv_path)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('2.1') == 2
    assert Item.string_to_number('12.5') == 12


def test_name_price_quantity():
    item1 = Item('Смартфон', 10000, 5)
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 5


def test_name_setter():
    item = Item("Test Item", 15.0, 3)

    item.name = "LongNameString"
    assert item._Item__name == "LongNameString"
    item.name = "ShortName"
    assert item._Item__name == "ShortName"


def test_repr():
    item1 = Item('Смартфон', 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item('Смартфон', 10000, 20)
    assert str(item1) == 'Смартфон'
