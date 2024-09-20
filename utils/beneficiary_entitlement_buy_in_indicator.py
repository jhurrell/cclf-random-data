# Beneficiary Entitlement Buy-in Indicator
# (from the PDF)
def get_codes():
    return [
		"0",     # Not Entitled
		"1",     # Part A Only
		"2",     # Part B Only
		"3",     # Part A and Part B
		"A",     # Part A, State Buy-In
		"B",     # Part B, State Buy-In
		"C",     # Parts A and B, State Buy-In 
    ]