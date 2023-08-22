from src.item import Item


class MixinLog():

    """ Дополнительный функционал по хранению и изменению раскладки клавиатуры """

    def __init__(self, name, price, quantity, language="EN"):

        """ Создание экземпляра класса MixinLog """

        super().__init__(name, price, quantity)
        self.__language = language


    @property
    def language(self):

        return self.__language


    def __str__(self):

        """ Метод, который выводит информацию для пользователей """

        return self.language


class Keyboard(MixinLog, Item):

    """ Дочерний класс для товара "клавиатура", который содержит в
    себе все атрибуты класса Item и дополнительный атрибут язык """

    def __init__(self, name, price, quantity):

        """ Создание экземпляров класса Keyboard """

        super().__init__(name, price, quantity)


    def change_lang(self):

        """ Метод для изменения языка клавиатуры """

        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"

        return self


    def __str__(self):

        """ Метод, который выводит информацию для пользователей """

        return self.name