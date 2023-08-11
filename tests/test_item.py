from src.item import Item
import pytest

@pytest.fixture
def item1():

    """ Экземпляр класса в фикстуре """

    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(item1):
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount(item1) -> None:

    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 10000
    assert item2.price == 20000

def test_string_to_number():
    #assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_name(item1):
    item = Item('Смартфон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

def test_repr(item1):

    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):

    assert str(item1) == "Смартфон"
