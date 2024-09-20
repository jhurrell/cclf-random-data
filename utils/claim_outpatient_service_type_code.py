# A code reported by the provider that indicates the specific type of claim (Inpatient, Outpatient, etc.). 
# (from the PDF)
def get_codes():
    return [
        "0",      # Blank
        "1",      # Emergency (The patient required immediate medical intervention because of severe life threatening or potentially disabling conditions. Generally, the patient was admitted through the emergency room)
        "2",      # Urgent (The patient required immediate attention for the care and treatment of a physical or mental disorder. Generally, the patient was admitted to the available and suitable accommodation)
        "3",      # Elective (The patient's condition permitted adequate time to schedule the availability of suitable accommodations)
        "5",      # Reserved
        "6",      # Reserved
        "7",      # Reserved
        "8",      # Reserved
        "9",      # Unknown (Information not available)
    ]
