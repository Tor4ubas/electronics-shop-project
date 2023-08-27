import csv
from src.instantiatecsverror import InstantiateCSVError


class Item:

    """
    Класс для представления товара в магазине.
    """


    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:

        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


    def calculate_total_price(self) -> float:

        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """

        all_price = self.price * self.quantity

        return all_price


    def apply_discount(self) -> None:

        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate

        return self.price


    @property
    def name(self):

        """ Метод геттер для name, используя @property """

        return self.__name


    @name.setter
    def name(self, value):

        """ Метод сеттер, где проверяем, что длина наименования товара
        не больше 10 символов. Если больше, то обрезаем строку до первых 10 символов"""

        self.__name = value

        if len(value) > 10:
            self.__name = value[:11]
        else:
            self.__name = value


    @classmethod
    def instantiate_from_csv(cls):

        """ Класс-метод, инициализирующий экземпляры класса Item
        данными из файла src/items.csv """


        cls.all = []

        try:
            with open("../src/items.csv", "rt", newline="", encoding="cp1251") as csv_file:

                reader = csv.DictReader(csv_file)

                for object in reader:
                    objects = cls(object["name"], object["price"], object["quantity"])
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл item.csv")
        except KeyError:
            print("InstantiateCSVError: Файл item.csv поврежден")




    @staticmethod
    def string_to_number(number):

        """ Статический метод, возвращающий число из числа-строки """

        return int(float(number))


    def __repr__(self):

        """ Метод, который выводит ифнормацию для разработиков """

        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):

        """ Метод, который выводит информацию для пользователей """

        return self.__name


    def __add__(self, other):

        """ Метод сложения количества товаров двух классов """

        if not isinstance(other, Item):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            return self.quantity + other.quantity
