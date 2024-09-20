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
beneficiaries = list(get_beneficiaries().values())

# Create n days worth of files.
for month in range(number_of_file_months):
    # Initialize.
    delta = timedelta(days=month * 30)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    contents = ""

    for bene in beneficiaries:
        # 1-10
        contents += bene["mbi"]                     # BENE_MBI_ID
        contents += "".ljust(11)                    # BENE_HIC_NUM
        contents += bene["state"]                   # BENE_FIPS_STATE_CD
        contents += bene["county"].ljust(3)         # BENE_FIPS_CNTY_CD
        contents += bene["zipCode"].ljust(5)        # BENE_ZIP_CD
        contents += bene["dob"]                     # BENE_DOB
        contents += bene["gender"]                  # BENE_SEX_CD  
        contents += bene["race"]                    # BENE_RACE_CD
        contents += bene["age"].rjust(3)            # BENE_AGE
        contents += random.choice(bmsc())           # BENE_MDCR_STUS_CD

        # 11-20
        contents += random.choice(bdsc())           # BENE_DUAL_STUS_CD
        contents += bene["dod"].ljust(10)           # BEBENE_DEATH_DT
        contents += dt()                            # BENE_RNG_BGN_DT
        contents += dt()                            # BENE_RNG_END_DT
        contents += bene["firstName"].ljust(30)     # BENE_1ST_NAME
        contents += bene["middleName"].ljust(15)    # BENE_MIDL_NAME
        contents += bene["lastName"].ljust(40)      # BENE_LAST_NAME
        contents += random.choice(beorcc())         # BENE_ORGNL_ENTLMT_RSN_CD
        contents += random.choice(bebi())           # BENE_ENTLMT_BUYIN_IND
        contents += dt()                            # BENE_PART_A_ENRLMT_BGN_DT

        # # 21-30
        contents += dt()                            # BENE_PART_B_ENRLMT_BGN_DT
        contents += bene["address1"].ljust(45)      # BENE_LINE_1_ADR
        contents += bene["address2"].ljust(45)      # BENE_LINE_2_ADR
        contents += bene["address3"].ljust(40)      # BENE_LINE_3_ADR
        contents += bene["address4"].ljust(40)      # BENE_LINE_4_ADR
        contents += bene["address5"].ljust(40)      # BENE_LINE_5_ADR
        contents += bene["address6"].ljust(40)      # BENE_LINE_6_ADR
        contents += bene["city"].ljust(100)         # GEO_ZIP_PLC_NAME
        contents += bene["state"]                   # GEO_USPS_STATE_CD
        contents += bene["zipCode"] 

        # # 31-40
        contents += bene["plus4"]                   # GEO_ZIP4_CD

        contents += "\n"

    generate_files("CCLF8", file_date, contents)        