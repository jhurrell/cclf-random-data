# cclf_0.py
import sys
import os
import shutil
from utils import random_int_by_len, random_alpha_string, random_alphanum_string, random_choice_from_array, random_date, random_float_in_range, random_int_in_range
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
    number_of_lines_per_file = 100

# Define the path for the file
directory = "./cclf/cclf_0"
shutil.rmtree(directory)
if not os.path.exists(directory):
    os.makedirs(directory, exist_ok=True)

# Replicate the contents to each of the file types.
def generate_files(file_date, contents):
    files = {
        f"P.A{random_alpha_string(3)}.ACO.ZC0Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.A{random_alpha_string(3)}.ACO.ZC0R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC0Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC0R{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC0Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.D{random_alpha_string(3)}.ACO.ZC0Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.K{random_alpha_string(3)}.ACO.ZC0Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.C{random_alpha_string(3)}.ACO.ZC0Y{random_alpha_string(2)}.D{file_date}.T010203t",
        f"P.F{random_alpha_string(3)}.ACO.ZC0Y{random_alpha_string(2)}.D{file_date}.T010203t",
    }

    for file in files:
        print(f"\tCreating {file}...")
        with open(f"{directory}/{file}", "w") as f:
            f.write(contents)

# Create n days worth of files.
for index in range(number_of_file_days):
    # Initialize the file contents.
    table_25 = ""
    table_26 = ""

    for _ in range(number_of_lines_per_file):
        # table_25 1-7
        table_25 = table_25 + random_int_in_range(1, 999999999).ljust(13)   # 1 File Number Label
        table_25 = table_25 + "|"                                           # 2 Delimiter
        table_25 = table_25 + random_alpha_string(20)                       # 3 File DescriptionLabel
        table_25 = table_25 + "|"                                           # 4 Delimiter
        table_25 = table_25 + random_int_in_range(1, 999999999).ljust(20)   # 5 Total Records Count Label
        table_25 = table_25 + "|"                                           # 6 Delimiter
        table_25 = table_25 + random_int_in_range(1, 999999999).ljust(13)   # 7 Record Length Label
        table_25 = table_25 + "\n"

        # table_26 1-8
        table_26 = table_26 + "CCLF" + random_choice_from_array(["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B"])
        table_26 = table_26 + "|"
        table_26 = table_26 + random_alpha_string(43)


    delta = timedelta(days=index)
    file_date = (datetime(2024, 1, 1) + delta).strftime("%y%m%d")
    print(f"CCLFB: Generating files for file_date {file_date}...")
    generate_files(file_date, table_25)            