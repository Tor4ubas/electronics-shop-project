import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        """
        Создание экземпляра класса item.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        cls.all = []  # Сбросить список перед загрузкой новых данных
        with open('C:/Users/User/PycharmProjects/electronics-shop-project/src/items.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                item = cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        """
        Возвращает число из числа-строки.
        """
        return int(float(number))

#print(Item.string_to_number('5'))
#print(Item.string_to_number('5.0'))
#print(Item.string_to_number('5.5'))

        #Item.instantiate_from_csv()
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"


    def __str__(self):
        return self._name
