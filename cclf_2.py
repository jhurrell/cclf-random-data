# cclf_2.py
import sys
import os
import shutil
from utils import random_int_by_len, random_alpha_string, random_choice_from_array, random_date, random_float_in_range
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

# Define the path for the file
directory = "./cclf/cclf_2"
shutil.rmtree(directory)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)    

# Replicate the contents to each of the file types.
def generate_files(file_date, contents):
    files = {
        f"P.A{random_alpha_string(3)}.ACO.ZC2Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.A{random_alpha_string(3)}.ACO.ZC2R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC2Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC2R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC2Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC2Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.K{random_alpha_string(3)}.ACO.ZC2Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.C{random_alpha_string(3)}.ACO.ZC2Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC2Y{random_alpha_string(2)}.D{file_date}.T010203t",
    }

    for file in files:
        print(f"\tCreating {file}...")
        with open(f"{directory}/{file}", "w") as f:
            f.write(contents)

# Create n days worth of files.
for index in range(number_of_file_days):
    #  Prepare for this file type.
    delta = timedelta(days=index)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    print(f"CCLF2: Generating files for file_date {file_date}...")

    # Initialize the file contents.
    contents = ""

    for _ in range(number_of_lines_per_file):
        # 1-10
        contents = contents + random_int_by_len(13)     # CUR_CLM_UNIQ_ID
        contents = contents + random_int_by_len(10)     # CLM_LINE_NUM
        contents = contents + random_alpha_string(11)   # BENE_MBI_ID
        contents = contents + random_alpha_string(11)   # BENE_HIC_NUM
        contents = contents + random_choice_from_array(["10", "20", "30", "40", "50", "60", "61"])   # CLM_TYPE_CD
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_FROM_DT
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_THRU_DT
        contents = contents + random_alpha_string(4)    # CLM_LINE_PROD_REV_CTR_CD
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_INSTNL_REV_CTR_DT
        contents = contents + random_int_by_len(5)      # CLM_LINE_HCPCS_CD
  
        # 11-20
        contents = contents + random_int_by_len(11)     # BENE_EQTBL_BIC_HICN_NUM
        contents = contents + random_int_by_len(6)      # PRVDR_OSCAR_NUM
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_FROM_DT
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_THRU_DT
        contents = contents + random_float_in_range(-9999.9999, 9999.9999, 24)  # CLM_LINE_SRVC_UNIT_QTY
        contents = contents + random_float_in_range(-9999.99, 9999.99, 17)      # CLM_LINE_CVRD_PD_AMT
        contents = contents + random_int_by_len(2)      # HCPCS_1_MDFR_CD
        contents = contents + random_int_by_len(2)      # HCPCS_2_MDFR_CD
        contents = contents + random_int_by_len(2)      # HCPCS_3_MDFR_CD
        contents = contents + random_int_by_len(2)      # HCPCS_4_MDFR_CD

        # 21-23
        contents = contents + random_int_by_len(2)      # HCPCS_5_MDFR_CD
        contents = contents + random_int_by_len(5)      # CLM_REV_APC_HIPPS_CD
        contents = contents + random_int_by_len(20)     # CLM_FAC_PRVDR_OSCAR_NUM

        contents = contents + "\n"

    generate_files(file_date, contents)        