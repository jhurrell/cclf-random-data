# Beneficiary Dual Status Code
# https://resdac.org/cms-data/variables/edual1-12
def get_codes():
    return [
		"00",     # Not Medicare Enrolled
		"01",     # QMB Only
		"02",     # QMB + full Medicaid
		"03",     # SLMB-only
		"04",     # SLMB + full dual Medicaid benefits
		"05",     # QWDI
		"06",     # QI
		"08",     # Other full benefit
		"09",     # Other dual eligible without Medicaid
		"99",     # Unknown
		"NA",     # Non Medicaid
		"XX",     # Enrolled in Medicare, no MIIR record        
    ]