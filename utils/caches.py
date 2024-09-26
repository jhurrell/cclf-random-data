import datetime
import os
import pickle
import random
import calendar
from datetime import date, timedelta
from faker import Faker
from utils import psc, brc, fips_county, fips_state

faker = Faker()

output_path = "./_output"
cache_path = f"{output_path}/cache"

beneficiaries = {}
providers = {}
claims = []


def cache_all(number_of_beneficiaries, number_of_providers, number_of_claims, claims_year, claims_month):
    print("Creating Fake Data:")
    cache_beneficiaries(number_of_beneficiaries)
    cache_providers(number_of_providers)
    cache_claims(number_of_claims, claims_year, claims_month)

def cache_beneficiaries(number_of_beneficiaries):
    print(f"\tBeneficiaries: {number_of_beneficiaries}")
    generate_beneficiaries(number_of_beneficiaries)
    cache_data("beneficiaries", beneficiaries)

def cache_providers(number_of_providers):
    print(f"\tProviders: {number_of_providers}")
    generate_providers(number_of_providers)
    cache_data("providers", providers)    

def cache_claims(number_of_claims, claims_year, claims_month):
    print(f"\tClaims: {number_of_claims}")
    generate_claims(number_of_claims, claims_year, claims_month)
    cache_data("claims", claims)


def generate_beneficiaries(quantity):
    today = date.today()
    for _ in range(quantity):

        dob = faker.date_of_birth(minimum_age=55, maximum_age=105)
        dod = faker.date_of_birth(minimum_age=1, maximum_age=5)
        age = today.year - dob.year
        
        person = {
            "mbi": random_mbi(),
            "hic": "",

            "firstName": faker.first_name(),
            "middleName": faker.first_name(),
            "lastName": faker.last_name(),
            "gender": random.choice(["0", "1", "U"]),
            "dob": dob.strftime("%Y-%m-%d"),
            "dod": dod.strftime("%Y-%m-%d"),
            "age": str(age),
            "race": random.choice(brc()),
            
            "address1": faker.street_address(),
            "address2": faker.secondary_address(),
            "address3": faker.secondary_address(),
            "address4": faker.secondary_address(),
            "address5": faker.secondary_address(),
            "address6": faker.secondary_address(),
            "city": faker.city(),
            "county": faker.country()[:3].upper(),
            "state": faker.state_abbr(),
            "fips_state": random.choice(fips_state()),
            "fips_county": random.choice(fips_county()),
            "zipCode": faker.postcode(),
            "plus4": faker.postalcode_plus4()[-4:]
        }
        
        beneficiaries[person["mbi"]] = person


def generate_providers(quantity):
    for _ in range(quantity):
        provider = {
            "npi": "".join(random.choices("0123456789", k=10)),     # NPI
            "fnpi": "".join(random.choices("0123456789", k=10)),    # Facility NPI
            "oscar": "".join(random.choices("0123456789", k=6)),    # OSCAR/CCN
            "psc": random.choice(psc()),
            "ein": faker.ein(),
            
            "firstName": faker.first_name(),
            "middleName": faker.first_name(),
            "lastName": faker.last_name(),
            "gender": random.choice(["0", "1", "U"]),
            "dob": faker.date_of_birth(minimum_age=55, maximum_age=105),

            "address1": faker.street_address(),
            "address2": faker.secondary_address(),
            "city": faker.city(),
            "state": faker.state_abbr(),
            "zipCode": faker.postcode(),
            "plus4": faker.postalcode_plus4()[-4:]
        }
        
        providers[provider["npi"]] = provider


def generate_claims(quantity, claims_year, claims_month):

    pad_size = 1 + len(str(quantity))


    for ic in range(quantity):

        # Prepare the claim
        claim_number = ic + 1
        num = f"{claims_year}{claims_month:02}{str(claim_number).zfill(pad_size)}"
        cd = get_date_in_month(claims_year, claims_month)
        bene = random.choice(list(beneficiaries.values()))
        prov = random.choice(list(providers.values()))

        claim = {
            "num": num,
            "ccn": faker.numerify("A#######"),
            "ocn": faker.numerify("B#######"),
            "mac": faker.numerify("MC###"),
            "from_dt": cd.strftime("%Y-%m-%d"),
            "thru_dt": (cd + timedelta(days=random.randint(0, 7))).strftime("%Y-%m-%d"),
            "mbi": bene["mbi"],
            "npi": prov["npi"],
            "lines": []
        }

        # Generate between 1 and 5 claim lines per claim.
        for icl in range(1, random.randint(1, 5)):
            cld = (cd + timedelta(days=random.randint(0, 7)))
            line = {
                "ln": f"{icl}",
                "from_dt": cld.strftime("%Y-%m-%d"),
                "thru_dt": cld.strftime("%Y-%m-%d"),
            }

            claim["lines"].append(line)

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

def get_date_in_month(year, month):
    if not 1 <= month <= 12:
        raise ValueError("Invalid month. Month should be between 1 and 12.")
    _, last_day = calendar.monthrange(year, month)
    day = faker.random_int(min=1, max=last_day)
    return datetime.date(year, month, day)