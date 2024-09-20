# cclf_9.py
import sys
sys.path.append("./utils/")
from utils import generate_files, random_alpha_string, random_choice_from_array, random_date
from datetime import datetime, timedelta

# Capture arguments or default if not provided.
if len(sys.argv) == 3:
    # Capture arguments and convert them
    try:
        number_of_file_months = int(sys.argv[1])
        number_of_lines_per_file = int(sys.argv[2])
    except ValueError as e:
        sys.exit(1)  # Exit with error code    
else:
    number_of_file_months = 1
    number_of_lines_per_file = 1000


# Create n days worth of files.
for month in range(number_of_file_months):
    # Initialize.
    delta = timedelta(days=month*30)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    contents = ""

    for _ in range(number_of_lines_per_file):
        # 1-6
        contents = contents + random_choice_from_array(["X", " "])                              # HICN_MBI_XREF_IND
        contents = contents + random_alpha_string(11)                                           # CRNT_NUM
        contents = contents + random_alpha_string(11)                                           # PRVS_NUM
        contents = contents + random_date(datetime(1940, 1, 1), datetime(1970, 12, 31))         # PRVS_ID_EFCTV_DT
        contents = contents + random_date(datetime(1940, 1, 1), datetime(1970, 12, 31))         # PRVS_ID_OBSLT_DT
        contents = contents + random_alpha_string(12)                                           # BENE_RRB_NUM

        contents = contents + "\n"

    generate_files("CCLF9", file_date, contents)        