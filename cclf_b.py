import random
import sys
import sys
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

# Add the path of the folder where the module is located
sys.path.append("./utils/")
from utils import generate_files, dol
from utils import get_claims, get_bene, get_prov
from utils import ynb, ctc, twobyte

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
            bene = get_bene(claim["mbi"])
            prov = get_prov(claim["npi"])
            
            # 1-10
            contents += claim["num"].ljust(13)          # CUR_CLM_UNIQ_ID
            contents += claim_line["ln"].rjust(10)      # CLM_LINE_NUM
            contents += bene["mbi"]                     # BENE_MBI_ID
            contents += bene["hic"].ljust(11)           # BENE_HIC_NUM
            contents += random.choice(ctc()).ljust(2)   # CLM_TYPE_CD
            contents += ynb()                           # CLM_LINE_NGACO_PBPMT_SW
            contents += ynb()                           # CLM_LINE_NGACO_PDSCHRG_HCBS_SW
            contents += ynb()                           # CLM_LINE_NGACO_SNF_WVR_SW
            contents += ynb()                           # CLM_LINE_NGACO_TLHLTH_SW
            contents += ynb()                           # CLM_LINE_NGACO_CPTATN_SW

            # 11-20
            contents += twobyte()                       # CLM_DEMO_1ST_NUM
            contents += twobyte()                       # CLM_DEMO_2ND_NUM
            contents += twobyte()                       # CLM_DEMO_3RD_NUM
            contents += twobyte()                       # CLM_DEMO_4TH_NUM
            contents += twobyte()                       # CLM_DEMO_5TH_NUM
            contents += dol().rjust(15)                 # CLM_PBP_INCLSN_AMT
            contents += dol().rjust(15)                 # CLM_PBP_RDCTN_AMT
            contents += ynb()                           # CLM_NGACO_CMG_WVR_SW
            contents += dol().rjust(19)                 # CLM_MDCR_DDCTBL_AMT
            contents += dol().rjust(15)                 # CLM_SQSTRTN_RDCTN_AMT

            # 21
            contents += "?"                             # CLM_LINE_CARR_HPSA_SCRCTY_CD

            contents += "\n"

    generate_files("CCLFB", file_date, contents)        