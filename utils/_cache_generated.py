from datetime import date, timedelta
import os
import pickle
import random
from faker import Faker
from utils import psc, brc

fake = Faker()

output_path = "./_output"
cache_path = f"{output_path}/cache"

beneficiaries = {}
providers = {}
claims = []


def cache_all(number_of_beneficiaries, number_of_claims, number_of_providers):
    print("Caching:")
    cache_beneficiaries(number_of_beneficiaries)
    cache_providers(number_of_providers)
    cache_claims(number_of_claims)

def cache_beneficiaries(number_of_beneficiaries):
    print(f"\tBeneficiaries {number_of_beneficiaries}...")
    generate_beneficiaries(number_of_beneficiaries)
    cache_data("beneficiaries", beneficiaries)

def cache_providers(number_of_providers):
    print(f"\tProvidesr {number_of_providers}...")
    generate_providers(number_of_providers)
    cache_data("providers", providers)    

def cache_claims(number_of_claims):
    print(f"\tClaims {number_of_claims}...")
    generate_claims(number_of_claims)
    cache_data("claims", claims)


def generate_beneficiaries(quantity):
    today = date.today()
    for _ in range(quantity):

        dob = fake.date_of_birth(minimum_age=55, maximum_age=105)
        dod = fake.date_of_birth(minimum_age=1, maximum_age=15)
        age = today.year - dob.year
        
        person = {
            "mbi": random_mbi(),
            "hic": "",

            "firstName": fake.first_name(),
            "middleName": fake.first_name(),
            "lastName": fake.last_name(),
            "gender": random.choice(["0", "1", "U"]),
            "dob": dob.strftime("%Y-%m-%d"),
            "dod": dod.strftime("%Y-%m-%d"),
            "age": str(age),
            "race": random.choice(brc()),
            
            "address1": fake.street_address(),
            "address2": fake.secondary_address(),
            "address3": fake.secondary_address(),
            "address4": fake.secondary_address(),
            "address5": fake.secondary_address(),
            "address6": fake.secondary_address(),
            "city": fake.city(),
            "county": fake.country()[:3].upper(),
            "state": fake.state_abbr(),
            "zipCode": fake.postcode(),
            "plus4": fake.postalcode_plus4()[-4:]
        }
        
        beneficiaries[person["mbi"]] = person


def generate_providers(quantity):
    for _ in range(quantity):
        provider = {
            "npi": "".join(random.choices("0123456789", k=10)),     # NPI
            "fnpi": "".join(random.choices("0123456789", k=10)),    # Facility NPI
            "oscar": "".join(random.choices("0123456789", k=6)),    # OSCAR/CCN
            "psc": random.choice(psc()),
            "ein": fake.ein(),
            
            "firstName": fake.first_name(),
            "middleName": fake.first_name(),
            "lastName": fake.last_name(),
            "gender": random.choice(["0", "1", "U"]),
            "dob": fake.date_of_birth(minimum_age=55, maximum_age=105),

            "address1": fake.street_address(),
            "address2": fake.secondary_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zipCode": fake.postcode(),
            "plus4": fake.postalcode_plus4()[-4:]
        }
        
        providers[provider["npi"]] = provider



def generate_claims(quantity):
    pad_size = 1 + len(str(quantity))

    for index in range(quantity):

        # Prepare the claim
        nul = f"CN{str(index + 1).zfill(pad_size)}"
        cd = fake.date_this_year()
        bene = random.choice(list(beneficiaries.values()))
        prov = random.choice(list(providers.values()))

        # Generate between 1 and 5 claim lines.
        for ln in range(1, random.randint(1, 5)):
            claim = {
                "num": nul,
                "ln": f"{ln}",
                "ccn": fake.numerify("A#######"),
                "ocn": fake.numerify("B#######"),
                "mac": fake.numerify("MC###"),
                "from_dt": cd.strftime("%Y-%m-%d"),
                "thru_dt": (cd + timedelta(days=random.randint(0, 7))).strftime("%Y-%m-%d"),

                # Assign the member.
                "mbi": bene["mbi"],

                # TODO: Assign different NPIs based on billing, rendering...
                "npi": prov["npi"]
            }

            claims.append(claim)


# Cache data with key.
def cache_data(key, data):
    if not os.path.exists(cache_path):
        os.makedirs(cache_path, exist_ok=True)

    cache_file_path = f"{cache_path}/{key}.pkl"
    with open(f"{cache_file_path}", 'wb') as f:
        pickle.dump(data, f)

   
# Define the characters that can be used for each element of an MBI.
c = "123456789"
n = "0123456789"
an = "AN"
a = "ACDEFGHJKMNPQRTUVWXY"

def random_mbi():
    return f"{random.choice(c)}{random.choice(a)}{random.choice(an)}{random.choice(n)}{random.choice(a)}{random.choice(an)}{random.choice(n)}{random.choice(a)}{random.choice(a)}{random.choice(n)}{random.choice(n)}"
