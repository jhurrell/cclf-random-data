# Claim Admission Type Code: Indicates the type and priority of impatient services.
# (from the PDF)
def get_codes():
    return [
        "0",      # Blank
        "1",      # Emergency
        "2",      # Urgent
        "3",      # Elective
        "4",      # Newborn
        "5",      # Trauma Center
        "6",      # Reserved
        "7",      # Reserved
        "8",      # Reserved
        "9",      # Unknown
    ]