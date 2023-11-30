from pathlib import Path

Parent_ = Path(__file__).resolve().parent.parent
Csv_path = Path.joinpath(Parent_, "src", "items.csv")
Csv_test = Path.joinpath(Parent_, "tests", "invalid_items_test.csv")
No_file = Path.joinpath(Parent_, "src", "items_.csv")
