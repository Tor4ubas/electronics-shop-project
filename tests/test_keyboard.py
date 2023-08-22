import pytest
from src.keyboard import Keyboard
from src.keyboard import MixinLog


@pytest.fixture()
def keyboard1():

    """ Экземпляр класса в фикстуре """

    return Keyboard('Dark Project KD87A', 9600, 5)


@pytest.fixture()
def language1():

    """ Язык по умолчанию в фикстуре """

    language = "EN"

    return language


def test_str(keyboard1, language1):

    """ Тест метода MixinLog """

    assert str(language1) == "EN"


def test_change_lang(keyboard1, language1):

    """ Тесты функции change_lang """

    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"
    keyboard1.change_lang()
    assert str(keyboard1.language) == "EN"


def test_str(keyboard1):

    """ Тест метода str """

    assert str(keyboard1) == "Dark Project KD87A"