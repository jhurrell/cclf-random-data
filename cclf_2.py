# cclf_1.py
from utils import random_int_by_len, random_alpha_string, random_choice_from_array, random_date, random_float_with_precision
from datetime import datetime

number_of_files = 10
number_of_lines_per_file = 10

for _ in range(number_of_lines_per_file):

    line = ""
    line = line + random_int_by_len(13)     # CUR_CLM_UNIQ_ID
    line = line + random_int_by_len(9)      # CLM_LINE_NUM
    line = line + random_alpha_string(11)   # BENE_MBI_ID
    line = line + random_alpha_string(11)   # BENE_HIC_NUM
    line = line + random_choice_from_array(["10", "20", "30", "40", "50", "60", "61"])   # CLM_TYPE_CD
    line = line + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_FROM_DT
    line = line + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_THRU_DT
    line = line + random_alpha_string(4)   # CLM_LINE_PROD_REV_CTR_CD
    line = line + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_LINE_INSTNL_REV_CTR_DT
    line = line + random_alpha_string(5)    # CLM_LINE_HCPCS_CD
    line = line + random_alpha_string(11)   # BENE_EQTBL_BIC_HICN_NUM
    line = line + random_alpha_string(6)   # PRVDR_OSCAR_NUM
    line = line + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_FROM_DT
    line = line + random_date(datetime(2024, 1, 1), datetime(2024, 12, 31)) # CLM_THRU_DT
    line = line + random_float_with_precision()

    print(line)
