# Carrier Claim Payment Denial Code
# https://resdac.org/cms-data/variables/carrier-claim-payment-denial-code
def get_codes():
    return [

        # Only one-byte was used until 1/2011 (currently, either 1- or 2-byte values may be used, symbols not currently allowed)
		"0",     # Denied
		"1",     # Physician/supplier
		"2",     # Beneficiary
		"3",     # Both physician/supplier and beneficiary
		"4",     # Hospital (hospital-based physicians)
		"5",     # Both hospital and beneficiary
		"6",     # Group practice prepayment plan
		"7",     # Other entries (e.g., Employer, union)
		"8",     # Federally funded
		"9",     # PA service
		"A",     # Beneficiary under limitation of liability
		"B",     # Physician/supplier under limitation of liability
		"D",     # Denied due to demonstration involvement
		"E",     # MSP cost avoided IRS/SSA/HCFA Data Match (after 01/2001 is First Claim Development)
		"F",     # MSP cost avoided HMO Rate Cell (after 1/2001 is Trauma Code Development)
		"G",     # MSP cost avoided Litigation Settlement (after 1/2001 is Secondary Claims Investigation)
		"H",     # MSP cost avoided Employer Voluntary Reporting (after 1/2001 is Self-Reports)
		"J",     # MSP cost avoided Insurer Voluntary Reporting (eff. 7/3/2000)
		"K",     # MSP cost avoided Initial Enrollment Questionnaire (eff. 7/3/2000)
		"P",     # Physician ownership denial
		"Q",     # MSP cost avoided â€” voluntary agreements including with employer
		"T",     # MSP cost avoided â€” Initial Enrollment Questionnaire
		"U",     # MSP cost avoided â€” HMO rate cell adjustment
		"V",     # MSP cost avoided â€” litigation settlement
		"X",     # MSP cost avoided â€” generic
		"Y",     # MSP cost avoided â€” IRS/SSA data match
		"00",     # MSP cost avoided â€” COB Contractor
		"12",     # MSP cost avoided â€” BC/BS Voluntary Data Sharing Agreements (VDSA)
		"13",     # MSP cost avoided â€” Office of Personnel Management (OPM) Data Match
		"14",     # MSP cost avoided â€” Workman's Compensation (WC) Data Match
		"15",     # MSP cost avoided â€” Workman's Compensation Insurer Voluntary Data Sharing Agreements (WC VDSA)
		"16",     # MSP cost avoided â€” Liability Insurer VDSA
		"17",     # MSP cost avoided â€” No-Fault Insurer VDSA
		"18",     # MSP cost avoided â€” Pharmacy Benefit Manager Data Sharing Agreement
		"19",     # MSP cost avoided â€” Workerâ€™s Compensation Medicare Set-Aside Arrangement (eff. 4/2006)
		"21",     # MSP cost avoided â€” MIR Group Health Plan
		"22",     # MSP cost avoided â€” MIR non-Group Health Plan
		"25",     # MSP cost avoided â€” Recovery Audit Contractor â€” California
		"26",     # MSP cost avoided â€” Recovery Audit Contractor â€” Florida
		"41",     # MSP cost avoided â€” non-Group Health Plan non-Ongoing responsibility for medical (ORM)
		"43",     # MSP cost avoided â€” Medicare Part C/Medicare Advantage

        # Prior to 2011, the following 1-byte character codes were also valid (these characters preceded use of 2-byte codes, above):
		"!",     # MSP cost avoided â€” COB Contractor (converted to '00' 2-byte code)
		"@",     # MSP cost avoided â€” BC/BS Voluntary Agreements (converted to '12' 2-byte code)
		"#",     # MSP cost avoided â€” Office of Personnel Management (converted to '13' 2-byte code)
		"$",     # MSP cost avoided â€” Workman's Compensation (WC) Datamatch (converted to '14' 2-byte code)
		"*",     # MSP cost avoided â€” Workman's Compensation Insurer Voluntary Data Sharing Agreements (WC VDSA) (eff. 4/2006) (converted to '15' 2-byte code)
		"(",     # MSP cost avoided â€” Liability Insurer VDSA (eff. 4/2006) (converted to '16' 2-byte code)
		")",     # MSP cost avoided â€” No-Fault Insurer VDSA (eff. 4/2006) (converted to '17' 2-byte code)
		"+",     # MSP cost avoided â€” Pharmacy Benefit Manager Data Sharing Agreement (eff. 4/2006) (converted to '18' 2-byte code)
		"<",     # MSP cost avoided â€” MIR Group Health Plan (eff. 1/2009) (converted to '21' 2-byte code)
		">",     # MSP cost avoided â€” MIR non-Group Health Plan (eff. 1/2009) (converted to '22' 2-byte code)
		"%",     # MSP cost avoided â€” Recovery Audit Contractor â€” California (eff. 10/2005) (converted to '25' 2-byte code)
		"&",     # MSP cost avoided â€” Recovery Audit Contractor â€” Florida (eff. 10/2005) (converted to '26' 2-byte code)
    ]
