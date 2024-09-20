# Claim Dispense as Written (DAW) Product Selection Code
# (from the PDF)
def get_codes():
    return [
		"0",     # No product selection indicated
		"1",     # Substitution not allowed by prescriber
		"2",     # Substitution allowed – Patient requested that brand be dispensed
		"3",     # Substitution allowed – Pharmacist selected product dispensed
		"4",     # Substitution allowed – Generic not in stock
		"5",     # Substitution allowed – Brand drug dispensed as generic
		"6",     # Override
		"7",     # Substitution not allowed – Brand drug mandated by law
		"8",     # Substitution allowed – Generic drug not available in marketplace
		"9",     # Other        
    ]