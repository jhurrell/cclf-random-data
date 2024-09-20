# Revenue Center APC or HIPPS Code
# https://resdac.org/cms-data/variables/revenue-center-apc-or-hipps-code
def get_codes():
    return [
        "0000",     # Code used when Payment Method Indicator equals 'N9'
        "0001",     # Photochemotherapy
        "0002",     # Fine needle Biopsy/Aspiration
        "0003",     # Bone Marrow Biopsy/Aspiration
        "0004",     # Level I Needle Biopsy/ Aspiration Except Bone Marrow
        "0005",     # Level II Needle Biopsy /Aspiration Except Bone Marrow
        "0006",     # Level I Incision & Drainage
        "0007",     # Level II Incision & Drainage
        "0008",     # Level III Incision & Drainage
        "0009",     # Nail Procedures
        "0010",     # Level I Destruction of Lesion
        "0011",     # Level II Destruction of Lesion
        "0012",     # Level I Debridement & Destruction
        "0013",     # Level II Debridement & Destruction
        "0014",     # Level III Debridement & Destruction
        "0015",     # Level IV Debridement & Destruction
        "0016",     # Level V Debridement & Destruction
        "0017",     # Level VI Debridement & Destruction
        "0018",     # Biopsy Skin, Subcutaneous Tissue or Mucous Membrane
        "0019",     # Level I Excision/ Biopsy
        "0020",     # Level II Excision/ Biopsy
        "0021",     # Level III Excision/ Biopsy
        "0022",     # Level IV Excision/ Biopsy
        "0023",     # Exploration Penetrating Wound
        "0024",     # Level I Skin Repair
        "0025",     # Level II Skin Repair
        "0026",     # Level III Skin Repair
        "0027",     # Level IV Skin Repair
        "0028",     # Level I Incision/Excision Breast
        "0029",     # Incision/Excision Breast (obsolete 12/00); Level II Incision/Excision Breast (effective 1/01)
        "0030",     # Breast Reconstruction/Mastectomy
        "0031",     # Hyperbaric Oxygen (obsolete 1/01)
        "0032",     # Placement Transvenous Catheters/Arterial Cutdown
        "0033",     # Partial Hospitalization
        "0040",     # Arthrocentesis & Ligament/Tendon Injection
        "0041",     # Arthroscopy
        "0042",     # Arthroscopically-Aided Procedures
        "0043",     # Closed Treatment Fracture Finger/Toe/Trunk
        "0044",     # Closed Treatment Fracture/Dislocation Except Finger/Toe/Trunk
        "0045",     # Bone/Joint Manipulation Under Anesthesia
        "0046",     # Open/Percutaneous Treatment Fracture or Dislocation
        "0047",     # Arthroplasty without Prosthesis
        "0048",     # Arthroplasty with Prosthesis
        "0049",     # Level I Musculoskeletal Procedures Except Hand and Foot
        "0050",     # Level II Musculoskeletal Procedures Except Hand and Foot
        "0051",     # Level III Musculoskeletal Procedures Except Hand and Foot
        "0052",     # Level IV Musculoskeletal Procedures Except Hand and Foot
        "0053",     # Level I Hand Musculoskeletal Procedures
        "0054",     # Level II Hand Musculoskeletal Procedures
        "0055",     # Level I Foot Musculoskeletal Procedures
        "0056",     # Level II Foot Musculoskeletal Procedures
        "0057",     # Bunion Procedures
        "0058",     # Level I Strapping and Cast Application
        "0059",     # Level II Strapping and Cast Application
        "0060",     # Manipulation Therapy
        "0070",     # Thoracentesis/Lavage Procedures
        "0071",     # Level I Endoscopy Upper Airway
        "0072",     # Level II Endoscopy Upper Airway
        "0073",     # Level III Endoscopy Upper Airway
        "0074",     # Level IV Endoscopy Upper Airway
        "0075",     # Level V Endoscopy Upper Airway
        "0076",     # Endoscopy Lower Airway
        "0077",     # Level I Pulmonary Treatment
        "0078",     # Level II Pulmonary Treatment
        "0079",     # Ventilation Initiation and Management
        "0080",     # Diagnostic Cardiac Catheterization
        "0081",     # Non-Coronary Angioplasty or Atherectomy
        "0082",     # Coronary Atherectomy
        "0083",     # Coronary Angiosplasty
        "0084",     # Level I Electrophysiologic Evaluation
        "0085",     # Level II Electrophysiologic Evaluation
        "0086",     # Ablate Heart Dysrhythm Focus
        "0087",     # Cardiac Electrophysiologic Recording/Mapping
        "0088",     # Thrombectomy
        "0089",     # Level I Implantation/Removal/Revision of Pacemaker, AICD Vascular Device (obsolete 12/00); Insertion/Replacement of Permanent Pacemaker and Electrodes (eff. 1/01)
        "0090",     # Level II Implantation/Removal/Revision of Pacemaker AICD Vascular Device (obsolete 12/00); Insertion/Replacement of Permanent Pacemaker and Pulse Generator
        "0091",     # Level I Vascular Ligation
        "0092",     # Level II Vascular Ligation
        "0093",     # Vascular Repair/Fistula Construction
        "0094",     # Resuscitation and Cardioversion
        "0095",     # Cardiac Rehabilitation
        "0096",     # Non-Invasive Vascular Studies
        "0097",     # Cardiovascular Stress Test (obsolete 12/00); Cardiac Monitoring for 30 days (eff. 1/01)
        "0098",     # Injection of Sclerosing Solution
        "0099",     # Continuous Cardiac Monitoring (obsolete 12/00); Electrocardiograms (eff. 1/01)
        "0100",     # Stress test and continuous ECG
        "0101",     # Tilt Table Evaluation
        "0102",     # Electronic Analysis of Pacemakers/other Devices
        "0103",     # Miscellaneous Vascular Procedures (eff. 1/01)
        "0104",     # Transcatheter Placement of Intracoronary Stents (eff. 1/01)
        "0105",     # Revision/Removal of Pacemakers, AICD or Vascular (eff. 1/01)
        "0106",     # Insertion/Replacement/Repair of Pacemaker Electrode (eff. 1/01)
        "0107",     # Insertion of Cardioverter-Defibrillator (eff. 1/01)
        "0108",     # Insertion/Replacement/Repair of Cardioverter-Defibrillator Leads (eff. 1/01)
        "0109",     # Bone Marrow Harvesting and Bone Marrow/Stem Cell Transplant (obsolete 12/00); Removal of Implanted Devices (eff. 1/01)
        "0110",     # Transfusion
        "0111",     # Blood PRODuct Exchange
        "0112",     # Extracorporeal Photopheresis
        "0113",     # Excision Lymphatic System
        "0114",     # Thyroid/Lymphadenectomy Procedures
        "0115",     # Cannula/Access Device Procedures (eff. 1/01)
        "0116",     # Chemotherapy Administration by Other Technique Except Infusion
        "0117",     # Chemotherapy Administration by Infusion Only
        "0118",     # Chemotherapy Administration by Both Infusion and Other Technique
        "0119",     # Implantation of Devices (eff. 1/01)
        "0120",     # Infusion Therapy Except Chemotherapy
        "0121",     # Level I Tube changes and Repositioning
        "0122",     # Level II Tube changes and Repositioning
        "0123",     # Bone Marrow Harvesting and Bone Marrow/Stem Cell Transplant
        "0124",     # Revision of Implanted Infusion Pump (eff. 1/01)
        "0130",     # Level I Laparoscopy
        "0131",     # Level II Laparoscopy
        "0132",     # Level III Laparoscopy
        "0140",     # Esophageal Dilation without Endoscopy
        "0141",     # Upper GI Procedures
        "0142",     # Small Intestine Endoscopy
        "0143",     # Lower GI Endoscopy
        "0144",     # Diagnostic Anoscopy
        "0145",     # Therapeutic Anoscopy
        "0146",     # Level I Sigmoidoscopy
        "0147",     # Level II Sigmoidoscopy
        "0148",     # Level I Anal/Rectal Procedure
        "0149",     # Level II Anal/Rectal Procedure
        "0150",     # Level III Anal/Rectal Procedure
        "0151",     # Endoscopic Retrograde Cholangio-Pancreatography (ERCP)
        "0152",     # Percutaneous Biliary Endoscopic Procedures
        "0153",     # Peritoneal and Abdominal Procedures
        "0154",     # Hernia/Hydrocele Procedures
        "0157",     # Colorectal Cancer Screening: Barium Enema (Not subject to National coinsurance)
        "0158",     # Colorectal Cancer Screening: Colonoscopy Not subject to National coinsurance.  Minimum unadjusted coinsurance is 25% of the payment rate.  Payment rate is lower of the HOPD payment rate or the Ambulatory Surgical Center payment.
        "0159",     # Colorectal Cancer Screening: Flexible Sigmoidoscopy Not subject to National coinsurance.  Minimum unadjusted coinsurance is 25% of the payment rate.  Payment rate is lower of the HOPD payment rate or the Ambulatory Surgical Center payment.
        "0160",     # Level I Cystourethroscopy and other Genitourinary Procedures
        "0161",     # Level II Cystourethroscopy and other Genitourinary Procedures
        "0162",     # Level III Cystourethroscopy and other Genitourinary Procedures
        "0163",     # Level IV Cystourethroscopy and other Genitourinary Procedures
        "0164",     # Level I  Urinary and Anal Procedures
        "0165",     # Level II  Urinary and Anal Procedures
        "0166",     # Level I Urethral Procedures
        "0167",     # Level II Urethral Procedures
        "0168",     # Level III Urethral Procedures
        "0169",     # Lithotripsy
        "0170",     # Dialysis for Other Than ESRD Patients
        "0180",     # Circumcision
        "0181",     # Penile Procedures
        "0182",     # Insertion of Penile Prosthesis
        "0183",     # Testes/Epididymis Procedures
        "0184",     # Prostate Biopsy
        "0190",     # Surgical Hysteroscopy
        "0191",     # Level I Female RePRODuctive Procedures
        "0192",     # Level II Female RePRODuctive Procedures
        "0193",     # Level III Female RePRODuctive Procedures
        "0194",     # Level IV Female RePRODuctive Procedures
        "0195",     # Level V Female RePRODuctive Procedures
        "0196",     # Dilatation & Curettage
        "0197",     # Infertility Procedures
        "0198",     # Pregnancy and Neonatal Care Procedures
        "0199",     # Vaginal Delivery
        "0200",     # Therapeutic Abortion
        "0201",     # Spontaneous Abortion
        "0210",     # Spinal Tap
        "0211",     # Level I Nervous System Injections
        "0212",     # Level II Nervous System Injections
        "0213",     # Extended EEG Studies and Sleep Studies
        "0214",     # Electroencephalogram
        "0215",     # Level I Nerve and Muscle Tests
        "0216",     # Level II Nerve and Muscle Tests
        "0217",     # Level III Nerve and Muscle Tests
        "0220",     # Level I Nerve Procedures
        "0221",     # Level II Nerve Procedures
        "0222",     # Implantation of Neurological Device
        "0223",     # Level I Revision/Removal Neurological Device (obsolete 12/00); Implantation of Pain Management Device (eff. 1/01)
        "0224",     # Level II Revision/Removal Neurological Device (obsolete 12/00); Implantation of Reservoir/Pump/Shunt (eff. 1/01)
        "0225",     # Implantation of Neurostimulator Electrodes
        "0226",     # Implantation of Drug Infusion Reservior (eff. 1/01)
        "0227",     # Implantation of Drug Infusion Device (eff. 1/01)
        "0228",     # Creation of Lumbar Subarachnoid Shunt (eff. 1/01)
        "0229",     # Transcatherter Placement of Intravascular Shunts (eff. 1/01)
        "0230",     # Level I Eye Tests
        "0231",     # Level II Eye Tests
        "0232",     # Level I Anterior Segment Eye
        "0233",     # Level II Anterior Segment Eye
        "0234",     # Level III Anterior Segment Eye Procedures
        "0235",     # Level I Posterior Segment Eye Procedures
        "0236",     # Level II Posterior Segment Eye Procedures
        "0237",     # Level III Posterior Segment Eye Procedures
        "0238",     # Level I Repair and Plastic Eye Procedures
        "0239",     # Level II Repair and Plastic Eye Procedures
        "0240",     # Level III Repair and Plastic Eye Procedures
        "0241",     # Level IV Repair and Plastic Eye Procedures
        "0242",     # Level V Repair and Plastic Eye Procedures
        "0243",     # Strabismus/Muscle Procedures
        "0244",     # Corneal Transplant
        "0245",     # Cataract Procedures without IOL Insert
        "0246",     # Cataract Procedures with IOL Insert
        "0247",     # Laser Eye Procedures Except Retinal
        "0248",     # Laser Retinal Procedures
        "0250",     # Nasal Cauterization/Packing
        "0251",     # Level I ENT Procedures
        "0252",     # Level II ENT Procedures
        "0253",     # Level III ENT Procedures
        "0254",     # Level IV ENT Procedures
        "0256",     # Level V ENT Procedures
        "0257",     # Implantation of Cochlear Device (obsolete 1/01)
        "0258",     # Tonsil and Adenoid Procedures
        "0260",     # Level I Plain Film Except Teeth
        "0261",     # Level II Plain Film Except Teeth Including Bone Density Measurement
        "0262",     # Plain Film of Teeth
        "0263",     # Level I Miscellaneous Radiology Procedures
        "0264",     # Level II Miscellaneous Radiology Procedures
        "0265",     # Level I Diagnostic Ultrasound Except Vascular
        "0266",     # Level II Diagnostic Ultrasound Except Vascular
        "0267",     # Vascular Ultrasound
        "0268",     # Guidance Under Ultrasound
        "0269",     # Echocardiogram Except Transesophageal
        "0270",     # Transesophageal Echocardiogram
        "0271",     # Mammography
        "0272",     # Level I Fluoroscopy
        "0273",     # Level II Fluoroscopy
        "0274",     # Myelography
        "0275",     # Arthrography
        "0276",     # Level I Digestive Radiology
        "0277",     # Level II Digestive Radiology
        "0278",     # Diagnostic Urography
        "0279",     # Level I Diagnostic Angiography and Venography Except Extremity
        "0280",     # Level II Diagnostic Angiography and Venography Except Extremity
        "0281",     # Venography of Extremity
        "0282",     # Level I Computerized Axial Tomography
        "0283",     # Level II Computerized Axial Tomography
        "0284",     # Magnetic Resonance Imaging
        "0285",     # Positron Emission Tomography (PET)
        "0286",     # Myocardial Scans
        "0290",     # Standard Non-Imaging Nuclear Medicine
        "0291",     # Level I Diagnostic Nuclear Medicine Excluding Myocardial Scans
        "0292",     # Level II Diagnostic Nuclear Medicine Excluding Myocardial Scans
        "0294",     # Level I Therapeutic Nuclear Medicine
        "0295",     # Level II Therapeutic Nuclear Medicine
        "0296",     # Level I Therapeutic Radiologic Procedures
        "0297",     # Level II Therapeutic Radiologic Procedures
        "0300",     # Level I Radiation Therapy
        "0301",     # Level II Radiation Therapy
        "0302",     # Level III Radiation Therapy
        "0303",     # Treatment Device Construction
        "0304",     # Level  I Therapeutic Radiation Treatment Preparation
        "0305",     # Level II Therapeutic Radiation Treatment Preparation
        "0310",     # Level III Therapeutic Radiation Treatment Preparation
        "0311",     # Radiation Physics Services
        "0312",     # Radioelement Applications
        "0313",     # Brachytherapy
        "0314",     # Hyperthermic Therapies
        "0320",     # Electroconvulsive Therapy
        "0321",     # Biofeedback and Other Training
        "0322",     # Brief Individual Psychotherapy
        "0323",     # Extended Individual Psychotherapy
        "0324",     # Family Psychotherapy
        "0325",     # Group Psychotherapy
        "0330",     # Dental Procedures
        "0340",     # Minor Ancillary Procedures
        "0341",     # Immunology Tests
        "0342",     # Level I Pathology
        "0343",     # Level II Pathology
        "0344",     # Level III Pathology
        "0345",     # Transfusion Laboratory Procedures Level I (eff. 1/01)
        "0346",     # Transfusion Laboratory Procedures Level II (eff. 1/01)
        "0347",     # Transfusion Laboratory Procedures Level III (eff. 1/01)
        "0348",     # Fertility Laboratory Procedures (eff. 1/01)
        "0349",     # Miscellaneous Laboratory Procedures (eff. 1/01)
        "0354",     # Administration of Influenza Vaccine (Not subject to national coinsurance)
        "0355",     # Level I Immunizations
        "0356",     # Level II Immunizations
        "0357",     # Level III Immunizations (obsolete 1/01)
        "0358",     # Level IV Immunizations (obsolete 1/01)
        "0359",     # Injections
        "0360",     # Level I Alimentary Tests
        "0361",     # Level II Alimentary Tests
        "0362",     # Fitting of Vision Aids
        "0363",     # Otorhinolaryngologic Function Tests
        "0364",     # Level I Audiometry
        "0365",     # Level II Audiometry
        "0366",     # Electrocardiogram (ECG) (obsolete 1/01)
        "0367",     # Level I Pulmonary Test
        "0368",     # Level II Pulmonary Test
        "0369",     # Level III Pulmonary Test
        "0370",     # Allergy Tests
        "0371",     # Allergy Injections
        "0372",     # Therapeutic Phlebotomy
        "0373",     # Neuropsychological Testing
        "0374",     # Monitoring Psychiatric Drugs
        "0600",     # Low Level Clinic Visits
        "0601",     # Mid Level Clinic Visits
        "0602",     # High Level Clinic Visits
        "0603",     # Interdisciplinary Team Conference (obsolete 1/01)
        "0610",     # Low Level Emergency Visits
        "0611",     # Mid Level Emergency Visits
        "0612",     # High Level Emergency Visits
        "0620",     # Critical Care
        "0701",     # Strontium (eligible for pass-through payments) (obsolete 12/00); SR 89 chloride, per mCi (eff. 1/01)
        "0702",     # Samariam (eligible for pass-through payments) (obsolete 12/00); SM 153 lexidronam, 50 mCi (eff. 1/01)
        "0704",     # IN 111 Satumomab Pendetide (eligible for pass-through payments)
        "0705",     # Tc99 Tetrofosmin (eligible for pass-through payments)
        "0725",     # Leucovorin Calcium (eligible for pass-through payments)
        "0726",     # Dexrazoxane Hydrochloride (eligible for pass-through payments)
        "0727",     # Injection, Etidronate Disodium (eligible for pass-through payments)
        "0728",     # Filgrastim (G-CSF) (eligible for pass-through payments)
        "0730",     # Pamidronate Disodium (eligible for pass-through payments)
        "0731",     # Sargramostim (GM-CSF) (eligible for pass-through payments)
        "0732",     # Mesna (eligible for pass-through payments)
        "0733",     # Non-ESRD Epoetin Alpha (eligible for pass-through payments)
        "0750",     # Dolasetron Mesylate 10 mg (eligible for pass-through payments)
        "0754",     # Metoclopramide HCL (eligible for pass-through payments)
        "0755",     # Thiethylperazine Maleate (eligible for pass-through payments)
        "0761",     # Oral Substitute for IV Antiemtic (eligible for pass-through payments)
        "0762",     # Dronabinol (elibible for pass-through payments)
        "0763",     # Dolasetron Mesylate 100 mg Oral (eligible for pass-through payments)
        "0764",     # Granisetron HCL, 100 mcg (eligible for pass-through payments)
        "0765",     # Granisetron HCL, 1mg Oral (eligible for pass-through payments)
        "0768",     # Ondansetron Hydrochloride per 1 mg Injection (eligible for pass-through payments)
        "0769",     # Ondansetron Hydrochloride 8 mg oral (eligible for pass-through payments)
        "0800",     # Leuprolide Acetate per 3.75 mg (eligible for pass-through payments)
        "0801",     # Cyclophosphamide (eligible for pass-through payments)
        "0802",     # Etoposide (eligible for pass-through payments)
        "0803",     # Melphalan (eligible for pass-through payments)
        "0807",     # Aldesleukin single use vial (eligible for pass-through payments)
        "0809",     # BCG (Intravesical) one vial (eligible for pass-through payments)
        "0810",     # Goserelin Acetate Implant, per 3.6 mg (eligible for pass-through payments)
        "0811",     # Carboplatin 50 mg (eligible for pass-through payments)
        "0812",     # Carmustine 100 mg (eligible for pass-through payments)
        "0813",     # Cisplatin 10 mg (eligible for pass-through payments)
        "0814",     # Asparaginase, 10,000 units (eligible for pass-through payments)
        "0815",     # Cyclophosphamide 100 mg (eligible for pass-through payments)
        "0816",     # Cyclophosphamide, Lyophilized 100 mg (eligible for pass-through payments)
        "0817",     # Cytrabine 100 mg (eligible for pass-through payments)
        "0818",     # Dactinomycin 0.5 mg (eligible for pass-through payments)
        "0819",     # Dacarbazine 100 mg (eligible for pass-through payments)
        "0820",     # Daunorubicin HCI 10 mg (eligible for pass-through payments)
        "0821",     # Daunorubicin Citrate, Liposomal Formulation, 10 mg (eligible for pass-through payments)
        "0822",     # Diethylstibestrol Diphosphate 250 mg (eligible for pass-through payments)
        "0823",     # Docetaxel 20 mg (eligible for pass-through payments)
        "0824",     # Etoposide 10 mg (eligible for pass-through payments)
        "0826",     # Methotrexate Oral 2.5 mg (eligible for pass-through payments)
        "0827",     # Floxuridine injection 500mg
        "0828",     # Gemcitabine HCL 200 mg (eligibile for pass-through payments)
        "0830",     # Irinotecan 20 mg (eligible for pass-through payments)
        "0831",     # Ifosfamide injection 1 gm (eligible for pass-through payments)
        "0832",     # Idarubicin HCL injection 5 mg (eligible for pass-through payments)
        "0833",     # Interferon Alfacon-1, 1 mcg (eligible for pass-through payments)
        "0834",     # Interferon,  Alfa-2A, Recombinant 3 million units (eligible for pass-through payments)
        "0836",     # Interferon,  Alfa-2B, Recombinant, 1 million units (eligible for pass-through payments)
        "0838",     # Interferon, Gamma 1-B injection, 3 million units (eligible for pass-through payments)
        "0839",     # Mechlorethamine HCL injection 10 mg (eligible for pass-through payments)
        "0840",     # Melphalan HCL 50 mg (eligible for pass-through payments)
        "0841",     # Methotrexate sodium injection 5 mg (eligible for pass-through payments)
        "0842",     # Fludarabine Phosphate injection 50 mg (eligible for pass-through payments)
        "0843",     # Pegaspargase, single dose vial (eligible for pass-through payments)
        "0844",     # Pentostatin injection, 10 mg (eligible for pass-through payments)
        "0847",     # Doxorubicin HCL 10 mg (eligible for pass-through payments)
        "0849",     # Rituximab, 100 mg (eligible for pass-through payments)
        "0850",     # Streptozocin injection, 1 gm (eligible for pass-through payments)
        "0851",     # Thiotepa injection, 15 mg (eligible for pass-through payments)
        "0852",     # Topotecan 4 mg (eligible for pass-through payments)
        "0853",     # Vinblastine Sulfate injection, 1 mg (eligible for pass-through payments)
        "0854",     # Vincristine Sulfate 1 mg (eligible for pass-through payments)
        "0855",     # Vinorelbine Tartrate per 10 mg (eligible for pass-through payments)
        "0856",     # Porfimer Sodium 75 mg (eligible for pass-through payments)
        "0857",     # Bleomycin Sulfate injection 15 units (eligible for pass-through payments)
        "0858",     # Cladribine, 1mg (eligible for pass-through payments)
        "0859",     # Fluorouracil injection 500 mg
        "0860",     # Plicamycin (mithramycin) injection, 2.5 mg
        "0861",     # Leuprolide Acetate 1 mg (eligible for pass-through payments)
        "0862",     # Mitomycin, 5mg (eligible for pass-through payments)
        "0863",     # Paclitaxel, 30mg (eligible for pass-through payments)
        "0864",     # Mitoxantrone HCl,  per 5mg (eligible for pass-through payments)
        "0865",     # Interferon alfa-N3, 250,000 IU (eligible for pass-through payments)
        "0884",     # Rho (D) Immune Globulin, Human one dose pack (eligible for pass-through payments)
        "0886",     # Azathioprine,  50 mg oral (Not subject to national coinsurance)
        "0887",     # Azathioprine, Parenteral 100 mg, 20 ml each injection (Not subject to national coinsurance)
        "0888",     # Cyclosporine, Oral 100 mg (Not subject to national coinsurance)
        "0889",     # Cyclosporine, Parenteral (Not subject to national coinsurance)
        "0890",     # Lymphocyte Immune Globulin 250 mg (Not subject to national coinsurance)
        "0891",     # Tacrolimus per 1 mg oral (Not subject to national coinsurance)
        "0892",     # Daclizumab, Parenteral, 25 mg (obsolete 1/01) (eligible for pass-through payments)
        "0900",     # Injection, Alglucerase per 10 units (eligible for pass-through payments)
        "0901",     # Alpha I, Proteinase Inhibitor, Human per 10mg (eligible for pass-through payments)
        "0902",     # Botulinum Toxin, Type A per unit (eligible for pass-through payments)
        "0903",     # CMV Immune Globulin (obsolete 12/00); Cytomegalovirus imm IV, vial (eligible for pass-through payments) (eff. 1/01)
        "0905",     # Immune Globulin per 500 mg (eligible for pass-through payments)
        "0906",     # RSV-ivig 50 mg (eligible for pass-through payments)
        "0907",     # Ganciclovir Sodium 500 mg injection (Not subject to national coinsurance)
        "0908",     # Tetanus Immune Globulin, injection up to 250 units (Not subject to national coinsurance)
        "0909",     # Interferon Beta - 1a   33 mcg (eligible for pass-through payments)
        "0910",     # Interferon Beta - 1b   0.25 mg (eligible for pass-through payments)
        "0911",     # Streptokinase per 250,000 iu (Not subject to national coinsurance)
        "0913",     # Ganciclovir long act implant 4.5  mg (eligible for pass-through payments)
        "0914",     # Reteplase, 37.6 mg (Not subject to national coinsurance)
        "0915",     # Alteplase injection,recombinant, 10mg (Not subject to national coinsurance)
        "0916",     # Imiglucerase per unit (eligible for pass-through payments)
        "0917",     # Dipyridamole, 10mg / Adenosine 6MG (Not subject to national coinsurance) (obsolete 1/01) Pharmalogic stresses (eff. 1/01)
        "0918",     # Brachytherapy Seeds, Any type, Each (eligible for pass-through payments) (obsolete 4/01)
        "0925",     # Factor VIII (Antihemophilic Factor, Human) per iu (eligible for pass-through payments)
        "0926",     # Factor VIII (Antihemophilic Factor, Porcine) per iu (eligible for pass-through payments)
        "0927",     # Factor VIII (Antihemophilic Factor, Recombinant) per iu (eligible for pass-through payments)
        "0928",     # Factor IX,  Complex (eligible for pass-through payments)
        "0929",     # Other Hemophilia Clotting Factors per iu (eligible for pass-through payments) (obsolete 1/01) Anti-inhibitor per iu (eff. 1/01)
        "0930",     # Antithrombin III (Human) per iu (eligible for pass-through payments)
        "0931",     # Factor IX (Antihemophilic Factor, Purified, Non-Recombinant) (eligible for pass-through payments)
        "0932",     # Factor IX (Antihemophilic Factor, Recombinant) (eligible for pass-through payments)
        "0949",     # Plasma, Pooled Multiple Donor, Solvent/Detergent Treated, Frozen (not subject to national coinsurance)
        "0950",     # Blood (Whole) For Transfusion (not subject to national coinsurance)
        "0952",     # Cryoprecipitate (not subject to national coinsurance)
        "0953",     # Fibrinogen Unit (not subject to national coinsurance)
        "0954",     # Leukocyte Poor Blood (not subject to national coinsurance)
        "0955",     # Plasma, Fresh Frozen (not subject to national coinsurance)
        "0956",     # Plasma Protein Fraction (not subject to national coinsurance)
        "0957",     # Platelet Concentrate (not subject to national coinsurance)
        "0958",     # Platelet Rich Plasma (not subject to national coinsurance)
        "0959",     # Red Blood Cells (not subject to national coinsurance)
        "0960",     # Washed Red Blood Cells (not subject to national coinsurance)
        "0961",     # Infusion, Albumin (Human) 5%, 500 ml (not subject to national coinsurance)
        "0962",     # Infusion, Albumin (Human) 25%, 50 ml (not subject to national coinsurance)
        "0970",     # New Technology - Level I  ($0 - $50) (not subject to national coinsurance)
        "0971",     # New Technology - Level II ($50 - $100) (not subject to national coinsurance)
        "0972",     # New Technology - Level III ($100 - $200) (not subject to national coinsurance)
        "0973",     # New Technology - Level IV   ($200 - $300) (not subject to national coinsurance)
        "0974",     # New Technology - Level V ($300 - $500) (not subject to national coinsurance)
        "0975",     # New Technology - Level VI   ($500 - $750) (not subject to national coinsurance)
        "0976",     # New Technology - Level VII   ($750 - $1000) (not subject to national coinsurance)
        "0977",     # New Technology - Level VIII  ($1000 - $1250) (not subject to national coinsurance)
        "0978",     # New Technology - Level IX ($1250 - $1500) (not subject to national coinsurance)
        "0979",     # New Technology - Level X  ($1500 - $1750) (not subject to national coinsurance)
        "0980",     # New Technology - Level XI ($1750 - $2000) (not subject to national coinsurance)
        "0981",     # New Technology - Level XII   ($2000 - $2500) (not subject to national coinsurance)
        "0982",     # New Technology - Level XIII   ($2500 - $3500) (not subject to national coinsurance)
        "0983",     # New Technology - Level XIV  ($3500 - $5000) (not subject to national coinsurance)
        "0984",     # New Technology - Level XV   ($5000 - $6000) (not subject to national coinsurance)
        "0987",     # New Device Technology - Level I ($0 - $250) (eff. 1/01)
        "0988",     # New Device Technology - Level II ($250 - $500) (eff. 1/01)
        "0989",     # New Device Technology - Level III ($500 - $750) (eff. 1/01)
        "0990",     # New Device Technology - Level IV ($750 - $1000) (eff. 1/01)
        "0991",     # New Device Technology - Level V ($1000 - $1500) (eff. 1/01)
        "0992",     # New Device Technology - Level VI ($1500 - $2000) (eff. 1/01)
        "0993",     # New Device Technology - Level VII ($2000 - $3000) (eff. 1/01)
        "0994",     # New Device Technology - Level VIII ($3000 - $4000) (eff. 1/01)
        "0995",     # New Device Technology - Level IX ($4000 - $5000) (eff. 1/01)
        "0996",     # New Device Technology - Level X ($5000 - $7000) (eff. 1/01)
        "0997",     # New Device Technology - Level XI ($7000 - $9000) (eff. 1/01)
        "1000",     # Perclose Closer Prostar Arterial Vascular Closure (eff. 1/01)
        "1001",     # AcuNav-diagnostic ultrasound ca (eff. 1/01) 
        "1002",     # Cochlear Implant System (eff. 1/01)
        "1003",     # Cath, ablation, livewire TC (eff. 1/01) 
        "1004",     # Fast-Cath, Swartz, SAFL, CSTA (eff. 1/01)
        "1006",     # ARRAY post chamb IOL (eff. 1/01) 1007",     # Ams 700 penile prosthesis (eff. 1/01)
        "1008",     # Urolume-implant urethral stent (eff. 1/01)
        "1009",     # Plasma, cryoprecipitate-reduced, unit (eff. 1/01)
        "1010",     # Blood, L/R CMV-neg (eff. 1/01)
        "1011",     # Platelets, L/R, CMV-neg (eff. 1/01)
        "1012",     # Platelet concentrate, L/R, irradiated, unit (eff. 1/01)
        "1013",     # Platelet concentrate, L/R, unit (eff. 1/01)
        "1014",     # Platelets, aph/pher, L/R, unit (eff. 1/01)
        "1016",     # Blood, L/R, froz/deglycerol/washed (eff. 1/01)
        "1017",     # Platelets, aph/pher, L/R CMV-neg, unit (eff. 1/01)
        "1018",     # Blood, L/R, irradiated (eff. 1/01)
        "1019",     # Platelets, aph/pher, L/R, irradiated, unit (eff. 1/01)
        "1024",     # Quinupristin 150 mg/dalfopriston 350 mg (eff. 1/01)
        "1025",     # Marinr CS catheter (eff. 1/01)
        "1026",     # RF Perfrmr cath 5F RF Marinr (eff. 1/01)
        "1027",     # Magic x/short, radius 14m (eff. 1/01)
        "1028",     # Prcis Twst trnsvg anch sys (eff. 1/01)
        "1029",     # CRE guided balloon dil cath (eff. 1/01)
        "1030",     # Cthtr:Mrshal, Blu Max Utr Dmnd (eff. 1/01)
        "1033",     # Sonicath mdl 37-410 (eff. 1/01)
        "1034",     # SURPASS, Long30 SURPASS-cath (eff. 1/01)
        "1035",     # Cath, Ultra ICE (eff. 1/01)
        "1036",     # R port/reservior impl dev (eff. 1/01)
        "1037",     # Vaxcelchronic dialysis cath (eff. 1/01)
        "1038",     # UltraCross Imaging Cath (eff. 1/01)
        "1039",     # Wallstent/RP:Trach (eff. 1/01)
        "1040",     # Wallstent/RP TIPS -- 20/40/60 (eff. 1/01)
        "1042",     # Wallstent, UltraFlex: Bil (eff. 1/01)
        "1045",     # I-131 MIBG (ioben-sulfate) 0.5 mCi (eff. 1/01)
        "1047",     # Navi-Star, Noga-Star cath (eff. 1/01)
        "1048",     # NeuroCyberneticPros: gen (eff. 1/01)
        "1051",     # Oasis Thrombectomy Cath (eff. 1/01)
        "1053",     # EnSite 3000 catheter (eff. 1/01)
        "1054",     # Hydrolyser Thromb Cath 6/7F (eff. 1/01)
        "1055",     # Transesoph 210, 210-S Cath (eff. 1/01)
        "1056",     # Thermachoice II Cath (eff. 1/01)
        "1057",     # Micromark Tissue Marker (eff. 1/01)
        "1059",     # Carticel, auto cult-chndr cyte (eff. 1/01)
        "1060",     # ACS multi-link tristor stent (eff. 1/01)
        "1061",     # ACS Viking Guiding cath (eff. 1/01)
        "1063",     # EndoTak Endurance EZ,RX leads (eff. 1/01)
        "1067",     # Megalink biliary stent (eff. 1/01)
        "1068",     # Pulsar DDD pmkr (eff. 1/01)
        "1069",     # Discovery DR, pmaker
        "1071",     # Pulsar Max, Pulsar SR pmkr (eff. 1/01)
        "1072",     # Guidant: blln dil cath (eff. 1/01)
        "1073",     # Gynecare Morcellator (eff. 1/01)
        "1074",     # RX/OTW Viatrac-peri dil cath (eff. 1/01)
        "1075",     # Guidant: lead (eff. 1/01)
        "1076",     # Ventak minisc defib (eff. 1/01)
        "1077",     # Ventak VR Prizm VR, sc defib (eff. 1/01)
        "1078",     # Ventak: Prizm, AVIIIDR defib
        "1079",     # CO 57/58 0.5 mCi (eff. 1/01)
        "1084",     # Denileukin diftitox, 300 mcg (eff. 1/01)
        "1086",     # Temozolomide, 5 mg (eff. 1/01)
        "1087",     # I-123 per uCi capsule (eff. 1/01)
        "1089",     # CO 57, 0.5 mCi (eff. 1/01)
        "1090",     # IN 111 Chloride, per mCi (eff. 1/01)
        "1091",     # IN 111 Oxyquinoline, per 5 mCi (eff. 1/01)
        "1092",     # IN 111 Pentetate, per 1.5 mCi (eff. 1/01)
        "1094",     # TC 99M Albumin aggr, per vial
        "1095",     # TC 99M Depreotide, per vial (eff. 1/01)
        "1096",     # TC 99M Exametazime, per dose (eff. 1/01)
        "1097",     # TC 99M Mebrofenin, per vial (eff. 1/01)
        "1098",     # TC 99M Pentetate, per vial (eff. 1/01)
        "1099",     # TC 99M Pyrophosphate, per vial (eff. 1/01)
        "1100",     # Medtronic AVE GT1 guidewire (eff. 1/01)
        "1101",     # Medtronic AVE, AVE Z2 cath (eff. 1/01)
        "1102",     # Synergy Neurostim Genrtr (eff. 1/01)
        "1103",     # Micro Jewell Defibrillator (eff. 1/01)
        "1104",     # RF ConductorAblative Cath (eff. 1/01)
        "1105",     # Sigman 300VDD pacmkr (eff. 1/01)
        "1106",     # SynergyEZ Pt Progmr (eff. 1/01)
        "1107",     # Torqr, Solist cath (eff. 1/01)
        "1108",     # Reveal Cardiac Recorder (eff. 1/01)
        "1109",     # Implantable anchor: Ethicon (eff. 1/01)
        "1110",     # Stable Mapper, cath electrd (eff. 1/01)
        "1111",     # AneuRxAort-Uni-llicstnt & cath (eff. 1/01)
        "1112",     # AneuRx Stent graft/del cath (eff. 1/01)
        "1113",     # Tlnt Endo Sprng Stnt Grft Sys (eff. 1/01)
        "1114",     # TalntSprgStnt + Graf endo pros (eff. 1/01)
        "1115",     # 5038S, 5038, 5038L pace lead (eff. 1/01)
        "1116",     # CapSureSP pacing lead (eff. 1/01)
        "1117",     # Ancure Endograft Del Sys (eff. 1/01)
        "1118",     # Sigma300DR LegIIDR, pacemkr (eff. 1/01)
        "1119",     # Sprint6932, 6943 defib lead (eff. 1/01)
        "1120",     # Sprint6942, 6945 defi lead (eff. 1/01)
        "1121",     # Gem defibrillator (eff. 1/01)
        "1122",     # TC 99M arcitumomab per dose (eff. 1/01)
        "1123",     # Gem II VR defibrillator (eff. 1/01)
        "1124",     # InterStim Test Stim Kit (eff. 1/01)
        "1125",     # Kappa 400SR, Ttopaz II SR pmkr (eff. 1/01)
        "1126",     # Kappa 700 DR pacemkr (eff. 1/01)
        "1127",     # Kappa 700SR, pmkr sgl chamber (eff. 1/01)
        "1128",     # Kappa 700D, Ruby IID pmkr (eff. 1/01)
        "1129",     # Kappa 700VDD, pacmkr (eff. 1/01)
        "1130",     # Sigma 200D, LGCY IID sc pmkr (eff. 1/01)
        "1131",     # Sigma 200DR pmker (eff. 1/01)
        "1132",     # Sigma 200SR Leg II:sc pac (eff. 1/01)
        "1133",     # Sigma SR, Vita SR, pmaker (eff. 1/01)
        "1134",     # Sigma 300D pmker (eff. 1/01)
        "1135",     # Entity DR 5326L/R, DC, pmkr (eff. 1/01)
        "1136",     # Affinity DR 5330L/R, DC, pmkr (eff. 1/01)
        "1137",     # CardioSEAL implant syst (eff. 1/01)
        "1143",     # AddVent mod 2060BL, VDD (eff. 1/01)
        "1144",     # Afnty SP 5130, Integrity SR, pmkr (eff. 1/01)
        "1145",     # Angio-Seal 6fr, 8fr (eff. 1/01)
        "1147",     # AV Plus DX 1368: lead (eff. 1/01)
        "1148",     # Contour MD sc defib (eff. 1/01)
        "1149",     # Entity DC 5226R-pmker (eff. 1/01)
        "1151",     # Passiveplus DXlead, 10mdls (eff. 1/01)
        "1152",     # LifeSite Access System (eff. 1/01)
        "1153",     # Regency SC+ 2402L pmkr (eff. 1/01)
        "1154",     # SPL:SPOI, 0204- defib lead (eff. 1/01)
        "1155",     # Repliform 8 sq cm (eff. 1/01)
        "1156",     # Tr 1102TrSR+ 2260L, 2264L, 5131 (eff. 1/01)
        "1157",     # Trilogy DCT 23/8L pmkr (eff. 1/01)
        "1158",     # TVL lead SV01, SV02, SV04 (eff. 1/01)
        "1159",     # TVL RV02, RV06, RV07: lead (eff. 1/01)
        "1160",     # TVL-ADX 1559: lead (eff. 1/01)
        "1161",     # Tendril DX, 1338 pacing lead (eff. 1/01)
        "1162",     # TempoDr, TrilogyDR+ DC pmkr (eff. 1/01)
        "1163",     # Tendril SDX, 1488T pacing lead (eff. 1/01)
        "1164",     # Iodine-125 brachytx seed (eff. 1/01)
        "1166",     # Cytarabine liposomal, 10 mg (eff. 1/01)
        "1167",     # Epirubicin hcl, 2 mg (eff. 1/01)
        "1171",     # Autosuture site marker stple (eff. 1/01)
        "1172",     # Spacemaker dissect ballon (eff. 1/01)
        "1173",     # Cor stntS540, S670, o-wire stn (eff. 1/01)
        "1174",     # Bard brachytx needle (eff. 1/01)
        "1178",     # Busulfan IV, 6 mg (eff. 1/01)
        "1180",     # Vigor SR, SC, pmkr (eff. 1/01)
        "1181",     # Meridian SSI, SC pmkr (eff. 1/01)
        "1182",     # Pulsar SSI, SC, pmkr (eff. 1/01)
        "1183",     # Jade IIS, Sigma 300S, SC, pmkr (eff. 1/01)
        "1184",     # Sigma 200S, SC, pmkr (eff. 1/01)
        "1188",     # I 131, per mCi (eff. 1/01)
        "1200",     # TC 99M Sodium Clucoheptonate, per vial (eff. 1/01)
        "1201",     # TC 99M succimer, per vial (eff. 1/01)
        "1202",     # TC 99M Sulfur Colloid, per dose (eff. 1/01)
        "1203",     # Verteporfin for Injection (eff. 1/01)
        "1205",     # TC 99M Disofenin, per vial (eff. 1/01)
        "1207",     # Octreotide acetate depot 1 mg (eff. 1/01)
        "1302",     # SQ01:lead (eff. 1/01)
        "1303",     # CapSure Fix 6940/4068-110, lead (eff. 1/01)
        "1304",     # Sonicath mdl 37-416,-418 (eff. 1/01)
        "1305",     # Apligraf (eff. 1/01)
        "1306",     # NeuroCyberneticsPros: lead (eff. 1/01)
        "1311",     # Trilogy DR + DAO pmkr (eff. 1/01)
        "1312",     # Magic WALLSTENT stent-mini (eff. 1/01)
        "1313",     # Magic medium, radius 31mm (eff. 1/01)
        "1314",     # Magic WALLSTENT stent-Long (eff. 1/01)
        "1315",     # Vigor DR, Meridian DR pmkr (eff. 1/01)
        "1316",     # Meridian DDD pmkr (eff. 1/01)
        "1317",     # Discovery SR, pmkr (eff. 1/01)
        "1318",     # Meridian SR pmkr (eff. 1/01)
        "1319",     # Wallstent/RP Enteral--60mm (eff. 1/01)
        "1320",     # Wallstent/RP lliac Del Sys (eff. 1/01)
        "1325",     # Pallidium - 103 seed (eff. 1/01)
        "1326",     # Angio-jet rheolytic thromb cath (eff. 1/01)
        "1328",     # ANS Renew NS trnsmtr (eff. 1/01)
        "1333",     # PALMZA Corinthian bill stent (eff. 1/01)
        "1334",     # Crown, Mini-crown,CrossLC (eff. 1/01)
        "1335",     # Mesh, Prolene (eff. 1/01)
        "1336",     # Constant Flow Imp Pump (eff. 1/01)
        "1337",     # IsoMed 8472-20/35/60 (eff. 1/01)
        "1348",     # I 131 per mCi solution (eff. 1/01)
        "1350",     # Prosta/OncoSeed, RAPID strand, I-125 (eff. 1/01)
        "1351",     # CapSure (Fix) pacing lead (eff. 1/01)
        "1352",     # Gem II defib (eff. 1/01)
        "1353",     # Itrel Interstm neurostim + ext (eff. 1/01)
        "1354",     # Kappa 400DR, Diamond II 820 DR (eff. 1/01)
        "1355",     # Kappa 600 DR, Vita DR (eff. 1/01)
        "1356",     # Profile MD V-186HV3 sc defib (eff. 1/01)
        "1357",     # Angstrom MD V-190HV3 sc defib (eff. 1/01)
        "1358",     # Affinity DC 5230R-Pacemaker (eff. 1/01)
        "1359",     # Pulsar, Pulsar Max DR, pmkr  (eff. 1/01)
        "1363",     # Gem DR, DC, defib (eff. 1/01)
        "1364",     # Photon DR V-230HV3 DC defib (eff. 1/01)
        "1365",     # Guidewire, Hi-Torque 14/18/35 (eff. 1/01)
        "1366",     # Guidewire, PTCA, Hi-Torque (eff. 1/01)
        "1367",     # Guidewire, Hi-Torque Crosslt (eff. 1/01)
        "1369",     # ANS Renew Stim Sys recvr (eff. 1/01)
        "1370",     # Tension-Free Vaginal Tape (eff. 1/01)
        "1371",     # Symp Nitinol Transhep Bil Sys (eff. 1/01)
        "1372",     # Cordis Nitinol bil Stent (eff. 1/01)
        "1375",     # Stent, corornary, NIR (eff. 1/01)
        "1376",     # ANS Renew Stim Sys lead (eff. 1/01)
        "1377",     # Specify 3988 neuro lead (eff. 1/01)
        "1378",     # InterStim Tx 3080/3886 lead (eff. 1/01)
        "1379",     # Pisces-Quad 3887 lead (eff. 1/01)
        "1400",     # Diphenhydramine hcl 50 mg (eff. 1/01)
        "1401",     # Prochlorperazine maleate 5 mg (eff. 1/01)
        "1402",     # Promethazine hcl 12.5 mg oral (eff. 1/01)
        "1403",     # Chlorpromazine hcl 10mg oral (eff. 1/01)
        "1404",     # Trimethobenzamide hcl 250mg (eff. 1/01)
        "1405",     # Thiethylperazine maleate 10 mg (eff. 1/01)
        "1406",     # Perphenazine 4 mg oral (eff. 1/01)
        "1407",     # Hydroxyzine pamoate 25 mg (eff. 1/01)
        "1409",     # Factor via recombinant, per 1.2 mg (eff. 1/01)
        "1410",     # Prosorba column (eff. 1/01)
        "1411",     # Herculink, OTW SDS bil stent (eff. 1/01)
        "1420",     # StapleTac2 Bone w/Dermis (eff. 1/01)
        "1421",     # StapleTac2 Bone w/o Dermis (eff. 1/01)
        "1450",     # Orthosphere Arthroplasty (eff. 1/01)
        "1451",     # Orthosphere Arthroplasty Kity (eff. 1/01)
        "1500",     # Atherectomy sys, peripheral (eff. 1/01)
        "1600",     # TC 99M sestamibi, per syringe (eff. 1/01)
        "1601",     # TC 99M medronate, per dose (eff. 1/01)
        "1602",     # TC 99M apcitide, per vial (eff. 1/01)
        "1603",     # TL 201, mCi (eff. 1/01)
        "1604",     # IN 111 capromab pendetide, per dose (eff. 1/01)
        "1605",     # Abciximab injection, 10 mg (eff. 1/01)
        "1606",     # Anistreplase, 30 u (eff. 1/01)
        "1607",     # Eptifibatide injection, 5 mg (eff. 1/01)
        "1608",     # Etanercept injection, 25 mg (eff. 1/01)
        "1609",     # Rho(D) Immune globulin h, sd 100 iu (eff. 1/01)
        "1611",     # Hylan G-F 20 injection, 16 mg (eff. 1/01)
        "1612",     # Daclizumab, parenteral, 25 mg (eff. 1/01)
        "1613",     # Trastuzumab, 10 mg (eff. 1/01)
        "1614",     # Valrubicin, 200 mg (eff. 1/01)
        "1615",     # Basiliximab, 20 mg (eff. 1/01)
        "1616",     # Histrelin Acetate, 0.5 mg (eff. 1/01)
        "1617",     # Lepirdin, 50 mg (eff. 1/01)
        "1618",     # Von Willebrand factor, per iu (eff. 1/01)
        "1619",     # Ga 67, per mCi (eff. 1/01)
        "1620",     # TC 99M Bicisate, per vial (eff. 1/01)
        "1621",     # Xe 133, per mCi (eff. 1/01)
        "1622",     # TC 99M Mertiatide, per vial (eff. 1/01)
        "1623",     # TC 99M Gluceptate (eff. 1/01)
        "1624",     # P32 sodium, per mCi (eff. 1/01)
        "1625",     # IN 111 Pentetreotide, per mCi (eff. 1/01)
        "1626",     # TC 99M Oxidronate, per vial (eff. 1/01)
        "1627",     # TC-99 labeled red blood cell, per test (eff. 1/01)
        "1628",     # P32 phosphate chromic,per mCi (eff. 1/01)
        "1700",     # Authen Mick TP brachy needle (eff. 1/01) (obsolete 4/01)
        "1701",     # Medtec MT-BT-5201-25 ndl (eff. 1/01) (obsolete 4/01)
        "1702",     # WWMT brachytx needle (eff. 1/01) (obsolete 4/01)
        "1703",     # Mentor Prostate Brachy (eff. 1/01) (obsolete 4/01)
        "1704",     # MT-BT-5001-25/5051-25 (eff. 1/01) (obsolete 4/01)
        "1705",     # Best Flexi Brachy Needle (eff. 1/01) (obsolete 4/01)
        "1706",     # Indigo Prostate Seeding Ndl (eff. 1/01) (obsolete 4/01)
        "1707",     # Varisource Implt Ndl (eff. 1/01) (obsolete 4/01)
        "1708",     # UroMed Prostate Seed Ndl (eff. 1/01) (obsolete 4/01)
        "1709",     # Remington Brachytx Needle (eff. 1/01) (obsolete 4/01)
        "1710",     # US Biopsy Prostate Needle (eff. 1/01) (obsolete 4/01)
        "1711",     # MD Tech brachytx needle (eff. 1/01) (obsolete 4/01)
        "1712",     # Imagyn brachytx needle (eff. 1/01) (obsolete 4/01)
        "1713",     # Anchor/screw bn/bn,tis/bn (eff. 4/01)
        "1714",     # Cath, trans atherectomy, dir (eff. 4/01)
        "1715",     # Brachytherapy needle (eff. 4/01)
        "1716",     # Brachytx seed, Gold 198 (eff. 4/01)
        "1717",     # Brachytx seed, HDR Ir-192 (eff. 4/01)
        "1718",     # Brachytx seed, Iodine 125 (eff. 4/01)
        "1719",     # Brachytx seed, Non-HDR Ir-192 (eff. 4/01)
        "1720",     # Brachytx, Palladium 103 (eff. 4/01)
        "1721",     # AICD, dual chamber (eff. 4/01)
        "1722",     # AICD, single chamber (eff. 4/01)
        "1723",     # Cath, ablation, non-cardiac (eff. 4/01)
        "1724",     # Cath, trans atherec, rotation (eff. 4/01)
        "1725",     # Cath, translumin non-laser (eff. 4/01)
        "1726",     # Cath, bal dil, non-vascular (eff. 4/01)
        "1727",     # Cath, bal tis, dis, nonvas (eff. 4/01)
        "1728",     # Cath, brachytx seed adm (eff. 4/01)
        "1729",     # Cath, drainage, biliary (eff. 4/01)
        "1730",     # Cath, EP, 19 or fewer elect (eff. 4/01)
        "1731",     # Cath, EP, 20 or more elect (eff. 4/01)
        "1732",     # Cath, EP, diag/abl, 3D/vect (eff. 4/01)
        "1733",     # Cath, EP, other than temp (eff. 4/01)
        "1750",     # Cath, hemodialysis, long-term (eff. 4/01)
        "1751",     # Cath, inf pr/cent/midline (eff. 4/01)
        "1752",     # Cath, hemodialysis, short-term (eff. 4/01)
        "1753",     # Cath, intravas ultrasound (eff. 4/01)
        "1754",     # Catheter, intradiscal (eff. 4/01)
        "1755",     # Catheter, intraspinal (eff. 4/01)
        "1756",     # Cath, pacing, transesoph (eff. 4/01)
        "1757",     # Cath, thrombectomy/embolect (eff. 4/01)
        "1758",     # Cath, ureteral (eff. 4/01)
        "1759",     # Cath, intra echocardiography (eff. 4/01)
        "1760",     # Closure dev, vasc, imp/insert (eff. 4/01)
        "1762",     # Conn tiss, human (inc fascia) (eff. 4/01)
        "1763",     # Conn tiss, non-human (eff. 4/01)
        "1764",     # Event recorder, cardiac (eff. 4/01)
        "1767",     # Generator, neurostim, imp (eff. 4/01)
        "1768",     # Graft, vascular (eff. 4/01)
        "1769",     # Guide wire (eff. 4/01)
        "1770",     # Imaging coil, MR insertable (eff. 4/01)
        "1771",     # Rep dev, urinary , w/sling (eff. 4/01)
        "1772",     # Infusion pump, programmable (eff. 4/01)
        "1773",     # Retrieval dev, insert (eff. 4/01)
        "1776",     # Joint device (implantable) (eff. 4/01)
        "1777",     # Lead, AICD, endo single coil (eff. 4/01)
        "1778",     # Lead, neurostimulator (eff. 4/01)
        "1779",     # Lead, pmkr, transvenous VDD (eff. 4/01)
        "1780",     # Lens, intraocular (eff. 4/01)
        "1781",     # Mesh (implantable) (eff. 4/01)
        "1782",     # Morcellator (eff. 4/01)
        "1784",     # Ocular dev, intraop, det ret (eff. 4/01)
        "1785",     # Pmkr, dual, rate-resp (eff. 4/01)
        "1786",     # Pmkr, single, rate-resp (eff. 4/01)
        "1787",     # Patient progr, neurostim (eff. 4/01)
        "1788",     # Port, indwelling, imp (eff. 4/01)
        "1789",     # Prosthesis, breast, imp. (eff. 4/01)
        "1790",     # Iridium 192 HDR (eff. 1/01) (obsolete 4/01)
        "1791",     # OncoSeed, Rapid Strand I-125 (eff. 1/01) (obsolete 4/01)
        "1792",     # UroMed I-125 Brachy seed (eff. 1/01) (obsolete 4/01)
        "1793",     # Bard InterSource P-103 seed (eff. 1/01) (obsolete 4/01)
        "1794",     # Bard IsoSeed P-103 seed (eff. 1/01) (obsolete 4/01)
        "1795",     # Bard BrachySource I-125 (eff. 1/01) (obsolete 4/01)
        "1796",     # Source Tech Med I-125 (eff. 1/01) (obsolete 4/01)
        "1797",     # Draximage I-125 seed (eff. 1/01) (obsolete 4/01)
        "1798",     # Syncor I-125 PharmaSeed (eff. 1/01) (obsolete 4/01)
        "1799",     # I-Plant I-125 Brachytx seed (eff. 1/01) (obsolete 4/01)
        "1800",     # Pd-103 brachytx seed (eff. 1/01) (obsolete 4/01)
        "1801",     # IoGold I-125 brachytx seed (eff. 1/01) (obsolete 4/01)
        "1802",     # Iridium 192 brachytx seed (eff. 1/01) (obsolete 4/01)
        "1803",     # Best Iodine 125 brachytx seeds (eff. 1/01) (obsolete 4/01)
        "1804",     # Best Palladium 103 seeds (eff. 1/01) (obsolete 4/01)
        "1805",     # IsoStar Iodine-125 seeds (eff. 1/01) (obsolete 4/01)
        "1806",     # Gold 198 (eff. 1/01) (obsolete 4/01)
        "1810",     # D114S Dilatation Cath (eff. 1/01) (obsolete 4/01)
        "1811",     # Surgical Dynamics Anchors (eff. 1/01) (obsolete 4/01)
        "1812",     # OBL Anchors (eff. 1/01) (obsolete 4/01)
        "1813",     # Prosthesis, penile, inflatab (eff. 4/01)
        "1815",     # Pros, urinary sph, imp (eff. 4/01)
        "1816",     # Receiver/transmitter, neuro (eff. 4/01)
        "1817",     # Septal defect imp sys (eff. 4/01)
        "1850",     # Repliform 14/21 sq cm (eff. 1/01) (obsolete 4/01)
        "1851",     # Repliform 24/28 sq cm (eff. 1/01) (obsolete 4/01)
        "1852",     # TransCyte, per 247 sq cm (eff. 1/01) (obsolete 4/01)
        "1853",     # Suspend, per 8/14 sq cm (eff. 1/01) (obsolete 4/01)
        "1854",     # Suspend, per 24/28 sq cm (eff. 1/01) (obsolete 4/01)
        "1855",     # Suspend, per 36 sq cm (eff. 1/01) (obsolete 4/01)
        "1856",     # Suspend, per 48 sq cm (eff. 1/01) (obsolete 4/01)
        "1857",     # Suspend, per 84 sq cm (eff. 1/01) (obsolete 4/01)
        "1858",     # DuraDerm, per 8/14 sq cm (eff. 1/01) (obsolete 4/01)
        "1859",     # DuraDerm, per 21/24 sq cm (eff. 1/01) (obsolete 4/01)
        "1860",     # DuraDerm, per 48 sq cm (eff. 1/01) (obsolete 4/01)
        "1861",     # DuraDerm, per 36 sq cm (eff. 1/01) (obsolete 4/01)
        "1862",     # DuraDerm, per 72 sq cm (eff. 1/01) (obsolete 4/01)
        "1863",     # DuraDerm, per 84 sq cm (eff. 1/01) (obsolete 4/01)
        "1864",     # SpermaTex, per 13/44 sq cm (eff. 1/01) (obsolete 4/01)
        "1865",     # FasLata, per 8/14 sq cm (eff. 1/01) (obsolete 4/01)
        "1866",     # FasLata, per 24/28 sq cm (eff. 1/01) (obsolete 4/01)
        "1867",     # FasLata, per 36/48 sq cm (eff. 1/01) (obsolete 4/01)
        "1868",     # FasLata, per 96 sq cm (eff. 1/01) (obsolete 4/01)
        "1869",     # Gore Thyroplasty Dev (eff. 1/01) (obsolete 4/01)
        "1870",     # DermMatrix, per 16 sq cm (eff. 1/01) (obsolete 4/01)
        "1871",     # DermMatrix, 32 or 64 sq cm (eff. 1/01) (obsolete 4/01)
        "1872",     # Dermagraft, per 37.5 sq cm (eff. 1/01) (obsolete 4/01)
        "1873",     # Bard 3DMax Mesh (eff. 1/01) (obsolete 4/01)
        "1874",     # Stent, coated/cov w/del sys (eff. 4/01)
        "1875",     # Stent, coated/cov w/o del sys (eff. 4/01)
        "1876",     # Stent, non-coated/no-cov w/del (eff. 4/01)
        "1877",     # Stent, non-coated/cov w/o del (eff. 4/01)
        "1878",     # Martl for vocal cord (eff. 4/01)
        "1879",     # Tissue marker, imp (eff. 4/01)
        "1880",     # Vena cava filter (eff. 4/01)
        "1881",     # Dialysis access system (eff. 4/01)
        "1882",     # AICD, other than sing/dual (eff. 4/01)
        "1883",     # Adapt/ext, pacing/neuro lead (eff. 4/01)
        "1885",     # Cath, translumin angio laser (eff. 4/01)
        "1887",     # Catheter, guiding (eff. 4/01)
        "1891",     # Infusion pump, non-prog, perm (eff. 4/01)
        "1892",     # Intro/sheath , fixed, peel-away (eff. 4/01)
        "1893",     # Intro/sheath, fixed, non-peel (eff. 4/01)
        "1894",     # Intro/sheath, non-laser (eff. 4/01)
        "1895",     # Lead, AICD, endo dual coil (eff. 4/01)
        "1896",     # Lead, AICD, non sing/dual (eff. 4/01)
        "1897",     # Lead, neurostim test kit (eff. 4/01)
        "1898",     # Lead, pmkr, other than trans (eff. 4/01)
        "1899",     # Lead, pmkr/AICD combination (eff. 4/01)
        "1929",     # Maverick PTCA Cath (eff. 1/01) (obsolete 4/01)
        "1930",     # Coyote Dil Cath, 20/30/40mm (eff. 1/01) (obsolete 4/01)
        "1931",     # Talon Dil Cath (eff. 1/01) (obsolete 4/01)
        "1932",     # Scimed remedy Dil Cath (eff. 1/01) (obsolete 4/01)
        "1933",     # Opti-Plast XL/Centurion Cath (eff. 1/01) (obsolete 4/01)
        "1934",     # Ultraverse 3.5F Bal Dil Cath (eff. 1/01) (obsolete 4/01)
        "1935",     # Workhorse PTA Bal Cath (eff. 1/01) (obsolete 4/01)
        "1936",     # Uromax Ultra Bal Dil Cath (eff. 1/01) (obsolete 4/01)
        "1937",     # Synergy Balloon Dil Cath (eff. 1/01) (obsolete 4/01)
        "1938",     # Uroforce Bal Dil Cath (eff. 1/01) (obsolete 4/01)
        "1939",     # Raptur, Ninja PTCA Dil Cath (eff. 1/01) (obsolete 4/01)
        "1940",     # PowerFlex, OPTA 5/LP Bal Cath (eff. 1/01) (obsolete 4/01)
        "1941",     # Jupiter PTA Dil Cath (eff. 1/01) (obsolete 4/01)
        "1942",     # Cordis Maxi LD PTA Bal Cath (eff. 1/01) (obsolete 4/01)
        "1943",     # RXCrossSail OTW OpenSail (eff. 1/01) (obsolete 4/01)
        "1944",     # Rapid Exchange Bil Dil Cath (eff. 1/01) (obsolete 4/01)
        "1945",     # Savvy PTA Dil Cath (eff. 1/01) (obsolete 4/01)
        "1946",     # R1s Rapid Dil Cath (eff. 1/01) (obsolete 4/01)
        "1947",     # Gazelle Bal Dil Cath (eff. 1/01) (obsolete 4/01)
        "1948",     # Pursuit Balloon Cath (eff. 1/01) (obsolete 4/01)
        "1949",     # Oracle Megasonics Cath (eff. 1/01) (obsolete 4/01)
        "1979",     # Visions PV/Avanar US Cath (eff. 1/01) (obsolete 4/01)
        "1980",     # Atlantis SR Coronary Cath (eff. 1/01) (obsolete 4/01)
        "1981",     # PTCA Catheters (eff. 1/01) (obsolete 4/01)
        "2000",     # Orbiter ST Steerable Cath (eff. 1/01) (obsolete 4/01)
        "2001",     # Constellation Diag Cath (eff. 1/01) (obsolete 4/01)
        "2002",     # Irvine 5F Inquiry Diag EP Cath (eff. 1/01) (obsolete 4/01)
        "2003",     # Irvine 6F Inquiry Diag EP Cath (eff. 1/01) (obsolete 4/01)
        "2004",     # Biosense EP Cath -- Octapolar (eff. 1/01) (obsolete 4/01)
        "2005",     # Biosense EP Cath -- Hexapolar (eff. 1/01) (obsolete 4/01)
        "2006",     # Biosense EP Cath -- Decapolar (eff. 1/01) (obsolete 4/01)
        "2007",     # Irvine 6F Luma-Cath EP Cath (eff. 1/01) (obsolete 4/01)
        "2008",     # 7F Luma-Cath EP Cath 81910-15 (eff. 1/01) (obsolete 4/01)
        "2009",     # Irvine 7F Luma-Cath EP Cath (eff. 1/01) (obsolete 4/01)
        "2010",     # Fixed Curve EP Cath (eff. 1/01) (obsolete 4/01)
        "2011",     # Deflectable Tip Cath--Quad (eff. 1/01) (obsolete 4/01)
        "2012",     # Celsius Abln Cath (eff. 1/01) (obsolete 4/01)
        "2013",     # Celsius Large Abln Cath (eff. 1/01) (obsolete 4/01)
        "2014",     # Celsius II Asym Abln Cath (eff. 1/01) (obsolete 4/01)
        "2015",     # Celsius II Sym Abln Cath (eff. 1/01) (obsolete 4/01)
        "2016",     # Navi-Star DS, Navi-Star Ther (eff. 1/01) (obsolete 4/01)
        "2017",     # Navi-Star Abln Cath (eff. 1/01) (obsolete 4/01)
        "2018",     # Polaris T Ablation Cath (eff. 1/01) (obsolete 4/01)
        "2019",     # EP Deflectable Cath (eff. 1/01) (obsolete 4/01)
        "2020",     # Blazer II XP Abln Cath (eff. 1/01) (obsolete 4/01)
        "2021",     # SilverFlex EP Cath (eff. 1/01) (obsolete 4/01)
        "2022",     # CP Chilli Cooled Abln Cath (eff. 1/01) (obsolete 4/01)
        "2023",     # Chilli Cld AblnCath-std, lg (eff. 1/01) (obsolete 4/01)
        "2100",     # CP CS Reference Cath (eff. 1/01) (obsolete 4/01)
        "2102",     # CP Radii 7F EP Cath (eff. 1/01) (obsolete 4/01)
        "2103",     # CP Radii 7F EP Cath w/Track (eff. 1/01) (obsolete 4/01)
        "2104",     # Lasso Deflectable Cath (eff. 1/01) (obsolete 4/01)
        "2151",     # Veripath Guiding Cath (eff. 1/01) (obsolete 4/01)
        "2152",     # Cordis Vista Brite Tip Cath (eff. 1/01) (obsolete 4/01)
        "2153",     # Bard Viking Cath (eff. 1/01) (obsolete 4/01)
        "2200",     # Arrow-Trerotola PTD Cath (eff. 1/01) (obsolete 4/01)
        "2300",     # Varisource Stnd Catheters (eff. 1/01) (obsolete 4/01)
        "2597",     # Clinicath/kit 16/18 sgl/dbl (eff. 1/01) (obsolete 4/01)
        "2598",     # Clinicath 18/20/24-G single (eff. 1/01) (obsolete 4/01)
        "2599",     # Clinicath 16/18-G-double (eff. 1/01) (obsolete 4/01)
        "2601",     # Bard DL Ureteral Cath (eff. 1/01) (obsolete 4/01)
        "2602",     # Vitesse Laser Cath 1.4/1.7mm (eff. 1/01) (obsolete 4/01)
        "2603",     # Vitesse Laser Cath 2.0mm (eff. 1/01) (obsolete 4/01)
        "2604",     # Vitesse E Laser Cath 2.0mm (eff. 1/01) (obsolete 4/01)
        "2605",     # Extreme Laser Catheter (eff. 1/01) (obsolete 4/01)
        "2606",     # SpineCath XL Catheter (eff. 1/01) (obsolete 4/01)
        "2607",     # SpineCath Intradiscal Cath (eff. 1/01) (obsolete 4/01)
        "2608",     # Scimed 6F Wiseguide Cath (eff. 1/01) (obsolete 4/01)
        "2609",     # Flexima Bil Draingage Cath (eff. 1/01) (obsolete 4/01)
        "2610",     # FlexTipPlus Intraspinal Cath (eff. 1/01) (obsolete 4/01)
        "2611",     # AlgoLine Intraspinal Cath (eff. 1/01) (obsolete 4/01)
        "2612",     # InDura Catheter (eff. 1/01) (obsolete 4/01)
        "2615",     # Sealant, pulmonary, liquid (eff. 4/01)
        "2616",     # Brachytx seed, Yttrium-90 (eff. 4/01)
        "2617",     # Stent, non-cor, tem w/o del (eff. 4/01)
        "2618",     # Probe, cryoablation (eff. 4/01)
        "2619",     # Pmkr, dual, non rate-resp (eff. 4/01)
        "2620",     # Pmkr, single, non rate-resp (eff. 4/01)
        "2621",     # Pmkr, other than single/dual (eff. 4/01)
        "2622",     # Prosthesis, penile, non-inf (eff. 4/01)
        "2625",     # Stent, non-cor , tem w/del sys (eff. 4/01)
        "2626",     # Infusion pump, non-prog, temp (eff. 4/01)
        "2627",     # Cath, suprapubic/cystoscopic (eff. 4/01)
        "2628",     # Catheter, occlusion (eff. 4/01)
        "2629",     # Intro/sheath, laser (eff. 4/01)
        "2630",     # Cath, EP, temp-controlled (eff. 4/01)
        "2631",     # Rep dev, urinary, w/o sling (eff. 4/01)
        "2700",     # MycroPhylax Plus CS defib (eff. 1/01) (obsolete 4/01)
        "2701",     # Phylax XM SC defib (eff. 1/01) (obsolete 4/01)
        "2702",     # Ventak Prizm 2VR Defib (eff. 1/01) (obsolete 4/01)
        "2703",     # Ventak Prizm VR HE Defib (eff. 1/01) (obsolete 4/01)
        "2704",     # Ventak Mini IV + Defib (eff. 1/01) (obsolete 4/01)
        "2801",     # Defender IV DR 612 DC defib (eff. 1/01) (obsolete 4/01)
        "2802",     # Phylax AV DC defib (eff. 1/01) (obsolete 4/01)
        "2803",     # Ventak Prizm DR HE Defib (eff. 1/01) (obsolete 4/01)
        "2804",     # Ventak Prizm 2 DR Defib (eff. 1/01) (obsolete 4/01)
        "2805",     # Jewel AF 7250 Defib (eff. 1/01) (obsolete 4/01)
        "2806",     # GEM VR 7227 Defib (eff. 1/01) (obsolete 4/01)
        "2807",     # Contak CD 1823 (eff. 1/01) (obsolete 4/01)
        "2808",     # Contak TR 1241 (eff. 1/01) (obsolete 4/01)
        "3001",     # Kainox SL/RV defib lead (eff. 1/01) (obsolete 4/01)
        "3002",     # EasyTrak Defib Lead (eff. 1/01) (obsolete 4/01)
        "3003",     # Endotak SQ Array XP lead (eff. 1/01) (obsolete 4/01)
        "3004",     # Intervene Defib lead (eff. 1/01) (obsolete 4/01)
        "3400",     # Siltex Spectrum, Contour Prof (eff. 1/01) (obsolete 4/01)
        "3401",     # Saline-Filled Spectrum (eff. 1/01) (obsolete 4/01)
        "3500",     # Mentor alpha I Inf Penile Pros (eff. 1/01) (obsolete 4/01)
        "3510",     # AMS 800 Urinary Pros (eff. 1/01) (obsolete 4/01)
        "3551",     # Choice/PT Graphix/Luge/Trooper (eff. 1/01) (obsolete 4/01)
        "3552",     # Hi-Torque Whisper (eff. 1/01) (obsolete 4/01)
        "3553",     # Cordis guidewires (eff. 1/01) (obsolete 4/01)
        "3554",     # Jindo guidewire (eff. 1/01) (obsolete 4/01)
        "3555",     # Wholey Hi-Torque Plus GW (eff. 1/01) (obsolete 4/01)
        "3556",     # Wave/FlowWire Guidewire (eff. 1/01) (obsolete 4/01)
        "3557",     # HyTek guidewire (eff. 1/01) (obsolete 4/01)
        "3800",     # SynchroMed EL infusion pump (eff. 1/01) (obsolete 4/01)
        "3801",     # Arrow/Microject PCAQ Sys (eff. 1/01) (obsolete 4/01)
        "3851",     # Elastic UV IOL AA-4203T/TF/TL (eff. 1/01) (obsolete 4/01)
        "4000",     # Opus G 4621, 4624 SC pmkr (eff. 1/01) (obsolete 4/01)
        "4001",     # Opus S 4121/4124 SC pmkr (eff. 1/01) (obsolete 4/01)
        "4002",     # Talent 113 SC pmkr (eff. 1/01) (obsolete 4/01)
        "4003",     # Kairos SR SC pmkr (eff. 1/01) (obsolete 4/01)
        "4004",     # Actros SR, Actros SLR SC pmkr (eff. 1/01) (obsolete 4/01)
        "4005",     # Philos SR/SR-B SC pmkr (eff. 1/01) (obsolete 4/01)
        "4006",     # Pulsar Max II SR pmkr (eff. 1/01) (obsolete 4/01)
        "4007",     # Marathon SR pmkr (eff. 1/01) (obsolete 4/01)
        "4008",     # Discovery II SSI pmkr (eff. 1/01) (obsolete 4/01)
        "4009",     # Discovery II SR pmkr (eff. 1/01) (obsolete 4/01)
        "4300",     # Integrity AFx DR 5342 pmkr (eff. 1/01) (obsolete 4/01)
        "4301",     # Integrity AFx DR 5346 pmkr (eff. 1/01) (obsolete 4/01)
        "4302",     # Affinity VDR 5430 DR (eff. 1/01) (obsolete 4/01)
        "4303",     # Brio 112 DC pmkr (eff. 1/01) (obsolete 4/01)
        "4304",     # Brio 212, Talent 213/223 DC pmkr (eff. 1/01) (obsolete 4/01)
        "4305",     # Brio 222 DC pmkr (eff. 1/01) (obsolete 4/01)
        "4306",     # Brio 220 DC pmkr (eff. 1/01) (obsolete 4/01)
        "4307",     # Kairos DR DC pmkr (eff. 1/01) (obsolete 4/01)
        "4308",     # Inos2, Inos2+ DC pmkr (eff. 1/01) (obsolete 4/01)
        "4309",     # Actros DR,D,DR-A, SLR DC pmkr (eff. 1/01) (obsolete 4/01)
        "4310",     # Actros DR-B DC pmkr (eff. 1/01) (obsolete 4/01)
        "4311",     # Philos DR/DR-B/SLR DC (eff. 1/01) (obsolete 4/01)
        "4312",     # Pulsar Max II DR pmkr (eff. 1/01) (obsolete 4/01)
        "4313",     # Marathon DR pmkr (eff. 1/01) (obsolete 4/01)
        "4314",     # Momentum DR pmkr (eff. 1/01) (obsolete 4/01)
        "4315",     # Selection AFm pmkr (eff. 1/01) (obsolete 4/01)
        "4316",     # Discovery II DR (eff. 1/01) (obsolete 4/01)
        "4317",     # Discovery II DDD (eff. 1/01) (obsolete 4/01)
        "4600",     # Snynox, Polyrox, Elox, Retrox (eff. 1/01) (obsolete 4/01)
        "4602",     # Tendril SDX, 1488K pmkr lead (eff. 1/01) (obsolete 4/01)
        "4603",     # Oscor/Flexion pmkr lead (eff. 1/01) (obsolete 4/01)
        "4604",     # CrystallineActFix, CapsureFix (eff. 1/01) (obsolete 4/01)
        "4605",     # CapSure Epi pmkr lead (eff. 1/01) (obsolete 4/01)
        "4606",     # Flextend pmkr lead (eff. 1/01) (obsolete 4/01)
        "4607",     # FinelineII/EZ, ThinlineII/EZ (eff. 1/01) (obsolete 4/01)
        "5000",     # BX Velocity w/Hepacoat (eff. 1/01) (obsolete 4/01)
        "5001",     # Memotherm Bil Stent, sm, med (eff. 1/01) (obsolete 4/01)
        "5002",     # Memotherm Bil Stent, large (eff. 1/01) (obsolete 4/01)
        "5003",     # Memotherm Bil Stent, x-large (eff. 1/01) (obsolete 4/01)
        "5004",     # PalmazCorinthian IQ Bil Stent (eff. 1/01) (obsolete 4/01)
        "5005",     # PalmazCorinthian IQ Trans/Bil (eff. 1/01) (obsolete 4/01)
        "5006",     # PalmazTran Bil Stent Sys-Med (eff. 1/01) (obsolete 4/01)
        "5007",     # PalmazTran XL Bil Stent--40mm (eff. 1/01) (obsolete 4/01)
        "5008",     # PalmazTran XL Bil Stent--50mm (eff. 1/01) (obsolete 4/01)
        "5009",     # VistaFlex Biliary Stent (eff. 1/01) (obsolete 4/01)
        "5010",     # Rapid Exchange Bil Stent Sys (eff. 1/01) (obsolete 4/01)
        "5011",     # IntraStent, IntraStent LP (eff. 1/01) (obsolete 4/01)
        "5012",     # IntraStent DoubleStrut LD (eff. 1/01) (obsolete 4/01)
        "5013",     # IntraStent DoubleStrut XS (eff. 1/01) (obsolete 4/01)
        "5014",     # AVE Bridge Stent Sys-10/17/28 (eff. 1/01) (obsolete 4/01)
        "5015",     # AVE/X3 Bridge Sys, 40-100 (eff. 1/010 (obsolete 4/01)
        "5016",     # Biliary stent single use cov (eff. 1/01) (obsolete 4/01)
        "5017",     # WallstentRP Bil--20/40/60/68mm (eff. 1/01) (obsolete 4/01)
        "5018",     # WallstentRP Bil--80/94mm (eff. 1/01) (obsolete 4/01)
        "5019",     # Flexima Bil Stent Sys (eff. 1/01) (obsolete 4/01)
        "5020",     # Smart Nitinol Stent--20mm (eff. 1/01) (obsolete 4/01)
        "5021",     # Smart Nitinol Stent--40/60mm (eff. 1/01) (obsolete 4/01)
        "5022",     # Smart Nitinol Stent--80mm (eff. 1/01) (obsolete 4/01)
        "5023",     # BX Velocity Stent--8/13mm (eff. 1/01) (obsolete 4/01)
        "5024",     # BX Velocity Stent 18mm (eff. 1/01) (obsolete 4/01)
        "5025",     # BX Velocity Stent 23 mm (eff. 1/01) (obsolete 4/01)
        "5026",     # BX Velocity Stent 28/33mm (eff. 1/01) (obsolete 4/01)
        "5027",     # BX Velocity Stent w/Hep--8/13mm (eff. 1/01) (obsolete 4/01)
        "5028",     # BX Velocity Stent w/Hep--18mm (eff. 1/01) (obsolete 4/01)
        "5029",     # BX Velocity Stent w/Hep--23mm (eff. 1/01) (obsolete 4/01)
        "5030",     # Stent, coronary, S660 9/12mm (eff. 1/01) (obsolete 4/01)
        "5031",     # Stent, coronary, S660 15/18mm (eff. 1/01) (obsolete 4/01)
        "5032",     # Stent, coronary, S660 24/30mm (eff. 1/01) (obsolete 4/01)
        "5033",     # Niroyal Stent Sys, 9mm (eff. 1/01) (obsolete 4/01)
        "5034",     # Niroyal Stent Sys, 12/15mm (eff. 1/01) (obsolete 4/01)
        "5035",     # Niroyal Stent Sys, 18mm (eff. 1/01) (obsolete 4/01)
        "5036",     # Niroyal Stent Sys, 25mm (eff. 1/01) (obsolete 4/01)
        "5037",     # Niroyal Stent Sys, 31mm (eff. 1/01) (obsolete 4/01)
        "5038",     # BX Velocity Stent w/Raptor (eff. 1/01) (obsolete 4/01)
        "5039",     # IntraCoil Periph Stent--40mm (eff. 1/01) (obsolete 4/01)
        "5040",     # IntraCoil Periph Stent--60mm (eff. 1/01) (obsolete 4/01)
        "5041",     # BeStent Over-the-Wire 24/30mm (eff. 1/01) (obsolete 4/01)
        "5042",     # BeStent Over-the-Wire 18mm (eff. 1/01) (obsolete 4/01)
        "5043",     # BeStent Over-the-Wire 15mm (eff. 1/01) (obsolete 4/01)
        "5044",     # BeStent Over-the-Wire 9/12mm (eff. 1/01) (obsolete 4/01)
        "5045",     # Multilink Tetra Cor Stent Sys (eff. 1/01) (obsolete 4/01)
        "5046",     # Radius 20mm cor stent (eff. 1/01) (obsolete 4/01)
        "5047",     # Niroyal Elite Cor Stent Sys (eff. 1/01) (obsolete 4/01)
        "5048",     # GR II Coronary Stent (eff. 1/01) (obsolete 4/01)
        "5130",     # Wilson-Cook Colonic Z-Stent (eff. 1/01) (obsolete 4/01)
        "5131",     # Bard Colorectal Stent-60mm (eff. 1/01) (obsolete 4/01)
        "5132",     # Bard Colorectal Stent-80mm (eff. 1/01) (obsolete 4/01)
        "5133",     # Bard Colorectal Stent-100mm (eff. 1/01) (obsolete 4/01)
        "5134",     # Enteral Wallstent-90mm (eff. 1/01) (obsolete 4/01)
        "5279",     # Contour/Percuflex Stent (eff. 1/01) (obsolete 4/01)
        "5280",     # Inlay Dbl Ureteral Stent (eff. 1/01) (obsolete 4/01)
        "5281",     # Wallgraft Trach Sys 70mm (eff. 1/01) (obsolete 4/01)
        "5282",     # Wallgraft Trach Sys 20/30/50 (eff. 1/01) (obsolete 4/01)
        "5283",     # Wallstent/RP TIPS--80mm (eff. 1/01) (obsolete 4/01)
        "5284",     # Wallstent TrachUltraFlex (eff. 1/01) (obsolete 4/01)
        "5600",     # Closure dev, VasoSeal ES (eff. 1/01) (obsolete 4/01)
        "5601",     # VasoSeal Model 1000 (eff. 1/01) (obsolete 4/01)
        "6001",     # Composix Mesh 8/21 in (eff. 1/01) (obsolete 4/01)
        "6002",     # Composix Mesh 32 in (eff. 1/01) (obsolete 4/01)
        "6003",     # Composix Mesh 48 in (eff. 1/01) (obsolete 4/01)
        "6004",     # Composix Mesh 80 in (eff. 1/01) (obsolete 4/01)
        "6005",     # Composix Mesh 140 in (eff. 1/01) (obsolete 4/01)
        "6006",     # Composix Mesh 144 in (eff. 1/01) (obsolete 4/01)
        "6012",     # Pelvicol Collagen 8/14 sq cm (eff. 1/01) (obsolete 4/01)
        "6013",     # Pelvicol Collagen 21/24/28 sq cm (eff. 1/01) (obsolete 4/01)
        "6014",     # Pelvicol Collagen 36 sq cm (eff. 1/01) (obsolete 4/01)
        "6015",     # Pelvicol Collagen 48 sq cm (eff. 1/01) (obsolete 4/01)
        "6016",     # Pelvicol Collagen 96 sq cm (eff. 1/01) (obsolete 4/01)
        "6017",     # Gore-Tex DualMesh 75/96 sq cm (eff. 1/01) (obsolete 4/01)
        "6018",     # Gore-Tex DualMesh 150 sq cm (eff. 1/01) (obsolete 4/01)
        "6019",     # Gore-Tex DualMesh 285 sq cm (eff. 1/01) (obsolete 4/01)
        "6020",     # Gore-Tex DualMesh 432 sq cm (eff. 1/01) (obsolete 4/01)
        "6021",     # Gore-Tex DualMesh 600 sq cm (eff. 1/01) (obsolete 4/01)
        "6022",     # Gore-Tex DualMesh 884 sq cm (eff. 1/01) (obsolete 4/01)
        "6023",     # Gore-TexPlus 1mm, 75/96 sq cm (eff. 1/01) (obsolete 4/01)
        "6024",     # Gore-TexPlus 1mm, 150 sq cm (eff. 1/01) (obsolete 4/01)
        "6025",     # Gore-TexPlus 1mm, 285 sq cm (eff. 1/01) (obsolete 4/01)
        "6026",     # Gore-TexPlus 1mm, 432 sq cm (eff. 1/01) (obsolete 4/01)
        "6027",     # Gore-TexPlus 1mm, 600 sq cm (eff. 1/01) (obsolete 4/01)
        "6028",     # Gore-TexPlus 1mm, 884 sq cm (eff. 1/01) (obsolete 4/01)
        "6029",     # Gore-TexPlus 2mm, 150 sq cm (eff. 1/01) (obsolete 4/01)
        "6030",     # Gore-TexPlus 2mm, 285 sq cm (eff. 1/01) (obsolete 4/01)
        "6031",     # Gore-TexPlus 2mm, 432 sq cm (eff. 1/01) (obsolete 4/01)
        "6032",     # Gore-TexPlus 2mm, 600 sq cm (eff. 1/01) (obsolete 4/01)
        "6033",     # Gore-TexPlus 2mm, 884 sq cm (eff. 1/01) (obsolete 4/01)
        "6034",     # Bard ePTFE: 150 sq cm-2mm (obsolete 4/01)
        "6035",     # Bard ePTFE: 150sqcm-1mm,75-2mm (eff. 1/01) (obsolete 4/01)
        "6036",     # Bard ePTFE: 50/75sqcm-1,2mm (eff. 1/01) (obsolete 4/01)
        "6037",     # Bard ePTFE: 300 sq cm-1,2mm (eff. 1/01) (obsolete 4/01)
        "6038",     # Bard ePTFE: 600 sq cm-1mm (eff. 1/01) (obsolete 4/01)
        "6039",     # Bard ePTFE: 884sq cm-1mm (eff. 1/01) (obsolete 4/01)
        "6040",     # Bard ePTFE: 600sq cm-2mm (eff. 1/01) (obsolete 4/01)
        "6041",     # Bard ePTFE: 884sq cm -2mm (eff. 1/01) (obsolete 4/01)
        "6050",     # Female Sling Sys w/wo Matrl (eff. 1/01) (obsolete 4/01)
        "6051",     # Stratasis Sling, 20/40 cm (eff. 1/01) (obsolete 4/01)
        "6052",     # Stratasis Sling, 60 cm (eff. 1/01) (obsolete 4/01)
        "6053",     # Surgisis Soft Graft (eff. 1/01) (obsolete 4/01)
        "6054",     # Surgisis Enhanced Graft (eff. 1/01) (obsolete 4/01)
        "6055",     # Surgisis Enhanced Tissue (eff. 1/01) (obsolete 4/01)
        "6056",     # Surgisis Soft Tissue Graft (eff. 1/01) (obsolete 4/01)
        "6057",     # Surgisis Hernia Graft (eff. 1/01) (obsolete 4/01)
        "6058",     # SurgiPro Hernia Plug, med/lg (eff. 1/01) (obsolete 4/01)
        "6080",     # Male Sling Sys w/wo Matrial (eff. 1/01) (obsolete 4/01)
        "6200",     # Exxcel Soft ePTFE vas graft (ef. 1/01) (obsolete 4/01)
        "6201",     # Impra Venaflo--10/20cm (eff. 1/01) (obsolete 4/01)
        "6202",     # Impra Venaflo--30/40 cm (eff. 1/01) (obsolete 4/01)
        "6203",     # Impra Venaflo--50 cm, vt45 (eff. 1/01) (obsolete 4/01)
        "6204",     # Impra Venaflo--stepped (eff. 1/01) (obsolete 4/01)
        "6205",     # Impra Carboflo--10cm (eff. 1/01) (obsolete 4/01)
        "6206",     # Impra Carboflo--20 cm (eff. 1/01) (obsolete 4/01)
        "6207",     # Impra Carboflo--30/35/40cm (eff. 1/01) (obsolete 4/01)
        "6208",     # Impra Carboflo--40/50cm (eff. 1/01) (obsolete 4/01)
        "6209",     # Impra Carboflo--ctrflex (eff. 1/01) (obsolete 4/01)
        "6210",     # Exxcel ePTFE vas graft (eff. 1/01) (obsolete 4/01)
        "6300",     # Vanguard III Endovas Graft (eff. 1/01) (obsolete 4/01)
        "6500",     # Preface Guiding Sheath (eff. 1/01) (obsolete 4/01)
        "6501",     # Soft Tip Sheaths (eff. 1/01) (obsolete 4/01)
        "6502",     # Perry Exchange Dilator (eff. 1/01) (obsolete 4/01)
        "6525",     # Spectranetics Laser Sheath (eff. 1/01) (obsolete 4/01)
        "6600",     # Micro Litho Flex Probes (eff. 1/01) (obsolete 4/01)
        "6650",     # Fast-Cath Guiding Introducer (eff. 1/01) (obsolete 4/01)
        "6651",     # Seal-Away Guding Introducer (eff. 1/01) (obsolete 4/01)
        "6652",     # Bard Excalibur Introducer (eff. 1/01) (obsolete 4/01)
        "6700",     # Focal Seal-L (eff. 1/01) (obsolete 4/01)
        "7000",     # Amifostine, 500 mg (eligible for pass-through payments)
        "7001",     # Amphotericin B lipid complex, 50 mg, Inj (eligible for pass-through payments)
        "7002",     # Clonidine, HCl, 1 MG (eligible for pass-through payments) (obsolete 1/01)
        "7003",     # Epoprostenol, 0.5 MG, inj (eligible for pass-through payments)
        "7004",     # Immune globulin intravenous human 5g, inj (eligible for pass-through payments)
        "7005",     # Gonadorelin hcI, 100 mcg (eligible for pass-through payments)
        "7007",     # Milrinone lacetate, per 5 ml, inj (not subject to national coinsurance)
        "7010",     # Morphine sulfate concentrate (preservative free) per 10 mg (eligible for pass-through payments)
        "7011",     # Oprelevekin, inj, 5 mg (eligible for pass-through payments)
        "7012",     # Pentamidine isethionate, 300 mg (eligible for pass-through payments) (obsolete 1/01)
        "7014",     # Fentanyl citrate, inj, up to 2 ml (eligible for pass-through payments)
        "7015",     # Busulfan, oral 2 mg (eligible for pass-through payments)
        "7019",     # Aprotinin, 10,000 kiu (eligible for pass-through payments)
        "7021",     # Baclofen, intrathecal, 50 mcg (eligible for pass-through payments) (obsolete 1/01)
        "7022",     # Elliotts B Solution, per ml (eligible for pass-through payments)
        "7023",     # Treatment for bladder calculi, I.e. Renacidin per 500 ml (eligible for pass-through payments)
        "7024",     # Corticorelin ovine triflutate, 0.1 mg (eligible for pass-through payments)
        "7025",     # Digoxin immune FAB (Ovine), 10 mg (eligible for pass-through payments)
        "7026",     # Ethanolamine oleate, 1000 ml (eligible for pass-through payments)
        "7027",     # Fomepizole, 1.5 G (eligible for pass-through payments)
        "7028",     # Fosphenytoin, 50 mg (eligible for pass-through payments)
        "7029",     # Glatiramer acetate, 25 mg (eligible for pass-through payments)
        "7030",     # Hemin, 1 mg (eligible for pass-through payments)
        "7031",     # Octreotide Acetate, 500 mcg (eligible for pass-through payments)
        "7032",     # Sermorelin acetate, 0.5 mg (eligible for pass-through payments)
        "7033",     # Somatrem, 5 mg (eligible for pass-through payments)
        "7034",     # Somatropin, 1 mg (eligible for pass-through payments)
        "7035",     # Teniposide, 50 mg (eligible for pass-through payments)
        "7036",     # Urokinase, inj, IV, 250,000 I.U. (not subject to national coinsurance)
        "7037",     # Urofollitropin, 75 I.U. (eligible for pass-through payments)
        "7038",     # Muromonab-CD3, 5 mg (eligible for pass-through payments)
        "7039",     # Pegademase bovine inj 25 I.U. (eligible for pass-through payments)
        "7040",     # Pentastarch 10% inj, 100 ml (eligible for pass-through payments)
        "7041",     # Tirofiban HCL, 0.5 mg (not subject to national coinsurance)
        "7042",     # Capecitabine, oral 150 mg (eligible for pass-through payments)
        "7043",     # Infliximab, 10 MG (eligible for pass-through payments)
        "7045",     # Trimetrexate Glucoronate (eligible for pass-through payments)
        "7046",     # Doxorubicin Hcl Liposome (eligible for pass-through payments)
        "7047",     # Droperidol/fentanyl inj (eff. 1/01)
        "7048",     # Alteplase, 1 mg (eff. 1/01)
        "7049",     # Filgrastim 480 mcg injection (eff. 1/01)
        "7315",     # Sodium hyaluronate, 20 mg (eff. 1/01)
        "8099",     # Spectranetics Lead Lock Dev (eff. 1/01) (obsolete 4/01)
        "8100",     # Adhesion barrier, ADCON-L (eff. 1/01) (obsolete 4/01)
        "8102",     # SurgiVision Esoph Coil (eff. 1/01) (obsolete 4/01)
        "9000",     # Na chromate Cr51, per 0.25mCi (eff. 1/01)
        "9001",     # Linezolid inj, 200mg (eff. 1/01)
        "9002",     # Tenecteplase, 50mg/vial (eff. 1/01)
        "9003",     # Palivizumab, per 50 mg (eff. 1/01)
        "9004",     # Gemtuzumab ozogamicin inj, 5mg (eff. 1/01)
        "9005",     # Reteplase inj, half-kit, 18.8 mg/vial (eff. 1/01)
        "9006",     # Tacrolimus inj, per 5 mg (1 amp) (eff. 1/01)
        "9007",     # Baclofen Intrathecal kit-1amp (eff. 1/01)
        "9008",     # Baclofen Refill Kit--500mcg (eff. 1/01)
        "9009",     # Baclofen Refill Kit--2000mcg (eff. 1/01)
        "9010",     # Baclofen Refill Kit--4000mcg (eff. 1/01)
        "9011",     # Caffeine Citrate, inj, 1ml (eff. 1/01)
        "9012",     # Arsenic Trioxide, 1mg/kg (eff. 4/01)
        "9013",     # Co 57 Cobaltous Cl, 1 ml (eff. 4/01)
        "9100",     # Iodinated I-131 Albumin (eff. 1/01)
        "9102",     # 51 Na chromate, 50mCi (eff. 1/01)
        "9103",     # Na lothalamate I-125, 10uCi (eff. 1/01)
        "9104",     # Anti-thymocyte globin, 25 mg (eff. 1/01)
        "9105",     # Hep B immun glob, per 1 ml (eff. 1/01)
        "9106",     # Sirolimus 1 mg/ml (eff. 1/01)
        "9107",     # Tinzaparin sodium, 2ml vial (eff. 1/01)
        "9108",     # Thyrotropin Alfa, 1.1 mg (eff. 1/01)
        "9109",     # Tirofiban hydrachloride 6.25 mg (eff. 1/01)
        "9217",     # Leuprolide acetate for depot suspension, 7.5 mg (eff. 1/01)
        "9500",     # Platelets, irrad, ea unit (eff. 1/01)
        "9501",     # Platelets, pheresis, ea unit (eff. 1/01)
        "9502",     # Platelets, pher/irrad, ea unit (eff. 1/01)
        "9503",     # Fresh frozen plasma, ea unit (eff. 1/01)
        "9504",     # RBC, deglycerolized, ea unit (eff. 1/01)
        "9505",     # RBC, irradiated, ea unit (eff. 1/01)
        "9998",     # Enoxaparin (eff. 1/01)
    ]