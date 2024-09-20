# Claim Service Classification Type Codes
# https://resdac.org/sites/datadocumentation.resdac.org/files/Claim%20Service%20Classification%20Type%20Code%20Table.txt
def get_codes():
    return [
        # For facility type code 1 thru 6, and 9:
        "1",      # Inpatient
        "2",      # Inpatient or Home Health (covered on Part B)
        "3",      # Outpatient (or HHA â€” covered on Part A)
        "4",      # Other (Part B) â€” (includes HHA medical and other health services, e.g., SNF osteoporosis injectable drugs)
        "5",      # Intermediate care â€” level I
        "6",      # Intermediate care â€” level II
        "7",      # Subacute Inpatient (revenue code 019X required) (formerly Intermediate care â€” level III)
        "8",      # Swing bed
        
        # For facility type code 7 (clinics):
        "1",      # Rural Health Clinic (RHC)
        "2",      # Hospital based or independent renal dialysis facility
        "3",      # Free-standing provider based federally qualified health center (FQHC)
        "4",      # Other Rehabilitation Facility (ORF)
        "5",      # Comprehensive Rehabilitation Center (CORF)
        "6",      # Community Mental Health Center (CMHC)
        "7",      # Federally Qualified Health Center (FQHC)

        # For facility type code 8 (special facility):
        "1",      # Hospice (non-hospital based)
        "2",      # Hospice (hospital based)
        "3",      # Ambulatory surgical center (ASC) in hospital outpatient department
        "4",      # Freestanding birthing center
        "5",      # Critical Access Hospital â€” outpatient services
        "7",      # Freestanding Non-residential Opioid Treatment Programs (eff. 1/2021)
]