# script_a.py
import subprocess
import sys

# Specifies the number of file dates that will be generated. Each file type 
# (CCLF1, CCLF2...) supports 9 different filename conventions so a single date 
# will result in 18 files (primary file and summary file) 2 dates will result 
# in 36 files and so on. 
number_of_file_days = 3

# Specifies the number of lines that will be written to each file. Note that 
# large numbers of records will take a long time to generate and really provide 
# little to no value for the purposes of this script.
number_of_lines_per_file = 1000

# Specifies the scripts that will be called each time main is executed.
scripts = [
    "./cclf_generators/cclf_1.py", 
    "./cclf_generators/cclf_2.py", 
    "./cclf_generators/cclf_3.py", 
    "./cclf_generators/cclf_4.py", 
    "./cclf_generators/cclf_5.py", 
    "./cclf_generators/cclf_6.py", 
    "./cclf_generators/cclf_7.py", 
    "./cclf_generators/cclf_8.py", 
    "./cclf_generators/cclf_9.py", 
    "./cclf_generators/cclf_a.py", 
    "./cclf_generators/cclf_b.py", 
]

# Convert the arguments to strins.
args = [str(number_of_file_days), str(number_of_lines_per_file)]

for script in scripts:
    # Use sys.executable to get the Python interpreter used to run this script (cross-platform)
    result = subprocess.run([sys.executable, script] + args, capture_output=False, text=True)
