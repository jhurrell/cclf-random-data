# Revenue Center Code (FFS)
# https://resdac.org/cms-data/variables/revenue-center-code-ffs
def get_codes():
    return [
        "0001",     # Total charge
        "0022",     # SNF claim paid under PPS submitted as type of bill (TOB)
        "21X",     # NOTE: This code may appear multiple times on a claim to identify different HIPPS Rate Code/assessment periods. 
        "0023",     # Home health services paid under PPS submitted as TOB 32X and 33X, eff. 10/2000. This code may appear multiple times on a claim to identify different HIPPS/home health Resource Groups (HRG) 
        "0024",     # Inpatient rehabilitation facility services paid under PPS submitted as TOB 11X, eff. for cost reporting periods beginning on or after 1/1/2002 (dates of service after 12/31/2001). This code may appear only once on a claim 
        "0100",     # All-inclusive rate room and board plus ancillary
        "0101",     # All-inclusive rate room and board
        "0110",     # Private medical or general general classification
        "0111",     # Private medical or general medical/surgical/GYN
        "0112",     # Private medical or general OB
        "0113",     # Private medical or general pediatric
        "0114",     # Private medical or general psychiatric
        "0115",     # Private medical or general hospice
        "0116",     # Private medical or general detoxification
        "0117",     # Private medical or general oncology
        "0118",     # Private medical or general rehabilitation
        "0119",     # Private medical or general other
        "0120",     # Semi-private 2 bed (medical or general) general classification
        "0121",     # Semi-private 2 bed (medical or general) medical/surgical/GYN
        "0122",     # Semi-private 2 bed (medical or general) OB
        "0123",     # Semi-private 2 bed (medical or general) pediatric
        "0124",     # Semi-private 2 bed (medical or general) psychiatric
        "0125",     # Semi-private 2 bed (medical or general) hospice
        "0126",     # Semi-private 2 bed (medical or general) detoxification
        "0127",     # Semi-private 2 bed (medical or general) oncology
        "0128",     # Semi-private 2 bed (medical or general) rehabilitation
        "0129",     # Semi-private 2 bed (medical or general) other
        "0130",     # Semi-private 3 and 4 beds general classification
        "0131",     # Semi-private 3 and 4 beds medical/surgical/GYN
        "0132",     # Semi-private 3 and 4 beds OB
        "0133",     # Semi-private 3 and 4 beds pediatric
        "0134",     # Semi-private 3 and 4 beds psychiatric
        "0135",     # Semi-private 3 and 4 beds hospice
        "0136",     # Semi-private 3 and 4 beds detoxification 
        "0137",     # Semi-private 3 and 4 beds oncology
        "0138",     # Semi-private 3 and 4 beds rehabilitation
        "0139",     # Semi-private 3 and 4 beds other
        "0140",     # Private (deluxe)-general classification
        "0141",     # Private (deluxe) medical/surgical/GYN
        "0142",     # Private (deluxe) OB
        "0143",     # Private (deluxe) pediatric
        "0144",     # Private (deluxe) psychiatric
        "0145",     # Private (deluxe) hospice
        "0146",     # Private (deluxe) detoxification
        "0147",     # Private (deluxe) oncology
        "0148",     # Private (deluxe) rehabilitation
        "0149",     # Private (deluxe) other
        "0150",     # Room and Board ward (medical or general) general classification
        "0151",     # Room and Board ward (medical or general) medical/surgical/GYN
        "0152",     # Room and Board ward (medical or general) OB
        "0153",     # Room and Board ward (medical or general) pediatric
        "0154",     # Room and Board ward (medical or general) psychiatric
        "0155",     # Room and Board ward (medical or general) hospice
        "0156",     # Room and Board ward (medical or general) detoxification
        "0157",     # Room and Board ward (medical or general) oncology
        "0158",     # Room and Board ward (medical or general) rehabilitation
        "0159",     # Room and Board ward (medical or general) other
        "0160",     # Other Room and Board general classification
        "0161",     # Hospital at home, RandB/hospital at home (eff. for claims received on or after July 1, 2022)
        "0164",     # Other Room and Board sterile environment
        "0167",     # Other Room and Board self care
        "0169",     # Other Room and Board other
        "0170",     # Nursery-general classification
        "0171",     # Nursery newborn level I (routine)
        "0172",     # Nursery premature newborn-level II (continuing care)
        "0173",     # Nursery newborn-level III (intermediate care)
        "0174",     # Nursery newborn-level IV (intensive care)
        "0179",     # Nursery other
        "0180",     # Leave of absence general classification
        "0182",     # Leave of absence patient convenience charges billable
        "0183",     # Leave of absence therapeutic leave
        "0184",     # Leave of absence-ICF mentally retarded any reason 
        "0185",     # Leave of absence nursing home (hospitalization)
        "0189",     # Leave of absence other leave of absence
        "0190",     # Subacute care general classification
        "0191",     # Subacute care level I
        "0192",     # Subacute care level II
        "0193",     # Subacute care level III
        "0194",     # Subacute care level IV
        "0199",     # Subacute care other
        "0200",     # Intensive care general classification
        "0201",     # Intensive care surgical
        "0202",     # Intensive care medical
        "0203",     # Intensive care pediatric
        "0204",     # Intensive care psychiatric
        "0206",     # Intensive careâ€”post ICU; redefined as intermediate ICU
        "0207",     # Intensive care burn care
        "0208",     # Intensive care trauma
        "0209",     # Intensive care other intensive care
        "0210",     # Coronary care general classification
        "0211",     # Coronary care myocardial infraction
        "0212",     # Coronary care pulmonary care
        "0213",     # Coronary care heart transplant
        "0214",     # Coronary care post CCU; redefined as intermediate CCU
        "0219",     # Coronary care other coronary care
        "0220",     # Special charges general classification
        "0221",     # Special charges admission charge
        "0222",     # Special charges technical support charge
        "0223",     # Special charges UR service charge
        "0224",     # Special charges late discharge, medically necessary
        "0229",     # Special charges other special charges
        "0230",     # Incremental nursing charge rate general classification
        "0231",     # Incremental nursing charge rate nursery
        "0232",     # Incremental nursing charge rate OB
        "0233",     # Incremental nursing charge rate ICU (include transitional care)
        "0234",     # Incremental nursing charge rate CCU (include transitional care)
        "0235",     # Incremental nursing charge rate hospice
        "0239",     # Incremental nursing charge rate other
        "0240",     # All-inclusive ancillary general classification
        "0241",     # All-inclusive ancillary basic
        "0242",     # All-inclusive ancillary comprehensive 
        "0243",     # All-inclusive ancillary specialty
        "0249",     # All-inclusive ancillary other inclusive ancillary
        "0250",     # Pharmacy general classification
        "0251",     # Pharmacy generic drugs
        "0252",     # Pharmacy nongeneric drugs
        "0253",     # Pharmacy take home drugs
        "0254",     # Pharmacy drugs incident to other diagnostic service-subject payment limit
        "0255",     # Pharmacy drugs incident to radiology-subject to payment limit
        "0256",     # Pharmacy experimental drugs
        "0257",     # Pharmacy non-prescription
        "0258",     # Pharmacy IV solutions
        "0259",     # Pharmacy other pharmacy
        "0260",     # IV therapy general classification
        "0261",     # IV therapy infusion pump
        "0262",     # IV therapy pharmacy services
        "0263",     # IV therapy drug supply/delivery
        "0264",     # IV therapy supplies
        "0269",     # IV therapy other IV therapy
        "0270",     # Medical/surgical supplies general classification (also reference 062X)
        "0271",     # Medical/surgical supplies nonsterile supply
        "0272",     # Medical/surgical supplies sterile supply 
        "0273",     # Medical/surgical supplies take home supplies
        "0274",     # Medical/surgical supplies prosthetic/orthotic devices
        "0275",     # Medical/surgical supplies pacemaker
        "0276",     # Medical/surgical supplies intraocular lens
        "0277",     # Medical/surgical supplies oxygen-take home
        "0278",     # Medical/surgical supplies other implants
        "0279",     # Medical/surgical supplies other devices
        "0280",     # Oncology general classification
        "0289",     # Oncology other oncology
        "0290",     # DME (other than renal) general classification
        "0291",     # DME (other than renal) rental
        "0292",     # DME (other than renal) purchase of new DME
        "0293",     # DME (other than renal) purchase of used DME
        "0294",     # DME (other than renal) related to and listed as DME
        "0299",     # DME (other than renal) other
        "0300",     # Laboratory general classification
        "0301",     # Laboratory chemistry
        "0302",     # Laboratory immunology 
        "0303",     # Laboratory renal patient (home)
        "0304",     # Laboratory non-routine dialysis
        "0305",     # Laboratory hematology
        "0306",     # Laboratory bacteriology and microbiology
        "0307",     # Laboratory urology
        "0308",     # Reserved laboratory
        "0309",     # Laboratory other laboratory
        "0310",     # Laboratory pathological general classification
        "0311",     # Laboratory pathological cytology
        "0312",     # Laboratory pathological histology
        "0314",     # Laboratory pathological biopsy
        "0319",     # Laboratory pathological other
        "0320",     # Radiology diagnostic general classification
        "0321",     # Radiology diagnostic angiocardiography
        "0322",     # Radiology diagnostic arthrography
        "0323",     # Radiology diagnostic arteriography
        "0324",     # Radiology diagnostic chest X-ray
        "0327",     # Reserved radiology, diagnostic
        "0329",     # Radiology diagnostic other
        "0330",     # Radiology therapeutic general classification
        "0331",     # Radiology therapeutic chemotherapy injected
        "0332",     # Radiology therapeutic chemotherapy oral
        "0333",     # Radiology therapeutic radiation therapy
        "0335",     # Radiology therapeutic chemotherapy IV
        "0339",     # Radiology therapeutic other
        "0340",     # Nuclear medicine general classification
        "0341",     # Nuclear medicine diagnostic
        "0342",     # Nuclear medicine therapeutic
        "0343",     # Nuclear medicine diagnostic radiopharmaceuticals
        "0344",     # Nuclear medicine therapeutic radiopharmaceuticals
        "0349",     # Nuclear medicine other
        "0350",     # Computed tomographic (CT) scan general classification
        "0351",     # CT scan head scan
        "0352",     # CT scan body scan
        "0359",     # CT scan other CT scans
        "0360",     # Operating room services general classification
        "0361",     # Operating room services minor surgery
        "0362",     # Operating room services organ transplant, other than kidney
        "0363",     # Reserved operating room services
        "0367",     # Operating room services kidney transplant 
        "0368",     # Reserved operating room services
        "0369",     # Operating room services other operating room services
        "0370",     # Anesthesia general classification
        "0371",     # Anesthesia incident to RAD and subject to the payment limit
        "0372",     # Anesthesia incident to other diagnostic service and subject to the payment limit
        "0374",     # Anesthesia acupuncture
        "0379",     # Anesthesia other anesthesia
        "0380",     # Blood general classification
        "0381",     # Blood packed red cells
        "0382",     # Blood whole blood
        "0383",     # Blood plasma
        "0384",     # Blood platelets
        "0385",     # Blood leukocytes
        "0386",     # Blood other components
        "0387",     # Blood other derivatives (cryoprecipitates)
        "0389",     # Blood other blood
        "0390",     # Blood storage and processing general classification
        "0391",     # Blood storage and processing blood administration
        "0392",     # Blood storage and processing storage and processing
        "0399",     # Blood storage and processing other
        "0400",     # Other imaging services general classification
        "0401",     # Other imaging services diagnostic mammography
        "0402",     # Other imaging services ultrasound
        "0403",     # Other imaging services screening mammography
        "0404",     # Other imaging services positron emission tomography
        "0405",     # Reserved imaging services
        "0409",     # Other imaging services other
        "0410",     # Respiratory services general classification
        "0412",     # Respiratory services inhalation services
        "0413",     # Respiratory services hyperbaric oxygen therapy
        "0419",     # Respiratory services other
        "0420",     # Physical therapy general classification
        "0421",     # Physical therapy visit charge
        "0422",     # Physical therapy hourly charge
        "0423",     # Physical therapy group rate
        "0424",     # Physical therapy evaluation or re-evaluation
        "0429",     # Physical therapy other
        "0430",     # Occupational therapy general classification
        "0431",     # Occupational therapy visit charge
        "0432",     # Occupational therapy hourly charge
        "0433",     # Occupational therapy group rate 
        "0434",     # Occupational therapy evaluation or re-evaluation
        "0439",     # Occupational therapy other (may include restorative therapy)
        "0440",     # Speech language pathology general classification
        "0441",     # Speech language pathology visit charge
        "0442",     # Speech language pathology hourly charge
        "0443",     # Speech language pathology group rate
        "0444",     # Speech language pathology evaluation or re-evaluation
        "0445",     # Reserved speech therapy
        "0449",     # Speech language pathology other
        "0450",     # Emergency room general classification
        "0451",     # Emergency room EMTALA emergency medical screening services
        "0452",     # Emergency room ER beyond EMTALA screening
        "0456",     # Emergency room urgent care
        "0459",     # Emergency room other
        "0460",     # Pulmonary function general classification
        "0461",     # Reserved pulmonary function
        "0469",     # Pulmonary function other
        "0470",     # Audiology general classification
        "0471",     # Audiology diagnostic
        "0472",     # Audiology treatment
        "0479",     # Audiology other
        "0480",     # Cardiology general classification
        "0481",     # Cardiology cardiac cath lab
        "0482",     # Cardiology stress test
        "0483",     # Cardiology Echocardiology
        "0489",     # Cardiology other
        "0490",     # Ambulatory surgical care general classification
        "0499",     # Ambulatory surgical care other
        "0500",     # Outpatient services general classification
        "0509",     # Outpatient services other
        "0510",     # Clinic general classification
        "0511",     # Clinic chronic pain center
        "0512",     # Clinic dental center
        "0513",     # Clinic psychiatric
        "0514",     # Clinic OB-GYN
        "0515",     # Clinic pediatric
        "0516",     # Clinic urgent care clinic
        "0517",     # Clinic family practice clinic
        "0519",     # Clinic other
        "0520",     # Free-standing clinic general classification
        "0521",     # Free-standing clinic clinic visit by a member to RHC/FQHC (eff. 7/1/2006). Prior to 7/1/2006 rural health clinic 
        "0522",     # Free-standing clinic home visit by RHC/FQHC practitioner (eff. 7/2006). Prior to 7/2006 rural health home
        "0523",     # Free-standing clinic family practice
        "0524",     # Free-standing clinic visit by RHC/FQHC practitioner to a member in a covered Part A stay at the SNF. (eff. 7/2006)
        "0525",     # Free-standing clinic visit by RHC/FQHC practitioner to a member in a SNF (not in a covered Part A stay) or NF or ICF MR or other residential facility. (eff. 7/2006)
        "0526",     # Free-standing clinic urgent care (eff. 10/1996)
        "0527",     # Free-standing clinic RHC/FQHC visiting nurse service(s) to a member's home when in a home health shortage area. (eff. 7/2006)
        "0528",     # Free-standing clinic visit by RHC/FQHC practitioner to other non- RHC/FQHC site (e.g., scene of accident). (eff. 7/2006)
        "0529",     # Free-standing clinic other
        "0530",     # Osteopathic services general classification
        "0531",     # Osteopathic services osteopathic therapy
        "0539",     # Osteopathic services other
        "0540",     # Ambulance general classification
        "0541",     # Ambulance supplies
        "0542",     # Ambulance medical transport
        "0543",     # Ambulance heart mobile
        "0544",     # Ambulance oxygen
        "0545",     # Ambulance air ambulance
        "0546",     # Ambulance neo-natal ambulance
        "0547",     # Ambulance pharmacy
        "0548",     # Ambulance â€”transmission EKG
        "0549",     # Ambulance other
        "0550",     # Skilled nursing general classification
        "0551",     # Skilled nursing visit charge
        "0552",     # Skilled nursing hourly charge
        "0559",     # Skilled nursing other
        "0560",     # Medical social services (home health) general classification
        "0561",     # Medical social services (home health) visit charge
        "0562",     # Medical social services (home health) hourly charges
        "0569",     # Medical social services (home health) other
        "0570",     # Home health aide (home health) general classification
        "0571",     # Home health aide (home health) visit charge
        "0572",     # Home health aide (home health) hourly charge
        "0579",     # Home health aide (home health) other
        "0580",     # Other visits (home health) general classification (under HHPPS, not allowed as covered charges)
        "0581",     # Other visits (home health) visit charge (under HHPPS, not allowed as covered charges) 
        "0582",     # Other visits (home health) hourly charge (under HHPPS, not allowed as covered charges)
        "0583",     # Other visits (home health) assessments under HHPPS, not allow as covered charges)
        "0589",     # Other visits (home health) other (under HHPPS, not allowed as covered charges)
        "0590",     # Units of service (home health) general classification (under HHPPS, not allowed as covered charges)
        "0599",     # Units of service (home health) other (under HHPPS, not allowed as covered charges)
        "0600",     # Oxygen (home health) general classification
        "0601",     # Oxygen (home health) stat or port equip/supply or contents
        "0602",     # Oxygen (home health)stat/equip/supply under 1 LPM
        "0603",     # Oxygen (home health) stat/equip/over 4 LPM
        "0604",     # Oxygen (home health) stat/equip/portable add-on
        "0609",     # Oxygen (home health) other
        "0610",     # Magnetic resonance technology (MRT) general classification
        "0611",     # MRT/MRI brain (including brainstem)
        "0612",     # MRT/MRI spinal cord (including spine)
        "0614",     # MRT/MRI other
        "0615",     # MRT/MRA Head and Neck
        "0616",     # MRT/MRA Lower Extremities
        "0618",     # MRT/MRA other
        "0619",     # MRT/Other MRI
        "0620",     # Reserved (Use 0270 for general classification)
        "0621",     # Medical/surgical supplies incident to radiology-subject to the payment limit extension of 027X
        "0622",     # Medical/surgical supplies incident to other diagnostic service-subject to the payment limit extension of 027X
        "0623",     # Medical/surgical supplies surgical dressings extension of 027X
        "0624",     # Medical/surgical supplies medical investigational devices and procedures with FDA approved IDE's extension of 027X
        "0630",     # Reserved
        "0631",     # Drugs requiring specific identification single drug source
        "0632",     # Drugs requiring specific identification multiple drug source
        "0633",     # Drugs requiring specific identification restrictive prescription
        "0634",     # Drugs requiring specific identification Erythropoietin (EPO) under 10,000 units
        "0635",     # Drugs requiring specific identification Erythropoietin (EPO) 10,000 units or more 
        "0636",     # Drugs requiring specific identification detailed coding
        "0637",     # Self-administered drugs administered in an emergency situation not requiring detailed coding
        "0640",     # Home IV therapy general classification
        "0641",     # Home IV therapy nonroutine nursing
        "0642",     # Home IV therapy IV site care, central line
        "0643",     # Home IV therapy IV start/change peripheral line
        "0644",     # Home IV therapy nonroutine nursing, peripheral line
        "0645",     # Home IV therapy train patient/caregiver, central line
        "0646",     # Home IV therapy train disabled patient, central line
        "0647",     # Home IV therapy train patient/caregiver, peripheral line
        "0648",     # Home IV therapy train disabled patient, peripheral line
        "0649",     # Home IV therapy other IV therapy services
        "0650",     # Hospice services general classification
        "0651",     # Hospice services routine home care
        "0652",     # Hospice services continuous home care
        "0655",     # Hospice services inpatient care 
        "0656",     # Hospice services general inpatient care (non-respite)
        "0657",     # Hospice services physician services
        "0659",     # Hospice services other
        "0660",     # Respite care (HHA) general classification
        "0661",     # Respite care (HHA) hourly charge/skilled nursing
        "0662",     # Respite care (HHA) hourly charge/home health aide/homemaker
        "0663",     # Respite care (HHA) - daily respite charge
        "0670",     # OP special residence charges general classification
        "0671",     # OP special residence charges hospital based
        "0672",     # OP special residence charges contracted
        "0679",     # OP special residence charges other special residence charges
        "0680",     # Trauma Response not used
        "0681",     # Trauma response Level I Trauma
        "0682",     # Trauma response Level II Trauma
        "0683",     # Trauma response Level III Trauma
        "0684",     # Trauma response Level IV Trauma
        "0689",     # Trauma response Other trauma response
        "0690",     # Pre-hospice/Palliative Care Services general (eff. 7/2017) 
        "0691",     # Pre-hospice/Palliative Care Services visit (eff. 7/2017)
        "0692",     # Pre-hospice/Palliative Care Services hourly (eff. 7/2017)
        "0693",     # Pre-hospice/Palliative Care Services evaluation (eff. 7/2017)
        "0694",     # Pre-hospice/Palliative Care Services consultation and education (eff. 7/2017)
        "0695",     # Pre-hospice/Palliative Care Services Inpatient (eff. 7/2017)
        "0696",     # Pre-hospice/Palliative Care Services Physician (eff. 7/2017)
        "0699",     # Pre-hospice/Palliative Care Services Other (eff. 7/2017)
        "0700",     # Cast room general classification
        "0709",     # Cast room other
        "0710",     # Recovery room general classification
        "0719",     # Recovery room other
        "0720",     # Labor room/delivery general classification
        "0721",     # Labor room/delivery labor
        "0722",     # Labor room/delivery delivery
        "0723",     # Labor room/delivery circumcision
        "0724",     # Labor room/delivery birthing center
        "0729",     # Labor room/delivery other
        "0730",     # EKG/ECG Electrocardiogram general classification
        "0731",     # EKG/ECG Holter monitor
        "0732",     # EKG/ECG telemetry
        "0739",     # EKG/ECG other
        "0740",     # EEG Electroencephalogram general classification
        "0743",     # Reserved electroencephalogram (EEG)
        "0749",     # EEG (electroencephalogram) other
        "0750",     # Gastro-intestinal services general classification
        "0751",     # Reserved gastrointestinal (GI) services
        "0759",     # Gastro-intestinal services other
        "0760",     # Treatment or observation room general classification
        "0761",     # Treatment or observation room treatment room
        "0762",     # Treatment or observation room observation room
        "0769",     # Treatment or observation room other
        "0770",     # Preventive care services general classification
        "0771",     # Preventive care services vaccine administration
        "0779",     # Preventive care services other
        "0780",     # Telemedicine general classification
        "0789",     # Telemedicine telemedicine
        "0790",     # Extra-Corporeal Shock Wave Therapy (formerly Lithotripsy) general classification 
        "0799",     # Extra-Corporeal Shock Wave Therapy (formerly Lithotripsy) other
        "0800",     # Inpatient renal dialysis general classification
        "0801",     # Inpatient renal dialysis inpatient hemodialysis
        "0802",     # Inpatient renal dialysis inpatient peritoneal (non-CAPD)
        "0803",     # Inpatient renal dialysis inpatient Continuous Ambulatory Peritoneal Dialysis (CAPD)
        "0804",     # Inpatient renal dialysis inpatient Continuous Cycling Peritoneal Dialysis (CCPD)
        "0809",     # Inpatient renal dialysis other inpatient dialysis
        "0810",     # Organ acquisition general classification
        "0811",     # Organ acquisition living donor
        "0812",     # Organ acquisition cadaver donor
        "0813",     # Organ acquisition unknown donor
        "0814",     # Organ acquisition unsuccessful organ search-donor bank charges
        "0815",     # Allogeneic Stem Cell Acquisition/Donor Services
        "0819",     # Organ acquisition other donor
        "0820",     # Hemodialysis OP or home dialysis general classification
        "0821",     # Hemodialysis OP or home dialysis hemodialysis-composite or other rate
        "0822",     # Hemodialysis OP or home dialysis home supplies
        "0823",     # Hemodialysis OP or home dialysis home equipment
        "0824",     # Hemodialysis OP or home dialysis maintenance/100%
        "0825",     # Hemodialysis OP or home dialysis support services
        "0829",     # Hemodialysis OP or home dialysis other
        "0830",     # Peritoneal dialysis OP or home general classification
        "0831",     # Peritoneal dialysis OP or home peritoneal-composite or other rate
        "0832",     # Peritoneal dialysis OP or home home supplies
        "0833",     # Peritoneal dialysis OP or home home equipment
        "0834",     # Peritoneal dialysis OP or home maintenance/100%
        "0835",     # Peritoneal dialysis OP or home support services
        "0839",     # Peritoneal dialysis OP or home other
        "0840",     # Continuous Ambulatory Peritoneal Dialysis (CAPD) outpatient general classification
        "0841",     # Continuous Ambulatory Peritoneal Dialysis (CAPD) outpatient CAPD/composite or other rate
        "0842",     # Continuous Ambulatory Peritoneal Dialysis (CAPD) outpatient home supplies
        "0843",     # Continuous Ambulatory Peritoneal Dialysis (CAPD) outpatient home equipment 
        "0844",     # Continuous Ambulatory Peritoneal Dialysis (CAPD) outpatient maintenance/100%
        "0845",     # Continuous Ambulatory Peritoneal Dialysis (CAPD) outpatient support services
        "0849",     # Continuous Ambulatory Peritoneal Dialysis (CAPD) outpatient other
        "0850",     # Continuous Cycling Peritoneal Dialysis (CCPD) outpatient general classification
        "0851",     # Continuous Cycling Peritoneal Dialysis (CCPD) outpatient CCPD/composite or other rate
        "0852",     # Continuous Cycling Peritoneal Dialysis (CCPD) outpatient home supplies
        "0853",     # Continuous Cycling Peritoneal Dialysis (CCPD) outpatient home equipment
        "0854",     # Continuous Cycling Peritoneal Dialysis (CCPD) outpatient maintenance/100%
        "0855",     # Continuous Cycling Peritoneal Dialysis (CCPD) outpatient support services
        "0859",     # Continuous Cycling Peritoneal Dialysis (CCPD) outpatient other
        "0860",     # Magnetoencephalography (MEG) general classification
        "0861",     # Magnetoencephalography (MEG) MEG
        "0870",     # Cell/Gene Therapy General
        "0871",     # Cell/Gene Therapy Cell Collection
        "0872",     # Cell/Gene Therapy Specialized Biologic Processing and Storage Prior To Transport
        "0873",     # Cell/Gene Therapy Storage and Processing After Receipt of Cells from Manufacturer
        "0874",     # Cell/Gene Therapy Infusion of Modified Cells (eff. 4/2019)
        "0875",     # Cell/Gene Therapy Injection of Modified Cells (eff. 4/2019)
        "0880",     # Miscellaneous dialysis general classification
        "0881",     # Miscellaneous dialysis ultrafiltration
        "0882",     # Miscellaneous dialysis home dialysis aide visit
        "0889",     # Miscellaneous dialysis other
        "0890",     # Other donor bank general classification; changed to reserved for national assignment
        "0891",     # Special Processed Drugs - FDA Approved Cell Therapy (eff. 4/2019);Other donor bank bone (retired 4/2019)
        "0892",     # Special Processed Drugs FDA Approved Gene Therapy (eff. 4/2020); Other donor bank- organ (other than kidney); changed to reserved for national assignment (terminated 3/2020)
        "0893",     # Other donor bank skin; changed to reserved for national assignment
        "0899",     # Other donor bank other; changed to reserved for national assignment
        "0900",     # Behavior Health Treatment/ Services general classification (eff. 10/2004); prior to 10/2004 defined as Psychiatric/ psychological treatments general classification 
        "0901",     # Behavior Health Treatment/ Services electroshock treatment (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological treatments electroshock treatment
        "0902",     # Behavior Health Treatment/ Services milieu therapy (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological treatments milieu therapy
        "0903",     # Behavior Health Treatment/Services play therapy (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological treatments play therapy
        "0904",     # Behavior Health Treatment/Services activity therapy (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological treatments activity therapy
        "0905",     # Behavior Health Treatment/Services intensive outpatient services psychiatric (eff. 10/2004)
        "0906",     # Behavior Health Treatment/Services intensive outpatient services chemical dependency (eff. 10/2004)
        "0907",     # Behavior Health Treatment/Services community behavioral health program day treatment (eff. 10/2004)
        "0909",     # Reserved for National Use (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological treatments other
        "0910",     # Behavioral Health Treatment/Services Reserved for National Assignment (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services general classification
        "0911",     # Behavioral Health Treatment/Services rehabilitation (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services rehabilitation
        "0912",     # Behavioral Health Treatment/Services partial hospitalization less intensive (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services less intensive
        "0913",     # Behavioral Health Treatment/Services partial hospitalization intensive (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services intensive 
        "0914",     # Behavioral Health Treatment/Services individual therapy (eff. 10/2004) prior to 10/2004 defined as Psychiatric/psychological services individual therapy
        "0915",     # Behavioral Health Treatment/Services group therapy (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services group therapy
        "0916",     # Behavioral Health Treatment/Services family therapy (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services family therapy 
        "0917",     # Behavioral Health Treatment/Services biofeedback (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services biofeedback
        "0918",     # Behavioral Health Treatment/Services testing (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services testing
        "0919",     # Behavioral Health Treatment/Services other (eff. 10/2004); prior to 10/2004 defined as Psychiatric/psychological services other
        "0920",     # Other diagnostic services general classification
        "0921",     # Other diagnostic services peripheral vascular lab
        "0922",     # Other diagnostic services electromyelogram
        "0923",     # Other diagnostic services pap smear
        "0924",     # Other diagnostic services allergy test
        "0925",     # Other diagnostic services pregnancy test
        "0929",     # Other diagnostic services other
        "0931",     # Medical Rehabilitation Day Program half day
        "0932",     # Medical Rehabilitation Day Program Full Day
        "0940",     # Other therapeutic services general classification
        "0941",     # Other therapeutic services recreational therapy
        "0942",     # Other therapeutic services education/training (include diabetes diet training)
        "0943",     # Other therapeutic services cardiac rehabilitation
        "0944",     # Other therapeutic services drug rehabilitation
        "0945",     # Other therapeutic services alcohol rehabilitation
        "0946",     # Other therapeutic services routine complex medical equipment
        "0947",     # Other therapeutic services ancillary complex medical equipment
        "0948",     # Other therapeutic services pulmonary rehab
        "0949",     # Other therapeutic services other
        "0951",     # Other therapeutic services athletic training (extension of 094X)
        "0952",     # Other therapeutic services kinesiotherapy (extension of 094X)
        "0953",     # Other therapeutic services chemical dependency (drug and alcohol) (extension of 094X)
        "0958",     # Reserved other, therapeutic services, extension of 094X
        "0960",     # Professional fees general classification
        "0961",     # Professional fees psychiatric
        "0962",     # Professional fees ophthalmology
        "0963",     # Professional fees anesthesiologist (MD)
        "0964",     # Professional fees anesthetist (CRNA) 
        "0969",     # Professional fees other (NOTE: 097X is an extension of 096X)
        "0971",     # Professional fees laboratory
        "0972",     # Professional fees radiology diagnostic
        "0973",     # Professional fees radiology therapeutic
        "0974",     # Professional fees nuclear medicine
        "0975",     # Professional fees operating room
        "0976",     # Professional fees respiratory therapy
        "0977",     # Professional fees physical therapy
        "0978",     # Professional fees occupational therapy
        "0979",     # Professional fees speech pathology (NOTE: 098X is an extension of 096X and 097X)
        "0981",     # Professional fees emergency room
        "0982",     # Professional fees outpatient services
        "0983",     # Professional fees clinic
        "0984",     # Professional fees medical social services
        "0985",     # Professional fees EKG
        "0986",     # Professional fees EEG
        "0987",     # Professional fees hospital visit
        "0988",     # Professional fees consultation
        "0989",     # Professional fees private duty nurse
        "0990",     # Patient convenience items general classification
        "0991",     # Patient convenience items cafeteria/guest tray
        "0992",     # Patient convenience items private linen service
        "0993",     # Patient convenience items telephone/telegraph
        "0994",     # Patient convenience items tv/radio
        "0995",     # Patient convenience items nonpatient room rentals
        "0996",     # Patient convenience items late discharge charge
        "0997",     # Patient convenience items admission kits
        "0998",     # Patient convenience items beauty shop/barber
        "0999",     # Patient convenience items other
        "1000",     # Behavioral health Accommodations general
        "1001",     # Behavioral health Accommodations residential treatment psychiatric
        "1002",     # Behavioral health Accommodations residential treatment chemical dependency
        "1003",     # Behavioral health Accommodations Supervised living
        "1004",     # Behavioral health Accommodations Halfway House
        "1005",     # Behavioral health Accommodations Group Home
        "1006",     # Behavioral health Accommodations Outdoor/wilderness behavioral health (eff. 7/1/17) 
        "2100",     # Alternative Therapy Services General
        "2101",     # Alternative Therapy Services Acupuncture
        "2102",     # Alternative Therapy Services Acupressure
        "2103",     # Alternative Therapy Services Massage
        "2104",     # Alternative Therapy Services Reflexology
        "2105",     # Alternative Therapy Services Biofeedback
        "2106",     # Alternative Therapy Services Hypnosis
        "2109",     # Alternative Therapy Services Other
        "3101",     # Adult Day Care Medical and Social (hourly)
        "3103",     # Adult Day Care Medical and Social (daily)
        "3104",     # Adult Day Care Social (daily)
        "3105",     # Adult Foster Care (daily)
        "3109",     # Adult Day Care other NOTE: Following Revenue Codes reported for NHCMQ (RUGS) demo claims eff. 2/96
        "9000",     # RUGS no MDS assessment available
        "9001",     # Reduced physical functions RUGS PA1/ADL index of 45
        "9002",     # Reduced physical functions RUGS PA2/ADL index of 45
        "9003",     # Reduced physical functions RUGS PB1/ADL index of 68
        "9004",     # Reduced physical functions RUGS PB2/ADL index of 68
        "9005",     # Reduced physical functions RUGS PC1/ADL index of 910
        "9006",     # Reduced physical functions RUGS PC2/ADL index of 910
        "9007",     # Reduced physical functions RUGS PD1/ADL index of 1115
        "9008",     # Reduced physical functions RUGS PD2/ADL index of 1115
        "9009",     # Reduced physical functions RUGS PE1/ADL index of 1618
        "9010",     # Reduced physical functions RUGS PE2/ADL index of 1618
        "9011",     # Behavior only problems RUGS BA1/ADL index of 45
        "9012",     # Behavior only problems RUGS BA2/ADL index of 45
        "9013",     # Behavior only problems RUGS BB1/ADL index of 610
        "9014",     # Behavior only problems RUGS BB2/ADL index of 610
        "9015",     # Impaired cognition RUGS IA1/ADL index of 45
        "9016",     # Impaired cognition RUGS IA2/ADL index of 45
        "9017",     # Impaired cognition RUGS IB1/ADL index of 610
        "9018",     # Impaired cognition RUGS IB2/ADL index of 610
        "9019",     # Clinically complex RUGS CA1/ADL index of 45
        "9020",     # Clinically complex RUGS CA2/ADL index of 45d
        "9021",     # Clinically complex RUGS CB1/ADL index of 610
        "9022",     # Clinically complex RUGS CB2/ADL index of 610d
        "9023",     # Clinically complex RUGS CC1/ADL index of 1116
        "9024",     # Clinically complex RUGS CC2/ADL index of 1116d
        "9025",     # Clinically complex RUGS CD1/ADL index of 1718
        "9026",     # Clinically complex RUGS CD2/ADL index of 1718d
        "9027",     # Special care RUGS SSA/ADL index of 713
        "9028",     # Special care RUGS SSB/ADL index of 1416
        "9029",     # Special care RUGS SSC/ADL index of 17-18
        "9030",     # Extensive services RUGS SE1/1 procedure
        "9031",     # Extensive services RUGS SE2/2 procedures
        "9032",     # Extensive services RUGS SE3/3 procedures
        "9033",     # Low rehabilitation RUGS RLA/ADL index of 411
        "9034",     # Low rehabilitation RUGS RLB/ADL index of 1218
        "9035",     # Medium rehabilitation RUGS RMA/ADL index of 4-7
        "9036",     # Medium rehabilitation RUGS RMB/ADL index of 815
        "9037",     # Medium rehabilitation RUGS RMC/ADL index of 1618
        "9038",     # High rehabilitation RUGS RHA/ADL index of 47
        "9039",     # High rehabilitation RUGS RHB/ADL index of 811
        "9040",     # High rehabilitation RUGS RHC/ADL index of 1214
        "9041",     # High rehabilitation RUGS RHD/ADL index of 1518 
        "9042",     # Very high rehabilitation RUGS RVA/ADL index of 47
        "9043",     # Very high rehabilitation RUGS RVB/ADL index of 813 
        "9044",     # Very high rehabilitation RUGS RVC/ADL index of 1418 
        "9019",     # Clinically complex RUGS CA1/ADL index of 11
        "9020",     # Clinically complex RUGS CA2/ADL index of 11D
        "9021",     # Clinically complex RUGS CB1/ADL index of 12-16
        "9022",     # Clinically complex RUGS CB2/ADL index of 12-16D
        "9023",     # Clinically complex RUGS CC1/ADL index of 17-18
        "9024",     # Clinically complex RUGS CC2/ADL index of 17-18D
        "9025",     # Special care RUGS SSA/ADL index of 14
        "9026",     # Special care RUGS SSB/ADL index of 1516
        "9027",     # Special care RUGS SSC/ADL index of 1718
        "9028",     # Extensive services RUGS SE1/ADL index 718/1 procedure
        "9029",     # Extensive services RUGS SE2/ADL index 718/2 procedures
        "9030",     # Extensive services RUGS SE3/ADL index 718/3 procedures
        "9031",     # Low rehabilitation RUGS RLA/ADL index of 413
        "9032",     # Low rehabilitation RUGS RLB/ADL index of 1418
        "9033",     # Low rehabilitation RUGS RLA/ADL index of 411
        "9034",     # Medium rehabilitation RUGS RMB/ADL index of 814
        "9035",     # Medium rehabilitation RUGS RMC/ADL index of 1518
        "9036",     # High rehabilitation RUGS RHA/ADL index of 47
        "9037",     # High rehabilitation RUGS RHB/ADL index of 812
        "9038",     # High rehabilitation RUGS RHC/ADL index of 1318
        "9039",     # Very High rehabilitation RUGS RVA/ADL index of 48
        "9040",     # Very high rehabilitation-RUGS RVB/ADL index of 915
        "9041",     # Very high rehabilitation RUGS RVC/ADL index of 16
        "9042",     # Very high rehabilitation RUGS RUA/ADL index of 48
        "9043",     # Very high rehabilitation RUGS RUB/ADL index of 915
        "9044",     # Ultra high rehabilitation RUGS RUC/ADL index of 1618
    ]