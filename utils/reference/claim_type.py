# Claim Type Codes
# (from the PDF)
def get_codes():
    return [
        "10",      # HHA claim
        "20",      # Non swing bed SNF claim
        "30",      # Swing bed SNF claim
        "40",      # Outpatient claim
        "50",      # Hospice claim
        "60",      # Inpatient claim
        "61",      # Inpatient “Full-Encounter” claim
        "71",      # RIC O local carrier non-DMEPOS claim (CCLF5)
        "71",      # RIC O local carrier DMEPOS claim (CCLF5)
    ]