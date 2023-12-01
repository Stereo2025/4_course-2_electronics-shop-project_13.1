import csv


class InstantiateCSVError(Exception):
    pass


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
        cls.all.clear()
        try:
            with open(path, 'r', encoding="windows-1251") as csv_file:
                csv_data: csv.DictReader = csv.DictReader(csv_file)
                csv_data_list = list(csv_data)
                for line in csv_data_list:
                    if len(line) < 3 or (line.get('name') and line.get('price') and line.get('quantity')) in ['', None]:
                        raise InstantiateCSVError('Ошибка при создании объектов из CSV')

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")
        except InstantiateCSVError as exception:
            raise InstantiateCSVError(exception.args[0])
        else:
            return True

    @staticmethod
    def string_to_number(value):
        return int(float(value))
