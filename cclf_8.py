# cclf_8.py
import sys
import os
import shutil
from utils import random_alpha_string, random_choice_from_array, random_date, random_num_string, random_int_in_range
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
directory = "./cclf/cclf_8"
shutil.rmtree(directory)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)    

# Replicate the contents to each of the file types.
def generate_files(file_date, contents):
    files = {
        f"P.A{random_alpha_string(3)}.ACO.ZC8Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.A{random_alpha_string(3)}.ACO.ZC8R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC8Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC8R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC8Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC8Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.K{random_alpha_string(3)}.ACO.ZC8Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.C{random_alpha_string(3)}.ACO.ZC8Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC8Y{random_alpha_string(2)}.D{file_date}.T010203t",
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
    print(f"CCLF8: Generating files for file_date {file_date}...")

    # Initialize the file contents.
    contents = ""

    for _ in range(number_of_lines_per_file):
        # 1-10
        contents = contents + random_alpha_string(11)           # BENE_MBI_ID
        contents = contents + random_alpha_string(11)           # BENE_HIC_NUM
        contents = contents + random_alpha_string(2)            # BENE_FIPS_STATE_CD
        contents = contents + random_alpha_string(3)            # BENE_FIPS_CNTY_CD
        contents = contents + random_num_string(5)              # BENE_ZIP_CD
        contents = contents + random_date(datetime(1940, 1, 1), datetime(1970, 12, 31))         # BENE_DOB
        contents = contents + random_choice_from_array(["1", "2", "0"])                         # BENE_SEX_CD
        contents = contents + random_choice_from_array(["0", "1", "2", "3", "4", "5", "6"])     # BENE_RACE_CD
        contents = contents + random_int_in_range(60, 100).rjust(3)                             # BENE_AGE
        contents = contents + random_choice_from_array(["10", "11", "20", "21", "31"])          # BENE_MDCR_STUS_CD

        # 11-20
        contents = contents + random_alpha_string(2)            # BENE_DUAL_STUS_CD
        contents = contents + random_date(datetime(1940, 1, 1), datetime(1970, 12, 31))         # BEBENE_DEATH_DT
        contents = contents + random_date(datetime(1940, 1, 1), datetime(1970, 12, 31))         # BENE_RNG_BGN_DT
        contents = contents + random_date(datetime(1940, 1, 1), datetime(1970, 12, 31))         # BENE_RNG_END_DT
        contents = contents + random_alpha_string(30)            # BENE_1ST_NAME
        contents = contents + random_alpha_string(15)            # BENE_MIDL_NAME
        contents = contents + random_alpha_string(40)            # BENE_LAST_NAME
        contents = contents + random_choice_from_array(["0", "1", "2", "3", "4"])               # BENE_ORGNL_ENTLMT_RSN_CD
        contents = contents + random_choice_from_array(["0", "1", "2", "3", "A", "B", "C"])     # BENE_ENTLMT_BUYIN_IND
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))         # BENE_PART_A_ENRLMT_BGN_DT

        # 21-30
        contents = contents + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31))         # BENE_PART_B_ENRLMT_BGN_DT
        contents = contents + random_alpha_string(45)           # BENE_LINE_1_ADR
        contents = contents + random_alpha_string(45)           # BENE_LINE_2_ADR
        contents = contents + random_alpha_string(40)           # BENE_LINE_3_ADR
        contents = contents + random_alpha_string(40)           # BENE_LINE_4_ADR
        contents = contents + random_alpha_string(40)           # BENE_LINE_5_ADR
        contents = contents + random_alpha_string(40)           # BENE_LINE_6_ADR
        contents = contents + random_alpha_string(100)          # GEO_ZIP_PLC_NAME
        contents = contents + random_alpha_string(2)            # GEO_USPS_STATE_CD
        contents = contents + random_num_string(5)              # GEO_ZIP5_CD

        # 31-40
        contents = contents + random_num_string(4)              # GEO_ZIP4_CD

        contents = contents + "\n"

    generate_files(file_date, contents)        