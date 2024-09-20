# Claim Frequency Code (FFS)
# https://resdac.org/cms-data/variables/claim-frequency-code-ffs
def get_codes():
    return [
        "0",      # Non-payment/zero claims
        "1",      # Admit thru discharge claim
        "2",      # Interim — first claim
        "3",      # Interim — continuing claim
        "4",      # Interim — last claim
        "5",      # Late charge(s) only claim
        "7",      # Replacement of prior claim
        "8",      # Void/cancel prior claim
        "9",      # Final claim (for HH PPS = process as a debit/credit to RAP claim)
        "G",      # Common Working File (NCH) generated adjustment claim
        "H",      # CMS generated adjustment claim
        "I",      # Misc adjustment claim (e.g., initiated by intermediary or QIO)
        "J",      # Other adjustment request
        "K",      # OIG Initiated Adjustment Claim
        "M",      # Medicare secondary payer (MSP) adjustment
        "P",      # Adjustment required by QIO
        "Q",      # Claim Submitted for Reconsideration Outside of Timely Limits
    ]