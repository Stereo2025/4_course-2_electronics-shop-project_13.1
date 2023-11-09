from pathlib import Path

Parent_ = Path(__file__).resolve().parent.parent
Csv_path = Path.joinpath(Parent_, "src", "items.csv")
