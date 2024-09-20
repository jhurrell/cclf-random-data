# cclf_5.py
import random
import sys
import sys
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

# Add the path of the folder where the module is located
sys.path.append("./utils/")
from utils import dol, generate_files
from utils import get_claims, get_beneficiaries, get_providers
from utils import ctc, rpt, tsc, pos, hcpcs, ppc, icd, cpd, pic, cat, flt, hcpcsm, cdc, tsc


# Capture arguments or default if not provided.
if len(sys.argv) == 2:
    # Capture arguments and convert them
    try:
        number_of_file_months = int(sys.argv[1])
    except ValueError as e:
        sys.exit(1)  # Exit with error code    
else:
    number_of_file_months = 1


# Prepare data structures for lookups.
clm = get_claims()
bene = get_beneficiaries()  
prov = get_providers()


# Create n days worth of files.
for month in range(number_of_file_months):
    # Initialize.
    delta = timedelta(days=month * 30)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    contents = ""

    for claim in clm:

        pr = random.choice(prov)
        diag = random.choice(icd())

        # 1-10
        contents += claim["num"].ljust(13)          # CUR_CLM_UNIQ_ID
        contents += claim["ln"].rjust(10)           # CLM_LINE_NUM
        contents += claim["mbi"]                    # BENE_MBI_ID
        contents += "".ljust(11)                    # BENE_HIC_NUM
        contents += random.choice(ctc()).ljust(2)   # CLM_TYPE_CD
        contents += claim["from_dt"]                # CLM_FROM_DT
        contents += claim["thru_dt"]                # CLM_THRU_DT
        contents += random.choice(rpt()).ljust(3)   # RNDRG_PRVDR_TYPE_CD
        contents += pr["state"]                     # RNDRG_PRVDR_FIPS_ST_CD
        contents += pr["psc"]                       # CLM_PRVDR_SPCLTY_CD

        # 11-20
        contents += random.choice(tsc())            # CLM_FED_TYPE_SRVC_CD
        contents += random.choice(pos())            # CLM_POS_CD
        contents += claim["from_dt"]                # CLM_LINE_FROM_DT
        contents += claim["thru_dt"]                # CLM_LINE_THRU_DT    
        contents += random.choice(hcpcs())          # CLM_LINE_HCPCS_CD  
        contents += str(dol()).rjust(15)            # CLM_LINE_CVRD_PD_AMT
        contents += random.choice(ppc()).ljust(1)   # CLM_LINE_PRMRY_PYR_CD ???
        contents += diag["code"].rjust(7)           # CLM_LINE_DGNS_CD
        contents += pr["ein"].rjust(10)             # CLM_RNDRG_PRVDR_TAX_NUM
        contents += pr["npi"]                       # RNDRG_PRVDR_NPI_NUM

        # 21-30
        contents += random.choice(cpd()).ljust(2)   # CLM_CARR_PMT_DNL_CD
        contents += random.choice(pic()).ljust(2)   # CLM_PRCSG_IND_CD
        contents += random.choice(cat()).ljust(2)   # CLM_ADJSMT_TYPE_CD
        contents += claim["from_dt"]                # CLM_EFCTV_DT
        contents += claim["thru_dt"]                # CLM_IDR_LD_DT
        contents += claim["ccn"].rjust(40)          # CLM_CNTL_NUM
        contents += "".ljust(11)                    # BENE_EQTBL_BIC_HICN_NUM
        contents += str(dol()).rjust(17)            # CLM_LINE_ALOWD_CHRG_AMT ???
        contents += str(flt()).rjust(24)            # CLM_LINE_SRVC_UNIT_QTY
        contents += random.choice(hcpcsm())         # HCPCS_1_MDFR_CD

        # 31-40
        contents += random.choice(hcpcsm())         # HCPCS_2_MDFR_CD
        contents += random.choice(hcpcsm())         # HCPCS_3_MDFR_CD
        contents += random.choice(hcpcsm())         # HCPCS_4_MDFR_CD
        contents += random.choice(hcpcsm())         # HCPCS_5_MDFR_CD
        contents += random.choice(cdc())            # CLM_DISP_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_1_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_2_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_3_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_4_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_5_CD

        # #41-50
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_6_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_7_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_8_CD
        contents += random.choice(icd())["ver"]             # DGNS_PRCDR_ICD_IND
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_9_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_10_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_11_CD
        contents += random.choice(icd())["code"].ljust(7)   # CLM_DGNS_12_CD
        contents += random.choice(tsc()).ljust(3)           # HCPCS_BETOS_CD
        contents += pr["npi"].ljust(10)                     # CLM_RNDRG_PRVDR_NPI_NUM

        # 51-60
        contents += pr["npi"]       # CLM_RFRG_PRVDR_NPI_NUM
        contents += claim["mac"]    # CLM_CNTRCTR_NUM

        contents += "\n"

    generate_files("CCLF5", file_date, contents)        