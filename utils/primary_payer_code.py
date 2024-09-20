# Line Primary Payer Code (if not Medicare)
# https://resdac.org/cms-data/variables/line-primary-payer-code-if-not-medicare
def get_codes():
    return [
		"A",     # Working aged bene/spouse with employer group health plan (EGHP)
		"B",     # End stage renal disease (ESRD) beneficiary in the 18 month coordination period with an employer group health plan
		"C",     # Conditional payment by Medicare; future reimbursement expected
		"D",     # Automobile no-fault (eff. 4/97; Prior to 3/94, also included any liability insurance)
		"E",     # Workers' compensation
		"F",     # Public Health Service or other federal agency (other than Dept. of Veterans Affairs)
		"G",     # Working disabled bene (under age 65 with LGHP)
		"H",     # Black Lung
		"I",     # Dept. of Veterans Affairs
		"L",     # Any liability insurance (eff. 4/97) (eff. 12/90 for carrier claims and 10/93 for FI claims; obsoleted for all claim types 7/1/96)
		"M",     # Override code: EGHP services involved (eff. 12/90 for carrier claims and 10/93 for FI claims; obsoleted for all claim types 7/1/96)
		"N",     # Override code: non-EGHP services involved (eff. 12/90 for carrier claims and 10/93 for FI claims; obsoleted for all claim types 7/1/96)
		"W",     # Workers’ Compensation Medicare Set-Aside Arrangement (WCMSA)
		"",     # Medicare is primary payer
    ]