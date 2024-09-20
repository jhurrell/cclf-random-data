# CCLF File Layouts

This set of scripts generates fake files and data to adhere to the
specifications outlined in the CMS Accountable Care Organization – Operational
System (ACO-OS) Claim and Claim Line Feed (CCLF) Information Packet (IP) Version
38.0, dated 02/02/2024

The PDF for this specification can be
[downloaded here](https://www.cms.gov/files/document/cclf-information-packet.pdf).

Each of the file types is generated using a Python script that generates random
data based on the specifications provided in the IP. The scripts are located in
the current directory and can be run from the command line using the following
commands:

```bash
python3 main.py
```

This will generate fake CCLF files for each of the file types listed in the IP.

The generated files are located in the `output` directory and have a filename
that includes the date, time, and type of file. The filenames follow the formats
specified in the requirements.

Each file contains random data based on the specifications provided in the IP.
The scripts use Python's built-in random number generator to generate fake data
for each field in the file. There is no intent to create realistic data, as this
would require a significant amount of time and resources. Instead, the scripts
generate random data that adheres to the specifications provided in the IP.

## Resources

- [Beneficiary Dual Status Code](https://resdac.org/cms-data/variables/edual1-12)
- [Carrier Claim Payment Denial Code](https://resdac.org/cms-data/variables/carrier-claim-payment-denial-code)
- [Claim Diagnosis Code I Diagnosis Present on Admission (POA) Indicator Code (FFS)](https://resdac.org/cms-data/variables/claim-diagnosis-code-i-diagnosis-present-admission-poa-indicator-code-ffs)
- [Claim Frequency Code (FFS)](https://resdac.org/cms-data/variables/claim-frequency-code-ffs)
- [Claim Medicare Non-Payment Reason Code Table](https://resdac.org/sites/datadocumentation.resdac.org/files/Claim%20Medicare%20Non-Payment%20Reason%20Code%20Table.txt)
- [Claim Service Classification Type Code Table](https://resdac.org/cms-data/variables/claim-service-classification-type-code-ffs)
- [Claim Source Inpatient Admission Code (FFS)](https://resdac.org/cms-data/variables/claim-source-inpatient-admission-code-ffs)
- [Line CMS Provider Specialty Code](https://resdac.org/cms-data/variables/line-cms-provider-specialty-code)
- [Line CMS Type Service Code](https://resdac.org/cms-data/variables/line-cms-type-service-code)
- [Line Place Of Service Code (FFS)](https://resdac.org/cms-data/variables/line-place-service-code-ffs)
- [Line Primary Payer Code (if not Medicare)](https://resdac.org/cms-data/variables/line-primary-payer-code-if-not-medicare)
- [Line Processing Indicator Code](https://resdac.org/cms-data/variables/line-processing-indicator-code)
- [Patient Discharge Status Code (FFS)](https://resdac.org/sites/datadocumentation.resdac.org/files/Patient%20Discharge%20Status%20Code%20Table%20%28FFS%29.txt)
- [Revenue Center APC or HIPPS Code](https://resdac.org/cms-data/variables/revenue-center-apc-or-hipps-code)
- [Revenue Center Code (FFS)](https://resdac.org/cms-data/variables/revenue-center-code-ffs)
