# script_a.py
import subprocess

# Define the command and arguments
number_of_file_days = 1
number_of_lines_per_file = 1000

commands = [
    ["python3", "cclf_1.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_2.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_3.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_4.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
    ["python3", "cclf_5.py", f"{number_of_file_days}", f"{number_of_lines_per_file}"],
]

# Call the script with arguments
for command in commands:
    result = subprocess.run(command, capture_output=True, text=True)

