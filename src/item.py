import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Ошибка при создании объектов из CSV'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        if len(name_str) > 10:
            self.__name = name_str
        else:
            self.__name = name_str[:10]

    @classmethod
    def instantiate_from_csv(cls, path):

        if Item.instantiate_from_csv_test(path) is True:
            Item.all = []

            with open(path, 'r', encoding="windows-1251") as csv_file:
                csv_data: csv.DictReader = csv.DictReader(csv_file)
                for line in csv_data:
                    cls(line['name'], float(line['price']), int(line['quantity']))

    @staticmethod
    def string_to_number(value):
        return int(float(value))

    @staticmethod
    def instantiate_from_csv_test(path):

        try:
            with open(path, 'r', encoding="windows-1251") as csv_file:
                csv_data: csv.DictReader = csv.DictReader(csv_file)
                csv_data_list = list(csv_data)
                for line in csv_data_list:
                    if (line.get('name') and line.get('price') and line.get('quantity')) in ['', None]:
                        raise InstantiateCSVError
        except FileNotFoundError:
            return 'Отсутствует файл invalid_items_test.csv'
        except InstantiateCSVError as exeption:
            return exeption.message
        else:
            return True