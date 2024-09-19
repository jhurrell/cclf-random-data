# cclf_1.py
import sys
import os
import shutil
from utils import random_int_by_len, random_alpha_string, random_alphanum_string, random_choice_from_array, random_date, random_float_in_range, random_int_in_range
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
directory = "./cclf/ccl_1"
shutil.rmtree(directory)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)

# Replicate the conents to each of the file types.
def generate_files(file_date, contents):
    files = {
        f"P.A{random_alpha_string(3)}.ACO.ZC1Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.A{random_alpha_string(3)}.ACO.ZC1R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC1Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC1R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC1Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC1Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.K{random_alpha_string(3)}.ACO.ZC1Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.C{random_alpha_string(3)}.ACO.ZC1Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC1Y{random_alpha_string(2)}.D{file_date}.T010203t",
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
        contents = contents + random_alpha_string(6)    # PRVDR_OSCAR_NUM
        contents = contents + random_alpha_string(11)   # BENE_MBI_ID
        contents = contents + random_alpha_string(11)   # BENE_HIC_NUM
        contents = contents + random_choice_from_array(["10", "20", "30", "40", "50", "60", "61"])   # CLM_TYPE_CD
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_FROM_DT
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_THRU_DT
        contents = contents + random_choice_from_array(["1", "2", "3", "4", "5", "6", "7", "8", "9"])   # CLM_BILL_FAC_TYPE_CD
        contents = contents + random_choice_from_array(["1", "2", "3", "4", "5", "6", "7", "8", "9"])   # CLM_BILL_CLSFCTN_CD
        contents = contents + random_alpha_string(7)    # PRNCPL_DGNS_CD

        # 11-20
        contents = contents + random_alpha_string(7)    # ADMTG_DGNS_CD
        contents = contents + random_alpha_string(2)    # CLM_MDCR_NPMT_RSN_CD
        contents = contents + random_float_in_range(-9999.99, 9999.99, 17)    # CLM_PMT_AMT
        contents = contents + random_alpha_string(1)    # CLM_NCH_PRMRY_PYR_CD
        contents = contents + random_alpha_string(2)    # PRVDR_FAC_FIPS_ST_CD
        contents = contents + random_alpha_string(2)    # BENE_PTNT_STUS_CD
        contents = contents + random_alpha_string(4)    # DGNS_DRG_CD
        contents = contents + random_int_by_len(1)      # CLM_OP_SRVC_TYPE_CD
        contents = contents + random_alpha_string(10)   # FAC_PRVDR_NPI_NUM
        contents = contents + random_alpha_string(10)   # OPRTG_PRVDR_NPI_NUM

        # 21-30
        contents = contents + random_alpha_string(10)   # ATNDG_PRVDR_NPI_NUM
        contents = contents + random_alpha_string(10)   # OTHR_PRVDR_NPI_NUM
        contents = contents + random_choice_from_array([" 1", " 2", " 3"])   # CLM_ADJSMT_TYPE_CD
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_EFCTV_DT
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_IDR_LD_DT
        contents = contents + random_alpha_string(11)   # OTHR_PRVDR_NPI_NUM
        contents = contents + random_int_by_len(1).rjust(2)   # CLM_ADMSN_TYPE_CD
        contents = contents + random_alpha_string(2)    # CLM_ADMSN_SRC_CD
        contents = contents + random_alpha_string(1)    # CLM_BILL_FREQ_CD
        contents = contents + random_int_in_range(0,5)  # CLM_QUERY_CD

        # 31-40
        contents = contents + random_choice_from_array(["0", "9", "U"])   # DGNS_PRCDR_ICD_IND
        contents = contents + random_float_in_range(-9999.99, 9999.99, 15)  # CLM_MDCR_INSTNL_TOT_CHRG_AMT
        contents = contents + random_float_in_range(-9999.99, 9999.99, 15)  # CLM_MDCR_IP_PPS_CPTL_IME_AMT
        contents = contents + random_float_in_range(-9999.99, 9999.99, 22)  # CLM_OPRTNL_IME_AMT
        contents = contents + random_float_in_range(-9999.99, 9999.99, 15)  # CLM_MDCR_IP_PPS_DSPRPRTNT_AMT
        contents = contents + random_float_in_range(-9999.99, 9999.99, 15)  # CLM_HIPPS_UNCOMPD_CARE_AMT
        contents = contents + random_float_in_range(-9999.99, 9999.99, 22)  # CLM_OPRTNL_DSPRPRTNT_AMT
        contents = contents + random_alpha_string(20)   # CLM_BLG_PRVDR_OSCAR_NUM
        contents = contents + random_alpha_string(10)   # CLM_BLG_PRVDR_NPI_NUM
        contents = contents + random_alpha_string(10)   # CLM_OPRTG_PRVDR_NPI_NUM

        # 41-45
        contents = contents + random_alpha_string(10)   # CLM_ATNDG_PRVDR_NPI_NUM
        contents = contents + random_alpha_string(10)   # CLM_OTHR_PRVDR_NPI_NUM
        contents = contents + random_alphanum_string(40)    #  CLM_CNTL_NUM
        contents = contents + random_alphanum_string(40)    # CLM_ORG_CNTL_NUM
        contents = contents + random_alphanum_string(5)     # CLM_CONTRCTR_NUM
        contents = contents + "\n"

    delta = timedelta(days=index)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    print(f"CCLF1: Generating files for file_date {file_date}...")
    generate_files(file_date, contents)
