# cclf_b.py
import sys
sys.path.append("./utils/")
from utils import generate_files, random_int_by_len, random_alpha_string, random_choice_from_array, random_float_in_range, random_num_string
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
        # 1-10
        contents += random_int_by_len(13)                         # CUR_CLM_UNIQ_ID
        contents += random_num_string(10)                         # CLM_LINE_NUM
        contents += random_alpha_string(11)                       # BENE_MBI_ID
        contents += random_alpha_string(11)                       # BENE_HIC_NUM
        contents += random_choice_from_array(["71", "72"])        # CLM_TYPE_CD
        contents += random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_PBPMT_SW
        contents += random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_PDSCHRG_HCBS_SW
        contents += random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_SNF_WVR_SW
        contents += random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_TLHLTH_SW
        contents += random_choice_from_array(["Y", "N"])          # CLM_LINE_NGACO_CPTATN_SW

        # 11-20
        contents += random_num_string(2)                          # CLM_DEMO_1ST_NUM
        contents += random_num_string(2)                          # CLM_DEMO_2ND_NUM
        contents += random_num_string(2)                          # CLM_DEMO_3RD_NUM
        contents += random_num_string(2)                          # CLM_DEMO_4TH_NUM
        contents += random_num_string(2)                          # CLM_DEMO_5TH_NUM
        contents += random_float_in_range(-9999.99, 9999.99, 15)  # CLM_PBP_INCLSN_AMT
        contents += random_float_in_range(-9999.99, 9999.99, 15)  # CLM_PBP_RDCTN_AMT
        contents += random_choice_from_array(["Y", "N"])          # CLM_NGACO_CMG_WVR_SW
        contents += random_float_in_range(-9999.99, 9999.99, 19)  # CLM_MDCR_DDCTBL_AMT
        contents += random_float_in_range(-9999.99, 9999.99, 15)  # CLM_SQSTRTN_RDCTN_AMT

        # 21
        contents += random_alpha_string(1)                        # CLM_LINE_CARR_HPSA_SCRCTY_CD

        contents += "\n"

    generate_files("CCLFB", file_date, contents)        