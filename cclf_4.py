# cclf_4.py
import sys
import os
import shutil
from utils import random_int_by_len, random_alpha_string, random_choice_from_array, random_date, random_float_in_range
from datetime import datetime, timedelta

# Check if there are enough arguments
if len(sys.argv) < 3:
    print("Usage: python cclf_4.py <number_of_file_days> <number_of_lines_per_file>")
    sys.exit(1)  # Exit with error code

# Capture arguments and convert them
try:
    number_of_file_days = int(sys.argv[1])
    number_of_lines_per_file = int(sys.argv[2])
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)  # Exit with error code

# Define the path for the file
directory = "./cclf/cclf4"
shutil.rmtree(directory)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)    

# Replicate the conents to each of the file types.
def generate_files(file_date, contents):
    files = {
        f"P.A{random_alpha_string(3)}.ACO.ZC5Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.A{random_alpha_string(3)}.ACO.ZC5R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC5Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC5R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC5Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC5Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.K{random_alpha_string(3)}.ACO.ZC5Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.C{random_alpha_string(3)}.ACO.ZC5Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC5Y{random_alpha_string(2)}.D{file_date}.T010203t",
    }

    for file in files:
        print(f"\tCreating {file}...")
        with open(f"{directory}/{file}", "w") as f:
            f.write(contents)

# Create n days worth of files.
for index in range(number_of_file_days):
    # Initialize the file contents.
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

    delta = timedelta(days=index)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    print(f"CCLF4: Generating files for file_date {file_date}...")
    generate_files(file_date, contents)        