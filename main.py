# script_a.py
import subprocess

# Specifies the number of file dates that will be generated. Each file type 
# (CCLF1, CCLF2...) supports 9 different filename conventions so a single date 
# will result in 18 files (primary file and summary file) 2 dates will result 
# in 36 files and so on. 
number_of_file_days = 1

# Specifies the number of lines that will be written to each file. Note that 
# large numbers of records will take a long time to generate and really provide 
# little to no value for the purposes of this script.
number_of_lines_per_file = 1000

# Specifies the scripts that will be called each time main is executed.
commands = [
    ["python3", "cclf_1.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_2.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_3.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_4.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_5.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_6.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_7.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_8.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_9.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_a.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_b.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
]

# Enumerate over each command and execute.
for command in commands:
    result = subprocess.run(command, capture_output=False, text=True)
