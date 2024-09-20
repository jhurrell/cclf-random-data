# Line CMS Type Service Code
# https://resdac.org/sites/datadocumentation.resdac.org/files/CMS%20Type%20of%20Service%20Table.txt
def get_codes():
    return [
		"1",     # Medical care
		"2",     # Surgery
		"3",     # Consultation
		"4",     # Diagnostic radiology
		"5",     # Diagnostic laboratory
		"6",     # Therapeutic radiology
		"7",     # Anesthesia
		"8",     # Assistant at surgery
		"9",     # Other medical items or services
		"0",     # Whole blood only eff 01/96, whole blood or packed red cells before 01/96
		"A",     # Used durable medical equipment (DME)
		"B",     # High risk screening mammography (obsolete 1/1/98)
		"C",     # Low risk screening mammography (obsolete 1/1/98)
		"D",     # Ambulance (eff 04/95)
		"E",     # Enteral/parenteral nutrients/supplies (eff 04/95)
		"F",     # Ambulatory surgical center (facility usage for surgical services)
		"G",     # Immunosuppressive drugs
		"H",     # Hospice services (discontinued 01/95)
		"I",     # Purchase of DME (installment basis) (discontinued 04/95)
		"J",     # Diabetic shoes (eff 04/95)
		"K",     # Hearing items and services (eff 04/95)
		"L",     # ESRD supplies (eff 04/95) (renal supplier in the home before 04/95)
		"M",     # Monthly capitation payment for dialysis
		"N",     # Kidney donor
		"P",     # Lump sum purchase of DME, prosthetics orthotics
		"Q",     # Vision items or services
		"R",     # Rental of DME
		"S",     # Surgical dressings or other medical supplies (eff 04/95)
		"T",     # Psychological therapy (term. 12/31/97) outpatient mental health limitation (eff. 1/1/98)
		"U",     # Occupational therapy
		"V",     # Pneumococcal/flu vaccine (eff 01/96), Pneumococcal/flu/hepatitis B vaccine (eff 04/95-12/95), Pneumococcal only before 04/95
		"W",     # Physical therapy
		"Y",     # Second opinion on elective surgery (obsoleted 1/97)
		"Z",     # Third opinion on elective surgery (obsoleted 1/97)        
    ]