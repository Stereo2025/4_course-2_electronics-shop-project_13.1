from src.item import Item


class Phone(Item):
    def __init__(self, name, price: float, quantity: int, sim_number: int) -> None:
        super().__init__(name, price, quantity)
        self.__sim_number = sim_number

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__sim_number})"

    @property
    def number_of_sim(self):
        return self.__sim_number

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        if new_number < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self.__sim_number = new_number
