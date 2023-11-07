"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
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

    assert len(Item.all) == 2
    assert item in Item.all
    assert item2 in Item.all
    Item.all.clear()
