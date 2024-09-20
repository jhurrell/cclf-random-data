# Sample CPT Modifiers
# https://www.mdclarity.com/blog/hcpcs-codes#:~:text=HCPCS%20modifiers%20are%20two%20characters,without%20changing%20the%20code%20meanings.
def get_codes():
    return [
        "25",   # The CPT-4 manual defines modifier 25 as a Significant, Separately Identifiable Evaluation and Management Service by the Same Physician on the Same Day of the Procedure or Other Service. Coders can use modifier 25 to indicate that the patient's condition requires a separately and significantly identifiable evaluation and management (E/M) service above and beyond the other service offered.
        "26",   # This modifier is called the professional component or PC. The PC is defined as a physician's service, which may include the interpretation of results, technician supervision, and a written report. Coders add modifier 26 to indicate that the physician only interprets but does not perform the test.
        "59",   # Modifier 59 is called " Distinct Procedural Service." Coders can use modifier 59 to identify procedures performed at different anatomic sites, aren't usually encountered or performed on the same day, and can't be described by one of the more specific anatomic Medicare NCCI procedure to procedure (PTP) modifiers.
        "91",   # Coders use modifier 91 when repeat tests are performed on the same day by the same provider to get reportable test values with individual specimens taken at different times. Coders should not use modifier 91 for testing problems and when a normal one-time result is required.
    ]