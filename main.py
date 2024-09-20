# script_a.py
import subprocess
import sys

sys.path.append("./utils/")
from utils import purge_output_folder
from caches import cache_all

# Specifies the number of file dates that will be generated. Each file type 
# (CCLF1, CCLF2...) supports 9 different filename conventions so a single date 
# will result in 18 files (primary file and summary file) 2 dates will result 
# in 36 files and so on. 
number_of_file_months = 1

# Specifies the total population size of beneficiaries that can be randomly
# chosen and used to generate files.
number_of_beneficiaries = 100

# Specifies the total population size of beneficiaries that can be randomly
# chosen and used to generate files.
number_of_providers = 200

# Specifies the number of claims that will be generated.
number_of_claims = 1000


# Clean up date from previous runs.
purge_output_folder()

# Prepare the caches.
cache_all(number_of_beneficiaries, number_of_providers, number_of_claims)

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
args = [str(number_of_file_months)]

for script in scripts:
    result = subprocess.run([sys.executable, script] + args, capture_output=False, text=True)
