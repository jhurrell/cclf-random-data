# cclf_b.py
import sys
import os
import shutil
from utils import random_int_by_len, random_alpha_string, random_choice_from_array, random_float_in_range, random_num_string
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
directory = "./cclf/cclf_b"
shutil.rmtree(directory)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)    

# Replicate the contents to each of the file types.
def generate_files(file_date, contents):
    files = {
        f"P.A{random_alpha_string(3)}.ACO.ZCBY{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.A{random_alpha_string(3)}.ACO.ZCBR{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZCBY{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZCBR{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZCBY{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZCBY{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.K{random_alpha_string(3)}.ACO.ZCBY{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.C{random_alpha_string(3)}.ACO.ZCBY{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZCBY{random_alpha_string(2)}.D{file_date}.T010203t",
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
    print(f"CCLFB: Generating files for file_date {file_date}...")

    # Initialize the file contents.
    contents = ""

    for _ in range(number_of_lines_per_file):
        # 1-10
        contents = contents + random_int_by_len(13)                         # CUR_CLM_UNIQ_ID
        contents = contents + random_num_string(10)                         # CLM_LINE_NUM
        contents = contents + random_alpha_string(11)                       # BENE_MBI_ID
        contents = contents + random_alpha_string(11)                       # BENE_HIC_NUM
        contents = contents + random_choice_from_array(["71", "72"])        # CLM_TYPE_CD
        contents = contents + random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_PBPMT_SW
        contents = contents + random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_PDSCHRG_HCBS_SW
        contents = contents + random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_SNF_WVR_SW
        contents = contents + random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_TLHLTH_SW
        contents = contents + random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_CPTATN_SW

        # 11-20
        contents = contents + random_num_string(2)                          # CLM_DEMO_1ST_NUM
        contents = contents + random_num_string(2)                          # CLM_DEMO_2ND_NUM
        contents = contents + random_num_string(2)                          # CLM_DEMO_3RD_NUM
        contents = contents + random_num_string(2)                          # CLM_DEMO_4TH_NUM
        contents = contents + random_num_string(2)                          # CLM_DEMO_5TH_NUM
        contents = contents + random_float_in_range(-9999.99, 9999.99, 15)  # CLM_PBP_INCLSN_AMT
        contents = contents + random_float_in_range(-9999.99, 9999.99, 15)  # CLM_PBP_RDCTN_AMT
        contents = contents + random_choice_from_array(["Y", "N"])          # CLM_NGACO_CMG_WVR_SW
        contents = contents + random_float_in_range(-9999.99, 9999.99, 19)  # CLM_MDCR_DDCTBL_AMT
        contents = contents + random_float_in_range(-9999.99, 9999.99, 15)  # CLM_SQSTRTN_RDCTN_AMT

        # 21
        contents = contents + random_alpha_string(1)                        # CLM_LINE_CARR_HPSA_SCRCTY_CD

        contents = contents + "\n"

    generate_files(file_date, contents)        