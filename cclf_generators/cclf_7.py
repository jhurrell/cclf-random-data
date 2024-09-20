# cclf_7.py
import sys
sys.path.append("./utils/")
from utils import generate_files, random_int_by_len, random_alpha_string, random_choice_from_array, random_date, random_float_in_range, random_alphanum_string, random_num_string
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
        contents += random_int_by_len(13)     # CUR_CLM_UNIQ_ID
        contents += random_alpha_string(11)   # BENE_MBI_ID
        contents += random_alpha_string(11)   # BENE_HIC_NUM
        contents += random_num_string(11)     # CLM_LINE_NDC_CD
        contents += random_choice_from_array(["01", "02", "03", "04"])   # CLM_TYPE_CD
        contents += random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_FROM_DT
        contents += random_choice_from_array(["01", "06", "07", "08", "11", "99"])   # PRVDR_SRVC_ID__QLFYR_CD
        contents += random_alpha_string(20)   # CLM_SRVC_PRVDR_GNRC_ID_NUM
        contents += random_choice_from_array(["P", "C"])   # CLM_DSPNSNG_STUS_CD
        contents += random_choice_from_array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])   # CLM_DAW_PROD_SLCTN_CD

        # 11-20
        contents += random_float_in_range(-9999.9999, 9999.9999, 24)  # CLM_LINE_SRVC_UNIT_QTY
        contents += random_num_string(9)     # CLM_LINE_DAYS_SUPLY_QTY
        contents += random_choice_from_array(["01", "06", "07", "08", "11", "12", "99"])   # PRVDR_PRSBNG_ID_QLFYR_CD
        contents += random_alpha_string(20)   # CLM_PRSBNG_PRVDR_GNRC_ID_NUM
        contents += random_float_in_range(-9999.99, 9999.99, 13)  # CLM_LINE_BENE_PMT_AMT
        contents += random_choice_from_array([" 0", " 1", " 2"])  # CLM_ADJSMT_TYPE_CD
        contents += random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_EFCTV_DT
        contents += random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_IDR_LD_DT
        contents += random_alphanum_string(12)    # CLM_LINE_RX_SRVC_RFRNC_NUM
        contents += random_alphanum_string(9)     # CLM_LINE_RX_FILL_NUM

        # 21-30
        contents += random_choice_from_array([" 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", "99"])   # CLM_PHRMCY_SRVC_TYPE_CD

        contents += "\n"

    generate_files("CCLF7", file_date, contents)        