# Indicates the diagnostic related group to which a hospital claim belongs for prospective payment purposes.
# (from the PDF)
def get_codes():
    return [
        "522",  # CMS-DRG: Alcohol/drug abuse or dependence w rehabilitation therapy w/o CC
        "523",  # CMS-DRG: Alcohol/drug abuse or dependence w/o rehabilitation therapy w/o CC
        "895",  # MS-DRG Alcohol/drug abuse or dependence w rehabilitation therapy
        "896",  # MS-DRG Alcohol/drug abuse or dependence w/o rehabilitation therapy w MCC
        "897",  # MS-DRG Alcohol/drug abuse or dependence w/o rehabilitation therapy w/o MCC        
   ]