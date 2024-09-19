# cclf_6.py
import sys
import os
import shutil
from utils import random_int_by_len, random_alpha_string, random_choice_from_array, random_date, random_float_in_range, random_alphanum_string
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
directory = "./cclf/cclf_6"
shutil.rmtree(directory)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)    

# Replicate the contents to each of the file types.
def generate_files(file_date, contents):
    files = {
        f"P.A{random_alpha_string(3)}.ACO.ZC6Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.A{random_alpha_string(3)}.ACO.ZC6R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC6Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC6R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC6Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC6Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.K{random_alpha_string(3)}.ACO.ZC6Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.C{random_alpha_string(3)}.ACO.ZC6Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC6Y{random_alpha_string(2)}.D{file_date}.T010203t",
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
    print(f"CCLF6: Generating files for file_date {file_date}...")

    # Initialize the file contents.
    contents = ""

    for _ in range(number_of_lines_per_file):
        # 1-10
        contents = contents + random_int_by_len(13)     # CUR_CLM_UNIQ_ID
        contents = contents + random_int_by_len(10)     # CLM_LINE_NUM
        contents = contents + random_alpha_string(11)   # BENE_MBI_ID
        contents = contents + random_alpha_string(11)   # BENE_HIC_NUM
        contents = contents + random_choice_from_array(["81", "82"])   # CLM_TYPE_CD
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_FROM_DT
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_THRU_DT
        contents = contents + random_alpha_string(1)   # CLM_FED_TYPE_SRVC_CD
        contents = contents + random_alpha_string(2)   # CLM_POS_CD
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_FROM_DT

        #11-20
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_THRU_DT
        contents = contents + random_alpha_string(5)      # CLM_LINE_HCPCS_CD
        contents = contents + random_float_in_range(-9999.99, 9999.99, 15)  # CLM_LINE_CVRD_PD_AMT
        contents = contents + random_alpha_string(1)    # CLM_PRMRY_PYR_CD
        contents = contents + random_alpha_string(10)   # PAYTO_PRVDR_NPI_NUM
        contents = contents + random_alpha_string(10)   # ORDRG_PRVDR_NPI_NUM
        contents = contents + random_choice_from_array(["G", "H", "J", "T", "X", "Y"]).rjust(2) # CLM_CARR_PMT_DNL_CD
        contents = contents + random_choice_from_array(["G", "H", "J", "19", "41"]).rjust(2)    # CLM_PRCSG_IND_CD
        contents = contents + random_choice_from_array(["0", "1", "2"]).rjust(2)                # CLM_ADJSMT_TYPE_CD
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))         # CLM_EFCTV_DT

        # 21-27
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))         # CLM_IDR_LD_DT
        contents = contents + random_alphanum_string(40)    #  CLM_CNTL_NUM
        contents = contents + random_alpha_string(11)       # BENE_EQTBL_BIC_HICN_NUM
        contents = contents + random_float_in_range(-9999.99, 9999.99, 17)  # CLM_LINE_ALOWD_CHRG_AMT
        contents = contents + random_choice_from_array(["01", "02", "03"])  # CLM_DISP_CD
        contents = contents + random_alpha_string(10)   # CLM_BLG_PRVDR_NPI_NUM
        contents = contents + random_alpha_string(10)   # CLM_RFRG_PRVDR_NPI_NUM

        contents = contents + "\n"

    generate_files(file_date, contents)        