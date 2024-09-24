# utils.py
import datetime
import os
import random
import pickle
import shutil
import sys
sys.path.append("./utils/reference")

from faker import Faker
from functools import lru_cache

from beneficiary_dual_status import get_codes as bdsc_get_codes
from beneficiary_entitlement_buy_in_indicator import get_codes as bebi_get_codes
from beneficiary_medicare_status import get_codes as bmcsc_get_codes
from beneficiary_original_entitlement_reason_code import get_codes as beorcc_get_codes
from beneficiary_race import get_codes as brc_get_codes
from carrier_payment_denial import get_codes as cpd_get_codes
from claim_adjustment_type import get_codes as catc_get_codes
from claim_admission_type  import get_codes as actc_get_codes
from claim_bill_facility_type import get_codes as cbfc_get_codes
from claim_dispensing import get_codes as cdsc_get_codes
from claim_disposition import get_codes as cdc_get_codes
from claim_frequency import get_codes as cfc_get_codes
from claim_outpatient_service_type import get_codes as cosc_get_codes
from claim_product_type import get_codes as ptc_get_codes
from claim_query import get_codes as cqc_get_codes
from claim_service_classification_type import get_codes as csc_get_codes
from claim_source_inpatient_admission import get_codes as csaic_get_codes
from claim_type import get_codes as ctc_get_codes
from cpt import get_codes as cpt_get_codes
from cpt_mod import get_codes as cpt_mod_get_codes
from daw_product_selection import get_codes as daw_get_codes
from drg import get_codes as drg_get_codes
from ffs_patient_discharge import get_codes as ffs_get_codes
from hcpcs import get_codes as hcpcs_get_codes
from hcpcs_mod import get_codes as hcpcs_mod_get_codes
from hipps import get_codes as hipps_get_codes
from icd import get_codes as icd_get_codes
from nhc_primary_payer import get_codes as nhc_get_codes
from pharmacy_service_type import get_codes as pstc_get_codes
from place_of_service import get_codes as pos_get_codes
from present_on_admission import get_codes as poa_get_codes
from primary_payer import get_codes as ppc_get_codes
from processing_indicator import get_codes as pic_get_codes
from provider_service_identifier_qualifier import get_codes as psiqc_get_codes
from provider_specialty import get_codes as psc_get_codes
from reason_payment import get_codes as rpc_get_codes
from rendering_provider_type import get_codes as rptc_get_codes
from revenue_code import get_codes as revo_get_codes
from type_service import get_codes as tsc_get_codes

faker = Faker()

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


@lru_cache(maxsize=None)
def get_beneficiaries():
    if os.path.exists(f"{cache_path}/beneficiaries.pkl"):
        with open(f"{cache_path}/beneficiaries.pkl", 'rb') as f:
            return pickle.load(f)
        
    return {}    


@lru_cache(maxsize=None)
def get_claims():
    if os.path.exists(f"{cache_path}/claims.pkl"):
        with open(f"{cache_path}/claims.pkl", 'rb') as f:
            return pickle.load(f)
        
    return {}   


@lru_cache(maxsize=None)
def get_providers():
    if os.path.exists(f"{cache_path}/providers.pkl"):
        with open(f"{cache_path}/providers.pkl", 'rb') as f:
            return pickle.load(f)
        
    return {}   


def get_bene(mbi):
    beneficiaries = get_beneficiaries()
    return beneficiaries[mbi]

def get_prov(npi):
    providers = get_providers()
    return providers[npi]


def bdsc():
    return bdsc_get_codes()

def bebi():
    return bebi_get_codes()

def bmsc():
    return bmcsc_get_codes()

def beorcc():
    return beorcc_get_codes()

def brc():
    return brc_get_codes()

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

def cptc():
    return ptc_get_codes()

def poa():
    return poa_get_codes()

def rpt():
    return rptc_get_codes()

def psc():
    return psc_get_codes()

def tsc():
    return tsc_get_codes()

def pos():
    return pos_get_codes()

def ppc():
    return ppc_get_codes()

def cdc():
    return cdc_get_codes()

# Returns a date this year in the format YYYY-MM-DD.
def dt():
    return faker.date_this_year().strftime("%Y-%m-%d")

# Returns a current numberic following the pattern (-)#.##.
def dol():
    return f"{random.uniform(-99, 9999):.2f}"

# Returns a float following the pattern #.####.
def flt():
    return f"{random.uniform(0, 9999):.4f}"

def cpd():
    return cpd_get_codes()

def pic():
    return pic_get_codes()

def ndc():
    return faker.numerify("###########")

def psiqc():
    return psiqc_get_codes()

def cdsc():
    return cdsc_get_codes()

def daw():
    return daw_get_codes()

def rint():
    return str(random.randint(1, 365))

def pstc():
    return pstc_get_codes()

def ynb():
    return random.choice(["Y", "N", " "])

def twobyte():
    return f"{random.randint(0, 255):02X}"

def replicate_files(type, date):
    print(f"{type} for {date} processing...")

    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    date = date.strftime("%y%m%d")
    print(date)


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
    rand_a = faker.pystr(min_chars=3, max_chars=3)
    rand_b = faker.pystr(min_chars=2, max_chars=2)

    # Define the filename patterns for the main types.
    primary_file_patterns = {
        f"P.A{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.A{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.K{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.C{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.P{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
    }

    # Define the output path for the files.
    output_dir = f"./_output/{date}/{type}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # Emit the generated data for the primary file.
    for file in primary_file_patterns:
        output_file = f"{output_dir}/{file}"
        print(f"\tCreating {type} {file}...")
        shutil.copy(f"{cache_path}/{type}.txt", output_file)


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
        with open(f"{output_dir}/{file}", "w") as f:
            # Table 25
            f.write(f"{"123".ljust(13)}|{"WHATEVER".ljust(20)}|{"456".ljust(20)}|{"789".ljust(13)}\n")            

            # Table 26
            if file.startswith(("P.A", "P.F", "P.P")):
                f.write(f"{str(type).ljust(7)}|{name.ljust(43)}|{"456".ljust(11)}|{"789".ljust(5)}{str().ljust(1)}\n")          
               


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
    rand_a = faker.pystr(min_chars=3, max_chars=3)
    rand_b = faker.pystr(min_chars=2, max_chars=2)

    # Define the filename patterns for the main types.
    primary_file_patterns = {
        f"P.A{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.A{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.K{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.C{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.P{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
    }

    # Define the path for the files.
    directory = f"./_output/{type}"
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # Emit the generated data for the primary file.
    for file in primary_file_patterns:
        print(f"\tCreating {type} {file}...")
        with open(f"{directory}/{file}", "w") as f:
            f.write(contents.rstrip())  

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
