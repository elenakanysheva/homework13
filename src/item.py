import csv
from pathlib import Path
from abc import ABC


class InstantiateCSVError(Exception):
    def __init__(self, item):
        self.item = item
        if "name" not in self.item or "quantity" not in self.item or "price" not in self.item:
            raise Exception('Файл item.csv поврежден')


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
        self.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        """Складывает экземпляры классов `Phone` и `Item` по количеству товара в магазине"""
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    # Геттер для name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data_string):
        if len(data_string) > 10:
            self.__name = data_string[:10]
        else:
            self.__name = data_string

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        file = Path(__file__).parent / 'items.csv'
        try:
            f = open(file)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        else:
            with open(file, encoding="windows-1251") as f:
                DictReader_obj = csv.DictReader(f)
                for item in DictReader_obj:
                    try:
                        inst_csv = InstantiateCSVError(item)
                    except Exception as ex:
                        print(ex)
                        break
                    else:
                        cls(item["name"], item["price"], item["quantity"])

    @staticmethod
    def string_to_number(string):
        return int(float(string))
