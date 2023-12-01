from src.item import Item
from src.paths import Csv_path, No_file

if __name__ == '__main__':
    # Файл invalid_items_test.csv отсутствует.
    Item.instantiate_from_csv(Csv_path)  # ----- >  No_file
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле invalid_items_test.csv удалена последняя колонка.
    Item.instantiate_from_csv(Csv_path)
    # InstantiateCSVError: Файл item.csv поврежден
