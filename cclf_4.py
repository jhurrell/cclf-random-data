# cclf_4.py
import sys
from utils import generate_files, random_int_by_len, random_alpha_string, random_choice_from_array, random_date
from datetime import datetime, timedelta

# Capture arguments or default if not provided.
if len(sys.argv) == 3:
    # Capture arguments and convert them
    try:
        number_of_file_days = int(sys.argv[1])
        number_of_lines_per_file = int(sys.argv[2])
    except ValueError as e:
        sys.exit(1)  # Exit with error code    
else:
    number_of_file_days = 1
    number_of_lines_per_file = 1000


# Create n days worth of files.
for index in range(number_of_file_days):
    # Initialize.
    delta = timedelta(days=index)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    contents = ""

    for _ in range(number_of_lines_per_file):
        # 1-10
        contents = contents + random_int_by_len(13)     # CUR_CLM_UNIQ_ID
        contents = contents + random_alpha_string(11)   # BENE_MBI_ID
        contents = contents + random_alpha_string(11)   # BENE_HIC_NUM
        contents = contents + random_choice_from_array(["10", "20", "30", "40", "50", "60", "61"])   # CLM_TYPE_CD
        contents = contents + random_choice_from_array(["0", "9", "U"])   # CLM_PROD_TYPE_CD
        contents = contents + random_int_by_len(2)      # CLM_VAL_SQNC_NUM
        contents = contents + random_int_by_len(7)      # CLM_DGNS_CD
        contents = contents + random_int_by_len(11)     # BENE_EQTBL_BIC_HICN_NUM
        contents = contents + random_alpha_string(6)    # PRVDR_OSCAR_NUM
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_FROM_DT

        # 11-14
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_THRU_DT
        contents = contents + random_int_by_len(7)      # CLM_POA_IND
        contents = contents + random_choice_from_array(["0", "9", "U"])   # DGNS_PRCDR_ICD_IND
        contents = contents + random_alpha_string(20)   # CLM_BLG_PRVDR_OSCAR_NUM

        contents = contents + "\n"

    generate_files("CCLF4", file_date, contents)        