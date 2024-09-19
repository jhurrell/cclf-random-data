# utils.py
import os
import random
import string
from datetime import timedelta

def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_days = random.randint(0, time_between_dates.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

def random_alpha_string(length):
    characters = string.ascii_letters
    return ''.join(random.choices(characters, k=length)).upper()

def random_num_string(length):
    characters = string.digits
    return ''.join(random.choices(characters, k=length))

def random_alphanum_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length)).upper()

def random_int_in_range(min_value, max_value):
    return str(random.randint(min_value, max_value))

def random_int_by_len(length):
    characters = string.digits
    return ''.join(random.choices(characters, k=length))

# Random float between a and b
def random_float_in_range(a, b, length):
    # Generate a random float between a and b
    random_float = random.uniform(a, b)
    # Randomly decide whether to make it positive or negative
    sign = random.choice([-1, 1])
    # Apply the sign and round to 2 decimal places
    return str(round(random_float * sign, 2)).ljust(length)    

def random_choice_from_array(arr):
    return random.choice(arr)

def generate_files(type, date, contents):
    print(f"{type} for {date} processing...")

    # Describe the mapping between the file type and the ZC suffix.
    suffix_map = { 
        "CCLF1": "1", 
        "CCLF2": "2", 
        "CCLF3": "3", 
        "CCLF4": "4", 
        "CCLF5": "5", 
        "CCLF6": "6", 
        "CCLF7": "7", 
        "CCLF8": "8", 
        "CCLF9": "9", 
        "CCLFA": "A", 
        "CCLFB": "B", 
    }
    sfx = suffix_map[type]

    # Generate random characters to fill the filenames.
    rand_a = random_alpha_string(3)
    rand_b = random_alpha_string(2)

    # Define the filename patterns for the main types.
    primary_file_patterns = {
        f"P.A{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.A{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC{sfx}R{rand_b}.D{date}.T010203t",
        f"P.K{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.C{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
        f"P.P{rand_a}.ACO.ZC{sfx}Y{rand_b}.D{date}.T010203t",
    }

    # Define the path for the files.
    directory = f"./output/{type}"
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # Emit the generated data for the primary file.
    for file in primary_file_patterns:
        print(f"\tCreating {type} {file}...")
        with open(f"{directory}/{file}", "w") as f:
            f.write(contents)  


    # Define the filename patterns for the Summary Statistics.
    summary_file_patterns = {
        f"P.A{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.A{rand_a}.ACO.ZC0R{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.F{rand_a}.ACO.ZC0R{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.D{rand_a}.ACO.ZC0R{rand_b}.D{date}.T010203t",
        f"P.K{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.C{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",
        f"P.P{rand_a}.ACO.ZC0Y{rand_b}.D{date}.T010203t",        
    }

    # Describe the mapping between the type and the name that will appear in the 
    # Summary Statistics.
    name_map = { 
        "CCLF1": "Part A Claims Header File.", 
        "CCLF2": "Part A Claims Revenue Center Detail File.", 
        "CCLF3": "Part A Procedure Code File.", 
        "CCLF4": "Part A Diagnosis Code File", 
        "CCLF5": "Part B Physicians File.", 
        "CCLF6": "Part B DME File.", 
        "CCLF7": "Part D File.", 
        "CCLF8": "Beneficiary Demographics File.", 
        "CCLF9": "BENE XREF File.", 
        "CCLFA": "Part A BE and Demo Codes File.", 
        "CCLFB": "Part B BE and Demo Codes File.", 
    }
    name = name_map[type]              

    # Emit data for the summary files.
    for file in summary_file_patterns:
        print(f"\tCreating CCLF0 {file}...")
        with open(f"{directory}/{file}", "w") as f:
            # Table 25
            f.write(f"{"123".ljust(13)}|{"WHATEVER".ljust(20)}|{"456".ljust(20)}|{"789".ljust(13)}\n")            

            # Table 26
            if file.startswith(("P.A", "P.F", "P.P")):
                f.write(f"{str(type).ljust(7)}|{name.ljust(43)}|{"456".ljust(11)}|{"789".ljust(5)}{str().ljust(1)}\n")
