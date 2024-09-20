# cclf_1.py
import random
import sys
import sys
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

# Add the path of the folder where the module is located
sys.path.append("./utils/")
from utils import generate_files, dol
from utils import get_claims, get_beneficiaries, get_providers, get_diagnoses
from utils import icd, ctc, nprc, cbfc, csc, nhc, ffs, drg, cosc, cat, atc, csaic, cfc, cqc, claim_num, dt


# Capture arguments or default if not provided.
if len(sys.argv) == 3:
    # Capture arguments and convert them
    try:
        number_of_file_months = int(sys.argv[1])
    except ValueError as e:
        sys.exit(1)  # Exit with error code    
else:
    number_of_file_months = 1


# Prepare data structures for lookups.
clm = get_claims()
bene = get_beneficiaries()  
prov = get_providers()
diag = get_diagnoses()

# Create n days worth of files.
for month in range(number_of_file_months):
    # Initialize.
    delta = timedelta(days=month * 30)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    contents = ""

    for claim in clm:
        # Get a random memeficiary and provider.
        beneficiary = random.choice(bene)
        provider = random.choice(prov)

        # 1-10
        contents += claim["num"].ljust(13)              # CUR_CLM_UNIQ_ID
        contents += provider["oscar"]                   # PRVDR_OSCAR_NUM
        contents += beneficiary["mbi"]                  # BENE_MBI_ID
        contents += beneficiary["hic"].ljust(11)        # BENE_HIC_NUM
        contents += random.choice(ctc()).ljust(2)       # CLM_TYPE_CD
        contents += dt()                                # CLM_FROM_DT
        contents += dt()                                # CLM_THRU_DT
        contents += random.choice(cbfc())               # CLM_BILL_FAC_TYPE_CD
        contents += random.choice(csc())                # CLM_BILL_CLSFCTN_CD
        contents += random.choice(icd())["code"].rjust(7)     # PRNCPL_DGNS_CD

        # 11-20
        contents += random.choice(icd())["code"].rjust(7)     # ADMTG_DGNS_CD
        contents += random.choice(nprc()).ljust(2)      # CLM_MDCR_NPMT_RSN_CD
        contents += dol().rjust(17)                     # CLM_PMT_AMT
        contents += random.choice(nhc())                # CLM_NCH_PRMRY_PYR_CD
        contents += fake.state_abbr()                   # PRVDR_FAC_FIPS_ST_CD  
        contents += random.choice(ffs()).ljust(2)       # BENE_PTNT_STUS_CD 
        contents += random.choice(drg()).ljust(4)       # DGNS_DRG_CD
        contents += random.choice(cosc())               # CLM_OP_SRVC_TYPE_CD
        contents += random.choice(prov)["npi"]          # FAC_PRVDR_NPI_NUM
        contents += random.choice(prov)["npi"]          # OPRTG_PRVDR_NPI_NUM

        # 21-30
        contents += random.choice(prov)["npi"]          # ATNDG_PRVDR_NPI_NUM
        contents += random.choice(prov)["npi"]          # OTHR_PRVDR_NPI_NUM
        contents += random.choice(cat()).rjust(2)       # CLM_ADJSMT_TYPE_CD
        contents += dt()                                # CLM_EFCTV_DT
        contents += dt()                                # CLM_IDR_LD_DT
        contents += beneficiary["hic"].ljust(11)        # BENE_EQTBL_BIC_HICN_NUM
        contents += random.choice(atc()).rjust(2)       # CLM_ADMSN_TYPE_CD   
        contents += random.choice(csaic()).rjust(2)     # CLM_ADMSN_SRC_CD
        contents += random.choice(cfc())                # CLM_BILL_FREQ_CD
        contents += random.choice(cqc())                # CLM_QUERY_CD

        # 31-40
        contents += random.choice(icd())["ver"]         # DGNS_PRCDR_ICD_IND
        contents += dol().rjust(15)                     # CLM_MDCR_INSTNL_TOT_CHRG_AMT
        contents += dol().rjust(15)                     # CLM_MDCR_IP_PPS_CPTL_IME_AMT
        contents += dol().rjust(22)                     # CLM_OPRTNL_IME_AMT
        contents += dol().rjust(15)                     # CLM_MDCR_IP_PPS_DSPRPRTNT_AMT
        contents += dol().rjust(15)                     # CLM_HIPPS_UNCOMPD_CARE_AMT
        contents += dol().rjust(22)                     # CLM_OPRTNL_DSPRPRTNT_AMT
        contents += provider["oscar"].ljust(20)         # CLM_BLG_PRVDR_OSCAR_NUM
        contents += random.choice(prov)["fnpi"]         # CLM_BLG_PRVDR_NPI_NUM
        contents += random.choice(prov)["npi"]          # CLM_OPRTG_PRVDR_NPI_NUM

        # 41-45
        contents += random.choice(prov)["npi"]          # CLM_ATNDG_PRVDR_NPI_NUM
        contents += random.choice(prov)["npi"]          # CLM_OTHR_PRVDR_NPI_NUM
        contents += claim["ccn"].rjust(40)              # CLM_CNTL_NUM
        contents += claim["ocn"].rjust(40)              # CLM_ORG_CNTL_NUM
        contents += claim["mac"]                        # CLM_ORG_CNTL_NUM
        contents += "\n"

    generate_files("CCLF1", file_date, contents)
