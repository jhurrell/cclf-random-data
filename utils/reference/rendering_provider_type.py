#  Rendering Provider Type Code: Indicates the type of provider who provided the service associated with this line item on the claim.
# (from the PDF)
def get_codes():
    return [
        "0",     # Clinics, groups, associations, partnerships, or other entities
        "1",     # Physicians or suppliers reporting as solo practitioners
        "2",     # Suppliers (other than sole proprietorship)
        "3",     # Institutional provider
        "4",     # Independent laboratories
        "5",     # Clinics (multiple specialties)
        "6",     # Groups (single specialty)
        "7",     # Other entities
        "8",     # Family Practice
        "UI",     # UPIN Identification
        "N2",     # National Council for Prescription Drug Programs
        "D",     # National Supplier Clearinghouse
        "BP",     # PIN Individual    
        "BG",     # PIN Group
        "A",     # Online Survey, Certification and Reporting
    ]