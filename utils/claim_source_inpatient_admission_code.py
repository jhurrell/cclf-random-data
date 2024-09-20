# Claim Source Inpatient Admission Codes (FFS)
# https://resdac.org/cms-data/variables/claim-source-inpatient-admission-code-ffs
def get_codes():
    return [
        # For inpatient/SNF claims:
        "0",      # ANOMALY: invalid value, if present, translate to â€œ9â€
        "1",      # Non-Health Care Facility Point of Origin (Physician Referral) â€” the patient was admitted to this facility upon an order of a physician
        "2",      # Clinic referral â€” the patient was admitted upon the recommendation of this facility's clinic physician
        "3",      # HMO referral â€” reserved for national Prior to 3/08, HMO referral â€” the patient was admitted upon the recommendation of a health maintenance organization (HMO) physician
        "4",      # Transfer from hospital (Different Facility) â€” the patient was admitted to this facility as a hospital transfer from an acute care facility where he or she was an inpatient
        "5",      # Transfer from a skilled nursing facility (SNF) or Intermediate Care Facility (ICF) â€” the patient was admitted to this facility as a transfer from a SNF or ICF where he or she was a resident
        "6",      # Transfer from another health care facility â€” the patient was admitted to this facility as a transfer from another type of health care facility not defined elsewhere in this code list where he or she was an inpatient
        "7",      # Emergency room â€” the patient was admitted to this facility after receiving services in this facility's emergency room department (CMS discontinued this code 07/2010, although a small number of claims with this code appear after that time)
        "8",      # Court/law enforcement â€” the patient was admitted upon the direction of a court of law or upon the request of a law enforcement agency's representative
        "9",      # Information not available â€” how the patient was admitted is not known
        "A",      # Reserved for national assignment. (eff. 3/08) Prior to 3/08 defined as: Transfer from a critical access hospital â€” patient was admitted/referred to this facility as a transfer from a critical access hospital

        # For Newborn Type of Admission:
        "1",      # Normal delivery â€” a baby delivered without complications
        "2",      # Premature delivery â€” a baby delivered with time and/or weight factors qualifying it for premature status
        "3",      # Sick baby â€” a baby delivered with medical complications, other than those relating to premature status
        "4",      # Extramural birth â€” a baby delivered in a nonsterile environment
        "5",      # Reserved for national assignment
        "6",      # Reserved for national assignment
        "7",      # Reserved for national assignment
        "8",      # Reserved for national assignment
        "9",      # Information not available
    ]