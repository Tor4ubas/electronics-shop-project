from src.item import Item
import pytest
from src.phone import Phone

@pytest.fixture
def item1():

    """ Экземпляр класса в фикстуре """

    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone1():

    """ Экземпляр класса в фикстуре """

    return Phone("IPhone", 30000, 10, 2)


def test_1(item1):

    """ Тест метода init """

    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):

    """ Тест функции calculate_total_price """

    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):

    """ Тест функции apply_discount """

    Item.pay_rate = 0.8

    assert item1.apply_discount() == 8000.0


def test_getter_name(item1):

    """ Тест property-getter """

    assert item1.name == "Смартфон"


def test_setter_name(item1):

    """ Тест property-setter """

    item1.name = "IPhone 13 Pro"
    assert item1.name == "IPhone 13 P"

    item1.name = "IPhone 13"
    assert item1.name == "IPhone 13"


def test_instantiate_from_csv():

    """ Тест функции instantiate_from_csv """

    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 0


def test_string_to_number():

    """ Тест статистического метода string_to_number """

    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_repr(item1):

    """ Тест метода repr """

    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):

    """ Тест метода str """

    assert str(item1) == "Смартфон"


def test_add(item1, phone1):

    """ Тест метода add """

    assert item1 + phone1 == 30