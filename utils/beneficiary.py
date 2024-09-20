import random
import functools
from faker import Faker
fake = Faker()

# Define the characters that can be used for each element of an MBI.
c = "123456789"
n = "0123456789"
an = "AN"
a = "ACDEFGHJKMNPQRTUVWXY"

def random_mbi():
    return f"{random.choice(c)}{random.choice(a)}{random.choice(an)}{random.choice(n)}{random.choice(a)}{random.choice(an)}{random.choice(n)}{random.choice(a)}{random.choice(a)}{random.choice(n)}{random.choice(n)}"

# Cache the results of the generate_mbis function to improve performance and to
# support sharing the same generated MBIs across multiple calls to the function.
@functools.lru_cache(maxsize=None)  # maxsize=None means unlimited cache
def generate_beneficiaries(quantity):
    people = []
    for _ in range(quantity):

        person = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "gender": random.choice(["0", "1", "U"]),
            "dateOfBirth": fake.date_of_birth(minimum_age=55, maximum_age=105),
            "mbi": random_mbi(),
            "hic": "",
            "address1": fake.street_address(),
            "address2": fake.secondary_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zipCode": fake.postcode(),
            "plus4": fake.postalcode_plus4()[-4:]
        }
        
        people.append(person)

    return people
