import datetime
import subprocess
import sys

sys.path.append("./utils/")
from utils import purge_output_folder
from caches import cache_all


# Specifies the total population size of beneficiaries that can be randomly
# chosen and used to generate files.
number_of_beneficiaries = 100

# Specifies the total population size of beneficiaries that can be randomly
# chosen and used to generate files.
number_of_providers = 200

# Specifies the number of claims that will be generated and in which month
# and year.
number_of_claims = 1000
claims_year = 2024
claims_month = 9


# Clean up date from previous runs.
purge_output_folder()

# Prepare the caches.
cache_all(number_of_beneficiaries, number_of_providers, number_of_claims, claims_year, claims_month)


# Specifies the scripts that will be called each time main is executed.
scripts = [
    "./cclf_1.py", 
    "./cclf_2.py", 
    "./cclf_3.py", 
    "./cclf_4.py", 
    "./cclf_5.py", 
    "./cclf_6.py", 
    "./cclf_7.py", 
    "./cclf_8.py", 
    "./cclf_9.py", 
    "./cclf_a.py",
    "./cclf_b.py",
]

# Convert the arguments to strins.
file_dt = datetime.date(claims_year, claims_month, 1).strftime("%Y-%m-%d")
args = [str(file_dt)]

for script in scripts:
    result = subprocess.run([sys.executable, script] + args, capture_output=False, text=True)
