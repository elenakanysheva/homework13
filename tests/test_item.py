"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def other():
    return 5


def test_item_calculate_total_price(item1, item2):
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_item_apply_discount(item1, item2):
    Item.pay_rate = 0.8
    item1.apply_discount()
    item2.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 16000.0


def test_item_name(item1):
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_item_string_to_number():
    Item.string_to_number('5') == 5
    Item.string_to_number('5.0') == 5
    Item.string_to_number('5.5') == 5


def test_item_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_item_str(item1):
    assert str(item1) == 'Смартфон'


def test_item_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert phone1.quantity + item1.quantity == 25
    assert phone1.quantity + phone1.quantity == 10
    with pytest.raises(ValueError):
        pass


