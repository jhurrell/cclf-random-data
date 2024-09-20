# Claim Diagnosis Code I Diagnosis Present on Admission (POA) Indicator Code (FFS)
# https://resdac.org/cms-data/variables/claim-diagnosis-code-i-diagnosis-present-admission-poa-indicator-code-ffs
def get_codes():
    return [
        "Y",    # Diagnosis was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'Y' for the POA Indicator.
        "N",    # Diagnosis was not present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'N' for the POA Indicator.
        "U",    # Documentation is insufficient to determine if the condition was present at the time of inpatient admission. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as 'U' for the POA Indicator.
        "W",    # Clinically undetermined. Provider is unable to clinically determine whether condition was present at the time of inpatient admission. CMS will pay the CC/MCC DRG for those selected HACs that are coded as 'W' for the POA Indicator.
        "1",    # Unreported/not used -- exempt from POA reporting -- This code is equivalent to a blank pn the UB-04, however, it was determined that blanks are undesirable when submitting this data via the 4010A. CMS will not pay the CC/MCC DRG for those selected HACs that are coded as '1' for the POA Indicator. The '1' POA Indicator should not be applied to any codes on the HAC list.
        "Z",    # Denotes the end of the POA indicators (terminated 1/2011).
        "X",    # Denotes the end of the POA indicators in special data processing situations that may be identified by CMS in the future (terminated 1/2011).
    ]