import random
import sys
import sys
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

# Add the path of the folder where the module is located
sys.path.append("./utils/")
from utils import dol, generate_files
from utils import get_claims
from utils import ctc, ynb, twobyte, cat

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
        # 1-10
        contents += claim["num"].ljust(13)          # CUR_CLM_UNIQ_ID
        contents += claim["mbi"]                    # BENE_MBI_ID
        contents += "".ljust(11)                    # BENE_HIC_NUM
        contents += random.choice(ctc()).rjust(2)   # CLM_TYPE_CD
        contents += claim["from_dt"]                # CLM_ACTV_CARE_FROM_DT
        contents += ynb()                           # CLM_NGACO_PBPMT_SW
        contents += ynb()                           # CLM_NGACO_PDSCHRG_HCBS_SW
        contents += ynb()                           # CLM_NGACO_SNF_WVR_SW
        contents += ynb()                           # CLM_NGACO_TLHLTH_SW
        contents += ynb()                           # CLM_NGACO_CPTATN_SW

        # 11-20
        contents += twobyte()                       # CLM_DEMO_1ST_NUM
        contents += twobyte()                       # CLM_DEMO_2ND_NUM
        contents += twobyte()                       # CLM_DEMO_3RD_NUM
        contents += twobyte()                       # CLM_DEMO_4TH_NUM
        contents += twobyte()                       # CLM_DEMO_5TH_NUM
        contents += dol().rjust(19)                 # CLM_PBP_INCLSN_AMT
        contents += dol().rjust(19)                 # CLM_PBP_RDCTN_AMT
        contents += ynb()                           # CLM_NGACO_CMG_WVR_SW
        contents += dol().rjust(19)                 # CLM_INSTNL_PER_DIEM_AMT
        contents += dol().rjust(15)                 # CLM_MDCR_IP_BENE_DDCTBL_AMT

        # 21-30
        contents += dol().rjust(19)                 # CLM_MDCR_COINSRNC_AMT
        contents += dol().rjust(15)                 # CLM_BLOOD_LBLTY_AMT
        contents += dol().rjust(15)                 # CLM_INSTNL_PRFNL_AMT
        contents += dol().rjust(19)                 # CLM_NCVRD_CHRG_AMT
        contents += dol().rjust(19)                 # CLM_MDCR_DDCTBL_AMT
        contents += ynb()                           # CLM_RLT_COND_CD
        contents += dol().rjust(19)                 # CLM_OPRTNL_OUTLR_AMT
        contents += dol().rjust(19)                 # CLM_MDCR_NEW_TECH_AMT
        contents += dol().rjust(19)                 # CLM_ISLET_ISOLN_AMT
        contents += dol().rjust(19)                 # CLM_SQSTRTN_RDCTN_AMT

        # 31-33
        contents += random.choice(cat()).ljust(3)   # CLM_1_REV_CNTR_ANSI_RSN_CD       
        contents += "??"                            # CLM_1_REV_CNTR_ANSI_GRP_CD
        contents += dol().rjust(19)                 # CLM_MIPS_PMT_AMT

        contents += "\n"

    generate_files("CCLFA", file_date, contents)        