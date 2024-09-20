# cclf_9.py
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
from utils import dt

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
        # 1-6
        contents += "M"             # HICN_MBI_XREF_IND
        contents += bene["mbi"]     # CRNT_NUM
        contents += bene["mbi"]     # PRVS_NUM
        contents += dt()            # PRVS_ID_EFCTV_DT
        contents += dt()            # PRVS_ID_OBSLT_DT
        contents += "".ljust(12)    # BENE_RRB_NUM

        contents += "\n"

    generate_files("CCLF9", file_date, contents)        