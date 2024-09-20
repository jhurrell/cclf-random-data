# cclf_2.py
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
from utils import ctc, revcd, dt, hcpcs, flt, hcpcsm, hipps

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

        # 1-10
        contents += claim["num"].ljust(13)              # CUR_CLM_UNIQ_ID
        contents += claim["ln"].rjust(10)               # CLM_LINE_NUM
        contents += claim["mbi"]                        # BENE_MBI_ID
        contents += "".ljust(11)                        # BENE_HIC_NUM
        contents += random.choice(ctc()).rjust(2)       # CLM_TYPE_CD
        contents += claim["from_dt"]                    # CLM_LINE_FROM_DT
        contents += claim["thru_dt"]                    # CLM_LINE_THRU_DT
        contents += random.choice(revcd()).rjust(4)     # CLM_LINE_PROD_REV_CTR_CD
        contents += dt()                                # CLM_LINE_INSTNL_REV_CTR_DT   
        contents += random.choice(hcpcs())              # CLM_LINE_HCPCS_CD
  
        # # 11-20
        contents += "".ljust(11)                        # BENE_EQTBL_BIC_HICN_NUM
        contents += pr["oscar"].ljust(6)                # PRVDR_OSCAR_NUM
        contents += claim["from_dt"]                    # CLM_FROM_DT
        contents += claim["thru_dt"]                    # CLM_THRU_DT       
        contents += flt().rjust(24)                     # CLM_LINE_SRVC_UNIT_QTY
        contents += flt().rjust(17)                     # CLM_LINE_CVRD_PD_AMT
        contents += random.choice(hcpcsm())             # HCPCS_1_MDFR_CD
        contents += random.choice(hcpcsm())             # HCPCS_2_MDFR_CD
        contents += random.choice(hcpcsm())             # HCPCS_3_MDFR_CD
        contents += random.choice(hcpcsm())             # HCPCS_4_MDFR_CD

        # # 21-23
        contents += random.choice(hcpcsm())             # HCPCS_5_MDFR_CD
        contents += random.choice(hipps()).rjust(5)     # CLM_REV_APC_HIPPS_CD
        contents += pr["oscar"].rjust(20)               # CLM_FAC_PRVDR_OSCAR_NUM

        contents += "\n"

    generate_files("CCLF2", file_date, contents)        