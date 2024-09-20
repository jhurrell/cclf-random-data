# cclf_8.py
import random
import sys
import sys
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

# Add the path of the folder where the module is located
sys.path.append("./utils/")
from utils import generate_files
from utils import get_beneficiaries
from utils import bmsc, bdsc, beorcc, dt, bebi

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
bene = get_beneficiaries()  

# Create n days worth of files.
for month in range(number_of_file_months):
    # Initialize.
    delta = timedelta(days=month * 30)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    contents = ""

    for b in bene:
        # 1-10
        contents += b["mbi"]                    # BENE_MBI_ID
        contents += "".ljust(11)                # BENE_HIC_NUM
        contents += b["state"]                  # BENE_FIPS_STATE_CD
        contents += b["county"].ljust(3)        # BENE_FIPS_CNTY_CD
        contents += b["zipCode"].ljust(5)       # BENE_ZIP_CD
        contents += b["dob"]                    # BENE_DOB
        contents += b["gender"]                 # BENE_SEX_CD  
        contents += b["race"]                   # BENE_RACE_CD
        contents += b["age"].rjust(3)           # BENE_AGE
        contents += random.choice(bmsc())       # BENE_MDCR_STUS_CD

        # 11-20
        contents += random.choice(bdsc())       # BENE_DUAL_STUS_CD
        contents += b["dod"].ljust(10)          # BEBENE_DEATH_DT
        contents += dt()                        # BENE_RNG_BGN_DT
        contents += dt()                        # BENE_RNG_END_DT
        contents += b["firstName"].ljust(30)    # BENE_1ST_NAME
        contents += b["middleName"].ljust(15)   # BENE_MIDL_NAME
        contents += b["lastName"].ljust(40)     # BENE_LAST_NAME
        contents += random.choice(beorcc())     # BENE_ORGNL_ENTLMT_RSN_CD
        contents += random.choice(bebi())       # BENE_ENTLMT_BUYIN_IND
        contents += dt()                        # BENE_PART_A_ENRLMT_BGN_DT

        # # 21-30
        contents += dt()                        # BENE_PART_B_ENRLMT_BGN_DT
        contents += b["address1"].ljust(45)     # BENE_LINE_1_ADR
        contents += b["address2"].ljust(45)     # BENE_LINE_2_ADR
        contents += b["address3"].ljust(40)     # BENE_LINE_3_ADR
        contents += b["address4"].ljust(40)     # BENE_LINE_4_ADR
        contents += b["address5"].ljust(40)     # BENE_LINE_5_ADR
        contents += b["address6"].ljust(40)     # BENE_LINE_6_ADR
        contents += b["city"].ljust(100)        # GEO_ZIP_PLC_NAME
        contents += b["state"]                  # GEO_USPS_STATE_CD
        contents += b["zipCode"] 

        # # 31-40
        contents += b["plus4"]                  # GEO_ZIP4_CD

        contents += "\n"

    generate_files("CCLF8", file_date, contents)        