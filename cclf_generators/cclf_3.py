# cclf_3.py
import random
import sys
import sys
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

# Add the path of the folder where the module is located
sys.path.append("./utils/")
from utils import generate_files
from utils import get_claims, get_beneficiaries, get_providers
from utils import ctc, icd

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
clm = get_claims()
bene = get_beneficiaries()  
prov = get_providers()

# Create n days worth of files.
for month in range(number_of_file_months):
    # Initialize.
    delta = timedelta(days=month * 30)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    contents = ""

    for claim in clm:
        pr = random.choice(prov)
        diag = random.choice(icd())

        # 1-10
        contents += claim["num"].ljust(13)          # CUR_CLM_UNIQ_ID
        contents += claim["mbi"]                    # BENE_MBI_ID
        contents += "".ljust(11)                    # BENE_HIC_NUM
        contents += random.choice(ctc()).rjust(2)   # CLM_TYPE_CD
        contents += "1".rjust(2)                    # CLM_VAL_SQNC_NUM
        contents += diag["code"].rjust(7)           # CLM_PRCDR_CD
        contents += claim["from_dt"]                # CLM_PRCDR_PRFRM_DT
        contents += "".ljust(11)                    # BENE_EQTBL_BIC_HICN_NUM
        contents += pr["oscar"].ljust(6)            # PRVDR_OSCAR_NUM
        contents += claim["from_dt"]                # CLM_FROM_DT

        # 11-13
        contents += claim["thru_dt"]                # CLM_THRU_DT   
        contents += diag["ver"]                     # DGNS_PRCDR_ICD_IND
        contents += pr["fnpi"].rjust(20)            # CLM_BLG_PRVDR_OSCAR_NUM

        contents += "\n"

    generate_files("CCLF3", file_date, contents)        