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
from utils import ctc, cdsc, ndc, psiqc, daw, flt, rint, cat, pstc

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

    for claim in claims:

        # Get the beneficiary and NPI provider.
        bene = get_bene(claim["mbi"])
        prov = get_prov(claim["npi"])

        # 1-10
        contents += claim["num"].ljust(13)          # CUR_CLM_UNIQ_ID
        contents += claim["mbi"]                    # BENE_MBI_ID
        contents += "".ljust(11)                    # BENE_HIC_NUM
        contents += ndc()                           # CLM_LINE_NDC_CD
        contents += random.choice(ctc()).ljust(2)   # CLM_TYPE_CD
        contents += claim["from_dt"]                # CLM_FROM_DT
        contents += random.choice(psiqc())          # PRVDR_SRVC_ID__QLFYR_CD
        contents += prov["npi"].ljust(20)           # CLM_SRVC_PRVDR_GNRC_ID_NUM
        contents += random.choice(cdsc())           # CLM_DSPNSNG_STUS_CD
        contents += random.choice(daw())            # CLM_DAW_PROD_SLCTN_CD
        
        # 11-20
        contents += flt().rjust(24)                 # CLM_LINE_SRVC_UNIT_QTY
        contents += rint().rjust(9)                 # CLM_LINE_DAYS_SUPLY_QTY
        contents += random.choice(psiqc())          # PRVDR_PRSBNG_ID_QLFYR_CD
        contents += prov["npi"].ljust(20)           # CLM_PRSBNG_PRVDR_GNRC_ID_NUM
        contents += dol().rjust(13)                 # CLM_LINE_BENE_PMT_AMT
        contents += random.choice(cat()).ljust(2)   # CLM_ADJSMT_TYPE_CD
        contents += claim["from_dt"]                # CLM_EFCTV_DT
        contents += claim["thru_dt"]                # CLM_IDR_LD_DT
        contents += rint().rjust(12)                # CLM_LINE_RX_SRVC_RFRNC_NUM  
        contents += rint().rjust(9)                 # CLM_LINE_RX_FILL_NUM

        # 21
        contents += random.choice(pstc()).ljust(2)  # CLM_PHRMCY_SRVC_TYPE_CD

        contents += "\n"

    generate_files("CCLF7", file_date, contents)        