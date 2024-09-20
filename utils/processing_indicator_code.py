# Line Processing Indicator Code
# https://resdac.org/cms-data/variables/line-processing-indicator-code
def get_codes():
    return [
		"A",     # Allowed
		"B",     # Benefits exhausted
		"C",     # Non-covered care
		"D",     # Denied (from BMAD)
		"G",     # MSP cost avoided â€” Secondary Claims Investigation
		"H",     # MSP cost avoided â€” Self Reports
		"I",     # Invalid data
		"J",     # MSP cost avoided â€” 411.25
		"K",     # MSP cost avoided â€” Insurer Voluntary Reporting
		"L",     # CLIA
		"M",     # Multiple submittal-duplicate line item
		"N",     # Medically unnecessary
		"O",     # Other
		"P",     # Physician ownership denial
		"Q",     # MSP cost avoided (contractor #88888) â€” voluntary agreement
		"R",     # Reprocessed adjustments based on subsequent reprocessing of claim
		"S",     # Secondary payer
		"T",     # MSP cost avoided â€” IEQ contractor
		"U",     # MSP cost avoided â€” HMO rate cell adjustment
		"V",     # MSP cost avoided â€” litigation settlement
		"X",     # MSP cost avoided â€” generic
		"Y",     # MSP cost avoided â€” IRS/SSA data match project
		"Z",     # Bundled test, no payment
		"00",     # MSP cost avoided â€” COB Contractor
		"12",     # MSP cost avoided â€” BC/BS Voluntary Agreements
		"13",     # MSP cost avoided â€” Office of Personnel Management
		"14",     # MSP cost avoided â€” Workman's Compensation (WC) Datamatch
		"15",     # MSP cost avoided â€” Workman's Compensation Insurer Voluntary Data Sharing Agreements (WC VDSA) (eff. 4/2006)
		"16",     # MSP cost avoided â€” Liability Insurer VDSA (eff.4/2006)
		"17",     # MSP cost avoided â€” No-Fault Insurer VDSA (eff.4/2006)
		"18",     # MSP cost avoided â€” Pharmacy Benefit Manager Data Sharing Agreement (eff.4/2006)
		"21",     # MSP cost avoided â€” MIR Group Health Plan (eff.1/2009)
		"22",     # MSP cost avoided â€” MIR non-Group Health Plan (eff.1/2009)
		"25",     # MSP cost avoided â€” Recovery Audit Contractor â€” California (eff.10/2005)
		"26",     # MSP cost avoided â€” Recovery Audit Contractor â€” Florida (eff.10/2005)
		"!",     # MSP cost avoided â€” COB Contractor ('00' 2-byte code)
		"@",     # MSP cost avoided â€” BC/BS Voluntary Agreements ('12' 2-byte code)
		"#",     # MSP cost avoided â€” Office of Personnel Management ('13' 2-byte code)
		"$",     # MSP cost avoided â€” Workman's Compensation (WC) Datamatch ('14' 2-byte code)
		"*",     # MSP cost avoided â€” Workman's Compensation Insurer Voluntary Data Sharing Agreements (WC VDSA) ('15' 2-byte code) (eff. 4/2006)
		"(",     # MSP cost avoided â€” Liability Insurer VDSA ('16' 2-byte code) (eff. 4/2006)
		")",     # MSP cost avoided â€” No-Fault Insurer VDSA ('17' 2-byte code) (eff. 4/2006)
		"+",     # MSP cost avoided â€” Pharmacy Benefit Manager Data Sharing Agreement ('18' 2-byte code) (eff. 4/2006)
		"<",     # MSP cost avoided â€” MIR Group Health Plan ('21' 2-byte code) (eff. 1/2009)
		">",     # MSP cost avoided â€” MIR non-Group Health Plan ('22' 2-byte code) (eff. 1/2009)
		"%",     # MSP cost avoided â€” Recovery Audit Contractor â€” California ('25' 2-byte code) (eff. 10/2005)
		"&",     # MSP cost avoided â€” Recovery Audit Contractor â€” Florida ('26' 2-byte code) (eff. 10/2005)
    ]