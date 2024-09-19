# utils.py

import random
import string
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_days = random.randint(0, time_between_dates.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

def random_alpha_string(length):
    characters = string.ascii_letters
    return ''.join(random.choices(characters, k=length)).upper()

def random_alphanum_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length)).upper()

def random_int_in_range(min_value, max_value):
    return str(random.randint(min_value, max_value))

def random_int_by_len(length):
    characters = string.digits
    return ''.join(random.choices(characters, k=length))



# Random integer between a and b (inclusive)
def random_int_in_range_with_sign(a, b):
    sign = random.choice([-1, 1])
    return (random.randint(a, b) * sign)

# Random float between a and b
def random_float_in_range(a, b, length):
    # Generate a random float between a and b
    random_float = random.uniform(a, b)
    # Randomly decide whether to make it positive or negative
    sign = random.choice([-1, 1])
    # Apply the sign and round to 2 decimal places
    return str(round(random_float * sign, 2)).ljust(length)    

def random_choice_from_array(arr):
    return random.choice(arr)
