import calendar
from faker import Faker
import datetime

faker = Faker()

def generate_fake_date(year, month):
    if not 1 <= month <= 12:
        raise ValueError("Invalid month. Month should be between 1 and 12.")
    _, last_day = calendar.monthrange(year, month)
    day = faker.random_int(min=1, max=last_day)
    return datetime.date(year, month, day)

fake_date = generate_fake_date(2023, 10)
print(fake_date)