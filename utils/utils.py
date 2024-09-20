# utils.py
import os
import random
import string
import pickle
import shutil

from faker import Faker
from datetime import timedelta

from claim_adjustment_type_code import get_codes as catc_get_codes
from claim_admission_type_code  import get_codes as actc_get_codes
from claim_bill_facility_type_code import get_codes as cbfc_get_codes
from claim_frequency_code import get_codes as cfc_get_codes
from claim_outpatient_service_type_code import get_codes as cosc_get_codes
from claim_query_code import get_codes as cqc_get_codes
from claim_service_classification_type_code import get_codes as csc_get_codes
from claim_source_inpatient_admission_code import get_codes as csaic_get_codes
from claim_type_code import get_codes as ctc_get_codes
from drg_code import get_codes as drg_get_codes
from ffs_patient_discharge_code import get_codes as ffs_get_codes
from icd import get_codes as icd_get_codes
from nhc_primary_payer_code import get_codes as nhc_get_codes
from reason_payment_code import get_codes as rpc_get_codes
from revenue_code_ffs import get_codes as revo_get_codes
from hcpcs import get_codes as hcpcs_get_codes
from hcpcs_mod import get_codes as hcpcs_mod_get_codes
from cpt import get_codes as cpt_get_codes
from cpt_mod import get_codes as cpt_mod_get_codes
from hipps import get_codes as hipps_get_codes

fake = Faker()

output_path = "./_output"
cache_path = f"{output_path}/cache"

# Purge output directory
def purge_output_folder():
    if not os.path.exists(output_path):
        return
    
    # Iterate through all files and folders in the directory
    for filename in os.listdir(output_path):
        file_path = os.path.join(output_path, filename)
        
        # Check if it's a file or directory
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)  # Remove the file or link
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)  # Remove the directory and its contents


def get_beneficiaries():
    if os.path.exists(f"{cache_path}/beneficiaries.pkl"):
        with open(f"{cache_path}/beneficiaries.pkl", 'rb') as f:
            return pickle.load(f)
        
    return {}    

def get_claims():
    if os.path.exists(f"{cache_path}/claims.pkl"):
        with open(f"{cache_path}/claims.pkl", 'rb') as f:
            return pickle.load(f)
        
    print("path does not exist")
    return {}   

def get_providers():
    if os.path.exists(f"{cache_path}/providers.pkl"):
        with open(f"{cache_path}/providers.pkl", 'rb') as f:
            return pickle.load(f)
        
    return {}   


# Claim Admission Type Codes
def atc():
    return actc_get_codes()

# Claim Adjustment Type Codes
def cat():
    return catc_get_codes()

# Claim Bill Facility Type Codes
def cbfc():
    return cbfc_get_codes()

# Claim Outpatient Service Type Codes
def cosc():
    return cosc_get_codes()

# Claim Service Classification Type Codes
def ctc():
    return ctc_get_codes()

# Claim Medicare Non-Payment Reason Codes
def nprc():
    return rpc_get_codes()

# Claim Service Classification Type Codes
def csc():
    return csc_get_codes()

# NCH Primary Payer Code (if not Medicare)
def nhc():
    return nhc_get_codes()

# FFS Patient Discharge Code
def ffs():
    return ffs_get_codes()

def icd():
    return icd_get_codes()

# CMS DRG / MSDRG Codes
def drg():
    return drg_get_codes()

def csaic():
    return csaic_get_codes()

def cfc():
    return cfc_get_codes()

def cqc():
    return cqc_get_codes()

def revcd():
    return revo_get_codes()

def hcpcs():
    return hcpcs_get_codes()

def hcpcsm():
    return hcpcs_mod_get_codes()

def cpt():
    return cpt_get_codes()

def cptm():
    return cpt_mod_get_codes()


def hipps():
    return hipps_get_codes()

# Returns a date this year in the format YYYY-MM-DD.
def dt():
    return fake.date_this_year().strftime("%Y-%m-%d")

# Returns a current numberic following the pattern (-)#.##.
def dol():
    return f"{random.uniform(-99, 9999):.2f}"

# Returns a float following the pattern #.####.
def flt():
    return f"{random.uniform(0, 9999):.4f}"

def claim_num(prefix, length):
    characters = string.ascii_letters + string.digits
    return prefix + ''.join(random.choices(characters, k=length - len(prefix))).upper()


def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_days = random.randint(0, time_between_dates.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

def random_alpha_string(length):
    characters = string.ascii_letters
    return ''.join(random.choices(characters, k=length)).upper()

def random_num_string(length):
    characters = string.digits
    return ''.join(random.choices(characters, k=length))

def random_alphanum_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length)).upper()

def random_int_in_range(min_value, max_value):
    return str(random.randint(min_value, max_value))

def random_int_by_len(length):
    characters = string.digits
    return ''.join(random.choices(characters, k=length))

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

def generate_files(type, date, contents):
    print(f"{type} for {date} processing...")

    # Describe the mapping between the file type and the ZC suffix.
    suffix_map = { 
        "CCLF1": "1", 
        "CCLF2": "2", 
        "CCLF3": "3", 
        "CCLF4": "4", 
        "CCLF5": "5", 
        "CCLF6": "6", 
        "CCLF7": "7", 
        "CCLF8": "8", 
        "CCLF9": "9", 
        "CCLFA": "A", 
        "CCLFB": "B", 
    }
    sfx = suffix_map[type]

    # Generate random characters to fill the filenames.
    rand_a = random_alpha_string(3)
    rand_b = random_alpha_string(2)

    # Define the filename patterns for the main types.
    primary_file_patterns = {
        f"P.A{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        # f"P.A{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        # f"P.F{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        # f"P.F{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        # f"P.D{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        # f"P.D{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        # f"P.K{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        # f"P.C{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        # f"P.P{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
    }

    # Define the path for the files.
    directory = f"./_output/{type}"
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # Emit the generated data for the primary file.
    for file in primary_file_patterns:
        print(f"\tCreating {type} {file}...")
        with open(f"{directory}/{file}", "w") as f:
            f.write(contents)  

    return
    # Define the filename patterns for the Summary Statistics.
    summary_file_patterns = {
        f"P.A{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.A{rand_a}.ACO.ZC0R{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC0R{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC0R{rand_b}.D{date}.T010203t",
        f"P.K{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.C{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.P{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",        
    }

    # Describe the mapping between the type and the name that will appear in the 
    # Summary Statistics.
    name_map = { 
        "CCLF1": "Part A Claims Header File.", 
        "CCLF2": "Part A Claims Revenue Center Detail File.", 
        "CCLF3": "Part A Procedure Code File.", 
        "CCLF4": "Part A Diagnosis Code File", 
        "CCLF5": "Part B Physicians File.", 
        "CCLF6": "Part B DME File.", 
        "CCLF7": "Part D File.", 
        "CCLF8": "Beneficiary Demographics File.", 
        "CCLF9": "BENE XREF File.", 
        "CCLFA": "Part A BE and Demo Codes File.", 
        "CCLFB": "Part B BE and Demo Codes File.", 
    }
    name = name_map[type]              

    # Emit data for the summary files.
    for file in summary_file_patterns:
        print(f"\tCreating CCLF0 {file}...")
        with open(f"{directory}/{file}", "w") as f:
            # Table 25
            f.write(f"{"123".ljust(13)}|{"WHATEVER".ljust(20)}|{"456".ljust(20)}|{"789".ljust(13)}\n")            

            # Table 26
            if file.startswith(("P.A", "P.F", "P.P")):
                f.write(f"{str(type).ljust(7)}|{name.ljust(43)}|{"456".ljust(11)}|{"789".ljust(5)}{str().ljust(1)}\n")
