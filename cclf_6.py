# cclf_6.py
import random
import sys
import sys
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

# Add the path of the folder where the module is located
sys.path.append("./utils/")
from utils import dol, generate_files
from utils import get_claims, get_bene, get_prov
from utils import ctc, tsc, pos, hcpcs, ppc, cpd, pic, cat, cdc, tsc

# Capture arguments or default if not provided.
if len(sys.argv) == 2:
    # Capture arguments and convert them
    try:
        number_of_file_months = int(sys.argv[1])
    except ValueError as e:
        sys.exit(1)  # Exit with error code    
else:
    number_of_file_months = 1

# Prepare data structures for lookups.
claims = get_claims()

# Create n days worth of files.
for month in range(number_of_file_months):
    # Initialize.
    delta = timedelta(days=month * 30)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    contents = ""

    # Enumerate the claims
    for claim in claims:

        # Enumerate the claim lines.
        for claim_line in claim["lines"]:

            # Get the beneficiary and NPI provider.
            bene = get_bene(claim["mbi"])
            prov = get_prov(claim["npi"])

            # 1-10
            contents += claim["num"].ljust(13)          # CUR_CLM_UNIQ_ID
            contents += claim_line["ln"].rjust(10)      # CLM_LINE_NUM
            contents += claim["mbi"]                    # BENE_MBI_ID
            contents += "".ljust(11)                    # BENE_HIC_NUM
            contents += random.choice(ctc()).ljust(2)   # CLM_TYPE_CD
            contents += claim["from_dt"]                # CLM_FROM_DT
            contents += claim["thru_dt"]                # CLM_THRU_DT
            contents += random.choice(tsc())            # CLM_FED_TYPE_SRVC_CD
            contents += random.choice(pos())            # CLM_POS_CD
            contents += claim_line["from_dt"]           # CLM_LINE_FROM_DT

            # 11-20
            contents += claim_line["thru_dt"]           # CLM_LINE_THRU_DT   
            contents += random.choice(hcpcs())          # CLM_LINE_HCPCS_CD
            contents += str(dol()).rjust(15)            # CLM_LINE_CVRD_PD_AMT
            contents += random.choice(ppc()).ljust(1)   # CLM_PRMRY_PYR_CD
            contents += prov["npi"]                     # PAYTO_PRVDR_NPI_NUM
            contents += prov["npi"]                     # ORDRG_PRVDR_NPI_NUM
            contents += random.choice(cpd()).ljust(2)   # CLM_CARR_PMT_DNL_CD
            contents += random.choice(pic()).ljust(2)   # CLM_PRCSG_IND_CD
            contents += random.choice(cat()).ljust(2)   # CLM_ADJSMT_TYPE_CD
            contents += claim["from_dt"]                # CLM_EFCTV_DT
            
            # 21-27
            contents += claim["thru_dt"]                # CLM_IDR_LD_DT
            contents += claim["ccn"].rjust(40)          # CLM_CNTL_NUM
            contents += "".ljust(11)                    # BENE_EQTBL_BIC_HICN_NUM
            contents += str(dol()).rjust(17)            # CLM_LINE_ALOWD_CHRG_AMT
            contents += random.choice(cdc()).ljust(2)   # CLM_DISP_CD
            contents += prov["npi"]                     # CLM_BLG_PRVDR_NPI_NUM
            contents += prov["npi"]                     # CLM_RFRG_PRVDR_NPI_NUM

            contents += "\n"

    generate_files("CCLF6", file_date, contents)        