# Indicates the type of claim record being processed with respect to payment 
# # (e.g., debit/credit indicator or interim/final indicator).
# (from the PDF)
def get_codes():
    return [
        "0",      # Credit adjustment
        "1",      # Interim bill
        "2",      # HHA benefits exhausted
        "3",      # Final bill
        "4",      # Discharge notice
        "5",      # Debit adjustment
    ]
